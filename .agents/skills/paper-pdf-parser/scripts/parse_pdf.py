#!/usr/bin/env python3
"""parse_pdf.py: 把論文 PDF 抽成附頁碼標記的 Markdown，供撰寫與查核時搜尋、定位頁碼。

用法（倉庫內任何位置皆可執行，macOS 與 Windows 通用）：
    python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/<檔名>.pdf
    python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/<檔名>.pdf --pages 1-3,8
    python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/<檔名>.pdf --engine mineru

引擎：
    pymupdf  以 PyMuPDF／pymupdf4llm 抽取 PDF 的文字層，每頁前加 <!-- pdf-page: N --> 標記。
             不辨識影像，掃描版論文的公式與雙欄順序可能錯亂。
    mineru   以 MinerU 在本機（或 Windows WSL2 隔離環境）解析版面、公式（轉為 LaTeX）與表格。
             較慢且不含頁碼標記，供抄寫公式草稿或讀取純圖片 PDF。失敗即報錯，不改用其他引擎。
    auto     （預設）先用 PyMuPDF；過半頁面沒有文字層（純圖片 PDF）或文字層為亂碼（字型編碼錯誤）
             且 MinerU 可用時，改用 MinerU，並在終端與輸出檔註明。

一律只在本機解析：本腳本不會傳入 MinerU 的 --remote、--remote-url 或 --api-key，
因 raw/ 含未公開之學位論文與私人資料。輸出預設為 work/parsed/<檔名>/（已列入 .gitignore）。
輸出僅供搜尋與定位，不得作為證據；證據表一律回原 PDF 引用印刷頁碼、表或圖。

結束代碼：0 成功；1 輸入或環境錯誤；2 解析失敗。
"""
import argparse
import datetime
import glob
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

REEXEC_FLAG = 'EK_PARSE_PDF_REEXEC'
MINERU_TIER = 'basic'  # 只用版面、公式、OCR 與表格小模型；standard 另需視覺語言模型
MIN_PAGE_CHARS = 50  # 少於此字數之頁面視為缺少文字層（多為掃描影像）
STOPWORDS = {'the', 'of', 'and', 'to', 'in', 'is', 'that', 'for', 'we', 'with', 'are', 'this', 'by', 'on'}


def looks_garbled(text):
    """英文頁面幾乎找不到常用字時，視為字型編碼錯誤之亂碼文字層（例如字母整體位移）。
    中文等非拉丁文字頁面不判定。"""
    letters = sum(c.isascii() and c.isalpha() for c in text)
    cjk = sum('\u3400' <= c <= '\u9fff' for c in text)
    if letters < 300 or cjk > 50:
        return False
    words = re.findall(r'[A-Za-z]+', text)
    hits = sum(w.lower() in STOPWORDS for w in words)
    return hits < max(3, len(words) * 0.02)


def repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        out = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=here,
                             capture_output=True, check=True)
        return out.stdout.decode().strip()
    except Exception:
        return os.path.abspath(os.path.join(here, '..', '..', '..', '..'))


ROOT = repo_root()
VENV = os.path.join(ROOT, '.venv-mineru')
BIN = os.path.join(VENV, 'Scripts' if platform.system() == 'Windows' else 'bin')
EXE = '.exe' if platform.system() == 'Windows' else ''
VENV_PY = os.path.join(BIN, 'python' + EXE)
MINERU_KIT = os.path.join(BIN, 'mineru-kit' + EXE)


def taipei_now():
    t = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)
    return t.strftime('%Y-%m-%d %H:%M')


def parse_pages(spec, count):
    """'all' 或 '1-5,8'（1 起算）轉為 0 起算之頁序清單。"""
    if spec in (None, '', 'all'):
        return list(range(count))
    pages = []
    for part in spec.split(','):
        part = part.strip()
        if '-' in part:
            a, b = part.split('-', 1)
            lo, hi = int(a), int(b)
        else:
            lo = hi = int(part)
        if lo < 1 or hi > count or lo > hi:
            raise ValueError('頁碼 %s 超出範圍（本檔共 %d 頁）' % (part, count))
        pages.extend(range(lo - 1, hi))
    return sorted(set(pages))


