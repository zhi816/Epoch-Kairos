---
title: "TULUN: Transparent and Adaptable Low-resource Machine Translation"
title_zh: "TULUN：透明且可自適應之低資源機器翻譯系統"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Raphaël Merx, Hanna Suominen, Lois Hong, Nick Thieberger, Trevor Cohn, Ekaterina Vylomova"
venue: "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), 129-139"
domain: "ai"
domain_tags: ["#自然語言處理", "#人工智慧", "#計算語言學"]
concepts: ["low-resource-machine-translation"]
status: "wiki"
verification: "verified"
my_focus: true
focus_role: "llm-assisted"
focus_languages: ["德頓語", "比斯拉馬語"]
doi_url: "https://doi.org/10.18653/v1/2025.acl-demo.13"
hook: "墨爾本大學團隊於 ACL 2025 發表開源低資源翻譯系統 TULUN：結合特化 NMT 初譯、spaCy 詞彙表與 Tantivy BM25 翻譯記憶庫檢索，交由 Gemini 2.0 Flash 進行術語感知 CoT 後編輯，在德頓語醫療與比斯拉馬語救災翻譯上取得 +16.90 至 +22.41 chrF++ 巨幅提升。"
card_line: "讓大模型參考詞彙表與舊譯文，修潤譯稿"
---

# TULUN：透明且可自適應之低資源機器翻譯系統 (TULUN: Transparent and Adaptable Low-resource Machine Translation)

> 「在極低資源與專業領域的交會處，等待數萬句資料去微調一個龐大模型是不切實際的奢望。將特化小型翻譯模型的語法敏捷性與大語言模型對術語詞彙的長語境駕馭力結合，是在現實世界中拯救瀕危語言服務的最短路徑。」（本頁引言為 Wiki 撰寫，非原文）

**2025 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Merx, Suominen, Hong, Thieberger, Cohn & Vylomova（墨爾本大學、澳洲國立大學與東帝汶 Maluk Timor 醫療非營利組織），*ACL 2025 System Demonstrations*, pp. 129–139。實施系統與評估聚焦於東帝汶德頓語（Tetun）、萬那杜比斯拉馬語（Bislama）及 FLORES-200 六大低資源語言。

---

## Card 1 ｜ 時代銘文 (The Hook)
在低資源語言（LRL）的真實應用場景中，非營利組織、醫療機構與原住民社群往往面臨特定領域（如急診醫療、災難救濟）專業術語翻譯嚴重失真的致命挑戰。傳統領域自適應（Domain Adaptation）必須依賴專業工程師進行模型重新微調（Fine-tuning），不僅算力與數據門檻高昂，且迭代週期動輒數月，根本無法應對前線緊急需求（§1, pp. 129–130）。

墨爾本大學 Trevor Cohn 團隊與東帝汶非營利醫療組織 Maluk Timor 合作，於 ACL 2025 系統展示（System Demonstrations）發表開源翻譯平台 **TULUN**（德頓語意為「援助／Assistance」）。該系統首創「特化神經翻譯（NMT）生成初稿 $\to$ 詞彙表與翻譯記憶庫動態檢索 $\to$ 大語言模型（LLM）術語感知後編輯」的模組化架構，讓使用者無需編寫代碼或重新訓練模型，只需在 Web 介面即時維護術語表與雙語句庫，即可實現即時領域自適應。

---

## Card 2 ｜ 世紀瓶頸：微調門檻與術語漂移的雙重困境 (The Dilemma)
在極端低資源專業翻譯任務中，傳統技術體系面臨難以調和的結構矛盾（§1–§2, pp. 129–130）：

* **模型微調的高門檻隔絕社群參與**：部落長老或前線醫護每發現一個新術語翻譯錯誤，若必須等待演算法工程師重新微調神經網路，系統的迭代週期過於漫長；且小型在地非營利機構根本不具備機器學習訓練資源。
* **通用大模型與純 NMT 模型的雙向缺陷**：純神經翻譯模型（如 NLLB、MADLAD）在未見過的特定領域術語上頻繁生成音近錯字、漏譯或幻覺（例如將 potable water 錯譯為非飲用水）；而通用大模型在未經引導時對極低資源語言底層語法掌握脆弱，常輸出文法崩潰的句子。

---

## Card 3 ｜ 突破架構與原理：模組化系統設計與檢索管線 (The Secret)

原文為系統展示與實證架構論文，全文無理論優化公式；Card 3 之數學式為流程示意表示（§3.1–§3.2, pp. 130–132）：

