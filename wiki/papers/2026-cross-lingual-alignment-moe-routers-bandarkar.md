---
title: "Cross-Lingual Alignment for Decoder-Only Models using MoE Routers"
title_zh: "利用混合專家路由器實現純解碼器模型之跨語言表徵對齊"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Lucas Bandarkar, Clark Peng, Ahmed Haj Ahmed, Aditi Khandelwal, Nanyun Peng"
venue: "arXiv preprint arXiv:2610.01921"
domain: "ai"
domain_tags: ["#人工智慧", "#深度學習", "#自然語言處理"]
concepts: ["low-resource-machine-translation"]
status: "published"
verification: "verified"
my_focus: true
focus_role: "report"
focus_languages: ["泰盧固語", "吉爾吉斯語", "康納達語", "泰語", "越南語", "僧伽羅語", "匈牙利語"]
doi_url: "https://arxiv.org/abs/2610.01921"
hook: "將混合專家（MoE）模型中間層路由器的序列平均激活權重作為序列級表徵，於持續預訓練階段以 KL 散度輔助損失對齊平行句對，在 4 個開源 MoE 模型與 7 種語言共 14 組設定中，13 組優於純語言模型基線且最高提升 2.1 平均分，同時提升底層隱狀態相似度。"
card_line: "訓練多語模型時，讓翻譯句對分派相似專家"
key_papers:
  - "Bandarkar et al. (2026c) Multilingual routing in mixture-of-experts. ICLR 2026. https://openreview.net/forum?id=ZoZR0x7tTD"
  - "Liu & Niehues (2025) Middle-layer representation alignment for cross-lingual transfer in fine-tuned LLMs. ACL 2025, 15979-15996. https://doi.org/10.18653/v1/2025.acl-long.778"
  - "Li & Zhou (2025) Your mixture-of-experts LLM is secretly an embedding model for free. ICLR 2025. https://openreview.net/forum?id=eFGQ97z5Cd"
  - "Wendler et al. (2024) Do llamas work in English? on the latent language of multilingual transformers. ACL 2024, 15366-15394. https://aclanthology.org/2024.acl-long.820/"
---

# 利用混合專家路由器實現純解碼器模型之跨語言表徵對齊 (Cross-Lingual Alignment for Decoder-Only Models using MoE Routers)

> 「純解碼器大語言模型沒有天然的句子級向量，對隱藏狀態直接做平均又容易讓不同詞元的特徵互相抵銷；若改以混合專家層的路由器分佈做序列平均對齊，反而能繞過詞元對應難題，連帶拉近底層的跨語言隱藏表徵。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Bandarkar、Peng、Ahmed（Haverford College）、Khandelwal（MILA & McGill University）與 Nanyun Peng（UCLA），*arXiv:2610.01921*（2026 年 10 月）。實驗以四款已後訓練開源 MoE 模型（Qwen3-30B-A3B、GPT-OSS-20B、Marco-Nano、Granite-4.0-H-Tiny）為測試平台，於七種目標語言之 200,000 筆英—目標語平行樣本進行短程持續預訓練與多基準評測。

---

## Card 1 ｜ 時代銘文 (The Hook)

在現代多語言大型語言模型中，低資源與預訓練暴露不足的語言往往效能落後；學界長期推測，能否將高資源語言習得的知識與推理能力遷移至其他語言（Cross-lingual transfer），取決於模型內部表徵是否具備跨語言對齊性（§1, p. 1）。早期編碼器—解碼器（Encoder-Decoder）架構可直接利用編碼器輸出的句子級嵌入向量搭配對比學習對齊平行語料，但當代主流語言模型全面轉向純解碼器（Decoder-only）架構後，既沒有天然的句子向量，各語言分詞詞彙與語法結構的差異也阻斷了精確的詞元對齊，使大量既有雙語翻譯語料未能有效化為跨語言表徵監督訊號（摘要 p. 1；§1, p. 2）。

