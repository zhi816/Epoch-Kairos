#!/usr/bin/env python3
"""檢查 wiki/cards/<slug>.md 卡片文字檔是否符合 paper-card-writer 規範。

用法（於倉庫根目錄）：
    python .agents/skills/paper-card-writer/scripts/check_cards.py            # 檢查全部卡片檔
    python .agents/skills/paper-card-writer/scripts/check_cards.py <slug> ... # 只檢查指定論文
    python .agents/skills/paper-card-writer/scripts/check_cards.py --missing  # 另列出尚無卡片檔的論文

規則來源：.agents/skills/paper-card-writer/SKILL.md 與 references/。
只用 Python 標準函式庫（3.7 以上）。有 ERROR 時以代碼 1 結束。
"""
import argparse
import datetime
import glob
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
WIKI = os.path.join(ROOT, 'wiki')

SECTIONS = ['封面', 'Card 2｜世紀瓶頸', 'Card 3｜突破原理', 'Card 4｜決定性數據', 'Card 5｜典範轉移', 'Card 6｜Kairos']
SPEC = {
    '封面': [('封面斷行', 1, 1), ('導語', 1, 1), ('封面標題', 0, 1), ('研究類型', 0, 1)],
    'Card 2｜世紀瓶頸': [('標題', 1, 1), ('對照', 2, 3), ('缺口', 1, 1), ('結語', 1, 1)],
    'Card 3｜突破原理': [('標題', 1, 1), ('公式', 1, 1), ('無公式理由', 0, 1), ('說明', 1, 1), ('圖類型', 1, 1), ('圖來源', 0, 1), ('圖說', 1, 1)],
    'Card 4｜決定性數據': [('模式', 1, 1), ('數字', 0, 4), ('結論', 0, 3), ('範圍', 1, 1)],
    'Card 5｜典範轉移': [('模式', 0, 1), ('標題', 1, 1), ('里程碑', 2, 5), ('註記', 1, 1)],
    'Card 6｜Kairos': [('結語', 1, 1), ('轉變', 1, 1)],
}
HEADER_KEYS = ['論文頁', '證據表', '撰寫者', '最後核對']
MATH_OK = {('Card 3｜突破原理', '說明'), ('Card 4｜決定性數據', '數字'), ('Card 4｜決定性數據', '結論')}
NO_TEXT_CHECK = {('Card 3｜突破原理', '公式')}
SOURCE_FIELDS = {('Card 5｜典範轉移', '里程碑'), ('Card 4｜決定性數據', '數字'), ('Card 4｜決定性數據', '結論'), ('Card 3｜突破原理', '圖來源'),
                 ('Card 3｜突破原理', '無公式理由')}
# Card 3 無公式模式：「公式」填「無」，「無公式理由」以下列其一開頭（card-03-secret.md 第四節）
NO_FORMULA_REASONS = ('原文無公式：', '原文僅有評估指標公式：')
# Card 5 新論文模式只適用於發表兩年內之論文（card-05-revolution.md 第六節）
NEW_PAPER_YEARS = 2

BANNED = ['開創性', '顛覆性', '革命性', '劃時代', '史無前例', '空前', '偉大', '驚人', '震撼', '完美', '神奇', '奇蹟',
          '天才', '最強', '無敵', '終極', '必讀', '改寫人類', '改變世界']
STRONG = ['首次', '第一次', '首創', '證明', '證實', '奠基', '奠定', '導致', '徹底', '完全', '全面', '所有', '唯一',
          '解決了', '突破性', '最早', '最大', '最快']
ABBR_OK = {'AI', 'DNA', 'RNA'}
SRC_MARK = re.compile(r'(p\.|pp\.|頁|Table|Fig|表|圖|§|式|Eq|依原文)')
CJK = re.compile(r'[\u3400-\u9fff\uf900-\ufaff]')
EMOJI = re.compile('[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]')

COLOR = {'k-line', 'k-accent', 'k-ink', 'k-muted', 'k-soft'}
MODIFIER = {'k-ring', 'k-dash', 'k-thin'}
TEXT_CLASS = {'k-label', 'k-label-accent'}
CLOSED = {'circle', 'ellipse', 'rect', 'polygon'}
SVG_ATTRS = {
    'g': {'class'},
    'path': {'class', 'd'},
    'line': {'class', 'x1', 'y1', 'x2', 'y2'},
    'polyline': {'class', 'points'},
    'polygon': {'class', 'points'},
    'circle': {'class', 'cx', 'cy', 'r'},
    'ellipse': {'class', 'cx', 'cy', 'rx', 'ry'},
    'rect': {'class', 'x', 'y', 'width', 'height', 'rx'},
    'text': {'class', 'x', 'y', 'text-anchor'},
}
PATH_ARGS = {'M': 'xy', 'L': 'xy', 'T': 'xy', 'C': 'xyxyxy', 'S': 'xyxy', 'Q': 'xyxy', 'H': 'x', 'V': 'y', 'Z': ''}

results = []


def report(level, path, line, msg):
    results.append((level, os.path.relpath(path, ROOT).replace(os.sep, '/'), line, msg))


# ---------------------------------------------------------------- 共用工具

