"""建置首頁 web/index.html（知識星圖與群星檔案卡片牆）。

用法（於倉庫根目錄執行）：
    python tools/build_home.py                      # 重建 web/index.html
    python tools/build_home.py --card <slug> ...    # 同上，另把自己這篇尚未提交的卡片檔放上卡片牆
    python tools/build_home.py --check [--card ...] # 只比對，不寫檔；與現有檔案不同時結束碼為 1

資料來源：
    * wiki/papers/*.md、wiki/concepts/*.md 之 Frontmatter（論文、概念、雙年份、card_line、我的關注欄位）。
    * AGENTS.md 第八章標籤白名單（標籤所屬學科）。
    * 卡片牆：wiki/cards/<slug>.md 之「封面」區段（封面斷行、封面標題、研究類型），只取 **Git 已提交**
      （精確說是 Git 索引中）的版本，工作目錄中他人尚未提交的卡片檔不會被帶上首頁；自己這篇尚未提交時以
      --card <slug> 帶入工作目錄之版本（paper-card-writer 之 references/card-wall.md）。每張卡連到
      web/prototypes/paper-v1/<slug>.html，該檔須同樣已提交（或與 --card 一起存在於工作目錄）。

群星模式開場不預選任何論文（DESIGN.md 第二章第 2 節），故本腳本不決定預設亮星。

學科色不在本腳本定義：頁面執行時讀取 web/assets/css/theme.css 之 --color-<domain>
（色碼唯一真實來源，見 AGENTS.md 第二章）；卡片牆以 CSS 變數 var(--color-<domain>) 上色。

本腳本只用 Python 標準函式庫（另呼叫 git 讀取已提交之卡片檔），輸出內容只取決於 wiki/、AGENTS.md 與 Git 索引，
重跑即可重現。版面與樣式請改 tools/home_template.html、web/assets/css/starmap.css、web/assets/js/starmap.js，
不要手改 web/index.html。卡片牆自我檢查有 ERROR 時不寫檔、結束碼為 1。
"""
import glob
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
WIKI = os.path.join(ROOT, 'wiki')
TEMPLATE = os.path.join(ROOT, 'tools', 'home_template.html')
OUT = os.path.join(ROOT, 'web', 'index.html')
CHECK_CARDS = os.path.join(ROOT, '.agents', 'skills', 'paper-card-writer', 'scripts', 'check_cards.py')
# 卡片牆每張卡連到的論文頁（相對於 web/）。正式論文頁（wiki/todo.md TD-002）產出前連到論文頁原型（2026-11-10 使用者決定）。
PAPER_HREF = 'prototypes/paper-v1/%s.html'
# 封面卡之硬上限（paper-card-writer 之 references/cover.md 第三、四節）
LINE_MAX, LINES_MAX, TITLE_MAX = 9, 3, 22

# ---------------------------------------------------------------- 設定

# 學科：顯示名稱、星圖方位角（度，0 為正右、順時針）與形狀（10x10 SVG 路徑，見 DESIGN.md 第七章）。
DOMAINS = [
    ('bio', '生醫', '生醫與生命科技', 210, 'M0.8 5 A4.2 4.2 0 1 0 9.2 5 A4.2 4.2 0 1 0 0.8 5 Z'),
    ('ai', 'AI', '人工智慧、計算與數學', 270, 'M1 1 H9 V9 H1 Z'),
    ('physics', '物理', '物理、天文與地球科學', 330, 'M5 0.6 L9.6 9.2 L0.4 9.2 Z'),
    ('econ', '經濟', '宏觀經濟與治理', 150, 'M5 0.3 L9.7 5 L5 9.7 L0.3 5 Z'),
    ('chem', '化學', '化學、材料與能源', 30, 'M5 0.4 L9.2 2.8 L9.2 7.2 L5 9.6 L0.8 7.2 L0.8 2.8 Z'),
    ('human', '人文', '語言、心理與社會', 90, 'M3.6 0.6 H6.4 V3.6 H9.4 V6.4 H6.4 V9.4 H3.6 V6.4 H0.6 V3.6 H3.6 Z'),
]
# 桌面星圖（1000 x 920，中心 500,460）之學科中心，取自畫布樣稿「首頁 v5」：各學科自成一團，
# 標籤繞著學科中心向外展開、論文在標籤外側，不擠成同心圓（圓形為手機版之折衷，見 DESIGN.md 第二章第 2 節）。
DESK = {'w': 1000, 'h': 920, 'c': (500, 460)}
# 生醫、AI、物理、經濟四團取樣稿 v5；化學與人文目前無已收錄論文，放在下緣、各靠最相近之學科
# （人文靠經濟、化學靠物理），環繞順序與手機版圓形一致：AI、物理、化學、人文、經濟、生醫。
DESK_HUB = {'bio': (285, 300), 'ai': (725, 290), 'physics': (730, 620), 'econ': (235, 610), 'chem': (610, 780), 'human': (370, 780)}
TBOX = (60, 60, 940, 860)   # 桌面標籤可用範圍
PBOX = (50, 50, 950, 870)   # 桌面論文星可用範圍
# 同一學科內標籤沿圓周排列的順序（減少連線交錯）；未列出的標籤依白名單順序接在後面。
TAG_ORDER = {
    'bio': ['#分子生物', '#基因工程', '#生物科技', '#神經科學', '#結構生物學'],
    'ai': ['#計算生物', '#計算機視覺', '#深度學習', '#強化學習', '#人工智慧'],
    'physics': ['#統計物理', '#量子物理', '#天體物理', '#宇宙學'],
    'econ': ['#宏觀經濟學', '#制度經濟學'],
}
# 桌面星團之標籤順序（手機同心圓仍用 TAG_ORDER）：AI 之 #人工智慧 六篇全用，放在扇形中段，
# 論文才會分往兩側；放在一端時每篇都要拉一條線到同一側，連線交錯成一團。
DESK_TAG_ORDER = {
    'ai': ['#計算生物', '#計算機視覺', '#人工智慧', '#深度學習', '#強化學習'],
}
# 桌面星團開口之個別設定（度，0 為向右、90 為向下）；未列者取「背離中心」與「朝左右兩側」之間。
# AI 論文最多（6 篇），但學科中心右側只剩約 215 單位，開口朝右會擠成一團；改朝右上，用上方與生醫之間的空處。
DESK_OPEN = {'ai': 310}
# focus_role 鍵值與名稱（AGENTS.md 第七章第 1 節）。
ROLES = [('senior-thesis', '學長姐論文'), ('report', '報告題材'), ('taiwan-linguistics', '臺灣語言學'),
         ('international', '國際文獻'), ('llm-assisted', '大模型輔助')]