針對此結構瓶頸，UCLA、Haverford College 與 MILA／McGill 團隊於 2026 年 10 月發表本篇研究，提出在混合專家（Mixture-of-Experts, MoE）模型架構上**以中間層路由器的序列平均權重分佈作為跨語言對齊目標**。研究者在持續預訓練（Continual Pre-training, CPT）期間加入基於 KL 散度的輔助路由對齊損失 $\mathcal{L}_{XLR}$，控制實驗涵蓋 4 款開源 MoE 模型與 7 種語言共 14 組模型—語言配對。結果顯示，該方法不僅實質縮減路由器跨語言分歧、連帶提升底層隱藏狀態的 SoftCKA 相似度，還在 13 組設定上超越純語言模型目標的 CPT 基線（另 1 組平手），為純解碼器 MoE 模型建立無須詞元對齊的跨語言對齊新途徑（摘要 p. 1；§1, p. 2；§5, pp. 6–8）。

---

## Card 2 ｜ 世紀瓶頸：解碼器架構欠缺序列向量與隱狀態平均的消減陷阱 (The Dilemma)

在把跨語言對比學習遷移至當代生成式大型語言模型時，研究團隊指出既有機制存在三層困難（§1–§2, pp. 1–3）：

* **編碼器句子嵌入無法直接沿用**：傳統多語言編碼器能為整段輸入產出語意集中之序列向量，藉平行語料拉近互譯句對、推開無關句對（§1, p. 2；§2.1, p. 2）；但純解碼器模型逐詞自回歸運作，沒有現成的整句表徵可供對齊（§1, p. 2）。
* **分詞差異與隱狀態平均池化的資訊衰減**：由於不同文字系統的分詞切分率（Token fertility）與句法順序差異巨大，平行句之間無法逐詞對齊；若改採末詞元隱狀態或全句隱狀態向量平均池化（Mean-pooling），高維表徵空間中指向不同語義方向的詞元特徵容易相互抵銷或衰減，難以穩定代表整句意義（§1, p. 2；§2.3, p. 3）。實際對照亦顯示，在 Marco-Nano 上直接對中間層隱狀態平均做餘弦對齊（$\mathcal{L}_{XLH}$，效仿 Liu & Niehues 2025）於匈牙利語會使多任務平均分數自基線 37.4 下滑至 36.9（§5.2, p. 7；Table 2, p. 8）。
* **盲目強制全層對齊會損傷語言特異性**：多語言大模型傾向在中段層執行跨語言共享語義計算，首尾兩端則保留語言及文化專屬的表層與詞彙結構；若無差別地在全模型各層強制表徵對齊，反而可能抹除特定語言結構或損傷表現（§2.2, p. 3；§3.1, p. 3）。

---

## Card 3 ｜ 突破原理：中間層 MoE 路由器權重平均之單向 KL 散度對齊 (The Secret)

研究團隊以兩個核心前提為基礎：第一，MoE 模型在每一解碼層為每個詞元 $t$ 計算經 Top-$k$ 歸一化後之稀疏專家機率分佈 $\boldsymbol{p}_{\mathrm{lang}, l}^t = \mathrm{G}(\boldsymbol{z}_{\mathrm{lang}, l}^t) \in \mathbb{R}^E$，其對整個輸入序列的平均池化 $\bar{\boldsymbol{p}} = \frac{1}{T}\sum_{t=1}^{T}\boldsymbol{p}^t$ 代表該句子動員各專家的整體分佈統計，在數學上為低維機率單體而非高維方向向量，因此能避免隱狀態平均時的向量抵銷（§2.3, p. 3；§3.2, pp. 3–4）。第二，藉由先行計算之跨語言路由發散曲線（Bandarkar et al., 2026c），可不經暴力搜尋便選定本來即存在跨語言專家共用的中間層集合 $\mathcal{M}$（§3.1, p. 3；Appendix C, p. 23）。

在此基礎上，論文定義**跨語言路由損失（Cross-Lingual Routing Loss）**，針對平行句對之英語端與目標語端在選中層集合 $\mathcal{M}$ 上計算序列平均路由分佈之間的單向 KL 散度平均（§3.2, p. 4，式 (1)）：

$$
\begin{aligned}
\mathcal{L}_{XLR} = \frac{1}{|\mathcal{M}|} \sum_{l \in \mathcal{M}} D_{\mathrm{KL}}\bigl(\bar{\boldsymbol{p}}_{\mathrm{eng}, l} \parallel \bar{\boldsymbol{p}}_{\mathrm{tgt}, l}\bigr)
\end{aligned}
$$

