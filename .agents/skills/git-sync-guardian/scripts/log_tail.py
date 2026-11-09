#!/usr/bin/env python3
"""log_tail.py: 依條目輸出 wiki/log.md 最後幾筆，供接手時掌握脈絡，免去整份讀取日誌。

日誌只寫不讀（AGENTS.md 第六章第 4 節）：接手時不得整份讀取 wiki/log.md。本腳本以 UTF-8 讀檔、
依 `## [` 標題切分條目，不會像以行數截尾（tail -n、Get-Content -Tail）那樣切在條目中間；
Windows PowerShell 5.1 的 Get-Content 未加 -Encoding UTF8 時，會以系統碼頁誤讀本庫的
UTF-8（無 BOM）檔案而顯示亂碼。跨平台（macOS、Linux、Windows）結果一致。

用法（於倉庫任意位置執行）：
    python .agents/skills/git-sync-guardian/scripts/log_tail.py              # 最後 3 筆
    python .agents/skills/git-sync-guardian/scripts/log_tail.py -n 5         # 最後 5 筆
    python .agents/skills/git-sync-guardian/scripts/log_tail.py --headings -n 20   # 只列最後 20 筆標題
    python .agents/skills/git-sync-guardian/scripts/log_tail.py --grep card_line   # 含關鍵字的最後 3 筆
    python .agents/skills/git-sync-guardian/scripts/log_tail.py --grep TD-004 -n 0 # 含關鍵字的全部條目

--grep 不分大小寫比對整筆條目（含標題）；-n 0 表示不限筆數。
"""
import argparse
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
LOG = os.path.join(ROOT, 'wiki', 'log.md')
HEADING = re.compile(r'(?m)^## \[')


def entries(text):
    idx = [m.start() for m in HEADING.finditer(text)]
    return [text[s:e].rstrip() for s, e in zip(idx, idx[1:] + [len(text)])]


def main():
    try:  # Windows 主控台預設編碼可能無法輸出中文
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    ap = argparse.ArgumentParser(description='依條目輸出 wiki/log.md 最後幾筆')
    ap.add_argument('-n', type=int, default=3, help='筆數，預設 3；0 表示不限')
    ap.add_argument('--headings', action='store_true', help='只輸出標題行')
    ap.add_argument('--grep', help='只保留含此關鍵字的條目（不分大小寫）')
    a = ap.parse_args()

    with open(LOG, 'rb') as f:
        items = entries(f.read().decode('utf-8').replace('\r\n', '\n'))
    total = len(items)
    if a.grep:
        key = a.grep.lower()
        items = [e for e in items if key in e.lower()]
    shown = items if a.n <= 0 else items[-a.n:]
    if a.headings:
        print('\n'.join(e.split('\n', 1)[0] for e in shown))
    else:
        print('\n\n'.join(shown))
    note = '含「%s」者 %d 筆，' % (a.grep, len(items)) if a.grep else ''
    print('\n--- wiki/log.md 共 %d 筆，%s顯示 %d 筆' % (total, note, len(shown)))


if __name__ == '__main__':
    main()
