# 已結案問題：papers/1992-creative-destruction-aghion.md

> 本檔收錄 [wiki/papers/1992-creative-destruction-aghion.md](../../../papers/1992-creative-destruction-aghion.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

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
- **問題**：[證據表](../../../evidence/1992-creative-destruction-aghion.md) 第 2 行寫「封存版本見 `raw/1992-creative-destruction-aghion.pdf`」，並據以將各列標為「符合來源」（引用 *Econometrica* pp. 323–351 之式 (2.1)–(2.17) 等位置）。但該封存檔實為 Giuseppe Bertola, "Factor Shares and Savings in Endogenous Growth", NBER Working Paper No. 3851（1991 年 9 月，31 頁，純圖片、無文字層），並非 Aghion and Howitt (1992)；全檔僅參考文獻提及 Aghion 一次。證據表各列之頁碼與公式位置無法以封存檔核實，頁面 `verified` 狀態缺乏可追溯之來源。須由使用者將封存檔換為 *Econometrica* 正式版後，依原文重新核對證據表各列。
- **來源**：封存檔 `raw/1992-creative-destruction-aghion.pdf` 第 1–2 頁（標題頁與摘要）及第 16、30–31 頁（以 MinerU 本機 OCR 確認內容）；正式版 *Econometrica* 60(2): 323–351，https://doi.org/10.2307/2951599
- **發現於**：wiki/log.md [2026-11-09 15:13] fix（Claude Code by Anthropic）
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。改採 Econometrica 正式版全文（JSTOR 掃描複本，由 University of Copenhagen 網站提供：https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf；DOI: https://doi.org/10.2307/2951599），逐列重核證據表並更正公式與頁碼。raw/1992-creative-destruction-aghion.pdf 仍是 Bertola 的 NBER WP 3851，依 raw 唯讀規範保留、不作為證據來源；此條改以正式版可追溯來源解決，不再要求該檔作為核實前提。

### EK-090 | fixed | papers/1992-creative-destruction-aghion.md | Card 3–4 與證據表 | 原文不符
- **問題**：EK-003 之處理行與證據表列「§2.4, p. 333, 式 (2.16)–(2.17)」，並稱 2 階循環為「Proposition 2」、於跨期映射導數 $\psi'(\hat{n}) < -1$ 時湧現。惟 *Econometrica* 正式版全文僅有 Proposition 1（p. 334），無式 (2.16)–(2.17)；平均成長率與方差實為 §3.C 之式 (3.11)（p. 336），原文寫作 $AGR=\lambda\phi(\hat{n})\ln\gamma$、$VGR=\lambda\phi(\hat{n})(\ln\gamma)^2$，$\lambda\hat{n}\ln\gamma$ 僅為線性研發 $\phi(n)=n$ 之特例。2 階循環（two-cycle）之存在條件為無成長陷阱存在且 $c'(\hat{n})+b'(\hat{n})>0$（§3.A, p. 333）；Cobb–Douglas 線性研發下，$\alpha$ 與 $r$ 足夠小時可出現實質 two-cycle（§3.A, p. 334）；原文未以 $\psi'(\hat{n})<-1$ 表述，亦未使用「極限環（limit cycle）」一詞。
- **來源**：*Econometrica* 60(2): 323–351 正式版掃描本（JSTOR stable 2951599），p. 333、p. 334、p. 336；https://doi.org/10.2307/2951599
- **發現於**：wiki/log.md [2026-11-09 20:12] fix（DeepSeek Harness）
- **處理**：2026-11-09，DeepSeek Harness（DeepSeek-V4.1-Flash）。回正式版掃描本核對後修正：論文頁 Card 3 改引式 (3.11)（§3.C, p. 336），成長率與方差改以 $\lambda\phi(\hat{n})$ 通式表述並註明線性研發特例；Card 4 刪除「Proposition 2」與 $\psi'(\hat{n})<-1$ 之無來源條件，改述 two-cycle 之實際存在條件。證據表同步更正兩列之位置與敘述。EK-003 原處理行之錯誤引用由本條更正。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。再核對期刊全文後明確拆分頁碼：一般 two-cycle 條件在 p. 333；Cobb–Douglas 線性研發下「$\alpha$ 與 $r$ 足夠小」的特例在 p. 334。論文頁與證據表均同步更正，避免把特例錯標為 p. 332–333。

### EK-203 | fixed | papers/1992-creative-destruction-aghion.md | Card 3 區塊公式 | 未能核實
- **問題**：依正式版線上文字，式 (2.1) 寫 $y=AF(x)$，頁面額外加上下標；頁面以線性特例展示的研發條件與式 (2.10) 的一般不等式形式不同；頁面以 $g$、$\sigma^2$ 與期望、變異數擴寫式 (3.11)，原文以 AGR、VGR 表達。須核對正式版掃描頁，逐式判斷是否為原文或 Wiki 推導，並依規範改寫、登記來源。
- **來源**：[Econometrica 正式版](https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf) pp. 327–330、332、336，式 (2.1)、(2.3)、(2.10)、(2.12)、(3.11)；[證據表](../../../evidence/1992-creative-destruction-aghion.md)。
- **發現於**：2026-11-10，處理 TD-011，Codex by OpenAI。`raw/` 檔案為其他論文；正式版線上文字可讀，但本環境無法取得掃描頁影像核對，尚未把文字擷取當作公式最終證據。
- **處理**：2026-11-13，Antigravity by Google DeepMind（Gemini 4 Hydrogen）。經使用者授權自 Wayback Machine 存檔之 `https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf` 下載 JSTOR 正式版掃描全本並取代 `raw/1992-creative-destruction-aghion.pdf`，將印刷頁 pp. 323–343（PDF pp. 2–22）轉為影像逐式核對：(1) 式 (2.1) 改為原文 $y = AF(x)$（p. 327）、式 (2.3) 獨立列為 $A_t = A_0 \gamma^t \ (t = 0, 1, \dots)$（p. 328），並將無對應編號展示式之 $N = n_t + x_t$ 改為行內引用（§3.A, p. 331）；(2) 式 (2.12) 與式 (2.10) 皆依原文將單變數研發函數符號改為 $\varphi$（$\varphi(n_t) \equiv \phi(n_t, R)$，p. 330），區塊公式 4 改列原文完整 Kuhn–Tucker 條件 $w_t \ge \varphi'(n_t)\lambda V_{t+1},\; n_t \ge 0,\; \text{with at least one equality}$，線性特例 $w_t = \lambda V_{t+1}$ 改為行內推導說明；(3) 式 (3.11) 改為原文 $AGR = \lambda \varphi(\hat{n}) \ln \gamma,\; VGR = \lambda \varphi(\hat{n}) (\ln \gamma)^2$（p. 336），移除未見於該式之 $g$、$\sigma^2$ 與 $\mathbb{E}$、$\operatorname{Var}$ 擴寫；(4) 同步更新 `wiki/cards/1992-creative-destruction-aghion.md` Card 3 公式之 $\varphi$ 符號與 `wiki/evidence/1992-creative-destruction-aghion.md` 區塊公式 1–5 逐條位置，覆核全頁 Frontmatter、Card 1–6 與 Crossref 後續論文書目後，將論文頁 `verification` 設為 `verified`。

### EK-225 | fixed | papers/1992-creative-destruction-aghion.md | Card 4–5 後續研究歸因 | 未能核實
- **問題**：Card 5 原第 2 點稱後續研究使宏觀經濟學能直接以專利引用、企業進出率及職位創造／毀滅資料診斷國家經濟活力；原第 3 點稱既得利益者面對通用目的技術時會遊說政府築起監管高牆，並因此造成中等收入陷阱與長期停滯，兩者均未列第一手來源或精確位置。複核另發現 Card 4 將 Klette & Kortum (2004) 與 Akcigit & Kerr (2018) 合併描述成使用美國人口普查資料、量化新創企業與既有大企業對總體 TFP 的貢獻比例；前者來源是企業創新的一般均衡理論模型，後者工作論文版區分探索型與利用型研發並以企業及專利資料檢驗模型預測，原列未支持該歸因與 TFP 貢獻比例說法。
- **來源**：[論文頁 Card 4–5](../../../papers/1992-creative-destruction-aghion.md)；[證據表](../../../evidence/1992-creative-destruction-aghion.md)；[Klette & Kortum NBER WP 8819](https://www.nber.org/papers/w8819) 摘要、§1；[Akcigit & Kerr NBER WP 16443](https://www.nber.org/papers/w16443) 摘要、§1、§3.1。NBER 書目頁分別列出 JPE 2004 與 2018 發表版本；本次未取得兩篇正式版全文，論文頁明示依據工作論文版本的主張。
- **發現於**：wiki/log.md [2026-11-14 11:05] audit（Codex by OpenAI）。
- **處理**：2026-11-14，Codex by OpenAI（GPT-6）。移除 Card 5 無直接來源的國家活力診斷，以及既得利益者遊說導致中等收入陷阱與長期停滯之因果主張；重寫 Card 4，分開記錄 Klette & Kortum 的企業創新一般均衡模型，以及 Akcigit & Kerr 工作論文版的探索型／利用型研發、資料來源與專利引用結果，移除未被支持的企業類型 TFP 貢獻比例。同步修訂 Card 5 里程碑、證據表與論文頁，將 verification 設為 partial；正式 JPE 全文未取得，現行文字已明示所採工作論文版本，詳見證據表。
