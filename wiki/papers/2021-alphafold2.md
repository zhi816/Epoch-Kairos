---
title: "Highly accurate protein structure prediction with AlphaFold"
title_zh: "AlphaFold2 與蛋白質結構預測：以演化資訊推算立體結構"
paper_year: 2021
award_year: 2024
timeline_year: 2024
authors: "John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko et al., Demis Hassabis"
laureates: "David Baker, Demis Hassabis, John M. Jumper"
venue: "Nature, 596(7873), 583-589"
honor: "2024 諾貝爾化學獎（表彰蛋白質結構預測與計算蛋白質設計之突破）"
domain: "ai"
domain_tags: ["#計算生物", "#人工智慧", "#結構生物學"]
concepts: ["ai-for-structural-biology", "generative-world-models", "programmable-cellular-engineering"]
status: "published"
verification: "partial"
my_focus: false
doi_url: "https://doi.org/10.1038/s41586-021-03819-2"
key_papers:
  - "Kuhlman, B., Dantas, G., Ireton, G. C., Varani, G., Stoddard, B. L., & Baker, D. (2003) Design of a Novel Globular Protein Fold with Atomic-Level Accuracy. Science 302(5649):1364-1368. https://doi.org/10.1126/science.1089427"
  - "Jumper, J. et al. (2021) Highly accurate protein structure prediction with AlphaFold. Nature 596(7873):583-589. https://doi.org/10.1038/s41586-021-03819-2"
  - "Varadi, M. et al. (2022) AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. Nucleic Acids Research 50(D1):D439-D444. https://doi.org/10.1093/nar/gkab1061"
hook: "以演化序列資訊與受三維幾何啟發的注意力架構預測蛋白質結構，在 CASP14 評估中達到 0.96 Å 的主鏈誤差中位數。"
card_line: "從胺基酸序列，準確預測蛋白質的立體結構"
---

# AlphaFold2 與蛋白質結構預測：以演化資訊推算立體結構

> 「一維的胺基酸序列是生命寫下的密碼，三維的空間摺疊則是它執行功能的機械實體；AlphaFold2 為這兩座世界之間架起了原子級精度的計算橋樑。」

**2021 發表 ｜ 2024 諾貝爾化學獎**

> **本頁範圍說明**：2024 年諾貝爾化學獎由 David Baker（1/2，表彰計算蛋白質從頭設計）與 Demis Hassabis、John M. Jumper（合得 1/2，表彰蛋白質三維結構預測）共享。諾貝爾委員會授予 Hassabis 與 Jumper 之獲獎核心依據即為本篇 2021 年發表於《Nature》之 AlphaFold2 論文（David Baker 並非本篇作者，其代表作列於 `key_papers`；後續 2024 年發表之 AlphaFold3 屬全生物分子交互作用之延伸工作，另見 [AlphaFold 3 條目](2024-alphafold3.md)）。

---

## Card 1 ｜ 時代銘文 (The Hook)
1972 年，Christian Anfinsen 在諾貝爾獎演講中提出著名的「安芬森法則（Anfinsen's Dogma）」：蛋白質的一維胺基酸序列應該完全決定其三維立體結構。然而，一條含 200 個胺基酸的多肽鏈在理論上擁有超過 $10^{100}$ 種可能構型（Levinthal 悖論），若靠冷凍電鏡（Cryo-EM）或 X 光晶體繞射實驗解析單一蛋白質結構，往往需耗費數個月至數年及數十萬美元。DeepMind 團隊由 John Jumper 與 Demis Hassabis 領軍開發的 **AlphaFold2**，在第 14 屆蛋白質結構預測雙年賽（CASP14）的評測中達到 $0.96\,\text{\AA}$ 的主鏈誤差中位數，為長期困難的蛋白質結構預測帶來顯著進展；這項結果不代表所有蛋白質或摺疊過程都已被解決。

---

## Card 2 ｜ 世紀瓶頸：Levinthal 構型爆炸與物理力場的精確度死胡同 (The Dilemma)
半世紀以來，計算結構生物學受困於兩條路線的各自的極限：

