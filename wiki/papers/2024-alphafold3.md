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
verification: "verified"
my_focus: false
doi_url: "https://doi.org/10.1038/s41586-024-07487-w"
key_papers:
  - "Jumper, J. et al. (2021) Highly accurate protein structure prediction with AlphaFold. Nature 596(7873):583-589. https://doi.org/10.1038/s41586-021-03819-2"
  - "Abramson, J. et al. (2024) Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630(8016):493-500. https://doi.org/10.1038/s41586-024-07487-w"
hook: "以全原子擴散生成模組（Diffusion Module）與成對主幹網路（Pairformer）取代傳統胺基酸剛體框架，將高精準度結構預測從單一蛋白質擴展至涵蓋 DNA、RNA、小分子藥物配體、離子與共價修飾的完整生命分子交互作用體系。"
card_line: "預測蛋白質與核酸、藥物結合後的立體結構"
---

# AlphaFold 3：以生成式擴散架構統一預測全生物分子交互作用結構

> 「生命從不靠孤立的蛋白質運作，而是蛋白質、核酸、小分子配體與金屬離子在三維空間中協同共舞的交響曲；AlphaFold 3 用同一個擴散方程統攝了整座細胞內的分子宇宙。」

**2024 發表 ｜ 全生物分子複合體預測里程碑**

> **本頁範圍說明**：本頁對應 `raw/2024-alphafold3.pdf`（Abramson et al. 2024, *Nature* 630:493-500），為 Google DeepMind 與 Isomorphic Labs 繼 2021 年 [AlphaFold2](2021-alphafold2.md)（2024 諾貝爾化學獎獲獎依據）之後，將結構預測範疇推進至全生物分子交互作用之新一代生成式架構。

---

## Card 1 ｜ 時代銘文 (The Hook)
雖然 AlphaFold2 在 2021 年解決了單一蛋白質鏈與同型/異型多聚體的結構預測，但細胞內的真實生理活動與臨床藥物作用，幾乎全部涉及**非蛋白質分子**——包括小分子藥物配體、DNA 雙螺旋、RNA 摺疊、糖基化與磷酸化等轉譯後共價修飾（PTMs）以及金屬離子。過去的方法幾乎都專精於特定交互作用類型，無法預測一般生物分子複合體（p. 493），例如小分子對接用 Vina、蛋白質—核酸複合體用 RoseTTAFold2NA。AlphaFold 3（AF3）大幅簡化演化特徵主幹，並引入直接在三維全原子座標上運作的**生成式擴散模組（Diffusion Module）**；作者報告除一類外，各類別均顯著優於只處理該任務的專用方法（p. 493；例外為 CASP15 RNA，AF3 之 47.3 不及有人工介入之 AIchemy_RNA2 的 54.5，Extended Data Table 1）。

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

擴散網路 $D_\theta\left(X_t, \sigma_t \mid s_{\text{trunk}}, z_{\text{trunk}}\right)$ 以 Pairformer 主幹輸出的單一與成對表徵為條件，直接預測去噪後的原子座標 $\hat{X}_0$。補充資料（Supplementary Information 式 6，SI p. 28）之擴散模組損失為：

$$\begin{aligned}
\mathcal{L}_{\text{diffusion}} &= \frac{\hat{t}^2 + \sigma_{\text{data}}^2}{(\hat{t} + \sigma_{\text{data}})^2} \cdot \left( \mathcal{L}_{\text{MSE}} + \alpha_{\text{bond}} \mathcal{L}_{\text{bond}} \right) \\
&\quad + \mathcal{L}_{\text{smooth-LDDT}}
\end{aligned}$$

其中 $\hat{t}$ 為取樣之雜訊尺度，$\sigma_{\text{data}}$ 為依資料變異數設定之常數（16），$\mathcal{L}_{\text{MSE}}$ 為預測座標與經加權剛體對齊後之真實座標間的加權均方誤差，$\alpha_{\text{bond}}$ 於一般訓練為 0、兩個微調階段為 1。正文指出，雜訊小時的去噪任務著重局部立體化學，雜訊大時則著重系統的大尺度結構（p. 495）。

### 2. 介面預測模板建模分數（ipTM）與複合體排序 (Interface pTM & Ranking Score)

為評估不同生物分子鏈（如蛋白質靶點與小分子配體或抗體與抗原）之間的結合介面可靠度，AF3 利用預測對齊誤差（PAE）分佈計算介面預測 TM-score（$\text{ipTM}$），並加入鼓勵無序區呈伸展構型（相對溶劑可及面積較高）的項，以及鏈間嚴重碰撞之懲罰，給出綜合排序分數（SI 式 19，p. 37；正文 p. 498）：