整體訓練目標則結合標準持續預訓練之目標語交叉熵語言模型損失 $\mathcal{L}_{LM}$（§3.2, p. 4）：

$$\mathcal{L} = \mathcal{L}_{LM} + \alpha \cdot \mathcal{L}_{XLR}$$

關鍵實作與最佳化細節（§3.2–§3.3, pp. 3–4；§6, p. 9）：

1. **單向梯度與錨定機制**：反向傳播僅通過目標語序列計算，英語平行句僅用於擷取參考路由分佈 $\bar{\boldsymbol{p}}_{\mathrm{eng}, l}$ 而**不接收任何梯度更新**，藉以將目標語路由與隱狀態拉向模型原本擅長的高資源英語運算軌跡，同時防止高資源表徵退化（§3.2, p. 4）。
2. **無負樣本而賴負載平衡防止坍塌**：與傳統對比學習須額外建構負樣本對不同，MoE 模型本身皆帶有專家負載平衡（Load-balancing）輔助損失，天然抑制作為少數專家的坍塌傾向（§6, p. 9）。
3. **無填補打包與早期退出（Split-forward Packing）**：實作上利用變長注意力將目標語與英語序列打包於同一次前向傳播而不插填補詞元，且英語序列在經過 $\mathcal{M}$ 最後一層後即提早停止前向計算，跳過剩餘深層與詞表投影，大幅壓低與單語 CPT 相比的額外算力開銷（§3.3, p. 4；Fig. 2）。

---

## Card 4 ｜ 決定性數據：14 組模型—語言實驗與消融驗證 (The Evidence)

### 實驗配置與規模（§4, pp. 4–5；Appendix D–F, pp. 24–25）
* **4 款開源已後訓練 MoE 模型**（Table 7, p. 24）：
  * 大規模組：`Qwen3-30B-A3B`（31B 總參數 / A3B 啟動，48 層，每詞元啟動 8 / 128 專家，$\mathcal{M} = 7\text{–}34$ 層）、`GPT-OSS-20B`（22B / A4B，24 層，4 / 32 專家，$\mathcal{M} = 4\text{–}17$ 層）。
  * 輕量組：`Marco-Nano`（8B / A0.6B，28 層，8 / 238 專家，$\mathcal{M} = 7\text{–}19$ 層）、`Granite-4.0-H-Tiny`（7B / 1B，40 層，6 / 64 專家，$\mathcal{M} = 10\text{–}35$ 層）。
* **7 種目標語言與平行訓練集**：大規模組測泰盧固語（8 項基準）、吉爾吉斯語（4）、康納達語（4）、泰語（7）；輕量組測越南語（9）、僧伽羅語（5）、匈牙利語（6）。每種語言建置 **200,000** 筆訓練平行樣本與 **1,000** 筆驗證樣本，統一訓練 1 epoch、有效批次大小 32，評測涵蓋 FLORES（eng$\to$tgt 翻譯）、Belebele（閱讀理解）、Global-MMLU 醫學子集、MMLU-ProX、MultiLoKo、INCLUDE、Global-PIQA、MGSM 與 PolyMath（§4.1, §4.4, pp. 4–5；Appendix E–F, pp. 24–25）。

### 下游基準全面對照（Table 1, p. 8；§5.2, p. 7）
在全體 14 組模型—語言配對上，加入 $\mathcal{L}_{XLR}$ 相較純目標語 $\mathcal{L}_{LM}$ 持續預訓練基線取得 **13 勝 1 平手**，平均提升 **0.9** 分，最大單組增益達 **+2.1** 分：

