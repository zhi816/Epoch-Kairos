# 已結案問題：papers/2016-ligo-gravitational-waves.md

> 本檔收錄 [wiki/papers/2016-ligo-gravitational-waves.md](../../../papers/2016-ligo-gravitational-waves.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-132 | fixed | papers/2016-ligo-gravitational-waves.md | Card 3 | 原文不符
- **問題**：Card 3 寫雷射光在臂內「往復反射約 280 次（等效光程擴增至約 1,120 km）」、腔內功率「100 kW（設計目標 750 kW）」、兩站「相距 3,002 km」。原文為臂內共振腔把重力波對光相位的效應放大 300 倍；20 W 輸入在分光鏡上增為 700 W、每條臂腔內循環 100 kW；原文未提 280 次、1,120 km、750 kW 與 3,002 km，只寫兩站之間 10 毫秒光行時間。另「雙場所同步验证」一詞用了簡體字。
- **來源**：`raw/2016-ligo-gravitational-waves.pdf`（Abbott et al. 2016, PRL 116:061102），§III Detectors, pp. 3–4；§II, p. 2。
- **發現於**：建立證據表時回原文核對（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫為 300 倍、20 W → 700 W → 100 kW、10 毫秒光行時間，刪除無出處之數字。

### EK-133 | fixed | papers/2016-ligo-gravitational-waves.md | Card 4 | 原文不符
- **問題**：Card 4 寫訊號「在 0.2 s 內完成 8 個週期，頻率由 35 Hz 橫掃至 250 Hz」。原文為約 0.2 秒、約 8 個週期內由 35 Hz 升至 150 Hz（振幅最大處）；35 至 250 Hz 是摘要對整段訊號頻率範圍的描述，兩者被混寫。
- **來源**：同 EK-132 之 PDF，§II, p. 3；摘要 p. 1。
- **發現於**：建立證據表時回原文核對（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。分開寫明 0.2 秒、8 週期、35 至 150 Hz 與整段 35 至 250 Hz。

### EK-134 | fixed | papers/2016-ligo-gravitational-waves.md | Card 2 | 原文不符
- **問題**：Card 2 寫空氣分子碰撞「需維持 1.2 × 10^4 m^3 超高真空」，並稱各種雜訊「每一項都比重力波信號大上數個至十數個數量級」；又稱臂長差「僅相當於單一質子直徑的千分之一」。原文為直徑 1.2 公尺之臂腔光束管道氣壓維持在 1 μPa 以下，隔震系統對 10 Hz 以上地面振動提供超過 10 個數量級之隔離；原文未比較各雜訊與訊號之量級，也未以質子比喻（約 4 × 10^-18 m 與質子直徑之比亦非千分之一）。
- **來源**：同 EK-132 之 PDF，§III, p. 4。
- **發現於**：建立證據表時回原文核對（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫雜訊頻段、隔震與真空之敘述，刪除質子比喻，臂長差標為依原文數據計算。

### EK-135 | fixed | papers/2016-ligo-gravitational-waves.md | Card 3 公式 | 原文未支持
- **問題**：啁啾質量公式改寫為 $[(5/96)^3 \pi^{-8} f^{-11} \dot{f}^3]^{1/5}$，與原文之寫法 $[(5/96)\pi^{-8/3} f^{-11/3} \dot{f}]^{3/5}$ 不同（數學上等價，但非原文式）；$E_{\text{GW}} = (m_1 + m_2 - M_f)c^2$ 為 Wiki 自擬之區塊公式；以「最後穩定圓軌道頻率與總質量成反比，直接證明只能是黑洞」說明，原文之推論則是以 75 Hz 軌道頻率與約 350 km 間距排除中子星，並稱黑洞是「唯一已知」夠緻密之天體。另 TT 規範、$\Box h_{\mu\nu} = 0$ 與天線方向圖函數之敘述原文未寫。
- **來源**：同 EK-132 之 PDF，§II, p. 3；§III, p. 3；§VI, p. 7。
- **發現於**：建立證據表時回原文核對（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。啁啾質量改為原文寫法；刪除 $E_{\text{GW}}$ 區塊公式，改以文字寫原文估計值；黑洞推論改依原文；刪除原文未寫之背景式。兩條區塊公式皆登記於證據表。

### EK-136 | fixed | papers/2016-ligo-gravitational-waves.md | Card 4 與 Card 5 | 原文未支持
- **問題**：Card 4 稱峰值光度「在那一瞬間比全可觀測宇宙所有恆星的電磁發光總和還要亮數十倍」，並稱重力子界限「與無質量引力子完全相容」；Card 5 稱過去只能推測「5–15 M☉」黑洞、GW150914「改寫了低金屬豐度大質量恆星演化理論」、兩黑洞以「v/c ≈ 0.6」碰撞，並以「標準汽笛」為本篇影響而無出處。原文無前兩項比較；原文為「質量大於約 25 M☉ 之恆星級黑洞存在」、「形成需要較弱恆星風，在金屬豐度低於太陽約一半之環境才可能」；速度只見於圖 2 之曲線，正文未給數值；標準汽笛是 2017 年 GW170817 之後續研究。
- **來源**：同 EK-132 之 PDF，§VI, pp. 7–8；Abbott et al. (2017), Nature 551:85–88, doi:10.1038/nature24471（摘要）。
- **發現於**：建立證據表時回原文核對（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪除無出處之比較與速度，Card 5 改依原文 p. 8 之結論；標準汽笛改列為後續研究並附出處。

### EK-137 | fixed | papers/2016-ligo-gravitational-waves.md | Card 4 後續 | 歸因／版本錯置
- **問題**：後續第一點把「重力波速度與光速之相對偏差小於 10^-15」歸給 PRL 119:161101 與 ApJL 848:L12，並稱「確認」金、鉑等重元素源自中子星併合、有「約 70」座天文台參與；第二點稱 GWTC-3（PRX 13:041039）藉「頻率相關量子壓縮態光」累計「近百起以至數百起」事件。速度界限出自 ApJL 848:L13（光速的 −3 × 10^-15 至 +7 × 10^-16）；三篇摘要皆未稱確認重元素來源；GWTC-3 摘要為前三次觀測運行共 90 起候選事件，未提頻率相關壓縮光。
- **來源**：Abbott et al. (2017) PRL 119:161101、ApJL 848:L12、ApJL 848:L13；Abbott et al. (2023) PRX 13:041039（Crossref 書目與 arXiv 摘要）。
- **發現於**：建立證據表時查核後續研究（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。後續改為五筆，各依其摘要撰寫並附 DOI。

### EK-138 | fixed | papers/2016-ligo-gravitational-waves.md | hook、開頭引言與 Card 1 | 過度表述
- **問題**：`hook` 稱以「質子直徑千分之一」之精度「完美驗證」廣義相對論；Card 1 稱「連愛因斯坦本人一度都認為人類永遠不可能測出」；開頭引言稱人類「四百年來始終只用眼睛看光」，且未註明為 Wiki 撰寫。原文為愛因斯坦了解重力波振幅會非常微小，1957 年前學界對其是否存在有爭論；本篇結論為首次直接偵測與波形與廣義相對論預測相符。
- **來源**：同 EK-132 之 PDF，摘要與 §I, p. 1。
- **發現於**：建立證據表時回原文核對（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`hook` 與 Card 1 依原文改寫；開頭引言改寫並加註「本頁引言為 Wiki 撰寫，非原文」。