$$\text{Score}_{\text{ranking}} = 0.8 \cdot \text{ipTM} + 0.2 \cdot \text{pTM} + 0.5 \cdot \text{disorder} - 100 \cdot \text{has\_clash}$$

其中 $\text{has\_clash}$ 為 0 或 1：任兩條聚合物鏈之間距離小於 1.1 Å 的原子對超過 100 個，或超過較小鏈原子數之一半時記為 1（SI §5.9.2，p. 37）。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Abramson et al. 2024）之核心證據
* **蛋白質—小分子配體（PoseBusters 基準）達 $76.4\%$ 成功率**：AF3 只輸入蛋白質序列與配體，不給結合口袋資訊，在 PoseBusters V1（428 個 2021 年以後釋出之 PDB 蛋白質—配體結構，p. 496；AF3 使用 2019 年截止之訓練資料）上之配體 $\text{r.m.s.d.} < 2\,\text{\AA}$ 成功率為 **$76.4\%$**（V2 為 $80.5\%$），高於 RoseTTAFold All-Atom 之 $42.0\%$、給定結合態蛋白質結構之 DiffDock 的 $37.9\%$，以及指定口袋殘基之 Vina 的 $52.3\%$（Extended Data Table 1，p. 21）。
* **蛋白質—核酸複合體**：在近期 PDB 評估集上，以介面 LDDT（iLDDT）衡量，蛋白質—RNA 為 **$39.4$**（RoseTTAFold2NA 為 $19.0$，$N=25$），蛋白質—雙股 DNA 為 **$64.8$**（RoseTTAFold2NA 為 $28.3$，$N=38$）。在 CASP15 的 RNA 目標上，平均表現高於 RoseTTAFold2NA 與 CASP15 最佳 AI 提交 AIchemy_RNA，但不及有人工介入的 AIchemy_RNA2（p. 497；Extended Data Table 1）。
* **抗體—抗原交互作用**：以 1,000 個隨機種子採樣並取排序最高之預測，抗體—抗原介面成功率（$\text{DockQ} > 0.23$）為 **$62.9\%$**，AlphaFold-Multimer v2.3 為 $29.6\%$（$N=65$ 個聚類；Fig. 1c、Fig. 5a；Extended Data Table 1）。
* **共價修飾**：成功率（口袋 $\text{r.m.s.d.} < 2\,\text{\AA}$）共價結合配體為 **$78.5\%$**（$N=66$）；高品質單殘基糖基化為 $72.1\%$（$N=28$），全部品質之多殘基多醣鏈為 $42.4\%$（$N=131$，正文記為 $42.1\%$）；修飾殘基整體為 $59.9\%$（蛋白質 $51.0\%$、DNA $68.6\%$、RNA $40.9\%$）（p. 497；Extended Data Table 1）。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **程式碼公開與同類模型**：Chai Discovery（2024 年 10 月，bioRxiv，doi:10.1101/2024.10.10.615955）發表分子結構預測模型 Chai-1，並公開模型權重與推論程式供非商業使用；Wohlwend et al.（2024 年 11 月，bioRxiv，doi:10.1101/2024.11.19.624167）發表開源模型 Boltz-1，摘要稱其在預測生物分子複合體結構上達到 AlphaFold 3 等級的準確度，並以 MIT 授權公開訓練與推論程式、權重與資料。2024 年 11 月 27 日，Abramson et al. 於 *Nature* 636:E4 發表附錄（Addendum），宣布 Google DeepMind 已釋出 AlphaFold 3 之推論程式碼。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **一個模型處理多類分子**：作者的結論是，這些結果顯示在單一深度學習框架內，對整個生物分子空間做高準確度建模是可能的（摘要，p. 493）；蛋白質、核酸、小分子、離子與修飾殘基以殘基或原子為單位放進同一個擴散去噪框架。
* **從序列與配體直接生成複合體**：AF3 不需事先給定結合口袋即可聯合預測蛋白質與配體之結構（PoseBusters 盲測設定，p. 496）。但作者也指出，在給定的配體與其他輸入下，模型預測的構型狀態可能不正確或不完整，例如 E3 泛素連接酶在無配體時天然呈開放構型，模型卻預測為閉合構型（模型限制，p. 498）。
* **生成式模型的取捨**：改用擴散生成後，同一輸入可透過不同隨機種子得到多個答案，但作者明言 AF3 仍預測 PDB 中所見的靜態結構，多個隨機種子「並不能近似溶液中的構型系綜」；擴散也帶來無序區被生成為假結構（幻覺）的問題，需以交叉蒸餾與排序項緩解（p. 498）。

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
