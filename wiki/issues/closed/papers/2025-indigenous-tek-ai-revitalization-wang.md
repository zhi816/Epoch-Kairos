# 已結案問題：papers/2025-indigenous-tek-ai-revitalization-wang.md

> 本檔收錄 [wiki/papers/2025-indigenous-tek-ai-revitalization-wang.md](../../../papers/2025-indigenous-tek-ai-revitalization-wang.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-078 | fixed | papers/2025-indigenous-tek-ai-revitalization-wang.md | Card 1 與 Card 3 | 原文不符
- **問題**：（1）Card 1（第 29 行）作者姓名寫作「王 reen-cheng」，中英大小寫混雜。（2）Card 3（第 45–53 行）將模型寫為 Nonaka 四階段 SECI 遞迴算子；原文 §3.2（pp. 7–11，圖 3）係將 Nonaka 模型擴展為四層知識矩陣（$K_1$ 個體內隱、$K_2$ 個體外顯、$K_3$ 部落社群、$K_4$ 文化系統）與 12 個知識轉換階段，並搭配五層 LKM 架構（§3.4，圖 5）與 Plan–Act–Observe–Adjust 代理迴圈（§3.5，圖 6）。（3）Card 3（第 56–61 行）列出基於餘弦相似度之禁忌懲罰損失函數；原文為質性系統架構論文，全文無任何數學公式或損失函數（文化禁忌係由第一層部落會議審查、第三層語義標籤與第五層規則權限矩陣控管）。
- **來源**：`raw/my-focus/英文論文/From Tacit Knowledge Distillation to AI-Enabled Culture Revitalization Modeling Knowledge Cycles in Indigenous Cultural Systems_socsci-15-00007.pdf`（§3.2–3.5 pp. 7–15 圖 3–6）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 1 將作者更正為國立臺東大學王任慶（Reen-Cheng Wang）教授團隊；Card 3 依原文圖 3 改寫為四層知識矩陣（$K_1 \sim K_4$）與 12 階段雙向知識循環模型，補列圖 5 之五層 LKM 架構（Layer 1 倫理治理至 Layer 5 代理部署）與圖 6 之 Plan–Act–Observe–Adjust 代理迴圈；刪除虛構之餘弦相似度禁忌損失函數，依原文說明文化禁忌係由部落會議審查、第一手權重與規則矩陣控管；Card 4 交代質性系統架構論文屬性。建立證據表 wiki/evidence/2025-indigenous-tek-ai-revitalization-wang.md，頁面 verification 改為 verified。

### EK-192 | fixed | papers/2025-indigenous-tek-ai-revitalization-wang.md | Card 1 與證據表 | 原文未支持
- **問題**：Card 1 稱作者為「教授」並稱研究「首創」，證據表將教授職稱歸給原文首頁；原文首頁僅列作者與機構，所查全文的 first 包括研究目標排序等用法，未支持該首創斷言。教授職稱目前未由所列來源核實，不應僅因首頁未列就判定職稱為假。此為 EK-078 原先姓名與架構問題以外的新缺口。
- **來源**：[原始論文](https://doi.org/10.3390/socsci15010007) 首頁與全文；[證據表](../../../evidence/2025-indigenous-tek-ai-revitalization-wang.md)。
- **發現於**：2026-11-10，使用者提供之分組複核，Codex by OpenAI 再查原文。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依原文首頁作者與機構移除論文頁未有列示來源支持的教授職稱，以及全文未支持的「首創」主張；證據表同步更正，不推斷作者實際職稱。頁面 verification 改為 partial。

### EK-230 | fixed | papers/2025-indigenous-tek-ai-revitalization-wang.md | 原 Card 2、Card 3 | 原文未支持
- **問題**：原頁三處細節原文沒有：Card 2 稱長老「藉手指感知土壤濕度」（原文只寫憑數十年親身觀察具有判斷土壤濕度的默會知識）；Card 2 稱通用大模型缺乏對排灣族社會階級制（Mamazangiljan）之理解（全文無此詞）；Card 3 第 4 層稱使用 LLaMA、Mistral 系列開源模型微調（原文列 OpenAI、LLaMA、Gemini，未提 Mistral）。另原 Card 5「證明文化保存不能僅靠靜態向量資料庫」「確立終身管轄權」等為 Wiki 加強之表述，原文為作者主張之三項設計原則。
- **來源**：[原文 PDF](../../../../raw/my-focus/大模型輔助/From%20Tacit%20Knowledge%20Distillation%20to%20AI-Enabled%20Culture%20Revitalization%20Modeling%20Knowledge%20Cycles%20in%20Indigenous%20Cultural%20Systems_socsci-15-00007.pdf)，p. 4、p. 8、p. 14、p. 19。
- **發現於**：2026-11-20 改寫為我的關注新六章時回原文抽查，Claude Code by Anthropic（Claude Opus 5.5）。
- **處理**：2026-11-20，Claude Code by Anthropic（Claude Opus 5.5）。改寫論文頁：土壤濕度、模型問題與第 4 層模型改依原文 p. 8、p. 4、p. 14；結果改寫為作者主張之三項設計原則（p. 19）；證據表新增四列。
