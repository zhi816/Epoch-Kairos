#!/usr/bin/env python3
"""venue_short_lookup.py: 查詢論文頁可用之期刊簡稱候選（references/paper-page.md 第三節）。

只使用標準函式庫，查 Crossref 需要網路。於倉庫任意位置執行：
    python .agents/skills/paper-card-writer/scripts/venue_short_lookup.py <slug> [<slug> ...]
    python .agents/skills/paper-card-writer/scripts/venue_short_lookup.py --long          # 列出所有可能被截斷者
    python .agents/skills/paper-card-writer/scripts/venue_short_lookup.py --long --no-net # 不查 Crossref

每篇列出：venue、目前之 venue_short、首頁與論文頁實際顯示之簡稱、顯示長度與截斷風險，
以及 Crossref 之 container-title 與 short-container-title。
本腳本只提供候選，不寫入任何檔案：期刊或學會自己的縮寫須另查原文 PDF 之引用格式或期刊官網，
查不到第一手來源之縮寫須經使用者確認才可採用（paper-page.md 第三節）。
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'wiki-content-audit', 'scripts'))
from lint_wiki import frontmatter, read, repo_root  # noqa: E402

ROOT = repo_root()
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from build_home import venue_of, award_line  # noqa: E402

UA = 'Epoch-Kairos-venue-check/1.0'
# 卡片牆雙年份「YYYY 發表 ｜ 」之後的期刊名寬度（2026-11-10 以 verify_wall.js 實測，桌面與手機相同）：
# 10 個半形字元放得下（Nat Astron、Eng. Proc.），17 個被截斷（ACM Comput. Surv.、Findings of ACL 2024）。
WALL_FIT, WALL_CUT = 10, 17
INFO_LINE = 17   # 論文頁資訊欄每行約 17 個半形字元（tools/build_paper_prototype.py 之 VENUE_LINE_MAX）


def width(s):
    """半形字元計 1，全形字元計 2。"""
    return sum(2 if ord(c) > 0x2E7F else 1 for c in s)


def crossref(doi):
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/')
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)['message'], None
        except Exception as e:  # 網路逾時常見（2026-11-10 曾連續逾時），重試兩次
            err = e
            time.sleep(2 * (attempt + 1))
    return None, err


def risk(shown):
    w = width(shown)
    wall = ('放得下' if w <= WALL_FIT else '會被截斷' if w >= WALL_CUT else '不確定，須以 verify_wall.js 確認')
    lines = -(-w // INFO_LINE)
    return w, wall, lines


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    net = '--no-net' not in sys.argv
    long_only = '--long' in sys.argv
    papers = os.path.join(ROOT, 'wiki', 'papers')
    slugs = args or sorted(f[:-3] for f in os.listdir(papers) if f.endswith('.md'))
    shown_any = False
    for slug in slugs:
        path = os.path.join(papers, slug + '.md')
        if not os.path.exists(path):
            print('MISSING  %s：找不到 wiki/papers/%s.md' % (slug, slug))
            continue
        fm = frontmatter(read(path))[0] or {}
        if not fm.get('venue'):
            print('SKIP  %s：無 venue' % slug)
            continue
        shown = venue_of(fm)
        w, wall, lines = risk(shown)
        awarded = bool(award_line(fm))
        if long_only and not args and (w < WALL_CUT and lines <= 2 or awarded and lines <= 2):
            continue
        shown_any = True
        print('== %s' % slug)
        print('   venue          ：%s' % fm['venue'])
        print('   venue_short    ：%s' % (fm.get('venue_short') or '（未填，自動縮短）'))
        print('   顯示簡稱       ：%s（寬 %d）' % (shown, w))
        if awarded:
            print('   卡片牆雙年份   ：顯示獎項，不顯示期刊')
        else:
            print('   卡片牆雙年份   ：%s' % wall)
        print('   論文頁資訊欄   ：約 %d 行%s' % (lines, '（超過兩行，須處理）' if lines > 2 else ''))
        doi = re.sub(r'^https?://(dx\.)?doi\.org/', '', str(fm.get('doi_url') or '').strip())
        if not net:
            continue
        if not doi or doi == str(fm.get('doi_url') or '').strip():
            print('   Crossref       ：無 doi.org 之 doi_url，略過')
            continue
        msg, err = crossref(doi)
        if msg is None:
            print('   Crossref       ：查詢失敗（%s），稍後重試' % err)
            continue
        ct = (msg.get('container-title') or [''])[0]
        sct = msg.get('short-container-title') or []
        print('   container-title：%s' % (ct or '（無）'))
        if sct:
            for s in sct:
                print('   short-container-title：%s（寬 %d，卡片牆%s）' % (s, width(s), risk(s)[1]))
        else:
            print('   short-container-title：（無）；改查原文 PDF 首頁引用格式或期刊官網')
        time.sleep(0.3)
    if long_only and not shown_any:
        print('沒有可能被截斷之期刊簡稱。')


if __name__ == '__main__':
    main()