* **分子動力學（Molecular Dynamics）的構型空間爆炸**：依據熱力學第一原理模擬每個原子的庫侖力與凡德瓦力，受限於飛秒（$10^{-15}\,\text{s}$）積分步長與自由能力場的微小近似誤差，即使動用全球最強超級電腦，也只能模擬少數微小蛋白在毫秒尺度的摺疊。
* **傳統共演化接觸圖（Contact Maps）缺乏三維全局幾何一致性**：早期生物資訊學透過多重序列比對（MSA）尋找共同突變的胺基酸對（若位置 $i$ 與 $j$ 在演化中同步突變，代表空間上相鄰），但二維成對距離預測往往違反三維歐氏空間的「三角不等式」（即 $d_{ij} + d_{jk} \ge d_{ik}$），在拼裝成三維原子座標時頻繁發生空間扭曲與原子碰撞。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
AlphaFold2 徹底屏棄了傳統拼湊式管線，設計出端到端可微分的「演化—幾何雙軌耦合架構」：

1. **Evoformer（演化序列與成對幾何的雙向注意力交換）**：
   * 網路同時維護兩個核心張量：多重序列比對表徵（MSA Representation，維度 $N_{\text{seq}} \times N_{\text{res}} \times c_m$）與殘基成對表徵（Pair Representation，維度 $N_{\text{res}} \times N_{\text{res}} \times c_z$）。
   * 在 48 個 Evoformer 模組中，成對表徵透過**三角形乘法更新（Triangular Multiplicative Update）**與**三角形自注意力（Triangular Self-Attention）**在有向圖三元閉環 $(i, j, k)$ 上傳遞訊息。其架構受三維歐氏距離「三角不等式（$d_{ij} + d_{jk} \ge d_{ik}$）」啟發，引導表徵逼近物理幾何的一致性（作為神經架構先驗，而非幾何硬性約束），並將成對幾何資訊即時回饋給 MSA 注意力。
2. **不變點注意力（Invariant Point Attention, IPA）與 $\mathrm{SE}(3)$ 等變結構模組**：
   * 結構模組將每個胺基酸殘基視為自由浮動的局部剛體座標系（Backbone Frame，$T_i = (R_i, \vec{t}_i) \in \mathrm{SE}(3)$），初始時全部置於原點（「黑洞初始化」）。IPA 在局部座標系內計算三維點距離注意力，其生成的標量特徵與注意力權重對全局三維旋轉與平移具備**嚴格不變性（$\mathrm{SE}(3)$-Invariance）**；結構模組隨後利用該激活值對殘基剛體坐標系進行**等變更新（$\mathrm{SE}(3)$-Equivariant Update）**，使整體結構模組滿足嚴格的等變性，直接預測全部主鏈框架與側鏈扭轉角 $\chi_1, \dots, \chi_4$。
3. **全局部框架對齊點誤差損失（Frame Aligned Point Error, FAPE）與循環精煉（Recycling）**：
   * FAPE 損失函數將預測出的所有原子座標分別投影到每一個殘基的局部剛體座標系中與真實結構比對，自然兼顧局部鍵角與手性（Chirality）的正確性。

### 1. Evoformer 三角形自注意力與乘法更新方程 (Triangular Updates on Pair Representation)

成對表徵的更新受距離三角不等式啟發，但不以硬性條件保證各項距離滿足它。原文補充資料 Algorithm 11（p. 18）中，向外邊的三角形乘法更新包括正規化、投影與閘控：

$$\begin{aligned}
\mathbf{z}_{ij} &\leftarrow \operatorname{LayerNorm}(\mathbf{z}_{ij}) \\
\mathbf{a}_{ij},\mathbf{b}_{ij} &= \operatorname{sigmoid}(\operatorname{Linear}(\mathbf{z}_{ij})) \odot \operatorname{Linear}(\mathbf{z}_{ij}) \\
\mathbf{g}_{ij} &= \operatorname{sigmoid}(\operatorname{Linear}(\mathbf{z}_{ij})) \\
\tilde{\mathbf{z}}_{ij} &= \mathbf{g}_{ij} \odot \operatorname{Linear}\left(\operatorname{LayerNorm}\left(\sum_k \mathbf{a}_{ik} \odot \mathbf{b}_{jk}\right)\right)
\end{aligned}$$

原文以相同的 `Linear` 名稱表示不同投影。圍繞起始節點的三角形自注意力，則在每個注意力頭 $h$ 使用第三條邊的偏置；其權重為（補充資料 Algorithm 13 第 5 行，p. 19）：

