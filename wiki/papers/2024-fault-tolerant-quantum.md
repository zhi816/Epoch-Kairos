---
title: "Logical quantum processor based on reconfigurable atom arrays"
title_zh: "可重構中性原子陣列之邏輯量子處理器"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Dolev Bluvstein, Simon J. Evered, Alexandra A. Geim, Sophie H. Li, Hengyun Zhou, Tom Manovitz, Sepehr Ebadi, Madelyn Cain, Marcin Kalinowski, Dominik Hangleiter et al., Markus Greiner, Vladan Vuletić, Mikhail D. Lukin"
venue: "Nature, 626(7997), 58-65"
domain: "physics"
domain_tags: ["#量子物理", "#統計物理"]
concepts: ["quantum-error-correction"]
status: "wiki"
verification: "partial"
my_focus: false
doi_url: "https://doi.org/10.1038/s41586-023-06927-3"
key_papers:
  - "Shor, P. W. (1995) Scheme for reducing decoherence in quantum computer memory. Physical Review A 52(4):R2493-R2496. https://doi.org/10.1103/PhysRevA.52.R2493"
  - "Kitaev, A. Y. (2003) Fault-tolerant quantum computation by anyons. Annals of Physics 303(1):2-30 (preprint 1997). https://doi.org/10.1016/S0003-4916(02)00018-0"
  - "Bluvstein, D. et al. (2024) Logical quantum processor based on reconfigurable atom arrays. Nature 626(7997):58-65. https://doi.org/10.1038/s41586-023-06927-3"
  - "Google Quantum AI and Collaborators (2024) Quantum error correction below the surface code threshold. Nature 638:920-926. https://doi.org/10.1038/s41586-024-08449-y"
hook: "利用光學鑷子在計算過程中移動中性銣原子，在最多 280 個物理位元的處理器上，以橫向邏輯閘操作編碼後的邏輯量子位元：表面碼碼距由 3 增至 7 時邏輯糾纏閘改善，並以三維碼執行含 48 個邏輯位元、228 個邏輯雙位元閘的取樣電路。"
card_line: "用雷射搬動原子，在受糾錯保護的位元上運算"
---

# 可重構中性原子陣列之邏輯量子處理器

> 「過去量子位元像被焊死在棋盤上的棋子，只能與隔壁鄰居緩慢交換資訊；光學鑷子讓中性原子在保持量子相干的同時凌空起舞，將三維高維度量子糾錯碼化為現實。」（本頁引言為 Wiki 撰寫，非原文）

**2024 發表 ｜ 容錯量子計算與邏輯量子位元突破**

> **本頁範圍說明**：本條目對應 `raw/2024-fault-tolerant-quantum.pdf`，為哈佛大學 Mikhail D. Lukin 團隊聯合 QuEra、MIT 與馬里蘭大學發表於《Nature》第 626 卷第 7997 期（頁 58–65）之里程碑論文。經 Crossref 核驗（DOI: `10.1038/s41586-023-06927-3`），該文於 2023 年 12 月 6 日先行線上刊出（Online First），正式紙本卷期出版日期為 **2024 年 2 月 1 日**，故依正式期刊卷期年份定 `paper_year: 2024`。`key_papers` 一併列出 Google Quantum AI 於 2024 年底在超導表面碼實現低於閾值指數糾錯（Willow 處理器）之互補里程碑。

---

## Card 1 ｜ 時代銘文 (The Hook)
物理量子位元（Physical Qubits）極度脆弱，環境熱擾動、雷射相位雜訊與自發輻射會在毫秒內摧毀量子疊加態（退相干）。自 Peter Shor (1995) 與 Alexei Kitaev（1997 年預印本，2003 年刊於 Annals of Physics）等人提出量子糾錯碼（Quantum Error Correction, QEC）以來，把資訊冗餘編碼到多個物理量子位元上，構成「邏輯量子位元（Logical Qubits）」並在其上執行邏輯閘，一直是大規模量子計算的必經之路；但邏輯位元所需的額外開銷，使大規模邏輯量子計算面臨重大挑戰（摘要）。哈佛大學 Lukin 團隊以二維聲光偏轉器（AOD）在計算途中**搬運光學鑷子中的中性銣原子（$\mathrm{^{87}Rb}$）**，結合分區架構，在最多 280 個物理位元的處理器上操作 **40 個色碼邏輯位元**，並以三維 $[[8,3,2]]$ 碼執行含 **48 個邏輯位元**、228 個邏輯雙位元閘與 48 個邏輯 CCZ 閘的取樣電路（摘要；Fig. 4–5）。作者認為這些結果預示早期糾錯量子計算的來臨（摘要）。

