---
title: "Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge: Russian-Kyrgyz"
title_zh: "以資料為中心之方法應用於 LoResMT 2026 突厥語翻譯挑戰賽：俄羅斯語至吉爾吉斯語"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Dmitry Novokshanov"
venue: "Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026), 225-230"
domain: "ai"
domain_tags: ["#自然語言處理", "#深度學習", "#人工智慧"]
concepts: ["low-resource-machine-translation"]
status: "wiki"
verification: "verified"
my_focus: true
focus_role: "llm-assisted"
focus_languages: ["吉爾吉斯語"]
doi_url: "https://doi.org/10.18653/v1/2026.loresmt-1.22"
hook: "斬獲 LoResMT 2026 突厥語翻譯競賽俄吉賽道第一名：以 SONAR（blaser_2.0）品質分級過濾與四階段課程學習（標準 OPUS → 高品質 OPUS → FineWeb-2 回譯 → 對話微調），配合 mt0-large 詞表剪枝至 800M，在競賽測試集達到 49.1 chrF++。"
card_line: "精挑語料、分段訓練，俄譯吉爾吉斯語奪冠"
---

# 以資料為中心之方法應用於 LoResMT 2026 突厥語翻譯挑戰賽 (Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge)

> 「在低資源機器翻譯的競技場上，最致命的陷阱是試圖用龐大複雜的神經網絡硬吃充斥雜訊的語料。當你將每一道資料流水線清洗至極致純淨，並依課程排程由粗到精訓練，800M 的小模型也能擊敗 54B 的巨無霸。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Dmitry Novokshanov（俄羅斯國立高等經濟大學，HSE University），*LoResMT 2026*, pp. 225–230。參賽系統針對俄羅斯語至吉爾吉斯語（Russian $\to$ Kyrgyz）翻譯任務。

---

## Card 1 ｜ 時代銘文 (The Hook)
在國際計算語言學頂級低資源競賽——第九屆低資源語言機器翻譯研討會（LoResMT 2026）的突厥語族翻譯挑戰賽中，俄語至吉爾吉斯語（Russian $\to$ Kyrgyz）任務吸引了全球眾多團隊角逐。突厥語族具備豐富的黏著構詞、母音和諧與動詞居末語序；吉爾吉斯語約有 500 萬使用者，但長期缺乏大規模平行語料（§1, p. 225）。

俄羅斯國立高等經濟大學（HSE University）的 Dmitry Novokshanov 摒棄盲目擴大模型參數的路線，提出一套極致的「以資料為中心（Data-Centric）」解決方案：結合烏茲別克語與塔吉克語的多語跨語言遷移、Meta SONAR 語義相似度品質分級過濾、`mt0-large` 詞表剪枝，以及「四階段課程學習（Four-Stage Curriculum Learning）」。該 800M 參數模型最終在官方共享任務測試集上取得 **49.1 chrF++** 與 **69.7 xCOMET-XXL**，榮獲俄吉賽道全場第一名，並在基準測試上全面超越 70 倍體量的 NLLB-200（54B）與 235B 的 Qwen3。

---

## Card 2 ｜ 世紀瓶頸：合成資料的毒化效應與混亂訓練進程 (The Dilemma)
在極低資源翻譯與競賽中，研究者通常面臨兩大核心瓶頸（§1, §2.1, pp. 225–226）：

* **回譯與網路爬取資料的「毒化陷阱」**：為擴充吉爾吉斯語數據，從網路抓取的單語文字往往含有大量拼寫錯誤、錯位對齊、非目標語言片段以及 LLM 回譯時引入的後設註解（Meta-commentary）與重複迴圈；未經清洗的數據會迅速毒化神經模型，造成注意力發散與嚴重語法幻覺。
* **無差別混洗訓練導致的梯度混亂**：傳統作法將數百萬句雜訊較多的合成數據與高品質黃金句對隨機混合訓練。這種做法忽視了學習規律：模型早期容易被噪聲誤導偏離正軌，晚期又無法集中於乾淨的領域規範進行收斂。

---

## Card 3 ｜ 突破架構與原理：SONAR 語意分級與四階段課程學習 (The Secret)

原文的核心架構由**跨語言輔助遷移**、**詞表剪枝**、**SONAR 語意過濾**與**四階段課程學習**組成（§2.1–§2.3, pp. 225–228）：