$$a_{ijk}^{h} = \operatorname{softmax}_{k}\left( \frac{1}{\sqrt{c}} (\mathbf{q}_{ij}^{h})^\top \mathbf{k}_{ik}^{h} + b_{jk}^{h} \right)$$

同一注意力頭將各位置的值依權重加總，並以閘門調節輸出（Algorithm 13 第 6 行）：

$$\mathbf o_{ij}^h=\mathbf g_{ij}^h\odot\sum_k a_{ijk}^h\mathbf v_{ik}^h$$

### 2. 不變點注意力（IPA）與 $\mathrm{SE}(3)$ 剛體運動不變性 (Invariant Point Attention)

IPA 在局部座標系生成查詢與鍵，再映到全局座標系計算點距離。原文補充資料 Algorithm 22 第 5–7 行（p. 28）的注意力權重為：

$$\begin{aligned}
w_C &= \sqrt{\frac{2}{9N_{\text{query points}}}}, \qquad w_L = \sqrt{\frac{1}{3}} \\
a_{ij}^{h} &= \operatorname{softmax}_{j}\!\left(w_L\left(\frac{1}{\sqrt{c}}(\mathbf{q}_i^{h})^\top \mathbf{k}_j^{h} + b_{ij}^{h} \\
&\quad - \frac{\gamma^{h}w_C}{2}\sum_p \left\|T_i \circ \vec{\mathbf{q}}_i^{hp} - T_j \circ \vec{\mathbf{k}}_j^{hp}\right\|^2\right)\right)
\end{aligned}$$

全局剛體旋轉與平移不改變上述點距離，因此 IPA 輸出對全局參考座標系不變；後續以局部框架更新座標時，整體結構隨相同剛體運動等變（補充資料 §1.8.2，pp. 26–28）。

### 3. 框架對齊點誤差損失函數 (Frame Aligned Point Error, FAPE)

FAPE 比較預測與真實原子在各自局部框架中的位置；補充資料 Algorithm 28（p. 34）包含長度尺度 $Z$ 與截斷值：

$$\begin{aligned}
\vec{x}_{ij} &= T_i^{-1} \circ \vec{x}_j, \quad \vec{x}_{ij}^{\text{true}} = (T_i^{\text{true}})^{-1} \circ \vec{x}_j^{\text{true}} \\
d_{ij} &= \sqrt{\left\|\vec{x}_{ij} - \vec{x}_{ij}^{\text{true}}\right\|^2 + \epsilon} \\
\mathcal{L}_{\text{FAPE}} &= \frac{1}{Z}\operatorname{mean}_{i,j}\!\left(\min(d_{\text{clamp}}, d_{ij})\right)
\end{aligned}$$