| 模型 | 訓練條件 | 泰盧固語 (8) | 吉爾吉斯語 (4) | 康納達語 (4) | 泰語 (7) |
|---|---|---:|---:|---:|---:|
| `Qwen3-30B-A3B` | Original checkpoint | 44.6 | 40.8 | 49.3 | 43.0 |
| `Qwen3-30B-A3B` | Baseline（純 $\mathcal{L}_{LM}$） | 45.4 | 43.5 | 49.6 | 44.9 |
| `Qwen3-30B-A3B` | **+ aux routing loss（本篇）** | **46.3** | **45.6** | **51.4** | **45.4** |
| `Qwen3-30B-A3B` | Router-only training | 45.1 | 42.2 | 49.9 | 43.8 |
| `GPT-OSS-20B` | Original checkpoint | 42.5 | 35.9 | 47.5 | 34.9 |
| `GPT-OSS-20B` | Baseline（純 $\mathcal{L}_{LM}$） | 46.5 | 42.0 | 55.5 | 39.9 |
| `GPT-OSS-20B` | **+ aux routing loss（本篇）** | **47.0** | **43.8** | **56.4** | **40.8** |
| `GPT-OSS-20B` | Router-only training | 43.2 | 36.4 | 48.8 | 34.7 |

| 模型 | 訓練條件 | 越南語 (9) | 僧伽羅語 (5) | 匈牙利語 (6) |
|---|---|---:|---:|---:|
| `Granite-4.0-H-Tiny` | Original checkpoint | 34.8 | 31.3 | 34.5 |
| `Granite-4.0-H-Tiny` | Baseline（純 $\mathcal{L}_{LM}$） | 36.5 | 32.8 | 38.1 |
| `Granite-4.0-H-Tiny` | **+ aux routing loss（本篇）** | **36.8** | **32.9** | **38.8** |
| `Granite-4.0-H-Tiny` | Router-only training | 36.5 | 31.9 | 38.2 |
| `Marco-Nano` | Original checkpoint | 44.2 | 24.0 | 36.3 |
| `Marco-Nano` | Baseline（純 $\mathcal{L}_{LM}$） | **45.6** | 26.1 | 37.4 |
| `Marco-Nano` | **+ aux routing loss（本篇）** | **45.6** | **26.8** | **38.1** |
| `Marco-Nano` | Router-only training | 44.8 | 25.2 | 37.1 |

### 關鍵機制消融與內部表徵驗證（§5.1–§5.2, pp. 6–8；Table 2, p. 8）
1. **路由器平均優於隱狀態平均（Table 2, p. 8）**：在 Marco-Nano 上比較隱狀態平均餘弦對齊 $\mathcal{L}_{XLH}$（$\alpha=5000$）與路由對齊 $\mathcal{L}_{XLR}$（$\alpha=10$）：僧伽羅語上隱狀態對齊僅達 **26.3**（基線 26.1，路由對齊 **26.8**）；匈牙利語上隱狀態對齊甚至退步至 **36.9**（低於基線 37.4），路由對齊則升至 **38.1**。
2. **僅更新路由器遠不足夠**：Router-only 設定雖只更新 **小於 0.1%** 參數，但在部分配對上分數與內部對齊皆呈劇烈雜訊，顯示成效主因來自路由器損失沿前向層傳遞並改造了輸入至路由器的底層隱藏表徵（§5.2, pp. 7–8）。
3. **跨語言路由收斂連帶拉近隱藏狀態**：在評測分布外（FLORES）平行句對上量測，純基線 CPT 幾乎不改變路由發散，加入 $\mathcal{L}_{XLR}$ 則在所有模型與語言中明顯壓低中間層路由發散（Fig. 1, p. 1；Fig. 3, p. 6），且 Qwen3-30B-A3B 的逐層 SoftCKA 隱狀態相似度於四種目標語言皆同步上升（Fig. 4, p. 7）。

---

## Card 5 ｜ 典範轉移：作為新預訓練／對齊介面的路由空間、公開資源與已知限制 (The Revolution)

### 本篇公開資源與科學貢獻
* **公開程式碼庫**：訓練、分詞打包（split-forward packing）與評測腳本已釋出於 `https://github.com/lucasbandarkar/xl_moe_alignment`（Code Availability, p. 10）。
* **為非對比階段補上直接早期梯度監督**：文章指出傳統語言模型僅靠頂層詞表 softmax 反向傳遞梯度會遇見梯度瓶頸；內部路由器對齊損失為前中層參數提供直接監督訊號，同時具備向跨模態（例如視覺—語言 MoE 推理專家對齊）推廣的潛力（§6, p. 9）。

