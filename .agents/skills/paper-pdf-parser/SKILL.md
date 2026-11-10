---
name: paper-pdf-parser
description: >-
  Extract academic paper PDFs into searchable Markdown with PDF page markers so wiki-content-audit and academic-paper-translator can locate claims, numbers and pages. Default to PyMuPDF; use local MinerU only for image-only PDFs, garbled text layers, or drafting long formulas. All output is a draft, never evidence: verify every number, formula and page against the original PDF before writing it anywhere. Runs locally only on macOS and Windows.
---

# Paper PDF Parser（論文 PDF 文字抽取與頁碼定位）

## 一、定位

把 `raw/` 中的論文 PDF 抽成可搜尋的 Markdown，每頁前加 `<!-- pdf-page: N -->` 標記，讓撰寫與查核時能快速找到某個數字、術語或句子在第幾頁。用途：

* `wiki-content-audit` 建立證據表前，先搜尋主張出處並記下頁碼（寫作模式第 1、2 步、查核模式）。
* 收錄新論文時，本 Skill 是 [`paper-pipeline`](../paper-pipeline/SKILL.md) 之 S2（讀原文）；讀原文時要記下的事見該 Skill 之 `references/intake.md` 第六節。
* `academic-paper-translator` 盤點來源時，快速清點章節、表格與公式。

## 二、兩條核心原則（動手前必讀）

### 原則一：預設用 PyMuPDF，MinerU 只在三種情況使用

定位頁碼、搜尋數字與句子，PyMuPDF 就夠了：每頁不到 1 秒，而且附 `pdf-page` 頁碼標記。MinerU 每頁約 2 至 16 秒，輸出又不含頁碼標記，不得拿來對整篇論文做一般定位，以免浪費時間。只有下列三種情況才用 MinerU：

1. **純圖片 PDF**：沒有文字層，PyMuPDF 讀不到字。
2. **文字層亂碼**：字型編碼錯誤，PyMuPDF 讀出亂碼（例如字母整體位移）。
3. **抄寫長公式**：要把原文公式轉成 KaTeX 時，用 MinerU 產生草稿，並以 `--pages` 只解析含該公式的頁面。

前兩種情況 `auto` 會自動判斷並改用 MinerU，不必手動指定；第三種須明確加 `--engine mineru --pages <頁>`。

### 原則二：輸出一律只當草稿，不得盲目相信

兩種引擎的輸出都是程式或模型對 PDF 的判讀，不是原文。**證據表與論文頁中的數字、公式、引文與頁碼，一律回原 PDF 頁面核對後才可寫入。** 最危險的錯誤不是亂碼，而是「看起來正確、其實錯」的內容。2026-11-09 與 2026-11-10 實測已見：

* MinerU 把行內「threshold $U_i$」轉成 `\overline{U_i^-}`、「$U_i = 0$」轉成 `U_i = \dot{0}`：LaTeX 合法，內容錯誤（Hopfield 1982）。
* MinerU 在掃描版出現 OCR 漢字幻覺，將連接權重 $T_{ij}$ 誤轉為 $T_{ 扩 }$（Hopfield 1982 Windows 實測）。
* 兩種引擎都把跨兩欄的訓練成本 $2.3 \cdot 10^{19}$ 錯拆為兩格，看似英德、英法各有一個值（Transformer 2017 Table 2）。
* PyMuPDF 在掃描版把 ≠ 抽成 #，左右兩欄文字混排（Hopfield 1982）。
* `pdf-page` 是 PDF 檔內頁序，不等於期刊印刷頁碼。

核對時直接看原 PDF 的頁面影像。不得以解析結果確認解析結果，也不得以「兩種引擎結果一致」代替回原頁核對：兩者可能犯同一個錯，如上述錯拆的儲存格。

## 三、硬性規則

