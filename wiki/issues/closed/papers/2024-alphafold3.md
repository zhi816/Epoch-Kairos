# 已結案問題：papers/2024-alphafold3.md

> 本檔收錄 [wiki/papers/2024-alphafold3.md](../../../papers/2024-alphafold3.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-029 | fixed | papers/2024-alphafold3.md | Card 4 | 歸因／版本錯置
- **問題**：將介面 LDDT 標成成功率；複雜多醣鏈 72.1% 之歸屬未獲主文支持。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 Nature 2024 原文 Extended Data Table 1 與正文（p. 497）核實修訂 Card 4：更正蛋白質—核酸複合體預測指標為平均介面 LDDT（iLDDT，雙股 DNA 為 64.8、RNA 為 39.4），糾正將分數誤標為百分比成功率之錯誤；修正糖基化與修飾殘基數值歸屬：72.1% 屬高質量單殘基糖基化成功率（多殘基多醣鏈成功率為 42.4%），修飾殘基總體成功率為 59.9%（蛋白質修飾殘基 51.0%、DNA 修飾 68.6%、RNA 修飾 40.9%），共價配體為 78.5%。證據表見 wiki/evidence/2024-alphafold3.md。

### EK-030 | fixed | papers/2024-alphafold3.md | Card 1 | 過度表述
- **問題**：「全面擊敗所有領域專用工具」強於原文「優於許多既有專用工具」；原文按任務與基準分別比較。
- **來源**：[封存原文](../../../../raw/2024-alphafold3.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文摘要與第 493 頁查核修訂 Card 1：將「全面擊敗所有領域專用工具」改為符合原文之「在單一統一深度學習架構中跨越了幾乎所有生物分子交互作用類別，預測準確度顯著超越眾多既有領域專用工具」，交代個別任務與專用工具之具體比較（如蛋白—配體超越對接軟體、蛋白—核酸超越專用預測器，但 CASP15 RNA 仍有人類專家介入模型略高）。證據表見 wiki/evidence/2024-alphafold3.md。

### EK-101 | fixed | papers/2024-alphafold3.md | Card 1 | 過度表述
- **問題**：Card 1 寫 AF3「在單一統一模型中全面擊敗所有領域專用工具」，並稱核酸用「RoseTTAFoldNA」。原文為「In all but one category, it achieves a substantially higher performance than strong methods that specialize in just the given task」；例外為 CASP15 RNA（AF3 47.3，有人工介入之 AIchemy_RNA2 54.5）。證據表 Card 1 列早已記為「核實更正」，但頁面未改。
- **來源**：`raw/2024-alphafold3.pdf`（Abramson et al. 2024, Nature 630:493–500），正文 p. 493；Extended Data Table 1（PDF p. 21）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為「除一類外，各類別均顯著優於只處理該任務的專用方法」並註明例外，工具名改為 RoseTTAFold2NA。

### EK-102 | fixed | papers/2024-alphafold3.md | Card 4 | 原文不符
- **問題**：Card 4 第一點稱 AF3 遠超「最佳深度學習盲對接工具 DiffDock-L（約 38%）」。Extended Data Table 1 所列為 DiffDock（非 DiffDock-L），其 37.9% 是在給定結合態蛋白質結構（Holo protein struct. given）之設定下，並非盲對接。
- **來源**：`raw/2024-alphafold3.pdf`（Abramson et al. 2024, Nature 630:493–500），Extended Data Table 1（PDF p. 21）；正文 p. 496。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為「給定結合態蛋白質結構之 DiffDock 的 37.9%」，並補 PoseBusters V1 之組成（428 個 2021 年以後釋出之結構）與 2019 年訓練截止。

### EK-103 | fixed | papers/2024-alphafold3.md | Card 4 | 原文不符
- **問題**：Card 4 第二點寫蛋白質—RNA「介面成功預測率達 62.4%（RoseTTAFold2NA 28.7%）」、雙股 DNA「成功率達 64.8%」，並稱 CASP15 RNA「超越所有自動預測伺服器」。Extended Data Table 1 之核酸指標為 iLDDT 分數，蛋白質—RNA 為 39.4（RoseTTAFold2NA 19.0），雙股 DNA 為 64.8（28.3）；62.4 與 28.7 不見於原文。CASP15 部分原文只與 RoseTTAFold2NA 及 AIchemy_RNA 比較，且不及 AIchemy_RNA2。證據表已記為更正，但頁面未改。
- **來源**：`raw/2024-alphafold3.pdf`（Abramson et al. 2024, Nature 630:493–500），正文 p. 497；Extended Data Table 1（PDF p. 21）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改為 iLDDT 數值與 N，CASP15 依原文改寫。

### EK-104 | fixed | papers/2024-alphafold3.md | Card 4 | 原文不符
- **問題**：Card 4 第四點寫共價結合配體、「磷酸化/甲基化修飾殘基」及「複雜多醣鏈」之成功率「分別達 78.5%、69.9% 與 72.1%」。原文無 69.9%（修飾殘基整體為 59.9%）；72.1% 為高品質單殘基糖基化，多殘基多醣鏈為 42.4%（正文 42.1%）。證據表已記為更正，但頁面未改。
- **來源**：`raw/2024-alphafold3.pdf`（Abramson et al. 2024, Nature 630:493–500），正文 p. 497；Extended Data Table 1（PDF p. 21）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依 Extended Data Table 1 逐項改寫並附 N。

### EK-105 | fixed | papers/2024-alphafold3.md | Card 3 | 原文不符
- **問題**：Card 3 之擴散損失寫成權重 $w(\sigma_t)$ 只乘均方誤差項；排序公式末項寫 $N_{\text{clash}}$（碰撞數），並稱「對無序區與原子碰撞施加懲罰」。補充資料式 6 之權重乘在 $(\mathcal{L}_{\text{MSE}} + \alpha_{\text{bond}} \mathcal{L}_{\text{bond}})$ 上；式 19 末項為 0 或 1 之 has_clash；disorder 項係鼓勵溶劑可及面積較高之伸展構型（正文 p. 498），並非懲罰無序區。
- **來源**：Abramson et al. (2024) Supplementary Information，式 6（SI p. 28）、§5.9.2 與式 19（SI p. 37）；正文 p. 498。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。兩條區塊公式依補充資料原式改寫，並說明各符號。

### EK-106 | fixed | papers/2024-alphafold3.md | Card 4 後續 | 過度表述
- **問題**：後續研究寫「2024 年 11 月 Google DeepMind 正式向學術界開放 AlphaFold 3 完整原始碼與訓練權重」，並稱開源社群「基於本篇揭示之 Pairformer + 全原子擴散架構復現出 Chai-1 與 MIT Boltz-1」「全面驗證了該架構的可重現性」，未附出處。Nature 附錄（636:E4，2024-11-27）只宣布釋出推論程式碼；Chai-1 與 Boltz-1 之摘要未稱復現 AF3 架構。
- **來源**：Abramson et al. (2024) Addendum, Nature 636:E4, doi:10.1038/s41586-024-08416-7；Chai Discovery (2024) bioRxiv doi:10.1101/2024.10.10.615955；Wohlwend et al. (2024) bioRxiv doi:10.1101/2024.11.19.624167（Crossref 元資料與摘要）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依三份來源改寫並附 DOI。

### EK-107 | fixed | papers/2024-alphafold3.md | Card 5 | 原文不符
- **問題**：Card 5 稱 AF3「自然捕捉到配體結合引發的蛋白質變構效應與口袋構型重組」，以及「擴散生成模型能透過不同隨機種子採樣出完整的構型分佈系綜」；第一點並稱「首次證明」。原文模型限制明言多個隨機種子「do not produce an approximation of the solution ensemble」，且 E3 泛素連接酶在無配體時也被預測為閉合構型；原文未稱「首次」。
- **來源**：`raw/2024-alphafold3.pdf`（Abramson et al. 2024, Nature 630:493–500），摘要 p. 493；模型限制 pp. 497–498、Fig. 5c。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。三點改寫為作者結論與所述限制。

### EK-202 | fixed | papers/2024-alphafold3.md | Card 3 公式與 Card 4 數據條件 | 原文不符
- **問題**：原頁與卡片使用補充資料未列出的自擬座標變換與加噪公式；排序分數式另加原文沒有的左側符號。卡片數據未標出原文評估指標，抗體成功率未寫 1,000 個模型種子的條件。
- **來源**：[官方補充資料](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-024-07487-w/MediaObjects/41586_2024_7487_MOESM1_ESM.pdf) Algorithm 19、§3.7.1、§5.9.3；[原文](../../../../raw/2024-alphafold3.pdf) p. 494 Fig. 1 圖說、PDF p. 21 Extended Data Table 1。
- **發現於**：2026-11-10，處理 TD-011 公式出處及抽查卡片，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。改以原文 Algorithm 19 座標變換步驟及作者文字說明呈現機制，排序公式保留原文表達；逐式登記來源，卡片補上指標與取樣條件，更新示意圖。
