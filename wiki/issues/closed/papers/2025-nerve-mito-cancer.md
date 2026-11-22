# 已結案問題：papers/2025-nerve-mito-cancer.md

> 本檔收錄 [wiki/papers/2025-nerve-mito-cancer.md](../../../papers/2025-nerve-mito-cancer.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-039 | fixed | papers/2025-nerve-mito-cancer.md | Card 4 | 原文不符
- **問題**：測序方法、實驗模型與轉移比例被混併；原文為分選癌細胞後之 Nanopore 分析，不是單細胞長讀長測序。
- **來源**：[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328229/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 Nature 2025 原文 §Mitochondrial genome tracking（p. 254）與 Fig. 2h–j 核實 Card 4：更正實驗流程為共培養後經 FACS 螢光活化分選純化人類癌細胞，隨後進行體外 Nanopore 長讀長定序與物種特異性 qPCR，糾正誤寫為「單細胞長讀長定序」之錯誤。證據表見 wiki/evidence/2025-nerve-mito-cancer.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。Nature 原文 Fig. 2f–g 與方法中的 Nanopore 分析為腫瘤組織分選出的 4T1 細胞及變異點附近 420 bp 片段；目前 Card 4 卻合併人類 MDA-MB-231 共培養並稱定序檢出完整小鼠粒線體基因組及其轉錄、複製，須拆開實驗與證據。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。區分人類癌細胞體外共培養、分選小鼠腫瘤 4T1 細胞的 420 bp Nanopore 分析，以及混合球體與宿主神經追蹤的不同轉移模型；刪除完整基因組及其轉錄、複製的無據推論，並逐項更新證據表。

### EK-040 | fixed | papers/2025-nerve-mito-cancer.md | Card 3 | 原文未支持
- **問題**：粒線體轉移—OCR 線性增益、轉移灶富集等符號模型未見於原文，卻呈現為本文模型；須標為教學推導並註明假設。
- **來源**：[封存原文](../../../../raw/2025-nerve-mito-cancer.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 3：在質子動力勢、OCR 線性增益與轉移富集模型前新增數理模型說明，明確標記其為基於 Mitchell 化學滲透假說與群體選擇概率建立之教學唯象推導（Didactic Theoretical Models），非原文直接擬合之實驗方程。證據表見 wiki/evidence/2025-nerve-mito-cancer.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。Card 3 雖已標示教學模型，仍有非本篇原文的區塊公式；現行 wiki-content-audit 要求區塊公式逐條出自原文或補充資料，Wiki 推導限行內或文字並須交代假設及依據。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。移除質子動力勢、OCR 線性增益與轉移富集的非本篇區塊公式，依原文改為特定實驗模型中的定性結果，並更新證據表；verification 改為 partial。

### EK-041 | fixed | papers/2025-nerve-mito-cancer.md | Card 6 | 原文未支持
- **問題**：推論癌細胞偽裝成受損組織、誘使神經元依修復程序供應粒線體；原文支持轉移與富集，未證明此機制，應標作假說或比喻；治療建議亦非本文已驗證療效。
- **來源**：同 EK-040
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照原文修訂 Card 5 與 Card 6：Card 6 將「癌細胞偽裝受損組織誘使神經救濟」明確標註為【演化假說與機制隱喻】，強調本文已嚴格證實轉移與富集現象，但觸發神經供能之上游精確分子信號仍為假說；Card 5 將靶向隧道奈米管之聯合療法明確標記為轉化醫學前景展望，非本文臨床已驗證之療法。證據表見 wiki/evidence/2025-nerve-mito-cancer.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。再次回查原文後，移除把「癌細胞偽裝受損組織」歸給作者的措辭；相關內容明標 Wiki 比喻，並保留其機制尚未證實及治療非臨床驗證的界線。

### EK-197 | fixed | papers/2025-nerve-mito-cancer.md | Card 1、3–6 與證據表 | 原文未支持
- **問題**：頁面與證據表將微流控分室、格點光片顯微鏡及 Cox8-Cre 寫為本篇方法；將體外奈米管樣結構擴稱所有活體轉移路徑；另將部分呼吸救援擴稱完全恢復、去神經化直接抑制遠端轉移灶，並把「癌細胞偽裝」歸為作者假說。這些說法未獲所列原文位置支持。
- **來源**：[Hoover 等原文](https://doi.org/10.1038/s41586-025-09176-8) pp. 253–261、Figures 1–5、Methods；Extended Data Figure 4c。
- **發現於**：2026-11-10，修正 EK-039、EK-040 時交叉複核，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。刪除無依據的方法與過度結論，分別說明體外、活體、小鼠、人類組織及不同追蹤模型的證據；調整標題、索引、證據表與 Wiki 比喻的歸屬。
