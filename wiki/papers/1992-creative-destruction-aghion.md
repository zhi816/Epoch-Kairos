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
card_line: "新技術淘汰舊技術，經濟才能長期成長"
---

# 創造性破壞與內生經濟成長模型（Aghion-Howitt 熊彼特成長理論）

> 「經濟成長並非平靜的資本累積，而是一場永不停歇的工業新陳代謝：每一次技術飛躍，都必然伴隨著既有技術租金的毀滅。」

**1992 發表 ｜ 2025 諾貝爾經濟學獎**

> **本頁範圍說明**：2025 年諾貝爾經濟學獎由 Joel Mokyr（1/2）與 Philippe Aghion、Peter Howitt（合得 1/2）共享，表彰其對「創新驅動之長期經濟成長」的理論與歷史闡釋。本頁以 Aghion 與 Howitt 於 1992 年發表於《Econometrica》之奠基論文為主軸；Joel Mokyr 以技術史與知識制度之研究獲獎，並非本篇論文之作者。

---

## Card 1 ｜ 時代銘文 (The Hook)
Aghion 與 Howitt (1992) 建立一個由垂直產品創新推動的內生成長模型：研發以泊松過程產生新中間財，每次創新提高生產率並使前一代產品過時、摧毀既有創新者的壟斷租金。這把熊彼特式創造性破壞寫入一個可分析的均衡模型。

---

## Card 2 ｜ 理論瓶頸：產品創新與過時 (The Dilemma)
本文引言將研究問題定位為：把工業產品創新（改善產品品質並使舊品過時）納入內生成長模型。

* **從知識累積到產品創新**：作者指出，既有內生成長文獻已研究知識累積，而本文聚焦於改善產品品質的工業創新。
* **水平多樣化模型不含產品淘汰**：作者指出，Judd (1985) 與 Romer (1990) 以水平產品創新建模，新產品並不優於既有產品，因此不會使舊品過時。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
Aghion 與 Howitt 將經濟體建模為一連串由研發（R&D）驅動的垂直品質躍遷過程，每一代新中間財都會完全取代上一代，摧毀前任創新者的獨占租金。

1. **泊松創新到達過程（Poisson Arrival of Innovations）**：
   * 當研發部門投入數量為 $n_t$ 的高技術研究勞動力時，下一次技術突破以泊松抵達率 $\lambda \phi(n_t)$ 發生。每次突破使中間財生產率提升固定倍數 $\gamma > 1$。
2. **跨期前瞻性研發套利均衡（Forward-Looking R&D Arbitrage）**：
   * 當前第 $t$ 代創新者的獨占利潤，取決於**下一代第 $t+1$ 次創新何時到來**。若未來預期的研發強度 $n_{t+1}$ 越高，當前專利的預期存活壽命就越短，從而抑制當前的研發意願。這構成了跨期負向回饋關係：$n_t = \psi(n_{t+1})$。
3. **租金竊取效應與社會最優偏離（Business-Stealing vs. Intertemporal Spillover）**：
   * 私人創新者在決策時，一方面忽略了自身創新對未來所有世代知識基底的永久墊高（跨期正外部性，使私人研發不足），另一方面卻將奪取前人獨占租金視為自身淨收益（業務竊取負外部性，使私人研發過度）。因此，自由市場的均衡成長率可能高於或低於社會福利最優成長率。

### 1. 最終財生產函數與垂直品質階梯 (Production & Quality Ladder)

一般基準模型的最終財生產函數為 $y_t=A_tF(x_t)$（式 2.1）；作者另以 Cobb–Douglas 作為特例，令 $F(x)=x^\alpha$、$0<\alpha<1$（式 2.8）。每次成功創新使技術水準 $A_t$ 提高固定倍數 $\gamma>1$，因此（式 2.3）：

$$\begin{aligned}
y_t &= A_t F(x_t) \\
A_t &= A_0 \gamma^t
\end{aligned}$$

其中 $t \in \{0, 1, 2, \dots\}$ 代表迄今已發生的累計成功創新次數。總勞動力 $N$ 在製造部門 $x_t$ 與研發部門 $n_t$ 之間滿足資源出清條件：

