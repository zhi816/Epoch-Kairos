#!/usr/bin/env python3
"""lint_wiki.py: Epoch-Kairos 知識庫機械檢查（AGENTS.md 第六章第 3 節 Lint）。

只使用標準函式庫。於倉庫任意位置執行皆可：
    python .agents/skills/wiki-content-audit/scripts/lint_wiki.py
    python .agents/skills/wiki-content-audit/scripts/lint_wiki.py --errors-only

ERROR：違反 AGENTS.md 硬性規範，提交前必須修正。
WARN ：啟發式提醒（公式、化學式、長公式）或日誌舊條目之問題（日誌 append-only，不回溯修改）。
結束代碼：有 ERROR 時為 1，否則為 0。

標籤白名單、domain 與 focus_role 均直接從 AGENTS.md 讀取，不在本腳本另寫一份。
"""
import argparse
import json
import os
import re
import subprocess
import sys

ACTIONS = {'init', 'ingest', 'query', 'lint', 'audit', 'fix', 'rule', 'design',
           'math', 'update', 'config', 'git'}
STATUSES = {'planned', 'wiki', 'published'}
VERIFICATIONS = {'unverified', 'partial', 'issues', 'verified'}
ISSUE_STATES = {'open', 'fixed', 'wontfix'}
VERDICTS = {'符合來源', '原文不符', '原文未支持', '過度表述', '歸因／版本錯置', '未能核實'}
PAPER_REQUIRED = ['title', 'title_zh', 'paper_year', 'award_year', 'timeline_year', 'authors',
                  'venue', 'domain', 'domain_tags', 'concepts', 'status', 'verification', 'hook',
                  'card_line', 'my_focus']
CARD_LINE_MAX = 20  # AGENTS.md 第七章第 1 節「卡片一句話」：20 字以內，全形標點計入
CONCEPT_REQUIRED = ['title', 'title_zh', 'domain', 'domain_tags', 'papers', 'related_concepts',
                    'verification']
# 日誌標題第三段規則之生效時間（AGENTS.md 第六章：2026-11-08 合併入 main 後生效）。
LOG_RULE_SINCE = '2026-11-09 00:00'

# 預設以 emoji 呈現之字元（Emoji_Presentation）與變體選擇符；不含 ★ ✦ 等幾何符號。
EMOJI = re.compile(
    '[\U0001F000-\U0001FAFF\uFE0F\u231A\u231B\u23E9-\u23EC\u23F0\u23F3\u25FD\u25FE'
    '\u2614\u2615\u2648-\u2653\u267F\u2693\u26A1\u26AA\u26AB\u26BD\u26BE\u26C4\u26C5'
    '\u26CE\u26D4\u26EA\u26F2-\u26F5\u26FA\u26FD\u2705\u270A\u270B\u2728\u274C\u274E'
    '\u2753-\u2755\u2757\u2795-\u2797\u27B0\u27BF\u2B1B\u2B1C\u2B50\u2B55]')
CJK = re.compile('[\u3400-\u9fff\uf900-\ufaff]')
CHEM = re.compile(r'(?<![A-Za-z\\{])(Na|K|Ca|Mg|Cl|Fe|Zn|Cu|Li|Rb|Cs|Sr|Ba|Al|Mn|Co|Ni|H)'
                  r'(?:_\{?\d+\}?)?\^\{?\d*[+\-]\}?')
WIKILINK = re.compile(r'\[\[(?![\d,\s]+\]\])[^\]\n]+\]\]')
MDLINK = re.compile(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
TEXT_EXT = {'.md', '.html', '.css', '.js', '.json', '.py', '.sh', '.txt', '.yml', '.yaml'}

results = []


def report(level, path, line, msg):
    results.append((level, path, line, msg))


def repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        out = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=here,
                             capture_output=True, check=True)
        return out.stdout.decode().strip()
    except Exception:
        return os.path.abspath(os.path.join(here, '..', '..', '..', '..'))


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def line_of(text, pos):
    return text.count('\n', 0, pos) + 1


