---
title: "Decepticons-IIITH : Morphology-Aware Lexicon Filtering of Back-Translated Data for Low-Resource English-to-Indic Translation"
title_zh: "以構詞感知詞彙過濾回譯資料提升低資源英語至印度諸語翻譯"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Soujanya Rao*, Sakhil Taneja*, Krishna Chaitanya, Radhika Mamidi"
venue: "Proceedings of the Eleventh Conference on Machine Translation, 2207-2212"
venue_short: "WMT"
domain: "ai"
domain_tags: ["#人工智慧", "#深度學習", "#自然語言處理", "#計算語言學"]
concepts: ["low-resource-machine-translation"]
key_papers:
  - "Brown et al. (1993) The mathematics of statistical machine translation: Parameter estimation. Computational Linguistics, 19(2):263-311"
  - "Creutz & Lagus (2007) Unsupervised models for morpheme segmentation and morphology learning. ACM TSLP, 4(1):1-34"
  - "Sennrich et al. (2016) Improving neural machine translation models with monolingual data. ACL 2016, 86-96"
  - "Costa-Jussà et al. (2022) No language left behind: Scaling human-centered machine translation. arXiv:2207.04672"
  - "Gala et al. (2023) IndicTrans2: Towards high-quality and accessible machine translation models for all 22 scheduled Indian languages. arXiv:2305.16307"
  - "Dettmers et al. (2023) QLoRA: Efficient finetuning of quantized LLMs. NeurIPS 36:10088-10115"
status: "published"
verification: "verified"
my_focus: true
focus_role: "report"
focus_languages: ["阿薩姆語", "博多語", "米佐語", "那加梅斯語"]
doi_url: "https://doi.org/10.18653/2026.wmt-main.160"
hook: "僅憑官方平行語料歸納詞彙表，結合借詞擴充與 Morfessor 詞幹子字串比對過濾回譯噪聲，使僅有 2,000 平行句對的那加梅斯語與 15,214 句對的博多語均獲 WMT 2026 主系統第一名。"
card_line: "用詞幹比對過濾回譯句對提升印度低資源翻譯"
---

# 以構詞感知詞彙過濾回譯資料提升低資源英語至印度諸語翻譯 (Decepticons-IIITH: Morphology-Aware Lexicon Filtering of Back-Translated Data)

> 「當雙語語料稀缺到連跨語言品質評估模型都尚未覆蓋時，從現有少數平行句對自身提煉構詞感知詞彙濾網，便成了把低資源回譯從噪聲化腐朽為訓練訊號的關鍵槓桿。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Rao*、Taneja*、Chaitanya 與 Mamidi（IIIT Hyderabad），*Proceedings of the Eleventh Conference on Machine Translation*（WMT 2026），pp. 2207–2212（DOI: `10.18653/2026.wmt-main.160`）。針對 WMT 2026 低資源印度語言翻譯任務（英語→阿薩姆語、博多語、米佐語、那加梅斯語），提出不依賴外部 QE 模型之構詞感知詞彙過濾方法 MALM 與兩階段 QLoRA 微調系統。

---

## Card 1 ｜ 時代銘文 (The Hook)

在缺乏大規模平行語料的低資源機器翻譯任務中，把目標語單語料反向翻譯成合成平行句對的「回譯（Back-Translation）」（Sennrich 等, 2016）是標準增廣策略；然而當平行語料極度稀缺時，反向模型本身翻譯品質不穩，會生成語意偏離、殘缺或錯碼的雜訊句對，反而拖累正向模型訓練（Khayrallah 與 Koehn, 2018；原文 p. 2207, 2209）。常見的合成資料過濾器高度依賴跨語言句嵌入模型（如 LaBSE）或無參考品質評估模型（如 CometKiwi），但在 WMT 2026 低資源印度語言翻譯共享任務評估的四種目標語（阿薩姆語、博多語、米佐語、那加梅斯語）中，此類工具僅覆蓋阿薩姆語（摘要 p. 2207；§4.2, p. 2209）。

