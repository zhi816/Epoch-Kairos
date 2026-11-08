import re, glob, json, os, math, sys
WIKI = sys.argv[1]; OUT = sys.argv[2]


def fm(p):
    s = open(p, encoding='utf-8').read()
    m = re.match(r'---\r?\n(.*?)\r?\n---', s, re.S)
    out = {}
    for line in m.group(1).splitlines():
        mm = re.match(r'^(\w+):\s*(.*)$', line)
        if not mm:
            continue
        k, v = mm.group(1), mm.group(2).strip()
        if v.startswith('['):
            try:
                v = json.loads(v)
            except Exception:
                pass
        elif v.startswith('"') and v.endswith('"'):
            v = v[1:-1]
        out[k] = v
    if not isinstance(out.get('papers'), list):
        body = m.group(1)
        if 'papers:' in body:
            seg = body.split('papers:')[1].split('related_concepts')[0]
            out['papers'] = re.findall(r'"([^"]+)"', seg)
    return out


P = {os.path.basename(p)[:-3]: fm(p) for p in sorted(glob.glob(os.path.join(WIKI, 'papers', '*.md')))}
C = {os.path.basename(p)[:-3]: fm(p) for p in sorted(glob.glob(os.path.join(WIKI, 'concepts', '*.md')))}

