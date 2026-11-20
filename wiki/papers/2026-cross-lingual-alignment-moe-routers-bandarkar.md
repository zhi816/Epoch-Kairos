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
focus_tags: ["llm-assisted"]
focus_direction: "transfer-align"
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

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Bandarkar、Peng、Ahmed（Haverford College）、Khandelwal（MILA & McGill University）與 Nanyun Peng（UCLA），*arXiv:2610.01921*（2026 年 10 月）。實驗以四款已後訓練開源 MoE 模型（Qwen3-30B-A3B、GPT-OSS-20B、Marco-Nano、Granite-4.0-H-Tiny）為測試平台，於七種目標語言之 200,000 筆英—目標語平行樣本進行短程持續預訓練與多基準評測。

---

## Card 1 ｜ 一句話看懂
這篇想讓多語大型語言模型把英語學到的能力更好地用到其他語言。它的做法是：在混合專家（MoE）模型的中間幾層，要求一句英文和它的譯文「分派到相似的專家」，把這個要求當成額外的訓練目標，在持續預訓練時一起學（§3）。在 4 個開源模型、7 種語言共 14 組實驗中，有 13 組比只做一般持續預訓練更好、1 組平手，平均提升 0.9 分、最多 2.1 分（§5.2, p. 7；Table 1, p. 8）。

* **語言**：泰盧固語、吉爾吉斯語、康納達語、泰語、越南語、僧伽羅語、匈牙利語（皆與英語配對）
* **任務**：多語大型語言模型的跨語言對齊（改善下游翻譯、閱讀理解、推理等）
* **方法**：在中間層對英文句與譯文的「專家分派比例」施加 KL 散度損失，與語言模型損失一起訓練（§3.2，式 (1)）
* **資料**：每種語言 200,000 筆英—目標語平行樣本、1,000 筆驗證樣本（§4.1）
* **公開**：程式碼公開於 GitHub `lucasbandarkar/xl_moe_alignment`（Code Availability, p. 10）
* **出處**：Bandarkar、Peng、Ahmed、Khandelwal、Nanyun Peng（UCLA、Haverford College、MILA／McGill），*arXiv:2610.01921*，2026 年 10 月

---

## Card 2 ｜ 要解決的問題
學界推測，模型能否把高資源語言學到的知識遷移到其他語言，取決於內部表徵是否跨語言對齊（§1, p. 1）。但要在當代模型上做對齊有三個困難（§1–§2, pp. 1–3）：

* **沒有句向量**：傳統多語編碼器能為整句輸出一個向量，用平行句拉近互譯句；純解碼器模型逐詞生成，沒有現成的整句表徵可對齊（§1, p. 2；§2.1, p. 2）。
* **平均會抵銷**：不同語言分詞差異大，平行句無法逐詞對齊；若把整句隱藏狀態取平均，指向不同方向的特徵容易互相抵銷（§1, p. 2；§2.3, p. 3）。在 Marco-Nano 上直接對隱藏狀態平均做對齊（$\mathcal{L}_{XLH}$），匈牙利語分數反而從 37.4 降到 36.9（§5.2, p. 7；Table 2）。
* **全層對齊有害**：多語模型傾向在中段層做跨語言共享的計算，首尾層保留語言專屬的結構；不分層地強制對齊，可能抹除語言特性（§2.2, p. 3；§3.1, p. 3）。

這篇的想法：改對齊中間層的「專家分派比例」，不必逐詞對應。

---

## Card 3 ｜ 方法流程
1. **選中間層**：依先前算好的跨語言路由差異曲線（Bandarkar et al. 2026c），為每個模型選出本來就有跨語言共用專家的中間層集合 $\mathcal{M}$，不需暴力搜尋（§3.1, p. 3；Appendix C）。
2. **算分派比例**：MoE 模型在每層為每個詞元算出分給各專家的機率，對整句取平均，得到這句話動用各專家的比例 $\bar{\boldsymbol{p}}$。它是低維的機率分佈，不是高維向量，因此不會像隱藏狀態平均那樣互相抵銷（§2.3, p. 3；§3.2, pp. 3–4）。
3. **對齊英文與譯文**：在選中的各層，計算英文句與目標語譯文分派比例之間的 KL 散度並取平均（式 (1)），再與一般的語言模型損失相加（§3.2, p. 4）：

