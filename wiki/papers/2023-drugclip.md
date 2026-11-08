---
title: "DrugCLIP: Contrastive Protein-Molecule Representation Learning for Virtual Screening"
title_zh: "DrugCLIP：以蛋白質—分子三維對比學習實現超高速虛擬藥物篩選"
paper_year: 2023
award_year: 2023
timeline_year: 2023
authors: "Bowen Gao, Bo Qiang, Haichuan Tan, Yinjun Jia, Minsi Ren, Minsi Lu, Jingjing Liu, Wei-Ying Ma, Yanyan Lan"
venue: "Advances in Neural Information Processing Systems (NeurIPS), 36, 44595-44614"
domain: "ai"
domain_tags: ["#人工智慧", "#計算生物"]
concepts: ["ai-for-structural-biology"]
status: "wiki"
verification: "issues"
my_focus: false
doi_url: "https://arxiv.org/abs/2310.06367"
key_papers:
  - "Radford, A. et al. (2021) Learning Transferable Visual Models From Natural Language Supervision (CLIP). ICML 2021, PMLR 139:8748-8763. https://arxiv.org/abs/2103.00020"
  - "Zhou, G. et al. (2023) Uni-Mol: A Universal 3D Molecular Representation Learning Framework. ICLR 2023. https://openreview.net/forum?id=6K2RM6wVqKu"
  - "Gao, B., Qiang, B., Tan, H., Jia, Y., Ren, M., Lu, M., Liu, J., Ma, W.-Y., & Lan, Y. (2023) DrugCLIP: Contrastive Protein-Molecule Representation Learning for Virtual Screening. NeurIPS 36:44595-44614. https://arxiv.org/abs/2310.06367"
hook: "將龐大的分子對接能量搜索轉化為共享三維幾何嵌入空間中的向量餘弦相似度檢索，使十億級化合物庫的虛擬藥物篩選速度提升十萬倍以上，並在零樣本基準測試全面超越傳統物理對接。"
---

# DrugCLIP：以蛋白質—分子三維對比學習實現超高速虛擬藥物篩選

> 「傳統分子對接像是拿著十億把鑰匙逐一插進鎖孔反覆轉動試探；DrugCLIP 則是在高維幾何空間裡直接讀懂『鎖與鑰匙的互補語言』，在一瞬間完成十億次精準配對。」

**2023 發表 ｜ NeurIPS 2023 計算藥物發現突破**

> **本頁範圍說明**：本條目對應 `raw/2023-drugclip.pdf`，經 arXiv API 與 NeurIPS 論文集核驗，為清華大學智能產業研究院（AIR）蘭艷艷、馬維英團隊與北京大學合作於 2023 年發表於 NeurIPS 36 之奠基論文（arXiv:2310.06367）。

---

## Card 1 ｜ 時代銘文 (The Hook)
在現代新藥研發中，如何從包含數十億至數百億個類藥小分子的超大型化學空間（如 ZINC、REAL 資料庫）中，找出能與目標致病蛋白質靶點（Protein Pocket）緊密結合的候選藥物？傳統分子對接（Molecular Docking，如 AutoDock Vina、Glide）必須針對每一個小分子在靶點口袋內反覆採樣成千上萬種三維構型與旋轉角度，單一化合物即需數秒至數十秒 CPU 時間，篩選十億個分子需耗費數百年算力。高博文、強博、蘭艷艷與馬維英等人提出的 **DrugCLIP**，將虛擬篩選重構為「蛋白質口袋與小分子的三維對比表徵學習（Contrastive Representation Learning）」，透過預先編碼的單次向量內積檢索，將篩選速度提升超過 **$10^5$ 倍**，同時在 DUD-E 與 LIT-PCBA 兩大權威基準上大幅刷新零樣本篩選精度。

---

## Card 2 ｜ 世紀瓶頸：構型採樣的算力高牆與監督回歸的過擬合陷阱 (The Dilemma)
計算機輔助藥物設計（CADD）長期受困於「速度」與「泛化能力」的兩難：

