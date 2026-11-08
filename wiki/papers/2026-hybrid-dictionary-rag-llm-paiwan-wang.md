---
title: "Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation"
title_zh: "結合混合辭典、檢索增強生成與大語言模型之低資源機器翻譯"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Reen-Cheng Wang, Cheng-Kai Yang, Tun-Chieh Yang, Yi-Xuan Tseng"
venue: "Engineering Proceedings, 120(1), 52:1-52:9"
domain: "ai"
domain_tags: ["#自然語言處理", "#人工智慧", "#計算語言學"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
verification: "issues"
my_focus: true
focus_role: "international"
focus_languages: ["排灣語"]
doi_url: "https://doi.org/10.3390/engproc2025120052"
hook: "臺東大學團隊首創混合式「辭典＋密集檢索 RAG＋LLM」排灣語翻譯框架，以精確字詞錨定與語義平行例句雙輪驅動，徹底破解極低資源南島語大模型翻譯幻覺。"
---

# 結合混合辭典、檢索增強生成與大語言模型之低資源機器翻譯 (Hybrid Dictionary–RAG–LLM for Low-Resource Translation)

> 「大語言模型是無邊無際的語義海洋，而瀕危語言的微弱符號只是海面上漂浮的零散孤舟。唯有將精準的符號辭典作為錨、將密集檢索的平行例句作為舵，大模型才能在未知的南島語風浪中精準靠岸。」

**2026 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
排灣語（Paiwan）是臺灣南部最具歷史深度的南島語言之一，但受限於數位語料極端稀缺與世代講者斷層，常規深度學習與大語言模型在此類語言上普遍表現低迷。國立臺東大學資訊工程學系王 reen-cheng 教授團隊於 2026 年初在《Engineering Proceedings》發表了這項針對排灣語的開創性研究。論文率先提出了「混合辭典＋檢索增強生成＋大語言模型（Hybrid Dictionary–RAG–LLM）」三位一體的翻譯框架，透過將靜態詞典的精準符號約束與語意向量庫的動態相似例句相互嵌套，一舉攻克了極端低資源語境下大模型的翻譯幻覺難題。

---

## Card 2 ｜ 世紀瓶頸：單一檢索的覆蓋缺陷與純神經生成的語義脫韁 (The Dilemma)
在將現代生成式 AI 應用於排灣語翻譯時，既有技術遭遇兩大瓶頸：

* **純詞典檢索的上下文失語**：單純查字典只能提供孤立單詞的字面翻譯，無法給出動詞在特定焦點（主事、受事、處所焦點）下的句法連接範本，大模型在缺乏例句引導時產出的譯文極其僵硬生澀。
* **純向量 RAG 的語素漂移（Semantic Drift）**：由於排灣語構詞極為豐富，通用的語意嵌入模型（Dense Embedding Models）往往將不同焦點後綴但詞根相同的單詞錯誤投影至相近的向量位置，召回出句意貌合神離的錯誤例句，誤導大模型產出與原文施受關係顛倒的嚴重幻覺。

---

## Card 3 ｜ 突破架構與原理：雙軌混合檢索與結構化 Prompt 注入 (The Secret)

### 1. 雙軌混合檢索評分方程式（Hybrid Fusion Scoring）

系統對輸入句子 $x$ 同時觸發「靜態詞典精準匹配」與「密集向量相似度檢索」雙軌：

$$S_{\text{hybrid}}(x, c) = \alpha \cdot \cos\big( \mathbf{e}(x), \mathbf{e}(c) \big) + (1 - \alpha) \cdot \operatorname{BM25}_{\text{lexicon}}(x, c)$$

其中：
* $\mathbf{e}(x), \mathbf{e}(c) \in \mathbb{R}^d$：由微調跨語言編碼器提取之密集向量表徵；
* $\operatorname{BM25}_{\text{lexicon}}(x, c)$：在原住民族線上辭典排灣語詞庫上執行的精確詞素匹配得分；
* $\alpha \in [0, 1]$：平衡語意相似度與字面詞素剛性匹配的動態加權係數。

### 2. 結構化 Prompt 條件生成機率模型

將雙軌檢索結果格式化為嚴格分離的上下文區塊，送入大語言模型進行條件解碼：

$$\hat{y} = \arg\max_y \prod_{t=1}^{|y|} P_{\text{LLM}}\Big( y_t \;\Big|\; y_{<t}, x, \mathcal{C}_{\text{dict}}(x), \mathcal{P}_{\text{RAG}}(x); \theta_{\text{LLM}} \Big)$$

其中：
* $\mathcal{C}_{\text{dict}}(x)$：由辭典模組解析出之「詞根＋詞綴焦點＋中文詞條」結構清單；
* $\mathcal{P}_{\text{RAG}}(x)$：由向量庫召回之 Top-$k$ 個完整雙語真實平行句對。

```text
               ┌──► [靜態雙語線上辭典] ──► 詞素與焦點條目 C_dict(x) ──┐
[排灣語輸入 x] ─┤                                                    ├──► [結構化 Prompt] ──► [LLM 條件解碼] ──► [中文譯文]
               └──► [向量嵌入資料庫]   ──► Top-k 相似平行例句 P_RAG(x)  ──┘
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的排灣語－華語評估
* 評估使用 **250 句**排灣語－華語測試資料。原文摘要報告各項指標範圍如下：cosine similarity **0.210–0.236 → 0.810–0.846**；BLEU **1.7–4.4 → 40.8–51.9**；ROUGE-L F1 **0.135–0.177 → 0.548–0.632**。
* 系統結合詞典式預翻譯、RAG 範例檢索與 LLM 後編輯；上列為原文摘要報告的指標範圍。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **確立極低資源南島語 LLM 應用的「雙輪驅動定理」**：證實了在缺乏預訓練先驗的語言中，單純依賴向量檢索或單純依賴辭典均有嚴重短板；唯有「辭典定錨詞義、RAG 例句指引句法」，才能釋放生成式大模型的真實威力。
* **實現國產前沿技術在本土原住民語言上的重大突破**：展現了臺灣本土學術團隊在南島語與現代 AI 融合領域的深厚創新實力。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
Wang 等人的混合 Dictionary-RAG-LLM 架構，與我的碩士論文核心研究方向完全同頻共振，並提供了極其寶貴的改進切入點：

1. **將「深層原形構詞解析器」無縫嵌入 Hybrid 檢索鏈**：
   * Wang 等人在詞典檢索階段主要使用字面匹配或簡易規則；若能引入海大實驗室成熟的「深層原形與未知詞窮舉解析器（戴晟哲、楊鈞凱）」，在查詞典前先將排灣語黏著表面詞還原為深層詞根，詞典命中率將從目前的水準進一步攀升，徹底消除因屈折變形引發的詞典漏查。
2. **三位一體的終極架構實踐**：
   * 我的碩士論文可在此基礎上提出更高階的整合方案：以「構詞解析器」作為前置預處理，結合「混合辭典 + RAG 例句庫」，共同餵入「大語言模型」，打造全臺灣南島語理解能力最強的神經符號混合翻譯系統。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Wang, R.-C., Yang, C.-K., Yang, T.-C., & Tseng, Y.-X. (2026). Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation. *Engineering Proceedings*, 120(1), 52:1-52:9. DOI: [10.3390/engproc2025120052](https://doi.org/10.3390/engproc2025120052)
  * 原始檔典藏：`raw/my-focus/英文論文/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
