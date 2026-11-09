"""建置首頁 web/index.html（知識星圖）。

用法（於倉庫根目錄執行）：
    python tools/build_home.py           # 重建 web/index.html
    python tools/build_home.py --check   # 只比對，不寫檔；與現有檔案不同時結束碼為 1

資料來源：
    * wiki/papers/*.md、wiki/concepts/*.md 之 Frontmatter（論文、概念、雙年份、card_line、我的關注欄位）。
    * AGENTS.md 第八章標籤白名單（標籤所屬學科）。

群星模式開場不預選任何論文（DESIGN.md 第二章第 2 節），故本腳本不決定預設亮星。

學科色不在本腳本定義：頁面執行時讀取 web/assets/css/theme.css 之 --color-<domain>
（色碼唯一真實來源，見 AGENTS.md 第二章）。

本腳本只用 Python 標準函式庫，輸出內容只取決於 wiki/ 與 AGENTS.md，重跑即可重現。
版面與樣式請改 tools/home_template.html、web/assets/css/starmap.css、web/assets/js/starmap.js，
不要手改 web/index.html。
"""
import glob
import json
import math
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
WIKI = os.path.join(ROOT, 'wiki')
TEMPLATE = os.path.join(ROOT, 'tools', 'home_template.html')
OUT = os.path.join(ROOT, 'web', 'index.html')

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
        venue = venue_short(f['venue'], int(f['paper_year']))
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
        venue = venue_short(f['venue'], int(f['paper_year']))
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


def build():
    P = {os.path.basename(p)[:-3]: frontmatter(p) for p in sorted(glob.glob(os.path.join(WIKI, 'papers', '*.md')))}
    C = {os.path.basename(p)[:-3]: frontmatter(p) for p in sorted(glob.glob(os.path.join(WIKI, 'concepts', '*.md')))}
    for s, f in C.items():
        if not isinstance(f.get('papers'), list):
            f['papers'] = []
    stars = build_stars(P, C, whitelist())
    data = dict(stars, focus=build_focus(P, C))
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    t = open(TEMPLATE, encoding='utf-8').read()
    for mark in ('/*__DATA__*/', '<!--__NOSCRIPT__-->'):
        if t.count(mark) != 1:
            raise SystemExit('範本中 %s 必須恰好出現一次' % mark)
    html = t.replace('/*__DATA__*/', blob).replace('<!--__NOSCRIPT__-->', noscript(stars))
    return html, data


def main():
    html, data = build()
    focus = data['focus'] or {'papers': []}
    summary = '群星 %d、標籤 %d、概念 %d、我的關注 %d' % (
        len(data['papers']), len(data['tags']), len(data['concepts']), len(focus['papers']))
    old = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else None
    if '--check' in sys.argv[1:]:
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
