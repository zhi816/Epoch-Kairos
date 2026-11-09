#!/usr/bin/env python3
"""Cross-platform PDF parser for academic and scientific papers.

Supports OpenDataLab MinerU (with MPS/CUDA hardware acceleration)
and PyMuPDF (fast local text extraction).
Works on macOS and Windows.
"""

import argparse
import os
import platform
import subprocess
import sys


def find_venv_python():
    venv_dir = os.path.abspath(".venv-mineru")
    if platform.system() == "Windows":
        py_bin = os.path.join(venv_dir, "Scripts", "python.exe")
        mineru_bin = os.path.join(venv_dir, "Scripts", "mineru.exe")
    else:
        py_bin = os.path.join(venv_dir, "bin", "python")
        mineru_bin = os.path.join(venv_dir, "bin", "mineru")
    return py_bin if os.path.exists(py_bin) else None, mineru_bin if os.path.exists(mineru_bin) else None


def parse_with_mineru(input_path, output_dir, pages="all", mineru_bin="mineru"):
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "content.md")
    cmd = [
        mineru_bin,
        "parse",
        input_path,
        "-p", pages,
        "-o", out_file,
        "-f", "markdown",
    ]
    print(f"Executing MinerU: {' '.join(cmd)}")
    res = subprocess.run(cmd)
    if res.returncode == 0:
        print(f"MinerU parsing completed successfully: {out_file}")
        return True
    else:
        print(f"MinerU parsing failed with return code {res.returncode}")
        return False


def parse_with_pymupdf(input_path, output_dir, py_bin=sys.executable):
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "content.md")
    
    script = (
        "import sys, os\n"
        "input_pdf = sys.argv[1]\n"
        "out_file = sys.argv[2]\n"
        "try:\n"
        "    import pymupdf4llm\n"
        "    md_text = pymupdf4llm.to_markdown(input_pdf)\n"
        "    with open(out_file, 'w', encoding='utf-8') as f:\n"
        "        f.write(md_text)\n"
        "    print('PyMuPDF4LLM extraction complete.')\n"
        "except Exception as e:\n"
        "    import fitz\n"
        "    doc = fitz.open(input_pdf)\n"
        "    text = []\n"
        "    for page_num in range(len(doc)):\n"
        "        page = doc[page_num]\n"
        "        text.append(f'## Page {page_num + 1}\\n\\n' + page.get_text())\n"
        "    with open(out_file, 'w', encoding='utf-8') as f:\n"
        "        f.write('\\n\\n'.join(text))\n"
        "    print('PyMuPDF basic extraction complete.')\n"
    )

    cmd = [py_bin, "-c", script, input_path, out_file]
    print(f"Executing PyMuPDF extraction...")
    res = subprocess.run(cmd)
    if res.returncode == 0:
        print(f"Extraction saved to: {out_file}")
        return True
    else:
        print(f"PyMuPDF extraction failed with return code {res.returncode}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Parse academic paper PDF into structured Markdown")
    parser.add_argument("input_pdf", help="Path to the PDF file to parse")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory for parsed results")
    parser.add_argument("--engine", "-e", choices=["auto", "mineru", "pymupdf"], default="auto", help="Parsing engine")
    parser.add_argument("--pages", "-p", default="all", help="Pages to parse (default: 'all')")

    args = parser.parse_args()

    if not os.path.isfile(args.input_pdf):
        print(f"Error: File not found: {args.input_pdf}")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(args.input_pdf))[0]
    output_dir = args.output_dir or os.path.join("work", "parsed", base_name)

    venv_py, mineru_bin = find_venv_python()
    effective_py = venv_py or sys.executable

    engine = args.engine
    if engine == "auto":
        if mineru_bin:
            engine = "mineru"
        else:
            engine = "pymupdf"
            print("Note: MinerU not found in venv. Falling back to PyMuPDF.")

    print(f"Input: {args.input_pdf}")
    print(f"Output Directory: {output_dir}")
    print(f"Engine: {engine}")

    if engine == "mineru":
        target_bin = mineru_bin or "mineru"
        success = parse_with_mineru(args.input_pdf, output_dir, pages=args.pages, mineru_bin=target_bin)
        if not success:
            print("MinerU failed. Attempting PyMuPDF fallback...")
            parse_with_pymupdf(args.input_pdf, output_dir, py_bin=effective_py)
    else:
        parse_with_pymupdf(args.input_pdf, output_dir, py_bin=effective_py)


if __name__ == "__main__":
    main()
