#!/usr/bin/env python3
"""crossref_check.py: 以 Crossref 核對論文頁書目（AGENTS.md 第六章 Ingest 第 1 步、Lint 第 6 條）。

只使用標準函式庫，需要網路。於倉庫任意位置執行：
    python .agents/skills/wiki-content-audit/scripts/crossref_check.py              # 全部論文頁
    python .agents/skills/wiki-content-audit/scripts/crossref_check.py 2005-optogenetics 2012-crispr-cas9

比對項目：
  - 年份：paper_year 是否等於 Crossref 的 published-print、published-online 或 issued 年份之一。
  - 作者：Crossref 每位作者之姓氏是否出現在 authors 欄位（忽略大小寫與重音符號）；
          作者過多時頁面常寫 et al.，此時只列為提醒。
  - 期刊：venue 是否包含 Crossref 之 container-title（忽略大小寫與標點）。
結果僅確認書目，不確認內容。無 doi_url 或 doi_url 非 doi.org 者略過。
結束代碼：有 MISMATCH 時為 1，否則為 0（網路錯誤不計入）。
"""
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lint_wiki import frontmatter, read, repo_root  # noqa: E402

UA = 'Epoch-Kairos-bibliography-check/1.0'


def fold(s):
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    s = s.replace('ae', 'a').replace('oe', 'o').replace('ue', 'u')  # Schütze 與 Schuetze 視為同名
    return re.sub(r'[^a-z0-9㐀-鿿]+', ' ', s).strip()


def title_in(container, venue):
    """Crossref 期刊名之實詞有七成以上出現在 venue 即視為相符（容許 Volume 1: Long Papers 等尾綴）。"""
    words = [w for w in fold(container).split() if len(w) > 2]
    if not words:
        return True
    present = venue.split()
    return sum(1 for w in words if w in present) / len(words) >= 0.7


def doi_of(url):
    m = re.match(r'^https?://(?:dx\.)?doi\.org/(.+)$', (url or '').strip())
    return urllib.parse.unquote(m.group(1)) if m else None


def doi_exists(doi):
    """向 doi.org 查詢 DOI 是否註冊：True / False / None（無法判斷）。"""
    url = 'https://doi.org/api/handles/' + urllib.parse.quote(doi, safe='/')
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode('utf-8')).get('responseCode') == 1
    except urllib.error.HTTPError as e:
        return False if e.code == 404 else None
    except Exception:
        return None


def fetch(doi):
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/')
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode('utf-8'))['message']


def years(msg):
    out = []
    for k in ('published-print', 'published-online', 'issued', 'published'):
        parts = (msg.get(k) or {}).get('date-parts') or []
        if parts and parts[0] and parts[0][0]:
            out.append((k, int(parts[0][0])))
    return out


def main():
    try:  # Windows 主控台預設編碼可能無法輸出中文
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    root = repo_root()
    papers_dir = os.path.join(root, 'wiki', 'papers')
    slugs = sys.argv[1:] or sorted(f[:-3] for f in os.listdir(papers_dir) if f.endswith('.md'))
    mismatches = 0
    for slug in slugs:
        path = os.path.join(papers_dir, slug + '.md')
        if not os.path.exists(path):
            print('SKIP  %s  找不到論文頁' % slug)
            continue
        fm, _, _ = frontmatter(read(path))
        doi = doi_of((fm or {}).get('doi_url'))
        if not doi:
            print('SKIP  %s  無 doi.org 連結' % slug)
            continue
        try:
            msg = fetch(doi)
        except urllib.error.HTTPError as e:
            if e.code != 404:
                print('NET   %s  無法取得 Crossref 資料（%s）：%s' % (slug, doi, e))
                continue
            exists = doi_exists(doi)
            if exists is False:
                mismatches += 1
                print('MISMATCH  %s  (%s)\n          - DOI 無法解析：doi.org 查無此號，請回原文首頁核對' % (slug, doi))
            elif exists:
                print('NOTE  %s  (%s)\n          - DOI 存在但非 Crossref 註冊（可能為 Airiti 或 DataCite 等），請人工核對書目' % (slug, doi))
            else:
                print('NET   %s  Crossref 查無資料，且無法連線 doi.org 判斷 DOI 是否存在（%s）' % (slug, doi))
            continue
        except Exception as e:
            print('NET   %s  無法取得 Crossref 資料（%s）：%s' % (slug, doi, e))
            continue
        problems, notes = [], []

        ys = years(msg)
        if ys and fm.get('paper_year') not in {y for _, y in ys}:
            problems.append('年份：頁面 %s，Crossref %s' % (
                fm.get('paper_year'), '、'.join('%s=%d' % (k, y) for k, y in ys)))

        page_authors = fold(fm.get('authors', ''))
        families = [a.get('family') or a.get('name') or '' for a in msg.get('author', [])]
        missing = [f for f in families if f and fold(f) not in page_authors]
        if missing:
            etal = 'et al' in page_authors or '等' in (fm.get('authors') or '')
            text = '作者：Crossref 有、頁面無：%s（Crossref 共 %d 位）' % ('、'.join(missing[:8]), len(families))
            (notes if etal else problems).append(text)

        containers = msg.get('container-title') or []
        venue = fold(fm.get('venue', ''))
        if containers and not any(title_in(c, venue) for c in containers):
            short = msg.get('short-container-title') or []
            if not any(title_in(c, venue) for c in short):
                notes.append('期刊：頁面「%s」，Crossref「%s」' % (fm.get('venue', ''), containers[0]))

        if problems:
            mismatches += 1
            print('MISMATCH  %s  (%s)' % (slug, doi))
            for p in problems + notes:
                print('          - ' + p)
        elif notes:
            print('NOTE  %s  (%s)' % (slug, doi))
            for p in notes:
                print('          - ' + p)
        else:
            print('OK    %s' % slug)
        time.sleep(0.3)
    sys.exit(1 if mismatches else 0)


if __name__ == '__main__':
    main()