# 我的星系中心星：不對應任何 Wiki 頁面，只顯示名稱與狀態，不公開題目與內容（DESIGN.md 第四章、第八章第 13 項）。
THESIS = {'name': '我的碩論', 'status': '進行中', 'statusEn': 'IN PROGRESS'}
# 未針對特定語言之研究，於說明中顯示的研究類型。
STUDY_TYPE = {'2023-low-resource-nmt-survey-ranathunga': '綜述', '2025-indigenous-tek-ai-revitalization-wang': '文化復振'}

# ---------------------------------------------------------------- 讀取


def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'---\r?\n(.*?)\r?\n---', text, re.S)
    if not m:
        raise SystemExit('缺少 Frontmatter：' + path)
    out, key = {}, None
    for line in m.group(1).splitlines():
        item = re.match(r'^\s+-\s+(.*)$', line)
        if item and key:
            if not isinstance(out.get(key), list):
                out[key] = []
            out[key].append(unquote(item.group(1).strip()))
            continue
        mm = re.match(r'^(\w+):\s*(.*)$', line)
        if not mm:
            continue
        key, v = mm.group(1), mm.group(2).strip()
        v = re.sub(r'\s+#\s.*$', '', v) if not v.startswith('"') else v
        if v.startswith('['):
            try:
                v = json.loads(v)
            except ValueError:
                pass
        elif v in ('true', 'false'):
            v = v == 'true'
        elif re.fullmatch(r'-?\d+', v):
            v = int(v)
        else:
            v = unquote(v)
        out[key] = v
    return out


def unquote(v):
    if len(v) >= 2 and v[0] == v[-1] == '"':
        return v[1:-1].replace('\\"', '"')
    return v


def whitelist():
    """AGENTS.md 第八章白名單：標籤 -> 所屬學科（依表格順序）。"""
    text = open(os.path.join(ROOT, 'AGENTS.md'), encoding='utf-8').read()
    sec = text.split('### 標籤白名單與色系歸屬', 1)[1].split('\n>', 1)[0]
    tags = {}
    for line in sec.splitlines():
        m = re.match(r'^\|\s*`(\w+)`\s*\|(.*)\|\s*$', line)
        if m:
            for t in re.findall(r'`(#[^`]+)`', m.group(2)):
                tags[t] = m.group(1)
    if not tags:
        raise SystemExit('讀不到 AGENTS.md 第八章之標籤白名單')
    return tags


# ---------------------------------------------------------------- 顯示文字


def short_name(title_zh):
    """星圖與說明框所用之短名：取中文標題冒號前一段，去掉括號內的英文原名。"""
    s = re.sub(r'（[^）]*）', '', title_zh.split('：')[0]).strip()
    return s or title_zh


def venue_short(venue, year):
    v = venue.strip()
    if v.startswith("Master's Thesis"):
        return '碩士論文'
    m = re.search(r'Findings of the Association for Computational Linguistics:\s*([A-Za-z]+ \d{4})', v)
    if m:
        return 'Findings of ' + m.group(1)
    m = re.search(r'\(([A-Za-z][A-Za-z-]*(?: \d{4})?)\)', v)
    if m and not m.group(1).startswith('published'):
        return m.group(1)
    if 'Annual Meeting of the Association for Computational Linguistics' in v:
        return 'ACL %d' % year
    if v.lower().startswith('arxiv'):
        return 'arXiv'
    return re.split(r',|;| \(', v)[0].strip()


def venue_of(f):
    """期刊或會議簡稱：Frontmatter 有 venue_short（AGENTS.md 第七章第 1 節，選填）時用之，否則由 venue 自動縮短。"""
    return str(f.get('venue_short') or '').strip() or venue_short(f['venue'], int(f['paper_year']))


def award_line(f):
    honor = f.get('honor') or ''
    if not honor:
        return None
    if '諾貝爾' in honor:
        return '%s 諾貝爾獎' % f['award_year']
    return honor.split('（')[0].strip()


def years_line(f, venue):
    """AGENTS.md 第七章雙年份：「2005 發表 ｜ 2026 諾貝爾獎」；未獲獎者為「發表年 發表 ｜ 期刊或會議」。"""
    return '%s 發表 ｜ %s' % (f['paper_year'], award_line(f) or venue)


def langs_text(f, slug):
    langs = f.get('focus_languages') or []
    if langs:
        return '研究語言：' + '、'.join(langs)
    return '研究類型：' + STUDY_TYPE.get(slug, '綜述')