# ---------------------------------------------------------------- frontmatter

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
        end = raw.rfind(']')
        body = raw[:end + 1]
        try:
            return json.loads(body)
        except ValueError:
            inner = body[1:-1].strip()
            return [s.strip().strip('"\'') for s in inner.split(',') if s.strip()] if inner else []
    raw = re.split(r'\s+#', raw, 1)[0].strip()
    if raw in ('true', 'false'):
        return raw == 'true'
    if re.fullmatch(r'-?\d+', raw):
        return int(raw)
    return raw


def frontmatter(text):
    """回傳 (dict, {key: 行號}, 結尾行號)；無 frontmatter 時回傳 (None, {}, 0)。"""
    lines = text.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, {}, 0
    data, where, key = {}, {}, None
    for i, line in enumerate(lines[1:], start=2):
        if line.strip() == '---':
            return data, where, i
        m = re.match(r'^([A-Za-z_][\w-]*):(.*)$', line)
        if m:
            key = m.group(1)
            where[key] = i
            val = parse_value(m.group(2))
            data[key] = [] if val is None else val
            continue
        m = re.match(r'^\s+-\s+(.*)$', line)
        if m and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(parse_value(m.group(1)))
    return None, {}, 0


# ---------------------------------------------------------------- AGENTS.md

def load_schema(root):
    text = read(os.path.join(root, 'AGENTS.md'))
    whitelist = {}
    sec = text.split('### 標籤白名單與色系歸屬', 1)
    if len(sec) == 2:
        for line in sec[1].split('\n'):
            if line.startswith('>') or line.startswith('##'):
                if whitelist:
                    break
                continue
            m = re.match(r'^\|\s*`(\w+)`\s*\|(.*)\|\s*$', line)
            if m:
                whitelist[m.group(1)] = set(re.findall(r'`(#[^`]+)`', m.group(2)))
    roles = set()
    m = re.search(r'\*\*`focus_role`\*\*(.*?)\*\*`focus_languages`\*\*', text, re.S)
    if m:
        roles = set(re.findall(r'^>\s*\|\s*`([a-z-]+)`\s*\|', m.group(1), re.M))
    if not whitelist:
        report('ERROR', 'AGENTS.md', 0, '無法從第八章讀出標籤白名單表格')
    if not roles:
        report('ERROR', 'AGENTS.md', 0, '無法從第七章第 1 節讀出 focus_role 鍵值表格')
    return whitelist, roles


# ---------------------------------------------------------------- content checks

def strip_code(text):
    """以空白取代程式碼區塊與行內程式碼，保留換行以維持行號。"""
    def blank(m):
        return re.sub(r'[^\n]', ' ', m.group(0))
    text = re.sub(r'```.*?```', blank, text, flags=re.S)
    return re.sub(r'`[^`\n]*`', blank, text)


def math_segments(text):
    """回傳 [(起始位置, 內容, 是否區塊)]；已先移除程式碼。"""
    segs = []
    masked = list(text)
    for m in re.finditer(r'(?<!\\)\$\$(.+?)(?<!\\)\$\$', text, re.S):
        segs.append((m.start(), m.group(1), True))
        for i in range(m.start(), m.end()):
            if masked[i] != '\n':
                masked[i] = ' '
    rest = ''.join(masked)
    for m in re.finditer(r'(?<!\\)\$(?!\s)([^$\n]+?)(?<![\s\\])\$', rest):
        segs.append((m.start(), m.group(1), False))
    return segs


