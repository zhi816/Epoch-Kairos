---
title: "Improving Low-Resource Machine Translation for Formosan Languages Using Bilingual Lexical Resources"
title_zh: "利用雙語詞彙資源改善臺灣南島語言之低資源機器翻譯"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Francis Zheng, Edison Marrese-Taylor, Yutaka Matsuo"
venue: "Findings of the Association for Computational Linguistics: ACL 2024, 11248-11259"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "published"
verification: "verified"
my_focus: true
focus_role: "international"
focus_languages: ["臺灣南島諸語"]
doi_url: "https://doi.org/10.18653/v1/2024.findings-acl.670"
hook: "把原住民族語言線上辭典的詞條直接當成平行資料加入訓練，16 種臺灣南島語與華語的翻譯全部提升；再搭配以詞典替換詞彙產生的偽平行資料，平均提升 5.55 BLEU、10.33 chrF。"
card_line: "把族語辭典的詞條拿來訓練，改善族語翻譯"
---

# 利用雙語詞彙資源改善臺灣南島語言之低資源機器翻譯 (Improving Low-Resource Machine Translation for Formosan Languages Using Bilingual Lexical Resources)

> 「當一種語言的平行句只有數千，辭典裡的數千條詞彙就是另一份尚未被用上的教材。」（本頁引言為 Wiki 撰寫，非原文）

**2024 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Zheng, Marrese-Taylor & Matsuo（東京大學工學系研究科），*Findings of ACL 2024*, pp. 11248–11259。另含西班牙語－納瓦特語的對照實驗。

---

## Card 1 ｜ 時代銘文 (The Hook)
全球約 7,000 種語言中約 70% 有詞典形式的資料（Wang et al. 2022；§1）。本文探討如何在訓練時加入雙語詞典的資訊，改善低資源翻譯，主要對象是華語與 16 種臺灣南島語（作者稱其皆為瀕臨消亡或極度瀕危）。作者收集了 16 種語言的平行句與詞典，比較三種做法：(1) 直接把詞典條目當成額外的平行資料；(2) 以詞典替換平行句中的詞，產生偽平行資料；(3) 兩者並用。三種做法都提升 BLEU 與 chrF，以 (3) 最多、(1) 次之、(2) 再次之（摘要）。

---

## Card 2 ｜ 世紀瓶頸：有詞典、缺平行句 (The Dilemma)
* **平行語料少**：各語言的平行句只有約 4,400 至 10,400 句（表 1, p. 11250），神經翻譯通常需要數百萬句。
* **詞典常被忽略**：雙語詞典比平行語料更容易取得、成本更低，能提供平行語料中沒出現的罕見詞資訊，但缺乏上下文（§1, p. 11248）。
* **先前做法**：既有研究多以詞典替換詞彙產生偽平行資料，或使用自動歸納的詞典；作者提出更簡單的做法——把現成詞典直接當成平行資料（§1–§2）。

---

## Card 3 ｜ 突破架構與原理：詞典即平行資料 (The Secret)

### 1. 資料（§3, pp. 11250–11251；表 1）
* 從原住民族語言研究發展基金會的「原住民族語言線上辭典」下載 PDF，轉成 HTML 後抽出詞條與例句。16 種語言：阿美、泰雅、布農、卡那卡那富、噶瑪蘭、排灣、卑南、魯凱、拉阿魯哇、賽夏、撒奇萊雅、賽德克、邵、太魯閣、鄒、達悟。
* 平行句依 8:1:1 切分為訓練、驗證、測試集；詞條數約 5,200 至 35,000（太魯閣語最多）。
* 作者特別說明英文文獻可能把太魯閣語與賽德克語混為一談（兩者共用 ISO 639-3 代碼 `trv`）；本文分開處理（p. 11251）。

### 2. 三種做法（§4–§5.1）
* **＋Lex.**：把「族語詞條」加到族語端、「華語釋義」加到華語端，視為額外平行資料。原文沒有權重或採樣設計。
* **＋PPD**：依 Wang et al. (2022)，用詞典替換平行句**族語端**的詞（華語端因斷詞困難不替換），與原平行資料一起訓練。替換率試過 10% 至 80%，多數情況以 **20%** 最好。
* **＋Lex.＋PPD**：兩者並用。

### 3. 模型（§4, p. 11251）
Transformer，編碼器與解碼器各 6 層、4 個注意力頭、隱藏維度 512、前饋 1024；SentencePiece unigram 詞彙 8,000；dropout 0.3；每個語言對與方向各訓練 2 小時。評估用 SacreBLEU 與 chrF（因臺灣南島語多為黏著語，另以字元層級評估）。

