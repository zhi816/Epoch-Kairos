#!/usr/bin/env python3
"""Cross-platform environment detector and setup assistant for paper-pdf-parser.

Supports macOS and Windows. Checks Python version, uv, GPU/MPS acceleration,
and installation status of MinerU and PyMuPDF.
"""

import os
import platform
import shutil
import subprocess
import sys


def detect_system():
    os_name = platform.system()
    arch = platform.machine()
    python_ver = sys.version.split()[0]
    return {
        "os": os_name,
        "arch": arch,
        "python": python_ver,
    }


def find_uv():
    return shutil.which("uv")


def check_venv(venv_path=".venv-mineru"):
    if not os.path.exists(venv_path):
        return None
    if platform.system() == "Windows":
        py_bin = os.path.join(venv_path, "Scripts", "python.exe")
    else:
        py_bin = os.path.join(venv_path, "bin", "python")
    return py_bin if os.path.exists(py_bin) else None


def check_module_in_python(py_bin, module_name, dist_name=None):
    dist = dist_name or module_name
    code = (
        f"try:\n"
        f"    import {module_name}\n"
        f"    import importlib.metadata\n"
        f"    try:\n"
        f"        print(importlib.metadata.version('{dist}'))\n"
        f"    except Exception:\n"
        f"        print(getattr({module_name}, '__version__', 'unknown'))\n"
        f"except Exception:\n"
        f"    pass\n"
    )
    try:
        res = subprocess.run(
            [py_bin, "-c", code],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass
    return None


def detect_hardware_acceleration(py_bin):
    code = (
        "import torch\n"
        "if torch.cuda.is_available():\n"
        "    print('cuda:' + torch.cuda.get_device_name(0))\n"
        "elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():\n"
        "    print('mps:Apple Silicon Metal')\n"
        "else:\n"
        "    print('cpu:CPU Only')\n"
    )
    try:
        res = subprocess.run(
            [py_bin, "-c", code],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception:
        pass
    return "unknown"


def print_status():
    sys_info = detect_system()
    uv_bin = find_uv()
    venv_py = check_venv()

    print("==================================================")
    print("Paper PDF Parser - Environment Status")
    print("==================================================")
    print(f"OS: {sys_info['os']} ({sys_info['arch']})")
    print(f"Host Python: {sys_info['python']}")
    print(f"uv installed: {'Yes (' + uv_bin + ')' if uv_bin else 'No'}")
    print(f"Virtualenv (.venv-mineru): {'Found (' + venv_py + ')' if venv_py else 'Not found'}")

    target_py = venv_py or sys.executable

    mupdf_ver = check_module_in_python(target_py, "fitz")
    print(f"PyMuPDF: {'Available (v' + mupdf_ver + ')' if mupdf_ver else 'Not installed'}")

    mineru_ver = check_module_in_python(target_py, "mineru")
    print(f"MinerU: {'Available (v' + mineru_ver + ')' if mineru_ver else 'Not installed'}")

    if mineru_ver:
        hw = detect_hardware_acceleration(target_py)
        print(f"Hardware Acceleration: {hw}")

    print("--------------------------------------------------")
    if not mineru_ver or not mupdf_ver:
        print("[Setup Instructions]")
        if sys_info["os"] == "Darwin":
            print("1. brew install uv")
            print("2. uv venv .venv-mineru --python 3.12")
            print("3. uv pip install -U \"mineru>=4.0,<5\" pymupdf --python .venv-mineru/bin/python")
        elif sys_info["os"] == "Windows":
            print("1. powershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\"")
            print("2. uv venv .venv-mineru --python 3.12")
            print("3. uv pip install -U \"mineru>=4.0,<5\" pymupdf --python .venv-mineru\\Scripts\\python.exe")
    else:
        print("Ready: All required dependencies are present.")
    print("==================================================")


if __name__ == "__main__":
    print_status()