### 1. 跨語言輔助遷移與詞表剪枝（§2.3.1–2.3.2, pp. 226–227）
* **輔助語言選擇**：納入地緣相鄰且同屬突厥語族的**烏茲別克語（Uzbek）**，以及共享西里爾字母書寫系統的**塔吉克語（Tajik）**。Table 2 證實，將俄－烏、俄－塔平行資料納入訓練，使俄吉翻譯表現從 21.5 顯著提升至 23.2 chrF++（xCOMET 從 16.9 提升至 18.7）。
* **詞表剪枝（Vocabulary Pruning）**：基底模型採用預訓練多語言模型 `mt0-large`（基於 mT5，原始參數量約 1.23B，詞表涵蓋 250,000 個詞元）。作者剪除未在訓練語料中出現的詞元嵌入，將模型參數量大幅壓縮至約 **800M**，在維持全部非嵌入層權重的同時極大降低顯存佔用與計算延遲。

### 2. SONAR 跨語言語義打分與資料過濾流水線（§2.1.1, pp. 225–226）
作者使用 Meta 開源的 `SONAR` 框架中之 **`blaser_2.0`** 跨語言語義相似度預測模型（評分區間為 1 至 5 分，非餘弦相似度）：
* **硬性淘汰**：評分 $< 3.0$ 的句對直接丟棄（判定為錯位對齊或低劣翻譯）。
* **標準品質層（Standard Quality）**：$3.0 \le \text{Score} < 3.7$（共 8,207,314 句，含俄、吉、烏、塔四語雙向）。
* **高品質層（High Quality）**：$\text{Score} \ge 3.7$（共 7,069,840 句）。

### 3. 四階段課程學習排程（Four-Stage Curriculum Training, §2.3.3, pp. 227–228）
依據資料規模與純度「由粗到精、由大到小、由噪到純」逐步推進：
1. **階段 1：OPUS 標準品質多語資料**：在標準品質層（$3.0 \le \text{SONAR} < 3.7$，8.2M 句）上訓練剪枝後的 800M 模型，建立廣泛跨語言翻譯基礎能力。
2. **階段 2：OPUS 高品質多語資料**：以階段 1 最佳 Checkpoint 在高品質層（$\text{SONAR} \ge 3.7$，7.1M 句）繼續微調，淨化語法結構並降低雜訊錯誤。
3. **階段 3：FineWeb-2 開源合成回譯資料**：自 FineWeb-2 抽取 50 萬吉爾吉斯語文件，切成 1,849,234 句，由 Gemma-3-27B 與 Qwen3-235B 回譯為俄語；經 MADLAD-400-7B-MT 交叉熵 $(0.1, 4.5)$ 雙向過濾後保留 1,566,927 句對（雙向 3,133,854 句），擴展模型對多樣化網路領域與長句的適應力。
4. **階段 4：SiberianPersonaChat 高品質合成對話資料**：使用 GPT-4o 翻譯之 56,529 段對話（雙向 113,058 句）進行最後微調，使模型適應口語會話語域。

