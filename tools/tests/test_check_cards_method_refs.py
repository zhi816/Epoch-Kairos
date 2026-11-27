"""Card 3 方法出處檢查（check_cards.py；paper-card-writer 之 file-format.md 第八節）。"""

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / '.agents/skills/paper-card-writer/scripts/check_cards.py'
SPEC = importlib.util.spec_from_file_location('check_cards', SCRIPT)
cc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cc)

HEAD = '| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |\n|---|---|---|---|---|\n'
STEP = '03｜方法流程'


def evidence(*rows):
    return HEAD + ''.join(r + '\n' for r in rows)


class MethodRefTest(unittest.TestCase):
    def setUp(self):
        cc.results.clear()

    def run_check(self, raw, ev, enforced=True, sec=STEP, key='步驟'):
        cc.check_method_refs('card.md', [(sec, key, raw, cc.strip_method_refs(raw), 5)], ev, enforced)
        return [(lvl, msg) for lvl, _p, _l, msg in cc.results]

    def test_strip_removes_marker(self):
        self.assertEqual(cc.strip_method_refs('查表｜先查詞典再補檢索〔方法-1、方法-2〕'), '查表｜先查詞典再補檢索')

    def test_cited_row_with_original_passes(self):
        ev = evidence('| 方法-1 | 詞典查表，未命中再以 BM25 檢索〔原文：dictionary lookup, then BM25〕 | 本篇研究結果 | §3, p. 4 | 符合來源 |')
        self.assertEqual(self.run_check('查表｜先查詞典，未命中用 BM25〔方法-1〕', ev), [])

    def test_missing_row_is_error(self):
        out = self.run_check('查表｜先查詞典〔方法-3〕', evidence())
        self.assertTrue(any(l == 'ERROR' and '方法-3' in m for l, m in out))

    def test_row_without_original_is_error(self):
        ev = evidence('| 方法-1 | 詞典查表 | 本篇研究結果 | p. 4 | 符合來源 |')
        out = self.run_check('查表｜先查詞典〔方法-1〕', ev)
        self.assertTrue(any(l == 'ERROR' and '〔原文：' in m for l, m in out))

    def test_latin_term_absent_from_row_warns(self):
        ev = evidence('| 方法-1 | 最大二分匹配〔原文：maximum bipartite matching〕 | 本篇研究結果 | §3.3 | 符合來源 |')
        out = self.run_check('對齊｜以 fast_align 對齊詞〔方法-1〕', ev)
        self.assertTrue(any(l == 'WARN' and 'fast_align' in m for l, m in out))

    def test_latin_term_check_ignores_inline_math(self):
        ev = evidence('| 方法-1 | 內積〔原文：dot products〕 | 本篇研究結果 | §3.2 | 符合來源 |')
        out = self.run_check('查詢與鍵 $q \\cdot k$ 的內積衡量相符程度。〔方法-1〕', ev, sec='Card 3｜突破原理', key='說明')
        self.assertEqual(out, [])

    def test_replace_term_absent_from_row_warns(self):
        ev = evidence('| 方法-1 | 詞級模糊匹配〔原文：word-level fuzzy matching〕 | 本篇研究結果 | §4.3 | 符合來源 |')
        out = self.run_check('檢索｜以稠密檢索找例句〔方法-1〕', ev)
        self.assertTrue(any(l == 'WARN' and '稠密檢索' in m for l, m in out))

    def test_future_work_keyword_warns(self):
        ev = evidence('| 方法-1 | 構詞解析〔原文：morphological analysis〕 | 本篇研究結果 | §3 | 符合來源 |',
                      '| 未來工作 | 把構詞資訊導入翻譯〔關鍵詞：詞綴特徵、構詞資訊〕 | 作者解釋 | p. 33 | 符合來源 |')
        out = self.run_check('遷移｜把詞綴特徵送進翻譯模型〔方法-1〕', ev)
        self.assertTrue(any(l == 'WARN' and '未來工作' in m for l, m in out))

    def test_new_card_without_marker_is_error(self):
        out = self.run_check('查表｜先查詞典', evidence(), enforced=True)
        self.assertTrue(any(l == 'ERROR' and '行尾須標' in m for l, m in out))

    def test_old_card_without_marker_is_silent(self):
        self.assertEqual(self.run_check('查表｜先查詞典', evidence(), enforced=False), [])

    def test_marker_must_be_at_line_end(self):
        ev = evidence('| 方法-1 | 查表〔原文：lookup〕 | 本篇研究結果 | p. 4 | 符合來源 |')
        out = self.run_check('查表｜〔方法-1〕先查詞典', ev)
        self.assertTrue(any(l == 'ERROR' and '行尾' in m for l, m in out))


