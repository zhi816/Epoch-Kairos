import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from wiki_redirects import is_redirect, is_redirect_text
import build_home


class WikiRedirectTests(unittest.TestCase):
    def test_only_first_line_marker_defines_redirect(self):
        self.assertTrue(is_redirect_text('<!-- epoch-kairos:redirect -->\n# Moved\n'))
        self.assertFalse(is_redirect_text('# Paper\n<!-- epoch-kairos:redirect -->\n'))
        self.assertFalse(is_redirect_text(''))

    def test_woodford_legacy_paths_resolve_without_alias_chains(self):
        old = '2007-woodford-inflation-dynamics.md'
        new = '2007-woodford-globalization-monetary-control.md'
        for section in ('papers', 'evidence', 'cards'):
            with self.subTest(section=section):
                alias = ROOT / 'wiki' / section / old
                target = alias.parent / new
                self.assertTrue(is_redirect(alias))
                self.assertIn('(%s)' % new, alias.read_text(encoding='utf-8'))
                self.assertTrue(target.is_file())
                self.assertFalse(is_redirect(target))

    def test_published_legacy_url_has_relative_fallback(self):
        page = ROOT / 'web/papers/2007-woodford-inflation-dynamics/index.html'
        html = page.read_text(encoding='utf-8')
        match = re.search(r'href="([^"]+)"', html)
        self.assertIsNotNone(match)
        self.assertTrue((page.parent / match.group(1) / 'index.html').is_file())
        self.assertIn('http-equiv="refresh"', html)

    def test_wall_ignores_redirect_even_when_it_is_in_git_index(self):
        with tempfile.TemporaryDirectory() as tmp:
            cards_dir = Path(tmp) / 'cards'
            cards_dir.mkdir()
            (cards_dir / 'new.md').write_text('# Normal card\n', encoding='utf-8')
            (cards_dir / 'old.md').write_text('<!-- epoch-kairos:redirect -->\n', encoding='utf-8')
            files = {'wiki/cards/new.md': 'new-hash', 'wiki/cards/old.md': 'old-hash'}
            blobs = {'new-hash': '# Normal card\n', 'old-hash': '<!-- epoch-kairos:redirect -->\n'}
            with patch.object(build_home, 'WIKI', tmp), \
                 patch.object(build_home, 'indexed', side_effect=[(files, []), ({}, [])]), \
                 patch.object(build_home, 'read_blobs', return_value=blobs):
                cards, _, errors, _, _ = build_home.wall_sources({'new': {}}, set())
            self.assertEqual(set(cards), {'new'})
            self.assertEqual(errors, [])


if __name__ == '__main__':
    unittest.main()
