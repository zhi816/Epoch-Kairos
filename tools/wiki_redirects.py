"""Identify Markdown compatibility redirects without treating them as wiki entries."""

REDIRECT_MARKER = '<!-- epoch-kairos:redirect -->'


def is_redirect_text(text):
    """Only an explicit first-line marker makes a Markdown file a redirect."""
    return bool(text) and text.splitlines()[0].strip() == REDIRECT_MARKER


def is_redirect(path):
    """Read only the marker; regular papers and cards remain ordinary entries."""
    try:
        with open(path, encoding='utf-8') as stream:
            return stream.readline().strip() == REDIRECT_MARKER
    except (OSError, UnicodeError):
        return False