1. **只在本機解析**：不得使用 MinerU 的 `--remote`、`--remote-url`、`--api-key` 或任何線上解析服務。`raw/` 含未公開之學位論文與私人資料，上傳即等同公開。`parse_pdf.py` 不會傳入這些參數，直接呼叫 MinerU 時亦同。
2. **輸出不進版控**：預設輸出至 `work/parsed/<檔名>/`，該目錄已列入 `.gitignore`。不得把解析結果複製進 `wiki/`、`web/` 或 `raw/`；`raw/` 仍為唯讀。
3. **頁碼要換算**：`pdf-page` 是 PDF 檔內頁序，常與期刊印刷頁碼不同（例如 Hopfield 1982 的 PDF 第 2 頁為印刷頁 2554，第 1 頁是封面）。寫入證據表前回原 PDF 確認印刷頁碼。
4. **文字層不可靠時看原圖**：掃描版論文的公式、上下標與雙欄順序常抽錯；腳本會在終端與 `content.md` 開頭標出無文字層或疑似亂碼的頁面。遇到這些頁面、表格或公式，一律直接看原 PDF 頁面。
5. **下載模型須先徵得使用者同意**：MinerU 模型存於家目錄 `~/.mineru/models`（不在倉庫內），`basic` 檔位約 0.9 GB、`standard` 檔位約 2.1 GB（2026-11-09 查 HuggingFace）。未經使用者同意不得執行 `mineru-kit models download`。

## 四、環境

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

**Windows 與 WSL2**：2026-11-09 曾有代理加入以 WSL2 呼叫舊版 `magic-pdf`（MinerU 1.x）的路線與另一支抽取腳本，因下列問題撤回：忽略 `--pages` 卻在檔頭照寫頁碼範圍；與 macOS 的 MinerU 4.x 是不同引擎、不同版本，輸出卻同標「MinerU」；預設把輸出寫進 `raw/`（違反 `raw/` 唯讀）；MinerU 失敗時默默改用 PyMuPDF；實測只記「完全成功通過」，未對照原頁核對正確性。該 WSL2 1.x 路線已永久撤回且不得重啟。

現行 Windows 路線一律依本機 `.venv-mineru\Scripts\mineru-kit.exe` 之 MinerU 4.x（搭配 DirectML / ONNX Runtime 後端），模型放於 `%USERPROFILE%\.mineru\models`（basic 檔位為 `MinerU-4_models_onnx`）。2026-11-10 於 Windows 實測驗證，已全面落實下列五項條件：
1. `--pages` 實際生效（傳入 `-p` 參數，實測指定第 3 頁時僅解析該頁）。
2. 輸出記錄引擎名稱與版本（`content.md` 檔頭明確記載 `MinerU 4.2.0（mineru-kit parse --tier basic，本機）`，單頁解析時另加 `<!-- pdf-page: N -->`）。
3. 輸出只寫入 `work/parsed/`（不碰觸 `raw/` 唯讀目錄，且 `work/` 列於 `.gitignore`）。
4. 無法使用時直接報錯（未下載模型時直接退出碼 1 報錯，絕不默默改用其他引擎）。
5. 依原則二抽樣對照原 PDF 頁面，並於第六章記錄日期、平台、引擎版本與發現的錯誤。

## 五、用法

```bash
# 全文（預設 auto：先用 PyMuPDF；過半頁面無文字層或為亂碼且 MinerU 可用時改用 MinerU，並註明）
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/2017-attention-is-all-you-need.pdf

# 指定頁碼（PDF 頁序，1 起算）
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/1982-hopfield-network.pdf --pages 2-3,6

# 需要公式的 LaTeX 草稿時明確指定 MinerU；無法使用時直接報錯，不改用其他引擎
python .agents/skills/paper-pdf-parser/scripts/parse_pdf.py raw/<檔名>.pdf --engine mineru --pages 3-4
```

引擎選擇依第二章原則一；任何輸出都依原則二回原 PDF 核對。

參數：`--pages`（如 `1-5,8`，預設 `all`）、`--engine`（`auto`／`pymupdf`／`mineru`）、`--output-dir`（預設 `work/parsed/<檔名>/`）。結束代碼：0 成功、1 輸入或環境錯誤、2 解析失敗。

輸出：

* `content.md`：開頭註解記載來源、引擎、頁碼範圍、產生時間與「不得作為證據」提醒，並列出無文字層或疑似亂碼之頁面；PyMuPDF 引擎與單頁 MinerU 於頁面開頭加 `<!-- pdf-page: N -->`。MinerU 引擎之嵌入圖片改為簡短標記，原圖見 `mineru/`。
* `content-pymupdf.md`（僅 `auto` 改用 MinerU 時）：先前 PyMuPDF 的結果，可用來對照頁碼。
* `meta.json`：來源、實際使用之引擎、頁碼與時間。
* `mineru/`（僅 MinerU 引擎）：MinerU 原始輸出。其 Markdown 不含頁碼標記，定位頁碼時另以 `--engine pymupdf` 產生對照。

## 六、引擎差異與實測紀錄

