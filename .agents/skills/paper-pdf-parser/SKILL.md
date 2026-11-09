---
name: paper-pdf-parser
description: >-
  Extract academic paper PDFs into searchable Markdown with PDF page markers (PyMuPDF; optional local MinerU for layout, formulas and tables), so wiki-content-audit and academic-paper-translator can locate claims, numbers and pages quickly. The output is a locating aid, never evidence. Runs locally only on macOS and Windows.
---

# Paper PDF Parser（論文 PDF 文字抽取與頁碼定位）

## 一、定位

把 `raw/` 中的論文 PDF 抽成可搜尋的 Markdown，每頁前加 `<!-- pdf-page: N -->` 標記，讓撰寫與查核時能快速找到某個數字、術語或句子在第幾頁。用途：

* `wiki-content-audit` 建立證據表前，先搜尋主張出處並記下頁碼（寫作模式第 1、2 步、查核模式）。
* `academic-paper-translator` 盤點來源時，快速清點章節、表格與公式。

**輸出只是定位輔助，不是證據。** 證據表一律回原 PDF 核對，引用印刷頁碼、表或圖；數字、限定語與公式以原 PDF 為準。

## 二、硬性規則

1. **只在本機解析**：不得使用 MinerU 的 `--remote`、`--remote-url`、`--api-key` 或任何線上解析服務。`raw/` 含未公開之學位論文與私人資料，上傳即等同公開。`parse_pdf.py` 不會傳入這些參數，直接呼叫 MinerU 時亦同。
2. **輸出不進版控**：預設輸出至 `work/parsed/<檔名>/`，該目錄已列入 `.gitignore`。不得把解析結果複製進 `wiki/`、`web/` 或 `raw/`；`raw/` 仍為唯讀。
3. **頁碼要換算**：`pdf-page` 是 PDF 檔內頁序，常與期刊印刷頁碼不同（例如 Hopfield 1982 的 PDF 第 2 頁為印刷頁 2554，第 1 頁是封面）。寫入證據表前回原 PDF 確認印刷頁碼。
4. **文字層不可靠時看原圖**：掃描版論文的公式、上下標與雙欄順序常抽錯；腳本會標出幾乎沒有文字層的頁面。遇到這些頁面、表格或公式，一律直接看原 PDF 頁面。
5. **下載模型須先徵得使用者同意**：MinerU 模型約數 GB，未經使用者同意不得執行 `mineru-kit models download`。

## 三、環境

先檢查環境（只讀不改，會列出缺少項目的安裝指令）：

```bash
python .agents/skills/paper-pdf-parser/scripts/setup_env.py
```

依賴裝在倉庫根目錄的 `.venv-mineru`（已列入 `.gitignore`），不動系統 Python。`parse_pdf.py` 若發現目前的 Python 沒有 PyMuPDF，會自動改用 `.venv-mineru` 的 Python 執行，因此用系統 Python 呼叫即可。

**PyMuPDF 引擎（必要）**，於倉庫根目錄執行：

```bash
# macOS
brew install uv
uv venv .venv-mineru --python 3.12
uv pip install pymupdf pymupdf4llm --python .venv-mineru/bin/python
```

```powershell
# Windows（PowerShell）
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv venv .venv-mineru --python 3.12
uv pip install pymupdf pymupdf4llm --python .venv-mineru\Scripts\python.exe
```

**MinerU 引擎（選用）**：`uv pip install -U "mineru>=4.0,<5" --python <同上>`，再經使用者同意後執行 `mineru-kit models download`（Windows 為 `.venv-mineru\Scripts\mineru-kit.exe`）。首次使用前以 `mineru telemetry status` 確認遙測設定。

## 四、用法

```bash
# 全文（預設 auto：MinerU 模型齊全時用 MinerU，否則用 PyMuPDF，並註明）
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/2017-attention-is-all-you-need.pdf

# 指定頁碼（PDF 頁序，1 起算）
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/1982-hopfield-network.pdf --pages 2-3,6

# 指定引擎；指定 mineru 而無法使用時直接報錯，不改用其他引擎
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/<檔名>.pdf --engine pymupdf
```

參數：`--pages`（如 `1-5,8`，預設 `all`）、`--engine`（`auto`／`pymupdf`／`mineru`）、`--output-dir`（預設 `work/parsed/<檔名>/`）。結束代碼：0 成功、1 輸入或環境錯誤、2 解析失敗。

輸出：

* `content.md`：開頭註解記載來源、引擎、頁碼範圍、產生時間與「不得作為證據」提醒；PyMuPDF 引擎於每頁前加 `<!-- pdf-page: N -->`。
* `meta.json`：來源、實際使用之引擎、頁碼與時間。
* `mineru/`（僅 MinerU 引擎）：MinerU 原始輸出。其 Markdown 不含頁碼標記，定位頁碼時另以 `--engine pymupdf` 產生對照。

## 五、引擎差異與已知限制

| | PyMuPDF（pymupdf4llm） | MinerU（本機） |
|---|---|---|
| 原理 | 讀取 PDF 內嵌文字層 | 以模型分析版面、公式、表格與 OCR |
| 頁碼標記 | 有 | 無（另以 PyMuPDF 對照） |
| 公式 | 純文字，非 LaTeX；掃描版常錯亂 | 宣稱可轉為 LaTeX，本專案尚未驗證 |
| 掃描版 PDF | 文字層品質決定成敗，需看原圖 | 可 OCR，本專案尚未驗證 |
| 需求 | 數十 MB 套件 | 套件約 1 GB 加上數 GB 模型 |

2026-11-09 於 macOS（Apple Silicon）實測：PyMuPDF 引擎可正確抽出 Transformer 2017 的正文與表格數字（如 28.4、41.8 BLEU），公式為純文字；Hopfield 1982 為掃描版，正文可搜尋，但公式與雙欄順序錯亂。MinerU 4.1.7 已安裝，但模型未下載，尚未實際解析成功；Windows 環境尚未實測。

## 六、腳本

* `scripts/setup_env.py`：環境檢查，列出缺少項目與對應平台之安裝指令；不自行安裝或下載。
* `scripts/parse_pdf.py`：解析 CLI。MinerU 一律以 `mineru-kit parse` 在本機執行。