DOM = {
    'bio': dict(name='生醫', full='生醫與生命科技', color='#9BDCB1', rgb='155,220,177', ang=210, shape='M0.8 5 A4.2 4.2 0 1 0 9.2 5 A4.2 4.2 0 1 0 0.8 5 Z'),
    'ai': dict(name='AI', full='人工智慧、計算與數學', color='#8FD5FD', rgb='143,213,253', ang=270, shape='M1 1 H9 V9 H1 Z'),
    'physics': dict(name='物理', full='物理、天文與地球科學', color='#D3BEFD', rgb='211,190,253', ang=330, shape='M5 0.6 L9.6 9.2 L0.4 9.2 Z'),
    'chem': dict(name='化學', full='化學、材料與能源', color='#FFB6A3', rgb='255,182,163', ang=30, shape='M5 0.4 L9.2 2.8 L9.2 7.2 L5 9.6 L0.8 7.2 L0.8 2.8 Z'),
    'human': dict(name='人文', full='語言、心理與社會', color='#F2B3D6', rgb='242,179,214', ang=90, shape='M3.6 0.6 H6.4 V3.6 H9.4 V6.4 H6.4 V9.4 H3.6 V6.4 H0.6 V3.6 H3.6 Z'),
    'econ': dict(name='經濟', full='宏觀經濟與治理', color='#E6C686', rgb='230,198,134', ang=150, shape='M5 0.3 L9.7 5 L5 9.7 L0.3 5 Z'),
}
TAGORDER = {
    'bio': ['#分子生物', '#基因工程', '#生物科技', '#神經科學', '#結構生物學'],
    'ai': ['#計算生物', '#計算機視覺', '#深度學習', '#強化學習', '#人工智慧'],
    'physics': ['#統計物理', '#量子物理', '#天體物理', '#宇宙學'],
    'econ': ['#宏觀經濟學', '#制度經濟學'],
}
SHORT = {
    '1982-hopfield-network': ('Hopfield 神經網絡', 'PNAS'),
    '1992-creative-destruction-aghion': ('創造性破壞與內生成長', 'Econometrica'),
    '2001-colonial-origins-acemoglu': ('比較發展的殖民起源', 'American Economic Review'),
    '2005-optogenetics': ('光遺傳學', 'Nature Neuroscience'),
    '2007-woodford-inflation-dynamics': ('宏觀穩定政策的微觀基礎', 'NBER Working Paper'),
    '2012-crispr-cas9': ('CRISPR-Cas9 基因剪刀', 'Science'),
    '2013-icecube-neutrino': ('冰立方高能宇宙微中子', 'Science'),
    '2016-ligo-gravitational-waves': ('LIGO 重力波直接探測', 'Physical Review Letters'),
    '2017-attention-is-all-you-need': ('Attention Is All You Need', 'NeurIPS'),
    '2021-alphafold2': ('AlphaFold2 蛋白質結構預測', 'Nature'),
    '2023-drugclip': ('DrugCLIP 虛擬藥物篩選', 'NeurIPS'),
    '2023-jwst-massive-galaxies': ('JWST 早期巨大星系', 'Nature Astronomy'),
    '2024-alphafold3': ('AlphaFold 3 全分子結構預測', 'Nature'),
    '2024-fault-tolerant-quantum': ('中性原子邏輯量子處理器', 'Nature'),
    '2024-sora-world-simulator': ('Sora 與世界模型', 'arXiv'),
    '2025-deepseek-r1': ('DeepSeek-R1 推理擴展', 'arXiv / Nature'),
    '2025-nerve-mito-cancer': ('神經元向癌細胞轉移粒線體', 'Nature'),
}
FSHORT = {
    '2019-generalized-data-augmentation-xia': ('低資源翻譯之泛化資料增強', 'ACL 2019'),
    '2021-seediq-chinese-mt-you': ('賽德克語－中文機器翻譯', '海大碩士論文'),
    '2022-formosan-say-verbs-hsieh': ('南島語「說」動詞語義', '臺灣語文研究'),
    '2023-atayal-truku-morphology-dai': ('泰雅與太魯閣構詞自動解析', '海大碩士論文'),
    '2023-atayalic-multilingual-mt-liao': ('泛泰雅語群多語言機器翻譯', '海大碩士論文'),
    '2023-low-resource-nmt-survey-ranathunga': ('低資源神經機器翻譯綜述', 'ACM Computing Surveys'),
    '2024-finnish-northern-sami-mt-saleva': ('芬蘭語至北薩米語翻譯', 'Findings of ACL'),
    '2024-formosan-mt-bilingual-lexicon-zheng': ('以雙語詞彙改善南島語翻譯', 'Findings of ACL'),
    '2024-formosan-temporal-words-lim': ('南島語時間詞跨語言比較', '台灣學誌'),
    '2024-taiwanese-mt-resegmentation-tang': ('以重斷詞改善台語翻譯', '海大碩士論文'),
    '2025-atayalic-affix-mt-jin': ('以詞綴資訊提升泛泰雅翻譯', '海大碩士論文'),
    '2025-atayalic-oov-enumeration-yang': ('構詞規則窮舉解決未知詞', '海大碩士論文'),
    '2025-formosanbench-llm-benchmark-lin': ('FormosanBench 南島語評測', 'Findings of EMNLP'),
    '2025-fragment-shot-reasoning-mt-frontull': ('以推理補償數據', 'arXiv'),
    '2025-indigenous-tek-ai-revitalization-wang': ('默會知識蒸餾與文化復振', 'Social Sciences'),
    '2025-manchu-in-context-mt-pei': ('滿語上下文機器翻譯', 'ACL'),
    '2025-paiwan-bunun-morphology-mt-wu': ('排灣、布農構詞分析與翻譯', '海大碩士論文'),
    '2025-tulun-adaptable-lrl-mt-merx': ('TULUN 可自適應翻譯系統', 'ACL Demo'),
    '2026-context-volume-rag-domain-shift-setiawan': ('語境容量與領域偏移', 'LoResMT'),
    '2026-data-centric-russian-kyrgyz-mt-novokshanov': ('俄語至吉爾吉斯語翻譯', 'LoResMT'),
    '2026-epark-formosan-dialectometry-gagnier': ('族語 E 樂園方言計量', 'DialRes'),
    '2026-formosanmt-parallel-corpus-scheppat': ('FormosanMT 平行語料庫', 'LREC'),
    '2026-hybrid-dictionary-rag-llm-paiwan-wang': ('辭典、RAG 與大模型翻譯', 'Engineering Proceedings'),
    '2026-tao-filipino-nmt-macayan': ('達悟語－菲律賓語翻譯', 'LoResMT'),
}
TYPE = {'2023-low-resource-nmt-survey-ranathunga': '綜述', '2025-indigenous-tek-ai-revitalization-wang': '文化復振'}
ROLES = [['senior-thesis', '學長姐論文'], ['report', '報告題材'], ['taiwan-linguistics', '臺灣語言學'], ['international', '國際文獻'], ['llm-assisted', '大模型輔助']]
NUM = {2: '二', 3: '三', 4: '四', 5: '五'}


