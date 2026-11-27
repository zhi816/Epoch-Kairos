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


if __name__ == '__main__':
    unittest.main()