$$N = x_t + n_t$$

### 2. 創新價值泛函與跨期研發套利方程 (Bellman Value & R&D Arbitrage)

令 $V_{t+1}$ 為第 $t+1$ 次創新成功者所能獲得的期望貼現獨占價值。在利率為 $r$、下一期研發投入為 $n_{t+1}$ 的條件下，該專利以泊松速率 $\lambda \phi(n_{t+1})$ 被下一次創新摧毀。原文的專利價值式為（§2.C，式 2.12）：

$$V_{t+1} = \frac{\pi_{t+1}}{r + \lambda \phi(n_{t+1})}$$

其中 $\pi_{t+1}$ 為第 $t+1$ 代獨占者的利潤流。自由進入下的研發條件為 $w_t \geq \lambda\phi'(n_t)V_{t+1}$，且正研發投入時取等號（式 2.10）；在線性研發技術 $\phi(n)=n$ 下簡化為：

$$w_t = \lambda V_{t+1}$$

### 3. 穩態內生經濟成長率與方差 (Steady-State Growth Rate)

在平穩均衡（Stationary Equilibrium，$n_t = \hat{n}$）下，對數產出 $\ln y(\tau)$ 在連續時間長度為 $1$ 的區間內服從複合泊松過程，其長期平均對數成長率（Average Growth Rate，$g$）與成長波動方差（Variance，$\sigma^2$）皆由研發投入 $\hat{n}$ 內生決定（式 3.11，§3.C，p. 336）：

$$\begin{aligned}
g &= \mathbb{E}[\ln y(\tau + 1) - \ln y(\tau)] = \lambda \phi(\hat{n}) \ln \gamma \\
\sigma^2 &= \operatorname{Var}[\ln y(\tau + 1) - \ln y(\tau)] = \lambda \phi(\hat{n}) (\ln \gamma)^2
\end{aligned}$$

在線性研發技術 $\phi(n) = n$ 之特例下，兩式化為 $g = \lambda \hat{n} \ln \gamma$ 與 $\sigma^2 = \lambda \hat{n} (\ln \gamma)^2$；原文以此通式推導，線性特例僅用於後續 Cobb–Douglas 比較靜態分析。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Aghion & Howitt 1992）之核心理論證明
* **穩態均衡與內生 2 階循環（Two-Cycle）條件**：作者分析跨期研發套利映射 $n_t = \psi(n_{t+1})$。基準模型存在唯一平穩穩態 $\hat{n}$；當無成長陷阱（No-Growth Trap）存在且 $c'(\hat{n}) + b'(\hat{n}) > 0$ 時，可出現高研發與低研發交替之實質 2 階循環（一般存在條件 §3.A, p. 333；Cobb–Douglas 特例 p. 334）。在 Cobb–Douglas 生產函數與線性研發技術 $\phi(n) = n$ 之特例下，該條件約化為競爭程度參數 $\alpha$ 與利率 $r$ 足夠小（$1-\alpha$ 為 Lerner 壟斷力，故 $\alpha$ 越小表市場力量越大）。原文將此循環定位為創造性破壞導致內生波動之理論展示，並未宣稱可直接解釋現實商業週期；全文僅有 Proposition 1（p. 334），未以 $\psi'(\hat{n}) < -1$ 表述穩定條件，亦未使用「極限環（limit cycle）」一詞。
* **福利效果的方向取決於多種扭曲**：社會計畫者的折現率為 $r-\lambda\phi(n)(\gamma-1)$，而私人專利估值的折現率為 $r+\lambda\phi(n)$。業務竊取、壟斷扭曲、可占有性與跨期外溢的效果彼此牴觸，因此自由放任下的成長可能高於或低於社會最適；在線性 Cobb–Douglas 例中，當市場力量較大（$\alpha$ 接近 0）且創新幅度不大時，業務竊取效應可主導並導致過度研發。
* **自由放任下的創新幅度偏小**：第 6 節讓研究企業同時選擇創新頻率與幅度；在顛覆性創新情形下，私人企業選擇的創新幅度低於社會最適。非顛覆性創新下，利潤率誘因會部分抵銷這一傾向；總體成長效果方向仍不確定。

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