# ---------------------------------------------------------------- 幾何


def pol(a, r, c=(500, 500)):
    t = math.radians(a)
    return [c[0] + r * math.cos(t), c[1] + r * math.sin(t)]


def ang(x, y, c=(500, 500)):
    return math.degrees(math.atan2(y - c[1], x - c[0])) % 360


def cmean(angles):
    sx = sum(math.cos(math.radians(a)) for a in angles)
    sy = sum(math.sin(math.radians(a)) for a in angles)
    return math.degrees(math.atan2(sy, sx)) % 360


def relax(pos, keys, mind, rmin, rmax, iters, step=0.5, rfix=None):
    """互相推開距離小於 mind 的點，並把半徑限制在 [rmin, rmax]（或固定為 rfix）。"""
    for _ in range(iters):
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                dx = pos[a][0] - pos[b][0]
                dy = pos[a][1] - pos[b][1]
                d = math.hypot(dx, dy) or 1
                if d < mind:
                    m = (mind - d) / 2 * step
                    pos[a][0] += dx / d * m
                    pos[a][1] += dy / d * m
                    pos[b][0] -= dx / d * m
                    pos[b][1] -= dy / d * m
        for s in keys:
            a = ang(*pos[s])
            r = math.hypot(pos[s][0] - 500, pos[s][1] - 500)
            r = rfix if rfix else min(max(r, rmin), rmax)
            pos[s] = pol(a, r)
            pos[s][0] = min(max(pos[s][0], 40), 960)
            pos[s][1] = min(max(pos[s][1], 40), 960)


def rel(a, base):
    """角度 a 相對於 base 之差，落在 (-180, 180]。"""
    return (a - base + 180) % 360 - 180


def reach(h, a, box):
    """自 h 沿角度 a 前進、仍留在 box 內之最遠距離。"""
    t = math.radians(a)
    dx, dy = math.cos(t), math.sin(t)
    lim = []
    if dx > 1e-9:
        lim.append((box[2] - h[0]) / dx)
    if dx < -1e-9:
        lim.append((box[0] - h[0]) / dx)
    if dy > 1e-9:
        lim.append((box[3] - h[1]) / dy)
    if dy < -1e-9:
        lim.append((box[1] - h[1]) / dy)
    return min(lim) if lim else 1e9


def relax_free(pos, keys, fixed, mind, mfix, box, iters, step=0.5, keep=None):
    """桌面星圖：可動點互相推開（距離小於 mind），並避開固定點（距離小於 mfix），最後限制在 box 內；
    keep(key, xy) 可再加約束（例如標籤與學科中心之距離）。"""
    x0, y0, x1, y1 = box
    for _ in range(iters):
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                dx = pos[a][0] - pos[b][0]
                dy = pos[a][1] - pos[b][1]
                d = math.hypot(dx, dy) or 1
                if d < mind:
                    m = (mind - d) / 2 * step
                    pos[a][0] += dx / d * m
                    pos[a][1] += dy / d * m
                    pos[b][0] -= dx / d * m
                    pos[b][1] -= dy / d * m
            for q in fixed:
                dx = pos[a][0] - q[0]
                dy = pos[a][1] - q[1]
                d = math.hypot(dx, dy) or 1
                if d < mfix:
                    pos[a][0] += dx / d * (mfix - d) * step
                    pos[a][1] += dy / d * (mfix - d) * step
        for s in keys:
            if keep:
                pos[s] = keep(s, pos[s])
            pos[s][0] = min(max(pos[s][0], x0), x1)
            pos[s][1] = min(max(pos[s][1], y0), y1)


def spread(n, center, gap, lo, hi):
    """一列 n 顆星在 [lo, hi] 內以 center 為中心等距排開；放不下時縮小間距。"""
    if n > 1:
        gap = min(gap, (hi - lo) / (n - 1))
    xs = [center + (i - (n - 1) / 2) * gap for i in range(n)]
    shift = max(0, lo - xs[0]) - max(0, xs[-1] - hi)
    return [x + shift for x in xs]


# ---------------------------------------------------------------- 群星


