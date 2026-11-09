---
title: "Formosan Computational Linguistics & Morphological Analysis"
title_zh: "臺灣南島語計算語言學與構詞解析"
domain: "ai"
domain_tags: ["#計算語言學", "#自然語言處理", "#人工智慧", "#語言學"]
papers:
  - "2021-seediq-chinese-mt-you"
  - "2022-formosan-say-verbs-hsieh"
  - "2023-atayal-truku-morphology-dai"
  - "2023-atayalic-multilingual-mt-liao"
  - "2024-formosan-temporal-words-lim"
  - "2024-formosan-mt-bilingual-lexicon-zheng"
  - "2025-atayalic-affix-mt-jin"
  - "2025-atayalic-oov-enumeration-yang"
  - "2025-formosanbench-llm-benchmark-lin"
  - "2025-indigenous-tek-ai-revitalization-wang"
  - "2025-paiwan-bunun-morphology-mt-wu"
  - "2026-epark-formosan-dialectometry-gagnier"
  - "2026-formosanmt-parallel-corpus-scheppat"
  - "2026-hybrid-dictionary-rag-llm-paiwan-wang"
  - "2026-tao-filipino-nmt-macayan"
related_concepts:
  - "low-resource-machine-translation"
verification: "issues"
---

# 概念：臺灣南島語計算語言學與構詞解析 (Formosan Computational Linguistics & Morphological Analysis)

> 領域：`#計算語言學` `#自然語言處理` `#人工智慧`

---

## 核心定義
**臺灣南島語言（Formosan Languages）**是整個南島語系（Austronesian Language Family）內部多樣性最高、歷史分化層次最深的活化石語言群，在世界語言類型學與演化歷史中佔據無可替代的起源地位（出臺灣假說，Out-of-Taiwan Hypothesis）。這類語言普遍展現極度複雜的**焦點系統（Focus System / Voice System）**與高度黏著甚至多式綜合的**構詞結構（Morphological Structure）**。
**臺灣南島語計算語言學**旨在運用計算模型、規則推導、音韻交替還原、方言計量學以及自然語言處理（NLP）技術，將深層詞根（Underlying Root）、時貌標記（Aspectual Affixes）與格位焦點結構自動解耦，克服極低數位資源與未知詞（OOV）瓶頸，推動瀕危母語的數位典藏、教學系統與下游多語言語意理解任務。

---

## 關鍵突破支柱與理論範式

* **構詞解析與深層原形還原（Deep Root Reconstruction）**：
  * 泛泰雅語群（泰雅語、賽德克語、太魯閣語）及排灣語、布農語中，詞根加後綴時結尾常改變（深層原形），書寫時元音會被刪略，並有中綴與重疊。
  * 海大實驗室的解析流程以「已知詞根」為輸入：先產生詞根的深層原形候選，窮舉中綴與後綴組合，比對目標詞的後半段，剩餘部分再以一元或二元機率模型判斷前綴組合（Lin et al., 2020；游景勝 2021；戴晟哲 2023）。各語言須另補專屬規則，例如泰雅語、太魯閣語改用三條書寫比對規則，排灣語另處理「重複詞根最後兩音節」的重疊（吳維中 2025）。概念上可寫成（Wiki 整理，非任一篇原文公式）：
    $$\langle \text{Word}, \text{Root} \rangle \;\longmapsto\; \langle \text{Prefixes}, \text{Infixes}, \text{Root}, \text{Suffixes} \rangle$$
  * 詳見核心研究：[賽德克語－中文機器翻譯之研究（游景勝 2021）](../papers/2021-seediq-chinese-mt-you.md)、[泰雅語與太魯閣語構詞結構之自動解析（戴晟哲 2023）](../papers/2023-atayal-truku-morphology-dai.md)、[排灣語、布農語構詞結構解析與機器翻譯（吳維中 2025）](../papers/2025-paiwan-bunun-morphology-mt-wu.md)。

* **構詞規則窮舉與未知詞消解（Morphological Enumeration for OOV）**：
  * 針對辭典未收錄之未知詞（OOV），為每個已知詞根窮舉其深層原形、音韻變化與加中綴後的字串，與未知詞比對並檢查前後綴是否合法，挑出候選詞根；再以 44 個特徵的成對比較隨機森林分類器兩兩投票選出詞根。原規劃的書寫形式篩選因濾掉過多正解而未採用。已知詞驗證資料正確率逾九成，賽德克語真實未知詞為 63.88%（族語 E 樂園）與 72.12%（臺大語料庫）。
  * 詳見核心研究：[以構詞規則窮舉解決泛泰雅語未知詞問題（楊鈞凱 2025）](../papers/2025-atayalic-oov-enumeration-yang.md)。

* **類型學考察與語法化路徑（Typology & Grammaticalization）**：
  * 從跨語言語義場延伸考察「說」動詞之施為性向補語標記、示證標記之演化，以及時間推移詞之實現／非實現標記對稱性，為計算模型提供深厚之語言學歸納偏置。
  * 詳見核心文獻：[台灣南島語「說」動詞語義現象初探（謝富惠 2022）](../papers/2022-formosan-say-verbs-hsieh.md)、[台灣南島語言時間詞之跨語言比較初探（林鴻瑞 2024）](../papers/2024-formosan-temporal-words-lim.md)。

* **方言計量學與語料庫基礎設施（Dialectometry & Corpus Infrastructure）**：
  * 利用詞級 TF-IDF 餘弦相似度、頻率 $\ge 5$ 詞型 Jaccard 相似度與前 500 高頻詞之字元級正規化 Levenshtein 距離，量化評估族語 E 樂園（ePark）16 族 42 方言間的詞彙重疊與親緣關係；建立涵蓋 15 種語言的標準化平行語料庫 FormosanMT 與多任務評測基準 FormosanBench。
  * 詳見核心研究：[ePark 語料庫方言計量學評估（Gagnier 2026）](../papers/2026-epark-formosan-dialectometry-gagnier.md)、[FormosanMT 多語言平行語料庫（Scheppat et al. 2026）](../papers/2026-formosanmt-parallel-corpus-scheppat.md)、[FormosanBench 大模型基準（Lin et al. 2025）](../papers/2025-formosanbench-llm-benchmark-lin.md)。

---

## 跨學科交會與延伸

1. **計算構詞學與現代神經架構的融合**：
   * 傳統通用斷詞法（如 Byte-Pair Encoding, BPE）若直接套用於高黏著度南島語，常因頻率驅動而將語素（Morpheme）切碎在錯誤邊界。
   * 將語言學構詞特徵（詞綴向量、深層詞根）作為顯式先驗嵌入神經網路，可使極低資源翻譯模型之注意力對齊更具可解釋性與強健性。
2. **本土文化傳統知識（TEK）與現代生成式 AI 的交織**：
   * 原住民族傳統生態知識（TEK）以口傳與祭儀深度嵌合於語言之中。將本體論結構、詞典檢索與檢索增強生成（RAG）結合，可打破語言壁壘，實現文化知識的永續演進與活態傳承。

---

## 關聯概念網絡
* [低資源神經機器翻譯與檢索增強生成](low-resource-machine-translation.md)
