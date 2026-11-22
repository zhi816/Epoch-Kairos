# 已結案問題：papers/2007-woodford-globalization-monetary-control.md

> 本檔收錄 [wiki/papers/2007-woodford-globalization-monetary-control.md](../../../papers/2007-woodford-globalization-monetary-control.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-008 | fixed | papers/2007-woodford-globalization-monetary-control.md | Card 1 | 過度表述
- **問題**：「嚴格證明決定權毫不動搖」強於原文摘要「全球化不太可能削弱央行控制通膨的能力」。
- **來源**：[原文（NBER WP 13329）](https://www.nber.org/system/files/working_papers/w13329/w13329.pdf)
- **發現於**：wiki/log.md [2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文摘要 p. 2 與引言修訂 Frontmatter hook 與 Card 1：將「嚴格證明決定權毫不動搖」改述為貼合原文之「系統檢驗金融、商品與要素全球化對貨幣傳導機制三大環節（LM、IS、AS 方程）之影響，論證全球化不太可能削弱央行控制本國通膨動態的能力」。證據表見 wiki/evidence/2007-woodford-globalization-monetary-control.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核卡片封面與 NBER WP 13329 摘要 p. 2：論文頁 hook／Card 1 保留「不太可能削弱」，但卡片封面仍寫成確定語氣「不會讓央行管不住通膨」；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看 NBER 原文摘要 p. 2，將論文頁 card_line 與卡片封面改為「全球化不太可能削弱央行的通膨控制力」，保留作者結論的限定語。

### EK-009 | fixed | papers/2007-woodford-globalization-monetary-control.md | Card 3 | 原文未支持
- **問題**：稱短期利率由準備金付息與供給條件決定，並列出未標號之 IS、NKPC 與廣義確定性公式。原文 p. 36 明說以 Taylor rule 表示政策、未建模央行如何實施操作利率；另行推導之標準式不得標為本文原式。
- **來源**：[封存原文](../../../../raw/2007-woodford-inflation-dynamics.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 §§1–2 查核修訂 Card 3：明確交代基準第 1 節直接以泰勒利率規則表示政策，第 2 節方進一步建構貨幣需求模型論證準備金行政付息對操作目標之保障；替換未標號之拼湊公式為本文之對數線性化開放動態 AD 方程（式 1.27）與開放 AS 關係（式 3.11/3.19）；確定性條件改依本文系統矩陣特徵根求解說明（$\phi_\pi > 1$），並註明廣義確定性不等式屬 Woodford 2003 經典封閉經濟微觀基礎。證據表見 wiki/evidence/2007-woodford-globalization-monetary-control.md。

### EK-010 | fixed | papers/2007-woodford-globalization-monetary-control.md | Card 4 | 原文不符
- **問題**：「本國利率傳導因開放而增強」與原文結論不符，原文指出國內通膨之政策效果不依賴進口份額參數；所列 β=0.99、σ=1、γ=0.2、κ=0.024 校準在原文找不到對應表或頁碼；把任何外國衝擊說成可完全隔絕亦過度概括。
- **來源**：同 EK-008
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 p. 14 註 9–10 與 p. 61 註 54 查核修訂 Card 4：校準參數更正為原文之跨期替代彈性 $\sigma=6.37$（相對風險規避係數約 $0.157$）、$\kappa=0.0236$、$\beta=0.99$、年化泰勒係數 $\phi_\pi=2, \phi_y=1$，開放度比較更正為 $\gamma \in \{0, 0.5, 1.0\}$；修正「完全隔絕」表述，精確說明僅在 $\sigma=1$ 特例下總需求解耦，實證校準下外國衝擊會外溢，但央行可透過調整利率有效對沖外溢影響。證據表見 wiki/evidence/2007-woodford-globalization-monetary-control.md。

### EK-011 | fixed | papers/2007-woodford-globalization-monetary-control.md | Card 5 | 歸因／版本錯置
- **問題**：點陣圖效果、終結貨幣主義及全球合作最優結論屬後續應用或綜合詮釋，被寫成本篇直接研究結果。
- **來源**：同 EK-008
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 典範轉移段落：明確將「終結貨幣主義奠定通膨目標制」歸為 Woodford 系列奠基理論（以 2003 年《Interest and Prices》為代表），將點陣圖與前瞻指引實踐標註為該微觀基礎理論之後續政策延伸應用，並釐清開放經濟貨幣政策獨立性結論與國際協調最優性之文獻界線。證據表見 wiki/evidence/2007-woodford-globalization-monetary-control.md。

### EK-112 | fixed | papers/2007-woodford-globalization-monetary-control.md | Card 3 | 原文不符
- **問題**：Card 3 第 75 行把開放經濟菲利浦曲線寫成國內通膨對「產出缺口」$y_t - y_t^n$、$y_t^* - y_t^{*n}$ 之關係，並標「式 3.11 / 3.19」；原文式 (3.19) 之產出項為相對穩態之對數偏離 $\hat{Y}_t$、$\hat{Y}^*_t$，且另有衝擊項 $-\xi \omega q_t$。第 83 行利率規則寫成 $\phi_y (y_t - y_t^n)$；原文式 (1.23) 為 $\hat{\imath}_t = \bar{\imath}_t + \phi_\pi \pi_t + \phi_y \hat{Y}_t$。
- **來源**：`raw/2007-woodford-inflation-dynamics.pdf`，式 (3.19) 於 PDF 第 58 頁，式 (1.23) 於 PDF 第 13 頁。
- **發現於**：第一、二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。逐式回原文核對後：(3.19) 改為原文式，並補 $\kappa_H$、$\kappa_F$ 之原文定義（PDF p. 58 未編號式）；(1.23) 改為原文式；(1.27) 左側原誤寫 $\hat{\pi}_t$，改為原文之 $\pi_t$，期望算子改為原文之 $E_t$。$\kappa_F$ 之說明原寫「透過進口要素或中間財成本溢出」、「等同於可被抵銷的外生衝擊」，改依 PDF p. 57 寫為 $\sigma > 1$ 時 $\kappa_F < 0$、與 global slack 論點方向相反。Card 3 第 3 點「即使菲利浦曲線極為平坦，央行仍可精確錨定通膨」與第 85 行引自 Woodford (2003) 之確定性條件（不在本篇）一併刪除，改寫為原文式 (1.25)–(1.26) 之向前求解條件。證據表逐式登記式號與 PDF 頁碼。

### EK-150 | fixed | papers/2007-woodford-globalization-monetary-control.md | Card 4 | 原文不符
- **問題**：（1）Card 4 第 94 行標題寫「要素市場全球化（$\tilde{\kappa}_H \to 0$）之極限穩健性證明」，並稱國內產出缺口對邊際成本之影響趨近於零、名目工資與物價須經匯率與利率平價錨定。原文 §3.3 為 $\tilde{\kappa}_H \equiv \kappa(1-\gamma) + \xi\gamma$，不趨近於零；只有 $\nu + \sigma^{-1} > 1$ 時才小於封閉經濟之 $\kappa$，在 Rotemberg & Woodford (1997) 校準下反而較大，作者結論為整合可能使菲利浦曲線變陡；原文未談經匯率與利率平價錨定。（2）第 92 行之 $\beta = 0.99$ 原文未寫；「CPI 通膨初期反應因匯率傳導而更為靈敏」之「因匯率傳導」原文未說，且漏了作者「至少在此校準例中」之限定。（3）第 93 行稱外國衝擊「完全可以被本國貨幣政策有效對沖」，原文結論為本國央行仍可單獨穩定本國通膨、不需國際協調。（4）第 96–99 行把早於本篇之 Eggertsson & Woodford (2003)、Hall (2005) 列為「後續」；Eggertsson & Woodford 頁碼誤為 139-211（Crossref 為 139-233）；Smets & Wouters (2007) 稱成為 FRB/US 等央行標準系統、Eggertsson & Woodford「直接指導」2008 與 2020 年之政策、Hall「解決了 Shimer 謎題」，三者摘要皆無此說。
- **來源**：`raw/2007-woodford-inflation-dynamics.pdf`，PDF pp. 14、24、60–61、71–73、75；doi:10.1257/aer.97.3.586、doi:10.1353/eca.2003.0010、doi:10.1257/0002828053828482（Crossref 書目與摘要）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫 Card 4 四點（參數、Figure 6、外溢與結論、全球要素市場之 $\tilde{\kappa}_H$），刪去 $\beta = 0.99$；相關研究改標「相關研究（非本篇成果）」並註明兩篇早於本篇，各附 DOI，描述改依摘要，改正頁碼。證據表逐項重登。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。原問題包括將早於本篇的研究誤列為後續；論文頁已改為相關研究，但[證據表](../../../evidence/2007-woodford-globalization-monetary-control.md) Card 4 的同一列仍將 Eggertsson & Woodford (2003)、Hall (2005) 與 Smets & Wouters (2007) 整列標為「後續研究」，與該列的「非後續」說明矛盾。證據表類型的處置依 TD-007 待決，本次未修改證據表。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。證據表將本頁按主題選取三篇相關研究的歸類明示為 Wiki 詮釋，註明 2003 與 2005 兩篇早於本篇、不代表後續或承接關係；各研究仍各引其來源。此頁其他 open 問題亦已處理，verification 改為 partial。

### EK-151 | fixed | papers/2007-woodford-globalization-monetary-control.md | Card 5 | 原文未支持
- **問題**：Card 5 三點（本篇與 Woodford 系列理論「終結了貨幣主義舊框架」、「直接啟發」聯準會 2012 年點陣圖、「及時化解政策恐慌，證明……」）均無出處；本篇發表於 2007 年，依 `wiki-content-audit` 須有至少 3 筆附出處之後續研究，頁面一筆也沒有（Card 4 所列兩篇早於本篇）。
- **來源**：頁面第 104–106 行；後續研究以 Crossref 與 OpenAlex 核對：doi:10.1111/j.1468-2362.2009.01248.x、doi:10.1016/j.jmacro.2010.04.002（摘要依 doi:10.24149/gwp33）、doi:10.1111/j.1468-2362.2010.01268.x、doi:10.24149/gwp300，四篇 OpenAlex 皆列為引用本篇（W2106451667）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪去三點無出處之影響敘述，改列四篇檢驗「全球產出缺口」假說之後續研究（Calza 2009、Milani 2010、Ihrig 等 2010、Auer 等 2017，後者結論相反），各附 DOI 與摘要所載之結果，並列 2026 年獎項；證據表登記四列「後續研究」。
