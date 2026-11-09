#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_paper.py - 學術論文 PDF 多層階梯式結構抽取工具

支援三層抽取架構：
1. 第一層（輕量極速）：PyMuPDF (fitz) 原生純文字與插圖無損抽取。
2. 第二層（高精度排版與 LaTeX）：WSL2 Ubuntu 隔離環境之 OpenDataLab MinerU (magic-pdf)。
3. 自動探測模式（auto）：優先探測 MinerU，若未就緒則平滑降級至 PyMuPDF。
"""

import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path

# 確保輸出編碼為 UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def win_to_wsl_path(win_path: Path) -> str:
    """將 Windows 路徑轉換為 WSL2 路徑（例如 C:\foo -> /mnt/c/foo）"""
    abs_path = win_path.resolve()
    drive = abs_path.drive.rstrip(":").lower()
    parts = list(abs_path.parts[1:])  # 去除磁碟機代號
    return f"/mnt/{drive}/" + "/".join(parts)


def check_pymupdf() -> bool:
    """檢查 Windows 本機是否安裝 PyMuPDF"""
    try:
        import pymupdf  # noqa: F401
        return True
    except ImportError:
        try:
            import fitz  # noqa: F401
            return True
        except ImportError:
            return False


def check_wsl_mineru() -> bool:
    """檢查 WSL2 Ubuntu 內是否具備可用的 MinerU 環境"""
    if shutil.which("wsl") is None:
        return False
    try:
        cmd = ["wsl", "-d", "Ubuntu", "-e", "bash", "-c", "test -x ~/.mineru-env/bin/magic-pdf"]
        res = subprocess.run(cmd, capture_output=True, stdin=subprocess.DEVNULL, timeout=30)
        return res.returncode == 0
    except Exception:
        return False


def run_check_env():
    """報告目前環境中 PDF 解析引擎之就緒狀態"""
    print("=" * 60)
    print("Epoch-Kairos PDF 結構解析引擎環境探測報告")
    print("=" * 60)

    # 1. 檢查 Windows 本機 PyMuPDF
    pymupdf_ok = check_pymupdf()
    print(f"[*] Windows 本機 PyMuPDF (fitz): {'[可用]' if pymupdf_ok else '[未安裝]'}")
    if pymupdf_ok:
        try:
            import pymupdf
            print(f"    - 版本：{pymupdf.__version__}")
        except Exception:
            pass
    else:
        print("    - 安裝指引：pip install pymupdf")

    # 2. 檢查 WSL2 與 MinerU
    wsl_available = shutil.which("wsl") is not None
    print(f"[*] Windows WSL2 支援: {'[可用]' if wsl_available else '[未檢測到]'}")

    mineru_ok = check_wsl_mineru()
    print(f"[*] WSL2 Ubuntu MinerU (magic-pdf): {'[可用]' if mineru_ok else '[未就緒 / 未安裝]'}")
    if mineru_ok:
        print("    - 環境位置：WSL2: Ubuntu -> ~/.mineru-env/bin/magic-pdf")
    else:
        print("    - 配置指引：於 WSL2 執行 uv pip install 'magic-pdf[full]' --python ~/.mineru-env")

    print("-" * 60)
    if mineru_ok:
        print("推薦模式：雙層就緒。可自由選擇 auto / mineru / pymupdf。")
    elif pymupdf_ok:
        print("推薦模式：第一層 PyMuPDF 已就緒，可立即執行秒級無損文字與圖表抽取。")
    else:
        print("警告：目前無可用之 PDF 抽取引擎，請先執行 pip install pymupdf。")
    print("=" * 60)


def extract_with_pymupdf(pdf_path: Path, output_dir: Path) -> Path:
    """使用 PyMuPDF 抽取結構化純文字與圖片"""
    try:
        import pymupdf as fitz
    except ImportError:
        import fitz

    output_dir.mkdir(parents=True, exist_ok=True)
    images_dir = output_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    md_lines = []
    
    md_lines.append(f"# {pdf_path.stem}\n")
    md_lines.append(f"> 來源檔案：`{pdf_path.name}`")
    md_lines.append(f"> 總頁數：{len(doc)} 頁\n")

    metadata = doc.metadata or {}
    if metadata.get("title"):
        md_lines.append(f"**原文件標題**：{metadata.get('title')}\n")
    if metadata.get("author"):
        md_lines.append(f"**作者**：{metadata.get('author')}\n")

    img_count = 0
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        page_num = page_idx + 1
        md_lines.append(f"\n---\n## 第 {page_num} 頁\n")

        # 抽取文字塊
        text = page.get_text("text").strip()
        if text:
            md_lines.append(text)
            md_lines.append("")

        # 抽取圖片
        image_list = page.get_images(full=True)
        for img_info in image_list:
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            img_count += 1
            img_filename = f"page_{page_num}_img_{img_count}.{image_ext}"
            img_filepath = images_dir / img_filename
            with open(img_filepath, "wb") as f_img:
                f_img.write(image_bytes)
            md_lines.append(f"\n![插圖 {img_count}](images/{img_filename})\n")

    doc.close()

    out_md = output_dir / f"{pdf_path.stem}_extracted.md"
    out_md.write_text("\n".join(md_lines), encoding="utf-8")
    return out_md


def extract_with_mineru(pdf_path: Path, output_dir: Path, device: str = "cpu") -> Path:
    """調用 WSL2 內的 MinerU (magic-pdf) 執行排版、表格與 LaTeX 公式抽取"""
    output_dir.mkdir(parents=True, exist_ok=True)
    wsl_pdf = win_to_wsl_path(pdf_path)
    wsl_out = win_to_wsl_path(output_dir)

    # magic-pdf 指令：-p 輸入檔 -o 輸出目錄 -m 解析模式
    # mode 可以是 auto, ocr, txt
    cmd_str = (
        f"source ~/.local/bin/env && "
        f"source ~/.mineru-env/bin/activate && "
        f"magic-pdf -p '{wsl_pdf}' -o '{wsl_out}' -m auto"
    )
    
    print(f"[*] 調用 WSL2 MinerU 解析中 (模式: auto)... 請稍候")
    cmd = ["wsl", "-d", "Ubuntu", "-e", "bash", "-c", cmd_str]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    
    if res.returncode != 0:
        print("[!] WSL2 MinerU 執行失敗：", file=sys.stderr)
        print(res.stderr, file=sys.stderr)
        raise RuntimeError("MinerU 解析失敗。")

    print("[*] MinerU 解析完成！成果已儲存至：", output_dir)
    # MinerU 會在 output_dir 下建立一個以 pdf stem 為名稱的子目錄
    expected_dir = output_dir / pdf_path.stem
    auto_md = expected_dir / "auto" / f"{pdf_path.stem}.md"
    if auto_md.exists():
        return auto_md
    return output_dir


def main():
    parser = argparse.ArgumentParser(description="學術論文 PDF 階梯式結構解析工具")
    parser.add_argument("pdf_path", nargs="?", help="欲解析之 PDF 檔案路徑")
    parser.add_argument(
        "--engine",
        choices=["auto", "mineru", "pymupdf"],
        default="auto",
        help="解析引擎選擇：auto (自動探測), mineru (高精度公式版面), pymupdf (極速無損文字)"
    )
    parser.add_argument("--output-dir", default=None, help="結果輸出目錄（預設為 PDF 同目錄下之 _extracted 資料夾）")
    parser.add_argument("--check-env", action="store_true", help="檢查並報告解析引擎環境就緒狀態")

    args = parser.parse_args()

    if args.check_env:
        run_check_env()
        return

    if not args.pdf_path:
        parser.print_help()
        sys.exit(1)

    pdf_file = Path(args.pdf_path).resolve()
    if not pdf_file.exists():
        print(f"[錯誤] 檔案不存在：{pdf_file}", file=sys.stderr)
        sys.exit(1)

    if args.output_dir:
        out_dir = Path(args.output_dir).resolve()
    else:
        out_dir = pdf_file.parent / f"{pdf_file.stem}_extracted"

    selected_engine = args.engine
    if selected_engine == "auto":
        if check_wsl_mineru():
            selected_engine = "mineru"
        elif check_pymupdf():
            selected_engine = "pymupdf"
        else:
            print("[錯誤] 無任何可用之解析引擎！請先安裝 pymupdf 或於 WSL 配置 MinerU。", file=sys.stderr)
            sys.exit(1)

    print(f"[*] 目標檔案：{pdf_file}")
    print(f"[*] 啟用引擎：{selected_engine}")
    print(f"[*] 輸出路徑：{out_dir}")

    if selected_engine == "mineru":
        try:
            result_path = extract_with_mineru(pdf_file, out_dir)
            print(f"[成功] MinerU 解析產出：{result_path}")
        except Exception as e:
            print(f"[警告] MinerU 執行失敗（{e}），自動降級嘗試 PyMuPDF...", file=sys.stderr)
            if check_pymupdf():
                result_path = extract_with_pymupdf(pdf_file, out_dir)
                print(f"[成功] 降級 PyMuPDF 解析產出：{result_path}")
            else:
                sys.exit(1)
    elif selected_engine == "pymupdf":
        if not check_pymupdf():
            print("[錯誤] 本機未安裝 PyMuPDF，請執行 pip install pymupdf", file=sys.stderr)
            sys.exit(1)
        result_path = extract_with_pymupdf(pdf_file, out_dir)
        print(f"[成功] PyMuPDF 解析產出：{result_path}")


if __name__ == "__main__":
    main()