def build_stars(P, C, tag_dom):
    ms = {s: f for s, f in P.items() if not f.get('my_focus')}
    dom_keys = [d[0] for d in DOMAINS]
    used = []
    for f in ms.values():
        for t in f['domain_tags']:
            if t not in tag_dom:
                raise SystemExit('標籤 %s 不在 AGENTS.md 第八章白名單' % t)
            if t not in used:
                used.append(t)
    domains = []
    hub = {}
    for key, name, full, a, shape in DOMAINS:
        hub[key] = [round(v) for v in pol(a, 210)]
        domains.append(dict(key=key, idx='%02d' % (len(domains) + 1), name=name, full=full, ang=a, shape=shape, hub=hub[key]))
    tags = {}
    for d in domains:
        order = [t for t in TAG_ORDER.get(d['key'], []) if t in used]
        order += [t for t in tag_dom if tag_dom[t] == d['key'] and t in used and t not in order]
        n = len(order)
        for i, t in enumerate(order):
            a = d['ang'] + (i - (n - 1) / 2) * 11
            tags[t] = dict(d=d['key'], a=a, xy=pol(a, 345))
        d['tags'] = order
    base = {s: cmean([tags[t]['a'] for t in f['domain_tags']]) for s, f in ms.items()}
    groups = {}
    for s in sorted(base):
        groups.setdefault(round(base[s] / 3), []).append(s)
    pos = {}
    for g in groups.values():
        for i, s in enumerate(g):
            off = (i - (len(g) - 1) / 2) * 9
            pos[s] = pol(base[s] + off, 430 + (i % 2) * 30)
    relax(pos, sorted(pos), 96, 372, 472, 500)

    papers = []
    for s, f in sorted(ms.items(), key=lambda kv: (-int(kv[1]['timeline_year']), kv[0])):
        venue = venue_of(f)
        papers.append(dict(
            slug=s, name=short_name(f['title_zh']), titleZh=f['title_zh'], title=f['title'], d=f['domain'],
            tags=f['domain_tags'], p=int(f['paper_year']), a=int(f['award_year']), award=award_line(f),
            nobel='諾貝爾' in (f.get('honor') or ''), honor=f.get('honor') or '', venue=venue,
            years=years_line(f, venue), cardLine=f['card_line'], doi=f.get('doi_url', ''),
            x=round(pos[s][0]), y=round(pos[s][1])))
    cpos = {}
    for s, f in C.items():
        ps = [p for p in f.get('papers', []) if p in ms]
        if ps:
            cpos[s] = pol(cmean([ang(*pos[p]) for p in ps]), 120)
    relax(cpos, sorted(cpos), 64, 0, 0, 300, step=0.25, rfix=120)
    concepts = [dict(slug=s, name=C[s]['title_zh'], d=C[s]['domain'], papers=[p for p in C[s]['papers'] if p in ms],
                     x=round(cpos[s][0]), y=round(cpos[s][1])) for s in sorted(cpos)]
    for d in domains:
        d['count'] = sum(1 for p in papers if p['d'] == d['key'])
        del d['ang']
    tag_out = {}
    for t in used:
        tag_out[t] = dict(d=tags[t]['d'], x=round(tags[t]['xy'][0]), y=round(tags[t]['xy'][1]),
                          count=sum(1 for f in ms.values() if t in f['domain_tags']))
    assert set(dom_keys) >= {p['d'] for p in papers}
    out = dict(domains=domains, tags=tag_out, papers=papers, concepts=concepts)
    build_desk(out, ms)
    return out


def build_desk(S, ms):
    """桌面星圖座標（欄位 dk）：學科中心取樣稿 v5；標籤在中心外側展開，跨學科標籤偏向所連論文之學科；
    論文在所屬學科標籤之外側；概念頁在半徑 120 之內圈。"""
    C = DESK['c']
    hub = {d['key']: DESK_HUB[d['key']] for d in S['domains']}
    # 星團開口：介於「背離中心」與「朝左右兩側」之間，讓寬版面的左右空間被用上（同樣稿 v4 之生醫、AI 兩團）
    theta = {k: cmean([ang(*hub[k], c=C), 0 if hub[k][0] >= C[0] else 180]) for k in hub}
    theta.update(DESK_OPEN)
    tdk, towner = {}, {}
    for d in S['domains']:
        k = d['key']
        first = [t for t in DESK_TAG_ORDER.get(k, []) if t in d['tags']]
        order = first + [t for t in d['tags'] if t not in first]
        if not order:
            continue
        want = {}
        for t in order:
            # 偏向之權重依本學科論文數加重：多數論文屬本學科之標籤（如 #人工智慧 有 6 篇 AI、1 篇物理），
            # 不因一篇跨學科論文被拉離自己的星團；只有跨學科論文在用的標籤（如 #結構生物學）才明顯偏向對方
            own = sum(1 for f in ms.values() if t in f['domain_tags'] and f['domain'] == k)
            dirs = [theta[k]] * (2 + own) + [ang(*hub[f['domain']], c=hub[k]) for f in ms.values()
                                             if t in f['domain_tags'] and f['domain'] != k]
            want[t] = rel(cmean(dirs), theta[k])
        # 只有明顯偏向（約 15 度以上）才改變順序，其餘依設定之標籤順序
        srt = sorted(order, key=lambda t: (round(want[t] / 30), order.index(t)))
        n = len(srt)
        center = sum(want.values()) / n
        offs = spread(n, center, 44, -100, 100)
        for i, t in enumerate(srt):
            a = theta[k] + offs[i]
            tdk[t] = pol(a, min(115 if i % 2 == 0 else 150, reach(hub[k], a, TBOX) - 70), hub[k])
            towner[t] = k

    def near_hub(t, xy):
        h = hub[towner[t]]
        a, r = ang(*xy, c=h), math.hypot(xy[0] - h[0], xy[1] - h[1])
        return pol(a, min(max(r, 100), 175), h)
    # 標籤互相推開、避開中心與其他學科中心，但留在自己學科中心 100 至 175 之間
    relax_free(tdk, sorted(tdk), [C] + list(hub.values()), 66, 84, TBOX, 300, keep=near_hub)
    # 論文：在所屬學科標籤之間、略往外（只有一個所屬標籤者放在該標籤外側）
    pos = {}
    for p in S['papers']:
        k = p['d']
        own = [t for t in p['tags'] if S['tags'][t]['d'] == k] or p['tags']
        mx = sum(tdk[t][0] for t in own) / len(own)
        my = sum(tdk[t][1] for t in own) / len(own)
        a = ang(mx, my, c=hub[k])
        r = math.hypot(mx - hub[k][0], my - hub[k][1]) + (65 if len(own) == 1 else 50)
        pos[p['slug']] = pol(a, min(r, reach(hub[k], a, PBOX)), hub[k])
    # 標籤相同的論文會落在同一點：沿垂直於學科中心方向的方向等距排開，再交給 relax_free
    same = {}
    for p in S['papers']:
        same.setdefault((p['d'], round(pos[p['slug']][0]), round(pos[p['slug']][1])), []).append(p['slug'])
    for (k, x, y), group in same.items():
        n = len(group)
        if n < 2:
            continue
        a = math.radians(ang(x, y, c=hub[k]) + 90)
        for i, s in enumerate(group):
            off = (i - (n - 1) / 2) * 48
            pos[s] = [x + off * math.cos(a), y + off * math.sin(a)]
    fixed = [C] + list(hub.values()) + list(tdk.values())
    relax_free(pos, sorted(pos), fixed, 58, 40, PBOX, 400)
    cpos = {}
    for c in S['concepts']:
        cpos[c['slug']] = pol(cmean([ang(*pos[s], c=C) for s in c['papers']]), 120, C)
    for _ in range(300):
        keys = sorted(cpos)
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                da, db = ang(*cpos[a], c=C), ang(*cpos[b], c=C)
                gap = rel(db, da)
                if abs(gap) < 30:
                    push = (30 - abs(gap)) / 4 * (1 if gap >= 0 else -1)
                    cpos[a] = pol(da - push, 120, C)
                    cpos[b] = pol(db + push, 120, C)
    for d in S['domains']:
        d['dk'] = list(hub[d['key']])
    for t, v in S['tags'].items():
        v['dk'] = [round(tdk[t][0]), round(tdk[t][1])]
    for p in S['papers']:
        p['dk'] = [round(pos[p['slug']][0]), round(pos[p['slug']][1])]
    for c in S['concepts']:
        c['dk'] = [round(cpos[c['slug']][0]), round(cpos[c['slug']][1])]
    S['desk'] = dict(w=DESK['w'], h=DESK['h'], c=list(C))