def describe_pages(pages, count):
    if pages == list(range(count)):
        return '全部 %d 頁' % count
    spans, start, prev = [], None, None
    for p in pages:
        if start is None:
            start = prev = p
        elif p == prev + 1:
            prev = p
        else:
            spans.append((start, prev)); start = prev = p
    spans.append((start, prev))
    return ','.join(str(a + 1) if a == b else '%d-%d' % (a + 1, b + 1) for a, b in spans) + '（共 %d 頁）' % count


def header(src, engine, pages_desc, extra=''):
    return ('<!--\n'
            'source: %s\n'
            'engine: %s\n'
            'pages: %s；pdf-page 為 PDF 檔內頁序，不一定等於期刊印刷頁碼\n'
            'generated: %s (UTC+8)\n'
            'note: 本檔為搜尋與定位輔助，不得作為證據。證據表一律回原 PDF 核對，引用印刷頁碼、表或圖。\n'
            '%s-->\n') % (src, engine, pages_desc, taipei_now(), extra)


def has_pymupdf():
    try:
        import pymupdf  # noqa: F401
        return True
    except ImportError:
        return False


def maybe_reexec():
    """目前的 Python 沒有 PyMuPDF 而 .venv-mineru 存在時，改用其 Python 重新執行本腳本。"""
    if has_pymupdf() or os.environ.get(REEXEC_FLAG) or not os.path.exists(VENV_PY):
        return
    env = dict(os.environ, **{REEXEC_FLAG: '1'})
    sys.exit(subprocess.run([VENV_PY, os.path.abspath(__file__)] + sys.argv[1:], env=env).returncode)


def dist_version(name):
    try:
        from importlib.metadata import version
        return version(name)
    except Exception:
        return '?'


def run_pymupdf(pdf, out_dir, pages_spec, rel_src):
    import pymupdf
    doc = pymupdf.open(pdf)
    try:
        pages = parse_pages(pages_spec, doc.page_count)
    except ValueError as e:
        sys.stderr.write('錯誤：%s\n' % e); sys.exit(1)
    try:
        import pymupdf4llm
        chunks = pymupdf4llm.to_markdown(doc, pages=pages, page_chunks=True, show_progress=False)
        texts = [(c['metadata']['page_number'], c['text']) for c in chunks]
        engine = 'pymupdf4llm %s（PyMuPDF %s）' % (dist_version('pymupdf4llm'), dist_version('PyMuPDF'))
    except ImportError:
        texts = [(p + 1, doc[p].get_text()) for p in pages]
        engine = 'PyMuPDF %s 純文字' % dist_version('PyMuPDF')
    thin = [n for n, t in texts if len(t.strip()) < MIN_PAGE_CHARS]
    garbled = [n for n, t in texts if n not in thin and looks_garbled(t)]
    extra = ''
    if thin:
        extra += 'warning: 第 %s 頁幾乎沒有文字層（可能是掃描影像），內容須直接看原 PDF。\n' % '、'.join(map(str, thin))
    if garbled:
        extra += 'warning: 第 %s 頁文字層疑似亂碼（字型編碼錯誤），內容須直接看原 PDF。\n' % '、'.join(map(str, garbled))
    body = ''.join('\n<!-- pdf-page: %d -->\n\n%s\n' % (n, t.strip()) for n, t in texts)
    out = os.path.join(out_dir, 'content.md')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(header(rel_src, engine, describe_pages(pages, doc.page_count), extra) + body)
    print('引擎：%s' % engine)
    print('頁數：%s' % describe_pages(pages, doc.page_count))
    if thin:
        print('注意：第 %s 頁幾乎沒有文字層，可能是掃描影像。' % '、'.join(map(str, thin)))
    if garbled:
        print('注意：第 %s 頁文字層疑似亂碼（字型編碼錯誤）。' % '、'.join(map(str, garbled)))
    print('輸出：%s' % out)
    return len(thin) + len(garbled), len(texts)