$$
\begin{aligned}
\mathcal{L}_{XLR} = \frac{1}{|\mathcal{M}|} \sum_{l \in \mathcal{M}} D_{\mathrm{KL}}\bigl(\bar{\boldsymbol{p}}_{\mathrm{eng}, l} \parallel \bar{\boldsymbol{p}}_{\mathrm{tgt}, l}\bigr)
\end{aligned}
$$

整體訓練目標則結合標準持續預訓練之目標語交叉熵語言模型損失 $\mathcal{L}_{LM}$（§3.2, p. 4）：

$$\mathcal{L} = \mathcal{L}_{LM} + \alpha \cdot \mathcal{L}_{XLR}$$

4. **只更新目標語那一側**：英文句只用來提供參考的分派比例，不接收梯度，藉此把目標語拉向模型擅長的英語運算方式，又不讓英語表現退化（§3.2, p. 4）。MoE 模型本身的負載平衡損失可防止所有詞元擠向少數專家，因此不需要額外的負樣本（§6, p. 9）。
5. **省算力**：英文與目標語序列打包在同一次前向計算，英文序列在 $\mathcal{M}$ 最後一層後就停止，跳過其餘層，額外算力很少（§3.3, p. 4；Fig. 2）。

---

## Card 4 ｜ 資料與實驗
* **4 款開源已後訓練 MoE 模型**（Table 7, p. 24）：
  * 大規模組：`Qwen3-30B-A3B`（31B 總參數 / A3B 啟動，48 層，每詞元啟動 8 / 128 專家，$\mathcal{M} = 7\text{–}34$ 層）、`GPT-OSS-20B`（22B / A4B，24 層，4 / 32 專家，$\mathcal{M} = 4\text{–}17$ 層）。
  * 輕量組：`Marco-Nano`（8B / A0.6B，28 層，8 / 238 專家，$\mathcal{M} = 7\text{–}19$ 層）、`Granite-4.0-H-Tiny`（7B / 1B，40 層，6 / 64 專家，$\mathcal{M} = 10\text{–}35$ 層）。
* **7 種目標語言與平行訓練集**：大規模組測泰盧固語（8 項基準）、吉爾吉斯語（4）、康納達語（4）、泰語（7）；輕量組測越南語（9）、僧伽羅語（5）、匈牙利語（6）。每種語言建置 **200,000** 筆訓練平行樣本與 **1,000** 筆驗證樣本，統一訓練 1 epoch、有效批次大小 32，評測涵蓋 FLORES（eng$\to$tgt 翻譯）、Belebele（閱讀理解）、Global-MMLU 醫學子集、MMLU-ProX、MultiLoKo、INCLUDE、Global-PIQA、MGSM 與 PolyMath（§4.1, §4.4, pp. 4–5；Appendix E–F, pp. 24–25）。

* **比較方式**：原始模型、只用語言模型損失的持續預訓練（基線）、加路由對齊損失（本篇）、只訓練路由器；另在 Marco-Nano 上比較隱藏狀態平均對齊（Table 1–2）。

---

## Card 5 ｜ 結果

### 下游基準對照（Table 1, p. 8；§5.2, p. 7）
在全部 14 組模型—語言配對上，加入路由對齊損失相較只用語言模型損失的基線取得 **13 勝 1 平手**，平均提升 **0.9** 分，最大單組增益 **+2.1** 分：

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

