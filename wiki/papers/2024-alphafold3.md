---
title: "Accurate structure prediction of biomolecular interactions with AlphaFold 3"
title_zh: "AlphaFold 3：以生成式擴散架構統一預測全生物分子交互作用結構"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Josh Abramson, Jonas Adler, Jack Dunger, Richard Evans, Tim Green, Alexander Pritzel, Olaf Ronneberger, Lindsay Willmore et al., Demis Hassabis, John M. Jumper"
venue: "Nature, 630(8016), 493-500"
domain: "ai"
domain_tags: ["#計算生物", "#人工智慧", "#結構生物學"]
concepts: ["ai-for-structural-biology", "generative-world-models", "programmable-cellular-engineering"]
status: "wiki"
verification: "issues"
my_focus: false
doi_url: "https://doi.org/10.1038/s41586-024-07487-w"
key_papers:
  - "Jumper, J. et al. (2021) Highly accurate protein structure prediction with AlphaFold. Nature 596(7873):583-589. https://doi.org/10.1038/s41586-021-03819-2"
  - "Abramson, J. et al. (2024) Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630(8016):493-500. https://doi.org/10.1038/s41586-024-07487-w"
hook: "以全原子擴散生成模組（Diffusion Module）與成對主幹網路（Pairformer）取代傳統胺基酸剛體框架，將高精準度結構預測從單一蛋白質擴展至涵蓋 DNA、RNA、小分子藥物配體、離子與共價修飾的完整生命分子交互作用體系。"
---

# AlphaFold 3：以生成式擴散架構統一預測全生物分子交互作用結構

> 「生命從不靠孤立的蛋白質運作，而是蛋白質、核酸、小分子配體與金屬離子在三維空間中協同共舞的交響曲；AlphaFold 3 用同一個擴散方程統攝了整座細胞內的分子宇宙。」

**2024 發表 ｜ 全生物分子複合體預測里程碑**

> **本頁範圍說明**：本頁對應 `raw/2024-alphafold3.pdf`（Abramson et al. 2024, *Nature* 630:493-500），為 Google DeepMind 與 Isomorphic Labs 繼 2021 年 [AlphaFold2](2021-alphafold2.md)（2024 諾貝爾化學獎獲獎依據）之後，將結構預測範疇推進至全生物分子交互作用之新一代生成式架構。

---

## Card 1 ｜ 時代銘文 (The Hook)
雖然 AlphaFold2 在 2021 年解決了單一蛋白質鏈與同型/異型多聚體的結構預測，但細胞內的真實生理活動與臨床藥物作用，幾乎全部涉及**非蛋白質分子**——包括小分子藥物配體、DNA 雙螺旋、RNA 摺疊、糖基化與磷酸化等轉譯後共價修飾（PTMs）以及金屬離子。過去針對不同分子配對，科學界必須分別使用完全不同的專用軟體（如小分子對接用 Vina/DiffDock、核酸用 RoseTTAFoldNA）。AlphaFold 3（AF3）透過大幅簡化演化特徵主幹並引入直接在三維全原子座標上運作的**生成式擴散模組（Diffusion Module）**，在單一統一模型中全面擊敗所有領域專用工具。

---

## Card 2 ｜ 世紀瓶頸：胺基酸剛體假設的不可擴展性與多模態碎裂 (The Dilemma)
將 AlphaFold2 擴展至任意化學分子面臨根本性的架構阻礙：

* **$\mathrm{SE}(3)$ 胺基酸剛體框架無法描述任意小分子與核酸**：AlphaFold2 的結構模組高度依賴「每個胺基酸皆由 $\mathrm{N}-\mathrm{C}_\alpha-\mathrm{C}$ 構成標準局部剛體三角形，且側鏈僅有至多 4 個可旋轉扭轉角 $\chi_1 \dots \chi_4$」的生物學先驗。然而，有機小分子藥物包含成千上萬種拓撲環系、手性中心與非標準化學鍵，根本無法用統一的主鏈剛體與固定扭轉角參數化。
* **多重序列比對（MSA）在非蛋白模態失效**：小分子配體與特定短鏈 DNA/RNA 並無跨物種演化同源序列可用，若過度依賴深層 MSA 特徵更新，模型既笨重又無法學習通用原子級物理化學互補規律。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
AlphaFold 3 對網路架構進行了大刀闊斧的「減法與重構」，實現了從氨基酸殘基級向**全原子級（All-Atom）生成模型**的跨越：

1. **從 Evoformer 精簡為 Pairformer（成對表徵成為唯一核心主幹）**：
   * AF3 將 MSA 處理模組大幅縮減為僅 4 個輕量級區塊，提取完共演化信號後即丟棄龐大的 MSA 張量；隨後的 48 層 **Pairformer** 僅在「單一標記表徵（Single Representation）」與「成對標記表徵（Pair Representation）」上運作（標準胺基酸與核苷酸以單一殘基為 1 個 Token，小分子與修飾基團則以**每一個重原子**為 1 個 Token）。
