# 已結案問題：papers/2021-alphafold2.md

> 本檔收錄 [wiki/papers/2021-alphafold2.md](../../../papers/2021-alphafold2.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-021 | fixed | papers/2021-alphafold2.md | Card 4 | 歸因／版本錯置
- **問題**：r=0.73 出自 Tunyasuvunakool et al. 人類蛋白質組伴篇；Jumper et al. 主論文 Figure 2c 在另一組測試鏈報 r=0.76。須標明出處。
- **來源**：[主論文](https://www.nature.com/articles/s41586-021-03819-2)、[伴篇](https://www.nature.com/articles/s41586-021-03828-1)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文主論文 Figure 2c 查核修訂 Card 4：明確標註主論文在近期 PDB 測試集（$n=10,795$）報告皮爾森相關係數為 $r = 0.76$（線性式 $\text{lDDT-C}_\alpha = 0.997 \times \text{pLDDT} - 1.17$），而在人類蛋白質組伴篇（Tunyasuvunakool et al. 2021）中報告為 $r = 0.73$，標明不同測試集出處。證據表見 wiki/evidence/2021-alphafold2.md。

### EK-022 | fixed | papers/2021-alphafold2.md | Card 3 | 過度表述
- **問題**：原文說三角更新受三角不等式「啟發」，頁面寫成「強制滿足」歐氏三角幾何；並把 IPA 注意力值之不變性與其後座標更新之等變性混稱。
- **來源**：[封存原文](../../../../raw/2021-alphafold2.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Nature 2021 pp. 584–587 查核修訂 Card 3：更正三角更新表述為受三角不等式「啟發」（作為神經先驗引導逼近物理幾何，非剛性滿足）；精確區分 IPA 模組之數學性質：IPA 局部點距離計算之標量值具全局 $\mathrm{SE}(3)$ 不變性（Invariance），而結構模組利用該激活值對殘基剛體座標系實施等變更新（Equivariant Update），修正混稱。證據表見 wiki/evidence/2021-alphafold2.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新掃描論文頁全篇：Card 3 已修正，但 Frontmatter hook 與 Card 5 仍稱三角不等式直接／精確編碼為網路架構；原文僅稱受其啟發，並分別描述 IPA 不變性與座標更新等變性；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Nature 主文及補充資料改寫 hook、Card 3、5、6，將三角不等式寫為啟發、區分 IPA 不變性與座標更新等變性；標題及 Card 1 不再將評測結果擴稱解決所有摺疊問題。相關公式另依原始補充資料更正並登記 EK-194。

### EK-023 | fixed | papers/2021-alphafold2.md | Card 5 | 歸因／版本錯置
- **問題**：把核孔複合體結構寫成直接套用 AF2 預測；後續研究是以 AlphaFold 模型結合 cryo-EM 等實驗資料做整合建模。
- **來源**：[封存主論文](../../../../raw/2021-alphafold2.pdf)、[NPC 整合建模研究](https://pubmed.ncbi.nlm.nih.gov/35679401/)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 典範轉移段落：明確將核孔複合體（NPC）等超大複合體結構解析標記為 AlphaFold 預測模型與低解析度冷凍電鏡（cryo-EM/ET）數據結合之「整合建模（Integrative Modeling）」應用，非單純直接預測之結果。證據表見 wiki/evidence/2021-alphafold2.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新核對 Card 5 與 Mosalaganti et al. 2022 Science（DOI: 10.1126/science.abm9326）：整合建模的歸因已修正，但該來源解析的是 NPC 細胞質環，不能支持頁面所稱完整逾千亞基 NPC 巨型結構已被攻克；建議重開為 open。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。更正前一行書目：DOI 10.1126/science.abm9326 是 Fontana 等的細胞質環研究；Mosalaganti 等為另一篇研究，DOI 10.1126/science.abm9506，報告人類核孔骨架超過九成的整合模型。核對頁面所指範圍時須分別查兩篇，不可混用作者與 DOI，也不可將細胞質環研究視為完整核孔的證據。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。分別列出 Fontana 等的非洲爪蟾細胞質環與 Mosalaganti 等覆蓋超過九成人類核孔骨架的整合模型，各附 DOI 並同步證據表；未將兩者歸為單一完整核孔預測。此頁 verification 改為 partial。

### EK-194 | fixed | papers/2021-alphafold2.md | Card 3 公式與卡片 | 原文不符
- **問題**：原頁三角形乘法更新漏掉輸出投影與閘控，三角形注意力省略注意力頭索引並改名；IPA 權重漏掉外層 $w_L$，FAPE 損失漏掉 $1/Z$。證據表未逐式列明補充資料位置，卡片沿用不一致的注意力式。
- **來源**：[Jumper 等補充資料](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_MOESM1_ESM.pdf) Algorithms 11、13、22、28，pp. 18、19、28、34。
- **發現於**：2026-11-10，處理 EK-022 時回看補充資料，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依各演算法補齊閘控、頭索引、$w_L$ 與 $1/Z$，移除不直接對應原式的獨立推導式；卡片及證據表同步核對。

### EK-195 | fixed | papers/2021-alphafold2.md | Card 4 與卡片 Card 5 | 歸因／版本錯置
- **問題**：原頁與卡片把 AlphaFold DB 超過兩億筆預測結構歸給 Varadi 等 2022 年初版資料庫論文；該論文摘要記載初版逾 36 萬筆，兩億筆為 2022 年 7 月後續資料庫擴充。
- **來源**：[Varadi 等原文](https://doi.org/10.1093/nar/gkab1061) 摘要；[EMBL-EBI 2022 年 7 月公告](https://www.ebi.ac.uk/about/news/technology-and-innovation/alphafold-200-million/)。
- **發現於**：2026-11-10，回查卡片後續研究來源，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。論文頁、卡片及證據表分開標示初版數量與後續擴充，兩億筆改引資料庫發布機構公告。
