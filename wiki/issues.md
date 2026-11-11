# 內容問題清單（Issues）

> 本檔登記查核發現之待修正事項，格式與狀態規則見 [AGENTS.md](../AGENTS.md) 第七章第 4 節。標題五段依序為：編號、狀態（`open` / `fixed` / `wontfix`）、相對於 `wiki/` 之檔案、位置、判定。修正時就地改狀態並追加「處理」行，不得刪除條目。
>
> EK-001 至 EK-056 係於 2026-11-09 自 [wiki/log.md](log.md) 2026-11-08 21:40 至 23:36 之 audit 條目逐筆轉錄（原查核者均為 Codex by OpenAI，EK-031 例外），問題描述與來源沿用原條目，轉錄時未重新核對原文。修正前須依 `wiki-content-audit` 回原文確認，不得只照本檔描述改寫。EK-057 至 EK-060 為轉錄同日以 `crossref_check.py` 查得之 DOI 問題。EK-061 至 EK-087 於 2026-11-09 00:55 之 audit 逐筆登記（Antigravity by Google DeepMind）。EK-088 至 EK-090 為同日核對證據表採用版本與先前修正引用時發現之錯置（Claude Code / DeepSeek Harness）。EK-091 至 EK-123 為 2026-11-09 至 2026-11-10 第一、二批卡片回填查核登記（Claude Code by Anthropic 等）。EK-130 至 EK-142、EK-150 至 EK-160、EK-170 至 EK-175 為 2026-11-10 第三批卡片回填抽查與概念頁同步登記（A、B、C 組依保留區段取號）。原有 153 筆條目與後續複核新增條目之狀態，以各條標題為準。條目依論文分節排列，編號順序不因分節而重排。

---

## 1982 Hopfield 網路

### EK-001 | fixed | papers/1982-hopfield-network.md | Card 3 | 過度表述
- **問題**：把所有局部能量極小值等同預先寫入的記憶吸引子。原文指出零閾值下全零狀態亦為穩定態，高能穩定態不必是儲存記憶；p. 5 隨機初態模擬（N=30、n=5）約 85% 落入已指定記憶、10% 落入無明顯意義之穩定態、5% 落在記憶附近。
- **來源**：[封存原文](../raw/1982-hopfield-network.pdf)，PNAS 79:2554–2558
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 p. 2556–2557 逐項確認後重寫 Card 3：明記並非所有局部極小值皆為名義記憶吸引子，零閾值下全零態（$0000\dots$）亦為穩定態，且隨機初態約有 10% 試驗落入無意義偽穩定態（Spurious States）、5% 停留在目標記憶鄰近態。證據表見 wiki/evidence/1982-hopfield-network.md。

