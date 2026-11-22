#!/usr/bin/env python3
"""stage_issues.py: 只把指定編號的問題條目加入 Git 暫存區（wiki/issues.md）。

wiki/issues.md 與日誌一樣由多個 AI 共用，工作目錄常同時含有別的代理尚未提交的狀態變更。
直接 `git add wiki/issues.md` 會把別人的修改一起提交。本腳本以「HEAD 版問題清單＋指定條目的
工作目錄版本」組出要提交的內容，寫入暫存區；工作目錄中的檔案不變，其他條目的修改留給其主人。

條目範圍：從 `### EK-NNN | ...` 標題行起，到下一個 `### ` 或 `## ` 標題行之前為止。
問題清單不分節（AGENTS.md 第七章第 4 節）；新條目（HEAD 中沒有）插在工作目錄中它前一筆已提交
條目之後。

已結案條目由 wiki-content-audit 之 archive_issues.py 搬到 wiki/issues/closed/。搬移提交以特殊
編號 ARCHIVED 暫存：只從 HEAD 版刪去「已結案、且已出現在歸檔檔中」之條目，其他代理之修改仍留在
工作目錄。ARCHIVED 只能與 PREAMBLE 併用。

用法（於倉庫任意位置執行）：
    python .agents/skills/git-sync-guardian/scripts/stage_issues.py EK-069 EK-070
    python .agents/skills/git-sync-guardian/scripts/stage_issues.py EK-088 --dry-run
    python .agents/skills/git-sync-guardian/scripts/stage_issues.py --next-id
    python .agents/skills/git-sync-guardian/scripts/stage_issues.py ARCHIVED

結束代碼：0 成功，1 錯誤（例如指定的編號不存在，或已提交的條目在工作目錄被刪除）。
"""
import argparse
import os
import re
import subprocess
import sys

PATH = 'wiki/issues.md'
CLOSED_DIR = 'wiki/issues/closed'
CLOSED_STATES = {'fixed', 'wontfix'}
ISSUE = re.compile(r'(?m)^### (EK-\d{3,}) ')
HEAD_LINE = re.compile(r'(?m)^### (EK-\d{3,}) \| (\w+) \| ')
BOUNDARY = re.compile(r'(?m)^##+ ')


def git(*args, data=None):
    r = subprocess.run(['git', *args], input=data, capture_output=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr.decode('utf-8', 'replace'))
        sys.exit(1)
    return r.stdout


def blocks(text):
    """回傳 {編號: (起點, 終點)}，終點為下一個 ## 或 ### 標題行之前。"""
    out = {}
    for m in ISSUE.finditer(text):
        nxt = BOUNDARY.search(text, m.end())
        out[m.group(1)] = (m.start(), nxt.start() if nxt else len(text))
    return out


def states(text):
    return {m.group(1): m.group(2) for m in HEAD_LINE.finditer(text)}


def preamble_end(text):
    m = BOUNDARY.search(text)
    return m.start() if m else len(text)


def rebuild(text, drop=()):
    """檔頭＋未刪去之條目（依原順序），不保留任何 ## 分節標題；結尾單一換行。"""
    drop = set(drop)
    head = text[:preamble_end(text)].rstrip('\n')
    b = blocks(text)
    kept = [text[s:e].strip('\n') for k, (s, e) in sorted(b.items(), key=lambda kv: kv[1][0]) if k not in drop]
    return head + '\n\n' + '\n\n'.join(kept) + '\n' if kept else head + '\n'


def norm(s):
    return s.replace('\r\n', '\n').strip()


def closed_ids(root):
    """歸檔資料夾（工作目錄版）中出現之編號。"""
    out = set()
    base = os.path.join(root, CLOSED_DIR)
    for dirpath, _, files in os.walk(base):
        for f in files:
            if f.endswith('.md'):
                with open(os.path.join(dirpath, f), encoding='utf-8') as fh:
                    out.update(ISSUE.findall(fh.read()))
    return out


def next_id(root):
    nums = []
    for p in [os.path.join(root, PATH)]:
        if os.path.exists(p):
            with open(p, encoding='utf-8') as fh:
                nums += [int(x[3:]) for x in ISSUE.findall(fh.read())]
    nums += [int(x[3:]) for x in closed_ids(root)]
    return 'EK-%03d' % (max(nums) + 1 if nums else 1)