def check_wsl_mineru():
    """檢查 Windows WSL2 Ubuntu 是否有隔離的 MinerU / magic-pdf 安裝。"""
    if platform.system() != 'Windows':
        return False
    if shutil.which('wsl') is None:
        return False
    try:
        cmd = ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'test -x ~/.mineru-env/bin/magic-pdf']
        res = subprocess.run(cmd, capture_output=True, stdin=subprocess.DEVNULL, timeout=30)
        return res.returncode == 0
    except Exception:
        return False


def to_wsl_path(win_path_str: str) -> str:
    """將 Windows 路徑轉為 WSL 路徑（例如 C:\\... -> /mnt/c/...）"""
    try:
        res = subprocess.run(['wsl', 'wslpath', '-u', win_path_str], capture_output=True, text=True, check=True)
        out = res.stdout.strip()
        if out:
            return out
    except Exception:
        pass
    p = Path(win_path_str).resolve()
    drive = p.drive.rstrip(':').lower()
    parts = list(p.parts[1:])
    return f"/mnt/{drive}/" + "/".join(parts)


def mineru_ready():
    # 優先檢查本機 mineru-kit
    if os.path.exists(MINERU_KIT):
        res = subprocess.run([MINERU_KIT, 'models', 'verify', '--tier', MINERU_TIER], capture_output=True, text=True)
        if res.returncode == 0:
            return True, 'local', ''
        return False, None, 'MinerU %s 檔位模型不齊全（執行 setup_env.py 查看下載方式）' % MINERU_TIER
    
    # 若在 Windows，檢查 WSL2 隔離環境
    if check_wsl_mineru():
        return True, 'wsl', ''

    return False, None, '找不到 %s 且未探測到 WSL2 隔離環境' % os.path.relpath(MINERU_KIT, ROOT)


def run_mineru(pdf, out_dir, pages_spec, rel_src, mode='local'):
    raw_dir = os.path.join(out_dir, 'mineru')
    os.makedirs(raw_dir, exist_ok=True)
    if mode == 'wsl':
        wsl_pdf = to_wsl_path(pdf)
        wsl_out = to_wsl_path(raw_dir)
        # 刻意不傳任何遠端參數，使用本機隔離環境
        wsl_cmd = f"source ~/.local/bin/env 2>/dev/null; source ~/.mineru-env/bin/activate && magic-pdf -p '{wsl_pdf}' -o '{wsl_out}' -m auto"
        cmd = ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', wsl_cmd]
        engine_desc = 'MinerU（magic-pdf，WSL2 隔離環境）'
    else:
        # 刻意不傳 --remote／--remote-url／--api-key：只在本機解析。
        cmd = [MINERU_KIT, 'parse', pdf, '-o', raw_dir, '-f', 'markdown', '--tier', MINERU_TIER]
        if pages_spec and pages_spec != 'all':
            cmd += ['-p', pages_spec]
        engine_desc = 'MinerU（mineru-kit parse --tier %s，本機）' % MINERU_TIER
    print('執行：%s' % (' '.join(cmd) if isinstance(cmd, list) else cmd))
    res = subprocess.run(cmd)
    mds = sorted(glob.glob(os.path.join(raw_dir, '**', '*.md'), recursive=True))
    if res.returncode != 0 or not mds:
        sys.stderr.write('錯誤：MinerU 解析失敗（代碼 %s，產出 %d 個 Markdown）。未改用其他引擎；'
                         '如只需搜尋文字，請改加 --engine pymupdf。\n' % (res.returncode, len(mds)))
        sys.exit(2)
    with open(mds[0], encoding='utf-8') as f:
        md = f.read()
    # MinerU 把圖片以 base64 嵌入 Markdown，體積大且不利搜尋；content.md 改為簡短標記，原始輸出不動。
    md, n_img = re.subn(r'!\[([^\]]*)\]\(data:image/[^)]*\)', r'[圖片已略去：\1，見 mineru/ 原始輸出]', md)
    extra = ('warning: MinerU 輸出不含頁碼標記；定位頁碼時請另以 --engine pymupdf 產生對照。原始輸出見 mineru/。\n'
             'warning: 公式與表格為模型判讀，行內符號與合併儲存格常出錯，引用前回原 PDF 核對。\n')
    if n_img:
        extra += 'note: 已略去 %d 張嵌入圖片。\n' % n_img
    out = os.path.join(out_dir, 'content.md')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(header(rel_src, engine_desc, pages_spec or 'all', extra) + '\n' + md)
    print('引擎：%s' % engine_desc)
    print('輸出：%s（原始輸出在 %s）' % (out, raw_dir))


