#!/usr/bin/env python3
"""issues_for.py: 列出某一頁的全部問題條目：wiki/issues.md 中尚未結案者、wiki/issues/closed/ 中已結案者，
以及 wiki/todo.md 中與本頁相關之待辦（提到本頁 slug，或「關聯」到本頁問題編號者）。

查核、修正或撰寫卡片前，用本腳本取得「這頁目前有沒有未結問題、過去錯過哪裡、怎麼改的」，
不必讀整份 wiki/issues.md，也不必知道歸檔檔的路徑。

<頁面> 可寫 slug（1982-hopfield-network）、相對於 wiki/ 之路徑（papers/1982-hopfield-network.md）
或倉庫路徑（wiki/papers/1982-hopfield-network.md）。只給 slug 時，同名之論文頁、概念頁、卡片檔、
證據表一併列出。頁面改名時，順著轉介檔（tools/wiki_redirects.py）同時找出新舊名字底下的紀錄。

用法：
    python .agents/skills/wiki-content-audit/scripts/issues_for.py 1982-hopfield-network
    python .agents/skills/wiki-content-audit/scripts/issues_for.py papers/2024-sora-world-simulator.md --open
    python .agents/skills/wiki-content-audit/scripts/issues_for.py 2024-alphafold3 --list

結束代碼：0。
"""
import argparse
import os
import posixpath
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '..', 'git-sync-guardian', 'scripts')))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'tools')))
from stage_issues import blocks, PATH, CLOSED_DIR  # noqa: E402
from wiki_redirects import is_redirect  # noqa: E402

KINDS = ('papers', 'concepts', 'cards', 'evidence')
HEAD_RE = re.compile(r'^### (EK-\d{3,}) \| (\w+) \| ([^|]+?) \|')
MDLINK = re.compile(r'\]\(([^)\s#]+)')


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read().replace('\r\n', '\n')


def redirect_target(root, target):
    """轉介檔指向之 wiki 相對路徑（取第一個指向 .md 之相對連結）。"""
    full = os.path.join(root, 'wiki', target)
    if not os.path.exists(full) or not is_redirect(full):
        return None
    for m in MDLINK.finditer(read(full)):
        p = os.path.normpath(os.path.join(os.path.dirname(full), m.group(1)))
        rel = os.path.relpath(p, os.path.join(root, 'wiki')).replace('\\', '/')
        if rel.endswith('.md') and not rel.startswith('..'):
            return rel
    return None


def targets_for(root, arg):
    arg = arg.replace('\\', '/')
    if arg.startswith('wiki/'):
        arg = arg[5:]
    if '/' in arg:
        base = [arg if arg.endswith('.md') else arg + '.md']
    else:
        slug = arg[:-3] if arg.endswith('.md') else arg
        base = ['%s/%s.md' % (k, slug) for k in KINDS]
    found = set(base)
    # 轉介：舊名 -> 新名
    changed = True
    while changed:
        changed = False
        for t in list(found):
            nt = redirect_target(root, t)
            if nt and nt not in found:
                found.add(nt)
                changed = True
        # 新名 <- 舊名：掃描同一資料夾中指向 found 任一路徑之轉介檔
        for k in KINDS:
            d = os.path.join(root, 'wiki', k)
            if not os.path.isdir(d):
                continue
            for f in os.listdir(d):
                t = '%s/%s' % (k, f)
                if f.endswith('.md') and t not in found and redirect_target(root, t) in found:
                    found.add(t)
                    changed = True
    return sorted(found)


def entries(text):
    out = []
    for iid, (s, e) in sorted(blocks(text).items(), key=lambda kv: int(kv[0][3:])):
        blk = text[s:e].strip('\n')
        m = HEAD_RE.match(blk)
        if m:
            out.append((iid, m.group(2), m.group(3).strip(), blk))
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    ap = argparse.ArgumentParser(description='列出某一頁之未結與已歸檔問題條目')
    ap.add_argument('page', help='slug、papers/<slug>.md 或 wiki/papers/<slug>.md')
    ap.add_argument('--open', action='store_true', help='只列出尚未結案之問題與相關待辦，不列歸檔')
    ap.add_argument('--list', action='store_true', help='只列標題，不印條目內容')
    a = ap.parse_args()

    root = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip() \
        or os.getcwd()
    targets = targets_for(root, a.page)
    print('查詢頁面：' + '、'.join(targets))

    cur = [x for x in entries(read(os.path.join(root, PATH))) if x[2] in targets] \
        if os.path.exists(os.path.join(root, PATH)) else []
    print('\n== wiki/issues.md 中本頁條目：%d 筆（open %d） ==' % (len(cur), sum(1 for x in cur if x[1] == 'open')))
    for iid, st, tg, blk in cur:
        print('\n' + (blk.split('\n', 1)[0] if a.list else blk))

    # 相關待辦：內文提到本頁 slug，或「關聯」到本頁之問題編號
    page_ids = {x[0] for x in cur}
    for t in targets:
        p = os.path.join(root, CLOSED_DIR, t)
        if os.path.exists(p):
            page_ids.update(x[0] for x in entries(read(p)))
    slugs = {posixpath.splitext(posixpath.basename(t))[0] for t in targets}
    todo_path = os.path.join(root, 'wiki', 'todo.md')
    related = []
    if os.path.exists(todo_path):
        tt = read(todo_path)
        heads = list(re.finditer(r'(?m)^### TD-\d{3,} .*$', tt))
        for i, m in enumerate(heads):
            blk = tt[m.start(): heads[i + 1].start() if i + 1 < len(heads) else len(tt)].strip('\n')
            links = set(re.findall(r'EK-\d{3,}', ' '.join(re.findall(r'(?m)^- \*\*關聯\*\*：(.*)$', blk))))
            if links & page_ids or any(re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(sl), blk) for sl in slugs):
                related.append(blk)
    print('\n== wiki/todo.md 中相關待辦：%d 筆 ==' % len(related))
    for blk in related:
        print('\n' + (blk.split('\n', 1)[0] if a.list else blk))
    if a.open:
        return

    print()
    for t in targets:
        p = os.path.join(root, CLOSED_DIR, t)
        if not os.path.exists(p):
            continue
        arch = entries(read(p))
        print('== %s/%s：已結案 %d 筆 ==' % (CLOSED_DIR, t, len(arch)))
        for iid, st, tg, blk in arch:
            print('\n' + (blk.split('\n', 1)[0] if a.list else blk))
        print()
    if not any(os.path.exists(os.path.join(root, CLOSED_DIR, t)) for t in targets):
        print('== 歸檔：本頁沒有已結案紀錄 ==')


if __name__ == '__main__':
    main()