2. **全原子三維座標生成式擴散模組（All-Atom Diffusion Module）**：
   * 徹底移除 AF2 的不變點注意力（IPA）、局部剛體框架與扭轉角預測，改用基於擴散轉換器（Diffusion Transformer）的去噪生成模組，直接接受受高斯雜訊污染的三維全原子笛卡兒座標 $\vec{x}_t \in \mathbb{R}^{N_{\text{atoms}} \times 3}$，一步步去噪還原出真實三維原子座標 $\hat{\vec{x}}_0$。
   * **拋棄硬性 $\mathrm{SE}(3)$ 等變層，改採隨機旋轉平移資料增強**：作者發現，不在網路內部強加複雜的 $\mathrm{SE}(3)$ 等變約束，而是直接在每次擴散去噪步驟前對輸入座標施加隨機三維剛體旋轉與平移增強（Data Augmentation），不僅大幅提升大核矩陣運算效率，且在全原子尺度上泛化能力更強。
3. **交叉蒸餾（Cross-Distillation）防止無序區幻覺（Hallucination）**：
   * 擴散生成模型天性傾向將天然無序蛋白區（IDRs）強行生成為看似合理的假性 $\alpha$-螺旋。AF3 利用 AlphaFold-Multimer v2.3 的預測結構進行交叉蒸餾訓練，教導擴散模型將無序區自然展開為延伸絲狀構型。

### 1. 多尺度全原子擴散正向加噪與去噪目標 (Multi-Scale All-Atom Diffusion)

設生物分子複合體中全部 $N_{\text{atoms}}$ 個重原子的真實三維座標為 $X_0 \in \mathbb{R}^{N_{\text{atoms}} \times 3}$。在擴散雜訊尺度 $\sigma_t \in [\sigma_{\min}, \sigma_{\max}]$ 下，經隨機全局剛體變換 $\mathcal{T} \sim \mathrm{SE}(3)$（中心化後隨機旋轉與平移）與各向同性高斯加噪後得到含噪座標 $X_t$：

$$\begin{aligned}
\tilde{X}_0 &= \mathcal{T}(X_0) \\
X_t &= \tilde{X}_0 + \varepsilon, \quad \varepsilon \sim \mathcal{N}\left(0, \sigma_t^2 I_{3N_{\text{atoms}}}\right)
\end{aligned}$$

擴散網路 $D_\theta\left(X_t, \sigma_t \mid s_{\text{trunk}}, z_{\text{trunk}}\right)$ 以 Pairformer 主幹輸出的單一與成對表徵為條件，直接預測去噪後的原子座標 $\hat{X}_0$。在多個雜訊尺度 $\sigma_t$ 上定義加權均方誤差與局部平滑全原子 LDDT 損失：

$$\mathcal{L}_{\text{diff}} = \mathbb{E}_{\sigma_t, \varepsilon, \mathcal{T}} \left[ w(\sigma_t) \left\| \hat{X}_0 - \tilde{X}_0^{\text{aligned}} \right\|_W^2 + \alpha_{\text{bond}} \mathcal{L}_{\text{bond}}\left(\hat{X}_0, \tilde{X}_0\right) + \mathcal{L}_{\text{smooth-LDDT}}\left(\hat{X}_0, \tilde{X}_0\right) \right]$$

其中 $\tilde{X}_0^{\text{aligned}}$ 為經加權剛體 Kabsch 對齊後的真實座標。當 $\sigma_t$ 較大時，模型被迫學習大尺度的蛋白質—配體全局對接拓撲；當 $\sigma_t$ 較小時，模型則聚焦於氫鍵、鹽橋與配位鍵的亞埃級（Sub-Angstrom）局部立體化學精煉。

### 2. 介面預測模板建模分數（ipTM）與複合體排序 (Interface pTM & Ranking Score)

為評估不同生物分子鏈（如蛋白質靶點與小分子配體或抗體與抗原）之間的結合介面可靠度，AF3 利用預測對齊誤差（PAE）分佈計算介面預測 TM-score（$\text{ipTM}$），並對無序區與原子碰撞施加懲罰，給出綜合排序信心分數：