# ---------------------------------------------------------------- 我的星系


def build_focus(P, C):
    fp = {s: f for s, f in P.items() if f.get('my_focus')}
    if not fp:
        return None
    counts = {}
    for f in fp.values():
        for c in f.get('concepts', []):
            counts[c] = counts.get(c, 0) + 1
    hubs = sorted(counts, key=lambda c: (-counts[c], c))[:2]
    if len(counts) > 2:
        print('WARN 我的關注涉及 %d 個概念，星系只畫篇數最多的兩個：%s' % (len(counts), '、'.join(hubs)), file=sys.stderr)
    # 南島語概念放左（F），低資源翻譯放右（L）；其他概念依篇數。
    hubs.sort(key=lambda c: (0 if 'formosan' in c else 1, c))
    keys = ['F', 'L'][:len(hubs)]
    con_key = dict(zip(hubs, keys))

    def zone(f):
        con = [con_key[c] for c in f.get('concepts', []) if c in con_key]
        return 'B' if len(con) != 1 else con[0]

    years = sorted({int(f['paper_year']) for f in fp.values()} | {2017})
    y0, y1 = years[0], years[-1]

    # 桌面（1000 x 920，樣稿 v5）：每年一條橫線，概念中心在左右兩側。
    step = 702 / max(1, y1 - y0)
    drow = {y: round(80 + (y - y0) * step) for y in range(y0, y1 + 1)}
    dzone = {'F': (300, 170, 410), 'B': (500, 420, 580), 'L': (710, 590, 840)}
    # 手機（1000 x H，原型 mobile-v2）：只排有論文的年份，概念中心在頂端。
    mrow = {y: 250 + i * 110 for i, y in enumerate(years)}
    mzone = {'F': (190, 60, 340), 'B': (500, 360, 640), 'L': (800, 660, 945)}
    mh = mrow[y1] + 200

    cells = {}
    for s, f in fp.items():
        cells.setdefault((int(f['paper_year']), zone(f)), []).append(s)
    dpos, mpos = {}, {}
    for (y, z), ss in cells.items():
        ss.sort()
        n = len(ss)
        for i, (s, x) in enumerate(zip(ss, spread(n, dzone[z][0], 66, dzone[z][1], dzone[z][2]))):
            dpos[s] = [round(x), drow[y] + ((7 if i % 2 else -7) if n > 1 else 0)]
        for i, (s, x) in enumerate(zip(ss, spread(n, mzone[z][0], 86 if n <= 3 else 78, mzone[z][1], mzone[z][2]))):
            mpos[s] = [round(x), mrow[y] + ((8 if i % 2 else -8) if n > 1 else 0)]

    roles = dict(ROLES)
    papers = []
    for s, f in sorted(fp.items(), key=lambda kv: (int(kv[1]['paper_year']), kv[0])):
        if f.get('focus_role') not in roles:
            raise SystemExit('%s 之 focus_role 不在五個鍵值內' % s)
        venue = venue_of(f)
        papers.append(dict(
            slug=s, name=short_name(f['title_zh']), titleZh=f['title_zh'], title=f['title'], d=f['domain'],
            year=int(f['paper_year']), role=f['focus_role'], langs=f.get('focus_languages') or [],
            langText=langs_text(f, s), con=[con_key[c] for c in f.get('concepts', []) if c in con_key],
            venue=venue, years=years_line(f, venue), cardLine=f['card_line'], doi=f.get('doi_url', ''),
            desk=dpos[s], mob=mpos[s]))
    zcount = {'F': 0, 'B': 0, 'L': 0}
    for f in fp.values():
        zcount[zone(f)] += 1
    hub_out = []
    for c, k in zip(hubs, keys):
        name = C[c]['title_zh'] if c in C else c
        hub_out.append(dict(key=k, slug=c, name=name.split('與')[0], full=name,
                            count=sum(1 for p in papers if k in p['con']),
                            desk=[95, 380] if k == 'F' else [905, 380], mob=[190, 70] if k == 'F' else [810, 70]))
    cols = [dict(key='F', label='僅南島語', count=zcount['F']), dict(key='B', label='兩者交集', count=zcount['B']),
            dict(key='L', label='僅低資源翻譯', count=zcount['L'])]
    return dict(
        hubs=hub_out, papers=papers, roles=[list(r) for r in ROLES], cols=cols, thesis=THESIS,
        desk=dict(w=1000, h=920, rows=[[y, drow[y], y in years] for y in range(y0, y1 + 1)], now=866,
                  thesisAt=[500, 866], colX={'F': 300, 'B': 500, 'L': 710}, colY=40),
        mob=dict(w=1000, h=mh, rows=[[y, mrow[y], True] for y in years], now=mrow[y1] + 120,
                 thesisAt=[500, mrow[y1] + 120], colX={'F': 190, 'B': 500, 'L': 810}, colY=205))