IIIT Hyderabad 團隊提出的 **Decepticons-IIITH** 系統以 **MALM（Morphology-Aware Lexicon Matching，構詞感知詞彙比對）** 正面突破這項覆蓋瓶頸：系統完全不依賴預訓練多語品質評估模型，僅從各語言官方平行訓練集自身歸納種子詞彙表，結合借詞編輯距離擴充與無監督 Morfessor 詞幹（及子字串詞根）比對來評估回譯語意保留度，再經兩階段 4-bit QLoRA 訓練（先在 MALM 過濾合成句對微調，再於官方平行語料微調），在平行資料最少的兩個 Category-2 方向——英語→博多語與英語→那加梅斯語——均奪得官方主系統第一名（摘要 p. 2207；§5, p. 2211）。

---

## Card 2 ｜ 世紀瓶頸：品質評估缺口與黏著構詞的雙重盲點 (The Dilemma)

作者團隊在極低資源英語至印度諸語翻譯任務（表 1，p. 2208）上面臨兩類跨語言過濾障礙（摘要 p. 2207；§1, §4.2, pp. 2207, 2209–2210）：

* **跨語言嵌入與 QE 模型對長尾語言幾近盲區**：評估涵蓋四個差距懸殊的語言對——屬於 Category-1 的 `en_to_as`（阿薩姆語，官方 54,000 句對，孟加拉－阿薩姆文）與 `en_to_lus`（米佐語，50,000 句對，拉丁文），以及屬於 Category-2 的極低資源方向 `en_to_brx`（博多語，15,214 句對，天城文）與 `en_to_nag`（那加梅斯語，僅 2,000 句對，拉丁文）（表 1, p. 2208）。除了阿薩姆語外，其餘三語皆不在 LaBSE 與 CometKiwi 覆蓋範圍內，無法直接使用現用語義過濾工具。
* **書寫與規則檢驗看不見語意漂移，字面比對又誤殺屈折構詞**：以 fastText 語言識別與長度比例檢查只能揪出格式異常或錯語種輸出，無法判別譯文是否保留來源句實質意義（摘要 p. 2207）。若退而進行字面詞表比對，則會在兩處失靈：其一，僅 2,000 句平行資料歸納出的那加梅斯語詞表只有 750 條實詞，漏掉大量日常借用英文詞彙；其二，博多語等黏著語言會在詞幹後方附加格位與屈折後綴（例如屬格 `हादोरनि` 與方位格 `हादोराव` 同出於詞根 `हादोर`），字面比對會誤將忠實翻譯打為零分（§4.2, pp. 2209–2210）。

---

## Card 3 ｜ 突破原理：MALM 三步驟過濾與兩階段 QLoRA 微調 (The Secret)

本研究全文未列出編號數學公式，核心技術在於一套僅由官方平行語料自舉建構的三步驟構詞感知過濾器 **MALM**，以及接續的兩階段訓練流程（§3.2–§4.3, pp. 2208–2210）：

### 1. 公開單語整理與反向 NLLB 回譯生成（§3.2–§4.1，表 2 與表 3）
* 從 IITB IndicMonoDoc、AI4Bharat IndicCorpV2、MWire Labs 4M、PMIndia 與 Kaggle／Nagamese Khobor 等公開來源彙整單語句並清理（移除零寬字元、保留 3–100 空白詞元句子、去重、阿薩姆語捨棄不含孟加拉－阿薩姆文字文本，超額者取最長句並設上限 200,000 句），最終單語資料量如**表 2**（p. 2208）：阿薩姆語 `200,000`、博多語 `147,670`、米佐語 `197,300`、那加梅斯語 `88,408`（總計 `633,378` 句，表 4）。
* 在官方平行資料上微調反向（Indic → En）`NLLB-200-3.3B` 模型將單語回譯為英語：因 NLLB 詞表缺乏那加梅斯語與博多語標籤，那加梅斯語沿用 `eng_Latn`，博多語則以固定 `<unk>` 前綴標記來源語。如**表 3**（p. 2209），四語原始回譯的近似複製率僅 `0.00%–3.63%`、LR→En 相似詞 `0.00%–1.90%`、長度比中位數（`en/lr`）`0.806–1.111`、截斷比例（`<0.5`）`1.97%–7.50%`，證實未出現明顯複製與幻覺。

