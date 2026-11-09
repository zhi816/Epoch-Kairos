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
verification: "verified"
my_focus: false
doi_url: "https://arxiv.org/abs/2310.06367"
key_papers:
  - "Radford, A. et al. (2021) Learning Transferable Visual Models From Natural Language Supervision (CLIP). ICML 2021, PMLR 139:8748-8763. https://arxiv.org/abs/2103.00020"
  - "Zhou, G. et al. (2023) Uni-Mol: A Universal 3D Molecular Representation Learning Framework. ICLR 2023. https://openreview.net/forum?id=6K2RM6wVqKu"
  - "Gao, B., Qiang, B., Tan, H., Jia, Y., Ren, M., Lu, M., Liu, J., Ma, W.-Y., & Lan, Y. (2023) DrugCLIP: Contrastive Protein-Molecule Representation Learning for Virtual Screening. NeurIPS 36:44595-44614. https://arxiv.org/abs/2310.06367"
hook: "將龐大的分子對接能量搜索轉化為共享三維幾何嵌入空間中的向量餘弦相似度檢索，使十億級化合物庫的虛擬藥物篩選速度提升十萬倍以上，並在零樣本基準測試全面超越傳統物理對接。"
card_line: "不再逐一模擬，從海量分子中快速挑出候選藥"
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
   * 基於 Uni-Mol 預訓練三維分子表徵框架，分別建立獨立的**蛋白質口袋編碼器 $g_\phi$**（以殘基原子與空間距離矩陣為輸入）與**小分子編碼器 $f_\theta$**（以三維分子原子坐標與類型為輸入），將兩者映射至同一個正規化超球面嵌入空間。由於推理階段雙塔完全解耦，小分子的向量表徵可離線預先算好並建立索引；當面對新靶點時，僅需對蛋白質口袋做一次前向編碼，即可透過 GPU 向量內積高速完成檢索（十億級化合物庫約在數小時內完成，詳見 Card 4）。
2. **雙向對稱 InfoNCE 對比損失（Symmetric Contrastive Learning）**：
   * 在同一個訓練批次（Batch）中，真實結合的「蛋白質口袋—配體」晶體複合物構成正樣本對，而同批次內與其他蛋白質配對的分子自然構成海量負樣本（In-Batch Negatives），直接塑造出高判別力的排序邊界。
3. **生物同源演化與 AlphaFold 資料增強（HomoAug）**：
   * 為克服 PDB 實驗複合物結構有限（僅數萬筆）的瓶頸，作者提出 **HomoAug**：使用 Jackhmmer 在經 MMseqs（50% 序列一致性聚類）與高可信度過濾（殘基 pLDDT $> 70$ 佔比 $> 90\%$）之 AlphaFold 蛋白質結構庫（約 845 萬條序列）中檢索同源蛋白；以 TMalign 進行三維結構對齊，保留結構相似（TM-score $\ge 0.4$）且結合口袋對齊率 $\ge 40\%$ 的配對，擷取配體 $6\,\text{Å}$ 範圍內的殘基構建新口袋，成功擴增出 758,107 個全新口袋—配體訓練對（擴增了 51% 的 PDBbind 實例）。

### 1. 雙塔三維距離感知自注意力編碼 (3D Distance-Aware Representation)

對於蛋白質口袋 $x^p = \{c_p, t_p\}$ 或小分子構型 $x^m = \{c_m, t_m\}$（其中 $t$ 為原子類型，$c \in \mathbb{R}^{L \times 3}$ 為原子三維坐標），編碼器利用原子間相對歐氏距離 $d_{ij} = \|c_i - c_j\|_2$ 初始化成對表徵 $q_{ij}^0$，並在 Transformer 層間作為注意力偏置持續更新節點表徵 $h_i^{(l)}$：

$$\begin{aligned}
\operatorname{Attention}(Q_i^l, K_j^l, V_j^l) &= \operatorname{softmax}_j\left( \frac{Q_i^l (K_j^l)^\top}{\sqrt{d}} + q_{ij}^l \right) V_j^l \\
q_{ij}^{l+1} &= q_{ij}^l + \frac{Q_i^l (K_j^l)^\top}{\sqrt{d}}
\end{aligned}$$

由於輸入依賴內部成對距離矩陣，輸出的口袋嵌入向量 $g_\phi(x^p)$ 與分子嵌入向量 $f_\theta(x^m)$ 對全域剛體旋轉與平移完全不變（$\mathrm{SE}(3)$-Invariant），無須在篩選前預先對齊空間坐標。

### 2. 對稱雙向 InfoNCE 對比學習目標函數 (Symmetric Contrastive Loss)

給定包含 $N$ 個「蛋白質口袋—活性分子」正樣本對 $\{(x_k^p, x_k^m)\}_{k=1}^N$ 的訓練批次，定義兩者的相似度為 $s(x_i^p, x_j^m) = g_\phi(x_i^p)^\top f_\theta(x_j^m)$（可採點積或正規化餘弦相似度）。DrugCLIP 同時最小化「以口袋檢索分子（Pocket-to-Mol）」與「以分子檢索口袋（Mol-to-Pocket）」的雙向損失：