```text
[線上辭典 PDF] ──► 抽取 ──┬──► 平行例句（8:1:1 切分）──────────────────────┐
                         └──► 詞條（族語詞, 華語釋義）──► 直接當平行資料（＋Lex.）─┤
                                     └──► 替換平行句族語端 20% 的詞 ──► 偽平行資料（＋PPD）─┤
                                                                                         ▼
                                                                          Transformer 翻譯模型
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### ＋Lex. 對 16 種語言（表 2, p. 11252）
* 加入詞典後平均提升 **3.37 BLEU、6.06 chrF**；所有語言對、兩個方向、兩種指標**全部提升**。族語→華語平均 +2.90 BLEU，華語→族語平均 +3.84 BLEU；提升幅度 0.97 至 7.65 BLEU。

### 詞典量與平行句量（表 3–8, pp. 11252–11253）
* 加越多詞條，翻譯品質大致越好（各語言相關係數多在 0.9 以上）。
* 但**同樣數量的平行句比詞條更有用**：卡那卡那富語→華語，加 4,000 條詞條提升 3.11 BLEU，加 4,000 句平行句提升 6.22 BLEU（§5, p. 11253）。

### 三種做法比較（6 種語言；表 9, p. 11254）
* 所有情況下，＋Lex.＋PPD 都比只加詞典好。例如排灣語→華語：基線 3.80 → ＋Lex. 10.64 → ＋Lex.＋PPD 10.94 BLEU。
* 摘要報告方法 (3) 平均提升 **5.55 BLEU、10.33 chrF**。

### 其他實驗
* **外部詞典**：以 1,556 條的賽德克語辭典（Temi Nawi 編）測試，增益較小（賽德克語→華語 +0.51 BLEU），作者歸因於詞典較小、且不到一半的詞出現在平行句中（表 10, §5.2）。
* **西班牙語－納瓦特語**：方法同樣有效；西班牙語→納瓦特語 chrF 27.52，略高於 AmericasNLP 2023 最佳的 27.25，但 BLEU 較低（表 11, §5.3）。
* **多語言預訓練沒有明確幫助**：以 16 種語言一起預訓練再微調，BLEU 平均只高 0.15、chrF 反而低 0.17；作者推測臺灣南島語彼此差異太大、資料也太少（表 12, §5.4）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **作者結論**（§6）：詞典是改善低資源翻譯的重要資源，在平行語料有限時可明確教模型詞彙對應。
* **作者自述的限制**：詞典與平行句的重疊程度難以定義（尤其華語的「詞」界線模糊）；可用的外部詞典很少（§5.2）。本文自建的詞典條目幾乎都出現在平行句中，這可能使詞典的效果偏高；外部詞典的增益明顯較小。
* （Wiki 詮釋）表 9 的阿美語數列有重複數值（如「＋Lex.」族語→華語與基線華語→族語皆為 11.12／32.10），可能有誤植，引用時宜謹慎。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **詞典條目可以直接進訓練資料**：
   * 本文顯示這是最簡單、在 16 種語言上都有效的做法。我的研究若訓練或微調翻譯模型，可先以此作為基線。
2. **詞典與構詞解析結合**：
   * 線上辭典的詞條多為特定詞形；若以構詞規則從詞根衍生其他詞形再加入，或可涵蓋更多表面形。此想法本文未實驗，衍生出的詞形可能有錯，需實驗驗證。
3. **詞典與平行句的重疊**：
   * 本文的增益可能部分來自詞典與測試句高度重疊。評估詞典增強或 RAG 效果時，宜同時用與詞典來源不同的測試資料。
4. **RAG 索引**：
   * 線上辭典的詞條與例句也適合建立 BM25 或向量檢索索引（參見 Pei et al. 2025 對詞典與例句檢索的結果）。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Zheng, F., Marrese-Taylor, E., & Matsuo, Y. (2024). Improving Low-Resource Machine Translation for Formosan Languages Using Bilingual Lexical Resources. In *Findings of the Association for Computational Linguistics: ACL 2024* (pp. 11248-11259). DOI: [10.18653/v1/2024.findings-acl.670](https://doi.org/10.18653/v1/2024.findings-acl.670)
  * 原始檔典藏：`raw/my-focus/英文論文/Improving Low-Resource Machine Translation for Formosan Languages _ 2024.findings-acl.670v2.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2024-formosan-mt-bilingual-lexicon-zheng.md](../evidence/2024-formosan-mt-bilingual-lexicon-zheng.md)
