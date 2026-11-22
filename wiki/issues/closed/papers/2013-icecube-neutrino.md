# 已結案問題：papers/2013-icecube-neutrino.md

> 本檔收錄 [wiki/papers/2013-icecube-neutrino.md](../../../papers/2013-icecube-neutrino.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-016 | fixed | papers/2013-icecube-neutrino.md | Card 4 | 原文未支持
- **問題**：「高能端分析 4.3σ、p≈1.5×10⁻⁵」在原文找不到。原文報告為 26 個新事件 3.3σ、預先指定分析合併 28 個事件 4.1σ、事後計算全 28 事件 4.8σ，較高 charm 背景下分別降為 3.6σ 與 4.5σ。
- **來源**：[原文](https://arxiv.org/abs/1311.5238)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Science 2013 p. 4 查核修訂 Card 4：刪除非原文之「4.3σ、p≈1.5×10⁻⁵」陳述，更正為原文統計分析架構：26 個新事件顯著性為 3.3σ；預先指定 Fisher 合併 28 個事件為 4.1σ（90% CL 魅夸克上限下為 3.6σ）；事後全體 28 個事件計算為 4.8σ（90% CL 魅夸克上限下為 4.5σ）。證據表見 wiki/evidence/2013-icecube-neutrino.md。

### EK-017 | fixed | papers/2013-icecube-neutrino.md | Card 3 | 原文不符
- **問題**：99.999% 在原文是 6000 p.e. 門檻以上大氣緲子背景之拒斥率，頁面擴寫為同時濾除大氣微中子；原文仍估計約 6.1 個大氣微中子事件與 6.0 ± 3.4 個穿透緲子事件。
- **來源**：[封存原文](../../../../raw/2013-icecube-neutrino.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Science 2013 pp. 4, 7–8 查核修訂 Card 3：更正 99.999% 為 6000 p.e. 以上「穿透大氣緲子」之拒斥率，南半球大氣微中子伴隨緲子濾除率為約 70%，並補列兩年預期殘留背景之精確數據（6.0 ± 3.4 個緲子與 6.1 個大氣微中子），修正過度概括。證據表見 wiki/evidence/2013-icecube-neutrino.md。

### EK-199 | fixed | papers/2013-icecube-neutrino.md | Card 2–3 公式與卡片 | 原文未支持
- **問題**：論文頁與卡片使用的光錐角度、Frank–Tamm 光譜、截面冪律、存活率及一般化通量展示式未在本篇找到；證據表誤將 Frank–Tamm 公式歸給本文。頁面稱高能微中子穿透地球的碰撞機率極低，卡片更稱不被吸收，與原文指出的高能地球吸收不符。
- **來源**：[Aartsen 等原文](https://arxiv.org/pdf/1311.5238) pp. 2–6、Fig. 1–2；[論文頁](../../../papers/2013-icecube-neutrino.md) Card 2–3。
- **發現於**：2026-11-10，處理 TD-011 公式出處，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。刪除未見於本文的展示式及相關無來源數值，以原文的探測、背景與地球吸收描述取代；證據表同步更正，卡片以原文 p. 6 的資料分析式非探測機制為由採無公式模式，亦修正微中子不被吸收的說法。僅核對相關內容，核實狀態改為 partial。
