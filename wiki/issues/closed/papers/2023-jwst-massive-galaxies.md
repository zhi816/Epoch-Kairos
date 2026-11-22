# 已結案問題：papers/2023-jwst-massive-galaxies.md

> 本檔收錄 [wiki/papers/2023-jwst-massive-galaxies.md](../../../papers/2023-jwst-massive-galaxies.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-027 | fixed | papers/2023-jwst-massive-galaxies.md | Card 4 | 原文不符
- **問題**：將 ε≈0.57 指派至 z≈7.5；原文此值對應 z≈9.1 之 1σ 邊際一致性，z≈7.5 中心估計約 0.84。「觀測密度為理論上限 2–5 倍」亦超出原文結論。
- **來源**：[原文](https://www.nature.com/articles/s41550-023-01937-7.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 3 與 Figure 2 查核修訂 Card 4：明確標註 Labbé et al. 中心估計值分別對應 $\epsilon(z \approx 7.5) = 0.84$ 與 $\epsilon(z \approx 9) = 0.99$；在考慮星系質量、泊松噪聲與宇宙樣本方差之 $1\sigma$ 不確定度後，在 $z \approx 9.1$ 處與基準 $\Lambda\text{CDM}$ 邊際一致要求 $\epsilon(z \approx 9) \ge 0.57$，糾正原先錯配至 $z \approx 7.5$ 之問題；刪除超出原文結論之「比理論上限高出 2 至 5 倍」陳述。證據表見 wiki/evidence/2023-jwst-massive-galaxies.md。

### EK-028 | fixed | papers/2023-jwst-massive-galaxies.md | Card 3 | 歸因／版本錯置
- **問題**：主計算採 Sheth–Tormen 暈質量函數，後文卻附 Press–Schechter erfc 解析式；須明示 PS 為補充近似，非 Boylan-Kolchin 論文所用之 HMF。
- **來源**：[封存原文](../../../../raw/2023-jwst-massive-galaxies.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:00] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 2 查核修訂 Card 3：明確標註 Boylan-Kolchin 論文之累積暗物質暈數量與質量密度計算係採用 Sheth & Tormen (1999) 橢球坍縮質量函數進行數值積分，並註明互補誤差函數 $\operatorname{erfc}$ 解析解僅為經典 Press-Schechter (1974) 球對稱坍縮近似（用於解釋高斯尾部指數衰減先驗），非論文主計算來源。證據表見 wiki/evidence/2023-jwst-massive-galaxies.md。

### EK-114 | fixed | papers/2023-jwst-massive-galaxies.md | hook 與 Card 1 | 過度表述
- **問題**：`hook` 稱「部分觀測結果甚至要求超過 100% 的重子轉化效率」，Card 1 第 35 行稱即使暗物質暈中 100% 的重子都變成恆星，理論上限「依然低於觀測推估值」。原文為觀測值「lie at the theoretical limit」，對應 ε(z≈9) = 0.99、ε(z≈7.5) = 0.84，作者稱為 physically implausible，計入 1σ 誤差後則為 marginally consistent；並非超過 100%。
- **來源**：`raw/2023-jwst-massive-galaxies.pdf`（Boylan-Kolchin 2023），PDF 第 2 頁。
- **發現於**：第一、二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。以正式版（Nature Astronomy 開放取用全文，PMC10281863）核對後，`hook` 與 Card 1 改寫為：最重候選落在上限邊緣，需 ε(z≈9) = 0.99、ε(z≈7.5) = 0.84（作者稱物理上不太可能），計入 1σ 誤差後 ε(z≈9) ≥ 0.57 才勉強相容；刪去「掀起全面重估」，並改正 JWST 傳回資料之年份敘述與 Labbé 候選之紅移範圍（依 Labbé 摘要）。

### EK-115 | fixed | papers/2023-jwst-massive-galaxies.md | Card 3 與 Card 4 | 原文未支持
- **問題**：Card 3 第 54–55 行之「極值統計（Extreme Value Statistics）鎖定巡天體積中的最重暗物質暈」，與 Card 4 第 85 行之最重暗物質暈質量 $4 \times 10^{11}$、重子極限 $6.5 \times 10^{10}$ 與 $1.2 \times 10^{10}\,M_\odot$、共動體積約 $10^5\,\text{Mpc}^3$ 等數值，原文全文搜尋皆未見；原文之效率推論來自累積數密度與累積恆星質量密度。
- **來源**：同 EK-114 之 PDF，全文搜尋「extreme value」「6.5」「1.2」「4 ×」無相符結果。修正時須再看原文圖 1、圖 2 確認無圖中數值。
- **發現於**：第一、二批卡片回填 B 組回報，協調者以全文搜尋確認（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。預印本與正式版全文、圖 1 與圖 2 之圖中文字均無極值統計與上述三個質量值，刪除；Card 3 第 3 點改為原文之峰高 ν（Results）。共動體積 $V \approx 10^5\,\text{Mpc}^3$ 原文確有（Results 第 1 段，為每個紅移區間之巡天體積），保留並改寫為原文語境。Card 2 之「ε ≈ 0.1–0.3」依 Discussion 改為 ε ≲ 0.2。Card 4 改依 Results 逐項列出數密度、峰高與效率，證據表逐一登記。

### EK-154 | fixed | papers/2023-jwst-massive-galaxies.md | Frontmatter、開頭引言與 Card 3 | 原文不符
- **問題**：（1）Card 3 四條區塊公式皆非原文式：$M_{\text{halo}} = M_\star/(\epsilon f_b) \ge M_\star/f_b \approx 6.4 M_\star$ 為 Wiki 推算（且 $f_b$ 寫成 0.1564，原文為 0.156）；兩條積分把 $\epsilon$ 併入下限，原文式 (3)、(5) 取 $\epsilon = 1$ 並另以式 (1)、(2) 定義積分；Press–Schechter erfc 解析式與 $\delta_c \approx 1.686/D(z)$、$\propto e^{-\nu^2/2}$ 原文沒有（原文為 $\delta_c \approx 1.7$）。證據表未登記任何式號。（2）`title_zh`「JWST 早期宇宙成熟巨大星系發現」使讀者以為本篇發現了星系；本篇為對 Labbé 等候選之理論檢驗，原題為 Stress testing ΛCDM with high-redshift galaxy candidates。（3）開頭引言為 Wiki 撰寫卻未註明。（4）證據表未記載封存原文為 arXiv v2 預印本，而 `doi_url` 指向正式版。
- **來源**：Boylan-Kolchin 2023 正式版全文（PMC10281863），Assumptions 式 (1)–(5)、Results；`raw/2023-jwst-massive-galaxies.pdf`（arXiv:2208.01611v2）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。區塊公式改為原文之 $M_\star = \epsilon f_b M_{\text{halo}}$ 與式 (1)、(2)、(3)、(5)，刪去 Wiki 推算與 erfc 式；`title_zh` 與內文標題改為「以高紅移星系候選對 ΛCDM 宇宙學進行壓力測試」；引言加註為 Wiki 撰寫；證據表註明採用正式版並列出與預印本之差異。

### EK-155 | fixed | papers/2023-jwst-massive-galaxies.md | Card 4 後續與 Card 5 | 原文未支持
- **問題**：Card 4 後續段稱 Kocevski et al. (2023) 發現「Labbé 樣本中質量最大的候選者之一」實為 $z = 5.62$ 之遮蔽型 AGN、恆星質量「下修約一個數量級」，Kocevski 摘要未提 Labbé 樣本與下修幅度；稱 Carnall、Glazebrook、Dekel「光譜確認……效率高達 ε ≈ 0.3–0.5」，三篇摘要皆無此數；Glazebrook 寫成「z > 11 形成之 $10^{11}\,M_\odot$」，摘要為恆星約於 z ∼ 11 形成。Card 5 三點（「改寫教科書」、小紅點黑洞與恆星質量比 1%–10%、「精準劃分」宇宙學與天體物理）皆無出處。
- **來源**：doi:10.3847/2041-8213/ace5a0（Kocevski 2023 摘要）、doi:10.1038/s41586-024-07191-9（Glazebrook 2024，arXiv:2308.05606 摘要）、doi:10.1093/mnras/stad1557（Dekel 2023 摘要）、doi:10.1038/s41586-023-06158-6（Carnall 2023，arXiv:2301.11413 摘要）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪去 Card 4 後續段與 Card 5 三點無出處之敘述；Card 5 改列五篇經摘要核對之後續研究（Dekel 2023、Arrabal Haro 2023、Glazebrook 2024、Desprez 2024、Chworowsky 2024），各附 DOI，並註明結論不一致；Card 4 改列作者自己討論之可能解釋（含黑洞吸積貢獻）；Card 6 第 2 點改為不依賴未查核事實之寫法。證據表登記各列。
