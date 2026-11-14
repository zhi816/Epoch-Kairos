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
  - "2026-cross-lingual-alignment-moe-routers-bandarkar"
  - "2026-data-centric-continual-pretraining-ji"
  - "2026-data-centric-russian-kyrgyz-mt-novokshanov"
  - "2026-formosanmt-parallel-corpus-scheppat"
  - "2026-hybrid-dictionary-rag-llm-paiwan-wang"
  - "2026-tao-filipino-nmt-macayan"
related_concepts:
  - "formosan-computational-linguistics"
verification: "partial"
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
  * 把構詞資訊提供給翻譯模型的做法，在海大實驗室的研究中有兩種代表：游景勝（2021）把 52 維布林詞綴特徵拼接在詞的表示之後，最佳系統使用詞彙原文（非詞根）搭配自訓練嵌入（BLEU 21.03 → 25.10），但同樣的特徵搭配小語料預訓練嵌入反而使 BLEU 由 22.28 降至 12.09；金柏毅（2025）把族語句改寫為「詞綴字串形式」，並以兩個獨立 encoder 分別編碼詞與布林詞綴特徵、輸出串接（FC_ftr_jnt）。詞綴資訊的效果隨表示方式與嵌入來源而異，不宜一概而論。
  * 詳見核心研究：[賽德克語－中文機器翻譯之研究（游景勝 2021）](../papers/2021-seediq-chinese-mt-you.md)、[使用詞綴資訊提升泛泰雅語機器翻譯效能（金柏毅 2025）](../papers/2025-atayalic-affix-mt-jin.md)。

* **跨語言遷移與多語言模型（Multilingual Transfer & Related Language Sharing）**：
  * 合併親屬語言的語料，以共享 BPE 子詞詞彙表與語言別標籤聯合訓練；或以資料較多的語言訓練父模型再微調。廖恒慶（2023）在泛泰雅三語上發現，未經子詞處理的直接合併效果不佳，共享 BPE 後的多語言系統優於單一族語，而以馬來語、印尼語父模型做遷移式學習又更好；作者認為訓練資料量的增加是主要因素。在純解碼器混合專家（MoE）大模型架構上，Bandarkar 等（2026）則以中間層路由器之序列平均權重分佈進行單向 KL 散度對齊，於 7 種目標語言與 4 款模型上改善跨語言遷移表現。
  * 詳見核心研究：[泛泰雅語群與中文之多語言機器翻譯研究（廖恒慶 2023）](../papers/2023-atayalic-multilingual-mt-liao.md)、[達悟語－菲律賓語神經機器翻譯（Macayan et al. 2026）](../papers/2026-tao-filipino-nmt-macayan.md)、[FormosanMT 多語言平行語料庫（Scheppat et al. 2026）](../papers/2026-formosanmt-parallel-corpus-scheppat.md)、[利用混合專家路由器實現純解碼器模型之跨語言表徵對齊（Bandarkar et al. 2026）](../papers/2026-cross-lingual-alignment-moe-routers-bandarkar.md)。

* **泛化資料增強與以資料為中心策略（Data Augmentation & Data-Centric Pipelines）**：
  * 利用回譯（Back-Translation）、高資源語言轉化（HRL-to-LRL Pivot）、隨機替換與雙語詞典直接注入，合成高品質偽平行數據；搭配多階段課程學習與跨語言語義過濾器（如 SONAR）淘汰噪聲句對。在大規模大語言模型擴展上，Ji 等（2026）建構涵蓋 500 餘種語言與 2,507 個語言對的 MaLA 雙語翻譯語料庫，並透過單語與雙語混合配方進行全參數持續預訓練，實證納入雙語平行句對可顯著提升 204 語翻譯與低資源泛化能力。
  * 詳見核心文獻：[低資源翻譯之泛化資料增強（Xia et al. 2019）](../papers/2019-generalized-data-augmentation-xia.md)、[芬蘭語－北薩米語回譯策略（Sälevä & Lignos 2024）](../papers/2024-finnish-northern-sami-mt-saleva.md)、[以雙語詞典提升臺灣南島語機器翻譯（Zheng et al. 2024）](../papers/2024-formosan-mt-bilingual-lexicon-zheng.md)、[五百餘語言的雙語持續預訓練（Ji et al. 2026）](../papers/2026-data-centric-continual-pretraining-ji.md)、[LoResMT 2026 突厥語冠軍資料策略（Novokshanov 2026）](../papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md)。

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