def width(s):
    """字數：全形與寬度不明確字元計 1，半形計 0.5；行內數學以原始碼字元數乘 0.5。"""
    total = 0.0
    for part in re.split(r'(\$[^$]+\$)', s):
        if len(part) > 1 and part.startswith('$') and part.endswith('$'):
            total += 0.5 * len(part[1:-1])
            continue
        for ch in part:
            total += 1 if unicodedata.east_asian_width(ch) in ('W', 'F', 'A') else 0.5
    return total


def fmt(n):
    return ('%g' % n)


def parse_value(raw):
    raw = raw.strip()
    if not raw:
        return None
    if raw[0] in '"\'':
        q = raw[0]
        end = raw.find(q, 1)
        while end != -1 and raw[end - 1] == '\\':
            end = raw.find(q, end + 1)
        return raw[1:end] if end != -1 else raw[1:]
    if raw[0] == '[':
        inner = raw[1:raw.rfind(']')].strip()
        return [s.strip().strip('"\'') for s in inner.split(',') if s.strip()] if inner else []
    raw = re.split(r'\s+#', raw, 1)[0].strip()
    if raw in ('true', 'false'):
        return raw == 'true'
    if re.fullmatch(r'-?\d+', raw):
        return int(raw)
    return raw


def frontmatter(text):
    lines = text.split('\n')
    if not lines or lines[0].strip() != '---':
        return {}
    data, key = {}, None
    for line in lines[1:]:
        if line.strip() == '---':
            return data
        m = re.match(r'^([A-Za-z_][\w-]*):(.*)$', line)
        if m:
            key = m.group(1)
            val = parse_value(m.group(2))
            data[key] = [] if val is None else val
            continue
        m = re.match(r'^\s+-\s+(.*)$', line)
        if m and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(parse_value(m.group(1)))
    return {}


def norm_tex(s):
    s = re.sub(r'\\begin\{aligned\}|\\end\{aligned\}', '', s)
    s = re.sub(r'\\(,|;|!|quad|qquad)', '', s)
    s = s.replace('&', '')
    s = re.sub(r'\s+', '', s)
    return s.rstrip('.,')


def wiki_formulas(text):
    out = set()
    for block in re.findall(r'\$\$(.+?)\$\$', text, re.S):
        out.add(norm_tex(block))
        if 'aligned' in block or '\\\\' in block:
            body = re.sub(r'\\begin\{aligned\}|\\end\{aligned\}', '', block)
            for line in body.split('\\\\'):
                if line.strip():
                    out.add(norm_tex(line))
    return out


def short_name(title_zh):
    s = re.sub(r'（[^）]*）', '', title_zh.split('：')[0]).strip()
    return s or title_zh


def plain(s):
    """去掉行內數學的 $ 與 LaTeX 指令，方便取數字。"""
    s = s.replace('$', '')
    s = re.sub(r'\\[A-Za-z]+', ' ', s)
    return s


# ---------------------------------------------------------------- 文字規則

def check_text(path, line, sec, key, value, evidence):
    where = '%s「%s」' % (sec, key)
    if EMOJI.search(value):
        report('ERROR', path, line, where + '含表情符號')
    if '!' in value or '！' in value:
        report('ERROR', path, line, where + '不得使用驚嘆號')
    if '…' in value or '...' in value:
        report('ERROR', path, line, where + '不得使用省略號，放不下請改寫')
    if '~' in value or '～' in value:
        report('ERROR', path, line, where + '不得用「~」表示約略或範圍，改用「約」或「至」')
    if '台灣' in value:
        report('ERROR', path, line, where + '「台」應寫作「臺」')
    if '？' in value and not (sec == 'Card 2｜世紀瓶頸' and key == '標題'):
        report('ERROR', path, line, where + '問句只允許出現在 Card 2 標題')
    if '$' in value and (sec, key) not in MATH_OK:
        report('ERROR', path, line, where + '不得使用行內數學或 $ 符號（只有 Card 3 說明與 Card 4 可用）')
    for m in re.findall(r'\$([^$]+)\$', value):
        if CJK.search(m):
            report('ERROR', path, line, where + '行內數學內含中文：$%s$' % m)
    for w in BANNED:
        if w in value:
            report('ERROR', path, line, where + '含禁用評價詞「%s」' % w)
    for w in STRONG:
        if w in value and w not in evidence:
            report('WARN', path, line, where + '含強斷言「%s」，證據表中找不到同詞支持，請確認或降格' % w)
    if '網絡' in value and key != '封面標題':
        report('WARN', path, line, where + '「網絡」請用臺灣慣用之「網路」')
    if (sec, key) in SOURCE_FIELDS:
        return
    text = re.sub(r'\$[^$]+\$', '', value)
    if re.search(r'[\u3400-\u9fff][,.;:?()]|[,;:?()][\u3400-\u9fff]', text):
        report('WARN', path, line, where + '中文句中疑似使用半形標點，請改全形')
    for a in re.findall(r'(?<![A-Za-z])[A-Z]{2,}(?![A-Za-z])', text):
        if a not in ABBR_OK:
            report('WARN', path, line, where + '含縮寫「%s」，第一次出現須改寫成中文或附白話說明' % a)
            break


def limit(path, line, label, value, n):
    w = width(value)
    if w > n:
        report('ERROR', path, line, '%s %s 字，超過上限 %s 字' % (label, fmt(w), n))


