#!/usr/bin/env python3
"""archive_issues.py: 把 wiki/issues.md 中已結案（fixed / wontfix）的條目搬到 wiki/issues/closed/。

歸檔檔一頁一檔，路徑與條目標題第三段（相對於 wiki/ 之檔案）對應：
    papers/1982-hopfield-network.md 之條目 -> wiki/issues/closed/papers/1982-hopfield-network.md
條目內容原封不動，只把相對連結換算成歸檔檔所在位置，使連結仍指向原處。歸檔檔只追加。

多代理安全（AGENTS.md 第七章第 4 節）：搬移不在修正當下進行，而由本腳本一次完成：
  1. 先 fetch，本機須與 origin/main 一致（不落後、無未推送提交），且暫存區為空。
  2. wiki/issues.md 與 wiki/issues/ 有任何未提交的修改（可能屬於其他代理）即拒絕執行。
  3. 只搬 HEAD 版中已是 fixed / wontfix 的條目。
  4. 寫檔後立即以 safe_commit_push.py（--issue ARCHIVED）提交並推送。

用法（於倉庫任意位置執行）：
    python .agents/skills/wiki-content-audit/scripts/archive_issues.py                 # 預覽
    python .agents/skills/wiki-content-audit/scripts/archive_issues.py --apply --agent "Claude Code by Anthropic"
    python .agents/skills/wiki-content-audit/scripts/archive_issues.py --apply --no-commit   # 只寫檔，由呼叫者自行提交

結束代碼：0 成功（或無可搬條目），1 錯誤。
"""
import argparse
import os
import posixpath
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GUARDIAN = os.path.normpath(os.path.join(HERE, '..', '..', 'git-sync-guardian', 'scripts'))
sys.path.insert(0, GUARDIAN)
from stage_issues import blocks, rebuild, CLOSED_STATES, CLOSED_DIR, PATH  # noqa: E402

HEAD_RE = re.compile(r'^### (EK-\d{3,}) \| (\w+) \| ([^|]+?) \|')
LINK_RE = re.compile(r'\]\(([^)\s]+)((?:\s+"[^"]*")?)\)')


def run(args, cwd, check=True):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.stderr.write(r.stderr)
        sys.exit(1)
    return r


def archive_rel(target):
    return CLOSED_DIR + '/' + target


def rewrite_links(text, archive_path):
    """把相對於 wiki/ 的連結改為相對於歸檔檔所在資料夾。"""
    new_dir = posixpath.dirname(archive_path)

    def sub(m):
        target, title = m.group(1), m.group(2)
        if re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('#') or target.startswith('/'):
            return m.group(0)
        path, sep, frag = target.partition('#')
        if not path:
            return m.group(0)
        full = posixpath.normpath(posixpath.join('wiki', path))
        return '](%s%s%s%s)' % (posixpath.relpath(full, new_dir), sep, frag, title)

    return LINK_RE.sub(sub, text)


