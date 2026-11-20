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
status: "published"
verification: "partial"
my_focus: true
focus_role: "llm-assisted"
focus_direction: "llm-rag"
focus_languages: ["德頓語", "比斯拉馬語"]
doi_url: "https://doi.org/10.18653/v1/2025.acl-demo.13"
hook: "墨爾本大學團隊於 ACL 2025 發表開源低資源翻譯系統 TULUN：結合特化 NMT 初譯、spaCy 詞彙表與 Tantivy BM25 翻譯記憶庫檢索，交由 Gemini 2.0 Flash 進行術語感知 CoT 後編輯，不需微調模型；在德頓語醫療與比斯拉馬語救災翻譯上比基線 MT 高 16.90 至 22.41 ChrF++，在 FLORES 六種低資源語言上平均比 NLLB-54B 高 2.8 ChrF++。"
card_line: "讓大模型參考詞彙表與舊譯文，修潤譯稿"
---

# TULUN：透明且可自適應之低資源機器翻譯系統 (TULUN: Transparent and Adaptable Low-resource Machine Translation)

**2025 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Merx, Suominen, Hong, Thieberger, Cohn & Vylomova（墨爾本大學、澳洲國立大學與東帝汶 Maluk Timor 醫療非營利組織），*ACL 2025 System Demonstrations*, pp. 129–139。實施系統與評估聚焦於東帝汶德頓語（Tetun）、萬那杜比斯拉馬語（Bislama）及 FLORES-200 六大低資源語言。

---

## Card 1 ｜ 一句話看懂
這篇做了一套開源翻譯平台 TULUN：專用翻譯模型先出初稿，再由大型語言模型參考使用者上傳的詞彙表與過去的譯文（翻譯記憶）修正，不必重新訓練模型（§1, p. 130；§3.1, p. 131）。在德頓語醫療與比斯拉馬語救災兩個真實任務上，ChrF++ 平均提升 16.90 至 22.41 分；在 FLORES-200 六種低資源語言上，平均比 NLLB-54B 高 2.83 分（表 1, p. 133；表 2, p. 134）。

* **語言**：英語 → 德頓語（東帝汶）、比斯拉馬語（萬那杜），以及 FLORES-200 六種低資源語言
* **任務**：術語感知的低資源機器翻譯系統（系統展示論文）
* **方法**：神經機器翻譯初譯 ＋ 檢索詞彙表與翻譯記憶 ＋ 大型語言模型後編輯（§3）
* **資料**：合作組織提供之醫療與救災詞彙表、翻譯記憶；FLORES-200 devtest（§4）
* **公開**：程式碼以 MIT 授權公開於 GitHub `raphaelmerx/tulun`，另有線上系統與展示影片（p. 130 註 2；摘要）
* **出處**：Merx、Suominen、Hong、Thieberger、Cohn、Vylomova（墨爾本大學、澳洲國立大學、東帝汶 Maluk Timor），*ACL 2025 System Demonstrations*, pp. 129–139

---

## Card 2 ｜ 要解決的問題
低資源語言的實際使用者（非營利組織、醫療機構、原住民社群）常需要翻譯專業術語；商用翻譯服務很少支援低資源語言，更少提供術語自訂（§1, pp. 129–130）。

* **微調門檻高**：把術語約束加入神經翻譯模型的既有方法（在來源句替換或前置詞典條目）多半需要專用模型或微調，對小型組織耗費資源，也可能造成災難性遺忘（§2, p. 130）；德頓語的醫療組織雖有詞彙表與過去的譯文，卻無法用來改善機器翻譯（§1, p. 129）。
* **術語譯錯**：專用翻譯模型會譯錯領域術語，例如介面示例中翻譯模型把「potable」譯錯（Figure 2；§3.1, p. 131），在領域外推論時也常產生幻覺（§4.1.1, p. 133）。
* **大模型不準**：大型語言模型翻譯成低資源語言或特定領域時，準確度可能不如專用翻譯模型（§1–§2, p. 130）。

這篇的想法：讓翻譯模型先譯，再由大模型依使用者的詞彙表修正。作者稱就其所知，TULUN 是唯一支援德頓語、比斯拉馬語等低資源語言的開源術語感知翻譯工具（§2, p. 131）；Tulun 在德頓語意為「協助」，取其輔助而非取代人類專業之意（p. 129 註 1）。