class PositionScopeTest(unittest.TestCase):
    """依位置比對（file-format.md 第九節）：新卡片只看位置對應本卡的證據表列。"""

    def setUp(self):
        cc.results.clear()

    def msgs(self):
        return [(lvl, msg) for lvl, _p, _l, msg in cc.results]

    def test_number_only_in_other_position_warns(self):
        ev = evidence('| Card 3 | 隨機初態約 85% 落入指定記憶 | 本篇研究結果 | p. 2557 | 符合來源 |')
        cc.check_number_scope('card.md', 5, 'Card 4', ['≈ 85%'], 'p. 2557', ev, 'Card 4｜決定性數據')
        self.assertTrue(any('只出現在證據表其他位置' in m for _l, m in self.msgs()))

    def test_number_in_own_position_with_matching_page_passes(self):
        ev = evidence('| Card 3、Card 4 | 隨機初態約 85% 落入指定記憶 | 本篇研究結果 | pp. 2556–2557 | 符合來源 |')
        cc.check_number_scope('card.md', 5, 'Card 4', ['≈ 85%'], 'p. 2557', ev, 'Card 4｜決定性數據')
        self.assertEqual(self.msgs(), [])

    def test_source_table_mismatch_warns(self):
        ev = evidence('| Card 5 | 單語基準 15.50 | 本篇研究結果 | 表 6–7，pp. 23–24 | 符合來源 |')
        cc.check_number_scope('card.md', 5, '05', ['15.50'], '表 21，p. 34', ev, '05｜結果')
        self.assertTrue(any('對不上' in m for _l, m in self.msgs()))

    def test_year_digits_do_not_count_as_number(self):
        self.assertFalse(cc.num_in('85', 'Amit et al. (1985)'))
        self.assertTrue(cc.num_in('85', '約 85% 落入'))
        self.assertFalse(cc.num_in('2.5', '12.5 倍'))

    def test_table_and_page_spellings_are_normalised(self):
        self.assertTrue(cc.src_in_row(cc.src_tokens('Table 2')[0], '| Card 4 | x | 本篇研究結果 | 表 2，p. 8 | 符合來源 |'))
        self.assertTrue(cc.src_in_row(cc.src_tokens('p. 2557')[0], 'pp. 2556–2557'))

    def test_strong_word_needs_own_position_row(self):
        scoped = '\n'.join(cc.rows_for(evidence('| Card 4 | 首次直接測到重力波〔原文：first direct detection〕 | 本篇研究結果 | p. 1 | 符合來源 |'),
                                       'Card 2｜世紀瓶頸'))
        cc.check_text('card.md', 5, 'Card 2｜世紀瓶頸', '標題', '首次測到', scoped, scoped=True)
        self.assertTrue(any('強斷言' in m for _l, m in self.msgs()))

    def test_focus_result_rows_labelled_card5_still_match(self):
        rows = cc.rows_for(evidence('| Card 5 | BLEU 16.34 | 本篇研究結果 | 表 2 | 符合來源 |'), '05｜結果')
        self.assertEqual(len(rows), 1)


