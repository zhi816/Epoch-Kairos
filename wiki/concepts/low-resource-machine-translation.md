---
title: "Low-Resource Neural Machine Translation & Retrieval-Augmented Generation"
title_zh: "低資源神經機器翻譯與檢索增強生成"
domain: "ai"
domain_tags: ["#自然語言處理", "#深度學習", "#人工智慧", "#計算語言學"]
papers:
  - "2019-generalized-data-augmentation-xia"
  - "2021-seediq-chinese-mt-you"
  - "2023-atayalic-multilingual-mt-liao"
  - "2023-low-resource-nmt-survey-ranathunga"
  - "2024-finnish-northern-sami-mt-saleva"
  - "2024-formosan-mt-bilingual-lexicon-zheng"
  - "2024-taiwanese-mt-resegmentation-tang"
  - "2025-atayalic-affix-mt-jin"
  - "2025-formosanbench-llm-benchmark-lin"
  - "2025-fragment-shot-reasoning-mt-frontull"
  - "2025-manchu-in-context-mt-pei"
  - "2025-paiwan-bunun-morphology-mt-wu"
  - "2025-tulun-adaptable-lrl-mt-merx"
  - "2026-context-volume-rag-domain-shift-setiawan"
  - "2026-data-centric-russian-kyrgyz-mt-novokshanov"
  - "2026-formosanmt-parallel-corpus-scheppat"
  - "2026-hybrid-dictionary-rag-llm-paiwan-wang"
  - "2026-tao-filipino-nmt-macayan"
related_concepts:
  - "formosan-computational-linguistics"
verification: "unverified"
---

# 概念：低資源神經機器翻譯與檢索增強生成 (Low-Resource Neural Machine Translation & Retrieval-Augmented Generation)

> 領域：`#自然語言處理` `#深度學習` `#人工智慧` `#計算語言學`

---

## 核心定義
在神經機器翻譯（NMT）與大型語言模型（LLM）的繁榮發展中，高資源語言享有數以億計的雙語平行句對（Bitext）與龐大的網路預訓練資料；然而，全球超過 7,000 種活態語言中，絕大多數屬於**低資源語言（Low-Resource Languages, LRLs）**乃至極低資源瀕危語言（Extremely Low-Resource Languages），其數位雙語語料往往少於數千句。
**低資源機器翻譯與檢索增強生成**專門研究在資料極度稀缺、分佈偏移（Domain Shift）嚴重與構詞極端複雜的情境下，如何透過：
1. **先驗知識注入與構詞感知表示**（詞綴特徵、深層原形、雙語詞典對齊）；
2. **多語言遷移與跨語言知識共用**（Multilingual Transfer、語族共享 BPE、親屬語言回譯）；
3. **以資料為中心之強化學習與過濾機制**（Data-Centric Curriculum Filtering）；
4. **大型語言模型之檢索增強生成（RAG）、語境容量擴展（Context Volume）與少樣本推理（Fragment-Shot ICL）**；
使機器能夠在微量監督數據下突破泛化瓶頸，產出高語意保真度與語法流暢度的目標語翻譯。

---

## 關鍵技術路徑與核心突破

* **構詞特徵增強與架構調適（Morphology-Enhanced Architecture）**：
  * 在極低資源語境下，將構詞分析器產生的前綴、中綴、後綴標記向量化，與詞根嵌入向量以拼接（Concatenation）、加法或注意力權重融合，顯式提供語法與焦點特徵：
    $$e(w) = W_{\text{proj}} [e_{\text{root}}(w) \,\|\, e_{\text{affix}}(w)]$$
  * 詳見核心研究：[賽德克語－中文機器翻譯之研究（游景勝 2021）](../papers/2021-seediq-chinese-mt-you.md)、[使用詞綴資訊提升泛泰雅語機器翻譯效能（金柏毅 2025）](../papers/2025-atayalic-affix-mt-jin.md)。

* **跨語言遷移與多語言模型（Multilingual Transfer & Related Language Sharing）**：
  * 利用親屬語言之間的語法同源性與詞彙同源詞（Cognates），透過共享 BPE 子詞詞彙表進行聯合訓練，顯著降低低資源語言的 OOV 率並實現零樣本或微量樣本跨語言知識遷移。
  * 詳見核心研究：[泛泰雅語群與中文之多語言機器翻譯研究（廖恒慶 2023）](../papers/2023-atayalic-multilingual-mt-liao.md)、[達悟語－菲律賓語神經機器翻譯（Macayan et al. 2026）](../papers/2026-tao-filipino-nmt-macayan.md)、[FormosanMT 多語言平行語料庫（Scheppat et al. 2026）](../papers/2026-formosanmt-parallel-corpus-scheppat.md)。

* **泛化資料增強與以資料為中心策略（Data Augmentation & Data-Centric Pipelines）**：
  * 利用回譯（Back-Translation）、高資源語言轉化（HRL-to-LRL Pivot）、隨機替換與雙語詞典直接注入，合成高品質偽平行數據；搭配多階段課程學習與跨語言語義過濾器（如 SONAR）淘汰噪聲句對。
  * 詳見核心文獻：[低資源翻譯之泛化資料增強（Xia et al. 2019）](../papers/2019-generalized-data-augmentation-xia.md)、[芬蘭語－北薩米語回譯策略（Sälevä & Lignos 2024）](../papers/2024-finnish-northern-sami-mt-saleva.md)、[以雙語詞典提升臺灣南島語機器翻譯（Zheng et al. 2024）](../papers/2024-formosan-mt-bilingual-lexicon-zheng.md)、[LoResMT 2026 突厥語冠軍資料策略（Novokshanov 2026）](../papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md)。

* **大型語言模型檢索增強生成與上下文學習（LLM ICL & RAG）**：
  * 當傳統微調因訓練集太小而發生過擬合時，利用外部詞典、語法手冊、翻譯記憶庫（Translation Memory）與密集檢索器，透過高語境容量（Context Volume）、片段少樣本（Fragment-Shot）或動態後編輯（Post-Editing），引導大模型完成高品質翻譯。
  * 詳見核心研究：[滿語上下文機器翻譯理解（Pei et al. 2025）](../papers/2025-manchu-in-context-mt-pei.md)、[片段少樣本推理翻譯（Frontull & Ströhle 2025）](../papers/2025-fragment-shot-reasoning-mt-frontull.md)、[TULUN 可自適應低資源翻譯（Merx et al. 2025）](../papers/2025-tulun-adaptable-lrl-mt-merx.md)、[混合詞典 RAG 大模型排灣語翻譯（Wang et al. 2026）](../papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md)、[語境容量驅動極低資源 RAG 克服領域偏移（Setiawan et al. 2026）](../papers/2026-context-volume-rag-domain-shift-setiawan.md)。

---

## 系統架構演進：從序列統計到神經符號檢索

```text
階段一：統計與淺層神經模型（SMT / RNN-NMT）
       依賴小規模片語對齊，未登錄詞（OOV）導致嚴重語義脫落
                            │
                            ▼
階段二：Transformer 構詞增強與多語言遷移（Multilingual NMT）
       透過共享 BPE、詞綴嵌入向量與回譯資料擴增，大幅改善語法對齊
                            │
                            ▼
階段三：神經符號檢索增強與大語言模型（RAG + LLM Reasoning）
       結合深層構詞分析、結構化詞典檢索與長語境少樣本推理，實現領域自適應
```

---

## 關聯概念網絡
* [臺灣南島語計算語言學與構詞解析](formosan-computational-linguistics.md)