---

## Card 3 ｜ 方法流程
原文為系統展示論文，全文無編號公式，處理流程只以文字與 Figure 1 說明（§3.1–§3.2, pp. 131–132）。白話步驟：

1. **翻譯模型初譯**：用 MADLAD-400、OPUS-MT、NLLB 或 Google 翻譯產生初稿。
2. **查詞彙表**：把來源句切詞，找出詞彙表中出現的單詞與雙詞片語。
3. **找舊譯文**：用 BM25 從翻譯記憶取回最相似的過去句對。
4. **大模型後編輯**：把來源句、初稿、詞彙表條目與舊譯文放進提示，由大型語言模型修正，介面標出改動處。

細節如下：

### 1. 系統模組與後端架構（§3.2, p. 132）
* **後端實作**：以可設定的 Django 專案實作，並以 Docker 與 Docker Compose 封裝，方便各組織在自己的設備上部署。
* **初譯引擎（MT Backbone）**：支援 Google Translate（Cloud Translation API）與 Hugging Face 之 translation pipeline。評估時，德頓語與比斯拉馬語以 `MADLAD-400-10B` 為基線，並另評 `OPUS-MT`（MADLAD 在比斯拉馬語常照抄英文原句）；FLORES 評估以 `NLLB-54B` 為基線（§4.1.1, p. 132；§4.2, p. 133）。
* **後編輯引擎（LLM Post-Editor）**：透過 `LiteLLM` 支援數百種模型供應商，評估使用 `Gemini 2.0 Flash`。

### 2. 動態檢索管線具體實作（§3.2, p. 132）
* **詞彙表動態檢索（Glossary Retrieval）**：
  * 使用 spaCy 的 `en_core_web_sm` 模型對輸入來源句進行分詞。
  * 提取輸入詞元的 `{1,2}`-gram（單詞與雙詞片語），與使用者上傳之術語詞典進行重疊匹配，精確召回對應術語定義。
* **翻譯記憶庫檢索（Translation Memory, TM Retrieval）**：
  * 採用 Rust 撰寫之高效搜尋引擎函式庫 **`Tantivy`**。
  * 對輸入來源句與翻譯記憶庫的來源端執行 **Top-$N$ BM25 檢索**（$N$ 可在管理介面設定），取回最相似之過去句對；選用 BM25 是因其在以上下文學習檢索翻譯記憶上表現良好（§3.2, p. 132）。
* **Prompt 結構與思維鏈推理**：
  * 把檢索到的詞彙表條目與翻譯記憶注入 LLM 的提示，指引後編輯；第 4 節的評估一律使用含少樣本示例與思維鏈推理的系統提示，提示可在管理介面手動調整（§3.2, p. 132；提示範例見附錄 A）。
  * 流程依序為：來源句 → NMT 初譯 → 檢索詞彙表條目與翻譯記憶 → LLM 依來源句、初譯與檢索結果後編輯 → 最終譯文（Figure 1）。介面會以紅色標出初譯被改動處、以綠色標出最終譯文之改動，並列出所用的詞彙表條目與相似句（§3.1, p. 131）。

```text
[輸入來源句 x] ─────────────────────────────────────────────────────────────┐
       │                                                                     │
       ├─► [特化 NMT 初譯 (MADLAD/OPUS/NLLB)] ──► 初譯草稿 y_base ───────────┼─► [Gemini 2.0 Flash 後編輯]
       │                                                                     │            │
       ├─► [spaCy en_core_web_sm {1,2}-gram 匹配] ──► 命中專業術語詞彙 ───────┤            ▼
       │                                                                     │   [後編輯譯文 y_final]
       └─► [Tantivy Top-N BM25 檢索] ───────────────► 相關翻譯記憶 (TM) ─────┘
```

---