$$\text{Score}_{\text{ranking}} = 0.8 \cdot \text{ipTM} + 0.2 \cdot \text{pTM} + 0.5 \cdot \text{disorder} - 100 \cdot N_{\text{clash}}$$

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Abramson et al. 2024）之核心證據
* **蛋白質—小分子配體盲測（PoseBusters Benchmark）達 $76.4\%$ 成功率**：在完全不輸入已知蛋白質結合口袋結構（Blind Docking，僅給定蛋白質序列與配體 SMILES 化學式）的嚴苛設定下，AF3 在 PoseBusters V1 基準（428 個 2021 年後新增之 PDB 複合物）上達到 **$76.4\%$**（PoseBusters V2 為 $80.5\%$）的配體重原子 $\text{r.m.s.d.} < 2.0\,\text{\AA}$ 成功率，不僅遠超最佳深度學習盲對接工具 DiffDock-L（約 $38\%$）與 RoseTTAFold All-Atom（$42.0\%$），甚至大幅擊敗已知真實晶體口袋結構的傳統物理對接霸主 AutoDock Vina（$52.3\%$）。
* **蛋白質—核酸（DNA/RNA）與 RNA 單體結構大幅躍升**：在近期 PDB 評估集上，AF3 對蛋白質—RNA 複合體的介面成功預測率達 **$62.4\%$**（較 RoseTTAFold2NA 的 $28.7\%$ 提升逾一倍），蛋白質—雙股 DNA 複合體成功率達 **$64.8\%$**（RoseTTAFold2NA 為 $28.3\%$）；在 CASP15 RNA 結構預測目標上亦超越所有自動預測伺服器。
* **抗體—抗原（Antibody-Antigen）交互作用突破**：由於抗體互補決定區（CDR H3 環）缺乏跨物種共演化信號，向來是結構預測的最難關卡。AF3 透過隨機種子多次擴散採樣（例如 1,000 個 Seeds）並以信心分數排序，將抗體—抗原介面成功預測率（$\text{DockQ} \ge 0.23$）推升至超過 **$60\%$**，較 AlphaFold-Multimer v2.3 提升逾一倍。
* **共價修飾與糖基化高精準建模**：對共價結合配體、磷酸化/甲基化修飾殘基及複雜多醣鏈（Glycans）的結合位點與構型成功預測率分別達 $78.5\%$、$69.9\%$ 與 $72.1\%$。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **開源模型權重釋出與生態系復現（Chai-1、Boltz-1 與 AF3 開源）**：2024 年 11 月 Google DeepMind 正式向學術界開放 AlphaFold 3 完整原始碼與訓練權重；同時期開源社群亦基於本篇揭示之 Pairformer + 全原子擴散架構復現出 Chai-1 與 MIT Boltz-1 等全生物分子開源基座模型，全面驗證了該架構的可重現性。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **終結「一類分子一套算法」的割裂時代**：首次證明蛋白質、核酸、小分子、金屬離子與共價修飾皆可在同一個「原子與殘基混合 Token 空間 ＋ 三維擴散去噪」框架下協同演化與折疊。
* **實現「柔性誘導契合（Induced Fit）」的原生模擬**：傳統分子對接多假設蛋白質口袋為剛體或僅允許少數側鏈擺動；AF3 從一維序列與配體拓撲直接聯合生成複合物結構，自然捕捉到配體結合引發的蛋白質變構效應（Allostery）與口袋構型重組。
* **生成式擴散模型取代確定性回歸**：在一個具有多重亞穩態構型的生物物理世界中，確定性回歸模型面對多解時只能輸出模糊的平均座標；而擴散生成模型能透過不同隨機種子採樣出完整的構型分佈系綜（Conformational Ensemble）。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
從 AlphaFold 2 到 AlphaFold 3 的演進，是深度學習**「苦澀的教訓（The Bitter Lesson）」**在自然科學領域的又一次深刻印證：

1. **當通用生成架構足夠強大時，過度精巧的手工幾何約束反而成為枷鎖**：AF2 為了遷就胺基酸剛體幾何而設計了極為複雜的 $\mathrm{SE}(3)$ 等變 IPA 與扭轉角層，卻因此困死在蛋白質單一領域；AF3 勇敢拆掉這套專用鷹架，讓標準擴散 Transformer 直接在最基礎的 $(x, y, z)$ 笛卡兒座標上學習，反而一舉通吃了整個元素週期表的生物分子。
2. **從「讀懂演化（MSA）」到「習得物理化學（Atomistic Diffusion）」**：當 MSA 被壓縮至僅 4 層、模型被迫同時處理沒有演化歷史的小分子與抗體時，網路的注意力表徵真正從「查演化字典」昇華為「內化分子間的立體化學與靜電互補法則」。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [AI 驅動之結構生物學與分子設計](../concepts/ai-for-structural-biology.md)
  * [生成式世界模型與擴展定律](../concepts/generative-world-models.md)
  * [可編程細胞與基因工程](../concepts/programmable-cellular-engineering.md)
* **原始權威文獻**：
  * 官方學術出處：Abramson, J. et al. (2024). Nature, 630(8016), 493-500. DOI: [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w)
  * 原始檔典藏：`raw/2024-alphafold3.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
