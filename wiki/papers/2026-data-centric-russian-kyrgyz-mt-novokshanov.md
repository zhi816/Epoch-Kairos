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
status: "published"
verification: "verified"
my_focus: true
focus_role: "llm-assisted"
focus_direction: "data-corpus"
focus_languages: ["吉爾吉斯語"]
doi_url: "https://doi.org/10.18653/v1/2026.loresmt-1.22"
hook: "斬獲 LoResMT 2026 突厥語翻譯競賽俄吉賽道第一名：以 SONAR（blaser_2.0）品質分級過濾與四階段課程學習（標準 OPUS → 高品質 OPUS → FineWeb-2 回譯 → 對話微調），配合 mt0-large 詞表剪枝至 800M，在競賽測試集達到 49.1 chrF++。"
card_line: "精挑語料、分段訓練，俄譯吉爾吉斯語奪冠"
---

# 以資料為中心之方法應用於 LoResMT 2026 突厥語翻譯挑戰賽 (Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge)

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Dmitry Novokshanov（俄羅斯國立高等經濟大學，HSE University），*LoResMT 2026*, pp. 225–230。參賽系統針對俄羅斯語至吉爾吉斯語（Russian $\to$ Kyrgyz）翻譯任務。

---

## Card 1 ｜ 一句話看懂
這篇是 LoResMT 2026 突厥語翻譯競賽中俄語→吉爾吉斯語賽道的冠軍系統。作者不追求大模型，而是把資料整理到位：加入烏茲別克語、塔吉克語資料，用語意評分把語料分成兩級，再「先粗後精」分四階段訓練一個 800M 參數的模型（摘要；§2）。官方測試集得到 49.1 chrF++，賽道第一；在 FLORES-200 上也勝過 NLLB-200 54B 等大模型（§3.1–§3.2, p. 228）。

* **語言**：俄語 → 吉爾吉斯語（吉爾吉斯語約 500 萬使用者，缺乏大規模平行語料；§1, p. 225）
* **任務**：機器翻譯（共享任務參賽系統）
* **方法**：輔助語言（烏茲別克語、塔吉克語）＋ 詞表剪枝 ＋ SONAR 語意評分分級 ＋ 四階段課程學習（§2）
* **資料**：OPUS 平行語料、FineWeb-2 吉爾吉斯語回譯資料、GPT-4o 翻譯之對話資料（表 1, p. 226）
* **公開**：最終模型、過濾後的合成平行資料與線上展示皆公開於 Hugging Face（§3.3, p. 228）
* **出處**：Dmitry Novokshanov（HSE University），*LoResMT 2026*, pp. 225–230

---

## Card 2 ｜ 要解決的問題
全球約 7,000 種語言大多缺乏足以訓練翻譯系統的平行語料；突厥語族有豐富的黏著構詞、母音和諧與動詞居末語序，吉爾吉斯語仍缺乏大規模平行語料（§1, p. 225）。

* **平行句不足**：吉爾吉斯語缺乏大規模平行語料，需要借用其他語言資料與合成資料（§1；§2.1）。
* **合成雜訊**：大型語言模型回譯的資料會夾帶模型自己產生的註記、後設說明，或直接重複輸入，需要另外過濾（§2.1.1, p. 226）。
* **品質不一**：OPUS 等平行語料品質參差，大量但較雜的資料與較少但乾淨的資料該如何安排，影響訓練效果（§2.3.3, p. 227）。

這篇的想法：先把語料評分分級，再由粗到精分階段訓練小模型。

---

## Card 3 ｜ 方法流程
原文無編號公式，方法以文字與表格敘述（§2）。白話步驟：

1. **加入輔助語言**：除了俄—吉，也加入俄—烏茲別克語、俄—塔吉克語平行資料。
2. **剪小模型**：從 mt0-large 剪掉語料用不到的詞元，參數從約 1.23B 降到約 800M。
3. **語意評分分級**：用 SONAR 的 blaser_2.0 給每組句對打 1 到 5 分，低於 3.0 丟棄，其餘分成標準與高品質兩級。
4. **四階段訓練**：標準品質 → 高品質 → 網路回譯資料 → 對話資料，由大而雜到小而精。

細節如下：

### 1. 跨語言輔助遷移與詞表剪枝（§2.3.1–2.3.2, pp. 226–227）
* **輔助語言選擇**：納入地緣相鄰且同屬突厥語族的**烏茲別克語（Uzbek）**，以及共享西里爾字母書寫系統的**塔吉克語（Tajik）**。Table 2 顯示，將俄－烏、俄－塔平行資料納入訓練，使俄吉翻譯表現從 21.5 顯著提升至 23.2 chrF++（xCOMET 從 16.9 提升至 18.7）。
* **詞表剪枝（Vocabulary Pruning）**：基底模型採用預訓練多語言模型 `mt0-large`（基於 mT5，原始參數量約 1.23B，詞表涵蓋 250,000 個詞元）。作者剪除未在訓練語料中出現的詞元嵌入，將模型參數量大幅壓縮至約 **800M**，並保留全部非嵌入層權重。

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