## Card 4 ｜ 資料與實驗
* **德頓語醫療**：Maluk Timor 提供醫療詞彙表 2,698 條、翻譯記憶 1,018 句，其中保留 451 句作評估（§4.1.1, pp. 132–133）。
* **比斯拉馬語救災**：Pacific Creoles 合作方提供字典 5,769 條、翻譯記憶 3,353 段，其中保留 841 段作評估。兩個資料集屬於各合作組織，研究用途可依資料共享協議申請（§4.1.1, p. 132）。
* **FLORES-200**：六種低資源語言，devtest 全部 1,012 句；以 GATITOS 詞彙表與 allenai/nllb 平行句作翻譯記憶（§4.2, p. 133）。
* **比較方式**：只用翻譯模型、只用大型語言模型（0-shot、10-shot）與 TULUN（翻譯模型＋大模型後編輯）（表 1–2）。
* **評分方式**：ChrF++（字元層級重疊），表中未列 BLEU；另以系統可用性量表（SUS）與技術接受模型（TAM）問卷調查兩位使用者（§4.1.2）。

---

## Card 5 ｜ 結果
### 1. 真實世界領域任務評估（§4.1.1, pp. 132–133；表 1, p. 133）
* **德頓語醫療翻譯（Tetun, TDT）**：
  * Maluk Timor 提供醫療詞彙表 2,698 條、翻譯記憶 1,018 句；其中保留 451 句作評估。
  * 表 1 的 ChrF++：MADLAD-400-10B 基線 35.78，TULUN 47.87（+12.09）；OPUS-MT 基線 16.01，TULUN 34.27（+18.26）。
* **比斯拉馬語救災翻譯（Bislama, BIS）**：
  * Pacific Creoles 合作方提供字典 5,769 條、翻譯記憶 3,353 段；其中保留 841 段作評估。
  * 表 1 的 ChrF++：MADLAD-400-10B 基線 15.22，TULUN 47.94（+32.72）；OPUS-MT 基線 32.60，TULUN 48.14（+15.54）。
* **跨語言平均增益**：表 1 報告相對 MADLAD 的平均增益為 +22.41 ChrF++，相對 OPUS-MT 為 +16.90 ChrF++；這兩個數字是各自基線下跨 TDT、BIS 的平均增益，不是單一語言的增益。作為對照，只用 LLM 的 Gemini 10-shot 平均為 44.98（TDT 44.59、BIS 45.37），0-shot 為 39.63（表 1）。
* **指標範圍**：表 1 僅報告 ChrF++，未列 BLEU 分數。兩個資料集屬於各合作組織，研究用途可依資料共享協議申請（§4.1.1, p. 132）。

### 2. 系統易用性與接受度（§4.1.2, p. 133）
* **系統可用性量表（SUS）**：只收集兩份回應（Maluk Timor 臨床主任與一位比斯拉馬語語言學家），平均 **81.25 分**，屬「excellent」之可用性（Bangor et al. 2008）。依倫理聲明，兩位參與者為本篇共同作者（p. 135）。
* **技術接受模型（TAM）**：各題平均 4 至 5 分（滿分 5），「整體有用性」**5/5**，「提升翻譯品質」與「協助翻譯專業技術內容」均為 **4.5/5**。

### 3. FLORES-200 跨洲六大低資源語言通用評估（§4.2, pp. 133–134；表 2, p. 134）
使用 GATITOS 詞彙表與 allenai/nllb 平行句（依 NLLB 資料探勘策略）作為翻譯記憶，在 FLORES-200 devtest 全部 1,012 句上，以 NLLB-54B 為 MT 基線、Gemini 2.0 Flash 10-shot 為 LLM 基線。TULUN 平均比兩者分別高 2.83 與 2.15 ChrF++（摘要寫作 2.8）；作者觀察到 Gemini 常勝過 NLLB-54B，而 TULUN 多能在兩者較高者之上再提升（§4.2, p. 134）：

| 語言 | 代碼 | NLLB-54B (基線) | Gemini 2.0 (10-shot) | TULUN (NLLB + Gemini APE) | 淨提升 ($\Delta$) |
|---|---|---|---|---|---|
| 托克皮辛語 (Tok Pisin) | TPI | 41.61 | 44.07 | **46.80** | **+5.19** |
| 宗喀語 (Dzongkha) | DZO | 34.67 | 30.74 | **35.76** | **+1.09** |
| 克丘亞語 (Quechua) | QUY | 26.87 | 31.28 | **32.40** | **+5.53** |
| 基隆迪語 (Rundi) | RUN | **42.51** | 39.83 | 41.17 | -1.34* |
| 林加拉語 (Lingala) | LIN | 47.99 | 49.42 | **50.58** | **+2.59** |
| 阿薩姆語 (Assamese) | ASM | 35.91 | 38.29 | **39.80** | **+3.89** |
| **全體平均 (Average)** | | 38.26 | 38.94 | **41.09** | **+2.83** |