此處原文給定 $Z=10\,\text{\AA}$、$d_{\text{clamp}}=10\,\text{\AA}$。反射不屬於 $\mathrm{SE}(3)$；由於局部框架的構造，FAPE 對鏡像反射並不不變，因而可區分手性（補充資料 §1.9.3）。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Jumper et al. 2021）之核心證據
* **CASP14 主鏈中位數誤差 $0.96\,\text{\AA}$ vs. 亞軍 $2.8\,\text{\AA}$**：在 CASP14 盲測評估集上，AlphaFold2 的 $95\%$ 殘基覆蓋率 $\mathrm{C}_\alpha$ 均方根偏差（$\text{r.m.s.d.}_{95}$）中位數僅為 **$0.96\,\text{\AA}$**（$95\%$ 信賴區間 $0.85$–$1.16\,\text{\AA}$，低於單一碳原子共價半徑規模），而排名第二的最佳競爭方法則為 $2.8\,\text{\AA}$（$95\%$ 信賴區間 $2.7$–$4.0\,\text{\AA}$），誤差縮小近三倍。
* **全原子精度 $1.5\,\text{\AA}$**：包含全部側鏈重原子在內的全原子 $\text{r.m.s.d.}_{95}$ 中位數達 **$1.5\,\text{\AA}$**（亞軍為 $3.5\,\text{\AA}$），當局部預測信心指標 $\text{pLDDT} > 90$ 時，側鏈 $\chi_1$ 扭轉角正確率（誤差 $< 40^\circ$）高達 $90\%$ 以上，足以直接支援 X 光晶體學的分子置換（Molecular Replacement）相位求解。
* **自評估信心指標 pLDDT 與真實精度高度線性吻合**：模型內建的每個殘基局部距離差異測試預測值（pLDDT，$0$–$100$ 分）與真實實驗結構之 $\text{lDDT-C}_\alpha$ 高度吻合。在近期 PDB 測試集（$n = 10,795$ 條蛋白質鏈）上，線性擬合之皮爾森相關係數高達 **$r = 0.76$**（主論文 Figure 2c；在人類蛋白質組伴篇 Tunyasuvunakool et al. 2021 中報告為 $r = 0.73$），使研究者能高度可靠地分辨高信心摺疊區與天然無序區（Intrinsically Disordered Regions）。
* **消融實驗（Ablation Study）證實幾何與演化耦合缺一不可**：移除不變點注意力（IPA）或移除三角形更新、或僅使用預訓練語言模型取代 MSA，在無同源模板目標（Free-Modeling Category）上均導致顯著精度下降。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **人類蛋白質組與 AlphaFold DB**：Tunyasuvunakool et al.（2021）報告人類蛋白質組預測；Varadi et al.（2022）介紹資料庫初版逾 36 萬個預測結構。其後 [EMBL-EBI 於 2022 年 7 月宣布](https://www.ebi.ac.uk/about/news/technology-and-innovation/alphafold-200-million/)資料庫擴充至逾兩億個預測結構；這是較晚的資料庫更新，不是 Varadi 等初版論文的初始數字。
* **蛋白質複合體與從頭設計的雙向飛躍（AlphaFold-Multimer 與 RFdiffusion）**：Evans et al. (2021, bioRxiv) 擴展至多鏈蛋白質交互作用；共同得獎者 David Baker 團隊（Watson et al. 2023, *Nature* 620:1089-1100, RFdiffusion；Dauparas et al. 2022, *Science* 378:49-56, ProteinMPNN）將結構生成擴散模型與逆向摺疊結合，實現自然界從未存在之功能性蛋白質（如新型蛇毒中和蛋白、受體促效劑）的從頭定制。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **核孔複合體的整合建模**：[Fontana 等（2022）](https://doi.org/10.1126/science.abm9326) 結合冷凍電鏡與 AlphaFold，研究非洲爪蟾核孔的細胞質環；[Mosalaganti 等（2022）](https://doi.org/10.1126/science.abm9506) 則結合結構預測與實驗資訊，建立涵蓋超過九成人類核孔骨架的模型。兩篇研究的物種、構造範圍與結果不同，均不是單靠 AlphaFold 直接預測完整核孔。
* **幾何先驗與可檢驗的預測**：三角形更新受距離幾何一致性啟發；IPA 的全局剛體運動不變性與後續座標更新的等變性則有明確的架構設計。這些性質與結構預測結果應分別評估。
* **蛋白質設計的後續研究**：RFdiffusion 與 ProteinMPNN 分別研究結構生成及由結構設計序列；它們與結構預測及實驗驗證可以形成研究流程，但不同任務的成功率仍須各自檢驗。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
AlphaFold2 的成功是**「生命演化史（MSA）」與「歐氏空間幾何學（$\mathrm{SE}(3)$）」在深度學習張量空間中的偉大交會**：

1. **三十億年的自然選擇就是最強大的訓練集**：多重序列比對（MSA）並非單純的字串比對，而是地球生命在三十億年演化過程中已經替我們做過的數十億次突變存活實驗；Evoformer 則是讀懂這部演化史詩的解碼器。
2. **對稱性即先驗（Symmetry as Inductive Bias）**：三維整體旋轉或平移不應改變局部幾何關係；IPA 的不變表示與結構更新的等變性將此要求納入架構，但不保證預測結構必然正確。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [AI 驅動之結構生物學與分子設計](../concepts/ai-for-structural-biology.md)
  * [生成式世界模型與擴展定律](../concepts/generative-world-models.md)
  * [可編程細胞與基因工程](../concepts/programmable-cellular-engineering.md)
* **原始權威文獻**：
  * 官方學術出處：Jumper, J. et al. (2021). Nature, 596(7873), 583-589. DOI: [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)
  * 原始檔典藏：`raw/2021-alphafold2.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 獎項通告：[The Nobel Prize in Chemistry 2024](https://www.nobelprize.org/prizes/chemistry/2024/)