# ---------------------------------------------------------------- 卡片（首頁卡片牆與論文頁原型共用）


def card_numbers(P):
    """卡片編號：群星 No.、我的關注 F.，各自依 timeline_year 由新到舊、同年依 slug 排序。
    編號涵蓋全部已收錄論文（含尚無卡片檔者），補寫卡片不會改變其他卡片之編號；
    收錄新論文時，排在它之後的論文編號會後移。首頁卡片牆與 tools/build_paper_prototype.py 共用本函式。"""
    out = {}
    for focus, prefix in ((False, 'No.'), (True, 'F.')):
        group = sorted((s for s, f in P.items() if (f.get('my_focus') is True) == focus),
                       key=lambda s: (-int(P[s]['timeline_year']), s))
        for i, s in enumerate(group):
            out[s] = '%s%02d' % (prefix, i + 1)
    return out


def rnd(seed):
    """固定種子之亂數（mulberry32），與 web/assets/js/starmap.js 之 rndFrom 相同。"""
    s = [seed & 0xFFFFFFFF]

    def r():
        s[0] = (s[0] + 0x6D2B79F5) & 0xFFFFFFFF
        t = s[0]
        t = ((t ^ (t >> 15)) * (1 | t)) & 0xFFFFFFFF
        t = (t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return r


def cover_sky(f):
    """封面星窗內之 14 顆小星（左 %、上 %、直徑 px、不透明度）。首頁卡片牆與論文頁 Card 1 共用，同一篇兩處一致。"""
    r = rnd(int(f['paper_year']) * 7919 + len(f['card_line']))
    sizes = [1 if r() < 0.8 else 1.5 for _ in range(14)]
    return [(4 + r() * 92, 4 + r() * 42, sz, 0.3 + r() * 0.55) for sz in sizes]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git(*args, data=None):
    try:
        return subprocess.run(['git', '-C', ROOT] + list(args), input=data, capture_output=True)
    except OSError:
        return None


def indexed(prefix):
    """Git 索引中 prefix 下之檔案 {相對路徑: blob}，以及未解決衝突之路徑。
    平時索引即最近一次提交；合併進行中時，索引已含對方新增之檔案，故合併後重建也會帶上對方之卡片。
    不在 Git 工作區（或沒有 git）時回傳 None。"""
    r = git('ls-files', '-s', '-z', '--', prefix)
    if r is None or r.returncode != 0:
        return None
    files, conflicts = {}, []
    for rec in r.stdout.decode('utf-8').split('\0'):
        if not rec:
            continue
        meta, path = rec.split('\t', 1)
        _mode, sha, stage = meta.split()
        if stage == '0':
            files[path] = sha
        elif path not in conflicts:
            conflicts.append(path)
    return files, conflicts


def read_blobs(shas):
    if not shas:
        return {}
    r = git('cat-file', '--batch', data=''.join(s + '\n' for s in shas).encode('ascii'))
    if r is None or r.returncode != 0:
        raise SystemExit('無法以 git cat-file 讀取已提交之卡片檔')
    buf, i, out = r.stdout, 0, {}
    for s in shas:
        j = buf.index(b'\n', i)
        size = int(buf[i:j].split()[2])
        out[s] = buf[j + 1:j + 1 + size].decode('utf-8')
        i = j + 1 + size + 1
    return out


def cover_fields(text):
    """卡片檔「## 封面」區段之欄位。格式由 check_cards.py 檢查，這裡只取值。"""
    m = re.search(r'^## 封面\n(.*?)(?=^## |\Z)', text.replace('\r\n', '\n'), re.M | re.S)
    out = {}
    for line in (m.group(1) if m else '').splitlines():
        mm = re.match(r'^- ([^：\s*]+)：(.*)$', line)
        if mm and mm.group(1) not in out:
            out[mm.group(1)] = mm.group(2).strip()
    return out


def wall_sources(P, extra):
    """卡片牆要用的卡片檔：{slug: 內容}，以及錯誤、提示與來源說明。
    只收 Git 索引（已提交）之版本；extra（--card）指定之 slug 改用工作目錄版本，並先以 check_cards.py 檢查。"""
    errors, notes = [], []
    cards_dir = os.path.join(WIKI, 'cards')
    disk = {os.path.basename(p)[:-3]: p for p in glob.glob(os.path.join(cards_dir, '*.md'))}
    idx = indexed('wiki/cards/')
    if idx is None:
        notes.append(('WARN', '不在 Git 工作區：卡片牆改讀工作目錄之全部卡片檔，無法排除他人尚未提交之檔案'))
        cards = {s: open(p, encoding='utf-8').read() for s, p in disk.items()}
        protos = {s for s in P if os.path.exists(os.path.join(ROOT, 'web', PAPER_HREF % s))}
        source = '工作目錄'
    else:
        files, conflicts = idx
        for path in conflicts:
            errors.append('%s 有未解決之合併衝突：先解決卡片檔衝突再重建首頁' % path)
        slug_sha = {os.path.basename(p)[:-3]: sha for p, sha in files.items()
                    if p.endswith('.md') and os.path.dirname(p) == 'wiki/cards'}
        blobs = read_blobs(sorted(set(slug_sha.values())))
        cards = {s: blobs[sha] for s, sha in slug_sha.items()}
        pidx = indexed('web/prototypes/paper-v1/')
        protos = {os.path.basename(p)[:-5] for p in (pidx[0] if pidx else {}) if p.endswith('.html')}
        source = 'Git 已提交版本'
        for s, p in sorted(disk.items()):
            if s in extra:
                continue
            if s not in cards:
                notes.append(('INFO', 'wiki/cards/%s.md 尚未提交，未放上卡片牆。是自己這篇：加 --card %s；'
                                      '不是自己的：不要理會，也不要提交 web/index.html 以外的他人檔案' % (s, s)))
            elif open(p, encoding='utf-8').read() != cards[s].replace('\r\n', '\n'):   # core.autocrlf 下工作目錄可能是 CRLF
                notes.append(('INFO', 'wiki/cards/%s.md 在工作目錄有未提交之修改，牆上用的是已提交版本；'
                                      '修改是自己的：加 --card %s' % (s, s)))
    if extra:
        cc = load_module('check_cards_for_home', CHECK_CARDS)
        for s in extra:
            path = disk.get(s)
            if not path:
                errors.append('--card %s：找不到 wiki/cards/%s.md' % (s, s))
                continue
            cc.results.clear()
            cc.check_card(path, s, {})
            bad = [r for r in cc.results if r[0] == 'ERROR']
            for r in bad:
                errors.append('--card %s：check_cards.py ERROR %s:%s %s' % (s, r[1], r[2], r[3]))
            if bad:
                continue
            cards[s] = open(path, encoding='utf-8').read()
            if os.path.exists(os.path.join(ROOT, 'web', PAPER_HREF % s)):
                protos.add(s)
            else:
                protos.discard(s)
    return cards, protos, errors, notes, source


def build_wall(P, tag_dom, cards, protos, nums):
    """卡片牆（DESIGN.md 第二章第 3 節 F 版型）：群星卡在前、我的關注卡在後，各依編號排列。
    回傳 (HTML, 每張卡之摘要, 錯誤)。HTML 為靜態內容，starmap.js 只依模式與篩選切換 hidden。"""
    errors, rows, html = [], [], []
    roles = dict(ROLES)
    domains = {k: (short, full) for k, short, full, _a, _p in DOMAINS}
    for slug in sorted(cards, key=lambda s: (nums.get(s, '').startswith('F.'), nums.get(s, ''))):
        f = P.get(slug)
        if f is None:
            errors.append('wiki/cards/%s.md 沒有對應之論文頁 wiki/papers/%s.md' % (slug, slug))
            continue
        cv = cover_fields(cards[slug])
        where = 'wiki/cards/%s.md「封面」' % slug
        lines = cv.get('封面斷行', '').split('／')
        if ''.join(lines) != f['card_line']:
            errors.append('%s：封面斷行去掉「／」後須與論文頁 card_line 逐字相同（封面斷行「%s」，card_line「%s」）'
                          % (where, cv.get('封面斷行', ''), f['card_line']))
        if len(lines) > LINES_MAX or any(not x or cc_width(x) > LINE_MAX for x in lines):
            errors.append('%s：封面斷行須為 1 至 %d 行、每行 %d 字以內且不得有空行（cover.md 第三節）：%s'
                          % (where, LINES_MAX, LINE_MAX, cv.get('封面斷行', '')))
        title = cv.get('封面標題') or short_name(f['title_zh'])
        if cc_width(title) > TITLE_MAX:
            errors.append('%s：論文名「%s」超過 %d 字，須填「封面標題」（cover.md 第四節）' % (where, title, TITLE_MAX))
        focus = f.get('my_focus') is True
        tag = ''
        if focus:
            langs = f.get('focus_languages') or []
            tag = '、'.join(langs) if langs else cv.get('研究類型', '')
            if not tag:
                errors.append('%s：我的關注論文之 focus_languages 為空，須填「研究類型」（cover.md 第七節）' % where)
        if slug not in protos:
            errors.append('%s 尚無論文頁原型 web/%s（未提交或未建置）：先執行 python tools/build_paper_prototype.py %s，'
                          '並與卡片檔一起提交' % (slug, PAPER_HREF % slug, slug))
        no = nums[slug]
        d = f['domain']
        venue = venue_of(f)
        years = years_line(f, venue)
        sky = ''.join('<i style="left:%.1f%%;top:%.1f%%;width:%spx;height:%spx;opacity:%.2f"></i>' % (x, y, sz, sz, op)
                      for x, y, sz, op in cover_sky(f))
        line_html = ''.join('<span>%s</span>' % esc(x) for x in lines)
        if focus:
            head = roles.get(f.get('focus_role'), '')
            color = 'human' if d == 'human' else 'ai'
            label = '%s：%s。%s：%s，%s，%s，開啟論文頁' % (
                title, f['card_line'], '研究語言' if f.get('focus_languages') else '研究類型', tag, years, head)
            win = '%s<span class="tag">%s</span><span class="rep"></span>' % (sky, esc(tag))
            attrs = 'class="wc focus" data-set="focus" hidden'
        else:
            head = domains[d][0]
            color = d
            label = '%s：%s。%s，開啟論文頁' % (title, f['card_line'], years)
            win = '%s<span class="rep%s"></span>' % (sky, ' award' if f.get('honor') else '')
            ins = [d] + [tag_dom[t] for t in f.get('domain_tags') or [] if t in tag_dom and tag_dom[t] != d]
            attrs = 'class="wc" data-set="stars" data-in="%s"' % ' '.join(dict.fromkeys(ins))
        html.append(
            '<a %s data-slug="%s" href="%s" style="--c:var(--color-%s)" aria-label="%s">'
            '<span class="cv"><span class="top"><span>%s</span><span>%s</span></span>'
            '<span class="win">%s<span class="wl">%s</span></span>'
            '<span class="ttl">%s</span><span class="bot">%s</span></span></a>' % (
                attrs, esc(slug), esc(PAPER_HREF % slug), color, esc(label), esc(no), esc(head),
                win, line_html, esc(title), esc(years)))
        rows.append((no, slug, '／'.join(lines)))
    return '\n'.join(html), rows, errors


def cc_width(s):
    """字數計法同 check_cards.py（全形 1、半形 0.5；paper-card-writer 之 style.md 第一節）。"""
    return sum(1 if unicodedata.east_asian_width(ch) in ('W', 'F', 'A') else 0.5 for ch in s)


# ---------------------------------------------------------------- 輸出


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))


