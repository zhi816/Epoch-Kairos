"""建置論文頁參考原型 web/prototypes/paper-v1/<slug>.html。

用法（於倉庫根目錄執行）：
    python tools/build_paper_prototype.py               # 為所有已有卡片檔的論文建置
    python tools/build_paper_prototype.py <slug> ...    # 只建置指定論文

這是「卡片檔寫成什麼樣、網頁就長什麼樣」的參考原型，供各代理撰寫卡片時對照：
    * 版面：DESIGN.md 第五章「論文頁 F」（窄導軌、卡片欄、長文、資訊欄；卡片與長文捲動同步）。
    * 卡片：Card 1 封面依 DESIGN.md 第二章第 3 節；Card 2 至 6 為卡組丁（學科色底、深色重點色）。
    * 內容：卡片取自 wiki/cards/<slug>.md（paper-card-writer），長文取自 wiki/papers/<slug>.md 之 Card 1 至 6 段落，
      資訊欄取自 Frontmatter 與概念頁。公式以 KaTeX 渲染。
建置前先以 paper-card-writer 之 check_cards.py 檢查卡片檔，有 ERROR 即不產生。
正式之論文頁建置見 wiki/todo.md TD-002；本腳本只用 Python 標準函式庫。
"""
import glob
import html
import importlib.util
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
WIKI = os.path.join(ROOT, 'wiki')
TEMPLATE = os.path.join(ROOT, 'tools', 'paper_template.html')
OUTDIR = os.path.join(ROOT, 'web', 'prototypes', 'paper-v1')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


home = load('build_home', os.path.join(ROOT, 'tools', 'build_home.py'))
cc = load('check_cards', os.path.join(ROOT, '.agents', 'skills', 'paper-card-writer', 'scripts', 'check_cards.py'))

DOMAIN = {k: dict(short=s, full=f, shape=p) for k, s, f, _a, p in home.DOMAINS}
ROLE = dict(home.ROLES)
# 星光色以 web/assets/css/theme.css 之 --color-<domain> 為準；深色重點色尚未寫入 theme.css，
# 暫依 DESIGN.md 第七章色表（實作正式論文頁時改讀 --deep-<domain>）。
DEEP = {'bio': '#1A4F2C', 'ai': '#204960', 'physics': '#4D2E8B', 'econ': '#53401C', 'chem': '#693123', 'human': '#6D244D'}
FOCUS = {'human': '#F2B3D6'}            # 我的關注封面之重點色：藍，human 用玫瑰粉（DESIGN.md 第二章第 3 節）
FOCUS_DEFAULT = '#8FD5FD'
CARD_NAMES = ['時代銘文', '世紀瓶頸', '突破原理', '決定性數據', '典範轉移', 'Kairos']
VERIFY_TEXT = {'verified': '已逐項對照原文查核'}   # 其餘狀態之文字待定（DESIGN.md 第八章第 15 項）


def star_colors():
    css = open(os.path.join(ROOT, 'web', 'assets', 'css', 'theme.css'), encoding='utf-8').read()
    return {k: re.search(r'--color-%s:\s*(#[0-9A-Fa-f]{6})' % k, css).group(1) for k in DOMAIN}


def esc(s):
    return html.escape(str(s), quote=True)


