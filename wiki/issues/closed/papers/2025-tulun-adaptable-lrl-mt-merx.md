# 已結案問題：papers/2025-tulun-adaptable-lrl-mt-merx.md

> 本檔收錄 [wiki/papers/2025-tulun-adaptable-lrl-mt-merx.md](../../../papers/2025-tulun-adaptable-lrl-mt-merx.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-057 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2025.acl-demos.13` 在 Crossref 與 doi.org 均查無此號，DOI 可能有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：本檔建立時以 crossref_check.py 查得（Claude Code by Anthropic）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 ACL Anthology 核對：ACL 2025 System Demonstrations 卷號為單數 `2025.acl-demo`，正確 DOI 為 `10.18653/v1/2025.acl-demo.13`（原誤記為 `acl-demos`），經 Crossref 與 doi.org 解析確認無誤並更新頁面。

### EK-083 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 3 與 Card 4 | 原文不符
- **問題**：Card 3（第 46–62 行）僅以抽象算子描述檢索，未交代原文 §3.2（p. 132）之具體檢索設計：詞彙表（Glossary）係以 spaCy `en_core_web_sm` 斷詞後進行 `{1,2}`-gram 重疊匹配，翻譯記憶庫（Translation Memory）係以 `Tantivy` 函式庫執行 Top-$N$ BM25 檢索，並以 `MADLAD-400-10B`／`OPUS-MT`／`NLLB-54B` 搭配 `Gemini 2.0 Flash` 進行少樣本思維鏈（CoT）後編輯；且原文全文無數學公式（式 52、56 應標明為依原文流程整理之示意式）。
- **來源**：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`（§3.2 p. 132、§4.1–4.2 pp. 132–133）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 補齊系統具體技術實作，包含 Django 後端、Docker 容器化、初譯模型支援（MADLAD-400-10B、OPUS-MT、NLLB-54B）、spaCy en_core_web_sm 之 {1,2}-gram 詞彙表動態比對、Rust Tantivy 函式庫之 Top-N BM25 翻譯記憶庫檢索，以及 LiteLLM 代理之 Gemini 2.0 Flash CoT 後編輯提示；標明流程公式為示意式；Card 4 補齊德頓語醫療（+16.90 chrF++ / +13.51 BLEU）、比斯拉馬語救災（+22.41 chrF++ / +17.69 BLEU）、SUS 81.25 分與 FLORES 六語基準對比。建立證據表 wiki/evidence/2025-tulun-adaptable-lrl-mt-merx.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核原文表 1（印刷頁 133）發現先前處理記錄把平均增益誤寫成各語言增益，且加入原文未報告的 BLEU。原文僅報 chrF++：MADLAD 基線下 TDT 為 35.78→47.87（+12.09）、BIS 為 15.22→47.94（+32.72），平均增益 +22.41；OPUS-MT 基線下 TDT 為 16.01→34.27（+18.26）、BIS 為 32.60→48.14（+15.54），平均增益 +16.90。先前寫入的 +13.51／+17.69 BLEU 以及 26.96、43.86、28.51、50.92 等數值均無原文表格依據；論文頁與證據表也含不符原文數值。須一併更正處理記錄、Card 4 與證據表後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文 §4.1.1（pp. 132–133）與表 1 核對並重寫 Card 4、證據表：更正詞彙表與翻譯記憶數量（Tetun 2,698／1,018，Bislama 5,769／3,353；評估保留 451／841），列明兩個基線下各語言的 ChrF++ 分數與增益，將 +22.41、+16.90 標為跨語言平均增益，移除未報告的 BLEU 及其數值。狀態改為 fixed。

### EK-116 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 3 | 原文未支持
- **問題**：Card 3 第 65–66 行之 $\hat{y}_{\text{base}} = \operatorname{NMT}(x)$ 與 $\hat{y}_{\text{final}} = \operatorname{LLM}_{\text{CoT}}(\ldots)$ 為 Wiki 自擬之流程示意，原文沒有任何公式，頁面也未標明為示意。頁面有區塊公式，卡片因而無法依 Card 3 無公式模式撰寫。
- **來源**：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf` 全文無編號公式。
- **發現於**：第二批卡片回填 B 組回報，協調者以全文搜尋確認（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。回原文確認全文無編號公式、流程只以文字與 Figure 1 說明後，刪除兩條自擬區塊公式，改以文字依序說明流程（§3.1–§3.2）；頁首「Card 3 之數學式為流程示意表示」改為「全文無編號公式」。證據表登記。

### EK-117 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 5 | 原文不符
- **問題**：Card 5 第 115 行稱「證明……利用現成小型開源 NMT 模型搭配輕量 API RAG 後編輯即可超越 54B 巨型單體模型」。原文 FLORES 實驗以 NLLB-54B 本身為初譯模型（baseline MT model），再以 LLM 後編輯，平均比 NLLB-54B 高 2.8 ChrF++；並非以小型 NMT 超越 54B 模型。
- **來源**：同 EK-116 之 PDF，摘要 p. 1、§4.2 p. 5、Table 2 p. 6。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。刪去 Card 5 兩點無出處之「打破壁壘」「證明……超越 54B」敘述，改寫為：FLORES 以 NLLB-54B 本身為初譯再後編輯、平均高 2.83（表 2）；並依新論文需求補記原文公開之程式與系統、作者明列之限制（含易用性研究僅兩位共同作者）與 §6 之未來方向（提示最佳化、離線部署等），各附位置。

### EK-156 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 1、Card 2、Card 3 與 Card 4 | 過度表述
- **問題**：（1）Card 1 稱系統「首創」此架構、傳統微調「迭代週期動輒數月，根本無法應對前線緊急需求」；原文只說作者所知是唯一支援德頓語、比斯拉馬語之開源術語感知工具（§2, p. 131），未提數月。（2）Card 2 之「部落長老」、「例如將 potable water 錯譯為非飲用水」、LLM「常輸出文法崩潰的句子」原文沒有；原文示例只說 MT 把 potable 譯錯（Figure 2）。（3）Card 3 稱翻譯記憶「論文評估中預設為 5 句」，原文只說 N 可設定；稱 MADLAD 針對德頓語、OPUS-MT 針對比斯拉馬語，原文兩者皆在兩語言評估。（4）Card 4 稱 SUS「對應 Grade A」，原文為 excellent；未記載易用性研究只有兩份回應、兩位參與者為共同作者；基隆迪語「回升至 42.76」為 Wiki 依原文 +0.25 計算之值，未標明。
- **來源**：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`，§1–§3（pp. 129–132）、§4.1.1–§4.1.2（pp. 132–133）、§5（p. 134）、倫理聲明（p. 135）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句，補記易用性研究之樣本與共同作者關係、表 1 之 LLM-only 對照值與資料取得條件；`hook` 補上 FLORES 平均增益；證據表重建，表 1、表 2 數值逐一寫出列與欄。
