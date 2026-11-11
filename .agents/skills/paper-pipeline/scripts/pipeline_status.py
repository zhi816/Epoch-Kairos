"""論文收錄總流程（paper-pipeline）之進度檢查。

用法（於倉庫根目錄執行，Python 3.7 以上，只用標準函式庫）：
    python .agents/skills/paper-pipeline/scripts/pipeline_status.py             # 全庫：每篇論文各步驟狀態與下一步
    python .agents/skills/paper-pipeline/scripts/pipeline_status.py --new       # 只列 raw/ 中尚未有論文頁之原始檔
    python .agents/skills/paper-pipeline/scripts/pipeline_status.py <slug> ...  # 指定論文：逐步列出每項檢查與原因
    （論文頁尚未建立而證據表已存在時，只檢查 S3 之證據表部分，供 S3 完成時確認）

步驟代號與 SKILL.md 第四節相同：
    S1 收件      論文頁「原始檔典藏」所指之 raw/ 檔案存在
    S3 證據表    wiki/evidence/<slug>.md 存在；數值逐一寫出；區塊公式按序號逐條登記
    S4 論文頁    論文頁存在、結構完整（開頭引言、Card 1 至 6、知識網絡）、lint_wiki.py 對本頁無 ERROR（概念頁相關之 ERROR 歸 S5）、card_line 切得成封面斷行
    S5 概念索引  concepts 非空且概念頁雙向列出本篇；wiki/index.md 有本篇連結；lint_wiki.py 對本頁無概念頁相關之 ERROR
    S6 核實      verification 為 partial 或 verified；wiki/issues.md 無本頁 open 問題
    S7 卡片      wiki/cards/<slug>.md 存在且 check_cards.py 對本篇無 ERROR
    S8 網頁      web/papers/<slug>/index.html 存在，且不舊於卡片檔與論文頁；Card 1 編號與首頁卡片牆相同；論文頁 status 為 published
    S9 上架      卡片檔已提交；web/index.html 之星圖（或我的星系）與卡片牆都有本篇；首頁與資料一致
    S10 提交     本篇之論文頁、證據表、卡片檔、網頁皆無未提交之修改，且 wiki/log.md 有本篇之日誌
本腳本只檢查「做了沒有」與可機械判斷之形式，不判斷內容是否忠於原文（那是 wiki-content-audit 之人工核對）。
退出碼：指定 slug 時，任一步驟未完成即為 1；全庫與 --new 模式恆為 0。
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
WIKI = os.path.join(ROOT, 'wiki')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from wiki_redirects import is_redirect  # noqa: E402
RAW = os.path.join(ROOT, 'raw')
LINT = os.path.join(ROOT, '.agents', 'skills', 'wiki-content-audit', 'scripts', 'lint_wiki.py')
CHECK_CARDS = os.path.join(ROOT, '.agents', 'skills', 'paper-card-writer', 'scripts', 'check_cards.py')
BUILD_HOME = os.path.join(ROOT, 'tools', 'build_home.py')
STEPS = ['S1', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
NEXT = {
    'S1': 'S1 收件：依 references/intake.md 確認原始檔與檔名，論文頁「原始檔典藏」寫對路徑',
    'S3': 'S3 證據表：依 wiki-content-audit 寫作模式第 2 步建立或補齊 wiki/evidence/<slug>.md',
    'S4': 'S4 論文頁：依 references/paper-page-template.md 撰寫或修正論文頁，lint_wiki.py 本頁 ERROR 0',
    'S5': 'S5 概念與索引：依 references/concepts-and-index.md 更新概念頁雙向連結與 wiki/index.md',
    'S6': 'S6 核實：依 wiki-content-audit 第 4、5 步修正 open 問題、設定 verification',
    'S7': 'S7 卡片：依 paper-card-writer 第五節第 1 至 6 步撰寫卡片檔，check_cards.py ERROR 0',
    'S8': 'S8 網頁：python tools/build_paper_prototype.py <slug>，再以 verify_page.js 驗證',
    'S9': 'S9 上架：依 references/publish.md 以 build_home.py --card <slug> 上架並以 verify_wall.js、verify_star.js 驗證',
    'S10': 'S10 提交：寫日誌並以 safe_commit_push.py 一次提交本篇所有檔案（references/publish.md 第五節）',
}


def say(s=''):
    sys.stdout.write(s + '\n')


def run(args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONWARNINGS='ignore')
    p = subprocess.run(args, cwd=ROOT, capture_output=True, env=env)
    return p.returncode, p.stdout.decode('utf-8', 'replace') + p.stderr.decode('utf-8', 'replace')


def git(*args):
    return run(['git'] + list(args))


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


LINTMOD = load_module('lint_wiki', LINT)


def frontmatter(text):
    fm, where, _ = LINTMOD.frontmatter(text)
    return fm or {}


def tool_findings(output):
    """把 lint_wiki.py 或 check_cards.py 的輸出整理成 {相對路徑: [(等級, 訊息), ...]}。"""
    out = {}
    for line in output.splitlines():
        m = re.match(r'^(ERROR|WARN)\s+(\S+?):(\d+)\s+(.*)$', line)
        if m:
            out.setdefault(m.group(2).replace('\\', '/'), []).append((m.group(1), m.group(4).strip()))
    return out


CARD_NO = r'((?:No|F)\.\d+)'
# lint_wiki.py 中屬於概念頁連結之 ERROR：論文頁先填 concepts（S4），概念頁到 S5 才建立或反向登記，故歸 S5 判斷
CONCEPT_LINT = ('concepts 指向不存在的概念頁', '雙向對應缺漏', '相對連結指向不存在的檔案：../concepts/')


def homepage_data():
    """回傳（星圖論文、我的星系論文、卡片牆論文、卡片牆編號 {slug: 'No.04'}）。"""
    path = os.path.join(ROOT, 'web', 'index.html')
    if not os.path.exists(path):
        return set(), set(), set(), {}
    t = read(path)
    m = re.search(r'<script[^>]*id="ek-data"[^>]*>(.*?)</script>', t, re.S)
    stars, focus = set(), set()
    if m:
        d = json.loads(m.group(1))
        stars = {p['slug'] for p in d.get('papers', [])}
        focus = {p['slug'] for p in (d.get('focus') or {}).get('papers', [])}
    wall = set(re.findall(r'<a class="wc[^"]*"[^>]*\sdata-slug="([^"]+)"', t))
    numbers = dict(re.findall(r'<a class="wc[^"]*"[^>]*\sdata-slug="([^"]+)"[^>]*>(?:<[^>]+>){0,4}' + CARD_NO + '<', t))
    return stars, focus, wall, numbers


def proto_number(path):
    """論文頁原型 Card 1 左上之編號（No.04、F.23）；找不到時回傳 None。"""
    m = re.search('>' + CARD_NO + '<', read(path))
    return m.group(1) if m else None


def raw_cited(text):
    m = re.search(r'原始檔典藏[^`]*`(raw/[^`]+)`', text)
    return m.group(1) if m else None


def numless_rows(ev_text):
    rows, claim_col = [], None
    for line in ev_text.split('\n'):
        s = line.strip()
        if not s.startswith('|'):
            claim_col = None
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        if claim_col is None:
            claim_col = next((i for i, c in enumerate(cells) if '主張' in c), None)
            continue
        if set(s) <= set('|-: ') or claim_col >= len(cells):
            continue
        claim = cells[claim_col]
        if LINTMOD.NUMLESS_CLAIM.search(claim) and not re.search(r'\d', LINTMOD.TABLE_REF.sub('', claim)):
            rows.append(claim[:24])
    return rows


def formula_rows(ev_text):
    """讀取位置欄的「區塊公式 N」編號；回傳有效編號與格式問題。

    N 是論文頁所有區塊公式由上而下的 1-based 序號。一式一列。
    缺少主張或來源的列、同一列有多個編號的列，不能計為已登記。
    """
    rows, problems = {}, []
    columns = None
    for line in ev_text.splitlines():
        line = line.strip()
        if not line.startswith('|'):
            columns = None
            continue
        # \| 是表格儲存格內的直線，而非欄分隔符。
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line.strip('|'))]
        # 兼容現行五欄表及早期四欄表；欄名不同不代表已登記的公式失效。
        position = next((i for i, c in enumerate(cells) if c in ('位置', '頁面章節')), None)
        claim = next((i for i, c in enumerate(cells) if '主張' in c), None)
        source = next((i for i, c in enumerate(cells) if '來源' in c), None)
        if position is not None and claim is not None and source is not None:
            columns = (position, claim, source)
            continue
        if columns is None:
            continue
        pos, claim, source = columns
        if pos >= len(cells):
            continue
        ids = re.findall(r'區塊公式\s*([1-9]\d*)(?!\d)', cells[pos])
        if not ids:
            continue
        if len(ids) != 1:
            problems.append('同一證據列含多個區塊公式編號')
            continue
        number = int(ids[0])
        if (claim >= len(cells) or not cells[claim] or cells[claim] in ('-', '—')
                or source is None or source >= len(cells) or not cells[source]
                or cells[source] in ('-', '—')):
            problems.append('區塊公式 %d 缺主張或第一手來源欄' % number)
            continue
        rows[number] = rows.get(number, 0) + 1
    for number, count in sorted(rows.items()):
        if count > 1:
            problems.append('區塊公式 %d 重複登記 %d 列' % (number, count))
    return {n for n, count in rows.items() if count == 1}, problems


def block_formulas(page_text):
    body = re.sub(r'```.*?```', '', page_text, flags=re.S)
    return len(re.findall(r'(?<![\\$])\$\$(?!\$)(.+?)(?<![\\$])\$\$(?!\$)', body, flags=re.S))


def open_issues():
    path = os.path.join(WIKI, 'issues.md')
    res = {}
    if os.path.exists(path):
        for m in re.finditer(r'(?m)^### (EK-\d+) \| (\w+) \| (\S+) \|', read(path)):
            if m.group(2) == 'open':
                res.setdefault(m.group(3), []).append(m.group(1))
    return res


def dirty(paths):
    if not paths:
        return []
    code, out = git('status', '--porcelain', '--', *paths)
    return [line[3:] for line in out.splitlines() if line.strip()]


def tracked(path):
    code, _ = git('ls-files', '--error-unmatch', '--', path)
    return code == 0


def collect():
    papers_dir = os.path.join(WIKI, 'papers')
    papers = sorted(f[:-3] for f in os.listdir(papers_dir)
                    if f.endswith('.md') and not is_redirect(os.path.join(papers_dir, f)))
    _, lint_out = run([sys.executable, LINT])
    _, cards_out = run([sys.executable, CHECK_CARDS])
    hc, home_out = run([sys.executable, BUILD_HOME, '--check'])
    ctx = {
        'papers': papers,
        'lint': tool_findings(lint_out),
        'cards': tool_findings(cards_out),
        'home_ok': hc == 0,
        'home_msg': (home_out.strip().splitlines() or [''])[-1],
        'home': homepage_data(),
        'open': open_issues(),
        'index': read(os.path.join(WIKI, 'index.md')),
        'log': read(os.path.join(WIKI, 'log.md')),
        'concepts': {},
    }
    cdir = os.path.join(WIKI, 'concepts')
    for f in os.listdir(cdir):
        if f.endswith('.md'):
            ctx['concepts'][f[:-3]] = frontmatter(read(os.path.join(cdir, f)))
    return ctx


def completion_status(results):
    """九步皆 OK 才算完成；未完成依 NG、無法判斷、WARN 順序提示。"""
    for kind in ('NG', '--', 'WARN'):
        for step in STEPS:
            if results[step][0] == kind:
                return kind, step
    return 'OK', None


def check_evidence(slug, page=None):
    """S3：證據表存在、數值逐一寫出；論文頁已建立時比對各區塊公式之登記編號。"""
    ev_rel = 'wiki/evidence/%s.md' % slug
    ev_path = os.path.join(ROOT, ev_rel)
    if not os.path.exists(ev_path):
        return ('NG', ['缺少 ' + ev_rel])
    ev = read(ev_path)
    why = []
    nl = numless_rows(ev)
    if nl:
        why.append('證據表有未寫出數值之列：' + '、'.join(nl))
    formula_ids, problems = formula_rows(ev)
    why.extend(problems)
    if page is None:
        note = '證據表存在；公式編號 %d 個（論文頁尚未建立，於 S4 後檢查對應）' % len(formula_ids)
        return ('WARN', why) if why else ('OK', [note])
    nb = block_formulas(page)
    expected = set(range(1, nb + 1))
    missing = sorted(expected - formula_ids)
    extra = sorted(formula_ids - expected)
    if missing:
        why.append('論文頁有 %d 條區塊公式，證據表缺編號：%s' % (nb, '、'.join(map(str, missing))))
    if extra:
        why.append('證據表有超出論文頁範圍的公式編號：' + '、'.join(map(str, extra)))
    return ('WARN', why) if why else ('OK', ['證據表存在；區塊公式 %d 條，已逐條登記（仍須人工核對原文）' % nb])


def check(slug, ctx):
    """回傳 {步驟: (狀態, [原因, ...])}；狀態為 OK、NG、WARN 或 --（無法判斷）。"""
    r = {}
    page_rel = 'wiki/papers/%s.md' % slug
    ev_rel = 'wiki/evidence/%s.md' % slug
    card_rel = 'wiki/cards/%s.md' % slug
    proto_rel = 'web/papers/%s/index.html' % slug
    page_path = os.path.join(ROOT, page_rel)
    page = read(page_path)
    fm = frontmatter(page)

    # S1 收件
    cited = raw_cited(page)
    if not cited:
        r['S1'] = ('NG', ['論文頁「知識網絡與文獻出處」沒有「原始檔典藏：`raw/...`」一行'])
    elif not os.path.isdir(RAW):
        r['S1'] = ('--', ['本機沒有 raw/（未 clone Mine-RAW），無法確認原始檔'])
    elif not os.path.exists(os.path.join(ROOT, cited)):
        r['S1'] = ('NG', ['原始檔典藏所指之檔案不存在：' + cited])
    else:
        r['S1'] = ('OK', ['原始檔：' + cited])

    # S3 證據表
    r['S3'] = check_evidence(slug, page)

    # S4 論文頁
    why = []
    if not re.search(r'(?m)^> 「', page):
        why.append('標題下缺開頭引言（> 「……」）')
    for n in range(1, 7):
        if not re.search(r'(?m)^## Card %d ｜' % n, page):
            why.append('缺「## Card %d ｜」段落' % n)
    if '## 知識網絡與文獻出處' not in page:
        why.append('缺「## 知識網絡與文獻出處」')
    holes = re.findall(r'<(?:[一-鿿][^<>\n]{0,30}|slug|DOI|URL)>', page)
    if holes:
        why.append('有未替換之骨架佔位符：' + '、'.join(sorted(set(holes))[:5]))
    errs = [m for lv, m in ctx['lint'].get(page_rel, []) if lv == 'ERROR']
    concept_errs = [m for m in errs if m.startswith(CONCEPT_LINT)]
    why += ['lint ERROR：' + m for m in errs if m not in concept_errs]
    warn = [m for lv, m in ctx['lint'].get(page_rel, []) if lv == 'WARN' and '封面斷行' in m]
    if why:
        r['S4'] = ('NG', why)
    elif warn:
        r['S4'] = ('WARN', ['lint WARN：' + m for m in warn])
    else:
        r['S4'] = ('OK', ['結構完整，lint 本頁無 ERROR'])

    # S5 概念與索引
    why = []
    concepts = fm.get('concepts') or []
    if not concepts:
        why.append('Frontmatter 之 concepts 為空')
    for c in concepts:
        cfm = ctx['concepts'].get(c)
        if cfm is None:
            why.append('概念頁不存在：wiki/concepts/%s.md' % c)
        elif slug not in (cfm.get('papers') or []):
            why.append('概念頁 %s 之 papers 未列本篇' % c)
    for c, cfm in ctx['concepts'].items():
        if slug in (cfm.get('papers') or []) and c not in concepts:
            why.append('概念頁 %s 列了本篇，但論文頁 concepts 沒有列它' % c)
    if '(papers/%s.md)' % slug not in ctx['index']:
        why.append('wiki/index.md 沒有本篇連結（papers/%s.md）' % slug)
    # concepts 欄與雙向對應已由上方逐項檢查；正文中指向不存在之概念頁連結只有 lint 抓得到
    why += ['lint ERROR：' + m for m in concept_errs if m.startswith(CONCEPT_LINT[2])]
    r['S5'] = ('NG', why) if why else ('OK', ['概念：' + '、'.join(concepts) + '；index.md 已登記'])

    # S6 核實
    v = fm.get('verification')
    ops = ctx['open'].get('papers/%s.md' % slug, [])
    if ops:
        r['S6'] = ('NG', ['wiki/issues.md 有 open 問題：' + '、'.join(ops)])
    elif v in ('verified', 'partial'):
        r['S6'] = ('OK', ['verification：' + v])
    else:
        r['S6'] = ('NG', ['verification 為 %s，須依 wiki-content-audit 完成核對' % v])

    # S7 卡片
    card_path = os.path.join(ROOT, card_rel)
    if not os.path.exists(card_path):
        r['S7'] = ('NG', ['缺少 ' + card_rel])
    else:
        errs = [m for lv, m in ctx['cards'].get(card_rel, []) if lv == 'ERROR']
        warns = [m for lv, m in ctx['cards'].get(card_rel, []) if lv == 'WARN']
        if errs:
            r['S7'] = ('NG', ['check_cards ERROR：' + m for m in errs])
        elif warns:
            r['S7'] = ('WARN', ['check_cards WARN（須逐條交代）：' + m for m in warns])
        else:
            r['S7'] = ('OK', ['check_cards 無 ERROR、無 WARN'])

    # S8 網頁
    stars, focus, wall, numbers = ctx['home']
    proto_path = os.path.join(ROOT, proto_rel)
    if not os.path.exists(proto_path):
        r['S8'] = ('NG', ['缺少 ' + proto_rel])
    else:
        why = []
        newer = [p for p in (card_path, page_path) if os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(proto_path) + 1]
        if newer:
            why.append('網頁舊於 ' + '、'.join(os.path.relpath(p, ROOT).replace('\\', '/') for p in newer) + '，須重建')
        pn, hn = proto_number(proto_path), numbers.get(slug)
        if pn and hn and pn != hn:
            why.append('網頁 Card 1 編號 %s 與首頁卡片牆 %s 不同（收錄新論文會使其後之編號後移），須以 build_paper_prototype.py 重建' % (pn, hn))
        if fm.get('status') != 'published':
            why.append('網頁已產生，論文頁 status 須改為 published（目前為 %s）' % fm.get('status'))
        r['S8'] = ('NG', why) if why else ('OK', ['網頁存在且不舊於卡片檔與論文頁，編號與首頁一致，status 為 published（瀏覽器驗證須另行執行 verify_page.js）'])

    # S9 上架
    why = []
    focus_paper = fm.get('my_focus') is True
    if not os.path.exists(card_path):
        why.append('沒有卡片檔，無法上卡片牆')
    elif not tracked(card_rel) or dirty([card_rel]):
        why.append('卡片檔尚未提交或有未提交之修改；卡片牆只收已提交之卡片檔（提交時以 --card 帶入並重建）')
    if focus_paper and slug not in focus:
        why.append('我的星系（web/index.html 之 focus.papers）沒有本篇')
    if not focus_paper and slug not in stars:
        why.append('星圖（web/index.html 之 papers）沒有本篇')
    if os.path.exists(card_path) and slug not in wall:
        why.append('卡片牆沒有本篇')
    if not ctx['home_ok']:
        why.append('首頁與資料不一致（build_home.py --check：%s），須重建' % ctx['home_msg'])
    r['S9'] = ('NG', why) if why else ('OK', ['%s與卡片牆皆有本篇；首頁與資料一致（瀏覽器驗證須另行執行 verify_wall.js、verify_star.js）'
                                            % ('我的星系' if focus_paper else '星圖')])

    # S10 提交
    files = [p for p in (page_rel, ev_rel, card_rel, proto_rel) if os.path.exists(os.path.join(ROOT, p))]
    d = dirty(files)
    untracked = [p for p in files if not tracked(p)]
    why = []
    if d:
        why.append('有未提交之修改：' + '、'.join(d))
    if untracked:
        why.append('尚未加入版控：' + '、'.join(untracked))
    if slug not in ctx['log']:
        why.append('wiki/log.md 沒有提到本篇之日誌')
    r['S10'] = ('NG', why) if why else ('OK', ['本篇檔案皆已提交，日誌有紀錄'])
    return r


def raw_files():
    out = []
    if not os.path.isdir(RAW):
        return out
    for dirpath, dirs, files in os.walk(RAW):
        dirs[:] = [d for d in dirs if d not in ('.git', '.md')]
        for f in files:
            if f.lower().endswith('.pdf') and '繁體中文翻譯' not in f:
                out.append(os.path.relpath(os.path.join(dirpath, f), ROOT).replace('\\', '/'))
    return sorted(out)


def show_new():
    if not os.path.isdir(RAW):
        say('本機沒有 raw/（未 clone Mine-RAW），無法列出原始檔。')
        return
    pages = {}
    for f in os.listdir(os.path.join(WIKI, 'papers')):
        if f.endswith('.md') and not is_redirect(os.path.join(WIKI, 'papers', f)):
            pages[f[:-3]] = read(os.path.join(WIKI, 'papers', f))
    index = read(os.path.join(WIKI, 'index.md'))
    todo_path = os.path.join(WIKI, 'todo.md')
    todo = read(todo_path) if os.path.exists(todo_path) else ''
    todo_items = re.split(r'(?m)^(?=### TD-\d+ )', todo)
    main = {raw_cited(t): s for s, t in pages.items() if raw_cited(t)}
    rows = []
    for rel in raw_files():
        if rel in main:
            continue
        name = os.path.basename(rel)
        also = [s for s, t in pages.items() if rel in t or name in t]
        tds = [re.match(r'### (TD-\d+) \| (\w+)', it).group(1, 2) for it in todo_items
               if it.startswith('### TD-') and name in it]
        td_note = '、'.join('%s（%s）' % t for t in tds)
        if also:
            # 已被論文頁引用者（多半是奠基論文）優先歸「已引用」：待辦條目可能只是順帶提到這份檔案
            rows.append(('已引用', rel, '列於論文頁 %s（例如奠基論文），不另立頁面；需另立時依 intake.md 第三節判斷%s'
                         % ('、'.join(also), '；另見 wiki/todo.md ' + td_note if tds else '')))
        elif tds:
            rows.append(('已列待辦', rel, '已登記於 wiki/todo.md %s；依該條目之狀態處理（waiting 者不得自行動工），可動工時依 SKILL.md 第五節從 S0 開始'
                         % td_note))
        elif rel in index or name in index or name[:-4] in index:
            rows.append(('已立案', rel, 'wiki/index.md 有 [planned] 條目，依 SKILL.md 第四節從 S1 開始收錄'))
        else:
            rows.append(('新檔案', rel, '尚無論文頁，依 SKILL.md 第四節從 S0 開始收錄'))
    code, out = run(['git', '-C', 'raw', 'status', '--porcelain'])
    pending = [line[3:] for line in out.splitlines() if line.strip()]
    say('raw/ 原始檔 %d 個（不含中文譯本）；已有論文頁 %d 個；未收錄 %d 個' % (len(raw_files()), len(main), len(rows)))
    for kind, rel, note in rows:
        say('  [%s] %s' % (kind, rel))
        say('         %s' % note)
    if pending:
        say('raw/（Mine-RAW）有未提交之變動 %d 項，依 references/intake.md 第五節處理：' % len(pending))
        for p in pending:
            say('  ' + p)


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    args = sys.argv[1:]
    if args == ['--new']:
        show_new()
        return 0
    if any(a.startswith('-') for a in args):
        say(__doc__)
        return 2
    ctx = collect()
    if args:
        bad = 0
        for slug in args:
            if is_redirect(os.path.join(WIKI, 'papers', slug + '.md')):
                bad = 1
                say('%s：這是舊路徑轉介，請使用轉介檔連結的新論文頁。' % slug)
                continue
            if slug not in ctx['papers']:
                bad = 1
                if os.path.exists(os.path.join(WIKI, 'evidence', slug + '.md')):
                    state, why = check_evidence(slug)
                    say('== %s（尚無論文頁，只檢查證據表）' % slug)
                    say('  %-4s %-4s %s' % ('S3', state, '；'.join(why)))
                    say('  下一步：' + NEXT['S4'].replace('<slug>', slug))
                else:
                    say('%s：找不到 wiki/papers/%s.md 與 wiki/evidence/%s.md。尚未收錄者依 SKILL.md 第五節 S1 至 S4 先建立證據表與論文頁。' % (slug, slug, slug))
                continue
            r = check(slug, ctx)
            say('== %s' % slug)
            for step in STEPS:
                state, why = r[step]
                say('  %-4s %-4s %s' % (step, state, '；'.join(why)))
            state, step = completion_status(r)
            if state == 'NG':
                bad = 1
                say('  下一步：' + NEXT[step].replace('<slug>', slug))
            elif state != 'OK':
                pending = [s for s in STEPS if r[s][0] in ('WARN', '--')]
                say('  結果：尚待確認 %s；WARN 須逐條交代，無法判斷者須補查' % '、'.join(pending))
            else:
                say('  結果：全部完成')
        return bad
    say('%-52s %s  下一步' % ('slug', ' '.join('%-4s' % s for s in STEPS)))
    done = 0
    for slug in ctx['papers']:
        r = check(slug, ctx)
        marks = ' '.join('%-4s' % {'OK': 'ok', 'NG': 'NG', 'WARN': '!', '--': '--'}[r[s][0]] for s in STEPS)
        state, step = completion_status(r)
        if state == 'OK':
            done += 1
        next_step = '完成' if state == 'OK' else (step if state == 'NG' else '待確認 ' + step)
        say('%-52s %s  %s' % (slug, marks, next_step))
    say('---')
    say('論文 %d 篇；全部步驟完成 %d 篇。ok 完成、NG 未完成、! 有 WARN 須交代、-- 無法判斷。' % (len(ctx['papers']), done))
    if not ctx['home_ok']:
        say('首頁與資料不一致：' + ctx['home_msg'] + '（依 references/publish.md 重建）')
    say('逐項原因：python .agents/skills/paper-pipeline/scripts/pipeline_status.py <slug>；未收錄之原始檔：--new')
    return 0


if __name__ == '__main__':
    sys.exit(main())
