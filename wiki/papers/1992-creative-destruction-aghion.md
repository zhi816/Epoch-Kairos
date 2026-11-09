---
title: "A Model of Growth Through Creative Destruction"
title_zh: "創造性破壞與內生經濟成長模型（Aghion-Howitt 熊彼特成長理論）"
paper_year: 1992
award_year: 2025
timeline_year: 2025
authors: "Philippe Aghion, Peter Howitt"
laureates: "Joel Mokyr, Philippe Aghion, Peter Howitt"
venue: "Econometrica, 60(2), 323-351"
honor: "2025 諾貝爾經濟學獎（表彰對創新驅動經濟成長與創造性破壞理論之闡明）"
domain: "econ"
domain_tags: ["#宏觀經濟學", "#制度經濟學"]
concepts: ["institutions-and-macro-dynamics"]
status: "wiki"
verification: "verified"
my_focus: false
doi_url: "https://doi.org/10.2307/2951599"
key_papers:
  - "Aghion, P., & Howitt, P. (1992) A Model of Growth Through Creative Destruction. Econometrica 60(2):323-351. https://doi.org/10.2307/2951599"
  - "Romer, P. M. (1990) Endogenous Technological Change. Journal of Political Economy 98(5):S71-S102. https://doi.org/10.1086/261725"
  - "Aghion, P., Bloom, N., Blundell, R., Griffith, R., & Howitt, P. (2005) Competition and Innovation: An Inverted-U Relationship. Quarterly Journal of Economics 120(2):701-728. https://doi.org/10.1093/qje/120.2.701"
hook: "將熊彼特「創造性破壞」化為嚴謹的動態隨機一般均衡方程，證明長期經濟成長源自新技術對舊獨占者的不斷淘汰。"
---

# 創造性破壞與內生經濟成長模型（Aghion-Howitt 熊彼特成長理論）

> 「經濟成長並非平靜的資本累積，而是一場永不停歇的工業新陳代謝：每一次技術飛躍，都必然伴隨著既有技術租金的毀滅。」

**1992 發表 ｜ 2025 諾貝爾經濟學獎**

> **本頁範圍說明**：2025 年諾貝爾經濟學獎由 Joel Mokyr（1/2）與 Philippe Aghion、Peter Howitt（合得 1/2）共享，表彰其對「創新驅動之長期經濟成長」的理論與歷史闡釋。本頁以 Aghion 與 Howitt 於 1992 年發表於《Econometrica》之奠基論文為主軸；Joel Mokyr 以技術史與知識制度之研究獲獎，並非本篇論文之作者。

---

## Card 1 ｜ 時代銘文 (The Hook)
為何人類社會在工業革命後能維持兩百年的持續人均成長，而個別企業帝國卻不斷興衰更替？Joseph Schumpeter 在 1942 年提出「創造性破壞（Creative Destruction）」的直覺洞見，但長達半世紀無法寫入宏觀經濟學的均衡方程式。Aghion 與 Howitt (1992) 首度以垂直品質階梯（Quality Ladder）與泊松研發到達過程建立內生成長模型，讓「創新淘汰舊產業」成為現代宏觀經濟學可定量求解的核心引擎。

---

## Card 2 ｜ 世紀瓶頸：新古典外生殘差與無淘汰創新的盲區 (The Dilemma)
在 1992 年之前，宏觀成長理論面臨兩大理論瓶頸：

* **索洛模型（Solow Model, 1956）的黑箱殘差**：新古典成長模型將長期人均產出成長完全歸因於「外生技術進步（Solow Residual）」，無法解釋研發投資、專利制度與市場結構如何內生決定成長率。
* **水平多樣化模型忽略了「過時與淘汰」**：Romer (1990) 雖開創了基於產品種類擴張的內生成長模型，但假設新產品與舊產品永遠並存、永不淘汰。這無法解釋現實產業中「數位相機淘汰底片、智慧型手機淘汰功能機」的企業更替、摩擦性失業與既得利益者的政治阻撓。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
Aghion 與 Howitt 將經濟體建模為一連串由研發（R&D）驅動的垂直品質躍遷過程，每一代新中間財都會完全取代上一代，摧毀前任創新者的獨占租金。

1. **泊松創新到達過程（Poisson Arrival of Innovations）**：
   * 當研發部門投入數量為 $n_t$ 的高技術研究勞動力時，下一次技術突破以泊松抵達率 $\lambda \phi(n_t)$ 發生。每次突破使中間財生產率提升固定倍數 $\gamma > 1$。
