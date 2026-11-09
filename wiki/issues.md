# 內容問題清單（Issues）

> 本檔登記查核發現之待修正事項，格式與狀態規則見 [AGENTS.md](../AGENTS.md) 第七章第 4 節。標題五段依序為：編號、狀態（`open` / `fixed` / `wontfix`）、相對於 `wiki/` 之檔案、位置、判定。修正時就地改狀態並追加「處理」行，不得刪除條目。
>
> EK-001 至 EK-056 係於 2026-11-09 自 [wiki/log.md](log.md) 2026-11-08 21:40 至 23:36 之 audit 條目逐筆轉錄（原查核者均為 Codex by OpenAI，EK-031 例外），問題描述與來源沿用原條目，轉錄時未重新核對原文。修正前須依 `wiki-content-audit` 回原文確認，不得只照本檔描述改寫。EK-057 至 EK-060 為轉錄同日以 `crossref_check.py` 查得之 DOI 問題。

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

## 1992 Aghion–Howitt 創造性破壞

### EK-003 | fixed | papers/1992-creative-destruction-aghion.md | Card 4 | 過度表述
- **問題**：成長率與變異數公式以線性研發技術 φ(n)=n 為條件，卡片未明示；原文只說某些條件下存在週期均衡，頁面稱可解釋實際商業週期，強於原文。
- **來源**：[Aghion & Howitt 原文（Econometrica 60(2), 1992）](https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf)
- **發現於**：wiki/log.md [2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Econometrica 1992 pp. 333, 335–338 查核後修訂：Card 3 明確標註穩態對數成長率 $g=\lambda\hat{n}\ln\gamma$ 與方差 $\sigma^2=\lambda\hat{n}(\ln\gamma)^2$ 係在線性研發技術 $\phi(n)=n$ 條件下成立；Card 4 修正極限環陳述，精確說明 2 階極限環係在跨期映射導數 $\psi'(\hat{n}) < -1$ 條件下湧現之理論動態特徵，降格原先「可解釋商業週期」之過度表述。證據表見 wiki/evidence/1992-creative-destruction-aghion.md。

### EK-004 | fixed | papers/1992-creative-destruction-aghion.md | Card 5 | 原文未支持
- **問題**：把 1992 模型直接連到現代反壟斷標準與 Killer Acquisitions；屬後續政策延伸，須另引研究並標明非本文結果。Card 6 若有同類政策結論亦同。
- **來源**：同 EK-003
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 反壟斷政策段落：明確將科技巨頭併購審查與扼殺式收購（Killer Acquisitions，引 Cunningham et al., 2021 JPE）標記為創造性破壞架構在後續產業組織文獻與政策實踐之延伸應用，非 1992 奠基論文之直接檢驗結果。證據表見 wiki/evidence/1992-creative-destruction-aghion.md。

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

## 2007 Woodford 通膨動態

### EK-008 | fixed | papers/2007-woodford-inflation-dynamics.md | Card 1 | 過度表述
- **問題**：「嚴格證明決定權毫不動搖」強於原文摘要「全球化不太可能削弱央行控制通膨的能力」。
- **來源**：[原文（NBER WP 13329）](https://www.nber.org/system/files/working_papers/w13329/w13329.pdf)
- **發現於**：wiki/log.md [2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文摘要 p. 2 與引言修訂 Frontmatter hook 與 Card 1：將「嚴格證明決定權毫不動搖」改述為貼合原文之「系統檢驗金融、商品與要素全球化對貨幣傳導機制三大環節（LM、IS、AS 方程）之影響，論證全球化不太可能削弱央行控制本國通膨動態的能力」。證據表見 wiki/evidence/2007-woodford-inflation-dynamics.md。

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

### EK-023 | fixed | papers/2021-alphafold2.md | Card 5 | 歸因／版本錯置
- **問題**：把核孔複合體結構寫成直接套用 AF2 預測；後續研究是以 AlphaFold 模型結合 cryo-EM 等實驗資料做整合建模。
- **來源**：[封存主論文](../raw/2021-alphafold2.pdf)、[NPC 整合建模研究](https://pubmed.ncbi.nlm.nih.gov/35679401/)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 典範轉移段落：明確將核孔複合體（NPC）等超大複合體結構解析標記為 AlphaFold 預測模型與低解析度冷凍電鏡（cryo-EM/ET）數據結合之「整合建模（Integrative Modeling）」應用，非單純直接預測之結果。證據表見 wiki/evidence/2021-alphafold2.md。

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

### EK-027 | open | papers/2023-jwst-massive-galaxies.md | Card 4 | 原文不符
- **問題**：將 ε≈0.57 指派至 z≈7.5；原文此值對應 z≈9.1 之 1σ 邊際一致性，z≈7.5 中心估計約 0.84。「觀測密度為理論上限 2–5 倍」亦超出原文結論。
- **來源**：[原文](https://www.nature.com/articles/s41550-023-01937-7.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-028 | open | papers/2023-jwst-massive-galaxies.md | Card 3 | 歸因／版本錯置
- **問題**：主計算採 Sheth–Tormen 暈質量函數，後文卻附 Press–Schechter erfc 解析式；須明示 PS 為補充近似，非 Boylan-Kolchin 論文所用之 HMF。
- **來源**：[封存原文](../raw/2023-jwst-massive-galaxies.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:00] audit

## 2024 AlphaFold 3

### EK-029 | open | papers/2024-alphafold3.md | Card 4 | 歸因／版本錯置
- **問題**：將介面 LDDT 標成成功率；複雜多醣鏈 72.1% 之歸屬未獲主文支持。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-030 | open | papers/2024-alphafold3.md | Card 1 | 過度表述
- **問題**：「全面擊敗所有領域專用工具」強於原文「優於許多既有專用工具」；原文按任務與基準分別比較。
- **來源**：[封存原文](../raw/2024-alphafold3.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2024 可容錯量子處理器

### EK-032 | open | papers/2024-fault-tolerant-quantum.md | Card 4 | 原文不符
- **問題**：把「40 個 color-code qubits」混寫成「40 個橫向邏輯 CNOT 閘」，混淆量子位元數與閘數；另須與以 3D [[8,3,2]] code blocks 執行之 48 邏輯量子位元取樣電路分開敘述。
- **來源**：[原文](https://arxiv.org/abs/2312.03982)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit

### EK-033 | open | papers/2024-fault-tolerant-quantum.md | Card 1 | 原文不符
- **問題**：將中性 87Rb 原子寫成「帶電」搬運；原文為 neutral-atom 陣列。
- **來源**：[封存原文](../raw/2024-fault-tolerant-quantum.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

### EK-034 | open | papers/2024-fault-tolerant-quantum.md | Card 5 | 原文不符
- **問題**：把 qLDPC 說成已由本實驗實作；原文只把 qLDPC 列為未來降低開銷之方向。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2024 Sora

### EK-035 | open | papers/2024-sora-world-simulator.md | Card 3 | 原文未支持
- **問題**：把 VAE 具體架構、3D RoPE、adaLN-Zero 與 epsilon-prediction 當作 Sora 已知實作。OpenAI 報告未提供實作細節，並說模型訓練預測原始乾淨 patch，與 epsilon-MSE 公式不符；二手反向推測須明標推測。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-036 | open | papers/2024-sora-world-simulator.md | Card 1 | 過度表述
- **問題**：將遮擋後維持物體存在寫成一般穩定能力，報告措辭為「常能但並非總是」並明列物理模擬限制；即時互動與狀態記憶之說法亦超出原文示例。Card 5、6 之世界模型與隱式幾何重建描述應保留為有限能力觀察或詮釋。
- **來源**：同 EK-035
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit

## 2025 DeepSeek-R1

### EK-037 | open | papers/2025-deepseek-r1.md | Card 4 | 原文不符
- **問題**：將 cons@64 標成 cons@16，並須註明所用論文版本。
- **來源**：[論文](https://arxiv.org/abs/2501.12948)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-038 | open | papers/2025-deepseek-r1.md | Card 1 | 原文不符
- **問題**：把「完全不使用 SFT」同時套到 R1-Zero 與 R1；原文只有 R1-Zero 為純 RL，R1 使用冷啟動資料、RL、拒絕採樣與後續 SFT。
- **來源**：[封存原文](../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2025 神經元粒線體與癌症

### EK-039 | open | papers/2025-nerve-mito-cancer.md | Card 4 | 原文不符
- **問題**：測序方法、實驗模型與轉移比例被混併；原文為分選癌細胞後之 Nanopore 分析，不是單細胞長讀長測序。
- **來源**：[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328229/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-040 | open | papers/2025-nerve-mito-cancer.md | Card 3 | 原文未支持
- **問題**：粒線體轉移—OCR 線性增益、轉移灶富集等符號模型未見於原文，卻呈現為本文模型；須標為教學推導並註明假設。
- **來源**：[封存原文](../raw/2025-nerve-mito-cancer.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-041 | open | papers/2025-nerve-mito-cancer.md | Card 6 | 原文未支持
- **問題**：推論癌細胞偽裝成受損組織、誘使神經元依修復程序供應粒線體；原文支持轉移與富集，未證明此機制，應標作假說或比喻；治療建議亦非本文已驗證療效。
- **來源**：同 EK-040
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2025 滿語上下文機器翻譯

### EK-031 | fixed | papers/2025-manchu-in-context-mt-pei.md | Card 1 | 原文不符
- **問題**：第 27 行語族寫作「阿爾泰阿爾泰通古斯語族」，字詞重複，且「阿爾泰語系」歸類有爭議，宜依原文寫作通古斯語族（Tungusic）。
- **來源**：待回原文核對語族表述
- **發現於**：wiki/log.md [2026-11-08 22:06] audit（Claude Code by Anthropic）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。原文 §3（p. 8769）稱滿語為 critically endangered Tungusic language；Card 1 改為「通古斯語」，刪除重複且有爭議之「阿爾泰阿爾泰」。

## 概念頁

### EK-042 | open | concepts/neural-circuits.md | 2017 支柱 | 歸因／版本錯置
- **問題**：把 Transformer 注意力與 Hopfield 網路等價列在 2017 支柱；等價結果來自連續／現代 Hopfield 之後續工作（Ramsauer et al. 2021），不應歸給 1982 原始網路或 2017 Transformer 原文。
- **來源**：[Ramsauer et al.](https://arxiv.org/abs/2008.02217)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-043 | open | concepts/brain-machine-interface.md | 核心支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 能量吸引子寫成當代 BCI 神經流形解碼之數學基礎；神經流形屬獨立研究脈絡，現有來源不足以建立直接傳承。
- **來源**：[Hopfield 封存原文](../raw/1982-hopfield-network.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 21:57] audit

### EK-044 | open | concepts/brain-machine-interface.md | 跨學科延伸 | 過度表述
- **問題**：將雙光子讀取與全息光遺傳寫入概括為「萬級神經元的無損閉環互動」；原始研究為光刺激選定個別細胞、同時記錄數千神經元，未驗證萬級同時控制、無損或臨床可用。
- **來源**：[原始研究](https://www.nature.com/articles/s41593-026-02350-9)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit

### EK-045 | open | concepts/generative-world-models.md | 支柱與時間線 | 歸因／版本錯置
- **問題**：將 Hopfield/Hinton 能量模型合標為 1982（Boltzmann machine 學習論文為 Ackley、Hinton、Sejnowski 1985），並把 Hopfield、Boltzmann、score matching、擴散模型與 Transformer 寫成直接奠基鏈；須分開作者年代並改標為概念類比或補中間研究。
- **來源**：[Hopfield 封存原文](../raw/1982-hopfield-network.pdf)、[Ackley et al. 1985](https://doi.org/10.1207/s15516709cog0901_7)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:44] audit

### EK-046 | open | concepts/generative-world-models.md | DeepSeek-R1 段 | 歸因／版本錯置
- **問題**：將「無須人工示範」歸給 DeepSeek-R1（實為 R1-Zero），並把可驗證獎勵從原文之數學與程式任務推廣到任意驗證器與科學探索代理，應標為展望。
- **來源**：[DeepSeek-R1 封存原文](../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-047 | open | concepts/quantum-error-correction.md | 支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 列為表面碼／色碼隨機鍵 Ising 映射之直接來源；映射可追溯至 Dennis et al. 2002，其原文未引用 Hopfield，須分開數學類比與歷史來源。
- **來源**：[Dennis et al. 2002](https://arxiv.org/abs/quant-ph/0110143)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-048 | open | concepts/quantum-error-correction.md | 定義段 | 原文不符
- **問題**：稱以橫向閘即可阻止錯誤擴散並實現「任意深度」演算法；依 Eastin–Knill 定理，可偵測錯誤之非平凡量子碼不存在通用橫向邏輯閘集合，須說明其他非橫向或測量型資源。
- **來源**：[Eastin–Knill](https://arxiv.org/abs/0811.4262)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:00] audit

### EK-049 | open | concepts/quantum-error-correction.md | 跨學科延伸 | 過度表述
- **問題**：稱可重構中性原子陣列已能直接實作 3D／4D 拓撲碼與常數編碼率 qLDPC；所引 2024 實驗將 qLDPC 列為後續方向，未報告已實作。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-050 | open | concepts/multi-messenger-astrophysics.md | 核心定義 | 原文不符
- **問題**：把深空紅外線列為與重力波、微中子、宇宙射線並列之獨立信使；紅外線屬電磁波譜。定義與後文「三大信使」亦不一致，須統一分類（光、粒子、重力波）。
- **來源**：[NASA 多信使說明](https://svs.gsfc.nasa.gov/gallery/multimessengerastronomy/)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-051 | open | concepts/institutions-and-macro-dynamics.md | AJR 支柱 | 過度表述
- **問題**：稱 AJR 以殖民者死亡率「嚴格識別」制度而非地理為收入差距的唯一根因；原文是在排他性假設與控制條件下估計制度效果，不能概括為已排除所有地理作用或證明唯一根因。
- **來源**：[AER 原文摘要](https://www.aeaweb.org/articles?id=10.1257/aer.91.5.1369)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-052 | open | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文不符
- **問題**：稱 DrugCLIP 可「數秒」篩選百億級分子；原文為 6 billion 分子檢索少於 10,000 秒，GenomeScreenDB 規模約 10,000 個人類蛋白質、5 億化合物，全基因組篩選約 24 小時（8 張 A100）。
- **來源**：[DrugCLIP 封存原文](../raw/2023-drugclip.pdf)、[論文紀錄](https://pubmed.ncbi.nlm.nih.gov/41505557/)、[計算配置](https://www.biorxiv.org/content/10.1101/2024.09.02.610777v3.full)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit、[2026-11-08 23:21] audit

### EK-053 | open | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文未支持
- **問題**：把 AlphaFold 3＋FEP 描述成已實證之全原子誘導契合精排管線；AF3 原文報告的是複合體結構預測基準，應標為待驗證提案並另引直接驗證研究。
- **來源**：[AlphaFold 3 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit

### EK-054 | open | concepts/programmable-cellular-engineering.md | 跨學科延伸 | 過度表述
- **問題**：「已能直接在患者肝臟、視網膜與造血幹細胞中修正致病突變」合併不同遞送方式與證據階段：Casgevy 為體外編輯後回輸；EDIT-101 為小型 1–2 期試驗；肝臟 LNP 鹼基編輯為單一新生兒 N-of-1 個案。另須同步校正自 CRISPR 論文頁重述之 PAM 與衍生技術歸因（見 EK-012、EK-015）。
- **來源**：[FDA 審查文件](https://www.fda.gov/media/175179/download?attachment=)、[視網膜試驗](https://www.nejm.org/doi/10.1056/NEJMoa2309915)、[肝臟 N-of-1](https://www.nejm.org/doi/10.1056/NEJMoa2504747)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit、[2026-11-08 23:21] audit

### EK-055 | open | concepts/neural-circuits.md | Hopfield 支柱 | 歸因／版本錯置
- **問題**：與 EK-043、EK-045 同源，將 Hopfield 1982 吸引子延伸為後續多個領域之直接歷史基礎；22:44 審查指出此錯誤於多個概念頁重述，修正時須同步。
- **來源**：同 EK-042
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit

### EK-056 | open | concepts/generative-world-models.md | Sora 段 | 過度表述
- **問題**：重述 Sora 能力界線問題（見 EK-036），把有限能力觀察寫成已證明之通用物理模擬。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit

## DOI 無法解析（2026-11-09 crossref_check.py）

### EK-057 | open | papers/2025-tulun-adaptable-lrl-mt-merx.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2025.acl-demos.13` 在 Crossref 與 doi.org 均查無此號，DOI 可能有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：本檔建立時以 crossref_check.py 查得（Claude Code by Anthropic）

### EK-058 | open | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.loresmt-1.25` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：同 EK-057

### EK-059 | open | papers/2026-epark-formosan-dialectometry-gagnier.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.dialres-1.13` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：同 EK-057

### EK-060 | open | papers/2026-formosanmt-parallel-corpus-scheppat.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.lrec-1.273` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 LREC 2026 論文集原文首頁核對
- **發現於**：同 EK-057

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

### EK-078 | open | papers/2025-indigenous-tek-ai-revitalization-wang.md | Card 1 與 Card 3 | 原文不符
- **問題**：（1）Card 1（第 29 行）作者姓名寫作「王 reen-cheng」，中英大小寫混雜。（2）Card 3（第 45–53 行）將模型寫為 Nonaka 四階段 SECI 遞迴算子；原文 §3.2（pp. 7–11，圖 3）係將 Nonaka 模型擴展為四層知識矩陣（$K_1$ 個體內隱、$K_2$ 個體外顯、$K_3$ 部落社群、$K_4$ 文化系統）與 12 個知識轉換階段，並搭配五層 LKM 架構（§3.4，圖 5）與 Plan–Act–Observe–Adjust 代理迴圈（§3.5，圖 6）。（3）Card 3（第 56–61 行）列出基於餘弦相似度之禁忌懲罰損失函數；原文為質性系統架構論文，全文無任何數學公式或損失函數（文化禁忌係由第一層部落會議審查、第三層語義標籤與第五層規則權限矩陣控管）。
- **來源**：`raw/my-focus/英文論文/From Tacit Knowledge Distillation to AI-Enabled Culture Revitalization Modeling Knowledge Cycles in Indigenous Cultural Systems_socsci-15-00007.pdf`（§3.2–3.5 pp. 7–15 圖 3–6）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-079 | open | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 3 | 原文不符
- **問題**：第 43–62 行與架構圖稱方言距離係「對共享同一個語義概念的詞彙集合 $\mathcal{V}_{AB}$」計算編輯距離並執行「多維尺度分析（MDS）」。原文 §2.3（p. 125）並未對齊同義概念詞表亦未使用 MDS，而是直接對語料庫表面詞形計算三項指標：（1）詞級 TF-IDF 餘弦相似度（`min_df=2`、`sublinear_tf=True`）、（2）頻率 $\ge 5$ 詞型之未加權 Jaccard 相似度、（3）各方言前 500 高頻詞型雙向平均之字元級正規化 Levenshtein 距離。Card 3 完全漏述前兩項核心指標（TF-IDF 餘弦與 Jaccard），且虛構概念對齊詞表與 MDS。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`（§2.3 p. 125）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-080 | open | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 3 與 Card 6 | 原文不符
- **問題**：（1）Card 3（第 47 行與第 62 行架構圖）稱資料清洗採語言識別器与語義對齊過濾 $\operatorname{AlignScore}(x_i, y_i) \ge \tau$；原文 §3.3（p. 3448）係使用正則表達式與詞／字元長度比門檻（2 詞以上剔除 $r \le 0.2$ 或 $r > 8.0$；少於 2 詞剔除字元比 $r \le 0.05$ 或 $r > 20.0$），無語義對齊模型或語言識別器。（2）Card 3（第 49 行）所列 15 語言代碼含錯誤代碼 `puy`、`ruk`、`cou`、`sai`、`kan`、`sed` 且同時列出 `sed` 與 `trv`（漏列噶瑪蘭語 `ckv` 與撒奇萊雅語 `szy`）；原文表 1（p. 3447）之 ISO 639-3 代碼為 `ami, bun, ckv, dru, pwn, pyu, ssf, sxr, szy, tao, tay, trv, tsu, xnb, xsy`。（3）Card 3（第 53–59 行）稱對 NLLB-200 進行 15 語多語言聯合微調；原文 §4.2（p. 3450）明言係針對各族語－華語及 4 個族語－英語**分別訓練獨立之雙向雙語模型**，並於 §6（p. 3453）將多語言聯合預訓練列為未來工作。（4）Card 6（第 90 行）寫「30 萬高品質句對」，與 Card 4 之總量 493,519 句不一致。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`（§3.3 p. 3448、表 1 p. 3447、§4.2 p. 3450、§6 p. 3453）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-081 | open | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | Card 1 與 Card 3 | 原文不符
- **問題**：（1）Card 1（第 30 行）將作者寫作「王 reen-cheng 教授」，中英大小寫混雜。（2）Card 3（第 44–53 行）列出雙軌混合檢索線性加權公式（結合餘弦相似度與 BM25），並於第 62 行與架構圖（第 65–69 行）稱辭典模組解析出「詞根＋詞綴焦點＋中文詞條」且與向量庫並聯檢索。原文 §3.1–3.2（pp. 4–5，圖 1–3）全文無任何數學公式、未使用 BM25，亦未由辭典解析詞根與焦點；實際流程（圖 3）為**串聯式條件分支（if-else fallback）**：逐詞先查記憶體內 JSON 雜湊表（`Is it in the hash map? YES -> Word Merge`），僅當詞典未命中（`NO`）時才查詢 Qdrant 向量資料庫。
- **來源**：`raw/my-focus/英文論文/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`（§3.1–3.2 pp. 4–5 圖 1–3）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-082 | open | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 3 與 Card 4 | 原文不符
- **問題**：（1）Card 3（第 44–53 行）稱依據「句法成分樹（Constituency Tree）」拆解來源句，並檢索包含片段及其「對應目標語譯文子串的最小對齊例句對」。原文 §3（p. 3，圖 1）完全未使用句法成分樹剖析器或子串級目標語對齊，而是以**由 7 個連續詞遞減至 1 個詞之滑動視窗（sliding window）**在檢索庫來源端進行精確子字串匹配，為每個不重疊片段隨機抽取至多 6 組完整雙語句對；且 Card 3 漏述 Pivoted Fragment-Shot（§3，pp. 3–4，圖 2）經由義大利語樞紐進行兩階段巢狀片段檢索（排除整句完全重疊）之機制。（2）Card 4（第 83–84 行）兩度將研究對象 **Ladin（拉定語，北義多洛米蒂山區雷托－羅曼語支少數民族語言：Val Badia 與 Gherdëina）**誤寫為「**拉丁語**變體」。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`（§1 p. 1、§3–§4 pp. 3–4 圖 1–2）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-083 | open | papers/2025-tulun-adaptable-lrl-mt-merx.md | Card 3 | 過度表述
- **問題**：Card 3（第 46–62 行）僅以抽象算子描述檢索，未交代原文 §3.2（p. 132）之具體檢索設計：詞彙表（Glossary）係以 spaCy `en_core_web_sm` 斷詞後進行 `{1,2}`-gram 重疊匹配，翻譯記憶庫（Translation Memory）係以 `Tantivy` 函式庫執行 Top-$N$ BM25 檢索，並以 `MADLAD-400-10B`／`OPUS-MT`／`NLLB-54B` 搭配 `Gemini 2.0 Flash` 進行少樣本思維鏈（CoT）後編輯；且原文全文無數學公式（式 52、56 應標明為依原文流程整理之示意式）。
- **來源**：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`（§3.2 p. 132、§4.1–4.2 pp. 132–133）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-084 | open | papers/2026-context-volume-rag-domain-shift-setiawan.md | Card 3 | 原文不符
- **問題**：第 54–60 行稱論文證明 $\operatorname{chrF++}$ 與語境容量呈精確對數線性公式，且第 48 行稱使用「稠密檢索器」召回上下文。原文 §4.3 與 §5.2–5.3（pp. 90–93，表 2、4、5、6）全文無此對數線性公式；表現最佳之平行句檢索策略並非稠密向量檢索，而是基於 `rapidfuzz` 字元級正規化 Levenshtein 相似度 $\ge 0.5$ 之**詞級模糊匹配（Word-Level Fuzzy Matching）**；且句級檢索（BM25、BGE、ChrF-RAG）於 $K \approx 60$ 即飽和，詞級檢索於每詞 $n = 10$（有效句數 $K \approx 137$，35.28 chrF++）達峰值後，於 $n = 15, 20$（$K \approx 205, 272$）因語境雜訊回落至 35.16 與 34.22 chrF++（表 5），並非單調無限上升。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Context Volume Drives Performance Tackling Domain Shift in Extremely.pdf`（§4.3 p. 90、§5.2–5.3 pp. 91–93、附錄 E p. 100 表 4–6）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-085 | open | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | Card 3 | 原文不符
- **問題**：（1）第 46–48 行將 SONAR 評分寫為餘弦相似度；原文 §2.1.1（p. 226）明言使用 `blaser_2.0` 跨語言語義相似度預測模型（輸出 1–5 分段，故門檻為 3.0 與 3.7，餘弦相似度不可能大於 1）。（2）第 61–72 行與架構圖將四階段課程學習順序與資料集完全寫反：頁面寫作「階段 1：FineWeb-2 合成回譯 50 萬句 -> 階段 2：SONAR 標準品質 -> 階段 3：SONAR 高品質 -> 階段 4：官方驗證集收斂」。原文 §2.3.3（pp. 227–228）與表 1（p. 226）之真實順序為：**階段 1：OPUS 標準品質多語資料**（$3.0 \le \text{SONAR} < 3.7$，含俄、吉、烏茲別克、塔吉克四語全方向共 8,207,314 句）-> **階段 2：OPUS 高品質多語資料**（$\text{SONAR} \ge 3.7$，7,069,840 句）-> **階段 3：FineWeb-2 開源合成回譯資料**（由 50 萬篇吉爾吉斯語文件切出 1,849,234 段，經 Gemma-3-27B 與 Qwen3-235B 回譯及 MADLAD-400-7B-MT 交叉熵 $(0.1, 4.5)$ 過濾後保留 1,566,927 句對、雙向 3,133,854 句）-> **階段 4：SiberianPersonaChat 高品質合成對話資料**（由 GPT-4o 翻譯之 56,529 段俄吉對話、雙向 113,058 句，絕非在官方驗證集上訓練）。另漏述烏茲別克語／塔吉克語輔助遷移（§2.3.1）與 `mt0-large` 詞表剪枝（1.23B 至 800M，§2.3.2）。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Data-Centric Approach at the LoResMT 2026 Turkic Translation.pdf`（§2.1.1 p. 226 表 1、§2.3.1–2.3.3 pp. 227–228）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）

### EK-086 | open | concepts/formosan-computational-linguistics.md | Frontmatter 與關鍵突破支柱 | 原文不符
- **問題**：（1）Frontmatter `papers`（第 13 行）將研究臺灣閩南語（漢藏語系漢語族）之 `2024-taiwanese-mt-resegmentation-tang` 列入「臺灣南島語計算語言學」概念頁。（2）第 48–50 行重述 `2025-atayalic-oov-enumeration-yang.md` 之錯誤，稱楊鈞凱（2025）「利用音韻變化規則與構詞律正向窮舉所有合法衍生形」（實為子字串候選詞根挑選搭配成對隨機森林循環賽投票，且正向書寫形式比對篩選因有害而未執行，見 EK-067）。（3）第 57 行稱 Gagnier（2026）「利用正規化 Levenshtein 編輯距離與多維度對齊，量化臺灣南島語 16 族 42 方言」（漏述 TF-IDF 餘弦與 Jaccard 相似度且原文無多維尺度對齊，見 EK-079）。
- **來源**：同 EK-065、EK-067、EK-079
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理（部分）**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。第 (1) 點：已自 `papers` 移除 `2024-taiwanese-mt-resegmentation-tang`，論文頁 `concepts` 同步移除。第 (2) 點：依 EK-067 回原文確認之結果改寫楊鈞凱（2025）段；同時改寫「構詞解析與深層原形還原」段，刪除「未知表面形能準確逆向對映」之過度表述，註明解析需已知詞根。第 (3) 點（Gagnier 2026）尚未處理，本筆維持 open。

### EK-087 | fixed | concepts/low-resource-machine-translation.md | 關鍵技術路徑 | 原文不符
- **問題**：第 49–52 行將構詞特徵增強寫為詞根嵌入與詞綴嵌入拼接投影 $e(w) = W_{\text{proj}}[e_{\text{root}}(w) \,\|\, e_{\text{affix}}(w)]$ 並歸給游景勝（2021）與金柏毅（2025）；惟游景勝（2021）實驗證實詞根嵌入使 BLEU 暴跌、最佳模型係使用表面詞形搭配 52 維詞綴特徵（見 EK-062），而金柏毅（2025）最佳模型 `FC_ftr_jnt` 係使用雙獨立並聯 Transformer Encoder 分別編碼「詞綴字串形式子詞」與「詞綴組合特徵向量」後於編碼器輸出端串接（見 EK-066）。
- **來源**：同 EK-062、EK-066
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。依 EK-062、EK-066 回原文確認之結果改寫「構詞特徵增強」段：刪除無來源之 $W_{\text{proj}}$ 拼接式，改述游景勝（2021）之布林特徵拼接（含預訓練嵌入下 BLEU 下降之反例）與金柏毅（2025）之 FC_ftr_jnt 雙 encoder；同節「跨語言遷移」段一併依廖恒慶（2023）原文改寫，刪除原文未測量之「降低 OOV 率」「零樣本遷移」。
