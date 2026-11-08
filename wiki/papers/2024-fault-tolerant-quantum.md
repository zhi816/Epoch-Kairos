---
title: "Logical quantum processor based on reconfigurable atom arrays"
title_zh: "可重構中性原子陣列之邏輯量子處理器：邁向容錯量子計算的歷史跨越"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Dolev Bluvstein, Simon J. Evered, Alexandra A. Geim, Sophie H. Li, Hengyun Zhou, Tom Manovitz, Sepehr Ebadi, Madelyn Cain, Marcin Kalinowski, Dominik Hangleiter et al., Markus Greiner, Vladan Vuletić, Mikhail D. Lukin"
venue: "Nature, 626(7997), 58-65"
domain: "physics"
domain_tags: ["#量子物理", "#統計物理"]
concepts: ["quantum-error-correction"]
status: "wiki"
my_focus: false
doi_url: "https://doi.org/10.1038/s41586-023-06927-3"
key_papers:
  - "Shor, P. W. (1995) Scheme for reducing decoherence in quantum computer memory. Physical Review A 52(4):R2493-R2496. https://doi.org/10.1103/PhysRevA.52.R2493"
  - "Kitaev, A. Y. (2003) Fault-tolerant quantum computation by anyons. Annals of Physics 303(1):2-30. https://doi.org/10.1016/S0003-4916(02)00018-0"
  - "Bluvstein, D. et al. (2024) Logical quantum processor based on reconfigurable atom arrays. Nature 626(7997):58-65. https://doi.org/10.1038/s41586-023-06927-3"
  - "Google Quantum AI and Collaborators (2024) Quantum error correction below the surface code threshold. Nature 638:920-926. https://doi.org/10.1038/s41586-024-08449-y"
hook: "利用光學鑷子在計算過程中即時移動糾纏中性銣原子，首次在單一處理器上同時編碼多達 48 個邏輯量子位元並執行橫向容錯邏輯閘，打破超導固定晶格的二維近鄰連接限制。"
---

# 可重構中性原子陣列之邏輯量子處理器：邁向容錯量子計算的歷史跨越

> 「過去量子位元像被焊死在棋盤上的棋子，只能與隔壁鄰居緩慢交換資訊；光學鑷子讓中性原子在保持量子相干的同時凌空起舞，將三維高維度量子糾錯碼化為現實。」

**2024 發表 ｜ 容錯量子計算與邏輯量子位元突破**

> **本頁範圍說明**：本條目對應 `raw/2024-fault-tolerant-quantum.pdf`，為哈佛大學 Mikhail D. Lukin 團隊聯合 QuEra、MIT 與馬里蘭大學發表於《Nature》第 626 卷第 7997 期（頁 58–65）之里程碑論文。經 Crossref 核驗（DOI: `10.1038/s41586-023-06927-3`），該文於 2023 年 12 月 6 日先行線上刊出（Online First），正式紙本卷期出版日期為 **2024 年 2 月 1 日**，故依正式期刊卷期年份定 `paper_year: 2024`。`key_papers` 一併列出 Google Quantum AI 於 2024 年底在超導表面碼實現低於閾值指數糾錯（Willow 處理器）之互補里程碑。

---

## Card 1 ｜ 時代銘文 (The Hook)
物理量子位元（Physical Qubits）極度脆弱，環境熱擾動、雷射相位雜訊與自發輻射會在毫秒內摧毀量子疊加態（退相干）。自 Peter Shor (1995) 與 Alexei Kitaev (1997) 提出量子糾錯碼（Quantum Error Correction, QEC）以來，將多個物理量子位元冗餘編碼為受拓撲保護的「邏輯量子位元（Logical Qubits）」並在其上直接執行容錯邏輯閘，一直是量子計算的終極聖盃。然而，傳統超導量子晶片受限於平面固定佈線，僅能與相鄰位元交互，製造 1 個高碼距表面碼邏輯位元就需消耗上千個物理位元。哈佛大學 Lukin 與 Bluvstein 團隊利用聲光偏轉器（AOD）操控的可重構中性銣原子（$\mathrm{^{87}Rb}$）陣列，在計算途中**帶電相干搬運原子**，首次在 280 個物理位元上實現多達 **48 個邏輯量子位元** 與數百個橫向容錯邏輯閘（Transversal Logical Gates），正式揭開早期容錯量子計算（Early Fault-Tolerant QC）時代的序幕。