def header(target, archive_path):
    d = posixpath.dirname(archive_path)
    page = posixpath.relpath('wiki/' + target, d)
    issues = posixpath.relpath(PATH, d)
    return ('# 已結案問題：%s\n\n'
            '> 本檔收錄 [wiki/%s](%s) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 '
            '[wiki/issues.md](%s) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；'
            '同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。\n'
            % (target, target, page, issues))


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass
    ap = argparse.ArgumentParser(description='把已結案問題條目搬到 wiki/issues/closed/')
    ap.add_argument('--apply', action='store_true', help='實際寫檔（預設只預覽）')
    ap.add_argument('--no-commit', action='store_true', help='與 --apply 併用：只寫檔，不提交（呼叫者須立即自行提交）')
    ap.add_argument('--agent', default='', help='執行代理名稱（--apply 且提交時必填）')
    a = ap.parse_args()
    if a.apply and not a.no_commit and not a.agent:
        ap.error('--apply 會立即提交，須以 --agent 指定執行代理名稱')

    root = run(['git', 'rev-parse', '--show-toplevel'], os.getcwd()).stdout.strip()
    branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], root).stdout.strip()
    if branch != 'main':
        sys.exit('錯誤：目前分支為 %s；歸檔只能在 main 執行（worktree 中不得歸檔）。' % branch)

    # 1. 與遠端一致
    if run(['git', 'fetch', 'origin', 'main'], root, check=False).returncode != 0:
        sys.exit('錯誤：git fetch 失敗，未做任何變更。')
    head = run(['git', 'rev-parse', 'HEAD'], root).stdout.strip()
    remote = run(['git', 'rev-parse', 'origin/main'], root).stdout.strip()
    if head != remote:
        sys.exit('錯誤：本機與 origin/main 不一致（落後或有未推送提交）；先執行 git-sync-guardian 之 sync.py 或推送，再歸檔。')
    if run(['git', 'diff', '--cached', '--name-only'], root).stdout.strip():
        sys.exit('錯誤：暫存區已有檔案（可能屬於他人），未做任何變更。')

    # 2. 問題清單與歸檔資料夾無未提交修改
    dirty = run(['git', 'status', '--porcelain', '--', PATH, 'wiki/issues'], root).stdout.strip()
    if dirty:
        sys.exit('拒絕執行：下列檔案有尚未提交的修改（可能屬於其他代理），請待其提交後再歸檔：\n' + dirty)

    # 3. 只搬 HEAD 版已結案者（工作目錄已確認與 HEAD 相同）
    text = run(['git', 'show', 'HEAD:' + PATH], root).stdout.replace('\r\n', '\n')
    b = blocks(text)
    moves = {}
    for iid, (s, e) in sorted(b.items(), key=lambda kv: int(kv[0][3:])):
        block = text[s:e].strip('\n')
        m = HEAD_RE.match(block)
        if not m:
            sys.exit('錯誤：%s 標題格式不符，請先修正（lint_wiki.py）。' % iid)
        if m.group(2) in CLOSED_STATES:
            moves.setdefault(m.group(3).strip(), []).append((iid, block))
    if not moves:
        print('wiki/issues.md 沒有已結案條目，無需歸檔。')
        return

    n = sum(len(v) for v in moves.values())
    print('將搬移 %d 筆已結案條目至 %d 個歸檔檔：' % (n, len(moves)))
    for target in sorted(moves):
        print('  %s  <-  %s' % (archive_rel(target), '、'.join(i for i, _ in moves[target])))
    if not a.apply:
        print('（預覽）加 --apply 才會寫檔並提交。')
        return

    planned = []  # 先組好全部內容並檢查，再寫檔，避免檢查失敗時留下半套結果
    for target, items in sorted(moves.items()):
        rel = archive_rel(target)
        full = os.path.join(root, rel)
        if os.path.exists(full):
            with open(full, encoding='utf-8') as fh:
                cur = fh.read().replace('\r\n', '\n')
            dup = [i for i, _ in items if re.search(r'(?m)^### %s ' % i, cur)]
            if dup:
                sys.exit('錯誤：%s 已含 %s，未做任何變更，請人工檢查。' % (rel, '、'.join(dup)))
        else:
            cur = header(target, rel)
        body = cur.rstrip('\n') + '\n\n' + '\n\n'.join(rewrite_links(blk, rel) for _, blk in items) + '\n'
        planned.append((rel, full, body))
    written = []
    for rel, full, body in planned:
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(body)
        written.append(rel)
    moved_ids = [i for v in moves.values() for i, _ in v]
    with open(os.path.join(root, PATH), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(rebuild(text, moved_ids))
    print('已寫入 %d 個歸檔檔，並自 wiki/issues.md 移除 %d 筆。' % (len(written), n))

    if a.no_commit:
        print('未提交（--no-commit）。請立即提交：safe_commit_push.py ... --issue ARCHIVED -- wiki/issues.md 及上列歸檔檔。')
        return

    # 4. 立即提交並推送
    ids = sorted(moved_ids, key=lambda i: int(i[3:]))
    msg = 'chore(wiki): archive %d closed issues (%s..%s)' % (n, ids[0], ids[-1])
    cmd = [sys.executable, os.path.join(GUARDIAN, 'safe_commit_push.py'), msg, 'main', '--agent', a.agent,
           '--issue', 'ARCHIVED', '--', PATH] + written
    r = subprocess.run(cmd, cwd=root)
    if r.returncode != 0:
        sys.exit('錯誤：提交失敗；檔案已寫入工作目錄，請依上方訊息處理後重新以 safe_commit_push.py --issue ARCHIVED 提交，'
                 '或以 git checkout -- wiki/issues.md wiki/issues/closed/ 並刪除新增之歸檔檔還原。')


if __name__ == '__main__':
    main()