2. **跨期前瞻性研發套利均衡（Forward-Looking R&D Arbitrage）**：
   * 當前第 $t$ 代創新者的獨占利潤，取決於**下一代第 $t+1$ 次創新何時到來**。若未來預期的研發強度 $n_{t+1}$ 越高，當前專利的預期存活壽命就越短，從而抑制當前的研發意願。這構成了跨期負向回饋關係：$n_t = \hat{n}(n_{t+1})$。
3. **租金竊取效應與社會最優偏離（Business-Stealing vs. Intertemporal Spillover）**：
   * 私人創新者在決策時，一方面忽略了自身創新對未來所有世代知識基底的永久墊高（跨期正外部性，使私人研發不足），另一方面卻將奪取前人獨占租金視為自身淨收益（業務竊取負外部性，使私人研發過度）。因此，自由市場的均衡成長率可能高於或低於社會福利最優成長率。

### 1. 最終財生產函數與垂直品質階梯 (Production & Quality Ladder)

在聚焦於中間財 $x$ 與研發配置的核心基準模型中，最終財產出 $y$ 由中間財投入 $x$ 與當代技術水準 $A_t$ 決定：

$$\begin{aligned}
y_t &= A_t F(x_t) = A_t x_t^\alpha, \quad (0 < \alpha < 1) \\
A_t &= A_0 \gamma^t, \quad (\gamma > 1)
\end{aligned}$$

其中 $t \in \{0, 1, 2, \dots\}$ 代表迄今已發生的累計成功創新次數，每次創新使全要素生產率躍升 $\gamma$ 倍。總勞動力 $N$ 在製造部門 $x_t$ 與研發部門 $n_t$ 之間滿足資源出清條件：

$$N = x_t + n_t$$

### 2. 創新價值泛函與跨期研發套利方程 (Bellman Value & R&D Arbitrage)

令 $V_{t+1}$ 為第 $t+1$ 次創新成功者所能獲得的期望貼現獨占價值。在利率為 $r$、下一期研發投入為 $n_{t+1}$ 的條件下，該專利以泊松速率 $\lambda \phi(n_{t+1})$ 被第 $t+2$ 次創新摧毀，因此「有效貼現率」為 $r + \lambda \phi(n_{t+1})$：

$$V_{t+1} = \frac{\pi_{t+1}}{r + \lambda \phi(n_{t+1})}$$

其中 $\pi_{t+1}$ 為第 $t+1$ 代獨占者的單期利潤流。在線性研發技術 $\phi(n) = n$ 下，自由進入之研發套利條件要求「邊際研發工資成本」等於「創新成功機率乘以期望專利價值」：

$$\begin{aligned}
w_t &= \lambda V_{t+1} \\
\implies \quad \frac{w_t}{A_t} &= \frac{\lambda \gamma \tilde{\pi}(n_{t+1})}{r + \lambda n_{t+1}}
\end{aligned}$$

此方程完美刻畫了「創造性破壞」的雙重性：分母中的 $\lambda n_{t+1}$ 即為未來創新對當前專利價值的折舊毀滅率。

### 3. 穩態內生經濟成長率與方差 (Steady-State Growth Rate)

在平穩均衡（Stationary Equilibrium，$n_t = \hat{n}$）下，若設定研發成功率為研究勞動力的線性函數 $\phi(n) = n$，對數產出 $\ln y(\tau)$ 在連續時間長度為 $1$ 的區間內服從複合泊松過程，其長期平均對數成長率（Average Growth Rate, $g$）與成長波動方差（Variance, $\sigma^2$）皆由研發投入 $\hat{n}$ 內生決定（式 2.16–2.17）：