### 作者明列之研究限制與後續問題（§6–§7, pp. 8–9）
1. **後訓練檢查點上之短程試驗限制**：為避免純基座模型無法跟隨推理或評測指令導致分數雜訊，實驗只得於已後訓練完成的模型上補跑 200k 筆短程 CPT，因而壓低基線與實驗組之間的絕對增幅；作者指出此機制真正最理想的使用時機應在預訓練階段（MoE 路由動態多於早期形成），但該規模實驗成本過高而未執行（§6, pp. 8–9）。
2. **高度依賴平行語料與狹窄句級分佈**：$\mathcal{L}_{XLR}$ 天生須仰賴翻譯對照句對，無法單獨取代非平行預訓練、長文件理解或強化學習；現有平行語料多為單句、分佈狹隘（§6, p. 9）。
3. **未實證負載平衡交互影響與詞元粒度損失**：本研究未探討路由器對齊在預訓練超大規模下與負載平衡損失之交互效應，也未將序列平均進一步細化以減少詞元層級資訊流失；此外，結果並未明確驗證跨語言對齊對數學／常識推理類任務的助益是否顯著高於翻譯與閱讀理解（§6–§7, p. 9）。

---

## Card 6 ｜ KAIROS：低資源語言模型的另一條對齊介面 (Cross-Disciplinary Inspiration)

> **本段為 Wiki 詮釋與跨領域啟發分析**：以下聯繫低資源機器翻譯研究方向並推演跨領域涵義，均屬知識庫策展詮釋，非原論文作者所主張。

1. **當語料不夠寫滿所有參數，低維機率選擇分佈比高維語意向量更穩健**：在[低資源神經機器翻譯](../concepts/low-resource-machine-translation.md)領域中，多語言大語言模型常常面臨「英文看懂問題、低資源語言卻找錯推理路徑」的困境——問題有時不是模型缺乏知識，而是低資源語種的詞元序列觸發了錯誤的中間層運算專家。Bandarkar 等人示範了如何把「跨語言對齊」從維度龐大、受分詞長度干擾的隱藏狀態向量空間，轉移到維度固定且具功能語意的路由器選擇分佈（僅 $E$ 維稀疏機率）。這為低資源語言在極有限的平行語料預算下進行模型適配，提供了一個不需要重寫詞表、也不需要逐詞對齊的結構切入點。
2. **「保留首尾語言個性、對齊中段邏輯骨幹」的分層設計哲學**：本篇與多語言神經語言學近年觀點遙相呼應——過度一視同仁的表徵對齊容易伴隨「文化與詞彙抹除」，把細膩的在地語法強制揉進英語常模；將對齊嚴格鎖定在中間共享運算層，而讓前後端保留語種專屬詞法與表層生成空間，讓低資源多語言訓練在「能力遷移」與「語言多樣性保存」之間取得精細的結構分工。
3. **跨領域啟發（架構訊號作為可微分代理）**：就像早期對比學習依賴雙端結構對稱、難以直接套用在異質編碼時序系統，任何帶有離散模組選擇（MoE、多通道注意力、條件路由）的複雜計算架構，都存在一個比內部高維張量更緊緻的「調度統計介面」。將監督訊號落在調度分佈而非原始激活張量上，或許也能成為跨感測器融合與多模態神經網路在非同步採樣條件下實現結構對齊的通用手段。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Bandarkar, L., Peng, C., Ahmed, A. H., Khandelwal, A., & Peng, N. (2026). Cross-Lingual Alignment for Decoder-Only Models using MoE Routers. *arXiv preprint arXiv:2610.01921*. [https://arxiv.org/abs/2610.01921](https://arxiv.org/abs/2610.01921)
  * 公開程式碼：[GitHub / lucasbandarkar/xl_moe_alignment](https://github.com/lucasbandarkar/xl_moe_alignment)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026-cross-lingual-alignment-moe-routers-bandarkar.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-cross-lingual-alignment-moe-routers-bandarkar.md](../evidence/2026-cross-lingual-alignment-moe-routers-bandarkar.md)