def split_parts(path, line, label, value, n):
    parts = value.split('｜')
    if len(parts) != n:
        report('ERROR', path, line, '%s 須以全形直線「｜」分成 %d 段，目前 %d 段' % (label, n, len(parts)))
        return None
    if any(p != p.strip() or not p for p in parts):
        report('ERROR', path, line, '%s 的各段不得為空，「｜」前後不得有空格' % label)
    return parts


# ---------------------------------------------------------------- SVG

def path_points(d):
    if re.search(r'[a-z]', re.sub(r'e-?\d', '', d)):
        return None, '只能用大寫絕對座標指令（M、L、H、V、C、S、Q、T、Z）'
    if 'A' in d:
        return None, '不得使用弧線指令 A'
    tokens = re.findall(r'[MLHVCSQTZ]|-?\d*\.?\d+(?:e-?\d+)?', d)
    pts, cmd, buf = [], None, []
    for t in tokens:
        if t in PATH_ARGS:
            cmd, buf = t, []
            continue
        if cmd is None:
            return None, 'path 須以 M 開頭'
        pattern = PATH_ARGS[cmd]
        if not pattern:
            return None, 'Z 之後不得接數字'
        buf.append(float(t))
        if len(buf) == len(pattern):
            for axis, v in zip(pattern, buf):
                pts.append((axis, v))
            buf = []
    return pts, None


def check_svg(path, line, svg_text, caption, kind, context):
    try:
        root = ET.fromstring(svg_text)
    except ET.ParseError as e:
        report('ERROR', path, line, 'SVG 無法解析：%s' % e)
        return
    tag = lambda el: el.tag.split('}')[-1]
    if tag(root) != 'svg':
        report('ERROR', path, line, 'SVG 根元素須為 <svg>')
        return
    extra = set(root.attrib) - {'viewBox', 'role', 'aria-label'}
    if extra:
        report('ERROR', path, line, '<svg> 只能有 viewBox、role、aria-label，多了：%s' % '、'.join(sorted(extra)))
    m = re.fullmatch(r'0 0 300 (\d+)', root.attrib.get('viewBox', ''))
    if not m or not 90 <= int(m.group(1)) <= 140:
        report('ERROR', path, line, 'viewBox 須為「0 0 300 H」，H 為 90 至 140 的整數')
        H = 140
    else:
        H = int(m.group(1))
    if root.attrib.get('role') != 'img':
        report('ERROR', path, line, '<svg> 須有 role="img"')
    if root.attrib.get('aria-label') != caption:
        report('ERROR', path, line, '<svg> 的 aria-label 須與「圖說」逐字相同')
    shapes, texts, emphasis = 0, 0, False

    def inb(axis, v, slack=0.5):
        hi = 300 if axis == 'x' else H
        return -slack <= v <= hi + slack

    for el in root.iter():
        if el is root:
            continue
        t = tag(el)
        if t not in SVG_ATTRS:
            report('ERROR', path, line, 'SVG 不得使用 <%s>（白名單見 diagram.md 第五節）' % t)
            continue
        bad = set(el.attrib) - SVG_ATTRS[t]
        if bad:
            report('ERROR', path, line, '<%s> 不得使用屬性：%s' % (t, '、'.join(sorted(bad))))
        cls = set(el.attrib.get('class', '').split())
        if t == 'g':
            if cls - COLOR - MODIFIER:
                report('ERROR', path, line, '<g> 含未定義的 class：%s' % '、'.join(sorted(cls - COLOR - MODIFIER)))
            continue
        if t == 'text':
            texts += 1
            if len(cls) != 1 or not cls <= TEXT_CLASS:
                report('ERROR', path, line, '<text> 的 class 須為 k-label 或 k-label-accent 其中之一')
            if el.attrib.get('text-anchor', 'start') not in ('start', 'middle', 'end'):
                report('ERROR', path, line, 'text-anchor 只能是 start、middle、end')
            label = ''.join(el.itertext()).strip()
            if not label:
                report('ERROR', path, line, '<text> 不得為空')
            if width(label) > 8:
                report('ERROR', path, line, '圖中標籤「%s」%s 字，超過 8 字' % (label, fmt(width(label))))
            if kind == '示意圖' and re.search(r'\d', label):
                report('ERROR', path, line, '示意圖標籤不得含數字：「%s」' % label)
            core = re.sub(r'\s*[A-Z甲乙丙丁]$', '', label)
            if core and core not in context:
                report('WARN', path, line, '圖中標籤「%s」在 Card 3 文字與論文頁中找不到，請統一用詞' % label)
            if 'k-label-accent' in cls:
                emphasis = True
            try:
                x, y = float(el.attrib.get('x', 'nan')), float(el.attrib.get('y', 'nan'))
                if not (0 <= x <= 300 and 10 <= y <= H - 2):
                    report('WARN', path, line, '標籤「%s」位置 (%s, %s) 太靠近或超出邊界' % (label, fmt(x), fmt(y)))
            except ValueError:
                report('ERROR', path, line, '<text> 須有數值 x、y')
            continue
        shapes += 1
        colors = cls & COLOR
        if len(colors) != 1:
            report('ERROR', path, line, '<%s> 須有且只有一個顏色 class（k-line、k-accent、k-ink、k-muted、k-soft）' % t)
        if cls - COLOR - MODIFIER:
            report('ERROR', path, line, '<%s> 含未定義的 class：%s' % (t, '、'.join(sorted(cls - COLOR - MODIFIER))))
        if 'k-ring' in cls and t not in CLOSED:
            report('ERROR', path, line, 'k-ring 只能用於 circle、ellipse、rect、polygon')
        if colors & {'k-accent', 'k-line'}:
            emphasis = True
        try:
            if t == 'path':
                pts, err = path_points(el.attrib.get('d', ''))
                if err:
                    report('ERROR', path, line, '<path> ' + err)
                    pts = []
            elif t in ('polyline', 'polygon'):
                nums = [float(v) for v in re.findall(r'-?\d*\.?\d+', el.attrib.get('points', ''))]
                pts = [('x' if i % 2 == 0 else 'y', v) for i, v in enumerate(nums)]
            elif t == 'line':
                pts = [('x', float(el.attrib['x1'])), ('y', float(el.attrib['y1'])),
                       ('x', float(el.attrib['x2'])), ('y', float(el.attrib['y2']))]
            elif t in ('circle', 'ellipse'):
                pts = [('x', float(el.attrib['cx'])), ('y', float(el.attrib['cy']))]
            else:
                x, y = float(el.attrib['x']), float(el.attrib['y'])
                pts = [('x', x), ('y', y), ('x', x + float(el.attrib['width'])), ('y', y + float(el.attrib['height']))]
        except (KeyError, ValueError):
            report('ERROR', path, line, '<%s> 缺少必要的座標屬性或數值格式錯誤' % t)
            continue
        out = [v for axis, v in pts if not inb(axis, v)]
        if out:
            report('ERROR', path, line, '<%s> 有座標超出畫布 0 至 300、0 至 %d：%s' % (t, H, fmt(out[0])))
    if shapes + texts > 40:
        report('ERROR', path, line, 'SVG 元素 %d 個，超過 40 個' % (shapes + texts))
    if texts > 6:
        report('ERROR', path, line, 'SVG 標籤 %d 個，超過 6 個' % texts)
    if shapes == 0:
        report('ERROR', path, line, 'SVG 沒有任何圖形')
    if not emphasis:
        report('ERROR', path, line, 'SVG 須至少有一個 k-accent 或 k-line 元素標出重點')