def noscript(stars):
    rows = []
    names = {d['key']: d['full'] for d in stars['domains']}
    for p in stars['papers']:
        link = ' <a href="%s">DOI</a>' % esc(p['doi']) if p['doi'] else ''
        rows.append('<li>%s｜%s｜%s%s</li>' % (esc(p['name']), esc(p['years']), esc(names[p['d']]), link))
    return '\n'.join(rows)


def build(extra=()):
    P = {os.path.basename(p)[:-3]: frontmatter(p) for p in sorted(glob.glob(os.path.join(WIKI, 'papers', '*.md')))}
    C = {os.path.basename(p)[:-3]: frontmatter(p) for p in sorted(glob.glob(os.path.join(WIKI, 'concepts', '*.md')))}
    for s, f in C.items():
        if not isinstance(f.get('papers'), list):
            f['papers'] = []
    tag_dom = whitelist()
    stars = build_stars(P, C, tag_dom)
    data = dict(stars, focus=build_focus(P, C))
    cards, protos, errors, notes, source = wall_sources(P, set(extra))
    wall, rows, wall_errors = build_wall(P, tag_dom, cards, protos, card_numbers(P))
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    t = open(TEMPLATE, encoding='utf-8').read()
    for mark in ('/*__DATA__*/', '<!--__NOSCRIPT__-->', '<!--__WALL__-->'):
        if t.count(mark) != 1:
            raise SystemExit('範本中 %s 必須恰好出現一次' % mark)
    html = (t.replace('/*__DATA__*/', blob).replace('<!--__NOSCRIPT__-->', noscript(stars))
            .replace('<!--__WALL__-->', wall))
    report = dict(rows=rows, errors=errors + wall_errors, notes=notes, source=source, extra=list(extra),
                  stars=sum(1 for r in rows if r[0].startswith('No.')), focus=sum(1 for r in rows if r[0].startswith('F.')))
    return html, data, report


