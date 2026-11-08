---
title: "Using Affixal Information to Improve the Performance of Atayalic Languages Machine Translation"
title_zh: "使用詞綴資訊提升泛泰雅語機器翻譯效能"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Bo-Yi Jin"
venue: "Master's Thesis, Department of Computer Science and Engineering, National Taiwan Ocean University"
domain: "ai"
domain_tags: ["#自然語言處理", "#深度學習", "#計算語言學"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
verification: "issues"
my_focus: true
focus_role: "senior-thesis"
focus_languages: ["泰雅語", "賽德克語", "太魯閣語"]
doi_url: "https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=y8Gq.y/record?yes=1"
hook: "提出三種族語文字表示形式與三種神經編碼器架構，深度融合深層詞根與多維詞綴特徵嵌入，顯著突破泛泰雅語群神經機器翻譯的語法焦點對齊瓶頸。"
---

# 使用詞綴資訊提升泛泰雅語機器翻譯效能 (Using Affixal Information to Improve the Performance of Atayalic Languages Machine Translation)

> 「在低資源南島語的深層語義世界裡，詞綴不是邊緣的修飾附屬，而是調度全句語法角色、焦點指向與時相維度的最高指揮官。將詞綴資訊顯式注入神經網路，等於為黑箱模型裝上了語言學的透視鏡。」

**2025 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
臺灣南島語屬於極度缺乏數位平行語料的極低資源語言（Extremely Low-Resource Languages），傳統神經機器翻譯（NMT）在面對動詞焦點變化複雜的泛泰雅語群（泰雅語、賽德克語、太魯閣語）時，極易發生主被動倒置、主語賓語混淆與時態錯亂。國立臺灣海洋大學林川傑教授指導、金柏毅於 2025 年 7 月完成的碩士論文《使用詞綴資訊提升泛泰雅語機器翻譯效能》，系統性探索了符號構詞語素在現代神經架構中的多維度融合方案。論文創新性地提出原文形式、詞根形式與詞綴字串形式三種資料呈現維度，並設計出結合詞綴嵌入向量的專屬 Transformer 編碼器，全面刷新了泛泰雅語群機器翻譯的基準線。

---

## Card 2 ｜ 世紀瓶頸：標準 Tokenizer 的構詞盲區與焦點訊號湮滅 (The Dilemma)
在極低資源語境下，常規的神經機器翻譯架構遭遇深層技術瓶頸：

* **統計分詞器（如 BPE）的構詞盲區**：標準 BPE 僅基於純頻率共現進行子詞切分，往往將具有強烈語法功能的詞綴（如表主事焦點之中綴 `-um-` 或受事焦點之 `-un`）截斷在隨機字元邊界，破壞了完整的語法標記信號。
* **神經注意力機制的信號湮滅**：在平行句對僅有萬句規模的低資源條件下，Transformer 的多頭注意力機制很難單憑少數例句自發學會深奧的南島語焦點對齊規律，導致翻譯模型在生成中文譯文時頻繁翻錯施事者（Agent）與受事者（Patient）。

---

## Card 3 ｜ 突破架構與原理：多重文本形態與詞綴神經融合編碼 (The Secret)

### 1. 三種族語文本表示形態（Representation Modalities）

金柏毅首先設計了三種互補的來源端文本序列化表徵：

1. **原文形式（Surface Form, $\mathbf{S}_{\text{surf}}$）**：保留真實書寫形式，保留完整語境與音韻表徵。
2. **詞根形式（Root Form, $\mathbf{S}_{\text{root}}$）**：經由構詞解析器將表面詞還原為深層原形詞根，消解表面變形。
3. **詞綴字串形式（Affix String Form, $\mathbf{S}_{\text{affix}}$）**：將前綴、中綴、後綴以顯式語法 Token 展開（例如：`[PRE:m] [ROOT:qaniq] [SUF:un]`）。

### 2. Encoder 端詞綴特徵融合數學方程式

在神經編碼器輸入端，金柏毅比較了多種融合策略，其中最佳架構為**多維詞綴特徵嵌入投影模型（Affix Embedding Projection）**：

$$\mathbf{x}_i = \operatorname{LayerNorm}\Big( \mathbf{e}_{\text{tok}}(w_i) + W_{\text{affix}} \mathbf{e}_{\text{affix}}(a_i) + \mathbf{p}_i \Big)$$

其中：
* $\mathbf{e}_{\text{tok}}(w_i) \in \mathbb{R}^{d_{\text{model}}}$：BPE 子詞或詞根嵌入向量。
* $\mathbf{e}_{\text{affix}}(a_i) \in \mathbb{R}^{d_a}$：由構詞解析器提取之詞綴語法類別嵌入表示。
* $W_{\text{affix}} \in \mathbb{R}^{d_{\text{model}} \times d_a}$：可學習的語義空間投影矩陣。
* $\mathbf{p}_i \in \mathbb{R}^{d_{\text{model}}}$：正弦位置編碼。

### 3. 跨層級多頭注意力交互

在 Transformer 的自注意力層中，查詢矩陣 $Q$、鍵矩陣 $K$ 與值矩陣 $V$ 均包含顯式詞綴特徵，使得注意力權重能直接依據焦點語法形態計算相關性：

$$\operatorname{Attention}(Q, K, V) = \operatorname{softmax}\left( \frac{(X W^Q)(X W^K)^\top}{\sqrt{d_k}} \right) (X W^V)$$

```text
[輸入表面詞序列] ──► [構詞解析器] ──► 詞綴標籤序列 a_i ──► [詞綴嵌入層 e_affix] ──┐
                                                                             ├──► [特徵投影融合] ──► [Transformer Encoder] ──► [中文解碼]
[BPE 斷詞子詞]   ───────────────────► 子詞序列 w_i     ──► [詞嵌入層 e_tok]    ──┘
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的詞綴特徵翻譯結果
* 原文摘要指出，詞綴資訊有助於泛泰雅語群機器翻譯。族語翻中文的最佳系統 BLEU 依賽德克語、泰雅語、太魯閣語順序為 **20.38、23.84、22.61**。
* 中文翻族語的最佳系統 BLEU 依相同語言順序為 **28.07、29.49、33.25**。
* 此卡僅列原文摘要明確報告的最佳系統 BLEU 分數。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **證實神經架構可高效內化高階符號構詞語意**：推翻了「深度神經網絡不需要外加符號特徵」的高資源偏見，證明在極低資源語境下，顯式注入構詞先驗是克服注意力過度自由度的最關鍵手段。
* **建立泛泰雅語群機器翻譯的最佳實踐典範**：確立了「構詞解析器提取詞綴 $\to$ 嵌入投影 $\to$ Transformer 聯合注意力」的標準架構管線。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
金柏毅的研究是實驗室在泛泰雅語群翻譯技術演進上的成熟結晶，為我的碩士論文提供了直接的技術對接點：

1. **詞綴顯式編碼與 LLM In-Context Learning 的語法引導**：
   * 金柏毅在神經網絡中使用向量嵌入融合詞綴；這啟發了我：在現代大語言模型（如 GPT-4o、DeepSeek、Llama3）的少樣本與 RAG 提示詞設計中，我們可以借鑒金柏毅的「詞綴字串形式」，將未知詞的焦點類型以顯式符號 Prompt 餵入大模型（例如：`[單詞: m-ekan] [語素結構: m-(主事焦點) + ekan(吃)]`），直接激發大模型的跨語言推理能力。
2. **多任務聯合解碼（Joint Decoding of Translation & Affix）**：
   * 未來可進一步設計在生成目標語中文的同時，要求解碼端輔助預測來源詞的焦點標籤，透過多任務學習實現更緊密的雙向注意力正則化。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 學位論文出處：金柏毅 (2025)。使用詞綴資訊提升泛泰雅語機器翻譯效能。國立臺灣海洋大學資訊工程學系碩士學位論文，指導教授：林川傑博士。
  * 原始檔典藏：`raw/my-focus/學長姐論文/使用詞綴資訊提升泛泰雅機器翻譯_金伯毅.pdf`（對應文字檔：`raw/my-focus/學長姐論文/.md/使用詞綴資訊提升泛泰雅機器翻譯_金伯毅.md`，由私有倉庫 Mine-RAW 版控）