### EK-002 | fixed | papers/1982-hopfield-network.md | Card 4 | 原文不符
- **問題**：寫作「隨機正交型態」並稱 N=100 可穩定檢索 15 個完整記憶。原文稱隨機型態具 pseudoorthogonality，容量約 0.15N 是誤差變嚴重前之近似容量，不保證完整無誤檢索。另「隨機切除相當比例突觸或損毀神經元仍可正確重建」在原文無定量結果，須降格或另引直接實驗。
- **來源**：[封存原文](../raw/1982-hopfield-network.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 p. 2556–2557 逐項確認後重寫 Card 4：改述隨機型態具「偽正交性（pseudoorthogonality）」而非嚴格正交；容量 0.15N 註明為嚴重錯誤前之近似上限，並列出 N=100 時 n=5/10/15 之誤差分佈實況；補列信噪比高斯尾部單一位元錯誤率積分式 (10)；將突觸損毀定量表述降格為原文之非對稱突觸（信噪比降 $1/\sqrt{2}$）、二值截斷（信噪比降 $\sqrt{2/\pi}$）及隨突觸失效平緩退化之 fail-soft 質性分析。證據表見 wiki/evidence/1982-hopfield-network.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核論文頁 Card 4 與 PNAS p. 2557：非對稱連結及權重截斷的信噪比分析有原文依據，但「隨突觸失效增加而平緩退化」未見隨機失效實驗支持；建議重開為 open。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。更正前一行回核理由：Hopfield 原文 p. 2557 右欄確實以分析描述隨突觸失效而呈現 fail-soft，不能因未報不同失效比例的實驗而稱原文完全未支持此質性描述。同段原文寫信噪比與錯誤率皆緩慢上升，與前述信噪比下降以及 Wiki 現寫的下降方向存在待釐清差異；修訂時保留分析與實驗的區分，不應直接刪除有來源的 fail-soft。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 pp. 2556–2557 及 Fig. 2，將 $n=5$ 的「零錯誤」改為原文的「幾乎總是」；區分單向連接模擬與平緩退化分析，記錄原文信噪比方向的內部張力，不推定作者原意；同步更新證據表及卡片用詞。頁面 verification 改為 partial。

## 1992 Aghion–Howitt 創造性破壞

### EK-003 | fixed | papers/1992-creative-destruction-aghion.md | Card 4 | 過度表述
- **問題**：成長率與變異數公式以線性研發技術 φ(n)=n 為條件，卡片未明示；原文只說某些條件下存在週期均衡，頁面稱可解釋實際商業週期，強於原文。
- **來源**：[Aghion & Howitt 原文（Econometrica 60(2), 1992）](https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf)
- **發現於**：wiki/log.md [2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Econometrica 1992 pp. 333, 335–338 查核後修訂：Card 3 明確標註穩態對數成長率 $g=\lambda\hat{n}\ln\gamma$ 與方差 $\sigma^2=\lambda\hat{n}(\ln\gamma)^2$ 係在線性研發技術 $\phi(n)=n$ 條件下成立；Card 4 修正極限環陳述，精確說明 2 階極限環係在跨期映射導數 $\psi'(\hat{n}) < -1$ 條件下湧現之理論動態特徵，降格原先「可解釋商業週期」之過度表述。證據表見 wiki/evidence/1992-creative-destruction-aghion.md。
- **處理**：2026-11-09，DeepSeek Harness（DeepSeek-V4.1-Flash）。本條原處理行引用之「§2.4, p. 333, 式 (2.16)–(2.17)」與「Proposition 2」「$\psi'(\hat{n})<-1$」經正式版核對後確認有誤，正確位置與條件見 EK-090；論文頁與證據表已同步更正。

### EK-004 | fixed | papers/1992-creative-destruction-aghion.md | Card 5 | 原文未支持
- **問題**：把 1992 模型直接連到現代反壟斷標準與 Killer Acquisitions；屬後續政策延伸，須另引研究並標明非本文結果。Card 6 若有同類政策結論亦同。
- **來源**：同 EK-003
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 反壟斷政策段落：明確將科技巨頭併購審查與扼殺式收購（Killer Acquisitions，引 Cunningham et al., 2021 JPE）標記為創造性破壞架構在後續產業組織文獻與政策實踐之延伸應用，非 1992 奠基論文之直接檢驗結果。證據表見 wiki/evidence/1992-creative-destruction-aghion.md。

### EK-088 | fixed | papers/1992-creative-destruction-aghion.md | 證據表採用版本 | 未能核實
- **問題**：[證據表](evidence/1992-creative-destruction-aghion.md) 第 2 行寫「封存版本見 `raw/1992-creative-destruction-aghion.pdf`」，並據以將各列標為「符合來源」（引用 *Econometrica* pp. 323–351 之式 (2.1)–(2.17) 等位置）。但該封存檔實為 Giuseppe Bertola, "Factor Shares and Savings in Endogenous Growth", NBER Working Paper No. 3851（1991 年 9 月，31 頁，純圖片、無文字層），並非 Aghion and Howitt (1992)；全檔僅參考文獻提及 Aghion 一次。證據表各列之頁碼與公式位置無法以封存檔核實，頁面 `verified` 狀態缺乏可追溯之來源。須由使用者將封存檔換為 *Econometrica* 正式版後，依原文重新核對證據表各列。
- **來源**：封存檔 `raw/1992-creative-destruction-aghion.pdf` 第 1–2 頁（標題頁與摘要）及第 16、30–31 頁（以 MinerU 本機 OCR 確認內容）；正式版 *Econometrica* 60(2): 323–351，https://doi.org/10.2307/2951599
- **發現於**：wiki/log.md [2026-11-09 15:13] fix（Claude Code by Anthropic）
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。改採 Econometrica 正式版全文（JSTOR 掃描複本，由 University of Copenhagen 網站提供：https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf；DOI: https://doi.org/10.2307/2951599），逐列重核證據表並更正公式與頁碼。raw/1992-creative-destruction-aghion.pdf 仍是 Bertola 的 NBER WP 3851，依 raw 唯讀規範保留、不作為證據來源；此條改以正式版可追溯來源解決，不再要求該檔作為核實前提。

### EK-090 | fixed | papers/1992-creative-destruction-aghion.md | Card 3–4 與證據表 | 原文不符
- **問題**：EK-003 之處理行與證據表列「§2.4, p. 333, 式 (2.16)–(2.17)」，並稱 2 階循環為「Proposition 2」、於跨期映射導數 $\psi'(\hat{n}) < -1$ 時湧現。惟 *Econometrica* 正式版全文僅有 Proposition 1（p. 334），無式 (2.16)–(2.17)；平均成長率與方差實為 §3.C 之式 (3.11)（p. 336），原文寫作 $AGR=\lambda\phi(\hat{n})\ln\gamma$、$VGR=\lambda\phi(\hat{n})(\ln\gamma)^2$，$\lambda\hat{n}\ln\gamma$ 僅為線性研發 $\phi(n)=n$ 之特例。2 階循環（two-cycle）之存在條件為無成長陷阱存在且 $c'(\hat{n})+b'(\hat{n})>0$（§3.A, p. 333）；Cobb–Douglas 線性研發下，$\alpha$ 與 $r$ 足夠小時可出現實質 two-cycle（§3.A, p. 334）；原文未以 $\psi'(\hat{n})<-1$ 表述，亦未使用「極限環（limit cycle）」一詞。
- **來源**：*Econometrica* 60(2): 323–351 正式版掃描本（JSTOR stable 2951599），p. 333、p. 334、p. 336；https://doi.org/10.2307/2951599
- **發現於**：wiki/log.md [2026-11-09 20:12] fix（DeepSeek Harness）
- **處理**：2026-11-09，DeepSeek Harness（DeepSeek-V4.1-Flash）。回正式版掃描本核對後修正：論文頁 Card 3 改引式 (3.11)（§3.C, p. 336），成長率與方差改以 $\lambda\phi(\hat{n})$ 通式表述並註明線性研發特例；Card 4 刪除「Proposition 2」與 $\psi'(\hat{n})<-1$ 之無來源條件，改述 two-cycle 之實際存在條件。證據表同步更正兩列之位置與敘述。EK-003 原處理行之錯誤引用由本條更正。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。再核對期刊全文後明確拆分頁碼：一般 two-cycle 條件在 p. 333；Cobb–Douglas 線性研發下「$\alpha$ 與 $r$ 足夠小」的特例在 p. 334。論文頁與證據表均同步更正，避免把特例錯標為 p. 332–333。

## 2001 Acemoglu–Johnson–Robinson 殖民起源

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
- **問題**：[證據表](evidence/2001-colonial-origins-acemoglu.md) 第 2 行寫採用 *American Economic Review* 91(5): 1369–1401（2001 年 12 月），並稱「封存版本見 `raw/2001-colonial-origins-acemoglu.pdf`」，各列以 AER 頁碼標示位置。但封存檔實為工作論文版 NBER Working Paper No. 7771（2000 年 6 月，69 頁），頁碼體系不同，工作論文與正式版之表格數值與措辭亦可能有差異；證據表所列 AER 頁碼無法以封存檔核實。須取得 AER 正式版逐列重核，或將證據表改為引用工作論文版並註明頁碼與版本差異。
- **來源**：封存檔 `raw/2001-colonial-origins-acemoglu.pdf` 第 1–2 頁（NBER WP 7771 標題頁與摘要；此兩頁文字層為字型編碼亂碼，以 MinerU 本機 OCR 判讀，正文自第 3 頁起文字層正常）；AER 正式版 https://doi.org/10.1257/aer.91.5.1369
- **發現於**：wiki/log.md [2026-11-09 15:13] fix（Claude Code by Anthropic）
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。採用 MIT Economics 提供的正式 AER 全文 PDF，逐列核對本文數值與頁碼；封存之 NBER WP 7771 維持工作論文版本並明確註記未用作 AER 頁碼依據。修正 Table 3 p. 1385、Table 4 Panel A/C Column (1)、Tables 5–7 數值範圍與頁碼；論文頁同步更正穩健性分類及作者報告的 206 log points／約 7 倍上限，並將 8.2 倍標為從四捨五入數字重算。證據表與論文頁 verification 改為 verified。

## 2007 Woodford 通膨動態

### EK-008 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 1 | 過度表述
- **問題**：「嚴格證明決定權毫不動搖」強於原文摘要「全球化不太可能削弱央行控制通膨的能力」。
- **來源**：[原文（NBER WP 13329）](https://www.nber.org/system/files/working_papers/w13329/w13329.pdf)
- **發現於**：wiki/log.md [2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文摘要 p. 2 與引言修訂 Frontmatter hook 與 Card 1：將「嚴格證明決定權毫不動搖」改述為貼合原文之「系統檢驗金融、商品與要素全球化對貨幣傳導機制三大環節（LM、IS、AS 方程）之影響，論證全球化不太可能削弱央行控制本國通膨動態的能力」。證據表見 wiki/evidence/2007-woodford-inflation-dynamics.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核卡片封面與 NBER WP 13329 摘要 p. 2：論文頁 hook／Card 1 保留「不太可能削弱」，但卡片封面仍寫成確定語氣「不會讓央行管不住通膨」；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看 NBER 原文摘要 p. 2，將論文頁 card_line 與卡片封面改為「全球化不太可能削弱央行的通膨控制力」，保留作者結論的限定語。

### EK-009 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 3 | 原文未支持
- **問題**：稱短期利率由準備金付息與供給條件決定，並列出未標號之 IS、NKPC 與廣義確定性公式。原文 p. 36 明說以 Taylor rule 表示政策、未建模央行如何實施操作利率；另行推導之標準式不得標為本文原式。
- **來源**：[封存原文](../raw/2007-woodford-inflation-dynamics.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 §§1–2 查核修訂 Card 3：明確交代基準第 1 節直接以泰勒利率規則表示政策，第 2 節方進一步建構貨幣需求模型論證準備金行政付息對操作目標之保障；替換未標號之拼湊公式為本文之對數線性化開放動態 AD 方程（式 1.27）與開放 AS 關係（式 3.11/3.19）；確定性條件改依本文系統矩陣特徵根求解說明（$\phi_\pi > 1$），並註明廣義確定性不等式屬 Woodford 2003 經典封閉經濟微觀基礎。證據表見 wiki/evidence/2007-woodford-inflation-dynamics.md。

### EK-010 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 4 | 原文不符
- **問題**：「本國利率傳導因開放而增強」與原文結論不符，原文指出國內通膨之政策效果不依賴進口份額參數；所列 β=0.99、σ=1、γ=0.2、κ=0.024 校準在原文找不到對應表或頁碼；把任何外國衝擊說成可完全隔絕亦過度概括。
- **來源**：同 EK-008
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 p. 14 註 9–10 與 p. 61 註 54 查核修訂 Card 4：校準參數更正為原文之跨期替代彈性 $\sigma=6.37$（相對風險規避係數約 $0.157$）、$\kappa=0.0236$、$\beta=0.99$、年化泰勒係數 $\phi_\pi=2, \phi_y=1$，開放度比較更正為 $\gamma \in \{0, 0.5, 1.0\}$；修正「完全隔絕」表述，精確說明僅在 $\sigma=1$ 特例下總需求解耦，實證校準下外國衝擊會外溢，但央行可透過調整利率有效對沖外溢影響。證據表見 wiki/evidence/2007-woodford-inflation-dynamics.md。

### EK-011 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 5 | 歸因／版本錯置
- **問題**：點陣圖效果、終結貨幣主義及全球合作最優結論屬後續應用或綜合詮釋，被寫成本篇直接研究結果。
- **來源**：同 EK-008
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 典範轉移段落：明確將「終結貨幣主義奠定通膨目標制」歸為 Woodford 系列奠基理論（以 2003 年《Interest and Prices》為代表），將點陣圖與前瞻指引實踐標註為該微觀基礎理論之後續政策延伸應用，並釐清開放經濟貨幣政策獨立性結論與國際協調最優性之文獻界線。證據表見 wiki/evidence/2007-woodford-inflation-dynamics.md。

## 2012 CRISPR-Cas9

### EK-012 | fixed | papers/2012-crispr-cas9.md | Card 1 | 過度表述
- **問題**：寫更換 20 nt 即可「靶向任意基因」，省略 S. pyogenes Cas9 所需之 NGG PAM。
- **來源**：[封存原文](../raw/2012-crispr-cas9.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Science 2012 pp. 816–817 查核後修訂 Frontmatter hook 與 Card 1：明確補列化膿性鏈球菌 Cas9 靶向序列必須緊鄰 5'-NGG-3' PAM 基序之絕對前提條件，消除「任意基因」無約束靶向之過度表述。證據表見 wiki/evidence/2012-crispr-cas9.md。

### EK-013 | fixed | papers/2012-crispr-cas9.md | Card 4 | 原文不符
- **問題**：把 PAM 近端錯配效應寫成單一錯配即可完全廢除切割，與原文對連續配對需求及遠端錯配容忍度之結果不符。
- **來源**：[原文](https://doi.org/10.1126/science.1225829)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 pp. 818–819 及 Figure 3D–E 查核修訂 Card 4：改述種子區特異性窗口，精確說明高效切割係要求緊鄰 PAM 之原間隔序列 3' 端維持「至少 13 個連續鹼基對完全互補」，而遠端（5' 端）可容忍多達 6 個連續錯配，更正原先「單一錯配即可完全廢除切割」之錯誤陳述。證據表見 wiki/evidence/2012-crispr-cas9.md。

### EK-014 | fixed | papers/2012-crispr-cas9.md | Card 3 | 原文未支持
- **問題**：R-loop 自由能、切割速率常數與 K_d 等符號模型未見於原文，卻呈現為本文模型；可保留為教學推導，但須標明推導者、假設與來源。
- **來源**：[封存原文](../raw/2012-crispr-cas9.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 3 公式小節：在 R-loop 自由能與雙結構域反應動力學公式前加註理論模型說明，明確標註此二公式為後續生物物理學文獻（如 Sternberg et al., 2014 等）對 Cas9 靶向機制的標準教學量化模型，非 2012 原文之直接方程。證據表見 wiki/evidence/2012-crispr-cas9.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核 Card 3 公式與 wiki-content-audit 現行公式規則：頁面雖標示後續教學模型，仍以區塊公式呈現非 2012 原文方程，且證據表未逐式列明直接來源位置；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。移除無直接來源的自由能、速率與親和力模型，改以原文對辨識、可能 R-loop 與兩催化結構域分工的定性結果說明；同步修訂證據表，verification 改為 partial。

### EK-015 | fixed | papers/2012-crispr-cas9.md | Card 5 | 歸因／版本錯置
- **問題**：把 dCas9、nCas9 及鹼基／先導編輯工具家族寫成本篇建立；2012 原文報告的是雙 RNA 引導與嵌合單 RNA 切割，dCas9 調控平台見 2013 年後續研究。
- **來源**：[封存原文](../raw/2012-crispr-cas9.pdf)、[Qi et al. 2013](https://doi.org/10.1016/j.cell.2013.02.022)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 衍生工具生態系段落：精確說明 2012 本文係透過 D10A 與 H840A 突變完成催化結構域生化驗證，而將 dCas9 作為通用轉錄調控平台（CRISPRi，引 Qi et al., 2013 Cell）以及融合衍生之鹼基/先導編輯（David Liu 團隊 2016, 2019）明確標註為後續工具生態之重大延伸。證據表見 wiki/evidence/2012-crispr-cas9.md。

## 2013 IceCube 高能微中子

### EK-016 | fixed | papers/2013-icecube-neutrino.md | Card 4 | 原文未支持
- **問題**：「高能端分析 4.3σ、p≈1.5×10⁻⁵」在原文找不到。原文報告為 26 個新事件 3.3σ、預先指定分析合併 28 個事件 4.1σ、事後計算全 28 事件 4.8σ，較高 charm 背景下分別降為 3.6σ 與 4.5σ。
- **來源**：[原文](https://arxiv.org/abs/1311.5238)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Science 2013 p. 4 查核修訂 Card 4：刪除非原文之「4.3σ、p≈1.5×10⁻⁵」陳述，更正為原文統計分析架構：26 個新事件顯著性為 3.3σ；預先指定 Fisher 合併 28 個事件為 4.1σ（90% CL 魅夸克上限下為 3.6σ）；事後全體 28 個事件計算為 4.8σ（90% CL 魅夸克上限下為 4.5σ）。證據表見 wiki/evidence/2013-icecube-neutrino.md。

### EK-017 | fixed | papers/2013-icecube-neutrino.md | Card 3 | 原文不符
- **問題**：99.999% 在原文是 6000 p.e. 門檻以上大氣緲子背景之拒斥率，頁面擴寫為同時濾除大氣微中子；原文仍估計約 6.1 個大氣微中子事件與 6.0 ± 3.4 個穿透緲子事件。
- **來源**：[封存原文](../raw/2013-icecube-neutrino.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Science 2013 pp. 4, 7–8 查核修訂 Card 3：更正 99.999% 為 6000 p.e. 以上「穿透大氣緲子」之拒斥率，南半球大氣微中子伴隨緲子濾除率為約 70%，並補列兩年預期殘留背景之精確數據（6.0 ± 3.4 個緲子與 6.1 個大氣微中子），修正過度概括。證據表見 wiki/evidence/2013-icecube-neutrino.md。

## 2017 Transformer

### EK-018 | fixed | papers/2017-attention-is-all-you-need.md | Card 4 | 歸因／版本錯置
- **問題**：41.8 BLEU 符合 arXiv 版，NeurIPS 定稿 PDF 報 41.0（官方摘要頁 41.1）；頁面同時標 NeurIPS venue 與 arXiv 連結，須註明採用版本。
- **來源**：[NeurIPS 定稿 PDF](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 NeurIPS 30 定稿 PDF 查核修訂 Card 4：明確標註英譯法（EN-FR）在 NeurIPS 定稿正文第 8 頁報告為 41.0 BLEU，在 Table 2 與 arXiv 版中標註為 41.8 BLEU（官方摘要頁載為 41.1），完整呈現版本數值差異。證據表見 wiki/evidence/2017-attention-is-all-you-need.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核 NeurIPS 定稿 PDF Table 2 與 arXiv v7：定稿正文及 Table 2 均為 41.0，41.8 見於 arXiv v7；目前頁面、卡片與證據表仍把定稿 Table 2 標為 41.8；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看 NeurIPS 定稿與 arXiv v7 的 Table 2 頁面影像，論文頁與卡片以定稿 41.0 為主，分別註明 arXiv v7 的摘要／表格 41.8 與正文 41.0，以及會議網站摘要 41.1；同步更正證據表，並指出定稿表中集成模型 41.29 高於 41.0。頁面 verification 改為 partial。

### EK-019 | fixed | papers/2017-attention-is-all-you-need.md | Card 5 | 原文不符
- **問題**：稱原始 Transformer 訓練「完美契合 Tensor Cores」；原文使用 8 張 P100（Pascal），首代 Tensor Cores 出現於 Volta。
- **來源**：[NeurIPS 原文](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need.pdf)、[NVIDIA Volta 白皮書](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-product-literature/volta-architecture-whitepaper.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 硬體共振段落：精確指出 2017 原文係在 8 張 NVIDIA P100（Pascal 架構，無 Tensor Cores）上訓練，其高度並行之 GEMM 矩陣運算特性隨後與 Volta 架構（首代 Tensor Cores）及現代萬卡叢集產生共振，更正時代錯置。證據表見 wiki/evidence/2017-attention-is-all-you-need.md。

### EK-020 | fixed | papers/2017-attention-is-all-you-need.md | Card 6 | 過度表述
- **問題**：「拿掉歸納偏置」過於絕對；原模型仍使用位置編碼與遮罩等結構先驗。
- **來源**：同 EK-019
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 6 減法哲學段落：將原先「拿掉歸納偏置」改述為精確的「大幅放寬結構性歸納偏置」，明確交代模型仍保留位置編碼與因果遮罩等基礎先驗，修正絕對化表述。證據表見 wiki/evidence/2017-attention-is-all-you-need.md。

## 2021 AlphaFold2

### EK-021 | fixed | papers/2021-alphafold2.md | Card 4 | 歸因／版本錯置
- **問題**：r=0.73 出自 Tunyasuvunakool et al. 人類蛋白質組伴篇；Jumper et al. 主論文 Figure 2c 在另一組測試鏈報 r=0.76。須標明出處。
- **來源**：[主論文](https://www.nature.com/articles/s41586-021-03819-2)、[伴篇](https://www.nature.com/articles/s41586-021-03828-1)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文主論文 Figure 2c 查核修訂 Card 4：明確標註主論文在近期 PDB 測試集（$n=10,795$）報告皮爾森相關係數為 $r = 0.76$（線性式 $\text{lDDT-C}_\alpha = 0.997 \times \text{pLDDT} - 1.17$），而在人類蛋白質組伴篇（Tunyasuvunakool et al. 2021）中報告為 $r = 0.73$，標明不同測試集出處。證據表見 wiki/evidence/2021-alphafold2.md。

### EK-022 | fixed | papers/2021-alphafold2.md | Card 3 | 過度表述
- **問題**：原文說三角更新受三角不等式「啟發」，頁面寫成「強制滿足」歐氏三角幾何；並把 IPA 注意力值之不變性與其後座標更新之等變性混稱。
- **來源**：[封存原文](../raw/2021-alphafold2.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Nature 2021 pp. 584–587 查核修訂 Card 3：更正三角更新表述為受三角不等式「啟發」（作為神經先驗引導逼近物理幾何，非剛性滿足）；精確區分 IPA 模組之數學性質：IPA 局部點距離計算之標量值具全局 $\mathrm{SE}(3)$ 不變性（Invariance），而結構模組利用該激活值對殘基剛體座標系實施等變更新（Equivariant Update），修正混稱。證據表見 wiki/evidence/2021-alphafold2.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新掃描論文頁全篇：Card 3 已修正，但 Frontmatter hook 與 Card 5 仍稱三角不等式直接／精確編碼為網路架構；原文僅稱受其啟發，並分別描述 IPA 不變性與座標更新等變性；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Nature 主文及補充資料改寫 hook、Card 3、5、6，將三角不等式寫為啟發、區分 IPA 不變性與座標更新等變性；標題及 Card 1 不再將評測結果擴稱解決所有摺疊問題。相關公式另依原始補充資料更正並登記 EK-194。

### EK-023 | fixed | papers/2021-alphafold2.md | Card 5 | 歸因／版本錯置
- **問題**：把核孔複合體結構寫成直接套用 AF2 預測；後續研究是以 AlphaFold 模型結合 cryo-EM 等實驗資料做整合建模。
- **來源**：[封存主論文](../raw/2021-alphafold2.pdf)、[NPC 整合建模研究](https://pubmed.ncbi.nlm.nih.gov/35679401/)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 典範轉移段落：明確將核孔複合體（NPC）等超大複合體結構解析標記為 AlphaFold 預測模型與低解析度冷凍電鏡（cryo-EM/ET）數據結合之「整合建模（Integrative Modeling）」應用，非單純直接預測之結果。證據表見 wiki/evidence/2021-alphafold2.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新核對 Card 5 與 Mosalaganti et al. 2022 Science（DOI: 10.1126/science.abm9326）：整合建模的歸因已修正，但該來源解析的是 NPC 細胞質環，不能支持頁面所稱完整逾千亞基 NPC 巨型結構已被攻克；建議重開為 open。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。更正前一行書目：DOI 10.1126/science.abm9326 是 Fontana 等的細胞質環研究；Mosalaganti 等為另一篇研究，DOI 10.1126/science.abm9506，報告人類核孔骨架超過九成的整合模型。核對頁面所指範圍時須分別查兩篇，不可混用作者與 DOI，也不可將細胞質環研究視為完整核孔的證據。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。分別列出 Fontana 等的非洲爪蟾細胞質環與 Mosalaganti 等覆蓋超過九成人類核孔骨架的整合模型，各附 DOI 並同步證據表；未將兩者歸為單一完整核孔預測。此頁 verification 改為 partial。

## 2023 DrugCLIP

### EK-024 | fixed | papers/2023-drugclip.md | Card 4 | 原文不符
- **問題**：DUD-E 與 LIT-PCBA 之 EF、AUROC、BEDROC 數值與指標歸屬與原文表格不一致；10.66 被錯標為 LIT-PCBA BEDROC，原文該值屬 DUD-E EF@5%；HomoAug 之 LIT-PCBA 4.21 → 5.51 消融敘述未見於原文表格。
- **來源**：[原文](https://www.proceedings.com/content/075/075280-1932open.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 NeurIPS 2023 原文 Table 1、Table 3、Table 5 修正：DUD-E 零樣本精確更正為 EF@1%=31.89（EF@0.5%=38.07、EF@5%=10.66、AUROC=80.93%、BEDROC=50.52%）；LIT-PCBA 精確更正為 EF@1%=5.51（EF@0.5%=8.56、EF@5%=2.27、BEDROC=6.23%、AUROC=57.17%），糾正將 10.66% 誤植為 LIT-PCBA BEDROC 之錯誤；消融段落改述 Table 5（DUD-E 上引入 HomoAug 使 BEDROC 由 45.81% 升至 50.52%、EF@1% 由 29.12 升至 31.89），刪除非原文之 LIT-PCBA 4.21 到 5.51 陳述。證據表見 wiki/evidence/2023-drugclip.md。

### EK-025 | fixed | papers/2023-drugclip.md | Card 3 | 原文不符
- **問題**：寫「十億個分子全庫檢索在毫秒內完成」；原文 Section 4.3 報告 6 billion Enamine 分子檢索耗時少於 10,000 秒（約 2.78 小時；原文括號之「30 小時」與其秒數不符，見 22:44 勘誤）。
- **來源**：[封存原文](../raw/2023-drugclip.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:00] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 4.3（p. 8）查核修訂 Card 3 與 Card 4：更正檢索速度表述，明確指出 60 億 Enamine 分子庫在預編碼後單靶點檢索耗時小於 10,000 秒（約 2.78 小時；原文括號誤註為約 30 小時），相較商業對接（100 億分子約需 3,000 年）具顯著效率優勢，刪除「毫秒內完成十億級全庫檢索」之誇大陳述。證據表見 wiki/evidence/2023-drugclip.md。

### EK-026 | fixed | papers/2023-drugclip.md | Card 3 | 原文未支持
- **問題**：test-time 取 K 個構型最大相似度未見於原文方法（RDKit 構型主要用於訓練期噪聲輸入與消融）；HomoAug 實際流程為同源序列搜尋、AlphaFold DB、TM-align 與相似度篩選，頁面所寫 Pfam 未獲支持。
- **來源**：同 EK-025
- **發現於**：wiki/log.md [2026-11-08 22:00] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 3.4 與 Appendix B.1 查核修訂 Card 3：更正 HomoAug 資料增強技術流程為 Jackhmmer 搜尋 AlphaFold DB 聚類庫、TMalign 結構對齊（TM-score $\ge 0.4$、結合口袋對齊率 $\ge 40\%$）與 $6\,\text{Å}$ 口袋原子擷取，刪除非原文之 Pfam；刪除非原文之推論期多構型最大池化公式，改述原文 Proposition 1 數學原理（RDKit 構型用於訓練期帶噪聲輸入以消除訓練—測試不一致性，推論期由雙塔向量點積或餘弦直接檢索）。證據表見 wiki/evidence/2023-drugclip.md。

## 2023 JWST 大質量星系

### EK-027 | fixed | papers/2023-jwst-massive-galaxies.md | Card 4 | 原文不符
- **問題**：將 ε≈0.57 指派至 z≈7.5；原文此值對應 z≈9.1 之 1σ 邊際一致性，z≈7.5 中心估計約 0.84。「觀測密度為理論上限 2–5 倍」亦超出原文結論。
- **來源**：[原文](https://www.nature.com/articles/s41550-023-01937-7.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 3 與 Figure 2 查核修訂 Card 4：明確標註 Labbé et al. 中心估計值分別對應 $\epsilon(z \approx 7.5) = 0.84$ 與 $\epsilon(z \approx 9) = 0.99$；在考慮星系質量、泊松噪聲與宇宙樣本方差之 $1\sigma$ 不確定度後，在 $z \approx 9.1$ 處與基準 $\Lambda\text{CDM}$ 邊際一致要求 $\epsilon(z \approx 9) \ge 0.57$，糾正原先錯配至 $z \approx 7.5$ 之問題；刪除超出原文結論之「比理論上限高出 2 至 5 倍」陳述。證據表見 wiki/evidence/2023-jwst-massive-galaxies.md。

### EK-028 | fixed | papers/2023-jwst-massive-galaxies.md | Card 3 | 歸因／版本錯置
- **問題**：主計算採 Sheth–Tormen 暈質量函數，後文卻附 Press–Schechter erfc 解析式；須明示 PS 為補充近似，非 Boylan-Kolchin 論文所用之 HMF。
- **來源**：[封存原文](../raw/2023-jwst-massive-galaxies.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:00] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Section 2 查核修訂 Card 3：明確標註 Boylan-Kolchin 論文之累積暗物質暈數量與質量密度計算係採用 Sheth & Tormen (1999) 橢球坍縮質量函數進行數值積分，並註明互補誤差函數 $\operatorname{erfc}$ 解析解僅為經典 Press-Schechter (1974) 球對稱坍縮近似（用於解釋高斯尾部指數衰減先驗），非論文主計算來源。證據表見 wiki/evidence/2023-jwst-massive-galaxies.md。

## 2024 AlphaFold 3

### EK-029 | fixed | papers/2024-alphafold3.md | Card 4 | 歸因／版本錯置
- **問題**：將介面 LDDT 標成成功率；複雜多醣鏈 72.1% 之歸屬未獲主文支持。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 Nature 2024 原文 Extended Data Table 1 與正文（p. 497）核實修訂 Card 4：更正蛋白質—核酸複合體預測指標為平均介面 LDDT（iLDDT，雙股 DNA 為 64.8、RNA 為 39.4），糾正將分數誤標為百分比成功率之錯誤；修正糖基化與修飾殘基數值歸屬：72.1% 屬高質量單殘基糖基化成功率（多殘基多醣鏈成功率為 42.4%），修飾殘基總體成功率為 59.9%（蛋白質修飾殘基 51.0%、DNA 修飾 68.6%、RNA 修飾 40.9%），共價配體為 78.5%。證據表見 wiki/evidence/2024-alphafold3.md。

### EK-030 | fixed | papers/2024-alphafold3.md | Card 1 | 過度表述
- **問題**：「全面擊敗所有領域專用工具」強於原文「優於許多既有專用工具」；原文按任務與基準分別比較。
- **來源**：[封存原文](../raw/2024-alphafold3.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文摘要與第 493 頁查核修訂 Card 1：將「全面擊敗所有領域專用工具」改為符合原文之「在單一統一深度學習架構中跨越了幾乎所有生物分子交互作用類別，預測準確度顯著超越眾多既有領域專用工具」，交代個別任務與專用工具之具體比較（如蛋白—配體超越對接軟體、蛋白—核酸超越專用預測器，但 CASP15 RNA 仍有人類專家介入模型略高）。證據表見 wiki/evidence/2024-alphafold3.md。

## 2024 可容錯量子處理器

### EK-032 | fixed | papers/2024-fault-tolerant-quantum.md | Card 4 | 原文不符
- **問題**：把「40 個 color-code qubits」混寫成「40 個橫向邏輯 CNOT 閘」，混淆量子位元數與閘數；另須與以 3D [[8,3,2]] code blocks 執行之 48 邏輯量子位元取樣電路分開敘述。
- **來源**：[原文](https://arxiv.org/abs/2312.03982)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Abstract、Section 4 與 Fig. 4、Fig. 5 核實修訂 Card 4：明確區分兩大獨立實驗——(1) 40 個 $d=3$ 色碼邏輯量子位元在 280 個物理原子上的分區維持與操作（使用 20 個橫向 CNOT 實施標記容錯初始化，閒置退相干率約 1%），糾正混淆位元數與閘數之錯誤；(2) 48 個邏輯量子位元之三維 $[[8,3,2]]$ 碼取樣電路（動用 128 個物理原子，在 4D 超立方體連接拓撲下執行包含 228 個邏輯雙量子位元閘與 48 個邏輯 CCZ 閘之深層亂序電路，全錯誤偵測下 XEB 達約 0.1）。證據表見 wiki/evidence/2024-fault-tolerant-quantum.md。

### EK-033 | fixed | papers/2024-fault-tolerant-quantum.md | Card 1 | 原文不符
- **問題**：將中性 87Rb 原子寫成「帶電」搬運；原文為 neutral-atom 陣列。
- **來源**：[封存原文](../raw/2024-fault-tolerant-quantum.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Fig. 1 與 Methods 查核修訂 Card 1：糾正將中性原子光學鑷子搬運誤植為「帶電」之嚴重錯誤，精確表述為「以光學鑷子（2D AOD）相干搬運中性原子（Neutral Atoms）」。證據表見 wiki/evidence/2024-fault-tolerant-quantum.md。

### EK-034 | fixed | papers/2024-fault-tolerant-quantum.md | Card 5 | 原文不符
- **問題**：把 qLDPC 說成已由本實驗實作；原文只把 qLDPC 列為未來降低開銷之方向。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Outlook（p. 8）查核修訂 Card 5：更正 qLDPC 相關表述，明確本實驗實作之編碼為表面碼、色碼與三維 $[[8,3,2]]$ 碼，qLDPC 碼僅為原文展望中進一步降低硬體開銷的關鍵未來方向，刪除將 qLDPC 寫成已由本實驗實作之陳述。證據表見 wiki/evidence/2024-fault-tolerant-quantum.md。

## 2024 Sora

### EK-035 | fixed | papers/2024-sora-world-simulator.md | Card 3 | 原文未支持
- **問題**：把 VAE 具體架構、3D RoPE、adaLN-Zero 與 epsilon-prediction 當作 Sora 已知實作。OpenAI 報告未提供實作細節，並說模型訓練預測原始乾淨 patch，與 epsilon-MSE 公式不符；二手反向推測須明標推測。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 OpenAI 技術報告與 DiT、綜述原文核實修訂 Card 3：明確劃分 OpenAI 官方公開機制（時空壓縮網路、時空圖塊 Token 化、預測原始乾淨圖塊）與學界推測（adaLN-Zero 源自 Peebles & Xie 2023，3D-RoPE 與 3D-VAE 細節源自 Liu et al. 2024）；公式依官方報告明示更新為預測乾淨圖塊目標（$\hat{U}_0$），並對比經典 DiT 之 $\epsilon$ 預測目標。證據表見 wiki/evidence/2024-sora-world-simulator.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。OpenAI 報告未公開模型實作細節；Card 3 仍把 adaLN-Zero 與影片重標註並列為引導生成的機制，論文頁仍列圖塊映射、乾淨圖塊損失與 adaLN 區塊公式，卡片 Card 3 另列圖塊數量式，報告未提供這些公式。EK-099 原先所指的舊冪律式與運算量式已刪；其複核提出的現存公式缺口在此一併追蹤，修正時須同時核對論文頁與卡片。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 OpenAI 技術報告及 Liu 綜述圖 4 分開公開流程與逆向推測，移除未公開的圖塊數量、嵌入、損失與 adaLN 區塊公式；論文頁改以文字說明，卡片採無公式模式，證據表同步更正。DiT 的 adaLN-Zero 僅歸給 Peebles 與 Xie 的研究。

### EK-036 | fixed | papers/2024-sora-world-simulator.md | Card 1 | 過度表述
- **問題**：將遮擋後維持物體存在寫成一般穩定能力，報告措辭為「常能但並非總是」並明列物理模擬限制；即時互動與狀態記憶之說法亦超出原文示例。Card 5、6 之世界模型與隱式幾何重建描述應保留為有限能力觀察或詮釋。
- **來源**：同 EK-035
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 OpenAI 官方報告修訂 Card 1、Card 4 與 Card 5：Card 1 將遮擋存在性精確限定為「常能（但並非總是）維持短暫被遮擋物體時空存在感」，並補列報告明示之物理交互局限；Card 4 刪除 Minecraft 具備即時互動與完備狀態記憶之表述，改為提示詞零樣本渲染動態畫面，並客觀補列玻璃碎裂與吃食物咬痕等物理失敗模式；Card 5 將世界模型描述限定為初步探索與有限能力湧現，強調高維視覺統計擬合與顯式因果物理引擎之本質差異。證據表見 wiki/evidence/2024-sora-world-simulator.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。Card 1 的限定語已補，但 Card 5 仍將隱藏層的三維幾何關聯寫成既定事實，Card 6 稱模型被迫反推世界幾何與物理規則；報告展示的是有限生成能力與失敗案例，未直接驗證這些內部機制。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。Card 5、6 改述報告展示的樣本及失敗案例，移除對隱藏層幾何與物理推理的未證實斷言；封面導言、hook 與證據表同步收斂。僅修正登記問題，論文頁 verification 改為 partial。

## 2025 DeepSeek-R1

### EK-037 | fixed | papers/2025-deepseek-r1.md | Card 4 | 原文不符
- **問題**：將 cons@64 標成 cons@16，並須註明所用論文版本。
- **來源**：[論文](https://arxiv.org/abs/2501.12948)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 arXiv:2501.12948 預印本 Table 1 與 Nature 2025 正式發表版本核實 Card 4：更正 AIME 2024 之 86.7% 數值為 64 次採樣多數決（cons@64），糾正誤植為「cons@16」之錯誤，並標明出自預印本 Table 1。證據表見 wiki/evidence/2025-deepseek-r1.md。

### EK-038 | fixed | papers/2025-deepseek-r1.md | Card 1 | 原文不符
- **問題**：把「完全不使用 SFT」同時套到 R1-Zero 與 R1；原文只有 R1-Zero 為純 RL，R1 使用冷啟動資料、RL、拒絕採樣與後續 SFT。
- **來源**：[封存原文](../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照原文 §2.1 與 §2.3 核實修訂 Card 1：明確劃分僅 DeepSeek-R1-Zero 為完全不經 SFT 直接從 Base 模型以純 RL 訓練；正式版 DeepSeek-R1 為解決可讀性差與中英夾雜問題，採用包含冷啟動（數千筆長 CoT）、推理 RL、拒絕採樣及 80 萬筆混合 SFT、全場景二次 RL 的多階段管線，糾正將 Zero SFT 概括至 R1 之錯誤。證據表見 wiki/evidence/2025-deepseek-r1.md。

## 2025 神經元粒線體與癌症

### EK-039 | fixed | papers/2025-nerve-mito-cancer.md | Card 4 | 原文不符
- **問題**：測序方法、實驗模型與轉移比例被混併；原文為分選癌細胞後之 Nanopore 分析，不是單細胞長讀長測序。
- **來源**：[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328229/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 Nature 2025 原文 §Mitochondrial genome tracking（p. 254）與 Fig. 2h–j 核實 Card 4：更正實驗流程為共培養後經 FACS 螢光活化分選純化人類癌細胞，隨後進行體外 Nanopore 長讀長定序與物種特異性 qPCR，糾正誤寫為「單細胞長讀長定序」之錯誤。證據表見 wiki/evidence/2025-nerve-mito-cancer.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。Nature 原文 Fig. 2f–g 與方法中的 Nanopore 分析為腫瘤組織分選出的 4T1 細胞及變異點附近 420 bp 片段；目前 Card 4 卻合併人類 MDA-MB-231 共培養並稱定序檢出完整小鼠粒線體基因組及其轉錄、複製，須拆開實驗與證據。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。區分人類癌細胞體外共培養、分選小鼠腫瘤 4T1 細胞的 420 bp Nanopore 分析，以及混合球體與宿主神經追蹤的不同轉移模型；刪除完整基因組及其轉錄、複製的無據推論，並逐項更新證據表。

### EK-040 | fixed | papers/2025-nerve-mito-cancer.md | Card 3 | 原文未支持
- **問題**：粒線體轉移—OCR 線性增益、轉移灶富集等符號模型未見於原文，卻呈現為本文模型；須標為教學推導並註明假設。
- **來源**：[封存原文](../raw/2025-nerve-mito-cancer.pdf)
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

## 2025 滿語上下文機器翻譯

### EK-031 | fixed | papers/2025-manchu-in-context-mt-pei.md | Card 1 | 原文不符
- **問題**：第 27 行語族寫作「阿爾泰阿爾泰通古斯語族」，字詞重複，且「阿爾泰語系」歸類有爭議，宜依原文寫作通古斯語族（Tungusic）。
- **來源**：[封存原文](../raw/my-focus/報告論文題材/2025.acl-long.429.pdf) §3（p. 8769）；處理行已回原文核對
- **發現於**：wiki/log.md [2026-11-08 22:06] audit（Claude Code by Anthropic）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。原文 §3（p. 8769）稱滿語為 critically endangered Tungusic language；Card 1 改為「通古斯語」，刪除重複且有爭議之「阿爾泰阿爾泰」。

## 概念頁

### EK-042 | fixed | concepts/neural-circuits.md | 2017 支柱 | 歸因／版本錯置
- **問題**：把 Transformer 注意力與 Hopfield 網路等價列在 2017 支柱；等價結果來自連續／現代 Hopfield 之後續工作（Ramsauer et al. 2021），不應歸給 1982 原始網路或 2017 Transformer 原文。
- **來源**：[Ramsauer et al.](https://arxiv.org/abs/2008.02217)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂神經迴路因果解耦概念頁：明確將縮放點積注意力與現代連續型 Hopfield 網路之數學等價性歸因於 Ramsauer et al. (2020/2021) 之理論推導，糾正原先將後續等價結果混入 2017 Vaswani et al. 原始論文之歸因錯置。建立證據表 wiki/evidence/neural-circuits.md。

### EK-043 | fixed | concepts/brain-machine-interface.md | 核心支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 能量吸引子寫成當代 BCI 神經流形解碼之數學基礎；神經流形屬獨立研究脈絡，現有來源不足以建立直接傳承。
- **來源**：[Hopfield 封存原文](../raw/1982-hopfield-network.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂腦機介面與神經編碼概念頁：釐清 Hopfield (1982) 為群體狀態空間吸引子提供物理啟發，而現代 BCI 之神經流形解碼源自運動皮質實證降維建模脈絡（如 Churchland et al. 2012），兩者在群體狀態空間幾何上深層呼應而非直接數學繼承。建立證據表 wiki/evidence/brain-machine-interface.md。

### EK-044 | fixed | concepts/brain-machine-interface.md | 跨學科延伸 | 過度表述
- **問題**：將雙光子讀取與全息光遺傳寫入概括為「萬級神經元的無損閉環互動」；原始研究為光刺激選定個別細胞、同時記錄數千神經元，未驗證萬級同時控制、無損或臨床可用。
- **來源**：[原始研究](https://www.nature.com/articles/s41593-026-02350-9)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂腦機介面概念頁全光學 BCI 段落：將實驗規模客觀限定為在動物模型中記錄數千神經元並全息光刺激數十至數百個特定細胞之單細胞級閉環調控，刪除「萬級神經元無損閉環互動」之過度表述，交代光散射深度與光熱耐受等客觀物理瓶頸。建立證據表 wiki/evidence/brain-machine-interface.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。萬級與無損臨床的舊表述已收斂；但目前以單句將數千細胞記錄、數十至數百細胞刺激和單細胞級閉環調控合併，證據表所列研究尚未逐項支持同一實驗的全部條件。閉環研究存在，仍須為這項具體規模和回饋主張補直接來源或拆開。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。改以 Zhang 等（2018）小鼠皮質全光學閉環研究為直接例證，區分單細胞訊號觸發與目標細胞群，不再把不同實驗規模合成同一結果；同步改正概念頁及證據表。

### EK-045 | fixed | concepts/generative-world-models.md | 支柱與時間線 | 歸因／版本錯置
- **問題**：將 Hopfield/Hinton 能量模型合標為 1982（Boltzmann machine 學習論文為 Ackley、Hinton、Sejnowski 1985），並把 Hopfield、Boltzmann、score matching、擴散模型與 Transformer 寫成直接奠基鏈；須分開作者年代並改標為概念類比或補中間研究。
- **來源**：[Hopfield 封存原文](../raw/1982-hopfield-network.pdf)、[Ackley et al. 1985](https://doi.org/10.1207/s15516709cog0901_7)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂生成式世界模型概念頁：分開標註 Hopfield (1982) 李亞普諾夫能量函數與 Ackley、Hinton、Sejnowski (1985) 波茲曼機學習演算法之年代；將擴散模型、分數匹配與 Transformer 注意力之聯繫明確界定為統計物理能量景觀與連續狀態空間之深層理論類比與現代聯想記憶等價性，刪除直接線性奠基之過度概括。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。Hopfield 與 Boltzmann 年代已拆開；目前支柱仍稱該概念視角啟發分數匹配等方法，現有兩篇來源不足以建立所述歷史因果鏈，應補直接承接證據或明確改為有限的概念類比。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。將 Hopfield（1982）與波茲曼機（1985）分開描述，刪去對分數匹配等方法的未證實歷史因果鏈，限定為概念類比；同步更新證據表。

### EK-046 | fixed | concepts/generative-world-models.md | DeepSeek-R1 段 | 歸因／版本錯置
- **問題**：將「無須人工示範」歸給 DeepSeek-R1（實為 R1-Zero），並把可驗證獎勵從原文之數學與程式任務推廣到任意驗證器與科學探索代理，應標為展望。
- **來源**：[DeepSeek-R1 封存原文](../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂生成式世界模型概念頁 DeepSeek 段落：明確將「無須人工示範」限定於 R1-Zero 純 RL 模型，說明完整版 R1 結合冷啟動、多階段 SFT 與二次 RL，並將可驗證獎勵（RLVR）向任意領域驗證器與自主科學探索代理之推廣標明為重大未來展望。證據表見 wiki/evidence/2025-deepseek-r1.md。

### EK-047 | fixed | concepts/quantum-error-correction.md | 支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 列為表面碼／色碼隨機鍵 Ising 映射之直接來源；映射可追溯至 Dennis et al. 2002，其原文未引用 Hopfield，須分開數學類比與歷史來源。
- **來源**：[Dennis et al. 2002](https://arxiv.org/abs/quant-ph/0110143)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂容錯量子計算與量子糾錯碼概念頁：明確將拓撲表面碼容錯閾值向 2D 隨機鍵伊辛模型（RBIM）Nishimori 線相變之精確數學映射歸因於 Dennis et al. (2002) 之理論工作，將 Hopfield 能量景觀與量子糾錯釐清為統計物理相變理論在神經計算與量子拓撲之平行應用，糾正直接歷史繼承之歸因錯置。建立證據表 wiki/evidence/quantum-error-correction.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。現行句子的文法主詞為伊辛與自旋玻璃理論，不能直接引述成「Hopfield 直接構成映射」；但該段標題為 1982 且只連 Hopfield，未在正文區分表面碼映射研究的歷史來源與概念類比，仍須澄清並定位 Dennis 等研究的適用條件。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。引用 Dennis 等（2002）並分清完美症候群量測的二維無序伊辛模型與量測出錯時的三維規範理論；Hopfield 比較明標為類比，證據表同步改正。

### EK-048 | fixed | concepts/quantum-error-correction.md | 定義段 | 原文不符
- **問題**：稱以橫向閘即可阻止錯誤擴散並實現「任意深度」演算法；依 Eastin–Knill 定理，可偵測錯誤之非平凡量子碼不存在通用橫向邏輯閘集合，須說明其他非橫向或測量型資源。
- **來源**：[Eastin–Knill](https://arxiv.org/abs/0811.4262)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:00] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂容錯量子計算概念頁核心定義：依據 Eastin–Knill 定理，說明任何可偵測錯誤之非平凡量子碼均不存在通用橫向邏輯閘集合；補列魔術態蒸餾（Magic State Distillation）、格子手術或代碼切換以注入非橫向非 Clifford 資源之機制，糾正原先「單憑橫向閘即可實現任意深度演算法」之定理違背。建立證據表 wiki/evidence/quantum-error-correction.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。定義仍可能使讀者理解為只靠橫向閘即可通用容錯計算，缺少非橫向或測量型資源。Eastin–Knill 限制的是通用橫向閘集合；不可把「任意深度」本身等同於通用性。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Eastin–Knill 說明可偵測任一單一子系統錯誤之碼不能有通用橫向閘集合，並說明通用計算需要其他資源；區分通用性與計算深度，證據表同步更新。

### EK-049 | fixed | concepts/quantum-error-correction.md | 跨學科延伸 | 過度表述
- **問題**：稱可重構中性原子陣列已能直接實作 3D／4D 拓撲碼與常數編碼率 qLDPC；所引 2024 實驗將 qLDPC 列為後續方向，未報告已實作。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂容錯量子計算概念頁跨學科延伸：客觀交代中性原子處理器實驗實作之編碼為色碼與三維 [[8,3,2]] 碼，將常數編碼率 qLDPC 碼標明為該實驗展望之核心未來方向，刪除「已在實驗室直接實作 qLDPC」之過度表述。建立證據表 wiki/evidence/quantum-error-correction.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。概念頁仍將可重構原子陣列之 3D／4D 拓撲碼與常數編碼率 qLDPC 寫成已在實驗室直接實作；所引 Bluvstein 等研究將 qLDPC 作為未來改善編碼效率的方向。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Bluvstein 等（2024）區分已用的色碼、三維碼與四維連接圖，將 qLDPC 記為該文的未來方向，刪除未獲支持的硬體節省量；證據表同步更正。

### EK-050 | fixed | concepts/multi-messenger-astrophysics.md | 核心定義 | 原文不符
- **問題**：把深空紅外線列為與重力波、微中子、宇宙射線並列之獨立信使；紅外線屬電磁波譜。定義與後文「三大信使」亦不一致，須統一分類（光、粒子、重力波）。
- **來源**：[NASA 多信使說明](https://svs.gsfc.nasa.gov/gallery/multimessengerastronomy/)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂多信使天體物理與極端宇宙學概念頁：核心定義統一天體物理四大基本物理信使為電磁波（光子）、重力波、微中子與帶電宇宙射線，明確深空紅外線（如 JWST）屬電磁波譜長波波段，糾正將紅外線並列為獨立信使之錯誤；跨學科段落精確說明三大直進無偏轉之「中性信使（光、微中子、重力波）」協同觀測架構。建立證據表 wiki/evidence/multi-messenger-astrophysics.md。

### EK-051 | fixed | concepts/institutions-and-macro-dynamics.md | AJR 支柱 | 過度表述
- **問題**：稱 AJR 以殖民者死亡率「嚴格識別」制度而非地理為收入差距的唯一根因；原文是在排他性假設與控制條件下估計制度效果，不能概括為已排除所有地理作用或證明唯一根因。
- **來源**：[AER 原文摘要](https://www.aeaweb.org/articles?id=10.1257/aer.91.5.1369)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂制度演化與宏觀經濟動態概念頁：明確指出 AJR (2001) 係在排他性限制（Exclusion Restriction）假設下以歷史死亡率作為產權制度的工具變數，實證分離出制度環境之顯著因果貢獻；刪除將其寫成排除一切地理作用之「唯一根本原因」的過度表述，客觀呈現排他性外生性與地理直接影響之學術爭鳴。建立證據表 wiki/evidence/institutions-and-macro-dynamics.md。

### EK-052 | fixed | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文不符
- **問題**：稱 DrugCLIP 可「數秒」篩選百億級分子；原文為 6 billion 分子檢索少於 10,000 秒，GenomeScreenDB 規模約 10,000 個人類蛋白質、5 億化合物，全基因組篩選約 24 小時（8 張 A100）。
- **來源**：[DrugCLIP 封存原文](../raw/2023-drugclip.pdf)、[論文紀錄](https://pubmed.ncbi.nlm.nih.gov/41505557/)、[計算配置](https://www.biorxiv.org/content/10.1101/2024.09.02.610777v3.full)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit、[2026-11-08 23:21] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 AI 驅動之結構生物學與分子設計概念頁：更正 DrugCLIP 單靶點 60 億 Enamine 分子檢索耗時為小於 10,000 秒（約 2.78 小時），刪除「數秒內完成百億級初篩」之誇大陳述，並客觀交代 GPU 叢集一日內完成全基因組尺度篩選之實況。建立證據表 wiki/evidence/ai-for-structural-biology.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。舊的數秒篩百億分子已刪，概念頁的「小於 2.8 小時」是由小於 10,000 秒換算出的保守上界，數學上成立；但未註明預先編碼並存於記憶體的條件、換算依據，也未交代原文同句括註約 30 小時與秒數矛盾。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Gao 等（2023）§4.3 寫明分子預先編碼並存於記憶體的條件，並並列少於 10,000 秒與約 30 小時的原文矛盾；Jia 等（2026）的八張 A100、約 24 小時配對評分另作後續研究，證據表逐項登記。

### EK-053 | fixed | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文未支持
- **問題**：把 AlphaFold 3＋FEP 描述成已實證之全原子誘導契合精排管線；AF3 原文報告的是複合體結構預測基準，應標為待驗證提案並另引直接驗證研究。
- **來源**：[AlphaFold 3 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 AI 驅動之結構生物學與分子設計概念頁：明確將 AlphaFold 3 複合體預測與自由能微擾（FEP）結合標明為計算生物學界正在探索的前沿整合策略，刪除將其寫成已實證成熟精排管線之過度表述。建立證據表 wiki/evidence/ai-for-structural-biology.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。概念頁已將成熟管線降為探索，但其「計算生物學界正在探索」AF3 與 FEP 結合的主張仍只由 AF3 原文及一般 FEP 文獻支撐，缺少直接例證；不得因此推定這類研究不存在，應補合適的一手研究或明確標為提案。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。將 AF3 與 FEP 的串接明標為 Wiki 提案，刪除未以直接來源支持的『研究界正在探索』及成熟精排暗示；證據表同步說明來源範圍。

### EK-054 | fixed | concepts/programmable-cellular-engineering.md | 跨學科延伸 | 過度表述
- **問題**：「已能直接在患者肝臟、視網膜與造血幹細胞中修正致病突變」合併不同遞送方式與證據階段：Casgevy 為體外編輯後回輸；EDIT-101 為小型 1–2 期試驗；肝臟 LNP 鹼基編輯為單一新生兒 N-of-1 個案。另須同步校正自 CRISPR 論文頁重述之 PAM 與衍生技術歸因（見 EK-012、EK-015）。
- **來源**：[FDA 審查文件](https://www.fda.gov/media/175179/download?attachment=)、[視網膜試驗](https://www.nejm.org/doi/10.1056/NEJMoa2309915)、[肝臟 N-of-1](https://www.nejm.org/doi/10.1056/NEJMoa2504747)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit、[2026-11-08 23:21] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂可編程細胞與基因工程概念頁：關鍵突破支柱補列化膿性鏈球菌 Cas9 靶向必備之 5'-NGG-3' PAM 基序約束，並將 dCas9 調控底盤與鹼基/先導編輯標明為後續生態之重大延伸；跨學科延伸嚴格劃分體外改造回輸（Casgevy 造血幹細胞自體回輸）與體內局部/系統性靶向遞送（AAV 視網膜試驗與 LNP 肝臟探索性個案），消除已能在各器官普遍體內修正之過度表述。建立證據表 wiki/evidence/programmable-cellular-engineering.md。

### EK-055 | fixed | concepts/neural-circuits.md | Hopfield 支柱 | 歸因／版本錯置
- **問題**：與 EK-043、EK-045 同源，將 Hopfield 1982 吸引子延伸為後續多個領域之直接歷史基礎；22:44 審查指出此錯誤於多個概念頁重述，修正時須同步。
- **來源**：同 EK-042
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂神經迴路因果解耦概念頁 Hopfield 支柱：明確定界 Hopfield (1982) 為二值自旋玻璃李亞普諾夫能量函數，容量上限約 0.15N，係為海馬體 CA3 自聯想迴路提供經典物理抽象原型；跨學科對偶段落客觀劃分生物化學突觸調控、經典循環吸引子與現代張量注意力機制之異同，消除將離散吸引子泛化為後續多領域直接歷史基礎之過度表述。建立證據表 wiki/evidence/neural-circuits.md。

### EK-056 | fixed | concepts/generative-world-models.md | Sora 段 | 過度表述
- **問題**：重述 Sora 能力界線問題（見 EK-036），把有限能力觀察寫成已證明之通用物理模擬。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂生成式世界模型概念頁 Sora 支柱：將其界定為「時空圖塊與視覺物理世界模擬初步探索」，明確指出純視覺擴散模型基於高維統計關聯擬合，在因果狀態改變與嚴格物理規律（如碰撞、破碎）時頻繁出現穿模與失真，指明其距通用物理世界模型之長期挑戰。

## DOI 無法解析（2026-11-09 crossref_check.py）

### EK-057 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2025.acl-demos.13` 在 Crossref 與 doi.org 均查無此號，DOI 可能有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：本檔建立時以 crossref_check.py 查得（Claude Code by Anthropic）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 ACL Anthology 核對：ACL 2025 System Demonstrations 卷號為單數 `2025.acl-demo`，正確 DOI 為 `10.18653/v1/2025.acl-demo.13`（原誤記為 `acl-demos`），經 Crossref 與 doi.org 解析確認無誤並更新頁面。

### EK-058 | fixed | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.loresmt-1.25` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：本檔建立時以 crossref_check.py 查得（Claude Code by Anthropic）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 ACL Anthology 核對：該篇位於 LoResMT 2026 論文集第 225–230 頁，正確 DOI 為 `10.18653/v1/2026.loresmt-1.22`（原誤記為 `.25`），經 Crossref 與 doi.org 解析確認無誤並更新頁面。

### EK-059 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.dialres-1.13` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：同 EK-057
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 DialRes 2026 原文首頁與 ELRA 核對：本篇由 ELRA 出版，正式註冊之 DOI 為 `10.63317/4scoopyavtvi`，經 Crossref 與 doi.org 解析確認無誤並更新頁面。

### EK-060 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.lrec-1.273` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 LREC 2026 論文集原文首頁核對
- **發現於**：同 EK-057
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 LREC 2026 原文首頁與 ELRA 核對：本篇由 ELRA 出版，正式註冊之 DOI 為 `10.63317/3ut33xim33nt`，經 Crossref 與 doi.org 解析確認無誤並更新頁面。

## 24 篇 my-focus 論文頁與 2 篇概念頁第一手原文全維度查核（2026-11-09 Antigravity / Gemini 4 Argon）

### EK-061 | fixed | papers/2021-seediq-chinese-mt-you.md | Frontmatter doi_url | 原文不符
- **問題**：包含本篇在內之 7 篇海大碩士論文（`2021-seediq-chinese-mt-you.md`、`2023-atayal-truku-morphology-dai.md`、`2023-atayalic-multilingual-mt-liao.md`、`2024-taiwanese-mt-resegmentation-tang.md`、`2025-atayalic-affix-mt-jin.md`、`2025-atayalic-oov-enumeration-yang.md`、`2025-paiwan-bunun-morphology-mt-wu.md`），Frontmatter `doi_url` 均複製貼上同一個已過期之臺灣博碩士論文知識加值系統臨時查詢 session 網址（`https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=y8Gq.y/record?yes=1`），並非永久連結。
- **來源**：`raw/my-focus/學長姐論文/` 下 7 篇碩士論文原檔
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。7 篇碩士論文頁刪除失效之 `doi_url`（該欄非必填；碩士論文無 DOI，國家圖書館系統之永久連結未能取得）；游景勝頁改於文獻出處註明可依題名於臺灣博碩士論文知識加值系統查詢，並補列構詞解析方法之會議版本 ROCLING 2020（https://aclanthology.org/2020.rocling-1.1/）。

### EK-062 | fixed | papers/2021-seediq-chinese-mt-you.md | Card 3 | 原文不符
- **問題**：（1）第 52–54 行將前綴二元語素模型寫為以詞根為條件之 $P(s_{\text{pre}} \mid r) = \prod P(p_i \mid p_{i-1}, r)$；原文 §3.3（p. 27，式 3）之前綴二元機率模型為 $P(\text{pfx}) = P(x_1 \mid \$)\prod_{i=2}^m P(x_i \mid x_{i-1})$，不以詞根為條件。（2）第 60–68 行與架構圖將 $\mathbf{e}_{\text{word}}(w_t)$ 寫作「由自訓練 Skip-gram / FastText 學習之詞根或詞彙語義表示」；原文 §1.3.1（p. 4）、§4.2–4.3（pp. 30–33）與 §5.3（pp. 37–39，表 11）中，「自訓練詞嵌入」指 Seq2Seq Bi-LSTM 模型內以 one-hot 輸入端到端訓練之 Embedding Layer，而 fastText Skip-gram 屬「預訓練詞嵌入」；且表 11（p. 38）證實預訓練 Skip-gram 結合詞綴特徵會使 BLEU 由 22.28 暴跌至 12.09，改用詞根形式亦跌至 12.32 與 4.49，最佳系統（25.10 BLEU）係使用表面詞形搭配端到端自訓練 Embedding Layer 與 52 維布林詞綴組合特徵。
- **來源**：`raw/my-focus/學長姐論文/.md/賽德克語－中文機器翻譯之研究_游景勝.md`（§1.3.1 p. 4、§3.3 p. 27、§4.2–4.3 pp. 30–33、§5.3 pp. 37–39 表 11）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3.3、§4.1–4.3、§5.1–5.4 逐項確認後重寫 Card 3：前綴公式改為原文式 (2)(3)，刪除無來源之 MAP 式；明確區分預訓練（fastText skip-gram）與自訓練（one-hot 加 embedding layer）詞嵌入。另修正同頁未登記之問題：Card 4 改以表 8 為準並註明摘要 99.52%／85.34% 與結論 99.83%／82.01% 互不一致；補列表 11 完整結果；Card 1、Card 5 與 hook 刪除「首創」「最行之有效」等過度表述；Card 6 標明為個人研究詮釋並刪除「100% 精確」。證據表見 wiki/evidence/2021-seediq-chinese-mt-you.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 p. 27，將一元與二元公式左側的 Wiki 自加下標移除，依原文均寫作 $P(\text{pfx})$；同步修正 Card 3 的公式。

### EK-063 | fixed | papers/2023-atayal-truku-morphology-dai.md | Card 3–4 | 原文不符
- **問題**：（1）Card 3（第 45–60 行）寫出正向書寫轉換函數 $\Phi_{\text{ortho}}(\sigma) = w$ 並稱「雙唇音弱化（$p \to b$ 或 $p \to v$）」；原文 §3.4（pp. 27–28）明確指出無法歸納出泰雅語與太魯閣語的書寫形式轉換規則，故不再產生真正的書寫形式，而是對「詞根＋中綴＋後綴」制定三條比對規則（直接比對、保留最後兩母音、刪去全部母音）後，再以一元／二元模型挑選前綴；且 §3.1.2（p. 21）僅列泰雅語 $p \to b$ 及太魯閣語 $k \to b$、$t \to d$，無 $p \to v$。（2）Card 4（第 82 行）僅引結論章稱考慮邊界的二元模型在太魯閣語獲最佳 85.71%，漏未交代 §4.2.2（p. 36，表 21 對照表 22）中太魯閣語測試集上考慮邊界之一元模型（91.84%）實高於二元模型（85.71%），以及泰雅語測試集不考慮邊界之二元模型達 100.00%（表 20）。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/泰雅語與太魯閣語構詞結構之自動解析_戴晟哲.md`（§3.1.2 p. 21、§3.4 pp. 27–28、§4.2.2 p. 36 表 20–22）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3.1–3.5、§4.1–4.2 逐項確認後重寫 Card 3：刪除無來源之 $\Phi_{\text{ortho}}$、音韻交替算子與 argmax 目標式，改述原文四模組、十個詞根還原條件與三條書寫比對規則；結尾規則改列原文之 `p`→`b`、`k`→`b`、`t`→`d`。Card 4 改列表 14–23 完整結果，並註明泰雅語不考慮邊界之二元模型（100.00%）與太魯閣語一元模型（91.84%）測試正確率高於摘要所稱之最佳系統。另修正同頁未登記之 Card 5「僅需替換音變規則矩陣」與 Card 6「深層原形還原準確率可達 90%」等無來源表述。證據表見 wiki/evidence/2023-atayal-truku-morphology-dai.md。

### EK-064 | fixed | papers/2023-atayalic-multilingual-mt-liao.md | Card 2–4 | 原文不符
- **問題**：（1）Card 2（第 36 行）稱「泰雅語的 m-qaniq（吃）、賽德克語的 m-ekan 與太魯閣語的 m-ekan 在傳統詞級切分下被視為三個完全無關的獨立詞彙 ID」；泰雅語「吃」之主事焦點形為 `maniq`（詞根 `qaniq`），且賽德克語與太魯閣語同形詞 `mekan` 合併時字串完全相同。（2）Card 3（第 59–65 行）稱句首僅加目標語標籤 `<2zh>`、`<2tay>`、`<2trv>`、`<2sdq>`；原文 §4.1（p. 16）與 §4.3.2（p. 21）定義之標籤格式為同時編碼來源語與目標語之 `<X2Y>`（以單字母 `A`、`S`、`T`、`C`、`M`、`I` 表示，如 `<S2C>`、`<M2C>`）。（3）Card 1–3 僅描述泛泰雅三語聯合訓練（`|V|=10,000`，對應表 15 之 18.97／17.61／19.92 BLEU），完全漏述 §4.3 與 §5.4 之馬來語／印尼語遷移式學習（`|V|=15,000` 或 `20,000`），致與 Card 4 所列最佳分數（表 21–22 之 20.81／19.38／20.84 與 21.98／21.97／26.69）脫節。（4）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/泛泰雅語群與中文之多語言機器翻譯研究_廖恒慶.md`（§4.1 p. 16、§4.3 p. 21、§5.2 p. 27 表 15、§5.4 pp. 31–32 表 21–22）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §2.1、§4.1–4.3、§5.2–5.5 逐項確認後重寫 Card 1–4：刪除原文未出現之 `m-qaniq`／`m-ekan` 例子，改用原文表 2 之三語例句；語言別標籤改為原文之 `<X2Y>`（如 `<S2C>`）；補述馬來語、印尼語遷移式學習（BPE 15,000／20,000），使 Card 4 最佳分數與方法對應，並標明各最佳值之父語言與單一或多語言系統。另修正同頁未登記之問題：刪除無來源之 BPE 與損失函數公式及「首次」「一加一加一大於三」「通用工程標準」等表述；補述原文 §5.5.2 外部測試因叢書例句被辭典例句覆蓋而偏高、作者以交叉驗證為準。證據表見 wiki/evidence/2023-atayalic-multilingual-mt-liao.md。

### EK-065 | fixed | papers/2024-taiwanese-mt-resegmentation-tang.md | Card 3 | 原文不符
- **問題**：（1）第 43–56 行與架構圖稱使用 `IBM Model`／`fast_align` 統計詞對齊、點互資訊 $\operatorname{PMI}(w_i, t_j)$ 與 BERT 語言模型流暢度先驗進行全局最佳化；原文 §3.3（pp. 26–36）完全未使用統計詞對齊、PMI 或 BERT 流暢度打分，而是以最大二分匹配（Maximum Bipartite Matching，依同字 1.0、台華辭典翻譯 0.8、同義詞詞林 0.6 與最小子詞分數設定權重）執行四階段規則重斷詞（連續未對齊詞連接、部分對齊切分與同義詞重斷詞）。（2）第 59–62 行稱 BERT 台語斷詞器採用四分類 `B-I-E-S` 標籤；原文 §3.2（pp. 24–25，圖 14）明言「斷詞標記工作採用 BI 標籤模式」，僅有 `B` 與 `I` 二類標籤。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061），且 `concepts` 誤掛入 `formosan-computational-linguistics`（台語屬漢藏語系閩南語，非臺灣南島語）。
- **來源**：`raw/my-focus/學長姐論文/.md/利用重斷詞改善台語機器翻譯系統_湯景閔.md`（§3.2 pp. 24–25 圖 14、§3.3 pp. 26–36）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3.1–3.3、§4.1、§4.3 逐項確認後重寫 Card 3：刪除無來源之 IBM Model／fast_align、PMI 與 BERT 流暢度目標式，改述原文之最大二分匹配（1／0.8／0.6 與子詞最小分）與四步驟重斷詞；BERT 斷詞改為原文之 BI 兩類標籤。`concepts` 移除 `formosan-computational-linguistics`，並同步自該概念頁 `papers` 移除本頁。另修正同頁未登記之問題：Card 4 註明摘要「+7.56」為不同評估欄位之差值（同欄為 +9.19 或 +1.36），並補列字級 BLEU 與作者「不太能直接相比較」之說明；刪除 Card 1「首創」與 Card 5 無來源之概括。證據表見 wiki/evidence/2024-taiwanese-mt-resegmentation-tang.md。

### EK-066 | fixed | papers/2025-atayalic-affix-mt-jin.md | Card 3 | 原文不符
- **問題**：（1）第 48–49 行稱輸入序列轉為中括號語素標籤 `[PRE:m] [ROOT:qaniq] [SUF:un]`；原文 §2.2–2.3（pp. 11–16）定義之三種格式為「原文形式」、「詞根形式」（搭配 `F1`、`FM002` 等詞綴組合編號）及「詞綴字串形式」（前綴加 `-`、中綴以 `<...>` 標記並移至詞根前、後綴加 `-`，如 `m- osa <m> dayang <n> tatak -an`），無 `[PRE:...]` 等標籤。（2）第 52–68 行與架構圖將模型寫為單一編碼器內執行 LayerNorm 加法融合；原文 §3.1.1（pp. 22–25，圖 5）之最佳架構 `FC_ftr_jnt` 係採用**兩個獨立並聯之 Transformer Encoder**（其一編碼子詞嵌入，其二編碼 26／29／49／62 維布林詞綴特徵向量），再將兩編碼器輸出串接（Concatenate）送入解碼器；且未提及華翻族最佳架構 `CF_bert_base`（§3.2.2，pp. 30–31，圖 14）係以 `bert-base-chinese` 取代華語端編碼器。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/使用詞綴資訊提升泛泰雅語機器翻譯效能_金柏毅.md`（§2.2–2.3 pp. 11–16、§3.1–3.2 pp. 22–31 圖 5、14）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §2.1–2.4、第三章、§4.1–4.3 與第五章逐項確認後重寫 Card 1–4：刪除原文未出現之 `[PRE:m]` 標籤，改列原文三種文本形式與詞綴組合 ID；最佳架構改述為 FC_ftr_jnt 之雙 encoder 串接（布林特徵 49／26／29／62 維），刪除無來源之 LayerNorm 加法式與注意力公式；補述中文翻族語最佳系統 CF_bert_base 以 BERT 取代中文 encoder。另修正同頁未登記之問題：Card 4 補列基線並拆分 BERT 與詞綴字串之貢獻，註明外部測試以原文形式最佳；Card 2 補述詞綴資訊多為解析器預測；刪除 Card 5「推翻高資源偏見」「標準架構管線」等無來源表述。證據表見 wiki/evidence/2025-atayalic-affix-mt-jin.md。

### EK-067 | fixed | papers/2025-atayalic-oov-enumeration-yang.md | Card 3 | 原文不符
- **問題**：（1）第 45–52 行與第 66 行架構圖稱系統以音韻轉換函數 $\Phi_{\text{phon}}(p \oplus \text{Infix}(i, r) \oplus s) = w_{\text{unk}}$ 正向生成表面形，並將「第二階段：候選詞根篩選」標為「保留率 > 94%」。原文 §3.2、§3.3、§4.2、§4.3（pp. 29–35、47–57、73）中，94.08%／94.33%／95.74% 召回率屬「第一階段：候選詞根挑選」（直接檢查詞根或其刪母音／中綴變體是否為未知詞子字串，且前後剩餘子串為合法前後綴）；而利用書寫形式轉換規則比對之「第二階段：候選詞根篩選」因過濾掉過多正解詞根、對猜測有害，作者於 p. 73 明言**最終系統決定不執行該步驟**。（2）第 57–64 行將隨機森林寫為對單一候選詞根獨立打分之單點分類器；原文 §3.5（pp. 42–45）實為**成對比較（Pairwise）二元分類器**，對任意兩候選詞根 $(x, y)$ 抽取 44 維特徵（$x$ 13 維、$y$ 13 維、差值 13 維、比值 5 維）進行 $\binom{n}{2}$ 循環賽投票選出最高票詞根。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/以構詞規則窮舉來解決泛泰雅語未知詞問題_楊鈞凱.md`（§3.2–3.5 pp. 29–45、§4.2–4.3 pp. 47–57、§5 p. 73）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文第三至五章逐項確認後重寫 Card 3：刪除無來源之 $\Phi_{\text{phon}}$ 與集合式；94.08%／94.33%／95.74% 改歸「候選詞根挑選」階段；明確寫出原規劃之書寫形式篩選因濾掉過多正解而不執行；隨機森林改述為 44 個特徵之成對比較分類器，以兩兩配對投票選出詞根。另修正同頁未登記之問題：Card 4 補列表 38 之規則策略與隨機森林答對數及表 15 之詞根集合上限；Card 3、Card 5 註明中文語意特徵依賴含未知詞句子之中文翻譯；刪除「首創」「徹底扭轉」等過度表述。證據表見 wiki/evidence/2025-atayalic-oov-enumeration-yang.md。

### EK-068 | fixed | papers/2025-paiwan-bunun-morphology-mt-wu.md | Card 1–3 | 原文不符
- **問題**：（1）Card 1（第 29 行）、Card 2（第 36 行）與 Card 3（第 47–52、65 行）稱本文建立環綴算子、音節週期性自相關檢測，並將「構詞解析器提取之深層詞根與詞綴特徵注入預訓練多語言遷移模型」。原文第 3–6 章（pp. 9–33）中，重疊詞僅以複製詞根末 1–2 個 CV 音節為 `<RED>` 之四步驟字串規則處理；且第 4–5 章之機器翻譯實驗**完全未使用任何詞綴或構詞解析資訊**，第 6 章結論（p. 33）明確將「針對詞綴資訊並將資訊導入模型訓練中」列為未來工作。（2）Card 3（第 58–62 行）列出含 KL 散度正則化項之損失函數；原文 §4.3（pp. 23–24）僅為馬來語／印尼語預訓練後直接微調之兩階段訓練，無 KL 散度正則化項。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/排灣語、布農語的構詞結構自動分析與機器翻譯_吳維中.md`（§3.1–3.2 pp. 9–15、§4.3 pp. 23–24、§6 p. 33）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文第二至六章逐項確認後重寫 Card 1–3 與 hook：刪除原文未出現之環綴、音節週期性自相關檢測與 KL 正則化式；排灣語重疊改述為原文之「重複詞根最後兩音節」字串規則；明確寫出翻譯實驗未使用構詞資訊，作者將其列為未來工作。另修正同頁未登記之問題：Card 4 補列各技術疊加之 BLEU 與前綴組合正確率，註明表 22 與表 24 數值不一致、中文翻族語最終分數含 BERT 之貢獻；刪除「跨語系普適性」「首套開源基礎設施」等無來源表述。證據表見 wiki/evidence/2025-paiwan-bunun-morphology-mt-wu.md。

### EK-069 | fixed | papers/2022-formosan-say-verbs-hsieh.md | Frontmatter 與 Card 3 | 原文不符
- **問題**：（1）Frontmatter `title`（第 2 行）與主標題（第 20 行）將英文標題寫為 `"Semantic Phenomena of Verbs of Saying in Formosan Languages: A Typological Investigation"`；原文末頁（PDF p. 46，期刊 p. 92）之正式英文標題為 `"On the Semantics of SAY Verbs in Formosan Languages"`。（2）Card 3（第 46–63 行）之集合聯集式與連續向量空間線性插值式未見於原文（原文圖 4，p. 83 係以 `X[述說]、[動作]` 語義特徵標記描述語法化鏈），未標明為 Wiki 自行形式化推導。
- **來源**：`raw/my-focus/台灣相關論文/台灣南島語「說」動詞語義現象初探_謝富惠.pdf`（p. 83 圖 4、p. 92 英文摘要頁）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：`title` 與主標題改為英文摘要頁之正式題名 *On the Semantics of SAY Verbs in Formosan Languages*；刪除 Card 3 原文未出現之集合式、語法化分段函數與向量插值式，改述原文圖一至圖四之語義延伸機制與施為動詞假說。另修正同頁未登記之問題：Card 6 原列泛泰雅語例詞 `musa’`、`mhai`、`kema` 有誤（`kema` 為卑南語），改為原文表一、表二之泰雅語 `mha`、賽德克語 `mesa`／`kesa-un`、太魯閣語 `mesa`／`sun`，並補述其兼具「做」義；刪除 Card 5「可顯著提升依存句法分析」等無來源表述，補列作者自述之限制。證據表見 wiki/evidence/2022-formosan-say-verbs-hsieh.md。

### EK-070 | fixed | papers/2024-formosan-temporal-words-lim.md | Frontmatter、Card 3 與 Card 6 | 原文不符
- **問題**：（1）Frontmatter `title`（第 2 行）與主標題（第 20 行）將英文標題寫為 `"A Preliminary Cross-Linguistic Comparison of Temporal Words in Formosan Languages"`；原文末頁（PDF p. 27）之正式英文標題為 `"A Preliminary Comparative Study of Formosan Temporal Words"`。（2）Card 3（第 45–57 行）之代數分解式未見於原文，未標明為 Wiki 自行推導。（3）Card 6（第 93 行）稱泰雅語「包含未實現前綴（如 `sa-`）卻帶有過去時間詞根……檢索詞庫中對應之『昨天』詞根，從而推導出『明天』之正確語義」；原文表 12（p. 14）明確標示賽考利克泰雅語 `sa`（如 `sa knwan` 過去何時、`sa kaxa'` 前天）為**實現（realis，過去）**標記而非未實現標記，且表 3（p. 7）顯示泰雅語「昨天」（`shera'/hera'`）與「明天」（`suxan`）屬異根（類型 1.2）。
- **來源**：`raw/my-focus/台灣相關論文/台灣南島語言時間詞之跨語言比較初探_林鴻瑞.pdf`（p. 7 表 3、p. 14 表 12、p. 27 英文摘要頁）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：`title` 與主標題改為英文摘要頁之正式題名 *A Preliminary Comparative Study of Formosan Temporal Words*；刪除 Card 3 原文未出現之 $T(\Delta t)$、$\operatorname{Root}$ 與三類代數式，改列表九之五個次類型與表十一之三種標記類型；Card 6 改正：賽考利克泰雅語 `sa` 為實現標記（表十二），且泛泰雅語「昨天」與「明天」詞根不同（表三），改以「前天＝後天＝`kaxa’`、靠標記區分」為延伸重點。另修正同頁未登記之問題：Card 4 註明原文表九與表十三對賽夏語歸類不一致；刪除 Card 5「重構幾何視角」「建立數學先驗」等無來源表述。證據表見 wiki/evidence/2024-formosan-temporal-words-lim.md。

### EK-071 | fixed | papers/2024-finnish-northern-sami-mt-saleva.md | Card 3 與 Card 5 | 原文不符
- **問題**：（1）Card 3（第 55 行）將語言模型先驗正則化項之 KL 散度方向寫反為 $\mathcal{D}_{\text{KL}}(P_{\text{NMT}} \,\|\, P_{\text{LM}})$；原文 §3.2（p. 12950）定義之目標函數為由固定 LM 指向 NMT 之正向 KL 散度 $D_{\text{KL}}(p_{\text{LM}}(y) \,\|\, p_{\text{NMT}}(y \mid x))$。（2）Card 3 架構圖（第 63 行）將芬蘭語與北薩米語單語語料庫一併送入「逆向神經翻譯模型」；原文 §3.1（p. 12950）中，北薩米語單語資料由逆向模型回譯，而芬蘭語單語資料由正向模型正譯（forward translation）。（3）Card 5（第 80 行）稱「當回譯資料量充足時，必須全面採用 Tagged BT」；原文 §4.3（p. 12952，表 5）明確指出 `<BT>` 標記效果不一，在僅用回譯時使域內 UiT 測試集 BLEU 微降（41.75 至 41.71），結合正譯與回譯時使 UiT（38.96 至 38.84）與 YLE（17.91 至 17.36）之 BLEU 均下降。
- **來源**：`raw/my-focus/報告論文題材/2024.findings-acl.768.pdf`（§3.1–3.2 p. 12950、§4.3 p. 12952 表 5）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3–§5 與表 1–5 核對後：KL 散度改為原文式 $D_{\text{KL}}(p_{\text{LM}}(y) \| p_{\text{NMT}}(y \mid x))$；架構圖改為北薩米語單語經反向模型回譯、芬蘭語單語（mC4）經正向模型正譯；Card 5 刪除「必須全面採用 Tagged BT」，改述原文「標記在某些情況有益、在其他情況沒有」並列出各設定數值。另修正同頁未登記之問題：題名改為原文之 *Northern Sámi*；Card 4 補列表 5 完整結果並註明內文 33.80 與表 5 之 33.30 不一致；補列作者自述之單一語言對與單次執行限制。證據表見 wiki/evidence/2024-finnish-northern-sami-mt-saleva.md。

### EK-072 | fixed | papers/2025-manchu-in-context-mt-pei.md | Frontmatter、Card 3 與 Card 5–6 | 原文不符
- **問題**：（1）Frontmatter `hook`（第 17 行）、引言（第 22 行）、Card 5（第 83 行）與 Card 6（第 95 行）稱注入語法書會導致翻譯效能「推理衰退／下降」；原文 §4.3（p. 8772，表 3）與附錄 E（p. 8783，表 10）顯示加入語法書段落使分數微幅上升但統計上不顯著（$p = 0.4$），原文結論為「語法書幾乎無助益（grammars hardly help）」，而非造成衰退。（2）Card 3（第 45–53 行）將提示組合寫為「五大獨立組件的笛卡爾積」並以 $\arg\max$ 解碼；原文 §4（p. 8770）明言窮舉所有組合不可行，故採依序貪婪疊加（sequential greedy integration），且實驗使用溫度 0.9／1.0 採樣。（3）Card 3（第 62 行）稱加密實驗將滿文轉寫為「模型完全未見過的對應符號」；原文 §5.2（p. 8773）實為拉丁字母循環位移密碼（如 `a -> e`、`amban -> encep`）。
- **來源**：`raw/my-focus/報告論文題材/2025.acl-long.429.pdf`（§4 p. 8770、§4.3 p. 8772 表 3、§5.2 p. 8773、附錄 E p. 8783 表 10）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：hook 與 Card 1、5、6 改述原文結論「語法書幾乎沒有幫助」（微幅提升且不顯著，附錄 G 表 10 p = 0.4），下降者為 CoT；Card 3 刪除「笛卡爾積」與 argmax 式，改述依序加入組件之流程與溫度 0.9／1.0 採樣；加密改述為原文之字母位移替換（`amban`→`encep`）。另修正同頁未登記之問題：Card 4 補列各步驟數值、顯著性、人工評估與 §6 合成資料訓練 mT5 之結果；顯著性所在之附錄為 G（非 E）；註明英文平行語料由 Google 翻譯自中文。證據表見 wiki/evidence/2025-manchu-in-context-mt-pei.md。

### EK-073 | fixed | papers/2026-tao-filipino-nmt-macayan.md | Card 3 與 Card 6 | 原文不符
- **問題**：（1）Card 3（第 45–51 行與第 60 行架構圖）稱在菲律賓語（Tagalog）大規模預訓練並加上參數距離懲罰項；原文 §4.6（p. 32）中，Tagalog（Filipino）即為目標語言，Model 3 係先將 `NLLB-200 (600M)` 於巴丹語群親屬語 **Ivatan-to-Tagalog（伊巴丹語－菲律賓語）**平行語料微調，再於 Yami-to-Tagalog（達悟語－菲律賓語）微調，且無任何 $L_2$ 參數距離懲罰項。（2）Card 3（第 53–57 行與第 63 行架構圖）與 Card 6（第 90 行）稱本文訓練「構詞感知子詞正則化（Morphology-Aware Subword BPE），將語言學詞綴字典注入分詞優先級，確保 `mi-`、`ma-`、`om-` 不被截斷」；原文 §7（p. 34）明確指出**受限於研究時程，本文直接使用 NLLB-200 預設分詞器**，並將子詞／構詞分詞列為未來工作建議。
- **來源**：`raw/my-focus/報告論文題材/2026.loresmt-1.2.pdf`（§4.6 p. 32、§7 p. 34）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：Card 3 刪除「於菲律賓語大規模預訓練」與 $L_2$ 參數距離懲罰項，改述原文三個模型（Model 3 為伊巴丹語→他加祿語預訓練後再微調）；刪除「構詞感知子詞 BPE」，改述原文明言因時間限制使用 NLLB-200 預設分詞器、子詞處理列為未來工作。另修正同頁未登記之問題：Card 1 改依原文寫明達悟語屬巴丹語群「而非臺灣南島語」；補列合成資料之產生方式與表 3 完整數值；註明原文四處內部不一致（達悟語－英語／他加祿語混用、少於 5,000 句與 10,498 句、6.61 與 6.67、對 FormosanBench 之錯誤引述）。證據表見 wiki/evidence/2026-tao-filipino-nmt-macayan.md。

### EK-074 | fixed | papers/2019-generalized-data-augmentation-xia.md | Card 3 | 原文不符
- **問題**：（1）第 49–53 行稱以「字元級音變轉換模型」或構詞映射將高資源語言轉為低資源語言；原文 §3.1–3.2（pp. 5788–5789）實為透過正交 Procrustes SVD 與 CSLS 雙語詞典歸納進行逐詞替換（Word-by-word Substitution），或結合基於去噪自編碼與迭代回譯之改良無監督機器翻譯（M-UMT）。（2）第 56–59 行將 NMT 訓練寫為帶權重衰減係數 $\alpha_k$ 之加權對數似然；原文 §4.4（pp. 5790–5791）係將真實與偽平行語料直接串接預訓練後進行混合微調（mixed fine-tuning），無 $\alpha_k$ 加權目標式。
- **來源**：`raw/my-focus/英文論文/Generalized Data Augmentation for Low-Resource Translation_P19-1579.pdf`（§3.1–3.2 pp. 5788–5789、§4.4 pp. 5790–5791）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §2–§5 核對後：Card 3 刪除「字元級音變轉換」與 $\alpha_k$ 加權目標式，改述原文之 Procrustes／SVD＋CSLS 詞典歸納逐詞替換、M-UMT 修飾，以及預訓練後混合微調；補列原文四種增強情境。另修正同頁未登記之問題：Card 4 補列表 2 主要列；刪除 Card 5「被 mBART、NLLB 沿用」等無來源表述；Card 6 改為有條件之延伸。證據表見 wiki/evidence/2019-generalized-data-augmentation-xia.md。

### EK-075 | fixed | papers/2023-low-resource-nmt-survey-ranathunga.md | Card 1、Card 3 與 Card 6 | 原文不符
- **問題**：Card 1（第 17 行）與 Card 3（第 43–63 行）稱綜述建立四大支柱（含「語言學先驗融合：詞綴特徵拼接／投影、句法樹與詞典注入」及「輕量化 Adapter、參數高效微調 PEFT」）並列出含 $L_2$ 錨定項之遷移學習公式；Card 6（第 87 行）稱「綜述指出：在資料量小於一萬句的極端低資源語境中……真正的突破口在於構詞感知與外部符號知識庫的在線檢索（RAG）」。原文（ACM CSUR 2023，§3–§11，圖 1、2、7）將低資源 NMT 分為六類技術（資料增強、無監督、半監督、多語言、遷移學習、零樣本／樞紐），全文僅有一條 Google Scholar 離群值檢定公式（p. 229:22，式 1），決策流程圖（圖 7）以 50 萬句為低資源分界，且全文從未提及 RAG、LLM、Adapter 或 PEFT。
- **來源**：`raw/my-focus/英文論文/Neural Machine Translation for Low-resource Languages A Survey_3567592.pdf`（§3–§11 pp. 229:5–229:22 圖 1、2、7）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：Card 1、3 刪除「四大支柱」（含語言學先驗融合、Adapter、PEFT）與 $L_2$ 錨定遷移式，改列原文六類技術（資料增強、無監督、半監督、多語言、遷移學習、零樣本）與圖 7 選擇流程；Card 6 刪除「綜述指出一萬句以下應以構詞感知與 RAG 為突破口」，註明綜述資料截至 2021–2022 年，未涵蓋 LLM 與 RAG。另修正同頁未登記之問題：原 Card 4 稱「原文沒有提出語料門檻」不精確，改述原文以 50 萬／10 萬句為參考門檻並明言非絕對。證據表見 wiki/evidence/2023-low-resource-nmt-survey-ranathunga.md。

### EK-076 | fixed | papers/2024-formosan-mt-bilingual-lexicon-zheng.md | Card 3 | 原文不符
- **問題**：第 45–68 行稱本文採溫度採樣係數 $\tau$、動態衰減權重 $\beta \in (0, 1]$ 之混合損失函數，並定義交叉注意力香農熵；原文 §4–§5（pp. 11251–11254）全文無任何數學公式，方法一（`+ Lex.`）僅將雙語詞典詞條與平行句直接串接訓練，方法二（`+ PPD`，§5.1）則隨機替換平行句中 20% 族語詞彙合成偽平行資料，方法三為兩者結合。Card 3 完全漏述產生最佳成績（+5.55 BLEU／+10.33 chrF）之方法二 PPD，卻虛構溫度採樣、動態權重與注意力熵公式。
- **來源**：`raw/my-focus/英文論文/Improving Low-Resource Machine Translation for Formosan Languages _ 2024.findings-acl.670v2.pdf`（§4–§5 pp. 11251–11254）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3–§5 核對後：Card 3 刪除原文未出現之溫度採樣、動態衰減權重 $\beta$ 與注意力熵公式，改述原文三種做法——詞典直接作為平行資料、以詞典替換族語端詞彙產生偽平行資料（多以 20% 替換率最佳）、兩者並用。另修正同頁未登記之問題：Card 4 補列表 2（16 種語言全部提升，平均 +3.37 BLEU）、平行句比詞條更有用、外部詞典增益較小，以及多語言預訓練無明確改善之負面結果；刪除 Card 5「登上 ACL 讓臺灣南島語站上世界舞台」等表述；補列作者自述之限制。證據表見 wiki/evidence/2024-formosan-mt-bilingual-lexicon-zheng.md。

### EK-077 | fixed | papers/2025-formosanbench-llm-benchmark-lin.md | Card 2、Card 3 與 Card 6 | 原文不符
- **問題**：（1）Card 3（第 50 行）將資料點寫為含英語譯文與語音對齊之五元組；原文 §4（pp. 16529–16530，表 1）之三項任務取自三個彼此獨立之資料源（MT 取自原民會線上辭典族華句對且無英語譯文、ASR 取自族語 E 樂園教材音檔、摘要取自族語維基百科條目與首段），並非同源五元組。（2）Card 3 架構圖（第 72 行）列出 `chrF++` 與 `SBERT` 指標；原文 §5.3（p. 16532）僅使用 BLEU、WER、ROUGE-2／ROUGE-L、GPT-4o-mini 評分（1–5 分）與人工評估，未使用 `chrF++` 或 `SBERT`。（3）Card 2（第 37 行）與 Card 6（第 99 行）稱「論文揭示的 4~6 倍 Tokenizer 膨脹問題」；誠如 Card 4（第 81 行）已註明，原文並未測量或報告 Tokenizer 膨脹倍率。
- **來源**：`raw/my-focus/英文論文/FormosanBench Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models _ 2025.findings-emnlp.897.pdf`（§4 pp. 16529–16530 表 1、§5.3 p. 16532）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：Card 3 刪除「同源五元組」與 ICL 公式，改列三項任務之獨立資料來源（線上辭典、族語 E 樂園、族語維基百科）；評估指標改為原文之 BLEU、WER、ROUGE-2／L、GPT-4o-mini 評審與人工檢視；Card 2、Card 6 刪除原文未報告之「4~6 倍 Tokenizer 膨脹」。另修正同頁未登記之問題：Card 4 補列表 2–6 主要數值與母語者人工檢視結果；註明原文三處不一致：表 1 切分約 60:10:30 而非文稱 70:10:20、表 2 BLEU 看似 0–1 尺度、§6.1 對 LLM 評審分數方向之解讀與表 3 相反；刪除 Card 5「終結無基準可評」「指明必須開發形態解析外掛」等表述。證據表見 wiki/evidence/2025-formosanbench-llm-benchmark-lin.md。

### EK-078 | fixed | papers/2025-indigenous-tek-ai-revitalization-wang.md | Card 1 與 Card 3 | 原文不符
- **問題**：（1）Card 1（第 29 行）作者姓名寫作「王 reen-cheng」，中英大小寫混雜。（2）Card 3（第 45–53 行）將模型寫為 Nonaka 四階段 SECI 遞迴算子；原文 §3.2（pp. 7–11，圖 3）係將 Nonaka 模型擴展為四層知識矩陣（$K_1$ 個體內隱、$K_2$ 個體外顯、$K_3$ 部落社群、$K_4$ 文化系統）與 12 個知識轉換階段，並搭配五層 LKM 架構（§3.4，圖 5）與 Plan–Act–Observe–Adjust 代理迴圈（§3.5，圖 6）。（3）Card 3（第 56–61 行）列出基於餘弦相似度之禁忌懲罰損失函數；原文為質性系統架構論文，全文無任何數學公式或損失函數（文化禁忌係由第一層部落會議審查、第三層語義標籤與第五層規則權限矩陣控管）。
- **來源**：`raw/my-focus/英文論文/From Tacit Knowledge Distillation to AI-Enabled Culture Revitalization Modeling Knowledge Cycles in Indigenous Cultural Systems_socsci-15-00007.pdf`（§3.2–3.5 pp. 7–15 圖 3–6）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 1 將作者更正為國立臺東大學王任慶（Reen-Cheng Wang）教授團隊；Card 3 依原文圖 3 改寫為四層知識矩陣（$K_1 \sim K_4$）與 12 階段雙向知識循環模型，補列圖 5 之五層 LKM 架構（Layer 1 倫理治理至 Layer 5 代理部署）與圖 6 之 Plan–Act–Observe–Adjust 代理迴圈；刪除虛構之餘弦相似度禁忌損失函數，依原文說明文化禁忌係由部落會議審查、第一手權重與規則矩陣控管；Card 4 交代質性系統架構論文屬性。建立證據表 wiki/evidence/2025-indigenous-tek-ai-revitalization-wang.md，頁面 verification 改為 verified。

### EK-079 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 3 | 原文不符
- **問題**：第 43–62 行與架構圖稱方言距離係「對共享同一個語義概念的詞彙集合 $\mathcal{V}_{AB}$」計算編輯距離並執行「多維尺度分析（MDS）」。原文 §2.3（p. 125）並未對齊同義概念詞表亦未使用 MDS，而是直接對語料庫表面詞形計算三項指標：（1）詞級 TF-IDF 餘弦相似度（`min_df=2`、`sublinear_tf=True`）、（2）頻率 $\ge 5$ 詞型之未加權 Jaccard 相似度、（3）各方言前 500 高頻詞型雙向平均之字元級正規化 Levenshtein 距離。Card 3 完全漏述前兩項核心指標（TF-IDF 餘弦與 Jaccard），且虛構概念對齊詞表與 MDS。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`（§2.3 p. 125）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 刪除虛構之語義概念對齊詞表與 MDS 分析，改述原文真實採用之三項詞彙相似度指標（詞級 TF-IDF 餘弦、詞頻 $\ge 5$ 詞型 Jaccard 相似度、前 500 高頻詞之字元級正規化 Levenshtein 距離）與 Bootstrap 500 次抽樣信心區間檢驗；Card 4 補齊 Table 1–3 全語料特徵（Hapax 率 72%–79%）、多方言語言核心共有詞比例與分群發現（賽德克語 0.820 最緊密、布農語重現經典三分群、泰雅語 0.605 與魯凱語 0.648 分化最深）。建立證據表 wiki/evidence/2026-epark-formosan-dialectometry-gagnier.md，頁面 verification 改為 verified。

### EK-080 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 3 與 Card 6 | 原文不符
- **問題**：（1）Card 3（第 47 行與第 62 行架構圖）稱資料清洗採語言識別器与語義對齊過濾 $\operatorname{AlignScore}(x_i, y_i) \ge \tau$；原文 §3.3（p. 3448）係使用正則表達式與詞／字元長度比門檻（2 詞以上剔除 $r \le 0.2$ 或 $r > 8.0$；少於 2 詞剔除字元比 $r \le 0.05$ 或 $r > 20.0$），無語義對齊模型或語言識別器。（2）Card 3（第 49 行）所列 15 語言代碼含錯誤代碼 `puy`、`ruk`、`cou`、`sai`、`kan`、`sed` 且同時列出 `sed` 與 `trv`（漏列噶瑪蘭語 `ckv` 與撒奇萊雅語 `szy`）；原文表 1（p. 3447）之 ISO 639-3 代碼為 `ami, bun, ckv, dru, pwn, pyu, ssf, sxr, szy, tao, tay, trv, tsu, xnb, xsy`。（3）Card 3（第 53–59 行）稱對 NLLB-200 進行 15 語多語言聯合微調；原文 §4.2（p. 3450）明言係針對各族語－華語及 4 個族語－英語**分別訓練獨立之雙向雙語模型**，並於 §6（p. 3453）將多語言聯合預訓練列為未來工作。（4）Card 6（第 90 行）寫「30 萬高品質句對」，與 Card 4 之總量 493,519 句不一致。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`（§3.3 p. 3448、表 1 p. 3447、§4.2 p. 3450、§6 p. 3453）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 刪除虛構之語言識別器與 AlignScore 模型，改述原文真實採用之正則清洗與詞/字元長度比例過濾門檻；校正 15 個 ISO 639-3 語言代碼並補齊 ckv 與 szy；澄清模型訓練為獨立之雙向雙語基準，而非 15 語聯合多語言預訓練；Card 6 校正語料總量為 49.3 萬句對（含 39.7 萬族語－華語句對），消除數據矛盾。建立證據表 wiki/evidence/2026-formosanmt-parallel-corpus-scheppat.md，頁面 verification 改為 verified。

### EK-081 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | Card 1 與 Card 3 | 原文不符
- **問題**：（1）Card 1（第 30 行）將作者寫作「王 reen-cheng 教授」，中英大小寫混雜。（2）Card 3（第 44–53 行）列出雙軌混合檢索線性加權公式（結合餘弦相似度與 BM25），並於第 62 行與架構圖（第 65–69 行）稱辭典模組解析出「詞根＋詞綴焦點＋中文詞條」且與向量庫並聯檢索。原文 §3.1–3.2（pp. 4–5，圖 1–3）全文無任何數學公式、未使用 BM25，亦未由辭典解析詞根與焦點；實際流程（圖 3）為**串聯式條件分支（if-else fallback）**：逐詞先查記憶體內 JSON 雜湊表（`Is it in the hash map? YES -> Word Merge`），僅當詞典未命中（`NO`）時才查詢 Qdrant 向量資料庫。
- **來源**：`raw/my-focus/英文論文/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`（§3.1–3.2 pp. 4–5 圖 1–3）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核實後重寫：Card 1 將作者校正為「王任慶（Reen-Cheng Wang）教授團隊」；Card 3 刪除虛構之餘弦相似度結合 BM25 線性加權公式，改述原文真實採用之串聯條件分支（If-Else Fallback）管線（逐詞查詢記憶體 JSON 雜湊表，命中則 Word Merge，未命中才查詢 Qdrant 向量庫），並澄明詞典模組僅做表面詞字面匹配；Card 4 補齊 250 句評估測試集之 Cosine、BLEU 與 ROUGE-L 對比數據及語法複雜句局限。建立證據表 wiki/evidence/2026-hybrid-dictionary-rag-llm-paiwan-wang.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現論文首頁僅列 Reen-Cheng Wang 為通訊作者並列系所，未標示「教授」職稱；本頁與先前處理記錄使用「教授團隊」，若保留須補校方職稱來源，否則改為「作者團隊／通訊作者王任慶」。方法與測試指標本次抽查符合原文；因作者職稱來源尚未補足，狀態重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文首頁（p. 1）核對作者署名與通訊作者註記，移除頁面與證據表中原文未列出的「教授」職稱，改以作者團隊及通訊作者王任慶呈現。狀態改為 fixed。

### EK-082 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 3 與 Card 4 | 原文不符
- **問題**：（1）Card 3（第 44–53 行）稱依據「句法成分樹（Constituency Tree）」拆解來源句，並檢索包含片段及其「對應目標語譯文子串的最小對齊例句對」。原文 §3（p. 3，圖 1）完全未使用句法成分樹剖析器或子串級目標語對齊，而是以**由 7 個連續詞遞減至 1 個詞之滑動視窗（sliding window）**在檢索庫來源端進行精確子字串匹配，為每個片段隨機抽取至多 6 組完整雙語句對；原文只說片段選取會盡量避免重疊，理想上完整且不冗餘，並未保證零重疊；且 Card 3 漏述 Pivoted Fragment-Shot（§3，pp. 3–4，圖 2）經由義大利語樞紐進行兩階段巢狀片段檢索（排除整句完全重疊）之機制。（2）Card 4（第 83–84 行）兩度將研究對象 **Ladin（拉定語，北義多洛米蒂山區雷托－羅曼語支少數民族語言：Val Badia 與 Gherdëina）**誤寫為「**拉丁語**變體」。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`（§1 p. 1、§3–§4 pp. 3–4 圖 1–2）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核實後重寫：Card 3 刪除虛構之句法成分樹剖析與 argmax 公式，改述原文真實採用之 7 至 1 詞滑動視窗來源端匹配（抽取至多 6 組雙語例句、無重疊覆蓋）以及兩階段樞紐片段提示（PF）機制；Card 4 將研究對象正名為北義多洛米蒂山區雷托－羅曼語支「拉定語（Ladin）」兩大變體（Val Badia 與 Gherdëina），糾正「拉丁語變體」之筆誤；補列 Table 1–3 完整數據、推論耗時與語法有效性局限。建立證據表 wiki/evidence/2025-fragment-shot-reasoning-mt-frontull.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現先前處理記錄及證據表把原文「片段選擇會盡量避免重疊，理想上完整且不冗餘」寫成「無重疊覆蓋」，語氣過度絕對。方法本身修正符合原文；須將記錄與證據表改為「盡量避免重疊，力求完整且不冗餘覆蓋」後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文 §3（p. 3）核對，將引言、Card 3、Card 5 與證據表中的「不重疊／無重疊」絕對表述改為「盡量避免重疊，理想上完整且不冗餘」，並註明原文不保證零重疊；同步修正本問題對方法的描述，保留先前處理記錄以供追溯。狀態改為 fixed。

### EK-083 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 3 與 Card 4 | 原文不符
- **問題**：Card 3（第 46–62 行）僅以抽象算子描述檢索，未交代原文 §3.2（p. 132）之具體檢索設計：詞彙表（Glossary）係以 spaCy `en_core_web_sm` 斷詞後進行 `{1,2}`-gram 重疊匹配，翻譯記憶庫（Translation Memory）係以 `Tantivy` 函式庫執行 Top-$N$ BM25 檢索，並以 `MADLAD-400-10B`／`OPUS-MT`／`NLLB-54B` 搭配 `Gemini 2.0 Flash` 進行少樣本思維鏈（CoT）後編輯；且原文全文無數學公式（式 52、56 應標明為依原文流程整理之示意式）。
- **來源**：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`（§3.2 p. 132、§4.1–4.2 pp. 132–133）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 補齊系統具體技術實作，包含 Django 後端、Docker 容器化、初譯模型支援（MADLAD-400-10B、OPUS-MT、NLLB-54B）、spaCy en_core_web_sm 之 {1,2}-gram 詞彙表動態比對、Rust Tantivy 函式庫之 Top-N BM25 翻譯記憶庫檢索，以及 LiteLLM 代理之 Gemini 2.0 Flash CoT 後編輯提示；標明流程公式為示意式；Card 4 補齊德頓語醫療（+16.90 chrF++ / +13.51 BLEU）、比斯拉馬語救災（+22.41 chrF++ / +17.69 BLEU）、SUS 81.25 分與 FLORES 六語基準對比。建立證據表 wiki/evidence/2025-tulun-adaptable-lrl-mt-merx.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核原文表 1（印刷頁 133）發現先前處理記錄把平均增益誤寫成各語言增益，且加入原文未報告的 BLEU。原文僅報 chrF++：MADLAD 基線下 TDT 為 35.78→47.87（+12.09）、BIS 為 15.22→47.94（+32.72），平均增益 +22.41；OPUS-MT 基線下 TDT 為 16.01→34.27（+18.26）、BIS 為 32.60→48.14（+15.54），平均增益 +16.90。先前寫入的 +13.51／+17.69 BLEU 以及 26.96、43.86、28.51、50.92 等數值均無原文表格依據；論文頁與證據表也含不符原文數值。須一併更正處理記錄、Card 4 與證據表後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文 §4.1.1（pp. 132–133）與表 1 核對並重寫 Card 4、證據表：更正詞彙表與翻譯記憶數量（Tetun 2,698／1,018，Bislama 5,769／3,353；評估保留 451／841），列明兩個基線下各語言的 ChrF++ 分數與增益，將 +22.41、+16.90 標為跨語言平均增益，移除未報告的 BLEU 及其數值。狀態改為 fixed。

### EK-084 | fixed | papers/2026-context-volume-rag-domain-shift-setiawan.md | Card 3 | 原文不符
- **問題**：第 54–60 行稱論文證明 $\operatorname{chrF++}$ 與語境容量呈精確對數線性公式，且第 48 行稱使用「稠密檢索器」召回上下文。原文 §4.3 與 §5.2–5.3（pp. 90–93，表 2、4、5、6）全文無此對數線性公式；表現最佳之平行句檢索策略並非稠密向量檢索，而是基於 `rapidfuzz` 字元級正規化 Levenshtein 相似度 $\ge 0.5$ 之**詞級模糊匹配（Word-Level Fuzzy Matching）**；且句級檢索（BM25、BGE、ChrF-RAG）於 $K \approx 60$ 即飽和，詞級檢索於每詞 $n = 10$（有效句數 $K \approx 137$，35.28 chrF++）達峰值後，於 $n = 15, 20$（$K \approx 205, 272$）因語境雜訊回落至 35.16 與 34.22 chrF++（表 5），並非單調無限上升。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Context Volume Drives Performance Tackling Domain Shift in Extremely.pdf`（§4.3 p. 90、§5.2–5.3 pp. 91–93、附錄 E p. 100 表 4–6）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 刪除虛構之對數線性公式與單一稠密檢索器表述，改述真實之四種檢索策略（BM25、BGE、ChrF-RAG 以及基於 RapidFuzz 之詞級模糊匹配）；交代句級檢索在 $K \approx 60 \sim 80$ 飽和與詞級檢索在 $N=10$（eff. $K \approx 137$）達峰值 35.28 chrF++ 後因語境雜訊回落之實證消融數據；補列詞典檢索單調線性增長特性與完整詞典取得 31.32 chrF++；Card 4 補齊 Table 1、2、4、5、6 詳細數據與 Table 7 三大定性失敗修復案例。建立證據表 wiki/evidence/2026-context-volume-rag-domain-shift-setiawan.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現原文 §4.3.2（印刷頁 90）稱詞典共 2,375 條，附錄表 6（印刷頁 100）則列 2,377 條；證據表只採 2,377 並判為完全符合，未記錄原文內部差異。其餘檢索策略與容量結果本次抽查符合原文；須在證據表註明筆數差異後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文 §3.1（p. 89）、§4.3.2（p. 90）與附錄表 6（p. 100）核對，確認文內分別列 2,377 與 2,375 條詞典，未解釋該差異；已在論文頁與證據表並列兩個數值，並將表述限定為單調提升，移除線性增長之無來源描述。狀態改為 fixed。

### EK-085 | fixed | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | Card 3 | 原文不符
- **問題**：（1）第 46–48 行將 SONAR 評分寫為餘弦相似度；原文 §2.1.1（p. 226）明言使用 `blaser_2.0` 跨語言語義相似度預測模型（輸出 1–5 分段，故門檻為 3.0 與 3.7，餘弦相似度不可能大於 1）。（2）第 61–72 行與架構圖將四階段課程學習順序與資料集完全寫反：頁面寫作「階段 1：FineWeb-2 合成回譯 50 萬句 -> 階段 2：SONAR 標準品質 -> 階段 3：SONAR 高品質 -> 階段 4：官方驗證集收斂」。原文 §2.3.3（pp. 227–228）與表 1（p. 226）之真實順序為：**階段 1：OPUS 標準品質多語資料**（$3.0 \le \text{SONAR} < 3.7$，含俄、吉、烏茲別克、塔吉克四語全方向共 8,207,314 句）-> **階段 2：OPUS 高品質多語資料**（$\text{SONAR} \ge 3.7$，7,069,840 句）-> **階段 3：FineWeb-2 開源合成回譯資料**（由 50 萬篇吉爾吉斯語文件切出 1,849,234 段，經 Gemma-3-27B 與 Qwen3-235B 回譯及 MADLAD-400-7B-MT 交叉熵 $(0.1, 4.5)$ 過濾後保留 1,566,927 句對、雙向 3,133,854 句）-> **階段 4：SiberianPersonaChat 高品質合成對話資料**（由 GPT-4o 翻譯之 56,529 段俄吉對話、雙向 113,058 句，絕非在官方驗證集上訓練）。另漏述烏茲別克語／塔吉克語輔助遷移（§2.3.1）與 `mt0-large` 詞表剪枝（1.23B 至 800M，§2.3.2）。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Data-Centric Approach at the LoResMT 2026 Turkic Translation.pdf`（§2.1.1 p. 226 表 1、§2.3.1–2.3.3 pp. 227–228）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 更正 SONAR 評分為 `blaser_2.0` 跨語言語義相似度預測模型（1–5 分制，非餘弦相似度）；糾正四階段課程學習倒置錯誤，改述真實順序（階段 1：OPUS 標準 8.2M $\to$ 階段 2：OPUS 高品質 7.1M $\to$ 階段 3：FineWeb-2 回譯 3.1M $\to$ 階段 4：合成對話 113K）；補列烏茲別克與塔吉克雙語輔助遷移、以及 mt0-large 詞表剪枝由 1.23B 壓縮至 800M 架構；Card 4 補齊 Table 1–3 與官方競賽測試集（49.1 chrF++ / 69.7 xCOMET 奪冠）詳細數據。建立證據表 wiki/evidence/2026-data-centric-russian-kyrgyz-mt-novokshanov.md，頁面 verification 改為 verified。

### EK-086 | fixed | concepts/formosan-computational-linguistics.md | Frontmatter 與關鍵突破支柱 | 原文不符
- **問題**：（1）Frontmatter `papers`（第 13 行）將研究臺灣閩南語（漢藏語系漢語族）之 `2024-taiwanese-mt-resegmentation-tang` 列入「臺灣南島語計算語言學」概念頁。（2）第 48–50 行重述 `2025-atayalic-oov-enumeration-yang.md` 之錯誤，稱楊鈞凱（2025）「利用音韻變化規則與構詞律正向窮舉所有合法衍生形」（實為子字串候選詞根挑選搭配成對隨機森林循環賽投票，且正向書寫形式比對篩選因有害而未執行，見 EK-067）。（3）第 57 行稱 Gagnier（2026）「利用正規化 Levenshtein 編輯距離與多維度對齊，量化臺灣南島語 16 族 42 方言」（漏述 TF-IDF 餘弦與 Jaccard 相似度且原文無多維尺度對齊，見 EK-079）。
- **來源**：同 EK-065、EK-067、EK-079
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic & Antigravity by Google DeepMind。第 (1) 點：已自 `papers` 移除 `2024-taiwanese-mt-resegmentation-tang`，論文頁 `concepts` 同步移除。第 (2) 點：依 EK-067 回原文確認之結果改寫楊鈞凱（2025）段；同時改寫「構詞解析與深層原形還原」段，刪除「未知表面形能準確逆向對映」之過度表述，註明解析需已知詞根。第 (3) 點：依 EK-079 回 Gagnier（2026）原文核對，改述為詞級 TF-IDF 餘弦、頻率 $\ge 5$ Jaccard 相似度與前 500 高頻詞之正規化 Levenshtein 距離，刪除多維度對齊。建立證據表 wiki/evidence/formosan-computational-linguistics.md，概念頁 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現概念頁第 48 行仍稱逐一為已知詞根窮舉深層原形、音韻變化與加中綴形式，再檢查前後綴合法性；這正是本條「問題」欄指出須刪除的正向衍生形描述。雖處理記錄稱已依 EK-067 改寫，實際頁面未完成該處更正；須改為子字串候選詞根挑選與 44 維特徵成對隨機森林循環賽投票，並保留正向書寫形式篩選未納入最終系統的說明後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回楊鈞凱（2025）論文摘要（p. i）、§3.2（pp. 29–32）與 §3.5（pp. 42–45）核對，將概念頁與證據表改為已知詞根集合上的三種子字串比對、合法前後綴檢查及 44 維隨機森林成對投票；並註明書寫形式篩選曾測試但因移除過多正解而未納入最終流程。狀態改為 fixed。

### EK-087 | fixed | concepts/low-resource-machine-translation.md | 關鍵技術路徑 | 原文不符
- **問題**：第 49–52 行將構詞特徵增強寫為詞根嵌入與詞綴嵌入拼接投影 $e(w) = W_{\text{proj}}[e_{\text{root}}(w) \,\|\, e_{\text{affix}}(w)]$ 並歸給游景勝（2021）與金柏毅（2025）；惟游景勝（2021）實驗證實詞根嵌入使 BLEU 暴跌、最佳模型係使用表面詞形搭配 52 維詞綴特徵（見 EK-062），而金柏毅（2025）最佳模型 `FC_ftr_jnt` 係使用雙獨立並聯 Transformer Encoder 分別編碼「詞綴字串形式子詞」與「詞綴組合特徵向量」後於編碼器輸出端串接（見 EK-066）。
- **來源**：同 EK-062、EK-066
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。依 EK-062、EK-066 回原文確認之結果改寫「構詞特徵增強」段：刪除無來源之 $W_{\text{proj}}$ 拼接式，改述游景勝（2021）之布林特徵拼接（含預訓練嵌入下 BLEU 下降之反例）與金柏毅（2025）之 FC_ftr_jnt 雙 encoder；同節「跨語言遷移」段一併依廖恒慶（2023）原文改寫，刪除原文未測量之「降低 OOV 率」「零樣本遷移」。

### EK-091 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 5 | 原文未支持
- **問題**：Card 5 第 1 點（第 135 行）寫 Fragment-Shot「顛覆整句 RAG 定式」，並稱「能遠比整句語意檢索更有效」。原文沒有整句語意檢索的對照實驗：表 1 的比較對象只有零樣本（ZS）與隨機例句（RS，隨機選 16 組句對，§3, p. 3），作者並說明因缺乏合適模型，無法以詞嵌入計算語意相似度（§2, p. 3）；與以句子相似度選例之前人作法僅作定性對照（§7, p. 6）。「顛覆」亦屬評價用詞。建議改為「在無法建立可靠語意檢索模型的情況下，以片段覆蓋選例比零樣本與隨機例句有效」。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`（§2 與 §3 Random-Shot 定義，PDF p. 3；表 1 與 §7，PDF p. 6）
- **發現於**：wiki/log.md [2026-11-09 23:33] audit（Claude Code by Anthropic；第一批卡片回填 C 組只讀論文頁時提出，本代理回原文核對）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。Card 5 第 1 點改為「以片段覆蓋取代整句相似度選例」：限定於缺乏可靠語意嵌入模型之情境，比較對象寫明為零樣本與隨機例句（表 1, p. 6），並註明作者未與整句語意檢索直接比較（§2, p. 3）、僅作定性對照（§7, p. 6）；刪除「顛覆」。證據表增列對應主張，頁面 verification 改回 verified。

### EK-092 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 5 | 過度表述
- **問題**：Card 5 第 1 點（第 122 行）寫「證實簡單的詞彙相似度指標即可自動重現語言學家耗時數十年構擬的分群假說」，未保留原文限定。原文結論為「Among most groups, our results are extremely close to prior scholarship」（PDF p. 7），並明言排灣語「unable to make conclusions regarding the subgrouping」（PDF p. 5），萬山魯凱語兩種指標結果分歧（摘要，PDF p. 1）；同頁 Card 4 第 112–113 行亦已列出這些例外。建議改為「在多數語言中重現既有分群，排灣語無法判定、萬山方言指標分歧」。另第 35 行「開創性研究」屬評價用詞（「首次」為作者自述 first evaluation／first large-scale analysis，可保留並標明為作者主張）。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`（摘要，PDF p. 1；§4.1 Paiwan，PDF p. 5；§5 結論，PDF p. 7）
- **發現於**：wiki/log.md [2026-11-09 23:33] audit（Claude Code by Anthropic；第一批卡片回填 C 組只讀論文頁時提出，本代理回原文核對）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。Card 5 第 1 點改為「在多數語言中與既有分群研究結果相當接近，排灣語無法判定、萬山魯凱語兩指標分歧」，並附原文頁碼（摘要 p. 124、排灣語 p. 128、§5 p. 130）；第 35 行刪除「開創性」，「首次」改寫為作者自述。證據表增列對應主張，頁面 verification 改回 verified。

### EK-093 | fixed | papers/2026-context-volume-rag-domain-shift-setiawan.md | Frontmatter card_line | 過度表述
- **問題**：`card_line`「參考例句給得越多，達豪語翻譯得越好」暗示例句越多效果越好、單調上升。原文表 5 顯示詞級檢索在 N=10（有效例句約 137 句）達 35.28 chrF++ 後，N=15、N=20 回落至 35.16 與 34.22；原文主張的是「語境容量比檢索演算法更影響效能」，並非越多越好。同頁 Card 3 第 75 行亦已寫明「語境容量並非單調無限上升」。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Context Volume Drives Performance Tackling Domain Shift in Extremely.pdf`（表 5，p. 100；§6 結論，p. 94）
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`card_line` 改為「讓大模型參考例句，修補跨領域的達豪語翻譯」（19 字，描述本篇做了什麼，不含單調之斷言），重建首頁。

### EK-094 | fixed | papers/2024-sora-world-simulator.md | Card 4 | 原文不符
- **問題**：Card 4 第一點寫 DiT「在橫跨三個數量級的訓練算力區間內呈現單調緊密的負相關冪律（相關係數逾 $-0.95$）」。原文圖 8 為 12 種設定之「模型 Gflops」（單次前向運算量，0.3 至 118.6 Gflops）與 FID-50K 之相關，係數為 $-0.93$，並非訓練算力，亦未稱冪律。同點「ADM-U 的 3.94」在原文表 3 為 ADM-G、ADM-U 合用之 512 結果。
- **來源**：Peebles & Xie (2023), arXiv:2212.09748v2，圖 8（p. 8）、§4（p. 5）、§5（p. 8）、表 3（p. 9）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為模型 Gflops 與 FID-50K 相關係數 $-0.93$（圖 8，p. 8），256 由 LDM 之 3.60 降至 2.27、512 為 3.04（ADM-G、ADM-U 為 3.94），證據表增列。

### EK-095 | fixed | papers/2024-sora-world-simulator.md | Card 4 | 原文不符
- **問題**：Card 4 第二點寫「1×、4×、16×、32× 訓練算力對照」，並逐級描述「畫面模糊且物體結構瞬間崩解」「初具物體形狀但運動違反物理」「自發湧現逼真的流體力學波浪、光影反射……」。OpenAI 報告之影片標籤只有 Base compute、4x compute、32x compute 三組，文字僅寫「Sample quality improves markedly as training compute increases」；16× 與各級描述皆無出處。證據表原列「$1\times$ 至 $32\times$」亦判為符合。
- **來源**：Brooks et al. (2024), OpenAI 技術報告 §Scaling transformers for video generation（https://openai.com/index/video-generation-models-as-world-simulators/ ，2026-11-10 讀取頁面文字與影片標籤）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為基礎、4 倍、32 倍三組樣本與報告原句，註明只有影片樣本、無定量指標；證據表該列改判核實更正。

### EK-096 | fixed | papers/2024-sora-world-simulator.md | Card 4 | 過度表述
- **問題**：Card 4 第三點寫「對比實驗證明……頻繁出現人物無頭、主體出框」「主體完整居中率與電影級構圖品質顯著躍升」。原文為樣本之質性比較：方形裁切版本「sometimes generates videos where the subject is only partially in view」，Sora「have improved framing」；無「居中率」等量化指標。
- **來源**：OpenAI 報告 §Improved framing and composition；Liu et al. (2024), arXiv:2402.17177，圖 6 與正文，p. 7。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為「後者有時生成主體只部分入鏡的畫面，Sora 的取景較佳」，註明為質性比較。

### EK-097 | fixed | papers/2024-sora-world-simulator.md | Card 4 後續 | 歸因／版本錯置
- **問題**：後續研究寫「Kang et al. (2024, *ICML*, ...)」，並稱其發現模型在「牛頓力學碰撞動量守恆、流體質量守恆與複雜剛體因果交互」上發生「穿模或憑空生成」。該文為 arXiv:2411.02385（2024 年 11 月），發表於 ICML 2025；摘要所述為二維物體運動與碰撞模擬之分布內、分布外與組合泛化測試，未提流體質量守恆或穿模。
- **來源**：arXiv:2411.02385 摘要與 comment 欄（「ICML 2025」），2026-11-10 以 arXiv API 讀取。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫出處為 arXiv 2024 年 11 月、ICML 2025，內容依摘要：分布內完美泛化、組合泛化隨規模改善、分布外失敗，模型模仿最相近案例，作者認為單靠擴大規模不足以發現物理定律。

### EK-098 | fixed | papers/2024-sora-world-simulator.md | Card 1 | 原文未支持
- **問題**：Card 1 寫「早期的影片生成模型（如初代 Runway Gen-2、Pika）大多只能生成 2 至 4 秒、固定正方形裁剪……」並稱 Sora 由 Peebles 與 Brooks「領軍開發」。OpenAI 報告原文為過去做法「typically resize, crop or trim videos to a standard size—e.g., 4 second videos at 256x256 resolution」，未點名任何產品；報告僅列作者，無「領軍」之述。
- **來源**：OpenAI 報告 §Variable durations, resolutions, aspect ratios；作者列（Tim Brooks, Bill Peebles, ...）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改依報告原文敘述過去做法與一分鐘影片，作者改寫為「Brooks, Peebles et al., 2024；Peebles 亦為 DiT 之第一作者」。

### EK-099 | fixed | papers/2024-sora-world-simulator.md | Card 3 | 原文未支持
- **問題**：Card 3 第 3 節稱「Peebles & Xie (2023) 與 OpenAI 實驗共同證實」生成品質「嚴格受……總訓練算力 $C$ 的冪律支配」，並列區塊公式 $\mathcal{L}_{\text{val}}(C) \propto C^{-\alpha}$ 與 $G \propto N \cdot d^2 + N^2 \cdot d$。DiT 原文只報告模型 Gflops 與 FID 之強負相關（圖 8），OpenAI 報告只有三組算力之樣本；兩者皆無此冪律或公式。
- **來源**：Peebles & Xie (2023) 圖 8，p. 8；OpenAI 報告 §Scaling transformers for video generation。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。第 3 節改題「算力與生成品質」，改寫為兩來源實際所述，刪除冪律公式與運算量估算式。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：max，依使用者指示）。回查 OpenAI 官方報告與目前頁面：報告明言未提供模型及實作細節；目前 Card 3 仍列 patch 數量式，論文頁仍列 patch embedding 及 clean-patch diffusion 目標式，報告未見這些公式。舊冪律與運算量式已刪，現存公式仍須移除或明確標為 Wiki 推導並補一手依據，因此重開為 open。
- **總核**：2026-11-10，Codex by OpenAI（GPT-6）。原問題的冪律與運算量式已移除，故本條維持 fixed；複核指出的其他公式確實仍須處理，已明確併入同頁的 EK-035，避免重複計數。依現行公式規範，非原文公式不可僅加註 Wiki 推導後仍保留為區塊公式；必要的推導須改以行內公式或文字呈現，並標明假設與依據。

### EK-100 | fixed | papers/2024-sora-world-simulator.md | Card 4 後續 | 未能核實
- **問題**：後續研究第一點列出快手 Kling、智譜 CogVideoX、騰訊 HunyuanVideo、阿里 Wan2.1 與 Meta Movie Gen，稱其遵循「3D-VAE ＋ 時空圖塊 ＋ DiT ＋ 3D-RoPE ＋ 流匹配」範式並「全面驗證時空 DiT 架構作為視覺基座模型的普適性」，未附任何出處。
- **來源**：Yang et al. (2024) arXiv:2408.06072；Polyak et al. (2024) arXiv:2410.13720；Kong et al. (2024) arXiv:2412.03603；Wan Team (2025) arXiv:2503.20314（arXiv 摘要）。快手 Kling 無公開技術報告。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。以 arXiv API 取得 CogVideoX、Movie Gen、HunyuanVideo、Wan 四份技術報告之摘要，改寫為各報告自述之設計並附 arXiv 編號；刪除無技術報告之 Kling，以及「遵循同一範式」「全面驗證」等原頁說法，註明不據此推論與 Sora 之承接關係。

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

### EK-108 | fixed | papers/2017-attention-is-all-you-need.md | 證據表第 11–12 列 | 原文不符
- **問題**：證據表第 11 列把 WMT 2014 翻譯結果與路徑長度比較之出處寫作「§5.1, §5.2」，第 12 列把 WSJ 句法剖析寫作「§5.3」。原文 §5 為訓練設定（§5.1 訓練資料、§5.2 硬體與排程、§5.3 最佳化器）；路徑長度比較在 §4 Table 1，翻譯結果在 §6.1 Table 2，句法剖析在 §6.3 Table 4。
- **來源**：`raw/2017-attention-is-all-you-need.pdf`（Vaswani et al. 2017），§4 p. 6、§5.2 p. 7、§6.1 p. 8、§6.3 p. 9。
- **發現於**：第二批卡片回填 C 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。兩列改為正確節次與頁碼，數值不變。

### EK-109 | fixed | papers/2017-attention-is-all-you-need.md | 開頭引言 | 歸因／版本錯置
- **問題**：標題下之開頭引言「當模型不再被迫一個字一個字地順著時間軸緩慢爬行……」加了引號，卻未註明為 Wiki 撰寫，讀者會以為出自原文；原文無此句。`paper-card-writer` 之 `references/paper-page.md` 第四節第 1 條要求加註。
- **來源**：`raw/2017-attention-is-all-you-need.pdf` 全文無此句（引言為中文修辭，原文為英文）。
- **發現於**：第二批卡片回填 C 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。引言後加「（本頁引言為 Wiki 撰寫，非原文）」，重建論文頁原型。

### EK-110 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | 證據表第 13 列 | 原文不符
- **問題**：證據表第 13 列列出之模型為「DeepSeek-R1-Distill-Qwen-14B」，出處寫「§3.3, pp. 5–6」。原文為 DeepSeek-R1-Distill-Llama-70B，以 GPT-4o mini 為基準，另比較 Llama 3.1-70B 與 Gemma 3-27B；模型列於 §3.4，後編輯模組在 §3.2（皆 p. 5），§3.3 為語料收集。論文頁第 63、94 行之模型名正確。
- **來源**：`raw/my-focus/英文論文/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`（Eng. Proc. 2025, 120, 52），§3.2 與 §3.4，p. 5。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改正模型名與節次。

### EK-111 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | Card 5 | 原文未支持
- **問題**：Card 5 第一點（第 115 行）稱「以高精確的靜態詞典解決 80% 的關鍵詞錨定，以向量庫處理 20%」，並稱「向極低資源 NLP 界證實」。原文未見 80%、20% 之分配數字。
- **來源**：同 EK-110 之 PDF，全文搜尋「80%」「20%」無結果。修正時改用原文結果節之實際數據，或刪去比例。
- **發現於**：第二批卡片回填 B 組回報，協調者以全文搜尋確認（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。再次全文搜尋確認無 80%、20% 後，刪去比例、「證實」與第二點「徹底克服」；Card 5 改寫為作者結論（§4–§5, p. 7，並註明原文未報告各模組使用比例）、資料取得條件（p. 8）、作者明列之限制與未來方向（§5, p. 7）。證據表登記。

### EK-112 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 3 | 原文不符
- **問題**：Card 3 第 75 行把開放經濟菲利浦曲線寫成國內通膨對「產出缺口」$y_t - y_t^n$、$y_t^* - y_t^{*n}$ 之關係，並標「式 3.11 / 3.19」；原文式 (3.19) 之產出項為相對穩態之對數偏離 $\hat{Y}_t$、$\hat{Y}^*_t$，且另有衝擊項 $-\xi \omega q_t$。第 83 行利率規則寫成 $\phi_y (y_t - y_t^n)$；原文式 (1.23) 為 $\hat{\imath}_t = \bar{\imath}_t + \phi_\pi \pi_t + \phi_y \hat{Y}_t$。
- **來源**：`raw/2007-woodford-inflation-dynamics.pdf`，式 (3.19) 於 PDF 第 58 頁，式 (1.23) 於 PDF 第 13 頁。
- **發現於**：第一、二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。逐式回原文核對後：(3.19) 改為原文式，並補 $\kappa_H$、$\kappa_F$ 之原文定義（PDF p. 58 未編號式）；(1.23) 改為原文式；(1.27) 左側原誤寫 $\hat{\pi}_t$，改為原文之 $\pi_t$，期望算子改為原文之 $E_t$。$\kappa_F$ 之說明原寫「透過進口要素或中間財成本溢出」、「等同於可被抵銷的外生衝擊」，改依 PDF p. 57 寫為 $\sigma > 1$ 時 $\kappa_F < 0$、與 global slack 論點方向相反。Card 3 第 3 點「即使菲利浦曲線極為平坦，央行仍可精確錨定通膨」與第 85 行引自 Woodford (2003) 之確定性條件（不在本篇）一併刪除，改寫為原文式 (1.25)–(1.26) 之向前求解條件。證據表逐式登記式號與 PDF 頁碼。

### EK-113 | fixed | papers/2025-deepseek-r1.md | Card 4 與證據表第 16 列 | 歸因／版本錯置
- **問題**：Card 4 第 85 行與證據表第 16 列稱 R1-Zero 之 AIME 2024 pass@1 由 15.6% 升至 71.0%，第 85 行並稱「與 OpenAI o1-0912 持平」；第 86 行稱「8,000 多個強化學習訓練步」。本頁引用之 Nature 版原文為 77.9%，訓練共 10,400 步（8.2k 步出現明顯躍升）。證據表同一列寫 10,400 步而論文頁寫 8,000，二者也不一致。71.0% 與 o1-0912 之比較疑為 arXiv 初版之數字，修正時須一併確認 cons@16 之 86.7% 是否為 Nature 版數字。
- **來源**：`raw/2025-deepseek-r1.pdf`，PDF 第 3 頁（10,400 steps；8.2k step）、第 4 頁（15.6% → 77.9%）。
- **發現於**：第一、二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。回原文核對：R1-Zero AIME 2024 pass@1 改為 15.6% → 77.9%（§2.3, p. 4），刪除與 o1-0912 之比較；訓練步數改為共 10,400 步、第 8.2k 步長度上限提高後躍升（§2.1, p. 3）；cons@16 之 86.7% 經確認為正式版數字（p. 5）。另刪除 Card 4「R1 之 cons@64 與 o1-1217 持平」（原文無此比較），Table 8 各數字逐一附上 o1-1217 對照值；章節 §2.2 改為 §2.3。證據表依正式版逐項重建，數字逐一寫出表列與欄位。

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

### EK-116 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 3 | 原文未支持
- **問題**：Card 3 第 65–66 行之 $\hat{y}_{\text{base}} = \operatorname{NMT}(x)$ 與 $\hat{y}_{\text{final}} = \operatorname{LLM}_{\text{CoT}}(\ldots)$ 為 Wiki 自擬之流程示意，原文沒有任何公式，頁面也未標明為示意。頁面有區塊公式，卡片因而無法依 Card 3 無公式模式撰寫。
- **來源**：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf` 全文無編號公式。
- **發現於**：第二批卡片回填 B 組回報，協調者以全文搜尋確認（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。回原文確認全文無編號公式、流程只以文字與 Figure 1 說明後，刪除兩條自擬區塊公式，改以文字依序說明流程（§3.1–§3.2）；頁首「Card 3 之數學式為流程示意表示」改為「全文無編號公式」。證據表登記。

### EK-117 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 5 | 原文不符
- **問題**：Card 5 第 115 行稱「證明……利用現成小型開源 NMT 模型搭配輕量 API RAG 後編輯即可超越 54B 巨型單體模型」。原文 FLORES 實驗以 NLLB-54B 本身為初譯模型（baseline MT model），再以 LLM 後編輯，平均比 NLLB-54B 高 2.8 ChrF++；並非以小型 NMT 超越 54B 模型。
- **來源**：同 EK-116 之 PDF，摘要 p. 1、§4.2 p. 5、Table 2 p. 6。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。刪去 Card 5 兩點無出處之「打破壁壘」「證明……超越 54B」敘述，改寫為：FLORES 以 NLLB-54B 本身為初譯再後編輯、平均高 2.83（表 2）；並依新論文需求補記原文公開之程式與系統、作者明列之限制（含易用性研究僅兩位共同作者）與 §6 之未來方向（提示最佳化、離線部署等），各附位置。

### EK-118 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 3 | 原文未支持
- **問題**：Card 3 第 64 行之 $D_{\text{norm}}(s_1, s_2) = \operatorname{LD}(s_1, s_2) / \max(|s_1|, |s_2|)$ 寫明除以較長字串之長度。原文只說「normalized by word length」，未指明取較長者，也未寫出公式；證據表第 12 列未登記此式。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`，§2.3（PDF 第 2 頁，論文集 p. 125）。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。回原文確認全文無編號公式後，刪除該區塊公式，改以文字照原文寫「以詞長正規化，原文未指明以哪一個詞的長度」；行內之 Jaccard 與 sublinear_tf 式改為文字並註明原文未列式。頁面已無區塊公式，卡片改用無公式模式。證據表登記。

### EK-119 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 5 | 過度表述
- **問題**：Card 5 第二點（第 123 行）稱「證明南島語各語族不能一概而論」，排灣語與賽德克語「極適合進行多方言聯合訓練與跨方言遷移」，泰雅語與魯凱語「跨方言遷移容易引發負遷移」。原文為共有核心詞比例高者是「good candidates for cross-dialect model transfer」、「transfer learning should be tested」，獨有詞比例高者建議方言專屬模型或微調；未稱證明，也未談負遷移。
- **來源**：同 EK-118 之 PDF，PDF 第 3 頁（§3.1）、第 7 頁（§4）。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。Card 5 第二點改照原文：共有核心詞高者「是跨方言模型遷移的好候選」「應測試遷移學習」，獨有詞高者建議方言專屬模型或微調，並註明原文未做遷移實驗、未談負遷移（§3.1, p. 126；§4.1, p. 130）。另依新論文需求補記公開程式碼、作者明列之限制、四點建議與 §5 未來方向，各附位置。

### EK-120 | fixed | papers/2024-fault-tolerant-quantum.md | Card 3 與 Card 4 | 原文不符
- **問題**：Card 3 第 53 行寫相干時間 $T_2 > 1.5\,\text{s}$，原文為 T2 > 1 s。Card 4 第 96 行稱 d = 7 時「總計動用約 200 個物理原子」，原文圖 2 標示每個邏輯貝爾對所用物理量子位元數，d = 3、5、7 依序為 26、74、146。
- **來源**：`raw/2024-fault-tolerant-quantum.pdf`（Bluvstein et al. 2024），PDF 第 2、12 頁（T2 > 1 s）、第 3 頁圖 2（146）。
- **發現於**：第一、二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。以正式版（PMC10830422）與 arXiv v1 核對後，$T_2$ 改為 $> 1$ s；Card 4 改寫為每個邏輯貝爾對使用 26、74、146 個物理位元（Fig. 2d），並補上相關解碼與傳統解碼之差異、初態製備非容錯等限制。證據表登記。

### EK-121 | fixed | papers/2024-fault-tolerant-quantum.md | Card 3 | 原文未支持
- **問題**：Card 3 四組區塊公式（第 64–67 行里德堡哈密頓量、第 75 行穩定子碼空間、第 79 行橫向 CNOT、第 87 行邏輯錯誤率標度）皆未登記於證據表（證據表 Card 3 只有三區架構一列）；B 組回報其中三組原文找不到。原文以文字描述橫向 CNOT 與穩定子，未見以這些形式寫出之公式。
- **來源**：同 EK-120 之 PDF；修正時逐式回原文正文與 Methods 確認，找不到者刪除或標明為教科書式背景。
- **發現於**：第二批卡片回填 B 組回報，協調者核對證據表（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。逐式回原文正文與 Methods 核對：里德堡哈密頓量、穩定子碼空間、橫向 CNOT 張量積三式原文沒有，刪除；邏輯錯誤率標度在 Methods 只是行文中之 $\propto (p/p_{\text{th}})^{(d+1)/2}$（引 ref. 24），改為行內並刪去原文沒有之 $\Lambda$ 等式。另補入 Methods「Correlated decoding」之混合整數規劃（未編號式），為本篇相關解碼之原文公式，證據表登記位置。同時改正閘時原子間距為 $\lesssim 2\,\mu$m（Extended Data Fig. 1 圖說）。

### EK-122 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 3 | 原文未支持
- **問題**：Card 3 第 53–58 行之 $\mathcal{D}_{\text{clean}} = \{ (x_i, y_i) \mid \operatorname{ValidText} \land \operatorname{RatioFilter} \}$ 為 Wiki 自擬，原文沒有編號公式；且拆成兩行 aligned 片段，各行都不完整。原文過濾規則為文字敘述：兩側皆有兩個以上詞元時計算目標對來源之詞元比 r，r ≤ 0.2 或 r > 8.0 者捨棄。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`，PDF 第 4 頁（LREC 2026 論文集 p. 3448）。
- **發現於**：第二批卡片回填 C 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪除 Card 3 自擬之 $\mathcal{D}_{\text{clean}}$ 集合式，過濾規則依 §3.3（p. 3448）改以文字敘述；同章另一條自擬之語言代碼集合式一併改為文字列表（EK-174）。卡片 Card 3 採無公式模式。證據表登記原文無編號公式。

### EK-123 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 1、Card 5 與 Card 6 | 過度表述
- **問題**：Card 1 第 33 行稱本篇「具有里程碑意義」；Card 5 第 131 行稱「徹底解決了國際研究團隊無法取得標準化臺灣南島語資料的歷史痛點」並稱「首度大規模」；Card 6 第 147 行稱「完美聯動」、將產出「全球第一套」標註語料庫並「直接將研究成果推向頂會高度！」。原文無上述評價，「完美」屬禁用評價詞，驚嘆號亦不合學術語氣。另第 145–147 行寫到使用者之研究規劃，撰寫卡片時須依 `paper-card-writer` 第二節第 13 條，不得透露碩論題目、資料或結果。
- **來源**：同 EK-122 之 PDF 全文。
- **發現於**：第二批卡片回填 C 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。Card 1 刪去「里程碑意義」，改照摘要與 §1；Card 5 依新論文模式改記原文公開之資源、§7 限制與 §6 未來工作，刪去「徹底解決……歷史痛點」「首度大規模」「標準化工程範本」；Card 6 刪去「完美聯動」「全球第一套」「推向頂會高度！」與第一人稱之研究規劃，改寫為研究方向之延伸思考，不寫碩論題目、資料或結果。卡片 Card 6 不提碩論。

### EK-130 | fixed | papers/2023-atayal-truku-morphology-dai.md | Card 3 | 原文不符
- **問題**：Card 3 之前綴機率公式寫作 $P_{\text{uni}}(\text{pfx}) = \prod_{i=1}^{m} P(x_i), \qquad P_{\text{bi}}(\text{pfx}) = \cdots$。原文兩式皆寫作 $P(\mathit{pfx})$，以「一元機率」「二元機率」文字區分；uni、bi 下標為 Wiki 所加，與原文寫法不同。式子內容（上下限與條件機率）與原文相同。
- **來源**：`raw/my-focus/學長姐論文/泰雅語與太魯閣語構詞結構之自動解析_戴晟哲.pdf`，§3.5，p. 29（PDF 頁面影像）。
- **發現於**：撰寫卡片前回原文抽查時發現（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改為與原文相同之 $P(\mathit{pfx})$ 兩行 aligned，並以文字註明第一行為一元機率、第二行為二元機率；證據表該列同步改寫。

### EK-170 | fixed | papers/2024-finnish-northern-sami-mt-saleva.md | Card 3 與 Card 5 | 原文不符
- **問題**：（1）Card 3 區塊公式之 KL 項寫作雙豎線 D_KL(p_LM(y) ‖ p_NMT(y|x))，原文 §3.2 為單豎線 DKL(pLM(y)|pNMT(y|x))，且該式為正文內嵌式、無式號，論文頁未註明位置。（2）Card 5 漏記原文公開之資源與作者所述之方向：原文 §1 寫明全部程式與資料（含正譯與回譯輸出）公開於 GitHub `j0ma/sami-translation`；§5 指出方法能否推廣到其他語言為關鍵問題、因運算資源所限未能回答；§4.3 推測調整超參數後語言模型先驗與正譯或可並用。論文頁與證據表均未記載。另證據表第 16 列只寫「表中各 BLEU／chrF」，未逐一列出數值。
- **來源**：`raw/my-focus/報告論文題材/2024.findings-acl.768.pdf`，§1（p. 12949）、§3.2（p. 12950）、§4.3 與 §5（p. 12953）、表 1、3、4、5（pp. 12950–12953）。
- **發現於**：第二批卡片回填 C 組回報與第三批撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。回原文核對後：公式改照原文作單豎線，拆成兩行 aligned 並註明「§3.2 正文內嵌式，無式號，p. 12950」；Card 5 補列公開資源（§1）與作者所述之未來方向（§5、§4.3），作者自述限制補頁碼；證據表逐一列出表 1、3、4、5 數值並補登上述各項。另依 `cover.md` 第二節第 7 條改寫 `card_line`（原句切不出 3 行以內之封面斷行）。頁面 `verification` 改為 `partial`。

### EK-150 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 4 | 原文不符
- **問題**：（1）Card 4 第 94 行標題寫「要素市場全球化（$\tilde{\kappa}_H \to 0$）之極限穩健性證明」，並稱國內產出缺口對邊際成本之影響趨近於零、名目工資與物價須經匯率與利率平價錨定。原文 §3.3 為 $\tilde{\kappa}_H \equiv \kappa(1-\gamma) + \xi\gamma$，不趨近於零；只有 $\nu + \sigma^{-1} > 1$ 時才小於封閉經濟之 $\kappa$，在 Rotemberg & Woodford (1997) 校準下反而較大，作者結論為整合可能使菲利浦曲線變陡；原文未談經匯率與利率平價錨定。（2）第 92 行之 $\beta = 0.99$ 原文未寫；「CPI 通膨初期反應因匯率傳導而更為靈敏」之「因匯率傳導」原文未說，且漏了作者「至少在此校準例中」之限定。（3）第 93 行稱外國衝擊「完全可以被本國貨幣政策有效對沖」，原文結論為本國央行仍可單獨穩定本國通膨、不需國際協調。（4）第 96–99 行把早於本篇之 Eggertsson & Woodford (2003)、Hall (2005) 列為「後續」；Eggertsson & Woodford 頁碼誤為 139-211（Crossref 為 139-233）；Smets & Wouters (2007) 稱成為 FRB/US 等央行標準系統、Eggertsson & Woodford「直接指導」2008 與 2020 年之政策、Hall「解決了 Shimer 謎題」，三者摘要皆無此說。
- **來源**：`raw/2007-woodford-inflation-dynamics.pdf`，PDF pp. 14、24、60–61、71–73、75；doi:10.1257/aer.97.3.586、doi:10.1353/eca.2003.0010、doi:10.1257/0002828053828482（Crossref 書目與摘要）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫 Card 4 四點（參數、Figure 6、外溢與結論、全球要素市場之 $\tilde{\kappa}_H$），刪去 $\beta = 0.99$；相關研究改標「相關研究（非本篇成果）」並註明兩篇早於本篇，各附 DOI，描述改依摘要，改正頁碼。證據表逐項重登。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。原問題包括將早於本篇的研究誤列為後續；論文頁已改為相關研究，但[證據表](evidence/2007-woodford-inflation-dynamics.md) Card 4 的同一列仍將 Eggertsson & Woodford (2003)、Hall (2005) 與 Smets & Wouters (2007) 整列標為「後續研究」，與該列的「非後續」說明矛盾。證據表類型的處置依 TD-007 待決，本次未修改證據表。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。證據表將本頁按主題選取三篇相關研究的歸類明示為 Wiki 詮釋，註明 2003 與 2005 兩篇早於本篇、不代表後續或承接關係；各研究仍各引其來源。此頁其他 open 問題亦已處理，verification 改為 partial。

### EK-151 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 5 | 原文未支持
- **問題**：Card 5 三點（本篇與 Woodford 系列理論「終結了貨幣主義舊框架」、「直接啟發」聯準會 2012 年點陣圖、「及時化解政策恐慌，證明……」）均無出處；本篇發表於 2007 年，依 `wiki-content-audit` 須有至少 3 筆附出處之後續研究，頁面一筆也沒有（Card 4 所列兩篇早於本篇）。
- **來源**：頁面第 104–106 行；後續研究以 Crossref 與 OpenAlex 核對：doi:10.1111/j.1468-2362.2009.01248.x、doi:10.1016/j.jmacro.2010.04.002（摘要依 doi:10.24149/gwp33）、doi:10.1111/j.1468-2362.2010.01268.x、doi:10.24149/gwp300，四篇 OpenAlex 皆列為引用本篇（W2106451667）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪去三點無出處之影響敘述，改列四篇檢驗「全球產出缺口」假說之後續研究（Calza 2009、Milani 2010、Ihrig 等 2010、Auer 等 2017，後者結論相反），各附 DOI 與摘要所載之結果，並列 2026 年獎項；證據表登記四列「後續研究」。

### EK-171 | fixed | papers/2026-tao-filipino-nmt-macayan.md | Card 5 與證據表第 17 列 | 原文不符
- **問題**：（1）證據表第 17 列只寫「表 3 各數值」，未逐一列出數值與表列、欄位。（2）Card 5 漏記原文所述之未來工作與部分限制：原文 §7 Recommendations 列出進階正規化、更好硬體與更大模型、子詞斷詞處理罕見詞與構詞、與母語者及專家合作；Limitations 另指出只研究達悟語→他加祿語一個語言對、經文不能代表一般句構、未做人工評估且指標測不到比喻與偏誤。論文頁亦未說明原文是否公開資料或程式（原文未提及）。
- **來源**：`raw/my-focus/報告論文題材/2026.loresmt-1.2.pdf`，表 3（p. 33）、§7 與 Limitations（p. 34）。
- **發現於**：第二批卡片回填 C 組回報與第三批撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。回原文核對後：證據表第 17 列改為逐一列出表 3 之 BLEU、chrF、Median SBERT 各 6 格數值（皆與論文頁 Card 4 表相符）；Card 5 補列 §7 未來工作、Limitations 所列限制與頁碼，並註明原文未提及公開資源；證據表同步補登。頁面 `verification` 改為 `partial`。

### EK-172 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 1、Card 2、Card 5 與證據表第 15 列 | 原文未支持
- **問題**：（1）Card 2 第 1、2 點稱整句檢索在小語料中「命中率低、強制檢索出的整句往往只有少數不相關的高頻停用詞重疊」，並稱辭典提示「無法提供屈折變化、黏著語綴、詞序排列與焦點選擇的上下文示範」，原文 §1–§2 沒有這些說法；原文所述困難為大模型對小語言及其變體認識有限、少於 13,000 句對不足以訓練（Gu et al. 2018），以及拉定語沒有合適之語意嵌入模型。（2）Card 1 稱本篇「證明」大模型能以推理補償數據之不足，Card 5 第 2 點以圖 2 單一例子稱推理模型能「自發跨越兩跳完成語素映射，證明推理能部分補償數據匱乏」，且未交代 PF（20.94）仍低於有直接例句時之 FS（28.60）；原文摘要與結論之措辭為「更善用檢索知識」「讓模型超越例句而泛化」。（3）Card 5 漏記原文公開之程式碼、檢索語料與 PyPI 套件、Limitations 所列限制與 Future Work。（4）證據表第 15 列只寫「Table 1 之 BLEU 分數」，未逐一列出數值。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`，摘要與 §1（p. 1）、§2（pp. 2–3）、註 1（p. 3）、表 1（p. 6）、Conclusion 與 Future Work（p. 8）、Limitations（p. 9）。
- **發現於**：第三批卡片回填撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。回原文核對後：Card 2 依 §1–§2 改寫為大模型對小語言掌握有限、微調資料不足、拉定語無嵌入模型而無從語意檢索；Card 1「證明」改為摘要之發現；Card 5 第 2 點改述 PF 與 ZS、FS 之數值關係並引結論原句；Card 5 補列公開資源、限制與未來工作；證據表逐一列出表 1 四個方向（另含 Gherdëina→Italian GPT-4o 兩格）之數值與信賴區間，補登上述各項。頁面 `verification` 改為 `partial`。

### EK-152 | fixed | papers/2025-deepseek-r1.md | hook、Card 1 至 Card 3 與 Card 6 | 過度表述
- **問題**：（1）`hook` 與 Card 1 稱 R1-Zero「首次公開證明」「首次向全球嚴格證明」，正式版原文未稱首次；Card 1 稱 R1「徹底解決」可讀性與中英夾雜、「追平 OpenAI o1 正式版」，原文 §6 仍列語言混雜為限制，Table 8 中 R1 與 o1-1217 互有高低；Card 1 與 Card 4 稱思考長度達「上萬 Token」，原文寫 hundreds to thousands。（2）Card 2 稱 PPO「使訓練顯存與通訊開銷翻倍」、Card 3 稱 GRPO「大幅省去一半顯存」，原文 Supplementary A.3 只說價值模型帶來顯著記憶體與運算負擔；Card 2 稱神經獎勵模型「導致訓練在中途崩潰」，原文只說易遭獎勵駭客利用。（3）Card 3 區塊公式：KL 估計量式末加了原文沒有之「≥ 0」並稱「恆為非負且低方差」；目標函數之期望寫法與原文式 (1) 不同；獎勵寫成 Wiki 自擬之 $r_i = R_{\text{acc}}(q, o_i) + R_{\text{fmt}}(o_i)$，原文為式 (4)。（4）Card 4 稱 Table 2 之頓悟時刻「重新檢驗積分符號」，原文例題為方程式求實根之和；Card 3 稱蒸餾「1.5B 至 70B」皆優於直接強化學習，原文只在 Qwen2.5-32B 上對照。（5）Card 6 稱強化學習「首次在六千億參數規模上穩定釋放威力」，無出處。（6）`title_zh` 冠以「推理運算擴展定律」，原文標題與內文均未提出此定律。
- **來源**：`raw/2025-deepseek-r1.pdf`（Nature 版全文與補充資料）：§2.1–2.3, pp. 3–5；§6, pp. 10–11；Supplementary A.3, pp. 14–16；Table 8, p. 41；Table 16, p. 61。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句；三條區塊公式改照原文式 (1)–(3) 並補式 (4)，刪去「≥ 0」；`title_zh` 與內文標題刪去「與推理運算擴展定律」。證據表逐式登記式號與頁碼。

### EK-153 | fixed | papers/2025-deepseek-r1.md | Card 4 後續與 Card 5 | 原文未支持
- **問題**：Card 4「後續領域關鍵證據」稱本篇刊於 Nature 後「成為首篇公開完整強化學習動態與訓練配方的主流推理大模型論文」、GRPO 加可驗證獎勵「迅速成為全球……標準範式」，無出處，且 Nature 刊登是本篇本身而非後續研究。Card 5 三點（「開闢測試時運算擴展定律新維度」「證實……解鎖全新的智慧增長曲線」「開源對閉源護城河的歷史性追平」）皆無出處。本篇發表於 2025 年，依 `wiki-content-audit` 須記載原文公開之資源、作者明列之限制與未來工作，頁面皆未記載。
- **來源**：頁面第 95、100–102 行；原文 §6, pp. 10–11（限制與未來方向）、Supplementary I, pp. 65–66（公開權重、蒸餾模型與程式）、Supplementary H.3, p. 65（原文自述啟發之後續探索）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪去 Card 4 後續段與 Card 5 三點無出處之敘述；Card 5 改記原文公開之權重、蒸餾模型與程式，作者明列之能力限制、純強化學習之挑戰與未來方向，各附節與頁碼；註明原文自述之後續探索本頁未逐篇查核、不列為後續研究。證據表登記各列。

### EK-131 | fixed | papers/2022-formosan-say-verbs-hsieh.md | Frontmatter card_line 與 hook | 原文不符
- **問題**：`card_line` 寫「比較族語的「說」，發現多半也能表示「想」」，`hook` 寫「發現它們普遍從「說」延伸到「想」」。原文結論為所有台灣南島語的「說」動詞都有從述說語義場跨到認知語義場（「說」→「想」）的延伸；「多半」「普遍」比原文弱，與原文不符。
- **來源**：`raw/my-focus/台灣相關論文/台灣南島語「說」動詞語義現象初探_謝富惠.pdf`，第 5 節，p. 84（「所有的台灣南島語都同時呈現『同一語義場』以及從『述說語義場』跨到『認知語義場』的語義延伸」）。
- **發現於**：撰寫卡片前回原文抽查時發現（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`card_line` 改為「比較族語的「說」，發現都能表示「想」」，`hook` 之「普遍」改為「都」；證據表增列一列。

### EK-173 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 4 與 Card 5 第 3 點 | 原文不符
- **問題**：（1）Card 4 實驗設定稱檢索語料為「Gherdëina–Italian（18,485 句）」，原文無此數，原文為 Val Badia–Italian 18,140 句、Gherdëina–Italian 19,971 句，另對齊出 Val Badia–Gherdëina 14,953 句；證據表同列亦誤。（2）稱 BLEU 以「平均值 ± 標準差」報告，原文表 1 標題為平均值與信賴區間。（3）表 3 相關係數加註「p < 0.05」，原文僅以星號標示、未註明顯著水準。（4）「原文指出的局限性」7%–9% 一項寫作「無效拼寫或非標準詞」並標 Limitations p. 9，原文為 §7 p. 7「syntactically not valid in the target language」；Figure 2 一項寫成提示偏移「即」使 GPT-4o 找不到例句，原文為「may have caused」。（5）Card 5 第 3 點稱譯入高資源語言時「複雜提示無效甚至引入干擾」，原文為只有些微改善、FS 僅對 o1-mini 與 Llama-3.3 顯著，部分情形零樣本最好，未提干擾。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`，§4（pp. 4–5）、§6（p. 5）、表 1 標題與表 2（p. 6）、表 3（p. 7）、§7（p. 7）、Conclusion（p. 8）。
- **發現於**：第三批卡片回填交付稿撰寫時再抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。以原 PDF 頁面影像核對後，依原文改寫上述五處，表 2 補列 ZS、FS、PF 三種字元數與 DeepSeek-R1 推論秒數；證據表同步更正並逐一列出數值。卡片檔不受影響（Card 4 四個數字均取自表 1）。`verification` 維持 `partial`。

### EK-174 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 2、Card 3 與 Card 4 | 原文不符
- **問題**：（1）Card 4 稱族語－英語 95,809 句對「涵蓋 4 種具備英語對齊之語言：阿美語 36,039、布農語 25,627、魯凱語 13,010、泰雅語 21,133 句對」，並稱族語－華語「從阿美語 64,888 句對至邵語 21,795 句對」，原文表 2 無這些數字；表 2 每種語言都列有英語句對，只有四種語言之英語資料足以訓練模型。表 2 位置誤記為 p. 3449（實為 p. 3450）。（2）Card 2 將「宗教文獻」列為來源，原文 §2 明言不收錄聖經；稱各來源「在格式、拼寫標點、檔案編碼上互不相容」「直接訓練會導致大量的錯位幻覺」，稱 NLLB 新增語言之變通寫法「極易引發崩潰」、隨機初始化語言代碼「會嚴重損害預訓練權重的表徵遷移」，原文無這些說法。（3）Card 3 另有一條自擬之語言代碼集合式 $\mathcal{L}_{15}$，原文為表 1；「連續兩個以上之語氣助詞」原文為「more than two characters」；三種假影字串與舞台指示語之中文為 Wiki 回譯，原文僅有英譯描述。（4）Card 4 稱 NLLB「顯著勝過」OpenNMT，原文為「generally outperforms」，未做顯著性檢定；未記作者對譯入英語分數偏高之保留說明。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`，§2（p. 3446）、表 1 與 §3.2（p. 3447）、§3.3（p. 3448）、§3.4（p. 3449）、表 2（p. 3450）、表 3 與表 4（p. 3451）、§5（p. 3452）。
- **發現於**：第三批卡片回填 C 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。以表 2、表 3、表 4 之頁面影像核對後：Card 4 改記表 2 合計列與四種英語模型語言之訓練集句數，註明表 2 有兩組標為 xnb；Card 2 依 §1–§3 改寫並註明不收聖經；Card 3 語言代碼改為文字列表，語氣詞條件與假影字串照原文；Card 4 改為「整體優於」並補作者之保留說明。證據表逐一列出數值與位置。

### EK-175 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | hook、Card 1 與證據表 | 過度表述
- **問題**：`hook` 稱本篇為「首個涵蓋全臺 15 種南島語之標準化平行語料庫」，Card 1 稱「全球首個完整涵蓋臺灣 15 種官方南島語言……之標準化多語言平行語料庫」，證據表 Card 5 列稱「建立全球首個涵蓋全臺 15 種南島語之標準化 MT 基準」並判定符合來源；原文未稱首個，§2 僅說同一語族或地區之多語翻譯資料集較少。開頭引言（Wiki 撰寫）稱語料「高純度」，原文無此評價，且作者自承過濾帶有臨時性。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`，摘要與 §1（pp. 3445–3446）、§2（p. 3446）、§3.3（p. 3448）。
- **發現於**：第三批卡片回填 C 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`hook` 與 Card 1 刪去「首個」，改照摘要；開頭引言改寫，不作品質評價；證據表該列刪除，另立一列註明原文未稱首個。

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

### EK-156 | fixed | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 1、Card 2、Card 3 與 Card 4 | 過度表述
- **問題**：（1）Card 1 稱系統「首創」此架構、傳統微調「迭代週期動輒數月，根本無法應對前線緊急需求」；原文只說作者所知是唯一支援德頓語、比斯拉馬語之開源術語感知工具（§2, p. 131），未提數月。（2）Card 2 之「部落長老」、「例如將 potable water 錯譯為非飲用水」、LLM「常輸出文法崩潰的句子」原文沒有；原文示例只說 MT 把 potable 譯錯（Figure 2）。（3）Card 3 稱翻譯記憶「論文評估中預設為 5 句」，原文只說 N 可設定；稱 MADLAD 針對德頓語、OPUS-MT 針對比斯拉馬語，原文兩者皆在兩語言評估。（4）Card 4 稱 SUS「對應 Grade A」，原文為 excellent；未記載易用性研究只有兩份回應、兩位參與者為共同作者；基隆迪語「回升至 42.76」為 Wiki 依原文 +0.25 計算之值，未標明。
- **來源**：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`，§1–§3（pp. 129–132）、§4.1.1–§4.1.2（pp. 132–133）、§5（p. 134）、倫理聲明（p. 135）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句，補記易用性研究之樣本與共同作者關係、表 1 之 LLM-only 對照值與資料取得條件；`hook` 補上 FLORES 平均增益；證據表重建，表 1、表 2 數值逐一寫出列與欄。

### EK-157 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | hook、Card 1、Card 2、Card 4 與 Card 6 | 過度表述
- **問題**：（1）`hook` 稱「首度」分析並「客觀量化 16 族南島語親緣分支」，原文為作者自述首次，且成對比較只做 7 個多方言族語。（2）Card 1 稱臺灣南島語是南島語系「發源樞紐」、ePark 是「全球規模最完整」的資源庫、作者為「美國學者」；原文為 primary branch、high-quality comprehensive resource，作者單位為高中。（3）Card 2 稱過去分類「多依賴定性音變構擬與有限詞彙調查」、布農語次方言「存在長期爭論」，原文未如此描述，且本篇結果與布農語既有三分群相符。（4）Card 3 前處理寫保留 `^`，原文該字元在 PDF 文字層無法顯示，無法核實。（5）Card 4 稱最少詞元之 46,177 為「泰雅語四季」，表 1 為 Plngawan；稱主題差異「會壓過方言語言學差異」，原文只說須以相同篇章比較；未說明 ± 為標準差。（6）Card 6 稱直接混合訓練「必然遭遇」71% 獨有詞 OOV 衝擊，為 Wiki 推測卻寫成必然。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`，摘要與 §1（p. 124）、§2.1–§2.3（p. 125）、§3.1–§3.2（pp. 125–128）、表 1–3（pp. 127–128）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句；Card 6 該句改標為 Wiki 推測並改為「可能」；證據表重建，表 1 至表 3 數值逐一寫出列與欄。

### EK-158 | fixed | papers/2024-fault-tolerant-quantum.md | Frontmatter、Card 1、Card 3 與 Card 4 | 過度表述
- **問題**：（1）`hook` 與 Card 1 稱「首次」在單一處理器上編碼 48 個邏輯位元、「打破超導固定晶格限制」、製造一個高碼距邏輯位元「需消耗上千個物理位元」、「正式揭開」早期容錯時代序幕；原文未稱首次、未作這些比較，摘要為「herald the advent of early error-corrected quantum computation」。`title_zh` 冠以「邁向容錯量子計算的歷史跨越」；開頭引言為 Wiki 撰寫卻未註明。（2）Card 3 稱閘時原子間距 $\lesssim 3\,\mu$m，原文為 $\lesssim 2\,\mu$m；稱直接實作「三維與四維拓撲碼」，原文為三維 $[[8,3,2]]$ 碼塊在 4D 超立方體上糾纏。（3）Card 4 稱 $d = 3 \to 7$ 之邏輯貝爾態「超越所有單一物理位元對之成對糾纏保真度」，原文無此說，且未交代改善只在相關解碼下成立、傳統解碼反而變差；稱物理電路「因相干誤差累積導致 XEB 歸零」、48 位元希爾伯特空間「遠超古典模擬極限」，原文沒有；GHZ 段把中途讀取前饋與 GHZ 保真度混寫，未列 72(2)% 之容錯結果。
- **來源**：Bluvstein et al. 2024 正式版全文（PMC10830422）：Abstract；Logical processor based on atom arrays、Improving entangling gates with code distance、Fault-tolerant logical algorithms、Complex logical circuits using 3D codes 各節；Extended Data Fig. 1 圖說；Fig. 2–5。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句；`title_zh` 與內文標題刪去副題；引言加註；Card 2 註明晶格手術成本等為 Wiki 補充背景；Card 6 第 2 點改為不誇飾之寫法。證據表逐項登記。

### EK-159 | fixed | papers/2024-fault-tolerant-quantum.md | Card 4 後續與 Card 5 | 原文未支持
- **問題**：Card 4 後續段稱 Google Willow 為 105 位元、「首次……無後選擇」，摘要為 101 位元之 $d = 7$ 碼、未提後選擇；稱 Bravyi et al. 2024 證明 $[[144,12,12]]$ 碼降低開銷近 10 倍，且「本篇……正是實作此類 qLDPC 碼的最理想物理平台」，後者無出處，Bravyi 一文亦未引用本篇。Card 5 三點（「正式跨入 EFTQC」、「打破平面拓撲死局」、「定制解碼將容錯門檻再放寬數倍」）皆無出處。本篇發表於 2024 年，頁面也未記載原文所述之未來方向。
- **來源**：doi:10.1038/s41586-024-08449-y、doi:10.1038/s41586-024-07107-7、doi:10.1038/s41567-024-02479-z（arXiv:2308.08648）、doi:10.1038/s41586-025-09543-5（arXiv:2406.17653）、doi:10.1038/s41586-025-09596-6，皆以 Crossref 與摘要核對，OpenAlex 顯示前四者中除 Bravyi 外皆引用本篇；本篇 Outlook。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。後續段改列四篇引用本篇之後續研究（Xu 2024、Google Quantum AI 2024、Zhou 2025、Chiu 2025）並依摘要描述，Bravyi 2024 改標為未引用本篇之相關研究；Card 5 改為作者評價、後續發展與 Outlook 所列方向，各附出處。證據表登記各列。

### EK-160 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | Frontmatter、Card 1、Card 2 與 Card 6 | 過度表述
- **問題**：（1）`card_line`「翻譯排灣語與華語」暗示雙向，原文只評估排灣語譯華語；`hook` 用「暴升」。（2）Card 1 稱排灣語是「臺灣南部最具歷史深度的南島語言之一」，原文沒有；把文獻中「平行語料少於 10 萬句」之一般說法寫成排灣語之條件，證據表亦然；稱大模型「幻覺頻繁（BLEU 僅 1.7–4.4，§1–§2）」，BLEU 為 §4 之實驗結果，原文未說幻覺頻繁。（3）Card 2 稱純向量檢索會「召回表面詞根相似但焦點語義完全相反的例句，誤導大模型生成顛倒施受關係的幻覺」，原文只說例句稀疏時向量檢索可能失效；稱大模型「根本無法單獨承擔翻譯任務」。（4）Card 6 稱接上構詞解析器後「詞典命中率可由 60% 躍升至 85% 以上」、直接採用辭典譯名「能百分之百防止大模型幻覺」、「論文證實詞典命中時直接 Word Merge 最為穩健」，原文沒有命中率數據，也未做此比較。
- **來源**：`raw/my-focus/英文論文/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`，摘要（p. 1）、§1–§2（pp. 2–3）、§3.4–§3.5（p. 5）、§4（pp. 6–7）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`card_line` 改為「先查辭典再交給大模型，把排灣語譯成華語」，依原文改寫上述各句；Card 6 之推測改標為 Wiki 推測並刪去無出處之數字；Card 4 補記評估範圍之 Wiki 註記（只有自動指標、測試句與辭典語料同源未說明是否排除）；證據表重建。

### EK-139 | fixed | concepts/generative-world-models.md | 關鍵突破支柱（DeepSeek-R1） | 過度表述
- **問題**：概念頁仍沿用論文頁已修正之說法：條目名「推理運算擴展定律」，並稱 R1-Zero「證明無須人工示範即可激發」長鏈推理與測試時算力擴展。論文頁已依 Nature 版改寫（EK-113、EK-152），`title_zh` 已刪「與推理運算擴展定律」，原文未稱證明。
- **來源**：`wiki/papers/2025-deepseek-r1.md` Card 1、Card 5（依 `raw/2025-deepseek-r1.pdf` 修正後）。
- **發現於**：第三批卡片回填 B 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依修正後論文頁改寫條目與連結文字，補作者所列限制；概念頁 `verification` 改為 partial。

### EK-140 | fixed | concepts/multi-messenger-astrophysics.md | 關鍵突破支柱（LIGO、JWST） | 原文不符
- **問題**：LIGO 條目把峰值應變 $10^{-21}$ 寫成「極限應變靈敏度」，並稱「開啟……暗宇宙直接探測時代」；JWST 條目稱本篇「發現」大爆炸後 5 至 7 億年之大質量星系與「小紅點」超大質量黑洞，並沿用舊標題。論文頁已修正（EK-114、EK-115、EK-132 至 EK-138、EK-154、EK-155）：$1.0 \times 10^{-21}$ 為峰值應變；JWST 本篇是由暗物質暈質量函數推導上限，檢驗 Labbé 等之測光候選，未談小紅點。
- **來源**：`wiki/papers/2016-ligo-gravitational-waves.md` 與 `wiki/papers/2023-jwst-massive-galaxies.md` Card 1、Card 4（依原文修正後）。
- **發現於**：第三批卡片回填 B 組回報與 A 組 LIGO 修正，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。兩條依修正後論文頁改寫，更新連結文字；概念頁 `verification` 改為 partial。

### EK-141 | fixed | concepts/quantum-error-correction.md | 關鍵突破支柱（容錯量子計算） | 過度表述
- **問題**：條目稱本篇「首次在單一處理器同時編碼 48 個邏輯量子位元」並提「高編碼率超立方體碼」。論文頁已修正（EK-120、EK-121、EK-158、EK-159）：最多 280 個物理位元、40 個色碼邏輯位元，48 個邏輯位元之電路以三維 $[[8,3,2]]$ 碼執行，原文未稱首次。
- **來源**：`wiki/papers/2024-fault-tolerant-quantum.md` Card 1、Card 4（依正式版修正後）。
- **發現於**：第三批卡片回填 B 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依修正後論文頁改寫條目與連結文字；概念頁 `verification` 改為 partial。

### EK-142 | fixed | concepts/institutions-and-macro-dynamics.md | 關鍵突破支柱（Woodford） | 過度表述
- **問題**：條目稱本篇「證明」央行仍能「牢牢控制」本國通膨。論文頁已修正（EK-112、EK-150、EK-151）：本篇以理論推導與校準示例論證全球化不太可能削弱央行控制通膨之能力，後續實證結果不一。
- **來源**：`wiki/papers/2007-woodford-inflation-dynamics.md` Card 1、Card 4、Card 5（依原文修正後）。
- **發現於**：第三批卡片回填 B 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依修正後論文頁改寫條目並註明結論之性質；概念頁 `verification` 改為 partial。

### EK-190 | fixed | papers/2021-seediq-chinese-mt-you.md | Card 3 特徵拼接公式 | 原文未支持
- **問題**：Card 3 將詞嵌入與詞綴特徵的 Wiki 自行形式化寫成區塊公式；頁面已標示「形式化為 Wiki 整理」，但現行規則只允許原文或補充資料的公式置於區塊。這是 EK-062 原先二元前綴公式及詞嵌入歸屬問題以外的新缺口。
- **來源**：[論文頁](papers/2021-seediq-chinese-mt-you.md) Card 3；[原始學位論文](../raw/my-focus/學長姐論文/賽德克語－中文機器翻譯之研究_游景勝.pdf) §4.1、§4.3；[公式規則](../.agents/skills/wiki-content-audit/SKILL.md) 寫作模式第 3 步。
- **發現於**：2026-11-10，使用者提供之分組複核，Codex by OpenAI 再查原文。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 pp. 28–29、33、38，以原文支持的 250、52、302、22、272 維文字敘述保留特徵設計，移除 Wiki 自擬區塊公式與證據表中該公式列；一元模型卡片公式另依原文 p. 27 校正（EK-062）。此頁僅修已登記問題，verification 改為 partial。

### EK-191 | fixed | papers/2019-generalized-data-augmentation-xia.md | 證據表 Card 3 公式列 | 原文不符
- **問題**：[證據表](evidence/2019-generalized-data-augmentation-xia.md) Card 3 的 Procrustes 約束漏掉左側 W 並有不成對的公式分隔符；論文頁與卡片目前使用的約束為 $W^\top W = I$，須同步修正證據表。此為 EK-074 原先方法與加權目標式問題以外的新缺口。
- **來源**：[Xia 等原文](https://aclanthology.org/P19-1579.pdf) §3.1，p. 5788；[論文頁](papers/2019-generalized-data-augmentation-xia.md) Card 3。
- **發現於**：2026-11-10，使用者提供之分組複核，Codex by OpenAI 再查原文。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 §3.1 p. 5788 頁面影像，修正證據表約束為 $W^\top W = I$ 並補齊公式分隔符；論文頁與卡片原已一致。此頁僅修正已登記問題，verification 改為 partial。

### EK-192 | fixed | papers/2025-indigenous-tek-ai-revitalization-wang.md | Card 1 與證據表 | 原文未支持
- **問題**：Card 1 稱作者為「教授」並稱研究「首創」，證據表將教授職稱歸給原文首頁；原文首頁僅列作者與機構，所查全文的 first 包括研究目標排序等用法，未支持該首創斷言。教授職稱目前未由所列來源核實，不應僅因首頁未列就判定職稱為假。此為 EK-078 原先姓名與架構問題以外的新缺口。
- **來源**：[原始論文](https://doi.org/10.3390/socsci15010007) 首頁與全文；[證據表](evidence/2025-indigenous-tek-ai-revitalization-wang.md)。
- **發現於**：2026-11-10，使用者提供之分組複核，Codex by OpenAI 再查原文。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依原文首頁作者與機構移除論文頁未有列示來源支持的教授職稱，以及全文未支持的「首創」主張；證據表同步更正，不推斷作者實際職稱。頁面 verification 改為 partial。

### EK-193 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 4 模型參數與證據表 | 未能核實
- **問題**：論文頁列 GPT-3.5 175B、GPT-4o 200B、o1-mini 50B、Llama 3.3 70B、DeepSeek-R1 658B，與本篇原文 §5 所列數字一致，但證據表僅記模型名稱。DeepSeek 官方資料為原始 R1 列出 671B 總參數與 37B 啟用參數，與本篇的 658B 不一致；所查 OpenAI 資料的 175B 是 GPT-3 的數字，不能據此確定 GPT-3.5 的參數量，所查 GPT-4o 與 o1 系統卡亦未核實頁面列出的 200B 與 50B。Meta 的 Llama 3.3 70B 模型卡支持 70B 規模。原研究使用 API，未明確記載服務實例的具體快照；修訂時須保留論文與官方來源的差異，不把未證實直接視為證偽，也不能僅憑官方權重推定當時 API 版本。
- **來源**：[Frontull 與 Ströhle 原文](https://arxiv.org/html/2505.22293v1) §5 p. 5；[DeepSeek 官方模型資料](https://github.com/deepseek-ai/DeepSeek-R1)；[OpenAI GPT-3 資料](https://openai.com/index/language-models-are-few-shot-learners/)；[GPT-4o 系統卡](https://cdn.openai.com/gpt-4o-system-card.pdf)；[o1 系統卡](https://openai.com/index/openai-o1-system-card/)；[Meta Llama 3.3 70B 模型卡](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)。
- **發現於**：2026-11-10，第五批審查回報，Codex by OpenAI 再核對原文與官方資料。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。論文頁將參數量明確歸給原研究，並列官方 R1 的 671B／37B、GPT-3 175B 的版本歸屬及所查系統卡無法核實的數字，保留 API 快照未明的限制；證據表逐一登記原文及官方資料。無法核實的實際 API 規模不作猜測，此頁核實狀態改為 partial。

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

### EK-196 | fixed | papers/2012-crispr-cas9.md | Card 4 | 原文不符
- **問題**：頁面稱本篇實驗全數在體外，並把五組 GFP 切割測試寫成 100% 切割效率；原文也有細菌細胞內質體維持試驗，五項 GFP 測試報告正確位置的有效切割，未給出 100% 的切割效率。
- **來源**：[封存作者手稿](../raw/2012-crispr-cas9.pdf) pp. 4、6，Figures 3D、5D。
- **發現於**：2026-11-10，修正 EK-014 時交叉複核，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。區分細菌細胞內試驗與體外嵌合 RNA 切割實驗，移除 100% 效率主張，並同步證據表。

### EK-197 | fixed | papers/2025-nerve-mito-cancer.md | Card 1、3–6 與證據表 | 原文未支持
- **問題**：頁面與證據表將微流控分室、格點光片顯微鏡及 Cox8-Cre 寫為本篇方法；將體外奈米管樣結構擴稱所有活體轉移路徑；另將部分呼吸救援擴稱完全恢復、去神經化直接抑制遠端轉移灶，並把「癌細胞偽裝」歸為作者假說。這些說法未獲所列原文位置支持。
- **來源**：[Hoover 等原文](https://doi.org/10.1038/s41586-025-09176-8) pp. 253–261、Figures 1–5、Methods；Extended Data Figure 4c。
- **發現於**：2026-11-10，修正 EK-039、EK-040 時交叉複核，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。刪除無依據的方法與過度結論，分別說明體外、活體、小鼠、人類組織及不同追蹤模型的證據；調整標題、索引、證據表與 Wiki 比喻的歸屬。

### EK-198 | fixed | papers/2001-colonial-origins-acemoglu.md | Card 3 公式 | 原文未支持
- **問題**：論文頁把作者的文字示意鏈改寫為自擬符號區塊公式，並將自行寫出的第二階段及 2SLS 機率極限式作為展示公式；另將原文式 (4) 的對數記號改為 ln。
- **來源**：[AER 正式版](https://economics.mit.edu/sites/default/files/publications/colonial-origins-of-comparative-development.pdf) pp. 1370、1378、1383–1384，式 (1)–(5)。
- **發現於**：2026-11-10，處理 TD-011 公式出處，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。將自擬示意與估計式改為作者方法和識別假設的文字說明，恢復式 (4) 的原文記號，並逐式登記原文位置；卡片使用的式 (1) 未變。僅核對本次相關內容，核實狀態改為 partial。

### EK-199 | fixed | papers/2013-icecube-neutrino.md | Card 2–3 公式與卡片 | 原文未支持
- **問題**：論文頁與卡片使用的光錐角度、Frank–Tamm 光譜、截面冪律、存活率及一般化通量展示式未在本篇找到；證據表誤將 Frank–Tamm 公式歸給本文。頁面稱高能微中子穿透地球的碰撞機率極低，卡片更稱不被吸收，與原文指出的高能地球吸收不符。
- **來源**：[Aartsen 等原文](https://arxiv.org/pdf/1311.5238) pp. 2–6、Fig. 1–2；[論文頁](papers/2013-icecube-neutrino.md) Card 2–3。
- **發現於**：2026-11-10，處理 TD-011 公式出處，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。刪除未見於本文的展示式及相關無來源數值，以原文的探測、背景與地球吸收描述取代；證據表同步更正，卡片以原文 p. 6 的資料分析式非探測機制為由採無公式模式，亦修正微中子不被吸收的說法。僅核對相關內容，核實狀態改為 partial。

### EK-200 | fixed | papers/2017-attention-is-all-you-need.md | Card 3 公式與卡片 | 原文未支持
- **問題**：原頁將作者以文字敘述的內積均值與方差另寫為展示公式，卡片沿用該自擬方差式；頁面另把縮放防止 Softmax 極端值說得比作者的推測更強，並將位置編碼有助學習相對位置的假設寫成確定效果。
- **來源**：[NeurIPS 定稿](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) §3.2–3.5，pp. 4–6，p. 4 註 4。
- **發現於**：2026-11-10，處理 TD-011 公式出處，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。以原文註 4 的內積式取代自擬方差展示式，保留作者以文字給出的均值與方差；縮放及位置編碼的解釋還原為作者推測，卡片同步修正，並逐式登記原文位置。

### EK-201 | fixed | papers/1982-hopfield-network.md | Card 3 能量公式與 Card 4 後續研究 | 原文不符
- **問題**：頁面及卡片在 Hopfield 原文零閾值的能量式及能量變化式中加入閾值項；此外，頁面把 Amit 等 1985 年以副本對稱理論得到的 0.138 近似值，誤寫為以副本對稱破缺方法得到的嚴格解。
- **來源**：[Hopfield 原文](../raw/1982-hopfield-network.pdf) p. 2556，式 (7)–(8)；[Amit 等原文](https://doi.org/10.1103/PhysRevLett.55.1530) pp. 1531–1532。
- **發現於**：2026-11-10，處理 TD-011 公式出處及抽查卡片後續成果，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Hopfield 原式及零閾值條件修正論文頁與卡片，逐式登記來源；Amit 等之結果標為副本對稱近似，並記下作者對對稱破缺影響的討論。

### EK-202 | fixed | papers/2024-alphafold3.md | Card 3 公式與 Card 4 數據條件 | 原文不符
- **問題**：原頁與卡片使用補充資料未列出的自擬座標變換與加噪公式；排序分數式另加原文沒有的左側符號。卡片數據未標出原文評估指標，抗體成功率未寫 1,000 個模型種子的條件。
- **來源**：[官方補充資料](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-024-07487-w/MediaObjects/41586_2024_7487_MOESM1_ESM.pdf) Algorithm 19、§3.7.1、§5.9.3；[原文](../raw/2024-alphafold3.pdf) p. 494 Fig. 1 圖說、PDF p. 21 Extended Data Table 1。
- **發現於**：2026-11-10，處理 TD-011 公式出處及抽查卡片，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。改以原文 Algorithm 19 座標變換步驟及作者文字說明呈現機制，排序公式保留原文表達；逐式登記來源，卡片補上指標與取樣條件，更新示意圖。

### EK-203 | open | papers/1992-creative-destruction-aghion.md | Card 3 區塊公式 | 未能核實
- **問題**：依正式版線上文字，式 (2.1) 寫 $y=AF(x)$，頁面額外加上下標；頁面以線性特例展示的研發條件與式 (2.10) 的一般不等式形式不同；頁面以 $g$、$\sigma^2$ 與期望、變異數擴寫式 (3.11)，原文以 AGR、VGR 表達。須核對正式版掃描頁，逐式判斷是否為原文或 Wiki 推導，並依規範改寫、登記來源。
- **來源**：[Econometrica 正式版](https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf) pp. 327–330、332、336，式 (2.1)、(2.3)、(2.10)、(2.12)、(3.11)；[證據表](evidence/1992-creative-destruction-aghion.md)。
- **發現於**：2026-11-10，處理 TD-011，Codex by OpenAI。`raw/` 檔案為其他論文；正式版線上文字可讀，但本環境無法取得掃描頁影像核對，尚未把文字擷取當作公式最終證據。

### EK-204 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 1–5、證據表 | 原文不符
- **問題**：Table 1 與其註解（含 Run 數據、註 § 與 ＊）位於印刷頁 768（PDF 第 2 頁），論文頁、卡片檔與證據表多處標為 p.767；Series C 之出處標為「右欄末段」、Run D 之出處標為「右欄第 4 段」，但 p.767 右欄實為 3 段，兩者皆不對應。證據表原列之試劑與反應條件（20 mol%、0.208 mmol、甲苯、0 °C、96 h）亦未列。
- **來源**：[1995 原文](../raw/1995-soai-asymmetric-autocatalysis.pdf) PDF 第 2 頁（印刷頁 768）含 Table 1 與註 §（toluene 49 ml、0.208 mmol、0 °C、96 h）；PDF 第 1 頁（印刷頁 767）右欄 “On the other hand…”、“We propose…” 段。
- **發現於**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）統籌，調派 OpenCode MiniMax M3.1 Flash 逐列核對。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。Table 1 相關出處統一改為 p.768，段落序號依正文改為「右欄首段」「右欄第 2 段」；證據表補列試劑與條件列（以 PDF 文字層核對）。

### EK-205 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | hook、Card 1、Card 5、card_line；concepts/chiral-symmetry-breaking.md | 過度表述
- **問題**：頁面以「首次」「自發」描述 1995 年成果，原文兩頁文字層均未見 “first”，「自發」與本篇的種子實驗（2% e.e. 起始）與 Run D 對照矛盾。卡片導語「首個化學實證」、card_line「揭示同手性起源」超出原文能支持的範圍。概念頁另有「首次在有機合成反應中實現」「千倍自增殖」，並把 Kawasaki 2009 的同位素結果歸於 Soai 反應，又以「證明」「精確相通」描述後續模型與其他領域模型之關係。
- **來源**：[1995 原文](../raw/1995-soai-asymmetric-autocatalysis.pdf) PDF 第 1 頁摘要第 1 段（“Here we show experimentally that autocatalysis in a chemical reaction can indeed enhance…”）；PDF 第 2 頁（印刷頁 768）“It seems conceivable…”、“remains to be clarified”。
- **發現於**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）統籌；DeepSeek Harness 獨立審查提出，總指揮對照原文複核。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。刪除「首次」「自發」「首個」；card_line 改為「不對稱自催化，微弱手性偏差被逐輪放大」，封面斷行同步改寫；導語改為「為生命起源同手性提供化學實驗模型。」；概念頁第 24、26、32、34 行改寫；後續研究之二聚體內容於論文頁註明「以 Blackmond 2001 為準，本頁尚未對照該文全文」。已重建論文頁與首頁，論文頁與首頁相關驗證通過。

### EK-206 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 3 鋅烷氧化物循環式 | 原文未支持
- **問題**：步驟 3 寫作 `2_new + H+ → 1_new + Zn(II)`，質量與電荷皆不平衡（缺 i-PrH，且 H+ 數不足）。頁面與證據表原稱「鋅副產物未配平」，但缺漏的 i-PrH 為有機副產物，不屬於鋅物種。
- **來源**：依 Fig. 2 改寫（原文未配平）；以原子與電荷守恒推導為 `2_new + 2H+ → 1_new + i-PrH + Zn2+`（DeepSeek Harness 獨立審查提出，總指揮複核）。
- **發現於**：2026-11-11 10:28，DeepSeek Harness 獨立審查（只讀）。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。改為平衡式並註明「依 Fig. 2 改寫，未列鋅物種之完整計量」；證據表第 17 行同步。

### EK-207 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | frontmatter honor、正文表彰語、證據表獎項核對 | 原文不符
- **問題**：honor 與正文寫「表彰分子同手性起源與不對稱自催化合成」，但諾貝爾官網 2026 化學獎引文為 “for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis”；「分子同手性起源」為官方科普說明之概括，不是表彰語原文。
- **來源**：[Nobel Prize in Chemistry 2026](https://www.nobelprize.org/prizes/chemistry/2026/)
- **發現於**：2026-11-11 10:28，總指揮查證；DeepSeek Harness 獨立審查同樣指出。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。改為「表彰不對稱有機合成中非線性效應與自催化的發現」；證據表註明官方引文與科普概括之區別。

### EK-208 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 5 第 65 行 | 歸因／版本錯置
- **問題**：Card 5 里程碑將 2026 諾貝爾化學獎表彰語寫為「Kagan與Soai獲諾貝爾化學獎表彰不對稱自催化」，遺漏官方表彰核心「非線性效應（non-linear effects）」，且將非自催化發現者的 Kagan 錯誤歸為表彰不對稱自催化（Kagan 獲獎工作為非線性效應，Soai 為自催化）。
- **來源**：[Nobel Prize in Chemistry 2026](https://www.nobelprize.org/prizes/chemistry/2026/)；論文頁 Frontmatter 第 10 行與正文第 28 行；證據表第 5 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。里程碑改為「Kagan與Soai獲諾貝爾化學獎，表彰非線性效應」，補回官方引文核心「非線性效應」並不再把自催化單獨歸給 Kagan；另於註記標明獎項亦表彰自催化（官方引文：「for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis」）。

### EK-209 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 6 第 70 行與 Card 2 第 16–17 行 | 過度表述
- **問題**：Card 6 轉變寫「稀釋雜訊→自發放大」，Card 2 缺口寫「缺乏能自發濃縮微小手性偏差之化學反應網路」，但 1995 原文為 2% 及 5% e.e. 種子放大，Run D 外消旋對照（0% e.e.）產物手性選擇性低於檢測極限（BDL），未顯示能「自發」放大或濃縮；且 EK-205 已決議刪除「自發」，卡片檔未同步清除殘留之「自發放大」與「自發濃縮」。
- **來源**：印刷頁 768 Table 1 Run D；p. 767 左欄摘要第 1 段（文字層 `pdf_page1_text.txt` 第 18–25 行）；`wiki/issues.md` EK-205。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。Card 6 轉變改為「稀釋雜訊→種子逐輪放大」、Card 2 缺口改為「缺乏能把微小手性偏差逐輪放大的化學反應網路」，刪除「自發放大」與「自發濃縮」殘留；Card 2 結語改以 Run D 外消旋對照之實測結果表述（「無手性種子時，產物選擇性低於檢測極限。」），與種子實驗一致。

### EK-210 | fixed | concepts/chiral-symmetry-breaking.md | 第 34 行 | 歸因／版本錯置
- **問題**：內文稱「異手性二聚體充當『熱力學失活陷阱』，使主導手性單體在動力學活性池中佔據壓倒性催化優勢」，將活性催化中心誤寫為「單體」。在 Blackmond 2001 二聚體催化模型中，催化活性中心為同手性二聚體（homochiral dimer），並非單體；此處混淆了二聚體催化機制與單體催化模型（如 Noyori DAIB 機制），且與論文頁 Card 3 第 92、108 行矛盾。
- **來源**：Blackmond et al. (2001), *JACS* 123:10103–10104；論文頁 `papers/1995-soai-asymmetric-autocatalysis.md` Card 3 第 92、108 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。改為二聚體模型之正確描述：「異手性二聚體充當『熱力學失活陷阱』，使催化活性較高的同手性二聚體在活性池中佔據優勢」，刪除誤植之「單體」與「壓倒性」；並加註「依 Blackmond 2001 之模型描述，本頁尚未對照全文」，與論文頁 Card 3 表述一致。

### EK-211 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 6 第 144–145 行 | 過度表述
- **問題**：內文斷言「放大的本質不是『製造』手性，而是『選擇』手性」，並將異手性二聚體熱力學穩定化類比為「免疫系統的容忍機制」。原文實驗顯示自催化反應由非手性受質原位化學合成了新嘧啶醇分子（新生成物 e.e. 達 90%、物質量放大至 1,674 倍），為化學合成與不對稱誘導過程，並非被動篩選；且與免疫系統容忍機制之結構類比缺乏文獻支持，屬過度詮釋。
- **來源**：印刷頁 767–768 全文（文字層 `pdf_page1_text.txt`、`pdf_page2_text.txt` 均未見此類哲學主張與免疫學類比）；Table 1 新生成物數據（p. 768）。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。Card 6 第 1 點改為「放大的機制同時包含『合成』與『選擇』（Wiki 詮釋）」，並補述本篇確實原位化學合成新嘧啶醇分子（新生成物 e.e. 達 90%、(S)-1 總量放大 1,674 倍，Table 1，p.768），不再斷言僅為「選擇」；第 2 點明確標為 Wiki 詮釋，刪去「有結構上的類比」之過度延伸，改為「僅作為概念類比，不是本篇或文獻之結論」。

### EK-212 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 3 第 108 行 | 未能核實
- **問題**：內文斷言「異手性二聚體 S-R 的生成平衡常數大於同手性二聚體，即 $K_{\mathrm{hetero}} > K_{\mathrm{homo}}$；在相同標準態下以 $\Delta G^{\circ} = -RT \ln K$ 表示，異手性二聚體的 $\Delta G^{\circ}$ 較負，熱力學上較穩定」，忽視了純統計二聚即存在 $K_{\mathrm{hetero}} = 2 K_{\mathrm{homo}}$ 之對稱度因子，且 Blackmond 2001 核心在於催化活性差異（$k_{\mathrm{homo}} \gg k_{\mathrm{hetero}} \approx 0$）；內文坦承「本頁尚未對照該文全文」，證據表第 34 行亦標記為「內容未核對」，卻於正文作出肯定性熱力學數值判定。
- **來源**：Blackmond et al. (2001), *JACS* 123:10103–10104；證據表 `evidence/1995-soai-asymmetric-autocatalysis.md` 第 34 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。$K_{\mathrm{hetero}} > K_{\mathrm{homo}}$、$\Delta G^{\circ}$ 與「儲庫」推論全部改寫為「依 Blackmond 2001 之模型描述」之敘述（催化活性差異亦同），不再以本頁斷言該文數值；並加註判讀界線「同手性與異手性二聚體的統計因子會影響 $K$ 之直接比較，本頁未對照該文全文，數值判斷以原文為準」，證據表第 34 行同步標記。

### EK-213 | fixed | evidence/1995-soai-asymmetric-autocatalysis.md | 第 11 行 | 原文不符
- **問題**：表格將 Series A 出處標記為「印刷頁 768 Table 1 Runs A1–A5；p. 767 右欄首段」，但 p. 767 右欄首段實為 Series B 之延續與 A、B 兩系列總結（lines 122–126），Series A 之具體實驗描述與反應條件位於 p. 767 左欄第 3 段至末段（lines 37–53）。
- **來源**：印刷頁 767（PDF 第 1 頁）文字層 `pdf_page1_text.txt` 第 37–53 行（左欄 Series A）與第 122–126 行（右欄 Series B 結尾）。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。Series A 出處改為「印刷頁 768 Table 1 Runs A1–A5（1,674 倍見 Run A5）；p. 767 左欄第 3 段（Series A 起始 5% e.e. 之實驗描述與 20 mol% 條件）」，並註明 942 與 1,674 倍之合併總結句位於 p. 767 右欄首段（承左欄末段）。Series B 出處同步改為「印刷頁 768 Table 1 Runs B1–B5（942 倍見 Run B5）；p. 767 左欄末段（2% e.e. 起始與「increased by the factor of 942 times」之文字塊）」，均以 pymupdf 文字塊座標逐一核對。

### EK-214 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 5 第 64 行 | 過度表述
- **問題**：Card 5 里程碑將 Kawasaki 2009 表述為「證明碳同位素微弱差異亦能觸發手性自催化」，使用絕對化強斷言「證明」；該文在證據表第 26 行標註為「僅書目，內容未核對」，且自然科學實驗為「顯示/示範」（Triggered/demonstrated），不宜在未核對全文下逕寫「證明」。
- **來源**：Kawasaki et al. (2009), *Science* 324:492–495；證據表 `evidence/1995-soai-asymmetric-autocatalysis.md` 第 26 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。「證明」降格為「顯示」，並於出處欄保留「（書目未對照全文）」標示，與證據表第 26 行「僅書目」之狀態一致。