---

## Card 2 ｜ 世紀瓶頸：平面近鄰連線枷鎖與糾錯開銷的指數深淵 (The Dilemma)
在邁向實用容錯量子計算的道路上，硬體架構長期受制於三大物理瓶頸（以下為一般背景說明，第 2 點之晶格手術成本與編碼率為 Wiki 補充，非本篇內容）：

* **「愈糾愈錯」的閾值困境**：量子糾錯本身需要額外施加大量的雙量子位元閘（如 CNOT / CZ 閘）與輔助位元測量來提取錯誤症候群（Error Syndrome）。若物理閘保真度不夠高或線路過深，糾錯電路自身引入的錯誤反而比原本單一物理位元還多。
* **二維平面近鄰拓撲（2D Nearest-Neighbor）的巨額空間開銷**：在平面表面碼（2D Surface Code）上執行兩個邏輯量子位元之間的邏輯 CNOT 閘，傳統上需要透過複雜的「晶格手術（Lattice Surgery）」或「編織（Braiding）」，不僅需要 $O(d)$ 個時間步的重複症候群測量，且編碼率極低（$k/n \to 0$）。
* **中途讀取會干擾鄰近位元**：在中性原子系統中，演算法中途以成像讀取輔助位元時，需避免干擾仍在運算中的資料位元；本篇因此另設讀取區，使中途讀取不破壞其餘位元之相干性（Logical processor based on atom arrays 節）。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
本篇以**分區架構（Zoned Architecture）**結合可移動的光學鑷子，在邏輯層級控制整個處理器：

1. **儲存區、糾纏區與讀取區之空間分離（Storage, Entangling & Readout Zones）**：
   * 物理位元編碼於 $\mathrm{^{87}Rb}$ 原子基態超精細能階中 $m_F = 0$ 的鐘態，$T_2 > 1\,\text{s}$（Logical processor based on atom arrays 節；Methods, System overview）。
   * 儲存區供高密度、長相干的存放，不受糾纏閘誤差影響；糾纏區進行平行的邏輯位元編碼、穩定子量測與邏輯閘；讀取區可中途讀取所需的邏輯或物理位元，而不干擾仍在運算中之位元的相干性（同節，Fig. 1a）。雙位元閘利用里德堡阻塞，保真度 99.5%（ref. 8），任意連接則靠二維聲光偏轉器（AOD）搬運原子。
2. **以搬運原子實現橫向邏輯閘（Transversal Entangling Gates）**：
   * 以 AOD 產生的網格同時拾起兩個邏輯位元區塊，在糾纏區交錯排列，再打一道全域里德堡激發雷射，對兩區塊中每一對對應原子同時施加物理糾纏閘（Fig. 2a）；施加閘時同一閘位中原子相距 $\lesssim 2\,\mu\text{m}$，不同閘位相距至少 $10\,\mu\text{m}$（Extended Data Fig. 1 圖說）。這種逐對施加的橫向閘本身具容錯性：錯誤不會在同一邏輯區塊內擴散成多位元錯誤（同節；Methods, Fault tolerance and transversal gates）。
3. **相關解碼（Correlated Decoding）**：
   * 橫向 CNOT 會把物理錯誤在兩個區塊之間傳遞，使兩區塊的穩定子產生相關。本篇把兩個邏輯位元放進同一張解碼超圖，以邊與超邊連接兩區塊的穩定子，聯合解碼；以傳統方式各自解碼時，表面碼糾纏閘的保真度反而隨碼距下降（Improving entangling gates with code distance 節；Fig. 2b）。
4. **三維 $[[8,3,2]]$ 碼與超立方體連接**：
   * 每個 $[[8,3,2]]$ 碼塊以 8 個物理位元編碼 3 個邏輯位元；邏輯三元組在 4D 超立方體上糾纏，物理連接相當於 7D 超立方體（Fig. 5；Extended Data Fig. 6）。

### 相關解碼之混合整數規劃 (Correlated Decoding as a Mixed-Integer Program)