def check_math(rel, text):
    body = strip_code(text)
    for pos, seg, block in math_segments(body):
        ln = line_of(body, pos)
        if CJK.search(seg):
            hint = '；若為金額請改寫作 \\$ 或「美元」' if not block else ''
            report('ERROR', rel, ln, '公式內含中文字元' + hint + '：' + seg.strip()[:40])
        plain = re.sub(r'\\(mathrm|text|mathbf|operatorname)\{[^{}]*\}', '', seg)
        m = CHEM.search(plain)
        if m:
            report('WARN', rel, ln, '疑似化學元素或離子未用 \\mathrm{} 正體：' + m.group(0))
        if block:
            flat = ' '.join(seg.split())
            if len(flat) > 140 and 'aligned' not in seg and 'array' not in seg \
                    and 'matrix' not in seg and 'cases' not in seg:
                report('WARN', rel, ln, '長區塊公式（%d 字元）未使用 aligned 斷行' % len(flat))


def check_links(root, rel, text, is_log):
    level = 'WARN' if is_log else 'ERROR'
    body = strip_code(text)
    base = os.path.dirname(os.path.join(root, rel))
    raw_present = os.path.isdir(os.path.join(root, 'raw'))
    for m in MDLINK.finditer(body):
        target = m.group(1)
        if re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('#'):
            continue
        path = target.split('#', 1)[0]
        if not path:
            continue
        try:
            from urllib.parse import unquote
            path = unquote(path)
        except Exception:
            pass
        full = os.path.normpath(os.path.join(base, path))
        if os.path.relpath(full, root).replace('\\', '/').startswith('raw/') and not raw_present:
            continue
        if not os.path.exists(full):
            report(level, rel, line_of(body, m.start()), '相對連結指向不存在的檔案：' + target)


def mask_math(text):
    chars = list(text)
    for pos, seg, block in math_segments(text):
        end = pos + len(seg) + (4 if block else 2)
        for i in range(pos, min(end, len(chars))):
            if chars[i] != '\n':
                chars[i] = ' '
    return ''.join(chars)


def check_text_rules(rel, text, is_log):
    for m in EMOJI.finditer(text):
        report('ERROR', rel, line_of(text, m.start()), '含表情符號 U+%04X' % ord(m.group(0)))
    # Markdown 中寫在行內程式碼裡的 file:/// 是在說明規則，不算違規；本腳本自身亦同。
    scan = strip_code(text) if rel.endswith('.md') else text
    if not rel.endswith('scripts/lint_wiki.py'):
        for m in re.finditer(r'file:///', scan):
            report('WARN' if is_log else 'ERROR', rel, line_of(scan, m.start()), '含 file:/// 本機絕對路徑')
    if rel.endswith('.md'):
        # 公式內的 [[n, k, d]] 是量子碼記號，不是 wiki 連結。
        body = mask_math(strip_code(text))
        for m in WIKILINK.finditer(body):
            report('WARN' if is_log else 'ERROR', rel, line_of(body, m.start()),
                   '殘留 [[...]] 語法：' + m.group(0)[:40])


# ---------------------------------------------------------------- issues / evidence

def load_issues(root):
    path = os.path.join(root, 'wiki', 'issues.md')
    issues = []
    if not os.path.exists(path):
        return issues
    text = read(path)
    seen = set()
    for m in re.finditer(r'(?m)^### (.+)$', text):
        ln = line_of(text, m.start())
        parts = [p.strip() for p in m.group(1).split('|')]
        if len(parts) != 5 or not re.fullmatch(r'EK-\d{3,}', parts[0]):
            report('ERROR', 'wiki/issues.md', ln, '問題標題格式應為「EK-編號 | 狀態 | 檔案 | 位置 | 判定」')
            continue
        iid, state, target, _, verdict = parts
        if iid in seen:
            report('ERROR', 'wiki/issues.md', ln, '問題編號重複：' + iid)
        seen.add(iid)
        if state not in ISSUE_STATES:
            report('ERROR', 'wiki/issues.md', ln, '狀態須為 open / fixed / wontfix：' + state)
        if verdict not in VERDICTS:
            report('ERROR', 'wiki/issues.md', ln, '判定須取 wiki-content-audit 之六種判定：' + verdict)
        if not os.path.exists(os.path.join(root, 'wiki', target)):
            report('ERROR', 'wiki/issues.md', ln, '問題指向之檔案不存在：wiki/' + target)
        issues.append((iid, state, target))
    return issues