```text
[OPUS 俄/吉/烏/塔] ──► [SONAR blaser_2.0 分級] ──┬─► [標準品質層 8.2M] ──► 階段 1：基礎預熱
                                                  └─► [高品質層 7.1M]   ──► 階段 2：質量精煉
                                                                                  │
[FineWeb-2 吉語單語 50 萬篇] ──► [Gemma3/Qwen3 回譯 + MADLAD 過濾 3.1M] ──────────► 階段 3：領域廣度擴展
                                                                                  │
[SiberianPersonaChat 對話]  ──► [GPT-4o 翻譯 11.3 萬句] ─────────────────────────► 階段 4：會話語域微調
                                                                                  ▼
                                                                     [最終 800M 冠軍模型]
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 1. 訓練資料集規模（表 1, p. 226）
* **階段 1（OPUS 標準品質）**：8,207,314 句（含全方向）。
* **階段 2（OPUS 高品質）**：7,069,840 句。
* **階段 3（FineWeb-2 合成回譯）**：3,133,854 句。
* **階段 4（合成對話）**：113,058 句。

### 2. 輔助語言消融結果（表 2, p. 227，使用 mT0-small 300M 於 FLORES-200 devtest 評估）
* 僅用 `ru-ky`：16.9 xCOMET / 21.5 chrF++
* 加入 `ru-uz`：17.4 xCOMET / 22.1 chrF++
* 加入 `ru-uz + ru-tg`：**18.7 xCOMET / 23.2 chrF++**（證實兩輔助語言具備互補增益）。

### 3. FLORES-200 devtest 基準模型對比（表 3, p. 228，俄語 $\to$ 吉爾吉斯語）

| 模型類型 | 模型名稱 | 參數量 | chrF++ | xCOMET-XXL |
|---|---|---|---|---|
| 開源通用大模型 | Gemma3 27B | 27B | 40.2 | 67.1 |
| 開源通用大模型 | Qwen3 235B | 235B | 36.2 | 55.5 |
| 開源通用大模型 | GPT-oss 120B | 120B | 37.4 | 61.9 |
| 專業翻譯大模型 | MADLAD-400 7B | 7B | 40.8 | 74.9 |
| 專業翻譯巨型模型 | NLLB-200 54B | 54B | 41.7 | 73.4 |
| **本文課程進程** | **本文模型 (Stage 1)** | 800M | 32.2 | 38.5 |
| | **本文模型 (Stage 2)** | 800M | 43.0 | 73.1 |
| | **本文模型 (Stage 3)** | 800M | 44.8 | 78.8 |
| | **本文模型 (Stage 4 / 最終)** | **800M** | **44.9** | **80.5** |

* 本文 800M 模型在 chrF++ 上超越 NLLB-200 54B 達 **+3.2** 分，在 xCOMET-XXL 上領先 **+7.1** 分。
* 反向翻譯（吉爾吉斯語 $\to$ 俄語）同樣取得高分：**42.4 chrF++ / 82.8 xCOMET-XXL**。

### 4. 官方競賽共享任務測試集結果（§3.2, p. 228）
* 在 LoResMT 2026 官方包含公開與私有部分的 2,311 句測試集上：取得 **49.1 chrF++** 與 **69.7 xCOMET-XXL**，奪得俄語至吉爾吉斯語賽道**第一名**。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **「資料中心（Data-Centric）」在極低資源下的決定性勝利**：證明在低資源 NMT 中，語料的純度、多語言輔助遷移與課程學習的「順序」遠比盲目擴大參數量更具威力；一個經過精心設計資料管線訓練的 800M 模型，足以擊敗 54B 乃至 235B 的龐大模型。
* **詞表剪枝與多語言預訓練的高性價比結合**：利用已具備跨語言表徵能力的 mT0，透過詞表剪枝將 1.23B 壓縮至 800M，展示了如何在學術與受限算力條件下打造競賽級 SOTA 系統。
* **語義相似度預測模型作為品質看門人**：證明使用如 `blaser_2.0` 的跨語言語義打分模型進行分級篩選，能有效隔絕低品質對齊與機器翻譯幻覺對訓練過程的毒害。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **泛泰雅語群（Atayalic）的多語輔助遷移驗證**：
   * Novokshanov 納入烏茲別克語與塔吉克語顯著提升了吉爾吉斯語的翻譯表現。在泛泰雅語群研究中，泰雅語、太魯閣語與賽德克語語法高度同構；在訓練特定方言翻譯模型時，同時納入其他兩語的平行數據作為跨語言輔助資料，能帶來類似的跨語言正向遷移。
2. **詞表剪枝技術的本地落地**：
   * 針對 NLLB-200 或 mT5 等預訓練模型，其巨大詞表（25 萬詞元）大部分為與臺灣原住民族語無關的語言符號。若借鏡本文的 Vocabulary Pruning，將詞表剪枝僅保留目標族語與華語字符，可將模型參數量大幅壓縮 30%–40%，大幅緩解實驗室伺服器的顯存瓶頸並加速收斂。
3. **臺灣南島語多階段課程學習排程**：
   * 階段 1：使用原民會全語言龐大但雜訊較多的教材進行標準多語預熱；
   * 階段 2：以精校辭典例句（高品質）進行精煉；
   * 階段 3：以合成資料或回譯擴充領域詞彙；
   * 階段 4：以真實口語會話或目標方言測試域資料微調。此排程將顯著優於無差別混洗訓練。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Novokshanov, D. (2026). Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge: Russian-Kyrgyz. In *Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026)* (pp. 225-230). DOI: [10.18653/v1/2026.loresmt-1.22](https://doi.org/10.18653/v1/2026.loresmt-1.22)
  * 開源模型權重：[Hugging Face / Novokshanov/ru-ky-mt0-loresmt2026](https://huggingface.co/Novokshanov/ru-ky-mt0-loresmt2026)
  * 開源合成語料：[Hugging Face / datasets/Novokshanov/ru-ky-synthetic-loresmt2026](https://huggingface.co/datasets/Novokshanov/ru-ky-synthetic-loresmt2026)
  * 原始檔典藏：`raw/my-focus/英文論文/llm 輔助/Data-Centric Approach at the LoResMT 2026 Turkic Translation.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-data-centric-russian-kyrgyz-mt-novokshanov.md](../evidence/2026-data-centric-russian-kyrgyz-mt-novokshanov.md)