本篇以 Stim 依近似實驗誤差率之 Pauli 通道雜訊模型，求出電路中每個錯誤機制 $E_j$（$j = 1, \ldots, M$）的機率 $p_j$ 及其影響的偵測器 $D_i \in \{0, 1\}$（$i = 1, \ldots, N$）；$f(D_i)$ 為會翻轉偵測器 $D_i$ 奇偶的錯誤機制集合。最可能的物理錯誤即下列混合整數規劃的最佳解（Methods, Correlated decoding，未編號式；原文把目標與限制寫在同一個展示式中，此處分成兩式，符號與條件不變）。在 $E_j \in \{0, 1\}$（$j = 1, \ldots, M$）、$K_i \in \mathbb{Z}_{\ge 0}$（$i = 1, \ldots, N$）之下，最大化（maximize）：

$$\sum_{j=1}^{M} \log(p_j) E_j + \log(1 - p_j)(1 - E_j)$$

並使每個偵測器 $i = 1, \ldots, N$ 都滿足（subject to）：

$$\sum_{E_j \in f(D_i)} E_j - 2K_i = D_i$$

目標函數為所指派錯誤組態之對數機率；每個 $K_i$ 使 $f(D_i)$ 中錯誤變數之和與 $D_i$ 模 2 相符。作者以 Gurobi 求得最佳解，再套用 $E_j = 1$ 之錯誤所對應的校正（同節）。

理論上，造成一個邏輯錯誤需要 $(d+1)/2$ 個錯誤，故在錯誤率夠低時，邏輯錯誤率依 $\propto (p/p_{\text{th}})^{(d+1)/2}$ 指數壓低（Methods, Code distance, decoding and thresholds，引 ref. 24；原文為行文中之式子）。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Bluvstein et al. 2024）之核心證據
（本頁以 `doi_url` 指向之 Nature 正式版為準，全文以開放取用之 PMC10830422 核對；`raw/2024-fault-tolerant-quantum.pdf` 為 arXiv:2312.03982v1，所引數字兩版相同。）

* **表面碼碼距 $d = 3 \to 5 \to 7$，邏輯糾纏閘改善**：以兩個表面碼邏輯位元做橫向 CNOT，再投影量測邏輯貝爾態之穩定子；每個邏輯貝爾對使用之物理位元數，$d = 3$、5、7 依序為 26、74、146（Fig. 2d 橫軸）。使用相關解碼時，$d = 7$ 在 $X_L X_L$ 與 $Z_L Z_L$ 基底量得約 0.95 的布居，邏輯貝爾對錯誤隨碼距增大而下降；改用傳統各自解碼時，保真度反而隨碼距下降（Improving entangling gates with code distance 節；Fig. 2c–d）。限制：$d > 3$ 之初態製備並非容錯；作者強調此處超越的是整個電路（含投影讀取）的有效閾值，與多輪雜訊症候群量測下的閾值不同，後者是未來目標（同節）。
* **容錯 GHZ 態、中途讀取與 40 個色碼邏輯位元**：以 $d = 3$ 色碼容錯製備 4 個邏輯位元之 GHZ 態，使用相關解碼之保真度為 72(2)%；若後選擇所有穩定子皆正確，提升至 $99.85^{+0.1}_{-1.0}\%$，代價是捨棄資料；只捨棄 50% 資料時約 90%（Fault-tolerant logical algorithms 節；Fig. 3）。另以分區架構分批編碼，在 280 個物理位元上製備 40 個色碼邏輯位元，並以 20 個橫向 CNOT 容錯製備其中 20 個；每多一個編碼步驟約有 1% 的邏輯退相干（Fig. 4a–c）。
* **48 個邏輯位元之三維 $[[8,3,2]]$ 碼取樣電路**：以 $[[8,3,2]]$ 碼塊在 4D 超立方體連接上糾纏邏輯三元組，執行含 48 個邏輯位元、228 個邏輯雙位元閘與 48 個邏輯 CCZ 閘的電路；在錯誤偵測下，48 個邏輯位元之交叉熵基準（XEB）約為 0.1，作者稱比先前同等複雜度之物理位元數位電路實作最多高約一個數量級（Complex logical circuits using 3D codes 節；Fig. 5）。

