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
5. **下載模型須先徵得使用者同意**：MinerU 模型存於家目錄 `~/.mineru/models`（不在倉庫內），`basic` 檔位約 0.9 GB、`standard` 檔位約 2.1 GB（2026-11-09 查 HuggingFace）。未經使用者同意不得執行 `mineru-kit models download`。

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

**MinerU 引擎（選用）**：`uv pip install -U "mineru>=4.0,<5" --python <同上>`，再經使用者同意後執行 `mineru-kit models download --tier basic`（Windows 為 `.venv-mineru\Scripts\mineru-kit.exe`）。本 Skill 只用 `mineru-kit parse`，其程式碼不含遙測；遙測屬於另一個指令 `mineru` 的文件庫服務（需 `mineru server start`），本 Skill 不使用。

## 四、用法

```bash
# 全文（預設 auto：先用 PyMuPDF；過半頁面無文字層或為亂碼且 MinerU 可用時改用 MinerU，並註明）
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/2017-attention-is-all-you-need.pdf

# 指定頁碼（PDF 頁序，1 起算）
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/1982-hopfield-network.pdf --pages 2-3,6

# 需要公式的 LaTeX 草稿時明確指定 MinerU；無法使用時直接報錯，不改用其他引擎
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/<檔名>.pdf --engine mineru --pages 3-4
```

**何時用 MinerU**：定位頁碼、搜尋數字一律用預設（PyMuPDF）。只有三種情況用 MinerU：純圖片 PDF、文字層亂碼（字型編碼錯誤）的頁面，以及要把長公式抄成 KaTeX 時先產生草稿。MinerU 的輸出同樣只是草稿，引用前逐一回原頁核對。

參數：`--pages`（如 `1-5,8`，預設 `all`）、`--engine`（`auto`／`pymupdf`／`mineru`）、`--output-dir`（預設 `work/parsed/<檔名>/`）。結束代碼：0 成功、1 輸入或環境錯誤、2 解析失敗。

輸出：

* `content.md`：開頭註解記載來源、引擎、頁碼範圍、產生時間與「不得作為證據」提醒，並列出無文字層或疑似亂碼之頁面；PyMuPDF 引擎於每頁前加 `<!-- pdf-page: N -->`。MinerU 引擎之嵌入圖片改為簡短標記，原圖見 `mineru/`。
* `content-pymupdf.md`（僅 `auto` 改用 MinerU 時）：先前 PyMuPDF 的結果，可用來對照頁碼。
* `meta.json`：來源、實際使用之引擎、頁碼與時間。
* `mineru/`（僅 MinerU 引擎）：MinerU 原始輸出。其 Markdown 不含頁碼標記，定位頁碼時另以 `--engine pymupdf` 產生對照。

## 五、引擎差異與已知限制

| | PyMuPDF（pymupdf4llm） | MinerU（本機） |
|---|---|---|
| 原理 | 讀取 PDF 內嵌文字層 | 以模型分析版面、公式、表格與 OCR |
| 頁碼標記 | 有 | 無（另以 PyMuPDF 對照） |
| 公式 | 純文字，非 LaTeX；掃描版常錯亂 | 轉為 LaTeX；獨立公式準確度高，行內小符號常錯 |
| 純圖片或亂碼文字層 | 讀不到或讀成亂碼 | 可 OCR |
| 合併儲存格 | 常錯拆 | 常錯拆 |
| 速度 | 每頁不到 1 秒 | 實測每頁約 2 至 16 秒（含公式之掃描頁最慢） |
| 需求 | 數十 MB 套件 | 套件約 1.3 GB（含 PyTorch），加上 `basic` 模型約 0.9 GB |

**2026-11-09 於 macOS（Apple Silicon，MinerU 4.1.7 `basic` 檔位）實測，逐項對照原 PDF 頁面影像：**

* **Hopfield 1982（掃描版）**：MinerU 輸出之式 (1)–(4) 與原頁一致，連原文式 (3) 印作 $H_j^{s'}$（式 (4) 為 $H_i^{s'}$）都如實保留；但同頁行內之「threshold $U_i$」被轉為 `\overline{U_i^-}`、「$U_i = 0$」被轉為 `U_i = \dot{0}`，皆為形式合法、內容錯誤之 LaTeX。PyMuPDF 之公式則錯亂（如 ≠ 變成 #）。
* **Transformer 2017（數位排版）**：兩種引擎之 Table 2 BLEU 數值皆正確，MinerU 另將式 (1) 正確轉為 LaTeX；兩者都把跨兩欄之訓練成本（如 $2.3 \cdot 10^{19}$）錯拆為兩格。
* **Aghion 1992 與 Acemoglu 2001 之封存檔**：前者為純圖片、後者封面與摘要兩頁為字型編碼亂碼，PyMuPDF 皆讀不到；MinerU 可正確 OCR。也因此查出兩份封存檔與證據表所稱版本不符（見 `wiki/issues.md` EK-088、EK-089）。
* Windows 環境尚未實測。

## 六、腳本

* `scripts/setup_env.py`：環境檢查，列出缺少項目與對應平台之安裝指令；不自行安裝或下載。
* `scripts/parse_pdf.py`：解析 CLI。MinerU 一律以 `mineru-kit parse` 在本機執行。