def pol(a, r, c=(500, 500)):
    t = math.radians(a)
    return [c[0] + r * math.cos(t), c[1] + r * math.sin(t)]


def ang(x, y, c=(500, 500)):
    return math.degrees(math.atan2(y - c[1], x - c[0])) % 360


def cmean(angles):
    sx = sum(math.cos(math.radians(a)) for a in angles)
    sy = sum(math.sin(math.radians(a)) for a in angles)
    return math.degrees(math.atan2(sy, sx)) % 360


def award_line(f):
    h = f.get('honor', '')
    if h and '諾貝爾' in h:
        return f"{f['award_year']} 諾貝爾獎"
    if h:
        return h.split('（')[0]
    return None


def relax(pos, keys, mind, rmin, rmax, iters, step=0.5, rfix=None):
    for _ in range(iters):
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                dx = pos[a][0] - pos[b][0]; dy = pos[a][1] - pos[b][1]; d = math.hypot(dx, dy) or 1
                if d < mind:
                    m = (mind - d) / 2 * step
                    pos[a][0] += dx / d * m; pos[a][1] += dy / d * m
                    pos[b][0] -= dx / d * m; pos[b][1] -= dy / d * m
        for s in keys:
            a = ang(*pos[s]); r = math.hypot(pos[s][0] - 500, pos[s][1] - 500)
            r = rfix if rfix else min(max(r, rmin), rmax)
            pos[s] = pol(a, r)
            pos[s][0] = min(max(pos[s][0], 40), 960); pos[s][1] = min(max(pos[s][1], 40), 960)


# ---------- stars ----------
ms = {s: f for s, f in P.items() if f.get('my_focus') != 'true'}
for k, d in DOM.items():
    d['hub'] = [round(v) for v in pol(d['ang'], 210)]
tags = {}
for k, order in TAGORDER.items():
    n = len(order)
    for i, t in enumerate(order):
        a = DOM[k]['ang'] + (i - (n - 1) / 2) * 11
        tags[t] = {'d': k, 'a': a, 'xy': pol(a, 345)}
used = {t for f in ms.values() for t in f['domain_tags']}
assert used <= set(tags), used - set(tags)
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
    short, vshort = SHORT[s]
    papers.append(dict(slug=s, short=short, title=f['title'], titleZh=f['title_zh'], d=f['domain'], tags=f['domain_tags'],
                       p=int(f['paper_year']), a=int(f['award_year']), award=award_line(f), venue=f['venue'], venueShort=vshort,
                       hook=f.get('hook', ''), authors=f['authors'], doi=f.get('doi_url', ''), concepts=f['concepts'],
                       x=round(pos[s][0]), y=round(pos[s][1])))
cpos = {}
for s, f in C.items():
    ps = [p for p in f['papers'] if p in ms]
    if ps:
        cpos[s] = pol(cmean([ang(*pos[p]) for p in ps]), 120)
relax(cpos, sorted(cpos), 64, 0, 0, 300, step=0.25, rfix=120)
concepts = [dict(slug=s, name=C[s]['title_zh'], d=C[s]['domain'], papers=[p for p in C[s]['papers'] if p in ms],
                 x=round(cpos[s][0]), y=round(cpos[s][1])) for s in sorted(cpos)]
planned = {k: 0 for k in DOM}
TAG2DOM = {'#化學合成': 'chem', '#材料科學': 'chem', '#清潔能源': 'chem', '#量子物理': 'physics', '#免疫學': 'bio', '#生物科技': 'bio',
           '#農業科技': 'bio', '#古人類學': 'bio', '#基因工程': 'bio', '#分子生物': 'bio'}
for l in open(os.path.join(WIKI, 'index.md'), encoding='utf-8'):
    m = re.search(r'`(#[^`]+)`', l)
    if l.startswith('* `') and '[planned]' in l and m:
        planned[TAG2DOM[m.group(1)]] += 1
for k in DOM:
    DOM[k]['count'] = sum(1 for p in papers if p['d'] == k)
    DOM[k]['planned'] = planned[k]
    DOM[k]['tags'] = [t for t in TAGORDER.get(k, []) if t in used]