### 2. MALM 三步驟過濾機制（§4.2，表 4）
1. **詞彙歸納（Lexicon induction）**：於官方平行語料雙向執行 `5` 輪 EM 的 IBM Model 1（Brown 等, 1993），保留雙向分數幾何平均 $\ge 0.10$ 且至少出現於 `3` 句對的實詞對（移除英文停用詞、出現超過 `12%` 平行句之高頻目標詞、長度 `< 2` 與獨立數字），產生種子詞彙表：`8,384`（`asm`）、`7,189`（`brx`）、`5,555`（`lus`）、`750`（`nag`）。
2. **借詞感知擴充（Borrowing-aware expansion）**：直接納入借詞，目標詞與英文完全一致者賦予信心分數 `0.90`，相差單字元編輯距離（拼寫適應）賦予 `0.60`，詞表隨即擴充至 `9,277`（`asm`）、`7,622`（`brx`）、`9,149`（`lus`）與 `7,907`（`nag`，擴增約十倍，讓 2,000 句語料得以支撐過濾）。
3. **構詞感知評分與門檻（Morphology-aware scoring）**：對每個通過 fastText 語言識別、長度比例 `[0.45, 2.2]` 與去重之合成句對，為出現在擴充詞彙表內的英文詞彙建立預期詞表，先使用無監督 Morfessor（Creutz 與 Lagus, 2007）切出最長片段作為詞幹比對；若未命中，則退回檢查長度至少 `3` 字元的詞根是否出現於目標句某詞彙內部（例如博多語 `country` 對應屬格 `हादोरनि` 與合成句中的方位格 `हादोराव` 共享詞根 `हादोर`）。將命中的預期詞彙依其詞表信心加權求和計算保留分：阿薩姆語、米佐語與那加梅斯語設門檻 `k = 0.5`；博多語若用 `k = 0.5` 僅 `10,395` 句（`7%`）過關，且零分句集中 `98%` 仍正確保留來源數字（例句 `"Time8, Kokrajhar, December 7"` 音譯作 `"टाइम8, कक्राझार, डिसेम्बर7"` 卻因專有名詞缺席詞表而得分為 0），顯示低分多屬指標偽陰性，故改用較寬鬆門檻 `k = 0.2`。

### 3. 兩階段 4-bit QLoRA 訓練架構（§4.3）
* **正向模型選用**：阿薩姆／米佐／那加梅斯語採用 `NLLB-200-3.3B`（解碼標籤分別為 `asm_Beng`、`lus_Latn` 與借用 `eng_Latn`）；博多語改採原生支援該語的 `IndicTrans2-1B`（`brx_Deva`）。全數使用 4-bit NF4 雙重量化與 `fp16` 計算、LoRA `r=32, alpha=64, dropout=0.1`（`q, k, v, out`，`IndicTrans2-1B` 另含 `fc1, fc2`）、餘弦排程、權重衰減 `0.01`、分頁 8-bit AdamW、梯度檢查點與有效批次大小 64（4 張 RTX 2080 Ti）。
* **主系統 vs 對比系統**：主系統（Primary）先進行 **Stage-1**（MALM 過濾合成資料微調，lr `3e-4`；`asm/lus` 3 epochs、`brx/nag` 5 epochs，依驗證損失挑最佳 epoch），再接 **Stage-2**（官方平行語料微調，一般 lr `2e-5` 最多 15 epochs、100 warmup steps；`nag` lr `1e-5` 最多 25 epochs、0.1 warmup ratio；patience `5`，依 5% 留出集 `sacreBLEU chrF++` 選最佳檢查點）。對比系統（Contrastive）則略過 Stage-1，僅執行相同設定的 Stage-2。

---

## Card 4 ｜ 決定性數據：MALM 保留率與 WMT 2026 盲測實績 (The Evidence)

### 1. MALM 過濾前後合成平行句對數（表 4，原文 p. 2210）

