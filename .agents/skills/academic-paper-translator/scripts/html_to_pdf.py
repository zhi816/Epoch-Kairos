#!/usr/bin/env python3
"""html_to_pdf.py: 自動偵測本機可用瀏覽器將論文 HTML 編譯為 PDF 並檢查有效性。

遵循 academic-paper-translator 第 40 條「不寫死瀏覽器安裝路徑；等待產檔程序完成並確認輸出可開啟」。
支援 Windows / macOS / Linux 上之 Chrome / Edge / Chromium；含 `--virtual-time-budget` 以確保
KaTeX 數學公式與字型於 `--print-to-pdf` 前完成排版。

用法：
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out.pdf
    python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/out.html out.pdf --budget-ms 10000
"""
import argparse
import os
import pathlib
import platform
import shutil
import subprocess
import sys

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


def compile_pdf(html_path, pdf_path, budget_ms=8000, timeout_sec=120):
    browser = find_browser()
    if not browser:
        raise RuntimeError('找不到 Chrome / Edge / Chromium 執行檔，可設定環境變數 EK_BROWSER_BIN 指定路徑。')

    html_abs = os.path.abspath(html_path)
    pdf_abs = os.path.abspath(pdf_path)
    parent = os.path.dirname(pdf_abs)
    if parent:
        os.makedirs(parent, exist_ok=True)

    uri = pathlib.Path(html_abs).as_uri()
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
    parser.add_argument('--budget-ms', type=int, default=8000, help='等待字型與 KaTeX 渲染的虛擬時間預算毫秒數（預設 8000）')
    args = parser.parse_args()

    if not os.path.isfile(args.html):
        print(f'找不到輸入 HTML: {args.html}', file=sys.stderr)
        return 1

    try:
        info = compile_pdf(args.html, args.pdf, budget_ms=args.budget_ms)
        print(f"瀏覽器: {info['browser']}")
        print(f"已產生: {info['pdf']} ({info['pages']} 頁, {info['size_bytes']} bytes, 第一頁 {info['first_page_pt']} pt)")
        return 0
    except Exception as exc:
        print(f'產檔失敗: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
