#!/usr/bin/env python3
"""html_to_pdf.py: 自動偵測本機可用瀏覽器將論文 HTML 編譯為 PDF 並檢查有效性。

遵循 academic-paper-translator 第 40 條「不寫死瀏覽器安裝路徑；等待產檔程序完成並確認輸出可開啟」。
支援 Windows / macOS / Linux 上之 Chrome / Edge / Chromium；含 `--virtual-time-budget` 以確保
KaTeX 數學公式與字型於 `--print-to-pdf` 前完成排版。

用法：
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out_原版翻譯.pdf
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out_單欄翻譯.pdf --mode mobile
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out.pdf --budget-ms 10000
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py --check out_單欄翻譯.pdf --mode mobile

產檔後自動檢查（未通過時結束代碼 3）：PDF 中不得殘留 TeX 原始碼（公式未渲染）；mobile 模式另檢查
字級 12.5pt 以上之文字至少 20%、從頁面右半開始之文字行不超過 15%（確認覆寫樣式真的變成單欄）。
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


# 本機 Python 沒有 PyMuPDF 時（macOS 系統 Python 通常沒有），改用倉庫根目錄 .venv-mineru 之 Python 重新執行，
# 與 paper-pdf-parser 之 parse_pdf.py 相同；Windows 與 macOS 皆適用。
REEXEC_FLAG = 'EK_TRANSLATOR_REEXEC'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
VENV_PY = os.path.join(ROOT, '.venv-mineru', 'Scripts' if platform.system() == 'Windows' else 'bin',
                       'python.exe' if platform.system() == 'Windows' else 'python')


def _has_pymupdf():
    try:
        import pymupdf  # noqa: F401
        return True
    except ImportError:
        try:
            import fitz  # noqa: F401
            return True
        except ImportError:
            return False


if not _has_pymupdf():
    if not os.environ.get(REEXEC_FLAG) and os.path.exists(VENV_PY):
        sys.exit(subprocess.run([VENV_PY, os.path.abspath(__file__)] + sys.argv[1:],
                                env=dict(os.environ, **{REEXEC_FLAG: '1'})).returncode)
    sys.stderr.write('錯誤：找不到 PyMuPDF。請依 paper-pdf-parser 說明建立 .venv-mineru，或以 pip install pymupdf 安裝。\n')
    sys.exit(1)

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
/* 任何元素之多欄設定一律取消，不依賴特定 class 名稱；以 grid 或 flex 排成兩欄者由產檔後之單欄檢查擋下 */
*, .two-col, .two-col-auto, .one-col {
    columns: auto !important;
    column-count: auto !important;
    column-gap: 0 !important;
}
.span-all, .col-span-all {
    column-span: none !important;
}
/* 原稿為對齊雙欄而加之強迫分頁全數取消；有意義之分頁（如附錄前）加 class keep-mobile 保留 */
.page-break:not(.keep-mobile) {
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
            '--no-pdf-header-footer',
            '--allow-file-access-from-files',
            f'--virtual-time-budget={int(budget_ms)}',
            f'--print-to-pdf={pdf_abs}',
            uri,
        ]
        if platform.system() == 'Linux':
            cmd.insert(1, '--no-sandbox')  # 僅 Linux 容器或 root 環境需要；桌面 Windows 與 macOS 不關沙盒
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

    info = inspect_pdf(pdf_abs, mode)
    info['browser'] = browser
    return info


# 公式未渲染時 PDF 會印出 TeX 原始碼（KaTeX 未載入或 katex-error 皆然）
RAW_TEX_RE = re.compile(r'\\(?:frac|mathrm|mathbf|mathcal|text|sum|prod|int|sqrt|left|right|begin|end|cdot|times|'
                        r'alpha|beta|gamma|delta|theta|lambda|mu|sigma|log|exp|hat|bar|tilde|operatorname)\b|\$\$')
MOBILE_LARGE_PT = 12.5          # 單欄版內文覆寫為 13.5pt；表格、圖說與參考文獻另為 10-11pt
MOBILE_MIN_LARGE_SHARE = 0.20   # 字級達 12.5pt 之字元比例下限；既有單欄版 30-57%，原版 0%
MOBILE_MAX_RIGHT_RATIO = 0.15   # 起點落在頁面右半之文字行比例上限；單欄版 0-1%，雙欄版約五成


def inspect_pdf(pdf_abs, mode='original'):
    """量測已產出之 PDF：頁數、尺寸；檢查公式是否未渲染，mobile 模式另檢查是否真為單欄大字。"""
    doc = pymupdf.open(pdf_abs)
    try:
        pages = len(doc)
        if pages <= 0:
            raise RuntimeError('產出之 PDF 頁數為 0')
        rect = doc[0].rect
        tex_hits, sizes, lines = [], [], []  # sizes：每字元之字級；lines：(字元數, 行起點 x / 頁寬)
        for pno, page in enumerate(doc, 1):
            for m in RAW_TEX_RE.finditer(page.get_text()):
                tex_hits.append('第 %d 頁：%s' % (pno, m.group(0)))
            w = page.rect.width
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines', []):
                    spans = [sp for sp in line['spans'] if sp['text'].strip()]
                    if not spans:
                        continue
                    n = sum(len(sp['text'].strip()) for sp in spans)
                    size = max(spans, key=lambda sp: len(sp['text']))['size']
                    sizes.extend([round(size, 1)] * n)
                    lines.append((n, line['bbox'][0] / w))
        problems = []
        if tex_hits:
            problems.append('疑似公式未渲染（PDF 中出現 TeX 原始碼）%d 處，例：%s' % (len(tex_hits), '；'.join(tex_hits[:5])))
        large_share = sum(1 for x in sizes if x >= MOBILE_LARGE_PT) / len(sizes) if sizes else 0.0
        right_ratio = 0.0
        if mode == 'mobile':
            body = [(n, x) for n, x in lines if n >= 8]  # 短行（表格儲存格、式號、頁碼）不計
            if body:
                right_ratio = sum(n for n, x in body if x >= 0.5) / sum(n for n, _ in body)
            if large_share < MOBILE_MIN_LARGE_SHARE:
                problems.append('單欄版只有 %.0f%% 文字達 %.1fpt，內文放大之覆寫樣式可能未套用'
                                % (large_share * 100, MOBILE_LARGE_PT))
            if right_ratio > MOBILE_MAX_RIGHT_RATIO:
                problems.append('單欄版有 %.0f%% 內文行從頁面右半開始，仍像雙欄排版（可能以 grid／flex 或其他方式分欄）'
                                % (right_ratio * 100))
        return {
            'pdf': pdf_abs,
            'pages': pages,
            'size_bytes': os.path.getsize(pdf_abs),
            'first_page_pt': [round(rect.width, 2), round(rect.height, 2)],
            'large_share': round(large_share, 3),
            'right_ratio': round(right_ratio, 3),
            'problems': problems,
        }
    finally:
        doc.close()


def main():
    parser = argparse.ArgumentParser(description='使用本機 Chrome/Edge/Chromium 將論文 HTML 轉為 PDF 並檢查。')
    parser.add_argument('html', nargs='?', help='輸入 HTML 檔案路徑（搭配 --check 時省略）')
    parser.add_argument('pdf', nargs='?', help='輸出 PDF 檔案路徑')
    parser.add_argument('--check', metavar='PDF', help='不產檔，只檢查既有 PDF（公式渲染；--mode mobile 時另查單欄與字級）')
    parser.add_argument('--mode', choices=('original', 'mobile'), default='original',
                        help='輸出模式：original 依原稿 HTML 版面；mobile 強制轉為單欄大字手機閱讀版')
    parser.add_argument('--css', help='額外注入之 CSS 樣式表檔案路徑（可微調字級或表格）')
    parser.add_argument('--budget-ms', type=int, default=8000, help='等待字型與 KaTeX 渲染的虛擬時間預算毫秒數（預設 8000）')
    args = parser.parse_args()

    if args.check:
        if not os.path.isfile(args.check):
            print(f'找不到 PDF: {args.check}', file=sys.stderr)
            return 1
        return report(inspect_pdf(os.path.abspath(args.check), args.mode))
    if not args.html or not args.pdf:
        parser.error('需要輸入 HTML 與輸出 PDF 路徑')
    if not os.path.isfile(args.html):
        print(f'找不到輸入 HTML: {args.html}', file=sys.stderr)
        return 1
    if args.css and not os.path.isfile(args.css):
        print(f'找不到指定 CSS 檔: {args.css}', file=sys.stderr)
        return 1

    try:
        info = compile_pdf(args.html, args.pdf, budget_ms=args.budget_ms, mode=args.mode, extra_css_path=args.css)
        print(f"瀏覽器: {info['browser']}")
    except Exception as exc:
        print(f'產檔失敗: {exc}', file=sys.stderr)
        return 2
    return report(info)


def report(info):
    print(f"PDF: {info['pdf']} ({info['pages']} 頁, {info['size_bytes']} bytes, 第一頁 {info['first_page_pt']} pt, "
          f"{MOBILE_LARGE_PT}pt 以上文字 {info['large_share']:.0%}, 右半起始行 {info['right_ratio']:.0%})")
    if info['problems']:
        for p in info['problems']:
            print(f'ERROR: {p}', file=sys.stderr)
        print('檢查未通過：PDF 已寫出但不可交付，修正 HTML 後重新產檔。', file=sys.stderr)
        return 3
    print('檢查通過')
    return 0


if __name__ == '__main__':
    sys.exit(main())
