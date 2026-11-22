# 已結案問題：papers/2023-drugclip.md

> 本檔收錄 [wiki/papers/2023-drugclip.md](../../../papers/2023-drugclip.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-024 | fixed | papers/2023-drugclip.md | Card 4 | 原文不符
- **問題**：DUD-E 與 LIT-PCBA 之 EF、AUROC、BEDROC 數值與指標歸屬與原文表格不一致；10.66 被錯標為 LIT-PCBA BEDROC，原文該值屬 DUD-E EF@5%；HomoAug 之 LIT-PCBA 4.21 → 5.51 消融敘述未見於原文表格。
- **來源**：[原文](https://www.proceedings.com/content/075/075280-1932open.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 NeurIPS 2023 原文 Table 1、Table 3、Table 5 修正：DUD-E 零樣本精確更正為 EF@1%=31.89（EF@0.5%=38.07、EF@5%=10.66、AUROC=80.93%、BEDROC=50.52%）；LIT-PCBA 精確更正為 EF@1%=5.51（EF@0.5%=8.56、EF@5%=2.27、BEDROC=6.23%、AUROC=57.17%），糾正將 10.66% 誤植為 LIT-PCBA BEDROC 之錯誤；消融段落改述 Table 5（DUD-E 上引入 HomoAug 使 BEDROC 由 45.81% 升至 50.52%、EF@1% 由 29.12 升至 31.89），刪除非原文之 LIT-PCBA 4.21 到 5.51 陳述。證據表見 wiki/evidence/2023-drugclip.md。

### EK-025 | fixed | papers/2023-drugclip.md | Card 3 | 原文不符
- **問題**：寫「十億個分子全庫檢索在毫秒內完成」；原文 Section 4.3 報告 6 billion Enamine 分子檢索耗時少於 10,000 秒（約 2.78 小時；原文括號之「30 小時」與其秒數不符，見 22:44 勘誤）。
- **來源**：[封存原文](../../../../raw/2023-drugclip.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:00] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 4.3（p. 8）查核修訂 Card 3 與 Card 4：更正檢索速度表述，明確指出 60 億 Enamine 分子庫在預編碼後單靶點檢索耗時小於 10,000 秒（約 2.78 小時；原文括號誤註為約 30 小時），相較商業對接（100 億分子約需 3,000 年）具顯著效率優勢，刪除「毫秒內完成十億級全庫檢索」之誇大陳述。證據表見 wiki/evidence/2023-drugclip.md。

### EK-026 | fixed | papers/2023-drugclip.md | Card 3 | 原文未支持
- **問題**：test-time 取 K 個構型最大相似度未見於原文方法（RDKit 構型主要用於訓練期噪聲輸入與消融）；HomoAug 實際流程為同源序列搜尋、AlphaFold DB、TM-align 與相似度篩選，頁面所寫 Pfam 未獲支持。
- **來源**：同 EK-025
- **發現於**：wiki/log.md [2026-11-08 22:00] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 3.4 與 Appendix B.1 查核修訂 Card 3：更正 HomoAug 資料增強技術流程為 Jackhmmer 搜尋 AlphaFold DB 聚類庫、TMalign 結構對齊（TM-score $\ge 0.4$、結合口袋對齊率 $\ge 40\%$）與 $6\,\text{Å}$ 口袋原子擷取，刪除非原文之 Pfam；刪除非原文之推論期多構型最大池化公式，改述原文 Proposition 1 數學原理（RDKit 構型用於訓練期帶噪聲輸入以消除訓練—測試不一致性，推論期由雙塔向量點積或餘弦直接檢索）。證據表見 wiki/evidence/2023-drugclip.md。

### EK-227 | fixed | papers/2023-drugclip.md | Card 4 後續領域關鍵證據 | 原文不符
- **問題**：原頁 Card 4「後續領域關鍵證據」稱團隊在論文及後續跟進實驗中針對多巴胺受體、5-羥色胺轉運體（SERT）與新型抗腫瘤靶點進行實驗並取得 $15\%$–$20\%$ 以上命中率，卻未附任何 DOI 或正式出處，且 2023 年 NeurIPS 原文並無濕實驗；經核對該團隊 *Science*（2026）正式論文摘要，濕實驗命中率與冷凍電鏡驗證靶點實為去甲腎上腺素轉運體（NET，$15\%$ 命中率與 2 個抑制劑冷凍電鏡複合物）及 TRIP12（僅依 AlphaFold2 結構達 $17.5\%$ 命中率），並釋出涵蓋約 10,000 個人類蛋白質對 5 億化合物之 GenomeScreenDB。此外，原頁缺少至少 3 篇具明確出處之後續引用研究供卡片 Card 5 使用。
- **來源**：[Jia 等（2026）*Science* 391(6781):eads9530](https://doi.org/10.1126/science.ads9530)（PubMed 41505557 摘要）；[Feng 等（2025）*Patterns* 6(10):101371](https://doi.org/10.1016/j.patter.2025.101371)；[He 等（2026）*AAAI* 40(1):354–362](https://doi.org/10.1609/aaai.v40i1.36997)；[Zhang（2026）*Drug Development Research* 87(5):e70351](https://doi.org/10.1002/ddr.70351)。
- **發現於**：2026-11-15 撰寫 `2023-drugclip` 卡片前回第一手來源抽查，Antigravity by Google DeepMind（Gemini 4 Hydrogen）。
- **處理**：2026-11-15，Antigravity by Google DeepMind（Gemini 4 Hydrogen）。更正 `wiki/papers/2023-drugclip.md` Card 4「後續領域關鍵證據」，以 Jia 等（2026）*Science* 實測 NET（$15\%$）與 TRIP12（$17.5\%$）取代無出處之 SERT／多巴胺受體說法，並補入 Feng 等（2025）、He 等（2026）與 Zhang（2026）共四筆附 DOI 之後續研究，同步補登於 `wiki/evidence/2023-drugclip.md`。