# ---------------------------------------------------------------- 卡片檔

def parse_card(path, slug):
    text = open(path, encoding='utf-8').read()
    if text.startswith('\ufeff'):
        report('ERROR', path, 1, '檔案不得有 BOM')
        text = text[1:]
    if '\r' in text:
        report('ERROR', path, 1, '換行須為 LF')
    lines = text.split('\n')
    if lines[0] != '# 卡片文字：' + slug:
        report('ERROR', path, 1, '第一行須為「# 卡片文字：%s」' % slug)
    header, sections, order = {}, {}, []
    sec, svg, in_svg, svg_buf, svg_line = None, None, False, [], 0
    for i, raw in enumerate(lines[1:], start=2):
        if '\t' in raw:
            report('ERROR', path, i, '不得有 Tab 字元')
        if raw != raw.rstrip():
            report('ERROR', path, i, '行尾不得有空白')
        line = raw.rstrip()
        if in_svg:
            if line.strip() == '```':
                in_svg = False
                svg = ('\n'.join(svg_buf), svg_line)
            else:
                svg_buf.append(line)
            continue
        if not line.strip():
            continue
        if line.startswith('```svg'):
            if sec != 'Card 3｜突破原理':
                report('ERROR', path, i, 'svg 區塊只能放在 Card 3 區段')
            if svg is not None:
                report('ERROR', path, i, '只能有一個 svg 區塊')
            in_svg, svg_buf, svg_line = True, [], i
            continue
        if line.startswith('#'):
            m = re.match(r'^## (.+)$', line)
            if not m or m.group(1) not in SECTIONS:
                report('ERROR', path, i, '未定義的標題：%s' % line)
                continue
            sec = m.group(1)
            if sec in sections:
                report('ERROR', path, i, '區段重複：%s' % sec)
            sections[sec] = []
            order.append(sec)
            continue
        m = re.match(r'^- \*\*(.+?)\*\*：(.+)$', line)
        if m and sec is None:
            header[m.group(1)] = (m.group(2), i)
            continue
        m = re.match(r'^- ([^：\s*]+)：(.*)$', line)
        if m and sec is not None:
            sections[sec].append((m.group(1), m.group(2), i))
            continue
        report('ERROR', path, i, '無法解析的行（欄位須寫成「- 名稱：值」）：%s' % line[:40])
    if in_svg:
        report('ERROR', path, svg_line, 'svg 區塊沒有結束的 ```')
    if not text.endswith('\n') or text.endswith('\n\n'):
        report('ERROR', path, len(lines), '檔案須以單一換行結尾')
    return header, sections, order, svg


