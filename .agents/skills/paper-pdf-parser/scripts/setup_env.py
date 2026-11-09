#!/usr/bin/env python3
"""setup_env.py: 檢查 paper-pdf-parser 的執行環境（macOS 與 Windows 通用，只讀不改）。

用法（倉庫內任何位置皆可執行）：
    python .agents/skills/paper-pdf-parser/scripts/setup_env.py

檢查項目：作業系統、uv、倉庫根目錄之 .venv-mineru、PyMuPDF 與 pymupdf4llm、MinerU 套件與模型、
硬體加速（僅供參考）。缺少項目時列出對應平台的安裝指令；本腳本不會自行安裝或下載任何東西。
"""
import argparse
import os
import platform
import shutil
import subprocess
import sys


def repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        out = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=here,
                             capture_output=True, check=True)
        return out.stdout.decode().strip()
    except Exception:
        return os.path.abspath(os.path.join(here, '..', '..', '..', '..'))


ROOT = repo_root()
WIN = platform.system() == 'Windows'
BIN = os.path.join(ROOT, '.venv-mineru', 'Scripts' if WIN else 'bin')
EXE = '.exe' if WIN else ''
VENV_PY = os.path.join(BIN, 'python' + EXE)
MINERU_KIT = os.path.join(BIN, 'mineru-kit' + EXE)


def dist_version(py, dist):
    code = ('import importlib.metadata as m\n'
            'try:\n    print(m.version(%r))\n'
            'except Exception:\n    pass\n') % dist
    try:
        res = subprocess.run([py, '-I', '-c', code], capture_output=True, text=True, timeout=30)
        return res.stdout.strip() or None
    except Exception:
        return None


def accel(py):
    code = ('import torch\n'
            'if torch.cuda.is_available(): print("CUDA：" + torch.cuda.get_device_name(0))\n'
            'elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available(): print("MPS（Apple Silicon）")\n'
            'else: print("僅 CPU")\n')
    try:
        res = subprocess.run([py, '-I', '-c', code], capture_output=True, text=True, timeout=60)
        return res.stdout.strip() or '無法判斷'
    except Exception:
        return '無法判斷'


def models_ok():
    if not os.path.exists(MINERU_KIT):
        return None
    try:
        res = subprocess.run([MINERU_KIT, 'models', 'verify'], capture_output=True, text=True, timeout=120)
        return res.returncode == 0
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description='檢查 paper-pdf-parser 執行環境')
    ap.add_argument('--check', action='store_true', help='相容舊用法；預設即為檢查')
    ap.parse_args()
    venv = VENV_PY if os.path.exists(VENV_PY) else None
    py = venv or sys.executable
    uv = shutil.which('uv')
    mupdf = dist_version(py, 'PyMuPDF')
    m4llm = dist_version(py, 'pymupdf4llm')
    mineru = dist_version(py, 'mineru')
    models = models_ok() if mineru else None

    print('=' * 50)
    print('paper-pdf-parser 環境檢查')
    print('=' * 50)
    print('作業系統：%s（%s）' % (platform.system(), platform.machine()))
    print('uv：%s' % (uv or '未安裝'))
    print('虛擬環境 .venv-mineru：%s' % (os.path.relpath(venv, ROOT) if venv else '不存在'))
    print('PyMuPDF：%s' % (mupdf or '未安裝'))
    print('pymupdf4llm：%s' % (m4llm or '未安裝（仍可用 PyMuPDF 純文字模式）'))
    print('MinerU 套件：%s' % (mineru or '未安裝'))
    if mineru:
        print('MinerU 模型：%s' % ({True: '齊全', False: '不齊全', None: '無法檢查'}[models]))
        print('硬體加速（參考）：%s' % accel(py))
    print('-' * 50)

    act = '.venv-mineru\\Scripts\\python.exe' if WIN else '.venv-mineru/bin/python'
    kit = '.venv-mineru\\Scripts\\mineru-kit.exe' if WIN else '.venv-mineru/bin/mineru-kit'
    steps = []
    if not uv:
        steps.append('brew install uv' if not WIN else
                     'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"')
    if not venv:
        steps.append('uv venv .venv-mineru --python 3.12')
    if not mupdf or not m4llm:
        steps.append('uv pip install pymupdf pymupdf4llm --python %s' % act)
    if steps:
        print('[PyMuPDF 引擎所需步驟]（於倉庫根目錄執行）')
        for i, s in enumerate(steps, 1):
            print('%d. %s' % (i, s))
    else:
        print('PyMuPDF 引擎可用：parse_pdf.py 可抽出附頁碼標記之文字。')
    if not mineru:
        print('[MinerU 引擎，選用] uv pip install -U "mineru>=4.0,<5" --python %s' % act)
    elif models is False:
        print('[MinerU 引擎，選用] 模型不齊全。下載約數 GB，須先徵得使用者同意，再執行：')
        print('    %s models download' % kit)
    elif models:
        print('MinerU 引擎可用。首次使用前請確認遙測設定（mineru telemetry status）。')
    print('=' * 50)


if __name__ == '__main__':
    main()