* **分子對接（Docking）的構型搜索瓶頸**：物理與經驗打分函數依賴精確的「蛋白質—配體結合姿態（Binding Pose）」，必須透過蒙地卡羅或遺傳演算法在連續六維剛體空間加分子內可旋轉鍵空間中進行昂貴的迭代優化，無法擴展至十億級（Ultra-Large）虛擬化合物庫。
* **親和力回歸模型（Affinity Regression）的嚴重偽相關與過擬合**：既有深度學習方法多將問題視為預測結合自由能 $\Delta G$（或 $\mathrm{p}K_d$）的監督式回歸任務。然而，PDBbind 等實驗結晶資料庫中「具有結合力之正樣本加上實測親和力」總量僅約萬筆，且缺乏龐大的未結合負樣本（Decoys），導致回歸模型極易記憶訓練集分子骨架偏差，在面對全新蛋白質靶點（Zero-Shot Unseen Targets）時表現甚至不如傳統物理對接。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
DrugCLIP 跳脫了「先預測結合姿態、再回歸結合能」的傳統範式，將虛擬篩選重新定義為跨模態密集檢索（Dense Retrieval）問題：

1. **雙塔 $\mathrm{SE}(3)$ 三維幾何編碼器（Dual 3D Geometric Encoders）**：
   * 基於 Uni-Mol 預訓練三維分子表徵框架，分別建立獨立的**蛋白質口袋編碼器 $E_P$**（以殘基原子與空間距離矩陣為輸入）與**小分子編碼器 $E_M$**（由 RDKit 快速生成的三維分子構型為輸入），將兩者映射至同一個正規化超球面嵌入空間 $\mathbb{S}^{d-1}$。由於推理階段雙塔完全解耦，十億個小分子的向量表徵可離線預先算好並建立索引；當面對新靶點時，僅需對蛋白質口袋做一次前向編碼，即可透過 GPU 矩陣內積在毫秒內完成全庫檢索。
2. **雙向對稱 InfoNCE 對比損失（Symmetric Contrastive Learning）**：
   * 在同一個訓練批次（Batch）中，真實結合的「蛋白質口袋—配體」晶體複合物構成正樣本對，而同批次內與其他蛋白質配對的分子自然構成海量負樣本（In-Batch Negatives），直接塑造出高判別力的排序邊界。
3. **生物同源家族與AlphaFold 資料增強（HomoAug）**：
   * 為克服 PDB 實驗結構數量有限（僅數萬筆）的瓶頸，作者提出 **HomoAug**：利用蛋白質家族演化同源性（Pfam），從 AlphaFold 蛋白質結構資料庫（AlphaFold DB）中檢索與已知靶點具有高度結構相似性（TM-score 高）的同源蛋白口袋，將其與原配體配對作為擴充正樣本，將訓練資料多樣性擴增一個數量級。

### 1. 雙塔三維距離感知自注意力編碼 (3D Distance-Aware Representation)

對於蛋白質口袋 $P = \{(a_i^P, \vec{r}_i^P)\}_{i=1}^{N_P}$ 或小分子構型 $M = \{(a_j^M, \vec{r}_j^M)\}_{j=1}^{N_M}$（其中 $a$ 為原子類型，$\vec{r} \in \mathbb{R}^3$ 為三維座標），編碼器利用原子間歐氏距離 $d_{ij} = \|\vec{r}_i - \vec{r}_j\|_2$ 的高斯核（Gaussian Kernel）編碼 $\psi(d_{ij})$ 持續更新成對幾何偏置 $q_{ij}^{(l)}$ 與節點表徵 $h_i^{(l)}$：

$$\begin{aligned}
q_{ij}^{(l+1)} &= q_{ij}^{(l)} + \frac{Q^{(l)}(h_i^{(l)}) \cdot K^{(l)}(h_j^{(l)})^\top}{\sqrt{d_k}} \\
\alpha_{ij}^{(l)} &= \operatorname{softmax}_{j}\left( q_{ij}^{(l+1)} \right)
\end{aligned}$$

