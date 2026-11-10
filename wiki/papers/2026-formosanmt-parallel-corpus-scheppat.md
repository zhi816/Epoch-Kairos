---
title: "FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family"
title_zh: "FormosanMT：臺灣南島語言家族多語言平行語料庫"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Hunter Scheppat, Joshua K. Hartshorne, Sema Koc, Éric Le Ferrand, Emily Prud'hommeaux"
venue: "Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026), 3445-3455"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
verification: "issues"
my_focus: true
focus_role: "international"
focus_languages: ["臺灣南島諸語"]
doi_url: "https://doi.org/10.63317/3ut33xim33nt"
hook: "波士頓學院團隊於 LREC 2026 推出首個涵蓋全臺 15 種南島語之標準化平行語料庫 FormosanMT（近 50 萬句對），提出啟發式長度比與正則過濾清洗管線，開源相容繁體中文之 NLLB-200 分詞器與雙向基準模型。"
card_line: "彙整各族語與中文的對照句，建成翻譯語料庫"
---

# FormosanMT：臺灣南島語言家族多語言平行語料庫 (FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family)

> 「在數位語言學的版圖中，一個標準化、高純度的平行語料庫是所有演算法起飛的跑道。FormosanMT 將分散在歷史角落的十五種臺灣南島語言編織成一張通往世界機器翻譯主流舞台的統一經緯網。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：波士頓學院 Hunter Scheppat、Joshua K. Hartshorne 等人，*Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)*, pp. 3445–3455（ELRA 出版，DOI: [10.63317/3ut33xim33nt](https://doi.org/10.63317/3ut33xim33nt)）。以臺灣原住民族 15 種南島語言（含雅美/達悟語）與華語／英語之平行語料構建與雙向神經翻譯基準評測為核心。

---

## Card 1 ｜ 時代銘文 (The Hook)
長期以來，國際機器翻譯主流社群之所以甚少涉及臺灣南島語言，最大癥結在於缺乏符合現代深度學習標準格式（MT-Ready）的開源多語言平行資料集。波士頓學院（Boston College）、MGH 衛生職業學院與紐約州立大學水牛城分校的計算語言學團隊於第 15 屆國際語言資源與評測大會（LREC 2026）發布了具有里程碑意義的成果——**FormosanMT**。

這是全球首個完整涵蓋臺灣 15 種官方南島語言、同時支援繁體中文（Mandarin）與英語（English）雙語對齊的標準化多語言平行語料庫（總量達 **493,519 句對**，§3.4, p. 3448）。研究團隊同步開源了完整的數據抓取與啟發式清洗腳本、相容於 Meta NLLB-200 的繁體中文分詞模組，並為全數 15 個語言對釋出了 NLLB-200 與 OpenNMT 雙向翻譯基準模型（§1–§2, pp. 3445–3446）。

---

## Card 2 ｜ 世紀瓶頸：語料格式碎片化與多語言大模型的分詞排斥 (The Dilemma)
在構建臺灣南島語機器翻譯管線時，國際研究者普遍遭遇兩大工程瓶頸（§1–§3.3, pp. 3445–3448）：

* **原始文獻的格式孤島與雜訊重重**：各類線上辭典（ILRDF 詞典）、教育平台（ePark）、宗教文獻、田野採集筆記（臺大南島語語料庫 NTU Corpus）與口語字幕（ILRDF 影片）在格式、拼寫標點、檔案編碼上互不相容。尤其是田野筆記常包含語言學家的註記、疑問與說話者標籤，而口語字幕多有不連貫語氣詞與脫稿偏離，缺乏統一的清洗、拼寫正規化與長度比例過濾時，直接訓練會導致大量的錯位幻覺。
* **NLLB-200 等國際多語言大模型的分詞與微調相容障礙**：Meta 開源的著名多語言翻譯模型 NLLB-200 在繁體中文（`zho_Hant`）上的預設分詞器存在詞界切分缺陷；此外，向 NLLB-200 增添新低資源語言代碼的社群教學常依賴不穩定的版本黑客（Hacks），在面對新版 `tokenizers` 庫時極易引發崩潰，且詞表擴充後若隨機初始化語言代碼向量，會嚴重損害預訓練權重的表徵遷移。

---

## Card 3 ｜ 突破架構與原理：啟發式長度比清洗與 NLLB 繁中分詞調適 (The Secret)

### 1. FormosanMT 數據工程與啟發式過濾管線

Scheppat 等人建立了一套自動化提取、文字正規化與多層級啟發式過濾管線（§3.3, pp. 3448–3449）。過濾核心係基於正則表達式、結構性特徵與詞/字元長度比例，而非語言識別器或神經語義對齊模型：

$$
\begin{aligned}
\mathcal{D}_{\text{clean}} = \Big\{ (x_i, y_i) \in \mathcal{D}_{\text{norm}} \;\Big|\; &\operatorname{ValidText}(x_i, y_i) \\
&\land \operatorname{RatioFilter}(x_i, y_i) \Big\}
\end{aligned}
$$

具體過濾規則如下：
1. **文字正規化（Normalization）**：套用 Moses 標點正規化、Unicode NFKC 正規化、移除 ASCII 控制字元與多餘空白；
2. **正則清洗（Regex Cleaning）**：
   * 移除行首說話者標籤（大寫拉丁字母接冒號，如 `A:`）；
   * 刪除長度 1 至 10 個字元之括號內註解；
   * 移除已知中文假影字串（如「全文紀錄」、「中文紀錄」、「女人全名」等）；
   * 去除句尾逗號、修剪游離引號與括號、修正標點符號前後異常空格；
3. **非平行內容排除（Non-Parallel Filtering）**：
   * 排除華語端包含舞台指示短語（如「跳到下一項」、「我就講到這裡為止」）；
   * 排除華語端為純頁碼標記、孤立數字編號或年份標題；
   * 排除華語端純為重複標點或連續兩個以上之語氣助詞（如「哈」、「喔」等）；
   * 排除族語端含有漢字之語句對；
4. **長度比門檻過濾（Length Ratio Thresholds）**：
   * **雙邊詞數均 $\ge 2$ 時**：計算目標詞數與來源詞數比例 $r = \text{len}_{\text{tgt}} / \text{len}_{\text{src}}$，剔除 $r \le 0.2$ 或 $r > 8.0$ 之句對；
   * **任一邊詞數 $< 2$ 時**（多為詞典單詞詞條）：改採字元數比例 $r = \text{char}_{\text{tgt}} / \text{char}_{\text{src}}$，剔除 $r \le 0.05$ 或 $r > 20.0$ 之極端偏離句對。

### 2. 涵蓋之 15 種語言代碼

語料庫收錄臺灣官方認定之原住民族語言，共對應 15 個 ISO 639-3 語言代碼（表 1, p. 3447）：

$$
\begin{aligned}
\mathcal{L}_{15} = \{ &\text{ami}, \text{bun}, \text{ckv}, \text{dru}, \text{pwn}, \text{pyu}, \text{ssf}, \text{sxr}, \\
&\text{szy}, \text{tao}, \text{tay}, \text{trv}, \text{tsu}, \text{xnb}, \text{xsy} \}
\end{aligned}
$$

* 涵蓋：阿美語（`ami`）、布農語（`bun`）、噶瑪蘭語（`ckv`）、魯凱語（`dru`）、排灣語（`pwn`）、卑南語（`pyu`）、邵語（`ssf`）、拉阿魯哇語（`sxr`）、撒奇萊雅語（`szy`）、達悟/雅美語（`tao`）、泰雅語（`tay`）、賽德克語與太魯閣語（`trv`，政治上分立但語言學共享相同 ISO 代碼，數據合併）、鄒語（`tsu`）、卡那卡那富語（`xnb`）、賽夏語（`xsy`）。

### 3. 神經翻譯基準與 NLLB-200 分詞器調適

論文並未採取 15 語聯合多語言預訓練（該項於 §6 明確列為未來工作），而是**針對各語言對分別訓練獨立的雙向雙語基準模型**（§4.1–§4.2, pp. 3449–3451）：

1. **OpenNMT-py 端到端基準**：2 層 LSTM 編碼器－解碼器（Input feeding、General global attention、Embedding 256、RNN 512、Adam 學習率 $10^{-3}$、Batch 2048 tokens、Dropout 0.3），雙向語料串接為單一流，行首前置目標語言代碼。
2. **NLLB-200 雙向微調架構**：
   * **分詞器改造**：以原生方式重構 tokenizer，將南島語語言代碼置於 `additional_special_tokens` 並確保 `<mask>` 保持於末位；為新代碼賦予種子嵌入（非隨機初始化），並對新子詞進行 Warm-start；
   * **繁中適配**：修復原生 NLLB 在繁體中文上的分詞切分偏差；
   * **動態雙向訓練迴圈**：每步以 $p = 0.5$ 機率隨機採樣翻譯方向（族語 $\to$ 漢/英 或 漢/英 $\to$ 族語），即時設定 `tokenizer.src_lang`，採用 Adafactor 優化器（學習率 $10^{-4}$，1000 步 warmup），Batch size 8，最大序列長度 128。

```text
[FormosanBank + 影片字幕] ──► [NFKC / 正則清洗] ──► [詞/字長度比過濾] ──► [FormosanMT (49.3 萬句對)]
                                                                               │
       ┌───────────────────────────────────────────────────────────────────────┘
       ▼
[獨立語言對劃分 (80/10/10)] ──► [獨立雙向模型訓練] ──► (1) OpenNMT-py 2-layer LSTM
                                                    └──► (2) NLLB-200 (繁中補丁 + 雙向微調)
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 1. 平行語料庫規模與分割（表 2, p. 3449）
* **總語料規模**：過濾與分割後，全語料庫總計 **493,519 句對**：
  * **族語－華語（Formosan–Mandarin）**：共 **397,710 句對**（15 種語言均具備，規模從阿美語 64,888 句對至邵語 21,795 句對不等）；
  * **族語－英語（Formosan–English）**：共 **95,809 句對**（涵蓋 4 種具備英語對齊之語言：阿美語 36,039、布農語 25,627、魯凱語 13,010、泰雅語 21,133 句對）。
* **無偏差數據分割（Partitioning）**：各數據源分別以固定隨機種子進行 80/10/10 劃分（訓練集/開發集/測試集）；嚴格剔除重複句對，並將包含單側重複句子或詞典詞條（Lexeme）強制引流至訓練集，避免測試集評估虛高。

### 2. 機器翻譯基準評測結果（表 3 & 表 4, p. 3451）
* **族語 $\leftrightarrow$ 華語評測（表 3）**：
  * NLLB-200 在絕大多數語言與方向上顯著勝過 OpenNMT；
  * **族語 $\to$ 華語（BLEU 分數）**：卡那卡那富語 $\to$ 華語 NLLB 達 **26.90**（OpenNMT 15.40）；布農語 $\to$ 華語 NLLB 達 **25.08**（OpenNMT 19.70）；邵語 $\to$ 華語 NLLB 達 **25.09**（OpenNMT 14.10）；魯凱語 $\to$ 華語 OpenNMT（21.70）略高於 NLLB（19.97）；
  * **華語 $\to$ 族語（chrF++ 分數，反映豐富構詞準確度）**：華語 $\to$ 卡那卡那富語 NLLB 達 **51.79**（OpenNMT 35.10）；華語 $\to$ 噶瑪蘭語 NLLB 達 **48.88**（OpenNMT 28.70）；華語 $\to$ 邵語 NLLB 達 **47.28**（OpenNMT 32.70）。
* **族語 $\leftrightarrow$ 英語評測（表 4）**：
  * 布農語 $\to$ 英語 NLLB BLEU 達 **43.08**（chrF++ 53.55）；
  * 泰雅語 $\to$ 英語 NLLB BLEU 達 **41.02**（chrF++ 49.19）；
  * 阿美語 $\to$ 英語 OpenNMT BLEU 達 33.50（NLLB 為 25.02）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **鋪平臺灣南島語進入全球現代 NLP 主流的數位跑道**：徹底解決了國際研究團隊無法取得標準化臺灣南島語資料的歷史痛點，使全球多語言神經翻譯架構能夠首度大規模在臺灣 15 種原住民族語言上開箱即用評測。
* **開源完整生態系工程資產**：公開了標準化的抽取、長度比過濾與評測腳本，更重要的是提供了相容於現代 `transformers` 生態之 NLLB 繁體中文修復補丁與代碼嵌入初始化方案，為全球瀕危語言遷移微調提供了標準化工程範本。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

FormosanMT 是近年南島語 NLP 領域最重量級的開源基礎設施，為我的碩士論文研究提供了現成的高性能底座：

1. **直接採用 FormosanMT 作為預訓練與微調的核心語料庫**：
   * 我的模型不再局限於少數單一資料夾，而是可以直接以 FormosanMT 提供的 **49.3 萬句對（含 39.7 萬高品質族語－華語句對）** 作為基礎底座，快速微調各類神經翻譯網路與檢索增強索引。
2. **與構詞解析器（Morphological Analyzer）的完美聯動**：
   * FormosanMT 雖然規模完備，但其文本全部為表層詞形（Surface Word）；若將海大實驗室戴晟哲、楊鈞凱的深層構詞解析器應用於 FormosanMT 全語料，將產出全球第一套「標註深層詞根與焦點語素」的超高階臺灣南島語語法平行語料庫，直接將研究成果推向頂會高度！

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Scheppat, H., Hartshorne, J. K., Koc, S., Le Ferrand, É., & Prud'hommeaux, E. (2026). FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family. In *Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)* (pp. 3445-3455). DOI: [10.63317/3ut33xim33nt](https://doi.org/10.63317/3ut33xim33nt)
  * 原始檔典藏：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-formosanmt-parallel-corpus-scheppat.md](../evidence/2026-formosanmt-parallel-corpus-scheppat.md)