---

## Card 2 ｜ 世紀瓶頸：平面近鄰連線枷鎖與糾錯開銷的指數深淵 (The Dilemma)
在邁向實用容錯量子計算的道路上，硬體架構長期受制於三大物理瓶頸：

* **「愈糾愈錯」的閾值困境**：量子糾錯本身需要額外施加大量的雙量子位元閘（如 CNOT / CZ 閘）與輔助位元測量來提取錯誤症候群（Error Syndrome）。若物理閘保真度不夠高或線路過深，糾錯電路自身引入的錯誤反而比原本單一物理位元還多。
* **二維平面近鄰拓撲（2D Nearest-Neighbor）的巨額空間開銷**：在平面表面碼（2D Surface Code）上執行兩個邏輯量子位元之間的邏輯 CNOT 閘，傳統上需要透過複雜的「晶格手術（Lattice Surgery）」或「編織（Braiding）」，不僅需要 $O(d)$ 個時間步的重複症候群測量，且編碼率極低（$k/n \to 0$）。
* **中途測量對鄰近原子的光散射串擾（Mid-Circuit Readout Crosstalk）**：在中性原子系統中，若在演算法中途以螢光照射讀取輔助位元，散射光子會瞬間摧毀周圍資料位元的量子疊加態。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
Lukin 與 Bluvstein 團隊發明了**「三區分立動態架構（Zoned Architecture）」**，將中性原子的長相干超精細能階與動態光學鑷子完美結合：

1. **儲存區、糾纏區與讀取區之空間分離（Storage, Entangling & Readout Zones）**：
   * 量子資訊編碼於 $\mathrm{^{87}Rb}$ 原子基態超精細鐘態（Clock States，$|0\rangle = |F=1, m_F=0\rangle, |1\rangle = |F=2, m_F=0\rangle$），相干時間 $T_2 > 1.5\,\text{s}$。
   * 透過二維聲光偏轉器（2D AOD）移動光學鑷子，整個邏輯位元晶格可在不影響內部自旋相干性的前提下，在微秒至百微秒內整體平移至**糾纏區**（施加全局里德堡 Rydberg 激發雷射執行高保真度並行 CZ 閘，保真度 $99.5\%$），或將輔助位元單獨移入遠處的**讀取區**進行中途無損螢光成像。
2. **里德堡阻塞（Rydberg Blockade）與單步平行橫向邏輯閘（Transversal Entangling Gates）**：
   * 當將兩個分別編碼為表面碼（Surface Code）、色碼（Color Code）或高維超立方體碼（Hypercube Code）的邏輯量子位元區塊在空間上交錯平移，使第 $A$ 邏輯區塊的第 $i$ 個物理原子恰好停在第 $B$ 邏輯區塊的第 $i$ 個物理原子旁邊（間距 $\lesssim 3\,\mu\text{m}$，進入里德堡偶極阻塞半徑 $R_b$），僅需一道全局里德堡雷射脈衝，即可在單一時間步內同步完成全部物理位元對的平行控制相位閘，實現天然防止錯誤擴散的**橫向邏輯糾纏閘（Transversal Logical CNOT / CZ）**。
3. **高編碼率三维/四維超立方體量子碼（$[[8,3,2]]$ Color/Hypercube Codes）**：
   * 擺脫二維平面佈線束縛後，原子可透過遠程光鑷移動實現非局域全連接（All-to-All Connectivity），直接實作三維與四維拓撲碼，在僅用 8 個物理位元的區塊中同時編碼 3 個邏輯位元（編碼率高達 $3/8$）。

### 1. 里德堡偶極阻塞哈密頓量與雙原子受控相位閘 (Rydberg Blockade Hamiltonian)

當兩個相距為 $r_{ij}$ 的中性銣原子同時受到拉比頻率為 $\Omega$、失諧量為 $\Delta$ 的雷射耦合自基態 $|1\rangle$ 激發至高主量子數里德堡態 $|r\rangle$（如 $n=53S$ 或 $70S$）時，兩原子間的凡德瓦交互作用勢 $V(r_{ij}) = C_6 / r_{ij}^6$ 構成雙原子有效哈密頓量：