$$\begin{aligned}
\mathcal{L}_k^p &= -\frac{1}{N} \log \frac{\exp\left( s(x_k^p, x_k^m) / \tau \right)}{\displaystyle\sum_{i=1}^N \exp\left( s(x_k^p, x_i^m) / \tau \right)} \\
\mathcal{L}_k^m &= -\frac{1}{N} \log \frac{\exp\left( s(x_k^p, x_k^m) / \tau \right)}{\displaystyle\sum_{i=1}^N \exp\left( s(x_i^p, x_k^m) / \tau \right)} \\
\mathcal{L} &= \frac{1}{2} \sum_{k=1}^N \left( \mathcal{L}_k^p + \mathcal{L}_k^m \right)
\end{aligned}$$

其中 $\tau > 0$ 為可學習之溫度參數。

### 3. 化學模擬噪聲注入與訓練—測試不一致性消除 (Conformation Simulation for Generalization)

虛擬篩選面臨晶體結合態（Holo）與未結合游離態（Apo）構型差異的「訓練—測試不一致性」。DrugCLIP 在訓練期直接利用 RDKit 生成分子模擬構型作為帶噪聲輸入 $\tilde{x}^m = \{c_m + \delta, h_m\}$。作者在 Proposition 1 中證明：雙塔距離編碼架構的評分偏差在一階泰勒展開下與距離擾動成正比，當模擬構型與結合構型接近時（存在剛體旋轉 $R$ 與平移 $t$ 滿足 $(c + \delta)R^\top + t = c$），內部距離矩陣偏差為零，即：

$$\lim_{\delta \to 0} \{ s(\tilde{x}_m, x_p) - s(x_m, x_p) \} = 0$$

相較之下，傳統單塔親和力回歸模型因混入跨分子相對距離項，即使分子內部構型逼真，仍必須依賴分子對接演算法求出旋轉平移參數才能預測。DrugCLIP 藉此完全解耦相對空間坐標，在推論期僅需計算單一口袋向量與候選分子向量的點積或餘弦相似度。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Gao et al. 2023, NeurIPS）之核心證據
* **DUD-E 基準零樣本早期富集因子翻倍超越物理對接**：在涵蓋 102 個靶點、22,886 個活性分子與對應誘餌分子的 DUD-E 零樣本測試（嚴格剔除訓練集同源靶點）中，DrugCLIP 零樣本模型（$\text{DrugCLIP}_{\text{ZS}}$）的前 $1\%$ 富集因子（$\text{EF}_{1\%}$）達到 **$31.89$**（$\text{EF}_{0.5\%} = 38.07$、$\text{EF}_{5\%} = 10.66$、$\text{AUROC} = 80.93\%$、$\text{BEDROC} = 50.52\%$），大幅超越商業級物理對接軟體 Glide-SP（$\text{EF}_{1\%} = 16.18$、$\text{BEDROC} = 40.70\%$）、AutoDock Vina（$\text{EF}_{1\%} = 7.32$）以及既有深度學習方法 Planet（$\text{EF}_{1\%} = 8.83$）、Pafnucy（$\text{EF}_{1\%} = 3.86$）（Table 1, p. 7）。
* **更嚴苛無偏差基準 LIT-PCBA 之全面領先**：在專為消除人工誘餌偏差、基於 PubChem 劑量效應實驗構建的 LIT-PCBA 基準（15 個靶點、7,844 個活性分子與 407,381 個非活性分子）上，DrugCLIP 取得 **$\text{EF}_{1\%} = 5.51$**、$\text{EF}_{0.5\%} = 8.56$、$\text{EF}_{5\%} = 2.27$、$\text{BEDROC} = 6.23\%$、$\text{AUROC} = 57.17\%$，顯著擊敗 Glide-SP（$\text{EF}_{1\%} = 3.41$、$\text{BEDROC} = 4.00\%$）、Surflex（$\text{EF}_{1\%} = 2.50$）、Planet（$\text{EF}_{1\%} = 3.87$）、Gnina（$\text{EF}_{1\%} = 4.63$）與監督式親和力回歸模型 DeepDTA（$\text{EF}_{1\%} = 1.47$、$\text{BEDROC} = 2.53\%$）（Table 3, p. 8）。
* **超大規模分子庫檢索效率突破**：在包含 60 億（$6 \times 10^9$）個分子的 Enamine 超大型庫篩選實驗中（§4.3, p. 8），候選分子預先離線編碼後，DrugCLIP 完成單靶點全庫檢索耗時小於 10,000 秒（約 2.78 小時；原文括號誤註為約 30 小時）。相較之下，商業對接軟體 Glide 若在單核 CPU 篩選 100 億分子估計需耗時約 3,000 年（約 80 萬美元），單塔深度學習方法 Planet 在靶點數增加至 600 個時耗時擴增至 2 年以上。
* **HomoAug 與構型模擬消融驗證**：在 DUD-E 消融實驗中（Table 5, p. 9），未使用 RDKit 構型與 HomoAug 時 BEDROC 為 $38.13\%$、$\text{EF}_{1\%}$ 為 $23.86$；加入 RDKit 構型後升至 $45.81\%$ 與 $29.12$；進一步加入 HomoAug 後 BEDROC 提升至 **$50.52\%$**、$\text{EF}_{1\%}$ 達到 **$31.89$**（$\text{EF}_{0.5\%} = 38.07$），證明同源增強能有效提升模型泛化力。
* **專家雙盲評估**：在 ChemDiv 化合物庫中選取 5 個靶點進行虛擬篩選（§4.5, Table 8），由具備藥物設計經驗的專家對 DrugCLIP 與 Glide 篩選出的候選結構進行雙盲評審，在 4 個靶點中專家偏好選擇 DrugCLIP 之分子結構。

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
  * 證據表：[evidence/2023-drugclip.md](../evidence/2023-drugclip.md)
