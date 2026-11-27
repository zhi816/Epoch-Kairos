"""問題條目須寫明誰發現、誰修正（lint_wiki.py；AGENTS.md 第七章第 4 節，EK-234 起）。"""

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / '.agents/skills/wiki-content-audit/scripts/lint_wiki.py'
SPEC = importlib.util.spec_from_file_location('lint_wiki', SCRIPT)
lint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lint)


def entry(num, found, fix):
    return ('### EK-%03d | fixed | papers/x.md | Card 3 | 原文不符\n'
            '- **問題**：測試。\n- **來源**：p. 1\n- **發現於**：%s\n- **處理**：%s\n' % (num, found, fix))


class IssueAgentTest(unittest.TestCase):
    def setUp(self):
        lint.results.clear()
        self.tmp = tempfile.TemporaryDirectory()
        Path(self.tmp.name, 'wiki/papers').mkdir(parents=True)
        Path(self.tmp.name, 'wiki/papers/x.md').write_text('---\n---\n', encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def errors(self, text):
        lint._parse_issue_file(self.tmp.name, 'wiki/issues.md', text, {})
        return [m for lvl, _p, _l, m in lint.results if lvl == 'ERROR' and '代理名稱' in m]

    def test_new_issue_with_named_agents_passes(self):
        text = entry(234, '2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash）提出，Claude Code by Anthropic（Claude Opus 5.5）核對。',
                     '2026-11-28，Claude Code by Anthropic（Claude Opus 5.5）。改回原文寫法。')
        self.assertEqual(self.errors(text), [])

    def test_new_issue_with_only_log_reference_fails(self):
        text = entry(235, 'wiki/log.md [2026-11-28 10:00] audit', '2026-11-28，改回原文寫法。')
        self.assertEqual(len(self.errors(text)), 2)

    def test_user_as_finder_passes(self):
        text = entry(236, '2026-11-28，使用者指出。', '2026-11-28，Codex by OpenAI（GPT-6）。修正。')
        self.assertEqual(self.errors(text), [])

    def test_old_issue_is_not_checked(self):
        text = entry(33, 'wiki/log.md [2026-11-08 22:35] audit', '2026-11-09，修正。')
        self.assertEqual(self.errors(text), [])


if __name__ == '__main__':
    unittest.main()