def main():
    ap = argparse.ArgumentParser(description='把論文 PDF 抽成附頁碼標記的 Markdown（搜尋與定位用，非證據）')
    ap.add_argument('input_pdf', help='PDF 路徑')
    ap.add_argument('--output-dir', '-o', help='輸出目錄（預設 work/parsed/<檔名>/）')
    ap.add_argument('--engine', '-e', choices=['auto', 'mineru', 'pymupdf'], default='auto')
    ap.add_argument('--pages', '-p', default='all', help="頁碼，例如 '1-5,8'；預設 all")
    args = ap.parse_args()
    maybe_reexec()

    pdf = os.path.abspath(args.input_pdf)
    if not os.path.isfile(pdf):
        sys.stderr.write('錯誤：找不到檔案 %s\n' % args.input_pdf); sys.exit(1)
    try:
        rel_src = os.path.relpath(pdf, ROOT).replace(os.sep, '/')
    except ValueError:  # Windows 不同磁碟機
        rel_src = pdf
    name = os.path.splitext(os.path.basename(pdf))[0]
    out_dir = os.path.abspath(args.output_dir or os.path.join(ROOT, 'work', 'parsed', name))

    engine = args.engine
    mineru_mode = 'local'
    if engine == 'mineru':
        ok, mineru_mode, why = mineru_ready()
        if not ok:
            sys.stderr.write('錯誤：無法使用 MinerU：%s。未改用其他引擎。\n' % why); sys.exit(1)
    if engine in ('auto', 'pymupdf') and not has_pymupdf():
        sys.stderr.write('錯誤：找不到 PyMuPDF。請依 paper-pdf-parser 說明建立 .venv-mineru，'
                         '或執行 setup_env.py 查看安裝指引。\n')
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)
    print('來源：%s' % rel_src)
    if engine == 'mineru':
        run_mineru(pdf, out_dir, args.pages, rel_src, mode=mineru_mode)
    else:
        thin, total = run_pymupdf(pdf, out_dir, args.pages, rel_src)
        if engine == 'auto':
            engine = 'pymupdf'
            if thin * 2 > total:
                ok, mineru_mode, why = mineru_ready()
                if ok:
                    print('注意：過半頁面沒有可用文字層，改用 MinerU 重新解析（PyMuPDF 結果存為 content-pymupdf.md）。')
                    os.replace(os.path.join(out_dir, 'content.md'), os.path.join(out_dir, 'content-pymupdf.md'))
                    run_mineru(pdf, out_dir, args.pages, rel_src, mode=mineru_mode)
                    engine = 'mineru'
                else:
                    print('注意：過半頁面沒有可用文字層，但無法使用 MinerU（%s）；請直接看原 PDF。' % why)
    with open(os.path.join(out_dir, 'meta.json'), 'w', encoding='utf-8') as f:
        json.dump({'source': rel_src, 'engine': engine, 'pages': args.pages, 'generated': taipei_now()},
                  f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