def print_wall(rep):
    """卡片牆自我檢查報告（paper-card-writer 之 references/card-wall.md 要求原樣貼進交付說明）。"""
    print('卡片牆：群星 %d 張、我的關注 %d 張（卡片取自%s；--card：%s）' % (
        rep['stars'], rep['focus'], rep['source'], '、'.join(rep['extra']) or '無'))
    for no, slug, lines in rep['rows']:
        print('  %-6s %s  %s' % (no, slug, lines))
    for level, msg in rep['notes']:
        print('%-5s %s' % (level, msg))
    for msg in rep['errors']:
        print('ERROR %s' % msg)
    warns = sum(1 for lv, _m in rep['notes'] if lv == 'WARN')
    print('卡片牆自我檢查：ERROR %d、WARN %d' % (len(rep['errors']), warns))


def parse_args(argv):
    check, extra, i = False, [], 0
    while i < len(argv):
        a = argv[i]
        if a == '--check':
            check, i = True, i + 1
        elif a == '--card' and i + 1 < len(argv) and not argv[i + 1].startswith('--'):
            extra.append(argv[i + 1])
            i += 2
        else:
            raise SystemExit('不明參數：%s。用法：python tools/build_home.py [--check] [--card <slug> ...]' % a)
    return check, extra


def main():
    check, extra = parse_args(sys.argv[1:])
    html, data, rep = build(extra)
    focus = data['focus'] or {'papers': []}
    summary = '群星 %d、標籤 %d、概念 %d、我的關注 %d' % (
        len(data['papers']), len(data['tags']), len(data['concepts']), len(focus['papers']))
    print_wall(rep)
    if rep['errors']:
        print('卡片牆有 ERROR，未%s web/index.html' % ('比對' if check else '寫入'), file=sys.stderr)
        return 1
    old = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else None
    if check:
        if old == html:
            print('web/index.html 與建置結果一致（%s）' % summary)
            return 0
        print('web/index.html 與建置結果不同，請執行 python tools/build_home.py', file=sys.stderr)
        return 1
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(html)
    print('%s web/index.html（%s）' % ('未變更' if old == html else '已寫入', summary))
    return 0


if __name__ == '__main__':
    sys.exit(main())
