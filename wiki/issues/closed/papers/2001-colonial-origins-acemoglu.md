# 已結案問題：papers/2001-colonial-origins-acemoglu.md

> 本檔收錄 [wiki/papers/2001-colonial-origins-acemoglu.md](../../../papers/2001-colonial-origins-acemoglu.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-005 | fixed | papers/2001-colonial-origins-acemoglu.md | Card 4 | 原文不符
- **問題**：Table 3 第一階段係數原文為 −0.61（SE 0.13），頁面寫 −0.60；制度指標原文為 0–10 分，頁面寫 1–10；奈及利亞與智利差距原文表述為「至多約 7 倍」並提醒測量誤差，頁面之 8.2 倍須標為依四捨五入值計算；穩健性估計不宜概括為單一 0.7–1.0 範圍。
- **來源**：[原文（AER 91(5), 2001）](https://economics.mit.edu/sites/default/files/publications/colonial-origins-of-comparative-development.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 AER 2001 Table 3、4、5、6、7 與 p. 1387 查核修訂 Card 4：更正第一階段係數為 −0.61（SE 0.13）；PRS 產權保護指標更正為 0–10 分；奈及利亞與智利差距依原文表述為「206 對數點、至多約 7 倍差距」，並加註作者對測量誤差之提醒與純依點估計值計算之 8.2 倍對比；穩健性估計拆解為樣本替換（0.92–1.34）、控制歷史地理變數（0.74–1.36）及控制當代疾病健康變數（0.55–0.91），不再概括為單一範圍。證據表見 wiki/evidence/2001-colonial-origins-acemoglu.md。

### EK-006 | fixed | papers/2001-colonial-origins-acemoglu.md | Card 3 | 過度表述
- **問題**：把疾病免疫機制寫成支撐排他性限制之既定事實。原文 pp. 1371–1372 將排他性列為識別假設，並把當代疾病直接影響列為主要疑慮；免疫差異是作者論證假設合理性的依據。
- **來源**：同 EK-005
- **發現於**：wiki/log.md [2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 pp. 1371–1372 查核修訂 Card 3：明確將排他性限制表述為計量識別假設（識別威脅為當代疾病之直接延續影響），將外來歐洲士兵與本土具免疫力成年人口之死亡率差異（引 Philip Curtin 歷史軍事統計）表述為作者論證該假設經濟與流行病學合理性之論據，而非既定客觀事實證明。證據表見 wiki/evidence/2001-colonial-origins-acemoglu.md。

### EK-007 | fixed | papers/2001-colonial-origins-acemoglu.md | Card 5 | 原文未支持
- **問題**：外援與基建必然遭攫取之結論不屬 AJR 2001 實證檢驗，應補直接研究或標為政策推論。
- **來源**：同 EK-005
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 發展援助段落：明確將「單純外援易遭掠奪型菁英攫取」標註為後續制度經濟學文獻與政策延伸觀點，非 AJR 2001 本文直接檢驗之經驗結果。證據表見 wiki/evidence/2001-colonial-origins-acemoglu.md。

### EK-089 | fixed | papers/2001-colonial-origins-acemoglu.md | 證據表採用版本 | 歸因／版本錯置
- **問題**：[證據表](../../../evidence/2001-colonial-origins-acemoglu.md) 第 2 行寫採用 *American Economic Review* 91(5): 1369–1401（2001 年 12 月），並稱「封存版本見 `raw/2001-colonial-origins-acemoglu.pdf`」，各列以 AER 頁碼標示位置。但封存檔實為工作論文版 NBER Working Paper No. 7771（2000 年 6 月，69 頁），頁碼體系不同，工作論文與正式版之表格數值與措辭亦可能有差異；證據表所列 AER 頁碼無法以封存檔核實。須取得 AER 正式版逐列重核，或將證據表改為引用工作論文版並註明頁碼與版本差異。
- **來源**：封存檔 `raw/2001-colonial-origins-acemoglu.pdf` 第 1–2 頁（NBER WP 7771 標題頁與摘要；此兩頁文字層為字型編碼亂碼，以 MinerU 本機 OCR 判讀，正文自第 3 頁起文字層正常）；AER 正式版 https://doi.org/10.1257/aer.91.5.1369
- **發現於**：wiki/log.md [2026-11-09 15:13] fix（Claude Code by Anthropic）
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。採用 MIT Economics 提供的正式 AER 全文 PDF，逐列核對本文數值與頁碼；封存之 NBER WP 7771 維持工作論文版本並明確註記未用作 AER 頁碼依據。修正 Table 3 p. 1385、Table 4 Panel A/C Column (1)、Tables 5–7 數值範圍與頁碼；論文頁同步更正穩健性分類及作者報告的 206 log points／約 7 倍上限，並將 8.2 倍標為從四捨五入數字重算。證據表與論文頁 verification 改為 verified。

### EK-198 | fixed | papers/2001-colonial-origins-acemoglu.md | Card 3 公式 | 原文未支持
- **問題**：論文頁把作者的文字示意鏈改寫為自擬符號區塊公式，並將自行寫出的第二階段及 2SLS 機率極限式作為展示公式；另將原文式 (4) 的對數記號改為 ln。
- **來源**：[AER 正式版](https://economics.mit.edu/sites/default/files/publications/colonial-origins-of-comparative-development.pdf) pp. 1370、1378、1383–1384，式 (1)–(5)。
- **發現於**：2026-11-10，處理 TD-011 公式出處，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。將自擬示意與估計式改為作者方法和識別假設的文字說明，恢復式 (4) 的原文記號，並逐式登記原文位置；卡片使用的式 (1) 未變。僅核對本次相關內容，核實狀態改為 partial。