# ---------------------------------------------------------------- main

def main():
    try:  # Windows 主控台預設編碼可能無法輸出中文
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    ap = argparse.ArgumentParser(description='Epoch-Kairos 知識庫機械檢查')
    ap.add_argument('--errors-only', action='store_true', help='只顯示 ERROR')
    args = ap.parse_args()

    root = repo_root()
    whitelist, roles = load_schema(root)
    domains = set(whitelist)
    all_tags = set().union(*whitelist.values()) if whitelist else set()

    papers_dir = os.path.join(root, 'wiki', 'papers')
    concepts_dir = os.path.join(root, 'wiki', 'concepts')
    papers = {f[:-3]: os.path.join(papers_dir, f) for f in sorted(os.listdir(papers_dir)) if f.endswith('.md')}
    concepts = {f[:-3]: os.path.join(concepts_dir, f) for f in sorted(os.listdir(concepts_dir)) if f.endswith('.md')}
    issues = load_issues(root)
    open_by_target = {}
    for iid, state, target in issues:
        if state == 'open':
            open_by_target.setdefault(target, []).append(iid)

    fm_cache = {}

    def check_common(kind, slug, path, required):
        rel = os.path.relpath(path, root).replace('\\', '/')
        text = read(path)
        fm, where, _ = frontmatter(text)
        if fm is None:
            report('ERROR', rel, 1, '缺少 YAML frontmatter')
            return None
        fm_cache[(kind, slug)] = (fm, where, rel)
        for k in required:
            if k not in fm or fm[k] in (None, ''):
                report('ERROR', rel, 1, '缺少必填欄位：' + k)
        if fm.get('domain') and fm['domain'] not in domains:
            report('ERROR', rel, where.get('domain', 1), 'domain 不在六大色系內：' + str(fm['domain']))
        tags = fm.get('domain_tags')
        if tags is not None and not isinstance(tags, list):
            report('ERROR', rel, where.get('domain_tags', 1), 'domain_tags 須為陣列')
        elif tags:
            for t in tags:
                if t not in all_tags:
                    report('ERROR', rel, where.get('domain_tags', 1), '標籤不在第八章白名單：' + str(t))
        v = fm.get('verification')
        target = kind + '/' + slug + '.md'
        if v is not None and v not in VERIFICATIONS:
            report('ERROR', rel, where.get('verification', 1), 'verification 須為 unverified / partial / issues / verified')
        elif v:
            has_open = target in open_by_target
            evidence = os.path.exists(os.path.join(root, 'wiki', 'evidence', slug + '.md'))
            ln = where.get('verification', 1)
            if has_open and v != 'issues':
                report('ERROR', rel, ln, 'wiki/issues.md 仍有未結問題（%s），verification 應為 issues'
                       % '、'.join(open_by_target[target]))
            if v == 'issues' and not has_open:
                report('ERROR', rel, ln, 'verification 為 issues，但 wiki/issues.md 中本頁沒有 open 問題')
            if v == 'verified' and not evidence:
                report('ERROR', rel, ln, 'verification 為 verified，但缺少 wiki/evidence/%s.md' % slug)
        check_text_rules(rel, text, False)
        check_links(root, rel, text, False)
        check_math(rel, text)
        return fm

    for slug, path in papers.items():
        fm = check_common('papers', slug, path, PAPER_REQUIRED)
        if fm is None:
            continue
        fm, where, rel = fm_cache[('papers', slug)]
        m = re.match(r'^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*$', slug)
        if not m:
            report('ERROR', rel, 1, '檔名須為 YYYY-<小寫連字號 slug>.md')
        elif fm.get('paper_year') != int(m.group(1)):
            report('ERROR', rel, where.get('paper_year', 1),
                   '檔名年份 %s 與 paper_year %s 不一致' % (m.group(1), fm.get('paper_year')))
        if 'doi_url' not in fm:
            report('WARN', rel, 1, '缺少 doi_url（無 DOI 者請於正文註明原文連結）')
        cl = fm.get('card_line')
        if isinstance(cl, str):
            if len(cl) > CARD_LINE_MAX:
                report('ERROR', rel, where.get('card_line', 1),
                       'card_line 須在 %d 字以內（現為 %d 字）' % (CARD_LINE_MAX, len(cl)))
            if cl == fm.get('hook'):
                report('ERROR', rel, where.get('card_line', 1), 'card_line 不得直接沿用 hook')
            if re.search(r'\d', cl):
                report('WARN', rel, where.get('card_line', 1), 'card_line 含數字；規則不放數值')
        st = fm.get('status')
        if st and st not in STATUSES:
            report('ERROR', rel, where.get('status', 1), 'status 須為 planned / wiki / published')
        if st == 'published' and not os.path.exists(os.path.join(root, 'web', 'papers', slug, 'index.html')):
            report('ERROR', rel, where.get('status', 1), 'status 為 published，但缺少 web/papers/%s/index.html' % slug)
        if fm.get('my_focus') is True:
            if fm.get('focus_role') not in roles:
                report('ERROR', rel, where.get('focus_role', where.get('my_focus', 1)),
                       'focus_role 須取第七章第 1 節之鍵值：' + str(fm.get('focus_role')))
            if not isinstance(fm.get('focus_languages'), list):
                report('ERROR', rel, where.get('my_focus', 1), 'my_focus 為 true 時須有 focus_languages 陣列')
        elif 'focus_role' in fm:
            report('WARN', rel, where['focus_role'], 'my_focus 不為 true，卻填了 focus_role')
        if fm.get('laureates') and fm.get('authors') and fm['laureates'] == fm['authors']:
            report('WARN', rel, where.get('laureates', 1), 'laureates 與 authors 相同；第七章規定此欄僅於兩者不同時填寫')
        for c in fm.get('concepts') or []:
            if c not in concepts:
                report('ERROR', rel, where.get('concepts', 1), 'concepts 指向不存在的概念頁：' + str(c))

    for slug, path in concepts.items():
        fm = check_common('concepts', slug, path, CONCEPT_REQUIRED)
        if fm is None:
            continue
        fm, where, rel = fm_cache[('concepts', slug)]
        for p in fm.get('papers') or []:
            if p not in papers:
                report('ERROR', rel, where.get('papers', 1), 'papers 指向不存在的論文頁：' + str(p))
            elif slug not in (fm_cache.get(('papers', p), ({}, {}, ''))[0].get('concepts') or []):
                report('ERROR', rel, where.get('papers', 1), '雙向對應缺漏：論文頁 %s 的 concepts 未列出 %s' % (p, slug))
        for r in fm.get('related_concepts') or []:
            if r not in concepts:
                report('ERROR', rel, where.get('related_concepts', 1), 'related_concepts 指向不存在的概念頁：' + str(r))

    for slug in papers:
        entry = fm_cache.get(('papers', slug))
        if not entry:
            continue
        fm, where, rel = entry
        for c in fm.get('concepts') or []:
            cfm = fm_cache.get(('concepts', c))
            if cfm and slug not in (cfm[0].get('papers') or []):
                report('ERROR', rel, where.get('concepts', 1), '雙向對應缺漏：概念頁 %s 的 papers 未列出 %s' % (c, slug))

    # 孤島頁：沒有任何其他 wiki 檔案以連結或欄位指向本頁。
    wiki_texts = {}
    for dirpath, _, files in os.walk(os.path.join(root, 'wiki')):
        for f in files:
            if f.endswith('.md'):
                p = os.path.join(dirpath, f)
                wiki_texts[os.path.relpath(p, root).replace('\\', '/')] = read(p)
    for kind, pages in (('papers', papers), ('concepts', concepts)):
        for slug in pages:
            own = 'wiki/%s/%s.md' % (kind, slug)
            linked = any(slug in t for r, t in wiki_texts.items()
                         if r != own and r not in ('wiki/log.md', 'wiki/issues.md') and not r.startswith('wiki/evidence/'))
            if not linked:
                report('WARN', own, 1, '孤島頁：索引與其他頁面均未連結本頁')

    # 其他文字檔：Emoji、file:///、[[...]]、連結。
    targets = ['AGENTS.md', 'DESIGN.md', 'README.md']
    for top in ('wiki', 'web', '.agents', '.claude'):
        for dirpath, dirs, files in os.walk(os.path.join(root, top)):
            dirs[:] = [d for d in dirs if d not in ('node_modules', '.git')]
            for f in files:
                if os.path.splitext(f)[1] in TEXT_EXT:
                    targets.append(os.path.relpath(os.path.join(dirpath, f), root).replace('\\', '/'))
    for rel in targets:
        path = os.path.join(root, rel)
        if not os.path.exists(path) or rel.startswith('wiki/papers/') or rel.startswith('wiki/concepts/'):
            continue
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        is_log = rel == 'wiki/log.md'
        check_text_rules(rel, text, is_log)
        if rel.endswith('.md'):
            check_links(root, rel, text, is_log)
        if rel.startswith('wiki/') and rel.endswith('.md') and not is_log:
            check_math(rel, text)

    # 日誌標題格式。
    log_text = read(os.path.join(root, 'wiki', 'log.md'))
    for m in re.finditer(r'(?m)^## (.*)$', log_text):
        ln = line_of(log_text, m.start())
        h = re.match(r'^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (\S+) \| (.+?)(?: \| (.+))?$', m.group(1))
        if not h:
            report('WARN', 'wiki/log.md', ln, '日誌標題格式不符：' + m.group(1)[:40])
            continue
        ts, action, _, third = h.groups()
        new = ts >= LOG_RULE_SINCE
        level = 'ERROR' if new else 'WARN'
        if action not in ACTIONS:
            report(level, 'wiki/log.md', ln, '動作類型不在詞彙表內：' + action)
        if new:
            if not third:
                report(level, 'wiki/log.md', ln, '缺少標題第三段（領域標籤或「全域」）')
            elif third != '全域':
                bad = [t for t in third.split() if t not in all_tags]
                if bad:
                    report(level, 'wiki/log.md', ln, '標題第三段須為「全域」或白名單標籤：' + ' '.join(bad))
            end = log_text.find('\n## ', m.end())
            entry = log_text[m.end(): end if end != -1 else len(log_text)]
            for field in ('執行代理', '模型版本'):
                if '- **%s**：' % field not in entry:
                    report(level, 'wiki/log.md', ln, '缺少「%s」行' % field)

    shown = [r for r in results if not (args.errors_only and r[0] != 'ERROR')]
    shown.sort(key=lambda r: (r[0] != 'ERROR', r[1], r[2]))
    for level, rel, ln, msg in shown:
        print('%-5s %s:%d  %s' % (level, rel, ln, msg))
    n_err = sum(1 for r in results if r[0] == 'ERROR')
    n_warn = len(results) - n_err
    print('---')
    print('論文頁 %d、概念頁 %d、問題清單 %d 筆（open %d）；ERROR %d、WARN %d'
          % (len(papers), len(concepts), len(issues), sum(len(v) for v in open_by_target.values()), n_err, n_warn))
    sys.exit(1 if n_err else 0)


if __name__ == '__main__':
    main()