*\*註：基隆迪語（RUN）下降 1.34 分；作者以質性分析並以不在提示中注入詞彙表重新評估（結果比 NLLB 高 0.25 分），判定是 LLM 依詞彙表做了錯誤的改字，顯示需要調整提示與詞彙表（§5, p. 134；附錄 C）。*

---

## Card 6 ｜ 限制與可用性
* **作者說的限制**（§5, p. 134；倫理聲明, p. 135）：後編輯對準確度之影響因語言而異，基隆迪語反而下降 1.34 分；高度可設定也表示使用者需要了解翻譯模型與大型語言模型的選項；透明度仰賴大型語言模型能善用詞彙表與翻譯記憶，對構詞複雜或文字罕見、模型幾乎沒見過的極低資源語言，此假設可能不成立而產生更多幻覺；易用性研究只有兩位參與者，且皆為共同作者。
* **讀的時候要留意**：真實任務的平均增益（+22.41、+16.90）是各自基線下兩種語言的平均，不是單一語言的增益；FLORES 實驗是以 NLLB-54B 本身作為初譯模型，原文並未以小型翻譯模型與 54B 模型比較（表 2）。作者認為 TULUN 讓使用者能以自己的專業持續改進翻譯過程（§1；§6），此為作者觀點，非實驗結果。
* **公開程度**：程式碼以 MIT 授權公開於 GitHub `raphaelmerx/tulun`（p. 130 註 2）；線上系統 bislama-trans.rapha.dev 與展示影片（摘要；§1, p. 130）。德頓語與比斯拉馬語之評估資料屬合作組織，研究用途需依資料共享協議申請（§4.1.1, p. 132）。
* **作者的下一步**（§5, p. 134；§6, pp. 134–135）：以 DSPy 的 MIPRO 等方法系統化最佳化提示並調整少樣本示例；探索可在本機執行、專為後編輯微調的小型大型語言模型，以支援離線部署；擴大不同語言社群使用者之易用性研究；評估 DeepSeek-R1 等其他模型；提供智慧預設與提示調整模組。
* **適合拿來報告的點**：「翻譯模型初譯＋檢索詞彙表與舊譯文＋大模型後編輯」的完整系統，程式開源、可直接部署，適合拿來說明低資源翻譯如何落地到真實組織（Wiki 詮釋）。

### 延伸想法
以下為延伸思考（Wiki 推測），不是原文主張。

1. **臺灣南島語醫療與長照翻譯**：偏鄉原住民長者就醫或長照時，常遇到醫學術語的溝通困難。參考 TULUN 與東帝汶醫療組織的合作，可考慮建立包含臺灣南島語醫療詞彙（病症、藥物用法、器官名詞）的術語庫，結合族語翻譯模型與後編輯；效果需實驗驗證。
2. **族語教師的協同審校**：可參考 TULUN 的介面：顯示翻譯初稿與後編輯的修改痕跡，並讓審校後的句對直接存入翻譯記憶，作為之後翻譯的參考例句。
3. **詞彙雜訊控制**：基隆迪語的例子顯示，未經校驗的詞彙表可能讓大模型改錯字。在南島語系統中，同音異義詞或詞綴變化複雜的詞根，可能需要標註詞性與使用範疇，避免模型盲目替換。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Merx, R., Suominen, H., Hong, L., Thieberger, N., Cohn, T., & Vylomova, E. (2025). TULUN: Transparent and Adaptable Low-resource Machine Translation. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)* (pp. 129-139). DOI: [10.18653/v1/2025.acl-demo.13](https://doi.org/10.18653/v1/2025.acl-demo.13)
  * 開源專案儲存庫：[github.com/raphaelmerx/tulun](https://github.com/raphaelmerx/tulun)（MIT 授權）
  * 線上展示與系統影片：[bislama-trans.rapha.dev](https://bislama-trans.rapha.dev)；展示影片: [youtu.be/fQFwOxzR4MI](https://youtu.be/fQFwOxzR4MI)
  * 原始檔典藏：`raw/my-focus/大模型輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2025-tulun-adaptable-lrl-mt-merx.md](../evidence/2025-tulun-adaptable-lrl-mt-merx.md)