def check_card(path, slug, all_cards):
    paper_path = os.path.join(WIKI, 'papers', slug + '.md')
    evid_path = os.path.join(WIKI, 'evidence', slug + '.md')
    if not os.path.exists(paper_path):
        report('ERROR', path, 1, '找不到對應論文頁 wiki/papers/%s.md' % slug)
        return
    paper = open(paper_path, encoding='utf-8').read()
    fm = frontmatter(paper)
    evidence = ''
    if not os.path.exists(evid_path):
        report('ERROR', path, 1, '找不到證據表 wiki/evidence/%s.md：先依 wiki-content-audit 建立證據表再寫卡片' % slug)
    else:
        evidence = open(evid_path, encoding='utf-8').read()
    header, sections, order, svg = parse_card(path, slug)

    for k in HEADER_KEYS:
        if k not in header:
            report('ERROR', path, 1, '檔頭缺少「%s」' % k)
    if '論文頁' in header and '(../papers/%s.md)' % slug not in header['論文頁'][0]:
        report('ERROR', path, header['論文頁'][1], '論文頁連結須為 ../papers/%s.md' % slug)
    if '證據表' in header and '(../evidence/%s.md)' % slug not in header['證據表'][0]:
        report('ERROR', path, header['證據表'][1], '證據表連結須為 ../evidence/%s.md' % slug)
    for k in ('撰寫者', '最後核對'):
        if k in header and not re.search(r'（.+）.*\d{4}-\d{2}-\d{2}$', header[k][0]):
            report('ERROR', path, header[k][1], '「%s」須寫成「執行代理（模型版本），YYYY-MM-DD」' % k)
    if order != [s for s in SECTIONS if s in order] or set(order) != set(SECTIONS):
        missing = [s for s in SECTIONS if s not in order]
        report('ERROR', path, 1, '六個區段須齊全且依序排列' + ('；缺少：' + '、'.join(missing) if missing else ''))

    vals = {}
    for sec in SECTIONS:
        fields = sections.get(sec, [])
        spec = SPEC[sec]
        names = [s[0] for s in spec]
        last = -1
        for key, value, ln in fields:
            if key not in names:
                report('ERROR', path, ln, '%s 不得有欄位「%s」' % (sec, key))
                continue
            idx = names.index(key)
            if idx < last:
                report('ERROR', path, ln, '%s 欄位順序錯誤：「%s」應在前面' % (sec, key))
            last = idx
            if not value.strip():
                report('ERROR', path, ln, '%s「%s」不得為空' % (sec, key))
            if (sec, key) not in NO_TEXT_CHECK:
                check_text(path, ln, sec, key, value, evidence)
            vals.setdefault((sec, key), []).append((value, ln))
        for key, lo, hi in spec:
            n = len(vals.get((sec, key), []))
            if not lo <= n <= hi and not (sec == 'Card 4｜決定性數據' and key in ('數字', '結論')):
                report('ERROR', path, 1, '%s「%s」須有 %s 筆，目前 %d 筆' % (sec, key, str(lo) if lo == hi else '%d 至 %d' % (lo, hi), n))

    one = lambda sec, key: (vals.get((sec, key)) or [('', 1)])[0]

    # ---------- 封面與 Frontmatter
    card_line = fm.get('card_line') or ''
    if not card_line:
        report('ERROR', paper_path, 1, 'Frontmatter 缺少 card_line')
    else:
        if width(card_line) > 20:
            report('ERROR', paper_path, 1, 'card_line %s 字，超過 20 字（AGENTS.md 第七章第 1 節）' % fmt(width(card_line)))
        if re.search(r'[\d０-９]', card_line):
            report('ERROR', paper_path, 1, 'card_line 不得含數值')
        if card_line[-1] in '，。、；：？！,.;:?!':
            report('ERROR', paper_path, 1, 'card_line 不得以標點結尾')
        if card_line.count('，') > 2:
            report('ERROR', paper_path, 1, 'card_line 最多兩個全形逗號')
        if re.search(r'[A-Z]{2,}', card_line):
            report('WARN', paper_path, 1, 'card_line 疑似含縮寫或術語')
        for w in BANNED:
            if w in card_line:
                report('ERROR', paper_path, 1, 'card_line 含禁用評價詞「%s」' % w)
        for w in STRONG:
            if w in card_line and w not in evidence:
                report('WARN', paper_path, 1, 'card_line 含強斷言「%s」，證據表中找不到同詞支持' % w)
    brk, ln = one('封面', '封面斷行')
    if brk:
        rows = brk.split('／')
        if brk.replace('／', '') != card_line:
            report('ERROR', path, ln, '封面斷行去掉「／」後須與 card_line 逐字相同')
        if len(rows) > 3:
            report('ERROR', path, ln, '封面斷行最多 3 行，目前 %d 行' % len(rows))
        for r in rows:
            if not r:
                report('ERROR', path, ln, '封面斷行不得有空行')
            elif width(r) > 9:
                report('ERROR', path, ln, '封面斷行「%s」%s 字，每行最多 9 字' % (r, fmt(width(r))))
            elif r[0] in '，。、；：？！「」（）':
                report('ERROR', path, ln, '封面斷行「%s」不得以標點開頭' % r)
            if '，' in r[:-1]:
                report('ERROR', path, ln, '全形逗號須在行尾：「%s」' % r)
        if any(width(r) <= 2 for r in rows if r) and len(rows) > 1:
            report('WARN', path, ln, '封面斷行有只剩一到兩字的行，請確認是否能更平均')
    lead, ln = one('封面', '導語')
    if lead:
        limit(path, ln, '導語', lead, 60)
        if not lead.endswith('。'):
            report('ERROR', path, ln, '導語須以全形句號結尾')
        if card_line and card_line in lead:
            report('WARN', path, ln, '導語包含整句 card_line，請補充 card_line 沒說的內容')
        if re.search(r'\d', lead):
            report('WARN', path, ln, '導語不放數字（數字留給 Card 4）')
    title_over, ln = one('封面', '封面標題')
    if title_over:
        limit(path, ln, '封面標題', title_over, 22)
    elif fm.get('title_zh') and width(short_name(fm['title_zh'])) > 22:
        report('WARN', path, 1, 'title_zh 擷取之短名「%s」超過 22 字，請填「封面標題」' % short_name(fm['title_zh']))
    study, ln = one('封面', '研究類型')
    need_study = fm.get('my_focus') is True and not fm.get('focus_languages')
    if need_study and not study:
        report('ERROR', path, 1, '我的關注且 focus_languages 為空，須填「研究類型」')
    if study and not need_study:
        report('ERROR', path, ln, '只有我的關注且 focus_languages 為空時才可填「研究類型」')
    if study:
        limit(path, ln, '研究類型', study, 6)

    # ---------- Card 2
    s = 'Card 2｜世紀瓶頸'
    v, ln = one(s, '標題')
    if v:
        limit(path, ln, 'Card 2 標題', v, 16)
    for key, nlim, dlim in (('對照', 5, 30), ('缺口', 5, 32)):
        for value, ln in vals.get((s, key), []):
            parts = split_parts(path, ln, 'Card 2「%s」' % key, value, 2)
            if parts:
                limit(path, ln, 'Card 2「%s」名稱' % key, parts[0], nlim)
                limit(path, ln, 'Card 2「%s」說明' % key, parts[1], dlim)
                if parts[0] not in paper:
                    report('WARN', path, ln, 'Card 2 名稱「%s」在論文頁中找不到，名稱須是論文頁提到的對象' % parts[0])
    v, ln = one(s, '結語')
    if v:
        limit(path, ln, 'Card 2 結語', v, 22)
        if not v.endswith('。'):
            report('ERROR', path, ln, 'Card 2 結語須以全形句號結尾')

    # ---------- Card 3
    s = 'Card 3｜突破原理'
    v, ln = one(s, '標題')
    if v:
        limit(path, ln, 'Card 3 標題', v, 16)
    f, ln = one(s, '公式')
    reason, rln = one(s, '無公式理由')
    if f == '無':
        # 無公式模式：論文頁一條區塊公式都沒有，且原文沒有表達本篇機制的公式（card-03-secret.md 第四節）
        if wiki_formulas(paper):
            report('ERROR', path, ln, '論文頁有區塊公式，不得使用無公式模式；請取用論文頁的公式')
        if not reason:
            report('ERROR', path, ln, '公式填「無」時須填「無公式理由」')
        else:
            limit(path, rln, '無公式理由', reason, 50)
            if not reason.startswith(NO_FORMULA_REASONS):
                report('ERROR', path, rln, '「無公式理由」須以「%s」開頭' % '」或「'.join(NO_FORMULA_REASONS))
            elif not SRC_MARK.search(reason) and '全文' not in reason:
                report('ERROR', path, rln, '「無公式理由」須寫出如何確認（如「全文無編號公式」或評估指標公式所在之節、頁）')
    elif reason:
        report('ERROR', path, rln, '有公式時不得填「無公式理由」')
    if f and f != '無':
        if '$' in f:
            report('ERROR', path, ln, 'Card 3 公式不得加 $ 或 $$')
        if CJK.search(f):
            report('ERROR', path, ln, 'Card 3 公式內不得有中文')
        if 'aligned' in f or '\\\\' in f:
            report('ERROR', path, ln, 'Card 3 公式須為單行，不得含 aligned 或 \\\\')
        if len(f) > 70:
            report('WARN', path, ln, 'Card 3 公式原始碼 %d 字元，超過 70，手機上可能需要捲動，請改取較短的公式' % len(f))
        if norm_tex(f) not in wiki_formulas(paper):
            report('ERROR', path, ln, 'Card 3 公式須逐字取自論文頁的區塊公式（或 aligned 其中一行）')
    v, ln = one(s, '說明')
    if v:
        limit(path, ln, 'Card 3 說明', v, 40)
        if not v.endswith('。'):
            report('ERROR', path, ln, 'Card 3 說明須以全形句號結尾')
    kind, ln = one(s, '圖類型')
    if kind and kind not in ('示意圖', '數據圖'):
        report('ERROR', path, ln, '圖類型只能是「示意圖」或「數據圖」')
    src, sln = one(s, '圖來源')
    if kind == '數據圖' and not src:
        report('ERROR', path, ln, '數據圖須填「圖來源」')
    if kind == '示意圖' and src:
        report('ERROR', path, sln, '示意圖不得填「圖來源」')
    if src:
        limit(path, sln, '圖來源', src, 30)
    cap, cln = one(s, '圖說')
    if cap:
        limit(path, cln, '圖說', cap, 60)
        prefix = '數據：' if kind == '數據圖' else '示意：'
        if not cap.startswith(prefix):
            report('ERROR', path, cln, '圖說須以「%s」開頭' % prefix)
    if svg is None:
        report('ERROR', path, 1, 'Card 3 必須有示意圖（```svg 區塊）')
    else:
        context = paper + one(s, '標題')[0] + one(s, '說明')[0] + cap
        check_svg(path, svg[1], svg[0], cap, kind or '示意圖', context)

    # ---------- Card 4
    s = 'Card 4｜決定性數據'
    mode, ln = one(s, '模式')
    nums, concl = vals.get((s, '數字'), []), vals.get((s, '結論'), [])
    if mode not in ('數字', '結論'):
        report('ERROR', path, ln, 'Card 4「模式」只能是「數字」或「結論」')
    elif mode == '數字':
        if concl:
            report('ERROR', path, concl[0][1], '數字模式不得有「結論」欄位')
        if len(nums) not in (2, 4):
            report('ERROR', path, ln, '數字模式須有 2 或 4 個「數字」，目前 %d 個' % len(nums))
        for value, vln in nums:
            parts = split_parts(path, vln, 'Card 4「數字」', value, 3)
            if not parts:
                continue
            limit(path, vln, 'Card 4 數字的值', parts[0], 7)
            limit(path, vln, 'Card 4 數字的說明', parts[1], 24)
            limit(path, vln, 'Card 4 數字的來源位置', parts[2], 40)
            if not SRC_MARK.search(parts[2]):
                report('ERROR', path, vln, 'Card 4 來源位置須寫出頁、表、圖或節（如 p. 12、Table 3、Fig. 2）')
            for n in re.findall(r'\d+(?:\.\d+)?', plain(parts[0])):
                if (len(n) >= 2 or '.' in n) and evidence and n not in evidence:
                    report('ERROR', path, vln, 'Card 4 數字「%s」在證據表中找不到；數字只能取自證據表' % n)
    else:
        if nums:
            report('ERROR', path, nums[0][1], '結論模式不得有「數字」欄位')
        if len(concl) not in (2, 3):
            report('ERROR', path, ln, '結論模式須有 2 或 3 條「結論」，目前 %d 條' % len(concl))
        for value, vln in concl:
            parts = split_parts(path, vln, 'Card 4「結論」', value, 2)
            if not parts:
                continue
            limit(path, vln, 'Card 4 結論內容', parts[0], 26)
            limit(path, vln, 'Card 4 結論的來源位置', parts[1], 40)
            if not SRC_MARK.search(parts[1]):
                report('ERROR', path, vln, 'Card 4 來源位置須寫出頁、表、圖或節')
    v, ln = one(s, '範圍')
    if v:
        limit(path, ln, 'Card 4 範圍', v, 32)
        if v.startswith('範圍'):
            report('ERROR', path, ln, 'Card 4 範圍不得含「範圍：」字樣（網頁自動加）')

    # ---------- Card 5
    s = 'Card 5｜典範轉移'
    v, ln = one(s, '標題')
    if v:
        limit(path, ln, 'Card 5 標題', v, 16)
    prev, has_award = 0, False
    py = fm.get('paper_year') if isinstance(fm.get('paper_year'), int) else 0
    mode5, mln = one(s, '模式')
    newmode = mode5 == '新論文'
    rows = vals.get((s, '里程碑'), [])
    if mode5 and not newmode:
        report('ERROR', path, mln, 'Card 5「模式」只能填「新論文」；一般論文不填此欄')
    if newmode:
        this_year = datetime.date.today().year
        if py < this_year - NEW_PAPER_YEARS:
            report('ERROR', path, mln, '新論文模式只適用於發表 %d 年內之論文（paper_year ≥ %d）；較早之論文須先依 wiki-content-audit 補後續研究'
                   % (NEW_PAPER_YEARS, this_year - NEW_PAPER_YEARS))
        if not 2 <= len(rows) <= 4:
            report('ERROR', path, 1, '新論文模式「里程碑」須有 2 至 4 筆，目前 %d 筆' % len(rows))
    else:
        if not 3 <= len(rows) <= 5:
            report('ERROR', path, 1, 'Card 5「里程碑」須有 3 至 5 筆，目前 %d 筆' % len(rows))
        if rows and all(len(value.split('｜')) == 3 and value.split('｜')[2].startswith('本篇') for value, _l in rows):
            report('ERROR', path, 1, 'Card 5 里程碑全部出自本篇；論文太新且論文頁沒有後續研究時改用「模式：新論文」，否則須先補後續研究')
    for value, vln in rows:
        parts = split_parts(path, vln, 'Card 5「里程碑」', value, 3)
        if not parts:
            continue
        year, content, source = parts
        if not re.fullmatch(r'\d{4}', year):
            report('ERROR', path, vln, '里程碑年份須為 4 位數字')
            continue
        y = int(year)
        if y < py:
            report('ERROR', path, vln, '里程碑年份 %d 早於本篇發表年 %d' % (y, py))
        if y < prev:
            report('ERROR', path, vln, '里程碑須依年份由早到晚排列')
        prev = y
        limit(path, vln, '里程碑內容', content, 22)
        limit(path, vln, '里程碑出處', source, 60)
        if source == '獎項':
            has_award = True
            if not fm.get('honor'):
                report('ERROR', path, vln, '論文頁沒有 honor，不得有獎項列')
            elif y != fm.get('award_year'):
                report('ERROR', path, vln, '獎項列年份須等於 award_year（%s）' % fm.get('award_year'))
            laureates = str(fm.get('laureates') or '')
            names = re.findall(r'([A-Z][A-Za-z\'\-]+)(?=,|$)', laureates)
            if names and not any(n in content for n in names):
                report('WARN', path, vln, '獎項列內容未提及 laureates 中的得獎者姓氏')
        elif source == '本篇' or source.startswith('本篇 '):
            if newmode and not SRC_MARK.search(source):
                report('ERROR', path, vln, '新論文模式之本篇列須寫出位置，如「本篇 §7」「本篇 p. 9」')
            if newmode and y != py:
                report('ERROR', path, vln, '新論文模式之本篇列年份須等於發表年 %d' % py)
        else:
            m = re.match(r'([A-Z][A-Za-z\'\-]+|[一-鿿]{2,4}(?=[\s,]))', source)
            if not m:
                report('ERROR', path, vln, '里程碑出處須以第一作者姓氏（或中文全名）開頭，或寫「獎項」、「本篇」')
            elif m.group(1) not in paper:
                report('ERROR', path, vln, '里程碑出處作者「%s」不在論文頁中；後續研究須先寫進論文頁' % m.group(1))
            if year not in source:
                report('WARN', path, vln, '里程碑出處未包含年份 %s' % year)
    if fm.get('honor') and not has_award:
        report('WARN', path, 1, '論文頁有 honor，Card 5 建議以獎項列收尾')
    v, ln = one(s, '註記')
    if v:
        limit(path, ln, 'Card 5 註記', v, 24)
        if newmode and '本篇' not in v:
            report('ERROR', path, ln, '新論文模式之註記須說明哪些列出自本篇（例如「以上皆出自本篇，尚無後續研究」）')

    # ---------- Card 6
    s = 'Card 6｜Kairos'
    v, ln = one(s, '結語')
    if v:
        limit(path, ln, 'Card 6 結語', v, 40)
        if not v.endswith('。'):
            report('ERROR', path, ln, 'Card 6 結語須以全形句號結尾')
        if fm.get('my_focus') is True and re.search(r'我|碩論|碩士論文', v):
            report('ERROR', path, ln, '我的關注 Card 6 不得使用第一人稱或提及碩論')
    v, ln = one(s, '轉變')
    if v:
        if v.count('→') != 1 or ' →' in v or '→ ' in v:
            report('ERROR', path, ln, 'Card 6 轉變須寫成「甲→乙」，只用一個 →，前後不加空格')
        else:
            a, b = v.split('→')
            limit(path, ln, '轉變的前半', a, 6)
            limit(path, ln, '轉變的後半', b, 6)

    for key in (('Card 2｜世紀瓶頸', '標題'), ('Card 2｜世紀瓶頸', '結語'), ('Card 5｜典範轉移', '標題'), ('Card 6｜Kairos', '結語')):
        value, ln = one(*key)
        if value:
            all_cards.setdefault(key, []).append((value, path, ln))