def main():
    for stream in (sys.stdout, sys.stderr):
        try:  # Windows 主控台預設編碼可能無法輸出中文
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass
    ap = argparse.ArgumentParser(description='只暫存 wiki/issues.md 中指定編號的條目')
    ap.add_argument('ids', nargs='*', help='要提交的問題編號（例如 EK-069）；PREAMBLE 代表檔頭前言；ARCHIVED 代表歸檔搬移')
    ap.add_argument('--dry-run', action='store_true', help='只列出結果，不寫入暫存區')
    ap.add_argument('--next-id', action='store_true', help='印出下一個可用編號（同時掃描 issues.md 與歸檔資料夾）')
    a = ap.parse_args()

    root = git('rev-parse', '--show-toplevel').decode().strip()
    if a.next_id:
        print(next_id(root))
        return
    if not a.ids:
        ap.error('須指定編號、PREAMBLE、ARCHIVED，或使用 --next-id')

    base = git('-C', root, 'show', 'HEAD:' + PATH).decode('utf-8').replace('\r\n', '\n')
    # core.autocrlf=true 時工作目錄為 CRLF；暫存內容以 hash-object 寫入，不經換行轉換，故先統一為 LF。
    work = open(f'{root}/{PATH}', 'rb').read().decode('utf-8').replace('\r\n', '\n')
    bb, wb = blocks(base), blocks(work)

    want_preamble = 'PREAMBLE' in a.ids
    archived = 'ARCHIVED' in a.ids
    raw_ids = [k for k in a.ids if k not in ('PREAMBLE', 'ARCHIVED')]
    gone = [k for k in bb if k not in wb]

    if archived:
        if raw_ids:
            sys.stderr.write('錯誤：ARCHIVED 只能與 PREAMBLE 併用，其他條目請另行提交：%s\n' % '、'.join(raw_ids))
            sys.exit(1)
        if not gone:
            sys.stderr.write('錯誤：ARCHIVED 模式下工作目錄沒有被搬走的條目。\n')
            sys.exit(1)
        st = states(base)
        not_closed = [k for k in gone if st.get(k) not in CLOSED_STATES]
        if not_closed:
            sys.stderr.write('錯誤：以下條目在 HEAD 中不是 fixed / wontfix，不得歸檔：%s\n' % '、'.join(not_closed))
            sys.exit(1)
        have = closed_ids(root)
        missing = [k for k in gone if k not in have]
        if missing:
            sys.stderr.write('錯誤：以下條目已自 wiki/issues.md 移除，卻不在 wiki/issues/closed/ 中：%s\n' % '、'.join(missing))
            sys.exit(1)
        staged = rebuild(base, gone)
        print('暫存：歸檔搬移 %d 筆（%s 至 %s）' % (len(gone), gone[0], gone[-1]))
    else:
        if gone:
            shown = '、'.join(gone[:10]) + ('等 %d 筆' % len(gone) if len(gone) > 10 else '')
            sys.stderr.write('錯誤：工作目錄刪除了已提交的問題條目（問題清單不得刪除條目；歸檔請用 archive_issues.py）：%s\n'
                             '若有人正在執行 archive_issues.py，等它提交完成（通常數秒）後重試。\n' % shown)
            sys.exit(1)
        missing = [k for k in raw_ids if k not in wb]
        if missing:
            sys.stderr.write('錯誤：工作目錄中找不到指定的問題編號：%s\n' % '、'.join(missing))
            sys.exit(1)
        staged = base
        wanted = set(raw_ids)
        # 先處理既有條目的修改（由後往前替換，位置才不會位移）
        for k in sorted((k for k in wanted if k in bb), key=lambda k: bb[k][0], reverse=True):
            s, e = bb[k]
            ws, we = wb[k]
            staged = staged[:s] + work[ws:we] + staged[e:]
        # 再插入新條目，依工作目錄順序；插在工作目錄中前一筆已在暫存內容中的條目之後
        order = sorted(wb, key=lambda k: wb[k][0])
        for k in [k for k in order if k in wanted and k not in bb]:
            ws, we = wb[k]
            chunk = work[ws:we]
            cur = blocks(staged)
            prev = [p for p in order[:order.index(k)] if p in cur]
            pos = cur[prev[-1]][1] if prev else len(staged)
            if pos == len(staged) and not staged.endswith('\n\n'):
                staged += '\n' if staged.endswith('\n') else '\n\n'
                pos = len(staged)
            staged = staged[:pos] + chunk + staged[pos:]
        for k in raw_ids:
            print(('暫存（新條目）：' if k not in bb else '暫存：') + k)

    if want_preamble:
        staged = work[:preamble_end(work)] + staged[preamble_end(staged):]
        print('暫存：檔頭說明（PREAMBLE）')

    wanted = set(raw_ids)
    others = [k for k in wb if k not in wanted and (k not in bb or norm(work[slice(*wb[k])]) != norm(base[slice(*bb[k])]))]
    for k in others:
        print('略過（未指定，留在工作目錄）：' + k)
    if a.dry_run:
        print('（dry-run）未寫入暫存區。')
        return
    sha = git('-C', root, 'hash-object', '-w', '--stdin', data=staged.encode('utf-8')).decode().strip()
    git('-C', root, 'update-index', '--add', '--cacheinfo', '100644,%s,%s' % (sha, PATH))
    print('已暫存；工作目錄中的 %s 未變更，其他 %d 筆修改留在工作目錄。' % (PATH, len(others)))


if __name__ == '__main__':
    main()