$$\begin{aligned}
g &= \mathbb{E}[\ln y(\tau + 1) - \ln y(\tau)] = \lambda \hat{n} \ln \gamma \\
\sigma^2 &= \operatorname{Var}[\ln y(\tau + 1) - \ln y(\tau)] = \lambda \hat{n} (\ln \gamma)^2
\end{aligned}$$

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Aghion & Howitt 1992）之核心理論證明
* **穩態均衡與內生極限環（Limit Cycles）條件**：作者分析跨期研發套利映射 $n_t = \psi(n_{t+1})$。在基準模型中存在唯一平穩穩態 $\hat{n}$；在特定參數條件下（當跨期映射在穩態之導數 $\psi'(\hat{n}) < -1$ 時），穩態局部不穩定，經濟體將內生湧現「繁榮（高研發、高產出、預期低折舊）與蕭條（低研發、低產出、預期高折舊）交替」的 2 階極限環（2-Cycle / Schumpeterian Wave，Proposition 2）。原文將此作為創造性破壞產生內生波動機制的理論展示，並非宣稱該極限環已能直接解釋現實世界的複雜實證商業週期。
* **福利雙向偏離定理**：推導出社會計畫者（Social Planner）的有效貼現率為 $r + \lambda(1 - \gamma)\hat{n}$，與私人市場的 $r + \lambda \hat{n}$ 對比，證明當創新步幅 $\gamma$ 較小時，「業務竊取效應（Business-Stealing Effect）」與「壟斷扭曲效應」可能壓倒知識外溢效應，導致自由放任市場出現過度研發（Over-investment in R&D）。
* **顛覆性大創新對增量研發的擠出**：在連續研發步幅擴展模型中，證明私人企業傾向選擇「恰好足以奪取市場」的短視創新步幅，而低估長遠基礎躍遷的社會價值。

### 後續領域關鍵實證（非本篇成果，標註出處）
* **競爭與創新的倒 U 型曲線（Inverted-U Relationship）**：Aghion, Bloom, Blundell, Griffith & Howitt (2005), *Quarterly Journal of Economics* 120(2):701-728，結合英國面板專利數據與熊彼特模型，實證發現在頸部競爭（Neck-and-Neck）產業中，適度競爭會激發「逃離競爭效應（Escape-Competition Effect）」，而過度競爭則抑制落後者的創新回報，整體呈顯著倒 U 型。
* **企業動態與創造性破壞的微觀量化**：Klette & Kortum (2004), *Journal of Political Economy* 112(5):986-1018 與 Akcigit & Kerr (2018), *Journal of Political Economy* 126(4):1374-1443，利用美國人口普查局微觀企業數據，量化驗證新創企業的激進創新（External Creative Destruction）與既有大企業的內部改良對總體 TFP 成長的貢獻比例。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **啟發動態反壟斷與產業競爭政策框架**：為產業組織學提供分析動態市場進入與技術取代的微觀基礎。隨後的政策與文獻將其延伸至現代反壟斷審查（例如 Cunningham, Ederer & Ma (2021, *Journal of Political Economy*) 針對預防性收購以扼殺潛在創新競爭者的「扼殺式收購 Killer Acquisitions」研究），利用創造性破壞架構評估專利壟斷保護與動態競爭激勵之間的權衡（非 1992 原始論文之直接檢驗結果）。
* **微觀企業數據與宏觀成長的統一**：使宏觀經濟學得以直接利用專利引用、企業出生率（Entry Rate）、退出率（Exit Rate）與職位創造/毀滅（Job Reallocation）數據來診斷國家經濟活力。
* **制度政治經濟學的延伸**：解釋了為何既得利益集團（Incumbents）在面對通用目的技術（如蒸汽機、電力、人工智慧）時，會遊說政府築起監管高牆以阻止「創造性破壞」，從而導致中等收入陷阱與長期停滯。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
Aghion-Howitt 模型的哲學精髓在於揭示了**「穩定（Stability）」與「演化（Evolution）」的深刻張力**：

1. **沒有退出機制的系統終將僵化**：無論是生物演化中的物種更替、深度學習中的權重修剪，還是宏觀經濟中的企業破產重整，長期適應力的提升都以局部舊結構的有序淘汰為前提。
2. **預期壽命決定當下創造力**：創新者不僅看重當下的獎勵，更看重制度能否在「保護創新果實」與「允許後浪推前浪」之間維持精妙的動態平衡。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [制度演化與宏觀經濟動態](../concepts/institutions-and-macro-dynamics.md)
* **原始權威文獻**：
  * 官方學術出處：Aghion, P., & Howitt, P. (1992). Econometrica, 60(2), 323-351. DOI: [10.2307/2951599](https://doi.org/10.2307/2951599)
  * 原始檔典藏：`raw/1992-creative-destruction-aghion.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 獎項通告：[The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2025](https://www.nobelprize.org/prizes/economic-sciences/2025/)
