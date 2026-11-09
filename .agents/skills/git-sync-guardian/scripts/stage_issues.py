#!/usr/bin/env python3
"""stage_issues.py: 只把指定編號的問題條目加入 Git 暫存區（wiki/issues.md）。

wiki/issues.md 與日誌一樣由多個 AI 共用，工作目錄常同時含有別的代理尚未提交的狀態變更。
直接 `git add wiki/issues.md` 會把別人的修改一起提交。本腳本以「HEAD 版問題清單＋指定條目的
工作目錄版本」組出要提交的內容，寫入暫存區；工作目錄中的檔案不變，其他條目的修改留給其主人。

條目範圍：從 `### EK-NNN | ...` 標題行起，到下一個 `### ` 或 `## ` 標題行之前為止。
新條目（HEAD 中沒有）插在工作目錄中它前一筆已提交條目之後；若它前面緊接著 HEAD 中沒有的
`## ` 分節標題，該標題一併帶入。

用法（於倉庫任意位置執行）：
    python .agents/skills/git-sync-guardian/scripts/stage_issues.py EK-069 EK-070
    python .agents/skills/git-sync-guardian/scripts/stage_issues.py EK-088 --dry-run

結束代碼：0 成功，1 錯誤（例如指定的編號不存在，或已提交的條目在工作目錄被刪除）。
"""
import argparse
import re
import subprocess
import sys

PATH = 'wiki/issues.md'
ISSUE = re.compile(r'(?m)^### (EK-\d{3,}) ')
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


def norm(s):
    return s.replace('\r\n', '\n').strip()


def main():
    for stream in (sys.stdout, sys.stderr):
        try:  # Windows 主控台預設編碼可能無法輸出中文
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass
    ap = argparse.ArgumentParser(description='只暫存 wiki/issues.md 中指定編號的條目')
    ap.add_argument('ids', nargs='+', help='要提交的問題編號，例如 EK-069')
    ap.add_argument('--dry-run', action='store_true', help='只列出結果，不寫入暫存區')
    a = ap.parse_args()

    root = git('rev-parse', '--show-toplevel').decode().strip()
    base = git('-C', root, 'show', 'HEAD:' + PATH).decode('utf-8')
    # core.autocrlf=true 時工作目錄為 CRLF；暫存內容以 hash-object 寫入，不經換行轉換，故先統一為 LF。
    work = open(f'{root}/{PATH}', 'rb').read().decode('utf-8').replace('\r\n', '\n')
    bb, wb = blocks(base), blocks(work)

    gone = [k for k in bb if k not in wb]
    if gone:
        sys.stderr.write('錯誤：工作目錄刪除了已提交的問題條目（問題清單不得刪除條目）：%s\n' % '、'.join(gone))
        sys.exit(1)
    missing = [k for k in a.ids if k not in wb]
    if missing:
        sys.stderr.write('錯誤：工作目錄中找不到指定的問題編號：%s\n' % '、'.join(missing))
        sys.exit(1)

    staged = base
    wanted = set(a.ids)
    # 先處理既有條目的修改（由後往前替換，位置才不會位移）
    for k in sorted((k for k in wanted if k in bb), key=lambda k: bb[k][0], reverse=True):
        s, e = bb[k]
        ws, we = wb[k]
        staged = staged[:s] + work[ws:we] + staged[e:]
    # 再插入新條目，依工作目錄順序
    order = sorted(wb, key=lambda k: wb[k][0])
    for k in [k for k in order if k in wanted and k not in bb]:
        ws, we = wb[k]
        chunk = work[ws:we]
        # 若前面緊接著 HEAD 中沒有的分節標題，一併帶入
        prev_text = work[:ws]
        heads = list(BOUNDARY.finditer(prev_text))
        if heads:
            h = heads[-1]
            line_end = prev_text.find('\n', h.start())
            heading = prev_text[h.start():line_end if line_end >= 0 else len(prev_text)]
            between = prev_text[h.start():]
            if heading.startswith('## ') and heading not in staged and not ISSUE.search(between):
                chunk = between + chunk
        # 插入位置：工作目錄中前一筆已在暫存內容中的條目之後
        cur = blocks(staged)
        prev = [p for p in order[:order.index(k)] if p in cur]
        pos = cur[prev[-1]][1] if prev else len(staged)
        if pos == len(staged) and not staged.endswith('\n\n'):
            staged += '\n' if staged.endswith('\n') else '\n\n'
            pos = len(staged)
        staged = staged[:pos] + chunk + staged[pos:]

    others = [k for k in wb if k not in wanted and (k not in bb or norm(work[slice(*wb[k])]) != norm(base[slice(*bb[k])]))]
    for k in a.ids:
        print(('暫存（新條目）：' if k not in bb else '暫存：') + k)
    for k in others:
        print('略過（未指定，留在工作目錄）：' + k)
    if a.dry_run:
        print('（dry-run）未寫入暫存區。')
        return
    sha = git('-C', root, 'hash-object', '-w', '--stdin', data=staged.encode('utf-8')).decode().strip()
    git('-C', root, 'update-index', '--add', '--cacheinfo', '100644,%s,%s' % (sha, PATH))
    print('已暫存 %d 筆；工作目錄中的 %s 未變更，其他 %d 筆修改留在工作目錄。' % (len(a.ids), PATH, len(others)))


if __name__ == '__main__':
    main()
