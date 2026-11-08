#!/usr/bin/env python3
"""merge_log.py: 依 append-only 原則自動排解 wiki/log.md 的衝突。

適用於 `git merge` 或 `git stash pop`（含 merge --autostash）在 wiki/log.md 產生衝突時。
做法：以共同祖先（index stage 1）為基礎，保留雙方（stage 2、stage 3）新增的所有條目，
依標題的 [YYYY-MM-DD HH:MM] 時間排序後接在祖先之後，寫回工作目錄的 wiki/log.md。
只會寫檔，不會 git add；暫存與否由呼叫端決定。

若任一方改寫或刪除了祖先中已存在的條目（違反 append-only），本腳本拒絕自動處理並結束代碼 1。

用法：python .agents/skills/git-sync-guardian/scripts/merge_log.py
"""
import re
import subprocess
import sys

LOG_PATH = 'wiki/log.md'
HEADING = re.compile(r'(?m)^## \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]')


def git_show(root, spec):
    r = subprocess.run(['git', '-C', root, 'show', spec], capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def split(text):
    idx = [m.start() for m in HEADING.finditer(text)]
    if not idx:
        return text, []
    return text[:idx[0]], [text[a:b] for a, b in zip(idx, idx[1:] + [len(text)])]


def norm(entry):
    return entry.replace('\r\n', '\n').strip()


def main():
    root = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True).stdout.decode().strip()
    base, ours, theirs = (git_show(root, ':%d:%s' % (n, LOG_PATH)) for n in (1, 2, 3))
    if ours is None or theirs is None:
        sys.stderr.write('錯誤：%s 目前不在衝突狀態（找不到 stage 2/3）。\n' % LOG_PATH)
        sys.exit(1)
    base = base or ''
    _, base_entries = split(base)
    head, ours_entries = split(ours)
    _, theirs_entries = split(theirs)
    base_keys = {norm(e) for e in base_entries}
    for side, entries in (('ours', ours_entries), ('theirs', theirs_entries)):
        keys = {norm(e) for e in entries}
        lost = [e for e in base_entries if norm(e) not in keys]
        if lost:
            sys.stderr.write('錯誤：%s 一側改寫或刪除了既有條目（違反 append-only），請人工處理：\n' % side)
            for e in lost:
                sys.stderr.write('  ' + e.splitlines()[0] + '\n')
            sys.exit(1)
    # ours（merge 時為本機、stash 還原時為已提交的 HEAD）的順序一律不動；
    # theirs 獨有的新條目，依時間插入 ours 與 base 共同前綴之後的適當位置。
    prefix = 0
    while prefix < min(len(ours_entries), len(base_entries)) and norm(ours_entries[prefix]) == norm(base_entries[prefix]):
        prefix += 1
    result = list(ours_entries)
    ours_keys = {norm(e) for e in ours_entries}
    added = []
    for e in theirs_entries:
        k = norm(e)
        if k in base_keys or k in ours_keys:
            continue
        ts = HEADING.match(e).group(1)
        i = len(result)
        while i > prefix and HEADING.match(result[i - 1]).group(1) > ts:
            i -= 1
        result.insert(i, e)
        ours_keys.add(k)
        added.append(e)
    eol = '\r\n' if ours.count('\r\n') * 2 >= ours.count('\n') else '\n'
    added_ids = {id(e) for e in added}
    out = head
    for e in result:
        if id(e) in added_ids:
            if not out.endswith(eol + eol):
                out = out.rstrip('\r\n') + eol + eol
            out += e.rstrip('\r\n') + eol + eol
        else:
            out += e  # ours 的條目逐字保留，避免工作目錄與 HEAD 出現多餘差異
    out = out.rstrip('\r\n') + eol
    with open('%s/%s' % (root, LOG_PATH), 'wb') as f:
        f.write(out.encode('utf-8'))
    for e in added:
        print('併入：' + e.splitlines()[0])
    print('已依時間併入 %d 筆對方條目到 %s（尚未 git add）。' % (len(added), LOG_PATH))


if __name__ == '__main__':
    main()
