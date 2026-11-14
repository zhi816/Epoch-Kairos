#!/usr/bin/env python3
"""html_to_pdf.py: 自動偵測本機可用瀏覽器將論文 HTML 編譯為 PDF 並檢查有效性。

遵循 academic-paper-translator 第 40 條「不寫死瀏覽器安裝路徑；等待產檔程序完成並確認輸出可開啟」。
支援 Windows / macOS / Linux 上之 Chrome / Edge / Chromium；含 `--virtual-time-budget` 以確保
KaTeX 數學公式與字型於 `--print-to-pdf` 前完成排版。

用法：
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out_原版翻譯.pdf
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out_單欄翻譯.pdf --mode mobile
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out.pdf --budget-ms 10000
"""
import argparse
import os
import pathlib
import platform
import re
import shutil
import subprocess
import sys
import tempfile

try:
    import pymupdf
except ImportError:  # pragma: no cover
    import fitz as pymupdf  # type: ignore


def find_browser():
    """跨平台偵測 Chrome / Edge / Chromium 可執行檔，不寫死單一機器路徑。"""
    env_bin = os.environ.get('EK_BROWSER_BIN')
    if env_bin and os.path.isfile(env_bin):
        return env_bin

    candidates = []
    sys_name = platform.system()
    if sys_name == 'Windows':
        for root in (
            os.environ.get('PROGRAMFILES', r'C:\Program Files'),
            os.environ.get('PROGRAMFILES(X86)', r'C:\Program Files (x86)'),
            os.environ.get('LOCALAPPDATA', ''),
        ):
            if not root:
                continue
            candidates.extend([
                os.path.join(root, 'Google', 'Chrome', 'Application', 'chrome.exe'),
                os.path.join(root, 'Microsoft', 'Edge', 'Application', 'msedge.exe'),
                os.path.join(root, 'Chromium', 'Application', 'chrome.exe'),
            ])
        for cmd in ('chrome', 'chrome.exe', 'msedge', 'msedge.exe'):
            hit = shutil.which(cmd)
            if hit:
                candidates.append(hit)
    elif sys_name == 'Darwin':
        candidates.extend([
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
            '/Applications/Chromium.app/Contents/MacOS/Chromium',
        ])
        for cmd in ('google-chrome', 'chromium'):
            hit = shutil.which(cmd)
            if hit:
                candidates.append(hit)
    else:
        for cmd in ('google-chrome', 'chromium', 'chromium-browser', 'microsoft-edge'):
            hit = shutil.which(cmd)
            if hit:
                candidates.append(hit)

    for path in candidates:
        if path and os.path.isfile(path):
            return path
    return None


MOBILE_OVERRIDE_CSS = """
/* === Epoch-Kairos Single-Column Mobile Print Recipe (--mode mobile) === */
@page {
    size: A4 portrait !important;
    margin: 12mm 14mm 15mm 14mm !important;
    @top-left { content: none !important; }
    @top-right { content: none !important; }
    @bottom-center {
        content: counter(page);
        font-family: "Times New Roman", "Noto Serif", "Noto Serif TC", serif;
        font-size: 10.5pt;
        color: #333;
    }
}
@page :first {
    @bottom-center {
        content: counter(page);
    }
}
body {
    font-size: 13.5pt !important;
    line-height: 1.65 !important;
}
.title-block {
    margin-bottom: 16pt !important;
}
.paper-title-zh {
    font-size: 19pt !important;
    line-height: 1.35 !important;
}
.paper-title-en {
    font-size: 11.5pt !important;
    line-height: 1.35 !important;
}
.authors { font-size: 12.5pt !important; }
.affil { font-size: 11.5pt !important; }
.emails { font-size: 10pt !important; }
.abstract-title {
    font-size: 14.5pt !important;
    margin: 8pt 0 8pt 0 !important;
}
h1.sec {
    font-size: 15pt !important;
    margin: 18pt 0 7pt 0 !important;
}
h2.subsec {
    font-size: 13.5pt !important;
    margin: 14pt 0 6pt 0 !important;
}
p {
    margin: 0 0 8pt 0 !important;
}
ol.steps li {
    margin-bottom: 7pt !important;
}
.two-col, .two-col-auto, .one-col {
    column-count: 1 !important;
    column-gap: 0 !important;
}
.span-all, .col-span-all {
    column-span: none !important;
}
.page-break {
    display: none !important;
    height: 0 !important;
    break-before: auto !important;
    page-break-before: auto !important;
}
.venue-footer {
    margin: 12pt 0 14pt 0 !important;
    padding: 6pt 0 !important;
    border-top: 0.6pt solid #ccc !important;
    border-bottom: 0.6pt solid #ccc !important;
    font-size: 10pt !important;
    line-height: 1.45 !important;
}
.venue-footer .orig-pg {
    font-size: 10.5pt !important;
}
.footnote-box {
    margin-top: 12pt !important;
    padding-top: 6pt !important;
    font-size: 10.5pt !important;
    line-height: 1.5 !important;
}
.refs p {
    font-size: 11pt !important;
    line-height: 1.5 !important;
    padding-left: 16pt !important;
    text-indent: -16pt !important;
    margin-bottom: 7pt !important;
}
.table-wrap, .table-wrap-wide {
    margin: 12pt 0 14pt 0 !important;
    break-inside: avoid !important;
    page-break-inside: avoid !important;
}
table.acl, table.booktabs, table.grid, table.minimal-band {
    width: 100% !important;
    font-size: 10pt !important;
    line-height: 1.38 !important;
}
table thead { display: table-header-group; }
table tr { break-inside: avoid; page-break-inside: avoid; }
.table-caption, .table-caption-center, .table-caption-top, .table-note {
    font-size: 11pt !important;
    line-height: 1.48 !important;
}
figure.fig-wrap {
    margin: 14pt 0 !important;
}
figure.fig-wrap img {
    width: 100% !important;
    max-width: 100% !important;
}
figcaption.fig-caption {
    font-size: 11pt !important;
    line-height: 1.5 !important;
}
.rater-box, .prompt-box, .algo-box {
    font-size: 11pt !important;
    line-height: 1.5 !important;
}
code, .mono, pre {
    font-size: 10.5pt !important;
}
.katex-display {
    font-size: 0.96em !important;
}
"""