| | PyMuPDF（pymupdf4llm） | MinerU（本機） |
|---|---|---|
| 原理 | 讀取 PDF 內嵌文字層 | 以模型分析版面、公式、表格與 OCR |
| 頁碼標記 | 有 | 無（單頁解析有標記；多頁另以 PyMuPDF 對照） |
| 公式 | 純文字，非 LaTeX；掃描版常錯亂 | 轉為 LaTeX；獨立公式準確度高，行內小符號常錯 |
| 純圖片或亂碼文字層 | 讀不到或讀成亂碼 | 可 OCR |
| 合併儲存格 | 常錯拆 | 常錯拆 |
| 速度 | 每頁不到 1 秒 | 實測每頁約 2 至 30 秒（含公式之掃描頁最慢） |
| 需求 | 數十 MB 套件 | 套件約 1.3 GB（Windows DirectML/ONNX 或 macOS PyTorch），加上 `basic` 模型約 0.9 GB |

**2026-11-09 於 macOS（Apple Silicon，MinerU 4.1.7 `basic` 檔位）實測，逐項對照原 PDF 頁面影像：**

* **Hopfield 1982（掃描版）**：MinerU 輸出之式 (1)–(4) 與原頁一致，連原文式 (3) 印作 $H_j^{s'}$（式 (4) 為 $H_i^{s'}$）都如實保留；但同頁行內之「threshold $U_i$」被轉為 `\overline{U_i^-}`、「$U_i = 0$」被轉為 `U_i = \dot{0}`，皆為形式合法、內容錯誤之 LaTeX。PyMuPDF 之公式則錯亂（如 ≠ 變成 #）。
* **Transformer 2017（數位排版）**：兩種引擎之 Table 2 BLEU 數值皆正確，MinerU 另將式 (1) 正確轉為 LaTeX；兩者都把跨兩欄之訓練成本（如 $2.3 \cdot 10^{19}$）錯拆為兩格。
* **Aghion 1992 與 Acemoglu 2001 之封存檔**：前者為純圖片、後者封面與摘要兩頁為字型編碼亂碼，PyMuPDF 皆讀不到；MinerU 可正確 OCR。也因此查出兩份封存檔與證據表所稱版本不符（見 `wiki/issues.md` EK-088、EK-089）。

**2026-11-10 於 Windows 11（AMD64，MinerU 4.2.0 DirectML/ONNX Runtime，`basic` 檔位，CPU 模式）實測，逐項對照原 PDF 頁面影像：**

* **Hopfield 1982（掃描版第 3 頁，印刷頁 2555）**：以 `--pages 3 --engine mineru` 實測，`--pages` 實際生效（耗時約 28 秒，僅解析第 3 頁），輸出落於 `work/parsed/1982-hopfield-network/`。獨立區塊公式式 (1)–(4) 辨識完整，式 (1) 之分段條件結構及式 (3) 原文誤植之 $H_j^{s'}$ 均忠實反映；但同頁發現下列典型錯誤，再次印證原則二「僅供草稿，一律回原頁核對」：
  1. 行內符號 OCR 漢字幻覺：神經元連接權重 $T_{ij}$ 被誤識為包含漢字之 $T_{ 扩 }$（第 12 行）。
  2. 行內符號形式合法但內容錯誤：門檻「threshold $U_i$」被轉為 `\overline{U_i^-}`、「$U_i = 0$」被轉為 `U_i = \dot{0}`（第 14、20 行，與 macOS 4.1.7 表現一致）。
  3. 反饋箭頭幻覺：強反饋耦合符號 $A \rightleftarrows B \rightleftarrows C$ 被加上上方括號幻覺為 `\overbrace { A \rightleftarrows B \rightleftarrows C } ^ { A \rightleftarrows B \rightleftarrows C }`（第 22 行）。
  4. 混淆刺激公式：$0.6 O_1 + 0.4 O_2$ 被轉為 $0.6 O_1 + \bar{0}.4 O_2^-$（第 46 行）。
  對照同頁 PyMuPDF 輸出，PyMuPDF 雖將式 (1) 錯亂拆散為 5 行純文字無 LaTeX 結構，但耗時不到 1 秒且抽取純文字時無漢字幻覺。

## 七、腳本

* `scripts/setup_env.py`：環境檢查，列出缺少項目與對應平台之安裝指令；不自行安裝或下載。
* `scripts/parse_pdf.py`：解析 CLI。MinerU 一律以 `mineru-kit parse` 在本機執行。
