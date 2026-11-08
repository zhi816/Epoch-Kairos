---
title: "FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family"
title_zh: "FormosanMT：臺灣南島語言家族多語言平行語料庫"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Hunter Scheppat, Joshua Hartshorne, Sema Koc, Éric le Ferrand, Emily Prud'hommeaux"
venue: "Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026), 3445-3455"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
my_focus: true
focus_role: "international"
focus_languages: ["臺灣南島諸語"]
doi_url: "https://doi.org/10.18653/v1/2026.lrec-1.273"
hook: "波士頓學院團隊於 LREC 2026 推出首個涵蓋全臺 15 種南島語之標準化雙語平行語料庫 FormosanMT，並開源繁體中文相容之 NLLB-200 預訓練微調基線。"
---

# FormosanMT：臺灣南島語言家族多語言平行語料庫 (FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family)

> 「在數位語言學的版圖中，一個標準化、高純度的平行語料庫是所有演算法起飛的跑道。FormosanMT 將分散在歷史角落的十五種臺灣南島語言編織成一張通往世界機器翻譯主流舞台的統一經緯網。」

**2026 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
長期以來，國際機器翻譯主流社群之所以甚少涉及臺灣南島語言，最大癥結在於缺乏符合現代深度學習標準格式（MT-Ready）的開源多語言平行資料集。波士頓學院（Boston College）與紐約州立大學水牛城分校的計算語言學團隊於第 15 屆國際語言資源與評測大會（LREC 2026）發布了具有里程碑意義的成果——**FormosanMT**。這是全球首個涵蓋臺灣 15 種官方南島語言、同時支援繁體中文（Mandarin）與英語（English）雙語對齊的標準化多語言平行語料庫，並同步釋出了相容於 Meta NLLB-200 的繁體中文分詞模組與全部 15 種語言的神經翻譯基準。

---

## Card 2 ｜ 世紀瓶頸：語料格式碎片化與多語言大模型的分詞排斥 (The Dilemma)
在構建臺灣南島語機器翻譯管線時，國際研究者普遍遭遇兩大工程瓶頸：

* **原始文獻的格式孤島與雜訊重重**：各類線上辭典、宗教文獻、田野採集筆記在格式、拼寫標點、檔案編碼上互不相容，缺乏統一的清洗、拼寫正規化與過濾流程，直接訓練模型會引發大量的對齊錯誤。
* **NLLB-200 等國際大模型對繁體中文分詞的不相容**：Meta 開源的著名多語言翻譯模型 NLLB-200 在繁體中文（`zho_Hant`）上的預設分詞器存在缺陷，在處理臺灣特有字彙與語句時經常出現詞界切分錯亂，嚴重阻礙了模型向臺灣本土少數族語的遷移微調。

---

## Card 3 ｜ 突破架構與原理：MT-Ready 清洗管線與 NLLB 繁中分詞調適 (The Secret)

### 1. FormosanMT 數據工程與多語言語素對齊

Scheppat 等人建立了一套自動化提取、拼寫音標正規化與語意過濾管線：

$$\mathcal{D}_{\text{clean}} = \Big\{ (x_i, y_i) \in \mathcal{D}_{\text{raw}} \;\Big|\; \operatorname{Len}(x_i) \le L_{\max}, \; \operatorname{LangID}(x_i) = l, \; \operatorname{AlignScore}(x_i, y_i) \ge \tau \Big\}$$

覆蓋 15 種臺灣南島語言 $\mathcal{L}_{15} = \{ \text{ami}, \text{tay}, \text{pai}, \text{bun}, \text{puy}, \text{ruk}, \text{cou}, \text{sai}, \text{tao}, \text{tsu}, \text{kan}, \text{xnb}, \text{ssf}, \text{sed}, \text{trv} \}$。

### 2. NLLB-200 跨語言微調目標函數

採用預訓練 NLLB-200 作為骨幹，針對 15 種南島語進行多語言聯合微調：

$$\mathcal{L}_{\text{NLLB}}(\theta) = -\sum_{l \in \mathcal{L}_{15}} \sum_{(x, y) \in \mathcal{D}_l} \sum_{t=1}^{|y|} \log P_{\text{NLLB}}\Big( y_t \mid y_{<t}, x, \tau_{\text{tgt}}; \theta \Big) + \lambda \Omega_{\text{adapt}}(\theta)$$

其中：
* $\tau_{\text{tgt}} \in \{ \langle \text{zho\_Hant} \rangle, \langle \text{eng\_Latn} \rangle \}$ 為目標語言引導標記；
* $\Omega_{\text{adapt}}(\theta)$ 為正則化項，防止預訓練編碼器在高層注意力特徵空間發生表徵崩潰。

```text
[15 種臺灣南島語原始來源庫] ──► [清洗/正規化/語義過濾] ──► [FormosanMT 標準平行庫]
                                                                     │
       ┌─────────────────────────────────────────────────────────────┘
       ▼
[NLLB 繁中相容分詞器] ──► [NLLB-200 多語言聯合微調] ──► [15 種南島語 ↔ 中/英 基準模型]
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的平行語料與基準
* FormosanMT 收錄臺灣 **15 種**原住民族語言。經過篩選與切分後，語料共 **493,519 句對**：族語－華語 **397,710** 句對，族語－英語 **95,809** 句對。
* 論文提供 NLLB-200 與 OpenNMT 的雙向翻譯基準，並另提供適用 NLLB 的繁體中文 tokenizer 與訓練工具。原文分別按語言與翻譯方向列分數，此處不把方向各異的分數合併成平均增益。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **鋪平臺灣南島語進入全球現代 NLP 主流的數位跑道**：徹底解決了國際頂尖團隊無法取得標準化臺灣南島語資料的歷史痛點，使全球 AI 模型（如 Meta NLLB、Google Translate）能夠無縫整合臺灣南島語。
* **開源完整生態系代碼與預訓練權重**：為學術界提供了開箱即用的資料清洗腳本、Tokenizer 與評測 Baseline。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
FormosanMT 是近年南島語 NLP 領域最重量級的開源基礎設施，為我的碩士論文研究提供了現成的高性能底座：

1. **直接採用 FormosanMT 作為預訓練與微調的核心語料庫**：
   * 我的模型不再局限於少數單一資料夾，而是可以直接以 FormosanMT 提供的 30 萬高品質句對作為基礎底座，快速微調各類神經翻譯網路。
2. **與構詞解析器（Morphological Analyzer）的完美聯動**：
   * FormosanMT 雖然規模大，但其文本依然是表層形式；若將海大實驗室的深層構詞解析器應用於 FormosanMT 全語料，將產出全球第一套「標註深層詞根與焦點語素」的超高階臺灣南島語語法平行語料庫，直接將研究成果推向頂會高度。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Scheppat, H., Hartshorne, J., Koc, S., le Ferrand, É., & Prud'hommeaux, E. (2026). FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family. In *Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)* (pp. 3445-3455). DOI: [10.18653/v1/2026.lrec-1.273](https://doi.org/10.18653/v1/2026.lrec-1.273)
  * 原始檔典藏：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