| 語言 | 門檻 `k` | 過濾前句對 | 過濾後句對 | 保留率 |
|---|---:|---:|---:|---:|
| `asm`（阿薩姆語） | 0.5 | 200,000 | 128,939 | 64.5% |
| `brx`（博多語） | 0.2 | 147,670 | 47,489 | 32.2% |
| `lus`（米佐語） | 0.5 | 197,300 | 111,997 | 56.8% |
| `nag`（那加梅斯語） | 0.5 | 88,408 | 56,343 | 63.7% |
| **總計（Total）** | — | **633,378** | **344,768** | **54.4%** |

### 2. WMT 2026 官方盲測六項指標成績（表 5 與 §5，原文 p. 2211）

| 語言對 | 系統版本 | 官方平行規模 | BLEU↑ | METEOR↑ | TER↓ | chrF++↑ | BERTScore↑ | COMET↑ | 官方排名 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `en_to_as` | 主系統（+MALM BT） | 54,000 | 14.09 | 35.41 | 73.78 | 47.83 | 85.27 | 80.59 | 第 11 / 15 |
| `en_to_as` | 對比系統（僅官方） | 54,000 | 15.00 | 36.44 | 72.29 | 48.98 | 85.83 | 81.65 | — |
| `en_to_lus` | 主系統（+MALM BT） | 50,000 | 19.53 | 46.11 | 71.37 | 48.49 | 81.72 | 62.45 | 第 3 / 9 |
| `en_to_lus` | 對比系統（僅官方） | 50,000 | 19.41 | 46.23 | 73.81 | 48.79 | 81.74 | 63.45 | — |
| `en_to_brx` | **主系統（+MALM BT）** | 15,214 | **16.30** | **37.56** | **70.20** | **50.77** | **85.25** | **62.38** | **第 1 / 10** |
| `en_to_brx` | 對比系統（僅官方） | 15,214 | 15.64 | 36.18 | 71.19 | 49.56 | 84.78 | 62.05 | — |
| `en_to_nag` | **主系統（+MALM BT）** | 2,000 | **20.34** | **59.95** | **76.40** | **57.66** | **82.28** | **69.55** | **第 1 / 5** |
| `en_to_nag` | 對比系統（僅官方） | 2,000 | 12.01 | 47.84 | 105.06 | 47.78 | 76.48 | 62.47 | — |

* **極低資源區間（2k–15k）顯著勝出**：僅有 2,000 平行句對的英語→那加梅斯語受益最大，主系統相對純官方對比系統暴增 **+8.33 BLEU**、**+9.88 chrF++** 與 **+7.08 COMET**，成為四方向中最高 BLEU 分數系統並拿下第 1 名；擁有 15,214 句對的英語→博多語亦在全六項指標穩定進步（**+0.66 BLEU**、**+1.21 chrF++**），於 10 個主系統提交中名列第 1。
* **中等資源區間（50k–54k）現出效益反轉**：當官方平行語料達 50,000 句（米佐語）時，過濾回譯僅帶來混合微幅波動（BLEU 19.53 vs 19.41、chrF++ 48.49 vs 48.79、COMET 62.45 vs 63.45，排名第 3 / 9）；當官方平行語料達 54,000 句（阿薩姆語）時，加入來自較弱反向模型的合成語料反而導致多數指標約 1 分左右的輕微下滑（BLEU 14.09 vs 15.00、COMET 80.59 vs 81.65，排名第 11 / 15）。

---

## Card 5 ｜ 典範轉移：可自舉過濾的適用邊界與未解消融 (The Revolution)

### 本篇公開資源狀況（§3.2 與全文檢查）
* **外部單語資料來源**：作者於 §3.2 腳註 1–9 詳細標註了所有使用的公開資料集網址（IITB `IndicMonoDoc`、`indian-nlp/assamese-dataset`、PMIndia、AI4Bharat `IndicCorpV2`、MWire Labs `mizo-language-corpus-4M` 及 Kaggle / `nagamesekhobor.com` 之那加梅斯語語料）。
* **本篇程式碼與模型權重**：原文**未提及**本論文之 MALM 過濾腳本或微調模型檢查點之公開程式碼庫或模型下載連結。