class MarkerPlacementTest(unittest.TestCase):
    """標記只能放在 Card 3「說明」或 03「步驟」。"""

    def setUp(self):
        cc.results.clear()
        self.tmp = tempfile.TemporaryDirectory()
        self.original_wiki = cc.WIKI
        cc.WIKI = self.tmp.name
        for sub in ('papers', 'evidence', 'cards'):
            Path(self.tmp.name, sub).mkdir()
        Path(self.tmp.name, 'papers/x.md').write_text(
            '---\ntitle_zh: "測試"\nmy_focus: true\ncard_line: "測試"\n---\n', encoding='utf-8')
        Path(self.tmp.name, 'evidence/x.md').write_text(
            evidence('| 方法-1 | 查表〔原文：lookup〕 | 本篇研究結果 | p. 4 | 符合來源 |'), encoding='utf-8')
        self.original_new = cc.is_new_card
        cc.is_new_card = lambda path: False

    def tearDown(self):
        cc.WIKI = self.original_wiki
        cc.is_new_card = self.original_new
        self.tmp.cleanup()

    def test_marker_in_input_field_is_error(self):
        card = Path(self.tmp.name, 'cards/x.md')
        card.write_text('# 卡片文字：x\n\n## 03｜方法流程\n- 輸入：族語詞〔方法-1〕\n- 步驟：查表｜先查詞典〔方法-1〕\n', encoding='utf-8')
        cc.check_card(str(card), 'x', {})
        msgs = [m for lvl, _p, _l, m in cc.results if lvl == 'ERROR']
        self.assertTrue(any('只能標在' in m for m in msgs))
        self.assertFalse(any('行尾須標' in m for m in msgs))


class Card5FollowUpTest(unittest.TestCase):
    """新卡片之 Card 5：里程碑要對到證據表「後續研究」列；獎項要有官方來源。"""

    def setUp(self):
        cc.results.clear()
        self.tmp = tempfile.TemporaryDirectory()
        self.original_wiki = cc.WIKI
        cc.WIKI = self.tmp.name
        for sub in ('papers', 'evidence', 'cards'):
            Path(self.tmp.name, sub).mkdir()
        Path(self.tmp.name, 'papers/y.md').write_text(
            '---\ntitle_zh: "測試"\npaper_year: 2005\naward_year: 2026\nlaureates: "Robert E. Hall, Michael Woodford"\n'
            'honor: "2026 諾貝爾經濟學獎（測試）"\ncard_line: "測試"\n---\nShimer 2005 與 Pissarides 2009 的後續討論。\n',
            encoding='utf-8')
        self.original_new = cc.is_new_card
        cc.is_new_card = lambda path: True

    def tearDown(self):
        cc.WIKI = self.original_wiki
        cc.is_new_card = self.original_new
        self.tmp.cleanup()

    def run_card(self, rows):
        Path(self.tmp.name, 'evidence/y.md').write_text(evidence(*rows), encoding='utf-8')
        card = Path(self.tmp.name, 'cards/y.md')
        card.write_text('# 卡片文字：y\n\n## Card 5｜典範轉移\n- 標題：測試\n'
                        '- 里程碑：2005｜失業波動之謎｜Shimer 2005, AER 95:25-49\n'
                        '- 里程碑：2009｜工資僵固之爭論｜Pissarides 2009, Econometrica 77:1339-1369\n'
                        '- 里程碑：2026｜Hall 與 Woodford 獲諾貝爾經濟學獎｜獎項\n- 註記：測試\n', encoding='utf-8')
        cc.check_card(str(card), 'y', {})
        return [(lvl, m) for lvl, _p, _l, m in cc.results]

    def test_missing_follow_up_row_is_error_and_award_needs_official_source(self):
        out = self.run_card(['| Card 5 | Shimer 失業波動 | 後續研究 | Shimer (2005), AER 95:25–49, doi:10.1257/0002828053828572 | 符合來源 |'])
        self.assertTrue(any(l == 'ERROR' and 'Pissarides' in m and '後續研究' in m for l, m in out))
        self.assertFalse(any('Shimer' in m and '後續研究」列' in m for _l, m in out))
        self.assertTrue(any('官方來源' in m for _l, m in out))

    def test_follow_up_without_doi_warns_and_official_award_passes(self):
        out = self.run_card([
            '| Card 5 | Shimer 失業波動 | 後續研究 | Shimer (2005), AER 95:25–49 | 符合來源 |',
            '| Card 5 | Pissarides 工資僵固 | 後續研究 | Pissarides (2009), Econometrica 77:1339–1369, doi:10.3982/ECTA7562 | 符合來源 |',
            '| Card 5 | 2026 經濟學獎表彰語 | 後續研究 | https://www.nobelprize.org/prizes/economic-sciences/2026/summary/ | 符合來源 |'])
        self.assertTrue(any('沒有 DOI' in m for _l, m in out))
        self.assertFalse(any('官方來源' in m for _l, m in out))
        self.assertFalse(any('後續研究」列' in m for _l, m in out))


if __name__ == '__main__':
    unittest.main()