## Card 4 ｜ 資料與實驗
### 訓練資料（表 1, p. 226）
* **階段 1（OPUS 標準品質）**：8,207,314 句（含全方向）。
* **階段 2（OPUS 高品質）**：7,069,840 句。
* **階段 3（FineWeb-2 合成回譯）**：3,133,854 句。
* **階段 4（合成對話）**：113,058 句。

* **評測**：FLORES-200 devtest（與開源大模型比較），以及 LoResMT 2026 官方測試集 2,311 句（§3）。
* **評分方式**：chrF++ 與 xCOMET-XXL；沒有人工評分。

---

## Card 5 ｜ 結果

### 輔助語言消融（表 2, p. 227；使用 mT0-small 300M 於 FLORES-200 devtest 評估）
* 僅用 `ru-ky`：16.9 xCOMET / 21.5 chrF++
* 加入 `ru-uz`：17.4 xCOMET / 22.1 chrF++
* 加入 `ru-uz + ru-tg`：**18.7 xCOMET / 23.2 chrF++**。

### FLORES-200 devtest 基準模型對比（表 3, p. 228；俄語 $\to$ 吉爾吉斯語）
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

### 官方共享任務結果（§3.2, p. 228）
* 在 LoResMT 2026 官方包含公開與私有部分的 2,311 句測試集上：取得 **49.1 chrF++** 與 **69.7 xCOMET-XXL**，奪得俄語至吉爾吉斯語賽道**第一名**。

* **作者結論**（§4, p. 228）：結合 OPUS 語料的仔細整理、合成資料與完整的過濾流程，800M 模型勝過 NLLB-200 54B、Gemma3 27B 與 Qwen3 235B 等大得多的基線。

---

## Card 6 ｜ 限制與可用性
* **作者說的限制**：原文沒有限制專節。
* **讀的時候要留意**：這是競賽系統描述，各步驟（輔助語言、剪枝、分級、四階段）的貢獻只有輔助語言做了消融，且消融用的是較小的 mT0-small；四階段的效果以各階段分數呈現（表 3），沒有和「不分階段混合訓練」直接比較（Wiki 註記）。合成資料來自 Gemma、Qwen 與 GPT-4o，評測也部分依賴自動指標 xCOMET。
* **公開程度**：最終第 4 階段模型（`Novokshanov/ru-ky-mt0-loresmt2026`）、過濾後的 FineWeb-2 與 GPT-4o 合成平行資料（`Novokshanov/ru-ky-synthetic-loresmt2026`）與線上展示（Hugging Face Spaces）皆公開（§3.3, p. 228）。
* **適合拿來報告的點**：「小模型＋仔細整理資料＋分階段訓練」就能贏大模型的具體案例，模型與資料都公開，適合拿來討論以資料為中心的低資源翻譯（Wiki 詮釋）。

### 延伸想法
以下為延伸思考（Wiki 推測），不是原文主張。

1. **泛泰雅語群的輔助語言**：本文加入同語族、同文字的語言後吉爾吉斯語翻譯變好。泰雅語、太魯閣語與賽德克語彼此相近，訓練其中一語時或可加入另外兩語的平行資料；效果需實驗驗證。
2. **詞表剪枝**：NLLB-200、mT5 等模型的詞表大多與臺灣原住民族語無關；剪去用不到的詞元可縮小模型、降低記憶體需求。
3. **分階段訓練**：可考慮先用較雜的大量教材資料，再用精校辭典例句，最後用目標領域資料微調；是否優於混合訓練需另行比較。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Novokshanov, D. (2026). Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge: Russian-Kyrgyz. In *Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026)* (pp. 225-230). DOI: [10.18653/v1/2026.loresmt-1.22](https://doi.org/10.18653/v1/2026.loresmt-1.22)
  * 開源模型權重：[Hugging Face / Novokshanov/ru-ky-mt0-loresmt2026](https://huggingface.co/Novokshanov/ru-ky-mt0-loresmt2026)
  * 開源合成語料：[Hugging Face / datasets/Novokshanov/ru-ky-synthetic-loresmt2026](https://huggingface.co/datasets/Novokshanov/ru-ky-synthetic-loresmt2026)
  * 原始檔典藏：`raw/my-focus/大模型輔助/Data-Centric Approach at the LoResMT 2026 Turkic Translation.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-data-centric-russian-kyrgyz-mt-novokshanov.md](../evidence/2026-data-centric-russian-kyrgyz-mt-novokshanov.md)