### 研究侷限與未來方向（§5–§6，原文 p. 2211）
1. **明確界定合成回譯的資源轉折點**：實驗顯示過濾回譯之增益主要集中於極低資源語料（2k–15k），一旦官方平行語料充足（如本篇 50k–54k），較弱反向模型所生成的合成資料反而成為噪聲來源；因此第一階段合成預微調最適合保留給極低資源語言對。
2. **黏著構詞造成詞表濾網高偽陰性**：博多語因黏著後綴加上小平行詞表，對詞彙匹配最不友善，即使放寬至 `k = 0.2` 仍淘汰近七成句對。作者指出未來需從更多平行資源擴增博多語詞彙表，並以後綴感知比對取代單純無監督 Morfessor 切分。
3. **缺少「未過濾回譯」與強反向模型對照**：本篇消融僅比較「MALM 過濾回譯＋官方語料」與「純官方語料」，尚未直接與「未過濾回譯」比較，也尚未測試以原生支援博多語的 `IndicTrans2` 取代無語言標籤 `NLLB-200-3.3B` 擔任反向回譯器，或對唯一被覆蓋的阿薩姆語執行外部 QE 過濾對照（列為未來工作，p. 2211）。

---

## Card 6 ｜ KAIROS：低資源資料工程與模型覆蓋落差的跨語啟示 (Cross-Disciplinary Inspiration)

> **本段為 Wiki 詮釋與跨領域啟發分析**：以下聯繫[低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)領域脈絡，屬知識庫策展詮釋，非原論文作者所主張。

1. **當多語言品質評估器失語時，「自舉詞幹濾網」提供低門檻防線**：在多數未受現代大模型或 QE 模型重點覆蓋的極低資源語種中，研究團隊往往被迫在「直接餵入充滿噪聲的合成回譯」或「放棄單語料增廣」之間二選一。MALM 的設計證明，不必依賴大型外部語意模型，只要組合 IBM Model 1 種子對齊、借詞編輯距離擴充，以及「無監督詞幹＋短詞根子字串退回」的容錯機制，就能在僅兩千句對的語種中有效攔截偏離句並留住可用合成訊號。
2. **「多即是好」不適用於不對稱回譯的 5 萬句門檻以上**：過去直覺常認為先在大量回譯句對暖身總比只用小語料訓練安全，但本篇以同一套 4-bit QLoRA 與 MALM 濾網在四個規模區間證明，一旦真實雙語句對跨過某個足量門檻（此處約 50,000 句以上），反向模型有限精度帶來的分佈偏差就會大過覆蓋率紅利，反而傷及第二階段微調上限。這項資源門檻觀測為多語系統設計階段式課程調度提供了具體的實證界線。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **相關論文**：
  * [低資源翻譯之泛化資料增強（Xia et al. 2019）](2019-generalized-data-augmentation-xia.md)
  * [芬蘭語－北薩米語回譯策略（Sälevä & Lignos 2024）](2024-finnish-northern-sami-mt-saleva.md)
  * [以雙語詞典提升臺灣南島語機器翻譯（Zheng et al. 2024）](2024-formosan-mt-bilingual-lexicon-zheng.md)
  * [使用詞綴資訊提升泛泰雅語機器翻譯效能（金柏毅 2025）](2025-atayalic-affix-mt-jin.md)
* **原始權威文獻**：
  * 官方學術出處：Rao, S., Taneja, S., Chaitanya, K., & Mamidi, R. (2026). Decepticons-IIITH : Morphology-Aware Lexicon Filtering of Back-Translated Data for Low-Resource English-to-Indic Translation. *Proceedings of the Eleventh Conference on Machine Translation*, pp. 2207–2212. DOI: [10.18653/2026.wmt-main.160](https://doi.org/10.18653/2026.wmt-main.160)
  * 原文網頁索引：[ACL Anthology 2026.wmt-main.160](https://aclanthology.org/2026.wmt-main.160/)（本篇程式碼與模型權重未於原文釋出公開網址）
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026.wmt-main.160.pdf`（同目錄附繁體中文全譯本 `2026.wmt-main.160_繁體中文翻譯.pdf`，不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-malm-backtranslation-indic-mt-rao.md](../evidence/2026-malm-backtranslation-indic-mt-rao.md)