def mix(hex1, hex2, k):
    a = [int(hex1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(hex2[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02X%02X%02X' % tuple(round(x + (y - x) * k) for x, y in zip(b, a))


def rnd(seed):
    s = [seed & 0xFFFFFFFF]

    def r():
        s[0] = (s[0] + 0x6D2B79F5) & 0xFFFFFFFF
        t = s[0]
        t = ((t ^ (t >> 15)) * (1 | t)) & 0xFFFFFFFF
        t = (t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return r


# ---------------------------------------------------------------- 行內文字與 Markdown

MATH = re.compile(r'(\$\$.+?\$\$|\$(?:\\.|[^$\\\n])+?\$)')


def text_fmt(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)

    def link(m):
        label, url = m.group(1), m.group(2)
        if url.startswith('http'):
            return '<a href="%s">%s</a>' % (html.escape(url, quote=True), label)
        return label
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*(?![\s*])(.+?)(?<![\s*])\*(?!\*)', r'<em>\1</em>', t)
    return t


def inline(s):
    # 公式先換成佔位符，整段轉完粗體、斜體與連結再放回：若逐段轉換，
    # 「**容量（$0.15N$ 近似上限）**」之粗體頭尾分落公式兩側而配不起來，網頁會露出 **
    maths = []

    def keep(m):
        part = m.group(0)
        if part.startswith('$$'):
            maths.append('<span class="m-disp" data-tex="%s"></span>' % esc(part[2:-2].strip()))
        else:
            maths.append('<span class="m-in" data-tex="%s"></span>' % esc(part[1:-1]))
        return '\x00%d\x00' % (len(maths) - 1)
    t = text_fmt(MATH.sub(keep, s))
    return re.sub(r'\x00(\d+)\x00', lambda m: maths[int(m.group(1))], t)


LIST = re.compile(r'^(\s*)([*-]|\d+\.)\s+(.*)$')


def render_list(items):
    """items：[(indent, ordered, html)]，依縮排組成巢狀清單。"""
    out, stack = [], []
    for ind, ordered, body in items:
        while stack and ind < stack[-1][0]:
            out.append('</li></%s>' % stack.pop()[1])
        if stack and ind == stack[-1][0]:
            out.append('</li><li>' + body)
        else:
            tag = 'ol' if ordered else 'ul'
            stack.append((ind, tag))
            out.append('<%s><li>%s' % (tag, body))
    while stack:
        out.append('</li></%s>' % stack.pop()[1])
    return ''.join(out)


def markdown(lines):
    """只處理 Wiki 論文頁實際用到的語法：段落、###、清單、引言、表格、程式碼區塊、區塊公式。"""
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s or s == '---':
            i += 1
            continue
        if s.startswith('```'):
            j = i + 1
            buf = []
            while j < n and not lines[j].strip().startswith('```'):
                buf.append(lines[j])
                j += 1
            out.append('<pre>%s</pre>' % html.escape('\n'.join(buf), quote=False))
            i = j + 1
            continue
        if s.startswith('$$'):
            buf, j = [s], i
            if not (s.count('$$') >= 2 and s.endswith('$$')):
                while j + 1 < n:
                    j += 1
                    buf.append(lines[j].strip())
                    if lines[j].strip().endswith('$$'):
                        break
            tex = '\n'.join(buf).strip()[2:-2].strip()
            out.append('<span class="m-disp" data-tex="%s"></span>' % esc(tex))
            i = j + 1
            continue
        if s.startswith('### '):
            out.append('<h3>%s</h3>' % inline(s[4:]))
            i += 1
            continue
        if s.startswith('>'):
            buf = []
            while i < n and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append('<blockquote>%s</blockquote>' % inline(' '.join(b for b in buf if b)))
            continue
        if s.startswith('|'):
            rows = []
            while i < n and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            head = ''.join('<th>%s</th>' % inline(c) for c in rows[0])
            body = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in rows[1:])
            out.append('<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (head, body))
            continue
        m = LIST.match(line)
        if m:
            items = []
            while i < n:
                m = LIST.match(lines[i])
                if m:
                    items.append([len(m.group(1)), m.group(2)[0].isdigit(), inline(m.group(3))])
                    i += 1
                elif lines[i].strip() and lines[i].startswith(' ') and items:
                    items[-1][2] += ' ' + inline(lines[i].strip())
                    i += 1
                else:
                    break
            out.append(render_list(items))
            continue
        buf = []
        while i < n and lines[i].strip() and not LIST.match(lines[i]) and not lines[i].strip()[:1] in ('>', '|', '#') \
                and not lines[i].strip().startswith(('```', '$$', '---')):
            buf.append(lines[i].strip())
            i += 1
        out.append('<p>%s</p>' % inline(''.join(buf)))
    return '\n'.join(out)


# ---------------------------------------------------------------- 卡片

def card_fields(path, slug):
    header, sections, order, svg = cc.parse_card(path, slug)
    f = {}
    for sec, fields in sections.items():
        for key, value, _ln in fields:
            f.setdefault((sec, key), []).append(value)
    return f, svg[0] if svg else ''


def one(f, sec, key):
    return (f.get((sec, key)) or [''])[0]


def card_inline(s):
    out = []
    for part in re.split(r'(\$[^$]+\$)', s):
        if len(part) > 2 and part.startswith('$') and part.endswith('$'):
            out.append('<span class="m-in" data-tex="%s"></span>' % esc(part[1:-1]))
        else:
            out.append(esc(part))
    return ''.join(out)


def wrap(name, inner, cls=''):
    return ('      <section class="card%s" data-name="%s" aria-label="%s" aria-hidden="true">'
            '<div class="in">%s</div></section>') % (cls, esc(name), esc(name), inner)


def cover(fm, f, no, colors):
    d = fm['domain']
    focus = fm.get('my_focus') is True
    r = rnd(int(fm['paper_year']) * 7919 + len(fm['card_line']))
    stars = ''.join('<i style="left:%.1f%%;top:%.1f%%;width:%spx;height:%spx;opacity:%.2f"></i>'
                    % (4 + r() * 92, 4 + r() * 42, sz, sz, 0.3 + r() * 0.55)
                    for sz in [1 if r() < 0.8 else 1.5 for _ in range(14)])
    lines = ''.join('<span>%s</span>' % esc(x) for x in one(f, '封面', '封面斷行').split('／'))
    head_right = ROLE.get(fm.get('focus_role'), '') if focus else DOMAIN[d]['short']
    if focus:
        langs = fm.get('focus_languages') or []
        tag = '、'.join(langs) if langs else one(f, '封面', '研究類型')
        win_extra = '<span class="lang">%s</span>' % esc(tag)
        rep = '<span class="rep"></span>'
    else:
        win_extra = ''
        rep = '<span class="rep%s"></span>' % (' award' if fm.get('honor') else '')
    title = one(f, '封面', '封面標題') or home.short_name(fm['title_zh'])
    tags = '%s・%s' % (DOMAIN[d]['full'], ' '.join(fm.get('domain_tags') or []))
    inner = ('<div class="ph"><span>%s</span><span>%s</span></div>'
             '<div class="win">%s%s%s<span class="line">%s</span></div>'
             '<div class="tags">%s</div><div class="name">%s</div><div class="lead">%s</div><div class="yrs">%s</div>') % (
        esc(no), esc(head_right), stars, win_extra, rep, lines, esc(tags), esc(title),
        esc(one(f, '封面', '導語')), esc(years_full(fm)))
    return wrap(CARD_NAMES[0], inner, ' cover' + (' focus' if focus else ''))


def card2(f):
    s = 'Card 2｜世紀瓶頸'
    rows = ''.join('<div class="row"><b>%s</b><span>%s</span></div>' % tuple(esc(x) for x in v.split('｜'))
                   for v in f.get((s, '對照'), []))
    rows += ''.join('<div class="row gap"><b>%s</b><span>%s</span></div>' % tuple(esc(x) for x in v.split('｜'))
                    for v in f.get((s, '缺口'), []))
    inner = '<span class="kc">02 ｜ 世紀瓶頸</span><span class="hd">%s</span><div class="rows">%s</div><span class="ft" style="color:var(--ink)">%s</span>' % (
        esc(one(f, s, '標題')), rows, esc(one(f, s, '結語')))
    return wrap(CARD_NAMES[1], inner)


def card3(f, svg):
    s = 'Card 3｜突破原理'
    svg = re.sub(r'^<svg ', '<svg class="dia" ', svg.strip())
    inner = ('<span class="kc">03 ｜ 突破原理</span><span class="hd">%s</span>%s'
             '<div class="fbox"><span class="m-disp" data-tex="%s"></span></div>'
             '<span class="tx" style="margin-top:auto;color:var(--ink2)">%s</span>') % (
        esc(one(f, s, '標題')), svg, esc(one(f, s, '公式')), card_inline(one(f, s, '說明')))
    return wrap(CARD_NAMES[2], inner)


def card4(f):
    s = 'Card 4｜決定性數據'
    if one(f, s, '模式') == '數字':
        items = [v.split('｜') for v in f.get((s, '數字'), [])]
        body = '<div class="stats%s">%s</div>' % ('' if len(items) == 4 else ' two', ''.join(
            '<div class="stat"><span class="v">%s</span><span class="l">%s</span></div>' % (card_inline(v), card_inline(l))
            for v, l, _src in items))
    else:
        body = '<div class="concl">%s</div>' % ''.join('<p>%s</p>' % card_inline(v.split('｜')[0]) for v in f.get((s, '結論'), []))
    inner = '<span class="kc">04 ｜ 決定性數據</span>%s<span class="ft">範圍：%s</span>' % (body, esc(one(f, s, '範圍')))
    return wrap(CARD_NAMES[3], inner)


def card5(f):
    s = 'Card 5｜典範轉移'
    items = ''.join('<p><b>%s</b><span>%s</span></p>' % (esc(y), esc(t))
                    for y, t, _src in (v.split('｜') for v in f.get((s, '里程碑'), [])))
    inner = '<span class="kc">05 ｜ 典範轉移</span><span class="hd">%s</span><div class="time">%s</div><span class="ft">%s</span>' % (
        esc(one(f, s, '標題')), items, esc(one(f, s, '註記')))
    return wrap(CARD_NAMES[4], inner)


def card6(f):
    s = 'Card 6｜Kairos'
    a, b = one(f, s, '轉變').split('→')
    inner = ('<span class="kc">06 ｜ KAIROS</span><span class="quote">%s</span>'
             '<span class="shift"><span>%s</span><i aria-hidden="true"></i><b>%s</b></span>') % (
        esc(one(f, s, '結語')), esc(a), esc(b))
    return wrap(CARD_NAMES[5], inner)


# ---------------------------------------------------------------- 長文與資訊欄

def article(fm, body):
    lines = body.split('\n')
    pre, sections, cur = [], [], None
    for line in lines:
        m = re.match(r'^## Card (\d)\s*｜\s*(.+?)\s*(\([^)]*\))?\s*$', line)
        if m:
            cur = [int(m.group(1)), m.group(2), []]
            sections.append(cur)
            continue
        if line.startswith('## '):
            cur = None
            if sections:
                break
            continue
        if cur is None:
            if not sections:
                pre.append(line)
        else:
            cur[2].append(line)
    epigraph, scope, rest = pre_blocks(pre)
    head = ['<header>', '<span class="kicker">%s</span>' % esc(years_full(fm)),
            '<h1>%s</h1>' % esc(fm['title_zh']), '<p class="en">%s</p>' % esc(fm['title'])]
    if rest:
        head.append(markdown(rest))
    head.append('</header>')
    out = ['\n'.join(head)]
    for k, (num, name, body_lines) in enumerate(sections):
        # 樣稿「論文頁 F」：論文頁開頭之引言（> 「……」）不放在標題下，改為 01 時代銘文之第一段，去掉引號
        lead = ''
        if k == 0 and epigraph:
            lead = '<p class="epigraph">%s%s</p>\n' % (
                inline(epigraph[0]), '<span class="src">%s</span>' % inline(epigraph[1]) if epigraph[1] else '')
        out.append('<section data-card="%d"><div class="sh"><span class="num" aria-hidden="true">%02d</span><h2>%s</h2></div>\n%s%s\n</section>'
                   % (num, num, esc(name), lead, markdown(body_lines)))
    return '\n'.join(out), scope


def pre_blocks(pre):
    """把論文頁第一個 Card 段落之前的內容分成：引言、本頁範圍說明、其餘。

    引言為開頭以「 起頭之引用區塊；本頁範圍說明為以 **本頁範圍 起頭之引用區塊（AGENTS.md 第七章第 1 節
    「單篇頁容納多篇工作之原則」），改放資訊欄，不得刪除。標題行（# ）與雙年份行（**…發表…**）由頁首另行產生，略過。
    其餘內容原樣留在頁首，以免漏掉。"""
    blocks, cur = [], []
    for ln in pre + ['']:
        if ln.strip():
            cur.append(ln)
        elif cur:
            blocks.append(cur)
            cur = []
    epigraph, scope, rest = '', '', []
    for b in blocks:
        s = b[0].strip()
        if s.startswith('# ') or (s.startswith('**') and '發表' in s and len(b) == 1):
            continue
        if all(x.lstrip().startswith('>') for x in b):
            text = ' '.join(re.sub(r'^\s*>\s?', '', x).strip() for x in b).strip()
            if text.startswith('「') and not epigraph:
                # 去掉引號；引號後之出處註記（如「（本頁引言為 Wiki 撰寫，非原文）」）不可丟，另以小字保留
                m = re.match(r'^「(.*)」\s*(.*)$', text)
                epigraph = (m.group(1), m.group(2)) if m else (text, '')
                continue
            m = re.match(r'^\*\*本頁範圍(?:說明)?\*\*\s*[：:]\s*(.*)$', text)
            if m and not scope:
                scope = m.group(1)
                continue
        rest += b + ['']
    return epigraph, scope, rest


def years_full(fm):
    """論文頁之雙年份（Card 1 底部與長文頂部）：獎項寫全名，如「1982 發表 ｜ 2024 諾貝爾物理學獎」（樣稿「論文頁 F」，
    2026-11-09 使用者確認）。首頁卡片仍用 build_home.years_line 之簡稱「2024 諾貝爾獎」。未獲獎者為期刊或會議簡稱。"""
    honor = str(fm.get('honor') or '').split('（')[0].strip()
    if honor and not re.match(r'^\d{4}\s', honor):
        honor = '%s %s' % (fm['award_year'], honor)
    return '%s 發表 ｜ %s' % (fm['paper_year'], honor or home.venue_of(fm))


def side(fm, concepts, scope=''):
    venue = home.venue_of(fm)
    parts = ['<div class="blk"><div class="yr"><b>%s</b><span>發表・%s</span></div>' % (fm['paper_year'], esc(venue))]
    if fm.get('honor'):
        honor = re.sub(r'^\d{4}\s*', '', str(fm['honor']).split('（')[0].strip())
        parts.append('<div class="yr award"><b>%s</b><span>%s</span></div>' % (fm['award_year'], esc(honor)))
    parts.append('</div>')
    authors = [a.strip() for a in str(fm.get('authors', '')).split(',') if a.strip()]
    parts.append('<div class="blk"><span class="lab">作者</span><span>%s</span></div>' % '<br>'.join(esc(a) for a in authors))
    if fm.get('laureates'):
        laur = [a.strip() for a in str(fm['laureates']).split(',') if a.strip()]
        others = [a for a in laur if a not in authors]
        note = '<span class="note">%s 並非本篇作者；獎項表彰一系列工作。</span>' % esc('、'.join(a.split()[-1] for a in others)) if others else ''
        parts.append('<div class="blk"><span class="lab">得獎者</span><span>%s</span>%s</div>' % ('<br>'.join(esc(a) for a in laur), note))
    if fm.get('my_focus') is True:
        langs = fm.get('focus_languages') or []
        parts.append('<div class="blk"><span class="lab">我的關注</span><span>%s</span>%s</div>' % (
            esc(ROLE.get(fm.get('focus_role'), '')), '<span class="note">研究語言：%s</span>' % esc('、'.join(langs)) if langs else ''))
    doi = fm.get('doi_url') or ''
    parts.append('<div class="blk"><span class="lab">期刊</span><span>%s</span>%s</div>' % (
        esc(fm['venue']), '<a href="%s">%s</a>' % (esc(doi), esc(doi.replace('https://doi.org/', 'doi:'))) if doi else ''))
    parts.append('<div class="blk"><span class="lab">標籤</span><div class="chips">%s</div></div>' % ''.join(
        '<span class="chip">%s</span>' % esc(t) for t in fm.get('domain_tags') or []))
    if concepts:
        parts.append('<div class="blk"><span class="lab">關聯概念</span>%s</div>' % ''.join(
            '<span class="con"><svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M5 0.6 L9.4 5 L5 9.4 L0.6 5 Z" fill="none" stroke="#B5B0A6"/></svg>%s</span>' % esc(c)
            for c in concepts))
    keys = fm.get('key_papers') or []
    if keys:
        items = []
        for k, label in zip(keys, key_labels(keys)):
            m = re.search(r'(https?://\S+)', k)
            full = re.sub(r'\s*https?://\S+', '', k).strip()
            items.append('<a href="%s" title="%s">%s</a>' % (esc(m.group(1)), esc(full), esc(label)) if m
                         else '<span title="%s">%s</span>' % (esc(full), esc(label)))
        parts.append('<div class="blk"><span class="lab">奠基論文</span>%s</div>' % ''.join(items))
    if scope:
        # 論文頁之「本頁範圍說明」：樣稿長文開頭不放，移到此處保留（說明本頁與獎項、奠基論文之關係）
        parts.append('<div class="blk"><span class="lab">本頁範圍</span><span class="note">%s</span></div>' % inline(scope))
    v = fm.get('verification', '')
    parts.append('<div class="blk"><span class="lab">核實狀態</span><span class="ok">%s%s</span></div>' % (
        '<i aria-hidden="true"></i>' if v == 'verified' else '', esc(VERIFY_TEXT.get(v, '查核狀態：%s（顯示文字待定）' % v))))
    return '\n'.join('    ' + p for p in parts)


INITIALS = re.compile(r'^(?:[^\W\d_]\.[\s-]?)+$')   # 名字縮寫：J. J.、W.-Y.、Ł.


def key_labels(keys):
    """資訊欄奠基論文之顯示文字：「姓氏（年份）」，如「Hopfield（1982）」「Ackley、Hinton 與 Sejnowski（1985）」「Nagel 等（2003）」
    （DESIGN.md 第五章第 1 節，2026-11-09 定案）。不顯示期刊：key_papers 為自由格式，期刊名無法可靠擷取，寧缺勿錯；
    完整書目放在滑過提示。作者寫法依 paper-card-writer 之 style.md 第二節第 3 條。同頁同名同年者加 a、b。
    擷取不到年份或姓氏時，退回顯示完整書目。"""
    out = []
    for k in keys:
        text = re.sub(r'\s*https?://\S+', '', k).strip()
        m = re.search(r'\((\d{4})\)', text)
        authors = re.sub(r'\([^)]*\)', '', text[:m.start()]) if m else ''
        etal = bool(re.search(r'\bet al\.?', authors))
        authors = re.sub(r'\bet al\.?', '', authors).replace('&', ',')
        names = [p.strip() for p in authors.split(',') if p.strip() and not INITIALS.match(p.strip())]
        if not (m and names):
            out.append([text, None])
            continue
        if etal or len(names) >= 4:
            who = names[0] + ' 等'
        elif len(names) == 3:
            who = '%s、%s 與 %s' % tuple(names)
        elif len(names) == 2:
            who = '%s 與 %s' % tuple(names)
        else:
            who = names[0]
        out.append([who, m.group(1)])
    orig = [tuple(x) for x in out]
    for i, (who, year) in enumerate(orig):
        same = [j for j, wy in enumerate(orig) if year and wy == (who, year)]
        if len(same) > 1:
            out[i][1] = year + 'abcdefgh'[same.index(i)]
    return [who if year is None else '%s（%s）' % (who, year) for who, year in out]


# ---------------------------------------------------------------- 主程式

def numbering(papers):
    """卡片編號：群星與我的關注各自依 timeline_year 由新到舊、同年依 slug 排序（暫定，首頁卡片牆實作時統一）。"""
    out = {}
    for focus, prefix in ((False, 'No.'), (True, 'F.')):
        group = sorted((s for s, f in papers.items() if (f.get('my_focus') is True) == focus),
                       key=lambda s: (-int(papers[s]['timeline_year']), s))
        for i, s in enumerate(group):
            out[s] = '%s%02d' % (prefix, i + 1)
    return out


def build(slug, papers, concepts_zh, colors, tpl, nums):
    card_path = os.path.join(WIKI, 'cards', slug + '.md')
    cc.results.clear()
    cc.check_card(card_path, slug, {})
    errs = [r for r in cc.results if r[0] == 'ERROR']
    if errs:
        for r in errs:
            print('ERROR %s:%s  %s' % (r[1], r[2], r[3]))
        print('略過 %s：卡片檔有 ERROR，請先修正' % slug)
        return False
    fm = papers[slug]
    text = open(os.path.join(WIKI, 'papers', slug + '.md'), encoding='utf-8').read()
    body = re.split(r'^---\s*$', text, maxsplit=2, flags=re.M)[2]
    f, svg = card_fields(card_path, slug)
    d = fm['domain']
    star = colors[d]
    focus_c = FOCUS.get(d, FOCUS_DEFAULT)
    vars_ = '--star:%s;--deep:%s;--win:%s;--focus:%s' % (star, DEEP[d], mix(star, '#0F1114', 0.1), focus_c)
    cards = '\n'.join([cover(fm, f, nums[slug], colors), card2(f), card3(f, svg), card4(f), card5(f), card6(f)])
    art, scope = article(fm, body)
    page = (tpl.replace('{{PAGE_TITLE}}', esc(home.short_name(fm['title_zh'])))
            .replace('{{VARS}}', vars_)
            .replace('{{BACK}}', '../../index.html' + ('#my-constellation' if fm.get('my_focus') is True else ''))
            .replace('{{CARDS}}', cards)
            .replace('{{ARTICLE}}', art)
            .replace('{{SIDE}}', side(fm, [concepts_zh[c] for c in fm.get('concepts') or [] if c in concepts_zh], scope)))
    os.makedirs(OUTDIR, exist_ok=True)
    out = os.path.join(OUTDIR, slug + '.html')
    with open(out, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(page)
    print('已產生 %s' % os.path.relpath(out, ROOT))
    return selfcheck(slug, page, fm, body)


# ---------------------------------------------------------------- 產生後自我檢查

VENUE_LINE_MAX = 17   # 資訊欄「發表・期刊」約每行 8.5 字寬（1440 x 900 實測），超過兩行即提示補 venue_short


def selfcheck(slug, page, fm, body):
    """檢查產生的網頁有沒有把論文頁或卡片檔轉壞（paper-card-writer 第五節第 7 步）。
    只做靜態檢查；公式能否渲染、卡片有沒有溢出，須另以瀏覽器執行 verify_page.js。ERROR 時回傳 False。"""
    issues = []

    def add(level, msg):
        issues.append((level, msg))
    visible = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', '', page, flags=re.S)
    visible = html.unescape(re.sub(r'<[^>]+>', ' ', visible))
    if '\x00' in page:
        add('ERROR', '網頁殘留公式佔位符（\\x00）：build_paper_prototype.py 之 inline() 出錯')
    if '**' in visible:
        add('ERROR', '網頁露出 **：論文頁或卡片檔有未配對或未轉換的粗體，片段：%s' % snippet(visible, '**'))
    if '$' in visible:
        add('ERROR', '網頁露出 $：公式未轉換，或金額未依 AGENTS.md 第三章寫成「美元」，片段：%s' % snippet(visible, '$'))
    if '](' in visible:
        add('ERROR', '網頁露出 ](：Markdown 連結未轉換，片段：%s' % snippet(visible, ']('))
    if '`' in visible:
        add('WARN', '網頁露出反引號：行內程式碼未配對，片段：%s' % snippet(visible, '`'))
    if len(re.findall(r'<section class="card', page)) != 6:
        add('ERROR', '卡片不是 6 張')
    if re.findall(r'<section data-card="(\d)"', page) != list('123456'):
        add('ERROR', '長文段落不是依序之 Card 1 至 6：論文頁須有「## Card N ｜ 名稱」六段')
    for tex in re.findall(r'data-tex="([^"]*)"', page):
        if re.search('[㐀-鿿]', html.unescape(tex)):
            add('ERROR', '公式內含中文字元（AGENTS.md 第三章）：%s' % html.unescape(tex)[:60])
    pre = body.split('\n## Card 1')[0]
    if not re.search(r'^>\s*「', pre, re.M):
        add('ERROR', '論文頁標題下沒有開頭引言（> 「……」），長文 01 段將缺第一段')
    elif '<p class="epigraph">' not in page:
        add('ERROR', '論文頁有開頭引言，網頁 01 段卻沒有：引言格式須為單獨一段之 > 「……」')
    if re.search(r'^>\s*\*\*本頁範圍', pre, re.M) and '>本頁範圍</span>' not in page:
        add('ERROR', '論文頁有本頁範圍說明，網頁資訊欄卻沒有：格式須為 > **本頁範圍說明**：……')
    kicker = re.search(r'<span class="kicker">([^<]*)</span>', page)
    yrs = re.search(r'<div class="yrs">([^<]*)</div>', page)
    if not (kicker and yrs and kicker.group(1) == yrs.group(1)):
        add('ERROR', '長文頂部與 Card 1 底部之雙年份不一致')
    venue = home.venue_of(fm)
    if cc.width('發表・' + venue) > VENUE_LINE_MAX:
        add('WARN', '資訊欄「發表・%s」超過兩行：請依 paper-card-writer 之 references/paper-page.md 第三節補 venue_short' % venue)
    for level, msg in issues:
        print('%-5s %s  %s' % (level, slug, msg))
    n_err = sum(1 for lv, _m in issues if lv == 'ERROR')
    print('自我檢查 %s：ERROR %d、WARN %d' % (slug, n_err, len(issues) - n_err))
    return n_err == 0


def snippet(text, token):
    i = text.find(token)
    return re.sub(r'\s+', ' ', text[max(0, i - 20):i + 20]).strip()


def main():
    papers = {os.path.basename(p)[:-3]: home.frontmatter(p) for p in sorted(glob.glob(os.path.join(WIKI, 'papers', '*.md')))}
    concepts_zh = {os.path.basename(p)[:-3]: home.frontmatter(p).get('title_zh', '')
                   for p in glob.glob(os.path.join(WIKI, 'concepts', '*.md'))}
    slugs = sys.argv[1:] or sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(WIKI, 'cards', '*.md')))
    tpl = open(TEMPLATE, encoding='utf-8').read()
    colors, nums = star_colors(), numbering(papers)
    ok = all([build(s, papers, concepts_zh, colors, tpl, nums) for s in slugs])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