### 機制消融與內部表徵（§5.1–§5.2, pp. 6–8；Table 2, p. 8）
1. **路由器平均優於隱狀態平均（Table 2, p. 8）**：在 Marco-Nano 上比較隱狀態平均餘弦對齊 $\mathcal{L}_{XLH}$（$\alpha=5000$）與路由對齊 $\mathcal{L}_{XLR}$（$\alpha=10$）：僧伽羅語上隱狀態對齊僅達 **26.3**（基線 26.1，路由對齊 **26.8**）；匈牙利語上隱狀態對齊甚至退步至 **36.9**（低於基線 37.4），路由對齊則升至 **38.1**。
2. **僅更新路由器遠不足夠**：Router-only 設定雖只更新 **小於 0.1%** 參數，但在部分配對上分數與內部對齊皆呈劇烈雜訊，顯示成效主因來自路由器損失沿前向層傳遞並改造了輸入至路由器的底層隱藏表徵（§5.2, pp. 7–8）。
3. **跨語言路由收斂連帶拉近隱藏狀態**：在評測分布外（FLORES）平行句對上量測，純基線 CPT 幾乎不改變路由發散，加入 $\mathcal{L}_{XLR}$ 則在所有模型與語言中明顯壓低中間層路由發散（Fig. 1, p. 1；Fig. 3, p. 6），且 Qwen3-30B-A3B 的逐層 SoftCKA 隱狀態相似度於四種目標語言皆同步上升（Fig. 4, p. 7）。

---

## Card 6 ｜ 限制與可用性
* **作者說的限制**（§6–§7, pp. 8–9）：
  1. 實驗只在已後訓練的模型上補跑 200k 筆短程持續預訓練（純基座模型無法穩定跟隨評測指令），因而壓低了增幅；作者認為最理想的使用時機是預訓練階段，但成本過高未執行。
  2. 方法必須依賴平行語料，無法單獨取代非平行預訓練、長文件理解或強化學習；現有平行語料多為單句、分佈狹窄。
  3. 未探討預訓練大規模下與負載平衡損失的交互影響，也未把整句平均細化到詞元層級；對數學、常識推理類任務的助益是否明顯高於翻譯與閱讀理解，尚未驗證。
* **讀的時候要留意**：只適用於混合專家（MoE）架構的模型；平均提升 0.9 分，幅度不大；arXiv 預印本，尚未經同儕審查（Wiki 註記）。
* **公開程度**：程式碼公開於 `https://github.com/lucasbandarkar/xl_moe_alignment`（Code Availability, p. 10）。
* **適合拿來報告的點**：用「專家分派比例」代替隱藏狀態做跨語言對齊，避開分詞與平均抵銷的問題，概念新且有消融證據，適合報告多語大型語言模型如何照顧低資源語言（Wiki 詮釋）。作者也指出，路由器對齊損失能為模型前中層提供直接的訓練訊號，並可能推廣到跨模態的專家對齊（§6, p. 9）。

### 延伸想法
以下為延伸思考（Wiki 推測），不是原文主張。

1. **低維分佈比高維向量穩健**：低資源語言的問題有時不是模型缺乏知識，而是該語言的詞元觸發了錯誤的中間層專家。本文把對齊從高維、受分詞長度干擾的隱藏狀態，轉到維度固定的專家分派分佈，為平行語料很少的語言提供不必重寫詞表、也不必逐詞對齊的切入點。
2. **保留首尾、對齊中段**：只在中間層對齊、讓前後層保留語言專屬的詞法與表層，或許能在「能力遷移」與「語言多樣性」之間取得平衡；臺灣南島語若使用 MoE 模型，可參考這種分層設計，但需實驗驗證。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Bandarkar, L., Peng, C., Ahmed, A. H., Khandelwal, A., & Peng, N. (2026). Cross-Lingual Alignment for Decoder-Only Models using MoE Routers. *arXiv preprint arXiv:2610.01921*. [https://arxiv.org/abs/2610.01921](https://arxiv.org/abs/2610.01921)
  * 公開程式碼：[GitHub / lucasbandarkar/xl_moe_alignment](https://github.com/lucasbandarkar/xl_moe_alignment)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026-cross-lingual-alignment-moe-routers-bandarkar.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-cross-lingual-alignment-moe-routers-bandarkar.md](../evidence/2026-cross-lingual-alignment-moe-routers-bandarkar.md)
