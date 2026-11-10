---
title: "Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation"
title_zh: "結合混合辭典、檢索增強生成與大語言模型之低資源機器翻譯"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Reen-Cheng Wang, Cheng-Kai Yang, Tun-Chieh Yang, Yi-Xuan Tseng"
venue: "Engineering Proceedings, 120(1), 52:1-52:9"
venue_short: "Eng. Proc."
domain: "ai"
domain_tags: ["#自然語言處理", "#人工智慧", "#計算語言學"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
verification: "partial"
my_focus: true
focus_role: "international"
focus_languages: ["排灣語"]
doi_url: "https://doi.org/10.3390/engproc2025120052"
hook: "臺東大學團隊於 ICKII 2025 / Eng. Proc. 提出排灣語－華語混合翻譯管線：以記憶體 JSON 雜湊表詞典做預翻譯（未命中則 Fallback 至 Qdrant 向量檢索），再交由指令微調 LLM（GPT-4o mini、Llama 3.1、Gemma 3、DeepSeek-R1-Distill）進行語序重構與後編輯，在 250 句排灣語譯華語測試集上，使 BLEU 由 1.7–4.4 提高到 40.8–51.9。"
card_line: "先查辭典再交給大模型，把排灣語譯成華語"
---

# 結合混合辭典、檢索增強生成與大語言模型之低資源機器翻譯 (Hybrid Dictionary–RAG–LLM for Low-Resource Translation)

> 「大語言模型是無邊無際的語義海洋，而瀕危語言的微弱符號只是海面上漂浮的零散孤舟。唯有將精準的符號辭典作為錨、將條件分支檢索的平行例句作為舵，大模型才能在未知的南島語風浪中精準靠岸。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：國立臺東大學資訊工程學系作者團隊（通訊作者：王任慶 Reen-Cheng Wang；共同作者：楊承凱 Cheng-Kai Yang、楊惇傑 Tun-Chieh Yang、曾奕軒 Yi-Xuan Tseng），*Engineering Proceedings*, 120(1), 52, pp. 1–9（線上發表：2026 年 2 月 5 日；發表於 ICKII 2025 國際研討會）。以臺灣原住民族排灣語至華語（Paiwan $\to$ Mandarin）為實驗對象。

---

## Card 1 ｜ 時代銘文 (The Hook)
排灣語等臺灣原住民族語言面臨資料稀缺與講者人口減少的壓力；現有排灣語－華語工具多只能查詞，逐字輸出常語意不通（§1, p. 2）。文獻指出，平行語料少於 10 萬句時，遷移學習等既有低資源翻譯策略仍不足（§2, p. 2，引 Ranathunga et al.）。本篇實驗中，四個大型語言模型（LLM）未加本系統模組直接把排灣語譯成華語時，BLEU 僅 1.7–4.4（摘要；§4, p. 6）。

該研究由王任慶（Reen-Cheng Wang）等作者撰寫，於 2026 年 2 月 5 日在線上發表於 MDPI《Engineering Proceedings》，提出「混合辭典預翻譯 ＋ 向量 RAG 檢索 ＋ LLM 後編輯重構（Hybrid Dictionary–RAG–LLM）」三位一體管線。該方案以記憶體雜湊表提供確定性詞彙對齊，僅在詞典未命中時透過條件分支 Fallback 至 Qdrant 向量資料庫檢索平行例句，最後交由指令微調大模型重排語序與修飾成句，在 250 句排灣語譯華語測試集上，BLEU 由 1.7–4.4 提高到 **40.8–51.9**（摘要；§4, p. 6）。

---

## Card 2 ｜ 世紀瓶頸：單一檢索的局限與純大模型的語義失控 (The Dilemma)
在極低資源南島語翻譯中，單一技術路線均遭遇嚴重的結構性瓶頸（§1–§2, pp. 2–4）：

* **純詞典查找的字對字直譯**：現有排灣語－華語工具多只能查詞，無法滿足整句或整段翻譯；逐字輸出常造成語意不協調，也傳達不了語境與文化細節（§1, p. 2）。排灣語為動詞居首語言，具語態構詞，本篇的提示詞即特別說明這兩點（§3.4, p. 5）。
* **純向量檢索的例句稀疏**：排灣語以羅馬字書寫、書面語料極少，向量檢索可能因可用例句稀疏而失效（§2, p. 3）。
* **純大模型的表現不足**：本篇四個大模型在未加模組時，語意餘弦相似度僅 0.210–0.236、BLEU 僅 1.7–4.4（§4, p. 6），單獨使用難以勝任翻譯。

---

## Card 3 ｜ 突破架構與原理：串聯條件分支與三模組流水線 (The Secret)

原文為實證工程與架構設計論文，全文無理論加權公式（Card 3 早期版本之 BM25 線性加權為 Wiki 虛構，已予刪除）；其實際架構為**串聯式條件分支（If-Else Fallback）流水線**（§3.1–§3.2, pp. 4–5，圖 1–3）：

### 1. 模組一：雜湊表詞典預處理（Dictionary Pre-processing, 圖 1, p. 4）
* 自教育部東排灣語學習手冊、排灣語語法書與生活對話篇彙整高頻單詞與複合詞。
* 序列化為 JSON 格式並載入為記憶體內的**雜湊表（In-memory Hash Map）**，提供 $O(1)$ 常數時間的確定性精確字面映射（Deterministic Lexical Alignment）。

### 2. 模組二：條件分支與向量檢索（Vector Retrieval via Qdrant, 圖 2–3, pp. 4–5）
* 對輸入排灣語句子的每個詞元進行條件分支判斷：
  * **若雜湊表命中（`YES`）**：直接提取確定性的字面詞義，進行詞彙合併（Word Merge）。
  * **若雜湊表未命中（`NO`，詞典缺失）**：觸發 RAG 檢索模組，自儲存於 **`Qdrant`** 向量資料庫的教材與聖經平行句庫中，透過句子編碼器檢索語義最相關之上下文例句與近義片段，填補詞彙缺口。

### 3. 模組三：語法感知 LLM 後編輯（LLM Post-Editing, 圖 3, p. 5）
* 將詞典映射結果與檢索到的語境，組裝進語法感知提示詞（Syntax-aware Prompt）中。提示詞明確提示排灣語「動詞居首語序」與「焦點構詞特徵」。
* 指令微調大模型（評估 GPT-4o mini、Llama 3.1-70B、Gemma 3-27B 與 DeepSeek-R1-Distill-Llama-70B）執行語序重組（Reordering）、動詞屈折生成（Inflection）與詞義消歧，輸出流暢通順的現代華語。

```text
[輸入排灣語句子 x]
       │
       ▼ (逐詞查詢記憶體 JSON 雜湊表)
┌───────────────────────────────────────┐
│ 是 / 否在雜湊表詞典中？ (Hash Map)    │
└──────┬─────────────────────────┬──────┘
       │ [YES: 詞典命中]          │ [NO: 詞典未命中]
       ▼                         ▼
[確定性字面詞義合併]        [觸發 Qdrant 向量檢索召回相關平行例句]
       │                         │
       └──────────────┬──────────┘
                      ▼
        [組裝語法感知 Prompt (標註動詞居首與焦點)]
                      │
                      ▼
        [指令微調 LLM 進行語序重排、屈折生成與後編輯]
                      │
                      ▼
               [最終華語譯文]
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 1. 實驗設定與資料來源（§3.3–§3.5, p. 5）
* **語料來源**：教育部《東排灣語學習手冊》、《排灣語參考語法》、原住民族語言九階教材會話篇，以及《排灣語聖經》（Kai nua Cemas a Pinayuanan）。
* **測試集**：自教育部排灣語教材中隨機抽樣 **250 句**，覆蓋多樣句法結構與對話情境。
* **評估模型**：GPT-4o mini、Llama 3.1-70B、Gemma 3-27B、DeepSeek-R1-Distill-Llama-70B。
* **語義相似度度量**：使用普林斯頓大學 `sup-SimCSE-bert-base-uncased` 提取句子 $L_2$ 正規化 CLS 向量計算內積。

### 2. 定量增益幅度（§4, pp. 6–7，圖 4–6）
* **語義相似度（Cosine Similarity，圖 4）**：
  * 未增強基線 LLM：0.210 至 0.236
  * 本文混合系統：**0.810 至 0.846**（絕對提升約 **+0.60**）。
* **BLEU 分數（%，圖 5）**：
  * 未增強基線 LLM：1.7 至 4.4
  * 本文混合系統：**40.8 至 51.9**（絕對躍升約 **+40 至 +50** BLEU）。
* **ROUGE-L F1（圖 6）**：
  * 未增強基線 LLM：0.135 至 0.177
  * 本文混合系統：**0.548 至 0.632**（絕對提升約 **+0.45**）。

### 3. 原文分析與局限（§4–§5, pp. 7–8）
* **詞典覆蓋率決定成敗**：原文指出系統高度依賴詞典覆蓋率；一旦專有名詞或複合詞未收錄且向量庫缺乏相近例句，譯文會出現局部語義偏離。
* **句型表現差異**：系統在陳述句上表現最穩健；在倒裝句（Inverted constructions）與具有複雜語法相依性的文化從屬子句中，流暢度與準確度相對較低，需要更細緻的語義剖析引導。
* **評估範圍（Wiki 註記）**：結果只以三項自動指標衡量，且以四個模型之範圍呈現；§3.1 提到統計顯著性檢定，但正文未報告檢定結果。測試句與辭典、例句庫同樣取自教育部排灣語教材，原文未說明測試句是否排除於辭典與向量資料庫之外（§3.3, §3.5, p. 5）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
本篇發表於 2026 年，本頁尚未收錄附出處之後續研究。以下為原文之結論、資料取得、限制與未來方向：

* **作者結論**：作者認為把辭典嵌入有檢索支援、甚至小規模的大模型流程，是低資源翻譯有效率且有效的策略；辭典－檢索－大模型流程對低資源翻譯「深具潛力」，持續擴充辭典與改進架構，可望適用於更多瀕危語言（§4, p. 7；§5, p. 7）。原文未報告各模組之使用比例。
* **資料與程式**：研究資料可向通訊作者申請，因隱私限制不公開；原文未提及公開程式碼（Data Availability Statement, p. 8）。
* **作者明列之限制**（§5, p. 7）：系統高度依賴辭典覆蓋率，缺少單詞或多詞條目時譯文品質下降、出現語意偏離；目前在陳述句表現最好，倒裝句與牽涉複雜語法相依之文化語句準確度與流暢度較低。
* **作者所述之未來方向**（§5, p. 7）：擴充與修訂辭典，特別是專有名詞與高頻詞、句搭配；加入更細的語意剖析與語境機制，如更細緻的提示設計與明確的語法提示；與排灣語母語者合作並建立更完整的人工評估架構。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **將海大「構詞解析器」作為第一模組的前置增強**：
   * Wang 等人的詞典匹配目前基於表面詞形（Surface Word）。在排灣語與泛泰雅語群中，詞根常因附加焦點前後綴、中綴或重疊而改變字串形式，導致表面詞無法命中字典雜湊表。
   * **啟發**：若將海大實驗室戴晟哲、楊鈞凱、吳維中的構詞解析器串接在模組一之前，先將黏著表面詞切分為「深層詞根 + 焦點標記」，再以詞根查詢雜湊表，可望提高辭典命中率、減輕後續向量檢索的負擔（Wiki 推測；原文未報告辭典命中率，也未做此實驗）。
2. **先查辭典、查不到再檢索**：
   * 原文指出，系統為排灣語專有名詞與多詞語提供穩定的對應，使大模型能保住核心語意（§4, p. 7）；但原文並未比較「先查辭典再檢索」與「全句檢索」兩種做法。在南島語系統中，針對專有名詞、親屬稱謂與基礎名詞，直接採用辭典譯名可能比全句語意檢索更可靠（Wiki 推測）。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Wang, R.-C., Yang, C.-K., Yang, T.-C., & Tseng, Y.-X. (2026). Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation. *Engineering Proceedings*, 120(1), 52:1-52:9. DOI: [10.3390/engproc2025120052](https://doi.org/10.3390/engproc2025120052)
  * 原始檔典藏：`raw/my-focus/英文論文/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-hybrid-dictionary-rag-llm-paiwan-wang.md](../evidence/2026-hybrid-dictionary-rag-llm-paiwan-wang.md)
