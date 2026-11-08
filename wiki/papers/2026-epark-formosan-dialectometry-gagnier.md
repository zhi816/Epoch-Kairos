---
title: "Dialectometry and Evaluation of the ePark Corpus for Low-Resource Formosan Language Dialects"
title_zh: "族語 E 樂園語料庫之方言計量學分析與低資源臺灣南島語方言評估"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Henry Gagnier"
venue: "Proceedings of Workshop on Dialects in NLP — A Resource Perspective (DialRes 2026), 124-134"
domain: "ai"
domain_tags: ["#計算語言學", "#自然語言處理"]
concepts: ["formosan-computational-linguistics"]
status: "wiki"
my_focus: true
doi_url: "https://doi.org/10.18653/v1/2026.dialres-1.13"
hook: "首度對臺灣原民會族語 E 樂園（ePark）42 種方言展開大規模計量方言學分析，以正規化編輯距離與聚類矩陣精準量化南島語親緣分支與語料品質。"
---

# 族語 E 樂園語料庫之方言計量學分析與低資源臺灣南島語方言評估 (Dialectometry and Evaluation of the ePark Corpus)

> 「方言不是語言演化的碎屑，而是歷史在地理山川間刻下的活體等高線。透過計算方言學的精確度量，我們得以穿透教材編寫的表面同質化，看見四十二種南島鄉音真實的親疏密碼。」

**2026 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
臺灣南島語言是世界南島語系的發源樞紐，但長期以來，其內部多達 16 族、42 種次方言群的親緣細分與計算特徵鮮少受到國際 NLP 界的系統性量化。由原住民族語言研究發展基金會主持建置的「族語 E 樂園（ePark）」是全球規模最大、最完整的臺灣原住民族語數位教材庫。美國計算語言學新銳學者 Henry Gagnier 於 DialRes 2026 研討會發表此項研究，首次將現代方言計量學（Dialectometry）全面應用於 ePark 語料庫，透過數十萬詞彙的字元對齊與字串距離矩陣，客觀評估了該語料庫作為低資源 NLP 資源的優勢、盲區與方言分群能力。

---

## Card 2 ｜ 世紀瓶頸：次方言邊界爭端與教材標準化的雙刃劍 (The Dilemma)
在利用現有臺灣南島語語料進行計算建模時，研究者面臨兩大深層困境：

* **次方言劃分（Subgrouping）的歷史分歧與缺乏量化基準**：歷史語言學家（如 Paul Jen-kuei Li 李壬癸、Robert Blust 等）對於部分南島語次方言的歸屬長期存在爭議。傳統依賴人工音變構擬的定性分析耗時費力，缺乏現代計算語言學的大規模語料自動統計驗證。
* **統一教材編寫導致的「人為語音同質化（Artificial Homogenization）」**：族語 E 樂園在數位化過程中，為了教學便利，部分音標與書寫系統經歷了標準化委員會的修訂。這種修訂是否抹去了某些瀕危方言獨特的構詞與音韻特徵，先前從未有客觀的語料庫層級審查。

---

## Card 3 ｜ 突破架構與原理：正規化 Levenshtein 距離與層次聚類拓撲 (The Secret)

### 1. 跨方言正規化編輯距離方程式（Normalized Levenshtein Distance, NLD）

設方言 $A$ 與方言 $B$ 共享同一個語義概念的詞彙集合為 $\mathcal{V}_{AB}$。對於概念詞條 $w \in \mathcal{V}_{AB}$，其表面拼寫字串分別為 $s_A(w)$ 與 $s_B(w)$。兩方言間的詞彙距離定義為正規化 Levenshtein 距離的期望值：

$$D(A, B) = \frac{1}{|\mathcal{V}_{AB}|} \sum_{w \in \mathcal{V}_{AB}} \frac{\operatorname{LD}\big( s_A(w), s_B(w) \big)}{\max\big( |s_A(w)|, |s_B(w)| \big)}$$

其中 $\operatorname{LD}(s_1, s_2)$ 為標準編輯距離（插入、刪除、替換操作之最小代價）。

### 2. UPGMA 親緣樹分群與拓撲重構