def cross_file(all_cards):
    for key, items in all_cards.items():
        seen, heads = {}, {}
        for value, path, ln in items:
            k = re.sub(r'[，。、；：？「」\s]', '', value)
            if k in seen:
                report('WARN', path, ln, '%s「%s」與 %s 完全相同' % ('／'.join(key), value, seen[k]))
            seen.setdefault(k, os.path.relpath(path, ROOT))
            heads.setdefault(k[:3], []).append((path, ln))
        for head, where in heads.items():
            if len(where) > 3:
                for path, ln in where:
                    report('WARN', path, ln, '%s 有 %d 個檔案以「%s」開頭，句型重複，請改寫' % ('／'.join(key), len(where), head))


def main():
    ap = argparse.ArgumentParser(description='檢查 wiki/cards/ 卡片文字檔')
    ap.add_argument('slugs', nargs='*', help='只檢查指定論文（不含 .md）')
    ap.add_argument('--missing', action='store_true', help='另列出尚無卡片檔的論文')
    args = ap.parse_args()
    files = sorted(glob.glob(os.path.join(WIKI, 'cards', '*.md')))
    if args.slugs:
        files = [os.path.join(WIKI, 'cards', s + '.md') for s in args.slugs]
    all_cards = {}
    for p in files:
        slug = os.path.basename(p)[:-3]
        if not os.path.exists(p):
            report('ERROR', p, 0, '找不到卡片檔')
            continue
        check_card(p, slug, all_cards)
    cross_file(all_cards)
    if args.missing:
        have = {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(WIKI, 'cards', '*.md'))}
        for p in sorted(glob.glob(os.path.join(WIKI, 'papers', '*.md'))):
            if os.path.basename(p)[:-3] not in have:
                report('INFO', p, 0, '尚無卡片檔 wiki/cards/%s' % os.path.basename(p))
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
    order = {'ERROR': 0, 'WARN': 1, 'INFO': 2}
    for level, rel, line, msg in sorted(results, key=lambda r: (order[r[0]], r[1], r[2])):
        print('%-5s %s:%s  %s' % (level, rel, line, msg))
    errs = sum(1 for r in results if r[0] == 'ERROR')
    warns = sum(1 for r in results if r[0] == 'WARN')
    print('卡片檔 %d 個；ERROR %d、WARN %d' % (len(files), errs, warns))
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