由於輸入僅依賴內部成對距離 $d_{ij}$，最終池化並經 $L_2$ 正規化輸出的口袋嵌入向量 $\vec{u}_p = E_P(P)/\|E_P(P)\|_2$ 與分子嵌入向量 $\vec{v}_m = E_M(M)/\|E_M(M)\|_2$ 對任意三維旋轉與平移完全不變（$\mathrm{SE}(3)$-Invariant），無須在對接前對齊兩者的空間方向。

### 2. 對稱雙向 InfoNCE 對比學習目標函數 (Symmetric Contrastive Loss)

給定包含 $B$ 個「蛋白質口袋—活性分子」正樣本對 $\{(P_i, M_i)\}_{i=1}^B$ 的訓練批次，定義兩者的餘弦相似度為 $s(P_i, M_j) = \vec{u}_{p_i}^\top \vec{v}_{m_j}$。DrugCLIP 同時最小化「以口袋檢索分子（Pocket-to-Mol）」與「以分子檢索口袋（Mol-to-Pocket）」的雙向交叉熵損失：

$$\begin{aligned}
\mathcal{L}_{\text{P2M}} &= -\frac{1}{B} \sum_{i=1}^{B} \log \frac{\exp\left( s(P_i, M_i) / \tau \right)}{\displaystyle\sum_{j=1}^{B} \exp\left( s(P_i, M_j) / \tau \right)} \\
\mathcal{L}_{\text{M2P}} &= -\frac{1}{B} \sum_{i=1}^{B} \log \frac{\exp\left( s(P_i, M_i) / \tau \right)}{\displaystyle\sum_{j=1}^{B} \exp\left( s(P_j, M_i) / \tau \right)} \\
\mathcal{L}_{\text{DrugCLIP}} &= \frac{1}{2} \left( \mathcal{L}_{\text{P2M}} + \mathcal{L}_{\text{M2P}} \right)
\end{aligned}$$

其中 $\tau > 0$ 為可學習之溫度超參數。

### 3. 多構型集成最大池化檢索分數 (Multi-Conformation Ensemble Scoring)

在推理階段，為涵蓋柔性小分子在溶液中的構型空間，對候選分子 $M$ 由 RDKit 隨機採樣 $K$ 個低能三維構型 $\{M^{(k)}\}_{k=1}^K$，取其與目標口袋 $P$ 的最大餘弦相似度作為最終虛擬篩選排序分數：

