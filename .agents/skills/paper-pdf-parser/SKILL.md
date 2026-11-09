---
name: paper-pdf-parser
description: >-
  Extract and parse academic paper PDFs into structured Markdown with LaTeX math formulas, tables, and restored reading order using OpenDataLab MinerU and PyMuPDF. Supports cross-platform execution on macOS and Windows with automatic environment detection, hardware acceleration (MPS/CUDA/CPU), and graceful fallback.
---

# Paper PDF Parser（學術論文與複雜文檔高精度結構解析）

## 一、定位與核心目標

本技能專為學術文獻、科研論文與教材等高密度 PDF 設計，解決純多模態大模型在解析長篇雙欄排版、複雜數學公式與密集數據表格時可能產生的數值幻覺與 Token 浪費問題。

透過結合 **OpenDataLab MinerU** 與 **PyMuPDF**，本技能建立了一套具備自動降級與跨平台（macOS 與 Windows）相容能力的階梯式解析流程：
1. **結構與公式解析（MinerU）**：將雙欄排版還原為單流閱讀順序、將數學公式轉為標準 KaTeX/LaTeX 代碼（`$$...$$` 與 `$...$`）、精準提取多欄表格為 Markdown。
2. **極速文字提取（PyMuPDF）**：針對標準數位排版論文，以純 Python 代碼極速提取文字與座標，零模型權重、100% 數值保真。
3. **大模型職責聚焦**：解析完成的 Markdown 與圖表直接作為 `wiki-content-audit` 建立證據表（`wiki/evidence/`）與學術長文的客觀來源，讓大模型專注於學術推理、概念萃取與交叉驗證。

---

## 二、支援作業系統與環境架構

本工具鏈原生支援 **macOS** 與 **Windows** 雙系統環境，使用 `uv` 虛擬環境隔離所有深度學習依賴，絕不污染全域系統 Python：

| 作業系統 | 硬體加速 | 推薦 Python | 安裝管理工具 |
|---|---|---|---|
| **macOS** (Apple Silicon M1/M2/M3/M4) | MPS (Metal Performance Shaders) / CPU | Python 3.12 | `uv` / Homebrew |
| **Windows** (NVIDIA GPU / CPU) | CUDA / CPU | Python 3.12 | `uv` / Windows PowerShell |

---

## 三、環境配置與安裝工作流（Setup Workflow）

### 1. 自動檢測與環境準備（雙平台通用）
專案內建跨平台環境檢測腳本，會自動判定當前作業系統、Python 版本、可用硬體加速與依賴安裝狀態：

```bash
# 執行環境狀態診斷
python .agents/skills/paper-pdf-parser/scripts/setup_env.py --check
```

### 2. macOS 安裝步驟（使用 uv）
```bash
# 1. 安裝 uv（若尚未安裝）
brew install uv

# 2. 建立專用虛擬環境（指定 Python 3.12）
uv venv .venv-mineru --python 3.12

# 3. 啟動虛擬環境並安裝 MinerU 與 PyMuPDF
source .venv-mineru/bin/activate
uv pip install -U "mineru>=4.0,<5" pymupdf

# 4. 驗證硬體支援
mineru-kit hardware detect
```

### 3. Windows 安裝步驟（使用 PowerShell 與 uv）
```powershell
# 1. 安裝 uv（若尚未安裝）
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. 建立專用虛擬環境（指定 Python 3.12）
uv venv .venv-mineru --python 3.12

# 3. 啟動虛擬環境並安裝 MinerU 與 PyMuPDF
.venv-mineru\Scripts\activate
uv pip install -U "mineru>=4.0,<5" pymupdf

# 4. 驗證硬體支援（若有 NVIDIA 顯卡會自動啟用 CUDA）
mineru-kit hardware detect
```

---

## 四、命令列操作指南（Usage Guide）

解析腳本位於 `.agents/skills/paper-pdf-parser/scripts/parse_pdf.py`，支援多種抽取模式與自動降級：

### 1. 完整結構解析（推薦：包含雙欄重排與 LaTeX 公式）
```bash
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/1982-hopfield-network.pdf --output-dir work/parsed/1982-hopfield/
```
- **輸出內容**：
  - `content.md`：轉換後之標準 Markdown 文件（公式皆為 KaTeX 格式）。
  - `images/`：自動切割之插圖與高解析度圖表。
  - `tables/`：表格數據與對應之 Markdown 表。

### 2. 極速文字抽取（適用於數位文字版或純文字核對）
```bash
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/2001-colonial-origins-acemoglu.pdf --engine pymupdf --output-dir work/parsed/2001-colonial/
```

### 3. 參數說明
- `input_pdf`：輸入的 PDF 檔案路徑（支援相對路徑與絕對路徑）。
- `--output-dir`：解析成果存放目錄（預設為 `work/parsed/<檔名>/`）。
- `--engine`：指定解析引擎，可選 `auto`（預設）、`mineru`、`pymupdf`。
  - `auto`：若已安裝 MinerU 則優先使用 MinerU，未安裝時自動平滑降級為 PyMuPDF 並提示安裝。
- `--pages`：指定解析頁碼範圍，例如 `1-5` 或 `1,3,5`（節省運算資源）。
