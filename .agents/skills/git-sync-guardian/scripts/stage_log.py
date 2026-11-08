#!/usr/bin/env python3
"""stage_log.py: 只把「自己寫的」日誌條目加入 Git 暫存區。

多個 AI 共用同一個工作目錄時，wiki/log.md 常同時含有別的代理尚未提交的條目。
直接 `git add wiki/log.md` 會把別人的條目一起提交。本腳本改以「HEAD 版日誌 + 自己的新條目」
組出要提交的版本，寫入暫存區；工作目錄中的檔案不變，別人的條目留給他們自己提交。

判斷依據：條目中「- **執行代理**：」一行包含指定的代理名稱（不分大小寫）。

用法（於倉庫根目錄或任意子目錄執行）：
    python .agents/skills/git-sync-guardian/scripts/stage_log.py "Claude Code"
    python .agents/skills/git-sync-guardian/scripts/stage_log.py "Codex" --dry-run

結束代碼：0 成功（含沒有可暫存條目），1 錯誤（例如既有條目被改寫，違反 append-only）。
"""
import argparse
import re
import subprocess
import sys

LOG_PATH = 'wiki/log.md'
HEADING = re.compile(r'(?m)^## \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]')
AGENT_LINE = re.compile(r'(?m)^- \*\*執行代理\*\*：(.*)$')


def git(*args, data=None):
    r = subprocess.run(['git', *args], input=data, capture_output=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr.decode('utf-8', 'replace'))
        sys.exit(1)
    return r.stdout


def split(text):
    """回傳 (檔頭, [條目...])；每個條目從標題行開始，到下一個標題前為止（含尾端空行）。"""
    idx = [m.start() for m in HEADING.finditer(text)]
    if not idx:
        return text, []
    return text[:idx[0]], [text[a:b] for a, b in zip(idx, idx[1:] + [len(text)])]


def norm(entry):
    return entry.replace('\r\n', '\n').strip()


def main():
    ap = argparse.ArgumentParser(description='只暫存指定代理寫的 wiki/log.md 條目')
    ap.add_argument('agent', help='執行代理名稱的一部分，例如 "Claude Code"、"Codex"、"Antigravity"')
    ap.add_argument('--heading', action='append', default=[], help='只選取指定的新日誌標題行；可重複指定')
    ap.add_argument('--dry-run', action='store_true', help='只列出結果，不寫入暫存區')
    a = ap.parse_args()

    root = git('rev-parse', '--show-toplevel').decode().strip()
    base_bytes = git('-C', root, 'show', 'HEAD:' + LOG_PATH)
    work_bytes = open(f'{root}/{LOG_PATH}', 'rb').read()
    base = base_bytes.decode('utf-8')
    work = work_bytes.decode('utf-8')

    _, base_entries = split(base)
    _, work_entries = split(work)
    work_keys = [norm(e) for e in work_entries]
    base_keys = {norm(e) for e in base_entries}

    missing = [e for e in base_entries if norm(e) not in set(work_keys)]
    if missing:
        sys.stderr.write('錯誤：工作目錄的日誌改寫或刪除了已提交的條目（違反 append-only），請先處理：\n')
        for e in missing:
            sys.stderr.write('  ' + e.splitlines()[0] + '\n')
        sys.exit(1)

    new_entries = [e for e, k in zip(work_entries, work_keys) if k not in base_keys]
    if a.heading:
        available = {e.splitlines()[0].strip() for e in new_entries if e.splitlines()}
        missing = set(a.heading) - available
        if missing:
            sys.stderr.write('錯誤：找不到指定的新日誌標題：\n')
            for heading in sorted(missing):
                sys.stderr.write('  ' + heading + '\n')
            sys.exit(1)
        selected = set(a.heading)
        new_entries = [e for e in new_entries if e.splitlines() and e.splitlines()[0].strip() in selected]

    mine, others = [], []
    for e in new_entries:
        m = AGENT_LINE.search(e)
        who = m.group(1).strip() if m else '（未標明執行代理）'
        (mine if m and a.agent.lower() in who.lower() else others).append((e, who))

    for e, who in mine:
        print('暫存：' + e.splitlines()[0])
    for e, who in others:
        if a.heading and e.splitlines()[0].strip() in set(a.heading):
            sys.stderr.write('錯誤：指定的日誌標題不屬於代理「' + a.agent + '」：' + e.splitlines()[0] + '\n')
            sys.exit(1)
        print('略過（' + who + '）：' + e.splitlines()[0])
    if not mine:
        print('沒有「' + a.agent + '」的新條目，未變更暫存區。')
        return

    # 暫存版的條目順序一律跟隨工作目錄：已提交條目照 HEAD 原樣保留，自己的新條目放在
    # 它在工作目錄中的位置，他人的條目略過。若暫存順序與工作目錄不同，提交後日誌會一直
    # 顯示為「已修改」，下一個代理很可能把這個順序差異當成自己的修改提交出去。
    # 只有在工作目錄中已提交條目的相對順序被打亂時（理論上不應發生），才退回接在檔尾。
    # 此處只建立 index blob，不改工作目錄。
    base_header, base_entries = split(base)
    base_keys_list = [norm(e) for e in base_entries]
    mine_keys = {norm(e) for e, _ in mine}

    plan, ptr = [], 0
    for entry, key in zip(work_entries, work_keys):
        if ptr < len(base_entries) and key == base_keys_list[ptr]:
            plan.append(('base', base_entries[ptr]))
            ptr += 1
        elif key in mine_keys:
            plan.append(('mine', entry))
    if ptr != len(base_entries):
        sys.stderr.write('警告：工作目錄中已提交條目的順序與 HEAD 不同，新條目改為接在檔尾。\n')
        plan = [('base', e) for e in base_entries] + [('mine', e) for e, k in zip(work_entries, work_keys) if k in mine_keys]

    # 保留 base_header 與每個 base entry 的原始位元組；只正規化新插入條目的行尾。
    # Git 物件通常使用 LF；此處直接寫 index blob，不經過 autocrlf 轉換。
    eol = '\r\n' if base.count('\r\n') * 2 > base.count('\n') else '\n'
    staged = base_header

    def ensure_blank_line(text):
        if not text or text.endswith('\n\n') or text.endswith('\r\n\r\n'):
            return text
        return text + (eol if text.endswith('\n') else eol + eol)

    for kind, entry in plan:
        if kind == 'base':
            staged += entry
            continue
        staged = ensure_blank_line(staged)
        body = entry.replace('\r\n', '\n')
        if not body.endswith('\n'):
            body += '\n'
        if eol == '\r\n':
            body = body.replace('\n', '\r\n')
        staged += body
    if a.dry_run:
        print('（dry-run）共 %d 筆，未寫入暫存區。' % len(mine))
        return
    sha = git('-C', root, 'hash-object', '-w', '--stdin', data=staged.encode('utf-8')).decode().strip()
    git('-C', root, 'update-index', '--add', '--cacheinfo', '100644,%s,%s' % (sha, LOG_PATH))
    print('已暫存 %d 筆；工作目錄中的 %s 未變更，其他代理的 %d 筆條目留在工作目錄。' % (len(mine), LOG_PATH, len(others)))


if __name__ == '__main__':
    main()
