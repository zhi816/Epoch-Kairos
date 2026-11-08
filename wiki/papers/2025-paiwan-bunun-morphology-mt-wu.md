---
title: "Automatic Morphological Analysis and Machine Translation in Paiwan and Bunun"
title_zh: "排灣語、布農語的構詞結構自動分析與機器翻譯"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Wei-Chung Wu"
venue: "Master's Thesis, Department of Computer Science and Engineering, National Taiwan Ocean University"
domain: "ai"
domain_tags: ["#計算語言學", "#自然語言處理", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
my_focus: true
doi_url: "https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=y8Gq.y/record?yes=1"
hook: "將構詞解析與神經機器翻譯體系由泛泰雅語群跨語系推廣至排灣語與布農語，創下構詞解析精確率 98.09% 與 99.79% 的驚人紀錄，驗證了構詞感知翻譯框架的跨語系普適性。"
---

# 排灣語、布農語的構詞結構自動分析與機器翻譯 (Automatic Morphological Analysis and Machine Translation in Paiwan and Bunun)

> 「當一套計算構詞與神經翻譯方法能跨越泰雅語族的高山，成功降落在排灣語與布農語的廣袤聚落中，它便不再只是特定方言的工程補丁，而是被昇華為通往整體臺灣南島語言結構的普遍密碼。」

**2025 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
在臺灣南島語言的自然語言處理版圖中，排灣語（Paiwan）與布農語（Bunun）分別屬於南島語系內部極具代表性的重要語族，擁有高度獨特的重疊構詞（Reduplication）、環綴（Circumfix）以及極度密集的時相焦點系統。然而過去針對這兩大族語的計算語言學工具與機器翻譯系統幾乎處於空白狀態。國立臺灣海洋大學林川傑教授指導、吳維中於 2025 年 7 月完成的碩士論文《排灣語、布農語的構詞結構自動分析與機器翻譯》，成功將實驗室歷代累積之構詞解析與神經翻譯體系跨越至排灣語與布農語，在構詞解析上取得了精準度超過 $98\%$ 的突破，並奠定了兩大族語現代神經機器翻譯的先驅基準。

---

## Card 2 ｜ 世紀瓶頸：跨語系結構異質性與重疊構詞的非連續障礙 (The Dilemma)
將泛泰雅語群之計算模型直接套用至排灣語與布農語時，面臨嚴重的語言學結構衝突：

* **重疊構詞（Reduplication）與環綴的非線性複合**：排灣語廣泛使用詞根首音節重疊（$\text{Ca}-$ 重疊或完全重疊）來表達進行貌、複數或反覆動作，並經常與前綴和後綴形成包夾詞根的「環綴（Circumfix，如 `ka-...-an`）」。傳統單向線性剝離演算法會將重疊音節誤判為獨立未知詞根。
* **布農語複雜複合動詞的多重焦點交織**：布農語具有豐富的詞彙複合化傾向，動詞焦點標記在句法中會隨主語格位動態連鎖轉換，導致標準 Transformer 模型在翻譯成長句時發生嚴重的語義漂移與代詞指代混淆。

---

## Card 3 ｜ 突破架構與原理：廣義構詞算子擴展與多語言遷移架構 (The Secret)

### 1. 排灣與布農語重疊及環綴解析代數

吳維中擴展了深層構詞還原模型，引入非連續重疊算子 $\operatorname{Redup}_k(\cdot)$ 與環綴分解算子：

$$w = \operatorname{Circum}\Big( a_{\text{circ}}, \operatorname{Redup}_k(r \odot a_{\text{in}}) \Big) \circ a_{\text{suf}}$$

其中：
* $\operatorname{Redup}_k(r)$：表示提取深層詞根 $r$ 之首部音節長度為 $k$ 的重複模式：
  $$\operatorname{Redup}_k(\sigma_1 \sigma_2 \dots \sigma_m) = \sigma_1 \dots \sigma_k \sigma_1 \sigma_2 \dots \sigma_m$$
* 逆向解析時，演算法先執行**音節週期性自相關檢測**，剝離重疊模式後還原基本詞根，再進行環綴對齊校驗。

### 2. 多語言神經機器翻譯與遷移學習目標

在機器翻譯模組中，採用深度 Transformer 架構，並融合跨語言遷移式學習（Transfer Learning）：

$$\theta^* = \arg\min_\theta \Big[ \mathcal{L}_{\text{Paiwan-Bunun}}(\theta) + \beta \mathcal{D}_{\text{KL}}\big( P(y \mid x; \theta) \,\|\, P_{\text{prior}}(y \mid x; \theta_{\text{pre}}) \big) \Big]$$

先在全臺灣南島語多語言語料庫上進行參數預訓練 $\theta_{\text{pre}}$，再透過正則化 KL 散度微調至排灣語與布農語專屬模型，確保低資源方言不會遺失通用的南島語法表徵。

```text
[輸入排灣/布農表面詞] ──► [重疊音節自相關檢測] ──► [環綴與中綴分離] ──► [深層詞根辭典匹配]
                                                                        │
        ┌───────────────────────────────────────────────────────────────┘
        ▼
[詞綴特徵向量提取] ──► [預訓練 Transformer 遷移編碼器] ──► [中文解碼輸出]
```

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（吳維中 2025）之核心證據
* **構詞結構自動解析評測（Precision & Accuracy）**：
  * **布農語（Bunun）**：在語法書與線上辭典例句驗證集上，整體詞彙構詞結構解析精確率達到驚人的 **$99.79\%$**，幾近完美解構所有黏著形態。
  * **排灣語（Paiwan）**：在處理極為繁複的重疊詞與環綴條件下，解析精確率達到 **$98.09\%$**。
* **機器翻譯評測指標（BLEU & 語義完整度）**：
  * **排灣語 $\leftrightarrow$ 中文**：多語言遷移學習與詞綴增強使排灣翻中文 BLEU 分數相比常規從頭訓練（Train from scratch）的單語 Transformer 獲得顯著躍升。
  * **布農語 $\leftrightarrow$ 中文**：引入詞嵌入預訓練後，解決了布農語長詞切分過碎的難題，翻譯流暢度與關鍵詞召回率大幅提升。

### 跨語族橫向對比數據（非本篇成果，標註出處）
* **游景勝 (2021) 賽德克語**：構詞解析準確度約 $90\%\sim 99\%$；
* **戴晟哲 (2023) 泰雅語與太魯閣語**：構詞解析準確度約 $88\%\sim 93\%$；
* **吳維中 (2025) 排灣語與布農語**：構詞解析精準度達到 $98\%\sim 99.8\%$，標誌著海大南島語構詞自動解析體系的全面成熟。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **實現臺灣南島語計算語言學的「跨語群大跨越」**：證明了先前在泰雅語族發展出的深層原形還原與詞綴向量建模方法，具備通向整個臺灣南島語系的泛化潛力。
* **為排灣語與布農語建立了首套高水準的開源 NLP 與 MT 基礎設施**：為後續這兩大族群的族語數位教材、AI 輔助母語教學提供了現成可用的核心引擎。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
吳維中將構詞解析與機器翻譯推廣至排灣語和布農語的成功經驗，為我的碩士論文研究提供了極高價值的指引：

1. **重疊構詞算子在 RAG 檢索中的關鍵應用**：
   * 排灣語的重疊詞在傳統檢索系統中常常引發檢索失敗。吳維中提出的重疊音節自相關剝離機制，可以直接作為 RAG 檢索前的標準 Query Normalizer，在發送向量檢索前自動將重疊形映射回語素基底，大幅改善檢索命中率。
2. **通向通用臺灣南島語統一解析器（Unified Formosan Parser）之可能性**：
   * 既然泛泰雅語群、排灣語、布農語均能由同一套「深層原形 + 音韻算子 + 詞綴投影」框架解析，這啟發了我在碩士論文中可以構想一個支援多族語的統一構詞解析中介層，為跨族語的多語言機器翻譯與大型語言模型提供一致的語意介面。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 學位論文出處：吳維中 (2025)。排灣語、布農語的構詞結構自動分析與機器翻譯。國立臺灣海洋大學資訊工程學系碩士學位論文，指導教授：林川傑博士。
  * 原始檔典藏：`raw/my-focus/學長姐論文/排灣布農的構詞結構自動分析與機器翻譯_吳維中.pdf`（對應文字檔：`raw/my-focus/學長姐論文/.md/排灣布農的構詞結構自動分析與機器翻譯_吳維中.md`，由私有倉庫 Mine-RAW 版控）