$$\begin{aligned}
\hat{H}_{\text{Ryd}} = &\;\frac{\hbar \Omega}{2} \sum_{q \in \{i, j\}} \left( e^{i\phi} |r\rangle_q\langle 1| + e^{-i\phi} |1\rangle_q\langle r| \right) \\
&- \hbar \Delta \sum_{q \in \{i, j\}} |r\rangle_q\langle r| + V(r_{ij}) |rr\rangle\langle rr|
\end{aligned}$$

當兩原子由 AOD 光鑷移近至里德堡阻塞半徑 $R_b \equiv (C_6 / \hbar \Omega)^{1/6}$ 以內時，滿足強阻塞條件 $V(r_{ij}) \gg \hbar \Omega$，雙激發態 $|rr\rangle$ 被能量高牆完全禁止；施加時間最優相位調制脈衝後，系統精確實現雙位元受控相位閘 $\mathrm{CZ} = \operatorname{diag}(1, 1, 1, -1)$。

### 2. 穩定子量子糾錯碼與橫向邏輯算符 (Stabilizer Formalism & Transversal Gates)

一個 $[[n, k, d]]$ 量子穩定子碼利用 $n$ 個物理位元的 $2^n$ 維希爾伯特空間中的一個 $2^k$ 維子空間 $\mathcal{C}$ 編碼 $k$ 個邏輯位元，由阿貝爾穩定子群 $\mathcal{S} = \langle S_1, S_2, \dots, S_{n-k} \rangle \subset \mathcal{P}_n$（其中 $S_m^\dagger = S_m, [S_m, S_{m'}] = 0, -I \notin \mathcal{S}$）定義：

$$\mathcal{C} = \left\{ |\psi_L\rangle \in (\mathbb{C}^2)^{\otimes n} \;\middle|\; S_m |\psi_L\rangle = +|\psi_L\rangle, \;\forall S_m \in \mathcal{S} \right\}$$

對於兩個各自編碼於 $n$ 個物理位元之 CSS 碼區塊 $A$ 與 $B$，橫向邏輯受控反閘（Transversal $\overline{\mathrm{CNOT}}_{A \to B}$）直接由逐對物理位元之張量積構成：

$$\overline{\mathrm{CNOT}}_{A \to B} = \bigotimes_{i=1}^{n} \mathrm{CNOT}_{A_i \to B_i}$$

由於第 $i$ 對物理位元之間沒有跨位元連線，單一物理位元上的局部錯誤最多只在區塊 $A$ 與區塊 $B$ 的第 $i$ 個位元間一對一傳遞，**絕不會在同一個邏輯區塊內部擴散成不可糾正的多位元錯誤**，此即容錯（Fault Tolerance）的數學本質。

### 3. 碼距指數抑制錯誤標度律 (Exponential Error Suppression with Code Distance)

當物理位元單步錯誤率 $p$ 低於糾錯碼與解碼器之容錯閾值 $p_{\text{th}}$ 時，隨碼距 $d$（奇數，可糾正 $\lfloor (d-1)/2 \rfloor$ 個任意物理錯誤）增加，邏輯錯誤率 $P_L$ 呈指數級壓低：

$$P_L(d) \propto \left( \frac{p}{p_{\text{th}}} \right)^{\frac{d+1}{2}} = \frac{1}{\Lambda^{(d+1)/2}}$$

其中 $\Lambda = p_{\text{th}} / p > 1$ 為錯誤抑制因子。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Bluvstein et al. 2024）之核心證據
* **隨碼距 $d=3 \to 5 \to 7$ 糾纏邏輯態保真度單調提升**：在雙邏輯量子位元表面碼（Surface Code）橫向糾纏實驗中，隨碼距從 $d=3$（18 個資料位元）擴展至 $d=5$（50 個資料位元）與 $d=7$（98 個資料位元，總計動用約 200 個物理原子），經症候群解碼後之邏輯貝爾糾纏態（Logical Bell Pair）錯誤率顯著下降，超越所有單一物理位元對之成對糾纏保真度。
* **容錯製備邏輯 GHZ 貓態與即時前饋控制（Feedforward）**：在二維 $d=3$ 色碼（Color Code）上容錯製備 4-邏輯位元 GHZ 態（4 Logical Qubits），透過中途局部成像測量輔助位元、FPGA 即時解碼與條件式現場前饋操作（Mid-Circuit Measurement & Feedforward），直接獲得保真度顯著優於物理態之無後選擇（No Post-Selection）邏輯多體糾纏。
* **40 個橫向邏輯 CNOT 閘與 48 個邏輯量子位元複雜電路**：利用三維/四維超立方體碼 $[[8, 3, 2]]$，在 280 個物理原子的處理器上同時編碼多達 **48 個邏輯量子位元**，並執行包含多達 **40 個橫向糾纏閘**、跨 7 層深度的非平庸量子電路（如邏輯快速亂序器 Fast Scrambling Circuits 與 2D 易辛量子模擬）。在如此龐大的希爾伯特空間（$2^{48} \approx 2.8 \times 10^{14}$ 維，遠超古典電腦暴力精確模擬極限）中，經錯誤偵測與糾錯後的邏輯輸出分佈清晰呈現干涉條紋，而未經編碼的物理電路輸出則完全退化為白雜訊。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **超導表面碼低於閾值之記憶指數抑制（Google Willow 晶片）**：Google Quantum AI and Collaborators (2024), *Nature* 638:920-926，在 105 位元超導處理器 Willow 上實作 $d=3, 5, 7$ 表面碼多週期量子記憶，首次在超導硬體實現無後選擇之多輪錯誤抑制因子 $\Lambda = 2.14 \pm 0.02 > 1$（每增加碼距 2，邏輯錯誤率減半），且邏輯量子位元壽命超越晶片上最佳單一物理位元壽命達 $2.4$ 倍。
* **高閾值低開銷雙變數自行車量子低密度奇偶校驗碼（qLDPC Bivariate Bicycle Codes）**：Bravyi et al. (IBM Quantum) (2024), *Nature* 627:778-782，證明非局域連接之 $[[144, 12, 12]]$ qLDPC 碼可將容錯硬體物理位元開銷較傳統平面表面碼降低近 10 倍，而本篇建立的可重構中性原子光鑷陣列正是實作此類非局域 qLDPC 碼的最理想物理平台。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **從 NISQ（含噪中尺度量子）正式跨入 EFTQC（早期容錯量子計算）**：過去十年量子計算實驗多在未受保護的物理位元上運行淺層變分線路；本篇證明在數百個物理位元規模下，以邏輯位元直接執行深度算法已具備實質保真度優勢。
* **可重構動態連線打破平面拓撲死局**：證明「硬體連線拓撲不必在製造晶片時寫死，而可以隨量子演算法的每一步動態重排」，使橫向邏輯閘與高效率 qLDPC 碼從純數學理論變為實驗室日常操作。
* **硬體—糾錯協同設計（Co-Design）的新範式**：結合中性原子主要錯誤源為可精確定位之「擦除錯誤（Erasure Errors）」與高偏置相位雜訊的特性，定制解碼演算法（如結合神經網路與最小權重完美匹配 MWPM），將容錯門檻再放寬數倍。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
可重構中性原子邏輯處理器帶來了兩個跨越物理與計算機工程的深刻洞見：

1. **將「空間移動」化為「代數運算」**：在傳統電腦中，資料搬運是消耗能量的額外負擔；但在光學鑷子陣列中，把一整排原子平移交錯並同時點亮一道雷射，本身就是對數十個量子位元同步執行高維度拓撲張量運算。
2. **用多體糾纏對抗熱力學第二定律**：單一原子的量子相干性終究敵不過環境的熱漲落，但當資訊被非局域地編織進整個拓撲穩定子空間時，局部環境無法在不被察覺的情況下偷走全局相位——人類用資訊幾何學戰勝了微觀世界的無序。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [容錯量子計算與量子糾錯碼](../concepts/quantum-error-correction.md)
* **原始權威文獻**：
  * 官方學術出處：Bluvstein, D. et al. (2024). Nature, 626(7997), 58-65 (Published online 6 Dec 2023; print 1 Feb 2024). DOI: [10.1038/s41586-023-06927-3](https://doi.org/10.1038/s41586-023-06927-3)
  * 原始檔典藏：`raw/2024-fault-tolerant-quantum.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