$$S_{\text{VS}}(P, M) = \max_{k \in \{1, \dots, K\}} \left( \vec{u}_p^\top \vec{v}_{m^{(k)}} \right)$$

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Gao et al. 2023, NeurIPS）之核心證據
* **DUD-E 基準零樣本早期富集因子（$\text{EF}_{1\%}$）翻倍超越物理對接**：在涵蓋 102 個靶點、超過 22,000 個活性分子與 140 萬個誘餌分子的 DUD-E 零樣本測試（嚴格剔除訓練集同源靶點）中，DrugCLIP 的前 $1\%$ 富集因子（$\text{EF}_{1\%}$）達到 **$28.54$**（AUROC 達 $84.74\%$、BEDROC 達 $47.41\%$），大幅超越商業級物理對接軟體 Glide-SP（$\text{EF}_{1\%} = 16.21$）、AutoDock Vina（$7.32$）以及既有深度學習方法 Planet（$11.12$）、Gnina（$15.61$）。
* **更嚴苛無偏差基準 LIT-PCBA 之全面領先**：在專為消除人工誘餌偏差、採用真實高通量濕實驗活性與非活性數據構建的 LIT-PCBA 基準（15 個靶點、逾 260 萬筆測試對）上，DrugCLIP 在零樣本設定下取得 **$\text{EF}_{1\%} = 5.51$**（BEDROC $= 10.66\%$），顯著擊敗 Glide-SP（$\text{EF}_{1\%} = 3.41$）、Surflex（$2.50$）與所有監督式親和力回歸模型（如 DeepDTA 僅 $1.47$）。
* **篩選速度提升逾十萬倍（$10^5\times$ Speedup）**：以篩選單一靶點對 $100$ 萬個分子為例，傳統物理對接在單核 CPU 上需耗時數千小時（約 100 天以上），而預先編碼後的 DrugCLIP 僅需數毫秒至數秒即可完成全庫內積排序，使單日篩選百億級（10-Billion-Scale）化學庫在一般實驗室硬體上成為現實。
* **HomoAug 消融驗證**：加入基於 AlphaFold DB 的生物同源增強（HomoAug）後，在 LIT-PCBA 上將 $\text{EF}_{1\%}$ 從 $4.21$ 進一步推升至 $5.51$，證明合成結構生物資料能有效突破晶體資料庫規模限制。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **真實世界濕實驗靶點驗證與超高通量命中率**：蘭艷艷與高博文團隊在論文及後續跟進實驗中，針對多巴胺受體、5-羥色胺轉運體（SERT）與新型抗腫瘤靶點進行百萬至十億級化學庫實戰篩選並合成測試，在細胞與體外結合實驗中獲得高達 $15\%$–$20\%$ 以上之微莫耳至奈莫耳級（$\text{nM}$）高活性先導化合物命中率，並解析出冷凍電鏡複合物結構驗證其結合位點。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **虛擬篩選從「物理模擬（Simulation）」邁向「語義與幾何檢索（Retrieval）」**：正如搜尋引擎以向量嵌入取代逐字正規表達式比對，DrugCLIP 證明藥物篩選的第一階段無須昂貴地還原每一個原子的接觸力，而可透過高維度幾何對比空間直接完成超大規模粗篩與精排。
* **AlphaFold 結構庫與藥物發現的無縫閉環**：HomoAug 展示了如何將 AlphaFold2 釋出的兩億個預測蛋白質結構轉化為藥物篩選模型的訓練燃料，解決了 PDB 實驗複合物結構稀缺的長期瓶頸。
* **開啟百億級按需合成化學空間（Make-on-Demand Chemical Space）**：過去藥物化學家只能在數百萬個現成庫存分子中挑選；如今結合 DrugCLIP 的超高速檢索，科學家可直接探索 Enamine REAL 等高達數百億個可合成虛擬分子的廣袤空間。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
DrugCLIP 的核心突破源自一次極具洞察力的**「問題重構（Problem Reframing）」**：

1. **排序（Ranking）比回歸（Regression）更契合科學篩選的本質**：新藥篩選的目標並非把每個不結合分子的自由能算到小數點後第三位，而是從十億個分子中把最可能結合的前 100 個排到最前面。InfoNCE 對比損失將算力100%集中於「區分活性分子與海量背景誘餌」的決策邊界上。
2. **跨領域架構遷移（From Vision-Language CLIP to Pocket-Ligand CLIP）**：OpenAI 的 CLIP 將「圖片」與「文字」對齊在同一向量空間；DrugCLIP 則將「蛋白質口袋」與「小分子配體」視作生命語言中的兩個互補模態，證明對比表徵學習是連接不同物理實體的通用數學語言。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [AI 驅動之結構生物學與分子設計](../concepts/ai-for-structural-biology.md)
* **原始權威文獻**：
  * 官方學術出處：Gao, B., Qiang, B., Tan, H., Jia, Y., Ren, M., Lu, M., Liu, J., Ma, W.-Y., & Lan, Y. (2023). Advances in Neural Information Processing Systems (NeurIPS), 36, 44595-44614. arXiv: [2310.06367](https://arxiv.org/abs/2310.06367)
  * 原始檔典藏：`raw/2023-drugclip.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
