---
title: "Formosan Computational Linguistics & Morphological Analysis"
title_zh: "臺灣南島語計算語言學與構詞解析"
domain: "ai"
domain_tags: ["#計算語言學", "#自然語言處理", "#人工智慧"]
papers:
  - "2021-seediq-chinese-mt-you"
  - "2022-formosan-say-verbs-hsieh"
  - "2023-atayal-truku-morphology-dai"
  - "2023-atayalic-multilingual-mt-liao"
  - "2024-formosan-temporal-words-lim"
  - "2024-formosan-mt-bilingual-lexicon-zheng"
  - "2024-taiwanese-mt-resegmentation-tang"
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
  * 泛泰雅語群（泰雅語、賽德克語、太魯閣語）及排灣語、布農語中，詞綴附加常伴隨母音音變（Vowel Shift）、詞尾弱化脫落（Deletion）與中綴插入（Infixation）。
  * 透過構詞律匹配、二元音韻轉移轉移機率以及候選詞根排名，使未知表面形能準確逆向對映回深層原形：
    $$\text{Surface Form} \xrightarrow{\mathcal{T}_{\text{morph}}^{-1}} \langle \text{Prefixes}, \text{Infixes}, \text{Root}, \text{Suffixes} \rangle$$
  * 詳見核心研究：[賽德克語－中文機器翻譯之研究（游景勝 2021）](../papers/2021-seediq-chinese-mt-you.md)、[泰雅語與太魯閣語構詞結構之自動解析（戴晟哲 2023）](../papers/2023-atayal-truku-morphology-dai.md)、[排灣語、布農語構詞結構解析與機器翻譯（吳維中 2025）](../papers/2025-paiwan-bunun-morphology-mt-wu.md)。

* **構詞規則窮舉與未知詞消解（Morphological Enumeration for OOV）**：
  * 針對辭典未收錄之未知詞（OOV），利用音韻變化規則與構詞律正向窮舉所有合法衍生形，結合詞根頻率、字串編輯距離與隨機森林排名器進行逆向溯源，突破極端低資源語境下的辭典覆蓋限制。
  * 詳見核心研究：[以構詞規則窮舉解決泛泰雅語未知詞問題（楊鈞凱 2025）](../papers/2025-atayalic-oov-enumeration-yang.md)。

* **類型學考察與語法化路徑（Typology & Grammaticalization）**：
  * 從跨語言語義場延伸考察「說」動詞之施為性向補語標記、示證標記之演化，以及時間推移詞之實現／非實現標記對稱性，為計算模型提供深厚之語言學歸納偏置。
  * 詳見核心文獻：[台灣南島語「說」動詞語義現象初探（謝富惠 2022）](../papers/2022-formosan-say-verbs-hsieh.md)、[台灣南島語言時間詞之跨語言比較初探（林鴻瑞 2024）](../papers/2024-formosan-temporal-words-lim.md)。

* **方言計量學與語料庫基礎設施（Dialectometry & Corpus Infrastructure）**：
  * 利用正規化 Levenshtein 編輯距離與多維度對齊，量化臺灣南島語 16 族 42 方言間的詞彙相似度與分支演化；建立涵蓋 15 種語言的標準化平行語料庫 FormosanMT 與多任務評測基準 FormosanBench。
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