### 1. 系統模組與後端架構（§3.2, p. 132）
* **後端實作**：以 Python Django 框架開發，採用 Docker 與 Docker Compose 容器化封裝，提供極簡的本機與伺服器部屬流程。
* **初譯引擎（MT Backbone）**：支援 Google Translate API 以及 Hugging Face Translation Pipeline，實測評估使用開源特化翻譯模型（如針對德頓語的 `MADLAD-400-10B`、針對比斯拉馬語的 `OPUS-MT`，以及 `NLLB-54B`）。
* **後編輯引擎（LLM Post-Editor）**：透過 `LiteLLM` 代理支援數百種商用與開源大模型，實測使用 `Gemini 2.0 Flash`。

### 2. 動態檢索管線具體實作（§3.2, p. 132）
* **詞彙表動態檢索（Glossary Retrieval）**：
  * 使用 spaCy 的 `en_core_web_sm` 模型對輸入來源句進行分詞。
  * 提取輸入詞元的 `{1,2}`-gram（單詞與雙詞片語），與使用者上傳之術語詞典進行重疊匹配，精確召回對應術語定義。
* **翻譯記憶庫檢索（Translation Memory, TM Retrieval）**：
  * 採用 Rust 撰寫之高效搜尋引擎函式庫 **`Tantivy`**。
  * 對輸入來源句與翻譯記憶庫的來源端執行 **Top-$N$ BM25 檢索**（$N$ 可在管理介面自訂，論文評估中預設為 5 句），檢索最相似之歷史平行句對。
* **Prompt 結構與思維鏈推理**：
  * 將來源句、NMT 初譯草稿、召回之詞彙條目與 Top-$N$ 翻譯記憶注入 Prompt，透過包含思維鏈（Chain-of-Thought, CoT）的 Few-Shot 提示引導 LLM 比對初稿並執行術語約束修正：
    $$\hat{y}_{\text{base}} = \operatorname{NMT}(x)$$
    $$\hat{y}_{\text{final}} = \operatorname{LLM}_{\text{CoT}}\Big( x, \, \hat{y}_{\text{base}}, \, \operatorname{Glossary}_{\{1,2\}\text{-gram}}(x), \, \operatorname{TM}_{\text{BM25}}(x) \Big)$$