# ---------- focus ----------
fp = {s: f for s, f in P.items() if f.get('my_focus') == 'true'}
CON = {'formosan-computational-linguistics': 'F', 'low-resource-machine-translation': 'L'}
years = sorted({int(f['paper_year']) for f in fp.values()} | {2017})
ROWY = {y: 250 + i * 110 for i, y in enumerate(years)}
ZONE = {'F': 190, 'B': 500, 'L': 800}
rows = {}
for s, f in fp.items():
    con = [CON[c] for c in f['concepts']]
    z = 'B' if len(con) == 2 else con[0]
    rows.setdefault((int(f['paper_year']), z), []).append(s)
ANC = [dict(slug='2017-attention-is-all-you-need', short='Attention', year=2017),
       dict(slug='2025-deepseek-r1', short='DeepSeek-R1', year=2025)]
for a in ANC:
    rows.setdefault((a['year'], 'L'), []).append('ANC:' + a['slug'])
fpos = {}
for (y, z), ss in rows.items():
    ss.sort(key=lambda s: (s.startswith('ANC:'), s))
    n = len(ss); sp = 86 if n <= 3 else 78
    for i, s in enumerate(ss):
        x = ZONE[z] + (i - (n - 1) / 2) * sp + (20 if z == 'L' and n > 3 else 0)
        fpos[s] = [round(min(max(x, 50), 955)), ROWY[y] + ((8 if i % 2 else -8) if n > 1 else 0)]


def langs_display(L, s):
    if not L:
        return TYPE.get(s, '綜述'), '研究類型'
    if len(L) == 1:
        return L[0], '研究語言'
    if len(L) == 2 and all(x.endswith('語') for x in L):
        return L[0][:-1] + '・' + L[1], '研究語言'
    return f"{L[0]}等{NUM.get(len(L), len(L))}語", '研究語言'


focus = []
for s, f in sorted(fp.items(), key=lambda kv: (int(kv[1]['paper_year']), kv[0])):
    short, vshort = FSHORT[s]
    disp, lab = langs_display(f['focus_languages'], s)
    focus.append(dict(slug=s, short=short, title=f['title'], titleZh=f['title_zh'], d=f['domain'], tags=f['domain_tags'],
                      year=int(f['paper_year']), role=f['focus_role'], langs=f['focus_languages'], langDisp=disp, langLabel=lab,
                      con=[CON[c] for c in f['concepts']], venue=f['venue'], venueShort=vshort, hook=f.get('hook', ''),
                      authors=f['authors'], doi=f.get('doi_url', ''), x=fpos[s][0], y=fpos[s][1]))
for a in ANC:
    a['x'], a['y'] = fpos['ANC:' + a['slug']]
out = dict(dom=DOM, order=['bio', 'ai', 'physics', 'econ', 'chem', 'human'],
           tags={t: dict(d=v['d'], x=round(v['xy'][0]), y=round(v['xy'][1])) for t, v in tags.items() if t in used},
           papers=papers, concepts=concepts, focus=focus, roles=ROLES, ancestors=ANC,
           rowY={str(k): v for k, v in ROWY.items()},
           fhubs={'F': dict(name='臺灣南島語', full='臺灣南島語計算語言學與構詞解析', x=190, y=70),
                  'L': dict(name='低資源翻譯', full='低資源神經機器翻譯與檢索增強生成', x=810, y=70)},
           thesis=dict(x=500, y=ROWY[max(years)] + 120), focusH=ROWY[max(years)] + 200)
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('papers', len(papers), 'concepts', len(concepts), 'focus', len(focus), 'tags', len(out['tags']))
print({k: (v['count'], v['planned']) for k, v in DOM.items()})
for p in papers:
    print(f"{p['short'][:14]:16} {p['d']:8} {p['x']:4} {p['y']:4}")
for c in concepts:
    print('C', c['name'][:10], c['x'], c['y'])
print('thesis', out['thesis'], 'H', out['focusH'], 'rows', ROWY)
for f in focus:
    print(f"F {f['short'][:12]:14} {f['role']:18} {f['langDisp']:10} {f['x']:4} {f['y']:4}")
print('anc', ANC)