透過構造全對全 $42 \times 42$ 方言距離矩陣 $\mathbf{D} \in \mathbb{R}^{42 \times 42}$，採用非加權組平均法（UPGMA）迭代合併距離最近的方言集群：

$$D(C_i \cup C_j, C_k) = \frac{|C_i|}{|C_i| + |C_j|} D(C_i, C_k) + \frac{|C_j|}{|C_i| + |C_j|} D(C_j, C_k)$$

```text
[ePark 42 種南島方言全語料庫] ──► [抽取語義對齊共享概念詞表 V_{AB}]
                                                   │
                                                   ▼
[計算全對全 Levenshtein 距離矩陣 D] ──► [UPGMA 層次聚類與多維尺度分析 MDS] ──► [驗證 16 族 42 方言親緣演化樹]
```

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Gagnier 2026）之核心證據
* **語料庫覆蓋範圍**：
  * 全面覆蓋臺灣原住民 **16 族全數 42 種官方認證方言變體**。
  * 提取跨方言對齊詞項超過 **$120,000$ 條**，構成臺灣南島語歷史上最大規模的方言計算矩陣。
* **方言計量學分群精確度**：
  * **計算樹與歷史語言學一致率**：演算法自動產生的樹狀拓撲在 **$86.4\%$** 的分支上精準復原了李壬癸等權威學者確立的語言學分類。
  * **泛泰雅語群內部驗證**：精準切分出賽考利克泰雅語（Squliq）、澤敖利泰雅語（C'uli'）、太魯閣語（Truku）與賽德克語都達／德路固／德克達雅三大次方言的階層距離。
  * **布農語五大方言群（郡社、巒社、丹社、卡社、卓社）**：距離矩陣顯示卓社與卡社的音韻距離最遠，完美印證了卓社群保留古輔音的田野結論。
* **ePark 語料庫評估發現之缺陷**：
  * 揭示少數偏遠方言（如沙阿魯阿語、卡那卡那富語）在部分階級教材中存在詞彙簡化與範例句重複率過高（超過 $35\%$）的問題，提醒 NLP 學者在訓練模型時需進行去重過濾。

### 相關文獻對照（非本篇成果，標註出處）
* **Blust (1999) & Li (2008)**：傳統南島語分群理論；Gagnier 的計算方言學研究提供了首次基於數位全語料庫的大規模統計驗證。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **將「族語 E 樂園」由純教學網站升格為國際級學術研究語料庫**：為國際計算語言學界揭開了臺灣原民會這座龐大數位寶庫的真實架構，建立了首套開源的方言計量評估腳本。
* **為跨方言機器翻譯奠定「語法距離矩陣」**：研究量化出的 $42 \times 42$ 距離矩陣，可直接作為多語言模型中知識遷移權重的數學依據。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
Gagnier 對 ePark 語料庫的方言計量分析，對我的碩士論文研究提供了極其關鍵的資料工程認知：

1. **多語言遷移權重的量化設計**：
   * 在訓練泛泰雅語或布農語的多語言機器翻譯模型時，我們過去常常均勻採樣或憑經驗給予權重。
   * **啟發**：可直接導入 Gagnier 算出的方言距離矩陣 $D(A, B)$！在遷移學習時，根據方言距離設計自適應溫度係數 $\tau_{AB} \propto 1/D(A, B)$，距離越近的方言賦予更高的正向遷移權重，有效防範負遷移（Negative Transfer）。
2. **語料庫清洗與標準化校準**：
   * 論文指出的 ePark 教材重複率與音標同質化問題，提醒我們在將 ePark 用於訓練神經網絡與構詞解析器前，必須先執行嚴格的正規化清洗與去重管線。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
* **原始權威文獻**：
  * 官方學術出處：Gagnier, H. (2026). Dialectometry and Evaluation of the ePark Corpus for Low-Resource Formosan Language Dialects. In *Proceedings of Workshop on Dialects in NLP — A Resource Perspective (DialRes 2026)* (pp. 124-134). DOI: [10.18653/v1/2026.dialres-1.13](https://doi.org/10.18653/v1/2026.dialres-1.13)
  * 原始檔典藏：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
