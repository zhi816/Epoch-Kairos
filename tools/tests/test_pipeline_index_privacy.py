"""Behavioral checks for S5 index routing between wiki/index.md and raw/my-focus/my-index.md."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / '.agents/skills/paper-pipeline/scripts/pipeline_status.py'
SPEC = importlib.util.spec_from_file_location('pipeline_status', SCRIPT)
pipeline = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pipeline)


class PrivacyIndexRoutingTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'wiki/papers').mkdir(parents=True)
        (self.root / 'wiki/evidence').mkdir(parents=True)
        (self.root / 'wiki/cards').mkdir(parents=True)
        (self.root / 'web/papers').mkdir(parents=True)
        self.originals = (pipeline.ROOT, pipeline.WIKI, pipeline.RAW)
        pipeline.ROOT = str(self.root)
        pipeline.WIKI = str(self.root / 'wiki')
        pipeline.RAW = str(self.root / 'raw')

    def tearDown(self):
        pipeline.ROOT, pipeline.WIKI, pipeline.RAW = self.originals
        self.tmp.cleanup()

    def _run_s5(self, slug, my_focus, index_text='', my_index_text=None):
        page_path = self.root / f'wiki/papers/{slug}.md'
        page_path.write_text(
            f'---\nconcepts: ["c1"]\nmy_focus: {"true" if my_focus else "false"}\n---\n',
            encoding='utf-8',
        )
        ctx = {
            'papers': [slug],
            'lint': {},
            'cards': {},
            'home_ok': True,
            'home_msg': '',
            'home': (set(), set(), set(), {}),
            'open': {},
            'index': index_text,
            'my_index': my_index_text,
            'log': '',
            'concepts': {'c1': {'papers': [slug]}},
        }
        return pipeline.check(slug, ctx)['S5']

    def test_focus_paper_checks_private_my_index(self):
        slug = '2026-focus-sample'
        state, why = self._run_s5(
            slug, True,
            index_text='',
            my_index_text=f'* `2026` ｜ [Test](../../wiki/papers/{slug}.md)\n',
        )
        self.assertEqual(state, 'OK', why)
        self.assertIn('my-index.md', why[0])

    def test_focus_paper_fails_when_missing_from_my_index(self):
        slug = '2026-focus-missing'
        state, why = self._run_s5(slug, True, index_text=f'(papers/{slug}.md)', my_index_text='')
        self.assertEqual(state, 'NG')
        self.assertIn('raw/my-focus/my-index.md', why[0])

    def test_focus_paper_returns_unknown_when_raw_absent(self):
        slug = '2026-focus-no-raw'
        state, why = self._run_s5(slug, True, index_text='', my_index_text=None)
        self.assertEqual(state, '--', why)

    def test_star_paper_still_checks_public_index(self):
        slug = '2026-star-sample'
        state_ng, _ = self._run_s5(slug, False, index_text='', my_index_text=f'(../../wiki/papers/{slug}.md)')
        self.assertEqual(state_ng, 'NG')
        state_ok, why = self._run_s5(slug, False, index_text=f'* [Star](papers/{slug}.md)\n', my_index_text=None)
        self.assertEqual(state_ok, 'OK', why)


if __name__ == '__main__':
    unittest.main()
