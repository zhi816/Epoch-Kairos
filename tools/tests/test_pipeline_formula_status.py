"""Behavioral checks for S3 formula evidence completeness."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / '.agents/skills/paper-pipeline/scripts/pipeline_status.py'
SPEC = importlib.util.spec_from_file_location('pipeline_status', SCRIPT)
pipeline = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pipeline)


class FormulaEvidenceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.original_root = pipeline.ROOT
        pipeline.ROOT = self.tmp.name
        self.evidence = Path(self.tmp.name) / 'wiki/evidence/example.md'
        self.evidence.parent.mkdir(parents=True)

    def tearDown(self):
        pipeline.ROOT = self.original_root
        self.tmp.cleanup()

    def check(self, rows, page):
        self.evidence.write_text(
            '| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |\n'
            '|---|---|---|---|---|\n' + rows, encoding='utf-8')
        return pipeline.check_evidence('example', page)

    def test_numeric_claims_do_not_cover_display_formulas(self):
        status, reasons = self.check(
            r'| Card 4 | $I = 30$、$k_B T/\hbar$ | 本篇研究結果 | p. 2 | 符合 |' + '\n',
            '$$x = y$$')
        self.assertEqual(status, 'WARN')
        self.assertIn('缺編號：1', ' '.join(reasons))

    def test_each_formula_requires_one_numbered_row(self):
        rows = (r'| Card 3 區塊公式 1 | $x = y$ | 本篇研究結果 | p. 2 式 (1) | 符合 |' + '\n'
                + r'| Card 3 區塊公式 2 | $\|x\| = 1$ | 作者解釋 | p. 3 | 符合 |' + '\n')
        status, reasons = self.check(rows, '$$x = y$$\n$$\\|x\\| = 1$$')
        self.assertEqual(status, 'OK', reasons)

    def test_legacy_evidence_table_headers_are_supported(self):
        self.evidence.write_text(
            '| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |\n'
            '|---|---|---|---|\n'
            '| Card 3 區塊公式 1 | x = y | p. 3 式 (1) | 符合 |\n',
            encoding='utf-8')
        status, reasons = pipeline.check_evidence('example', '$$x = y$$')
        self.assertEqual(status, 'OK', reasons)

    def test_duplicate_number_cannot_hide_missing_formula(self):
        row = '| Card 3 區塊公式 1 | x | 本篇研究結果 | p. 2 | 符合 |\n'
        status, reasons = self.check(row + row, '$$x$$\n$$y$$')
        self.assertEqual(status, 'WARN')
        self.assertIn('重複', ' '.join(reasons))
        self.assertIn('缺編號：1、2', ' '.join(reasons))

    def test_missing_source_and_stale_number_warn(self):
        rows = ('| Card 3 區塊公式 1 | x | 本篇研究結果 |  | 符合 |\n'
                '| Card 3 區塊公式 3 | y | 本篇研究結果 | p. 3 | 符合 |\n')
        status, reasons = self.check(rows, '$$x$$')
        self.assertEqual(status, 'WARN')
        self.assertIn('缺主張或第一手來源', ' '.join(reasons))
        self.assertIn('缺編號：1', ' '.join(reasons))
        self.assertIn('超出', ' '.join(reasons))

    def test_zero_formula_page_does_not_need_rows(self):
        status, reasons = self.check('', 'text\n```\n$$example$$\n```')
        self.assertEqual(status, 'OK', reasons)

    def test_escaped_dollar_in_inline_math_is_not_a_display_delimiter(self):
        page = r'邊界符號 $\$$ 與 $\$$。' + '\n$$x = y$$'
        rows = '| Card 3 區塊公式 1 | x | 本篇研究結果 | p. 2 | 符合 |\n'
        status, reasons = self.check(rows, page)
        self.assertEqual(status, 'OK', reasons)

    def test_summary_does_not_mark_warnings_or_unknown_as_complete(self):
        states = {step: ('OK', []) for step in pipeline.STEPS}
        self.assertEqual(pipeline.completion_status(states), ('OK', None))
        states['S3'] = ('WARN', ['公式缺來源'])
        self.assertEqual(pipeline.completion_status(states), ('WARN', 'S3'))
        states['S8'] = ('--', ['無法判斷'])
        self.assertEqual(pipeline.completion_status(states), ('--', 'S8'))
        states['S10'] = ('NG', ['尚未提交'])
        self.assertEqual(pipeline.completion_status(states), ('NG', 'S10'))


if __name__ == '__main__':
    unittest.main()