### 後續與相關研究（非本篇成果，標註出處）
* **原子陣列上的高編碼率糾錯碼**：Xu et al. (2024), *Nature Physics* 20:1084-1090, doi:10.1038/s41567-024-02479-z，提出以重新排列原子實作量子低密度奇偶校驗（qLDPC）碼的非局域症候群萃取，模擬顯示在物理錯誤率 $10^{-3}$ 下，數百個物理位元即開始優於表面碼（摘要依 arXiv:2308.08648）。
* **超導表面碼低於閾值**：Google Quantum AI and Collaborators (Acharya et al. 2024), *Nature* 638:920-926, doi:10.1038/s41586-024-08449-y，在超導處理器 Willow 上以 101 個位元之 $d = 7$ 表面碼記憶，碼距每增加 2，邏輯錯誤率降為 $1/\Lambda$，$\Lambda = 2.14 \pm 0.02$，並以 $2.4 \pm 0.3$ 倍超越最佳物理位元之壽命（摘要）。
* **常數輪之橫向容錯**：Zhou et al. (2025), *Nature* 646:303-308, doi:10.1038/s41586-025-09543-5（共同作者含本篇作者），結合橫向操作與新的相關解碼策略，說明多種糾錯碼只需常數輪症候群萃取即可容錯執行邏輯操作（摘要依 arXiv:2406.17653）。
* **連續運作的大型原子陣列**：Chiu et al. (2025), *Nature* 646:1075-1080, doi:10.1038/s41586-025-09596-6，以光晶格輸送帶持續補充原子，組成並維持超過 3,000 個原子之陣列超過兩小時，且補充時不破壞已存位元之量子態（摘要）。
* **相關研究（未引用本篇）**：Bravyi et al. (2024), *Nature* 627:778-782, doi:10.1038/s41586-024-07107-7（IBM），提出以低密度奇偶校驗碼實作之容錯量子記憶，在 0.1% 物理錯誤率下以 288 個物理位元保存 12 個邏輯位元近一百萬個週期，表面碼則需近 3,000 個；所需連接為兩個平面子圖構成之 6 度圖（摘要）。原文 Outlook 亦把 qLDPC 碼列為提高編碼效率之方向。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **邏輯層級的演算法表現**：作者認為，在錯誤偵測下，邏輯編碼使交叉熵基準與快速擾亂之量子模擬都優於物理位元保真度，這些結果預示早期糾錯量子計算的來臨（摘要）。此為作者之評價。
* **可重構連線之後續**：本篇以搬運原子實現任意連接與橫向閘；後續研究在此基礎上提出於原子陣列實作 qLDPC 碼（Xu et al. 2024）、以常數輪萃取達成橫向容錯（Zhou et al. 2025），並把原子陣列擴大為可連續補充、超過 3,000 個原子之系統（Chiu et al. 2025）；超導平台同年亦實現低於閾值之表面碼記憶（Google Quantum AI 2024）。出處見 Card 4 後續段。
* **作者所述之未來方向**（Outlook）：在擴大規模時提高編碼效率，例如採用量子低密度奇偶校驗碼、擦除轉換或雜訊偏置，並最佳化原子種類與光學控制；作者也指出多輪雜訊症候群量測下之閾值是重要的未來目標（Improving entangling gates with code distance 節）。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
可重構中性原子邏輯處理器帶來了兩個跨越物理與計算機工程的深刻洞見：

1. **將「空間移動」化為「代數運算」**：在傳統電腦中，資料搬運是消耗能量的額外負擔；但在光學鑷子陣列中，把一整排原子平移交錯並同時點亮一道雷射，本身就是對數十個量子位元同步執行高維度拓撲張量運算。
2. **把資訊分散到許多原子上**：單一原子的量子相干性終究會受環境干擾，但當資訊被冗餘地編碼在一整個邏輯區塊中，局部錯誤可以被偵測與校正，而不會直接破壞所存的資訊。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [容錯量子計算與量子糾錯碼](../concepts/quantum-error-correction.md)
* **原始權威文獻**：
  * 官方學術出處：Bluvstein, D. et al. (2024). Nature, 626(7997), 58-65 (Published online 6 Dec 2023; print 1 Feb 2024). DOI: [10.1038/s41586-023-06927-3](https://doi.org/10.1038/s41586-023-06927-3)
  * 原始檔典藏：`raw/2024-fault-tolerant-quantum.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2024-fault-tolerant-quantum.md](../evidence/2024-fault-tolerant-quantum.md)