def inject_override_css(html_abs, extra_css):
    """在暫存同目錄 HTML 中注入補充 CSS，保留相對圖檔路徑並於編譯後刪除。"""
    with open(html_abs, 'r', encoding='utf-8') as f:
        src = f.read()
    style_tag = f'\n<style id="ek-override-css">\n{extra_css}\n</style>\n'
    if re.search(r'</head>', src, flags=re.IGNORECASE):
        patched = re.sub(r'</head>', lambda _: style_tag + '</head>', src, count=1, flags=re.IGNORECASE)
    else:
        patched = style_tag + src
    html_dir = os.path.dirname(html_abs)
    fd, tmp_path = tempfile.mkstemp(prefix='._tmp_compile_', suffix='.html', dir=html_dir)
    os.close(fd)
    with open(tmp_path, 'w', encoding='utf-8') as f:
        f.write(patched)
    return tmp_path


def compile_pdf(html_path, pdf_path, budget_ms=8000, timeout_sec=120, mode='original', extra_css_path=None):
    browser = find_browser()
    if not browser:
        raise RuntimeError('找不到 Chrome / Edge / Chromium 執行檔，可設定環境變數 EK_BROWSER_BIN 指定路徑。')

    html_abs = os.path.abspath(html_path)
    pdf_abs = os.path.abspath(pdf_path)
    parent = os.path.dirname(pdf_abs)
    if parent:
        os.makedirs(parent, exist_ok=True)

    css_parts = []
    if mode == 'mobile':
        css_parts.append(MOBILE_OVERRIDE_CSS)
    if extra_css_path:
        with open(extra_css_path, 'r', encoding='utf-8') as cf:
            css_parts.append(cf.read())

    tmp_html = None
    target_html = html_abs
    if css_parts:
        tmp_html = inject_override_css(html_abs, '\n'.join(css_parts))
        target_html = tmp_html

    try:
        uri = pathlib.Path(target_html).as_uri()
        cmd = [
            browser,
            '--headless=new',
            '--disable-gpu',
            '--no-sandbox',
            '--no-pdf-header-footer',
            '--allow-file-access-from-files',
            f'--virtual-time-budget={int(budget_ms)}',
            f'--print-to-pdf={pdf_abs}',
            uri,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_sec)
        if res.returncode != 0:
            raise RuntimeError(f'瀏覽器結束代碼 {res.returncode}: {res.stderr.strip()}')
    finally:
        if tmp_html and os.path.exists(tmp_html):
            try:
                os.remove(tmp_html)
            except OSError:
                pass
    if not os.path.isfile(pdf_abs) or os.path.getsize(pdf_abs) < 512:
        raise RuntimeError(f'未產生有效 PDF 檔案：{pdf_abs}')

    with open(pdf_abs, 'rb') as f:
        head = f.read(8)
        f.seek(max(0, os.path.getsize(pdf_abs) - 64))
        tail = f.read()
    if not head.startswith(b'%PDF-') or b'%%EOF' not in tail:
        raise RuntimeError('PDF 檔頭或 %%EOF 結尾標記不完整')

    doc = pymupdf.open(pdf_abs)
    try:
        pages = len(doc)
        if pages <= 0:
            raise RuntimeError('產出之 PDF 頁數為 0')
        rect = doc[0].rect
        return {
            'browser': browser,
            'pdf': pdf_abs,
            'pages': pages,
            'size_bytes': os.path.getsize(pdf_abs),
            'first_page_pt': [round(rect.width, 2), round(rect.height, 2)],
        }
    finally:
        doc.close()


def main():
    parser = argparse.ArgumentParser(description='使用本機 Chrome/Edge/Chromium 將論文 HTML 轉為 PDF 並檢查。')
    parser.add_argument('html', help='輸入 HTML 檔案路徑')
    parser.add_argument('pdf', help='輸出 PDF 檔案路徑')
    parser.add_argument('--mode', choices=('original', 'mobile'), default='original',
                        help='輸出模式：original 依原稿 HTML 版面；mobile 強制轉為單欄大字手機閱讀版')
    parser.add_argument('--css', help='額外注入之 CSS 樣式表檔案路徑（可微調字級或表格）')
    parser.add_argument('--budget-ms', type=int, default=8000, help='等待字型與 KaTeX 渲染的虛擬時間預算毫秒數（預設 8000）')
    args = parser.parse_args()

    if not os.path.isfile(args.html):
        print(f'找不到輸入 HTML: {args.html}', file=sys.stderr)
        return 1
    if args.css and not os.path.isfile(args.css):
        print(f'找不到指定 CSS 檔: {args.css}', file=sys.stderr)
        return 1

    try:
        info = compile_pdf(args.html, args.pdf, budget_ms=args.budget_ms, mode=args.mode, extra_css_path=args.css)
        print(f"瀏覽器: {info['browser']}")
        print(f"已產生: {info['pdf']} ({info['pages']} 頁, {info['size_bytes']} bytes, 第一頁 {info['first_page_pt']} pt)")
        return 0
    except Exception as exc:
        print(f'產檔失敗: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