```text
[輸入來源句 x] ─────────────────────────────────────────────────────────────┐
       │                                                                     │
       ├─► [特化 NMT 初譯 (MADLAD/OPUS/NLLB)] ──► 初譯草稿 y_base ───────────┼─► [Gemini 2.0 Flash 後編輯]
       │                                                                     │            │
       ├─► [spaCy en_core_web_sm {1,2}-gram 匹配] ──► 命中專業術語詞彙 ───────┤            ▼
       │                                                                     │   [高精度修復譯文 y_final]
       └─► [Tantivy Top-N BM25 檢索] ───────────────► 相關翻譯記憶 (TM) ─────┘
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 1. 真實世界領域任務評估（§4.1.1, pp. 132–133；表 1, p. 133）
* **德頓語醫療翻譯（Tetun, TDT）**：
  * Maluk Timor 提供醫療詞彙表 2,698 條、翻譯記憶 1,018 句；其中保留 451 句作評估。
  * 表 1 的 ChrF++：MADLAD-400-10B 基線 35.78，TULUN 47.87（+12.09）；OPUS-MT 基線 16.01，TULUN 34.27（+18.26）。
* **比斯拉馬語救災翻譯（Bislama, BIS）**：
  * Pacific Creoles 合作方提供字典 5,769 條、翻譯記憶 3,353 段；其中保留 841 段作評估。
  * 表 1 的 ChrF++：MADLAD-400-10B 基線 15.22，TULUN 47.94（+32.72）；OPUS-MT 基線 32.60，TULUN 48.14（+15.54）。
* **跨語言平均增益**：表 1 報告相對 MADLAD 的平均增益為 +22.41 ChrF++，相對 OPUS-MT 為 +16.90 ChrF++；這兩個數字是各自基線下跨 TDT、BIS 的平均增益，不是單一語言的增益。
* **指標範圍**：表 1 僅報告 ChrF++，未列 BLEU 分數。

### 2. 系統易用性與接受度（§4.1.2, p. 134）
* **系統可用性量表（SUS）**：平均得分 **81.25 分**（對應 Grade A 優異等級）。
* **技術接受模型（TAM）**：臨床主任與語言學家在「整體有用性」評分給予滿分 **5/5**，「提升翻譯品質」與「協助翻譯專業技術內容」均給予 **4.5/5**。

### 3. FLORES-200 跨洲六大低資源語言通用評估（§4.2, 表 2, p. 134）
使用 GATITOS 詞彙表與 NLLB 訓練句庫，在 FLORES-200 devtest（1,012 句）上對比 NLLB-54B 基線與 Gemini 10-shot：

| 語言 | 代碼 | NLLB-54B (基線) | Gemini 2.0 (10-shot) | TULUN (NLLB + Gemini APE) | 淨提升 ($\Delta$) |
|---|---|---|---|---|---|
| 托克皮辛語 (Tok Pisin) | TPI | 41.61 | 44.07 | **46.80** | **+5.19** |
| 宗喀語 (Dzongkha) | DZO | 34.67 | 30.74 | **35.76** | **+1.09** |
| 克丘亞語 (Quechua) | QUY | 26.87 | 31.28 | **32.40** | **+5.53** |
| 基隆迪語 (Rundi) | RUN | **42.51** | 39.83 | 41.17 | -1.34* |
| 林加拉語 (Lingala) | LIN | 47.99 | 49.42 | **50.58** | **+2.59** |
| 阿薩姆語 (Assamese) | ASM | 35.91 | 38.29 | **39.80** | **+3.89** |
| **全體平均 (Average)** | | 38.26 | 38.94 | **41.09** | **+2.83** |

*\*註：基隆迪語（RUN）因詞彙表部分條目引入噪音導致略降 -1.34，若在 Prompt 中剔除詞彙表、僅保留 TM，分數即回升至 42.76（超越 NLLB-54B）。*

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **由「黑盒被動微調」轉向「透明協同的即時自適應」**：打破了傳統 AI 模型必須重新訓練才能吸收領域新詞的壁壘，讓在地醫護人員或族語教師只需在網頁上編輯 CSV 術語表，系統推論即刻修正，實踐了真正的人機協同翻譯範式。
* **確立「小模型保語法、大模型做修訂」的性價比路徑**：證明在邊緣與非營利機構資源受限下，無須追逐昂貴的巨型模型微調，利用現成小型開源 NMT 模型搭配輕量 API RAG 後編輯即可超越 54B 巨型單體模型。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **南島語醫療與長照專用翻譯模組之構想**：
   * 偏鄉原住民長者在就醫或長照時，常遭遇文化與現代醫學術語的溝通鴻溝。TULUN 與東帝汶醫療組織的合作經驗表明：建構一個包含臺灣南島語核心醫療詞彙（如病症、藥物用法、器官名詞）的動態術語庫，結合本地微調的泛泰雅模型進行 RAG 後編輯，能快速產生高保真度的醫療衛教譯文。
2. **Web 介面與族語教師的「協同審校迴圈」**：
   * 在論文系統展示中，可參考 TULUN 的 UI 設計：在前端顯示「NMT 初譯草稿」與「後編輯修改痕跡（紅綠標註）」，並提供單鍵將更正後的句對存入翻譯記憶庫（TM）之功能，讓每次使用者審校直接轉化為後續翻譯的即時少樣本參照。
3. **詞彙雜訊控制（Rundi 的教訓）**：
   * 原文指出未經校驗的詞彙表注入可能引入負面干擾（如 Rundi 案例）。在南島語系統中，針對同音異義詞或具有複雜詞綴變化的詞根，必須建立精確的詞性與範疇標記，避免 LLM 盲目替換。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Merx, R., Suominen, H., Hong, L., Thieberger, N., Cohn, T., & Vylomova, E. (2025). TULUN: Transparent and Adaptable Low-resource Machine Translation. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)* (pp. 129-139). DOI: [10.18653/v1/2025.acl-demo.13](https://doi.org/10.18653/v1/2025.acl-demo.13)
  * 開源專案儲存庫：[github.com/raphaelmerx/tulun](https://github.com/raphaelmerx/tulun)（MIT 授權）
  * 線上展示與系統影片：[bislama-trans.rapha.dev](https://bislama-trans.rapha.dev)；展示影片: [youtu.be/fQFwOxzR4MI](https://youtu.be/fQFwOxzR4MI)
  * 原始檔典藏：`raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2025-tulun-adaptable-lrl-mt-merx.md](../evidence/2025-tulun-adaptable-lrl-mt-merx.md)
