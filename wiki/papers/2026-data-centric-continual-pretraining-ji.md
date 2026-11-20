---
title: "Data-Centric Continual Pre-training for 500+ Languages: A New Bilingual Translation Corpus and Multilingual Models"
title_zh: "五百餘語言的雙語持續預訓練：新型翻譯語料庫與多語言模型"
paper_year: 2026
award_year: 2026
timeline_year: 2026
domain: "ai"
domain_tags: ["#人工智慧", "#深度學習", "#自然語言處理", "#計算語言學"]
my_focus: true
focus_role: "report"
focus_languages: []
authors: "Shaoxiong Ji, Zihao Li, Jaakko Paavola, Hengyu Luo, Jörg Tiedemann"
venue: "Findings of the Association for Computational Linguistics: ACL 2026, 18776-18807"
doi_url: "https://doi.org/10.18653/v1/2026.findings-acl.937"
card_line: "併入雙語平行句，替語言模型補足低資源語言"
concepts: ["low-resource-machine-translation"]
key_papers:
  - "Ji et al. (2024a) EMMA-500: Enhancing massively multilingual adaptation of large language models. arXiv:2409.17892"
  - "Lu et al. (2024) LLaMAX: Scaling linguistic horizons of LLM by enhancing translation capabilities beyond 100 languages. Findings of EMNLP 2024"
  - "Lin et al. (2024) MaLA-500: Massive language adaptation of large language models. arXiv:2401.13303"
  - "Springer et al. (2025) Over-trained language models are harder to fine-tune. arXiv:2503.19206"
hook: "建構涵蓋五百餘種語言的 MaLA 雙語翻譯語料庫，並以全參數持續預訓練對照單語與雙語混合配方，驗證平行句對對低資源語言遷移的關鍵影響。"
status: "published"
verification: "verified"
---

# 五百餘語言的雙語持續預訓練：新型翻譯語料庫與多語言模型 (Data-Centric Continual Pre-training for 500+ Languages)

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Ji、Li、Paavola、Luo（University of Helsinki / ELLIS Institute Finland / University of Turku）與 Tiedemann，*Findings of the Association for Computational Linguistics: ACL 2026*，pp. 18776–18807（DOI: `10.18653/v1/2026.findings-acl.937`）。研究建置 2,507 對語言之 MaLA 雙語翻譯語料庫，於 Llama 3 與 Llama 3.1（8B）進行不修改分詞器之全參數持續預訓練，並在 7 項任務、12 個基準評估四款 EMMA-500 模型。

---

## Card 1 ｜ 一句話看懂
這篇整理出涵蓋 500 多種語言、2,507 個語言對的雙語翻譯語料庫 MaLA，並拿它對 Llama 3 與 Llama 3.1（8B）做全參數持續預訓練，比較「只用單語資料」與「加入雙語平行句」兩種配方（摘要；§2–§3）。加入雙語平行句後翻譯明顯進步：Llama 3 在 FLORES-200 英語→其他語言的 chrF++ 從 24.08 提高到 42.15；但英語等高資源語言的閱讀理解退步，作者明言模型尚不適合直接部署（Table 11；Table 5；Limitations）。

* **語言**：500 多種語言（綜合研究，不針對單一語言）
* **任務**：多語大型語言模型的持續預訓練；翻譯與多項理解任務評測
* **方法**：建置 MaLA 雙語語料庫 ＋ 以偽文件格式把平行句併入訓練配方 ＋ 全參數持續預訓練（§2）
* **資料**：MaLA 雙語翻譯語料庫（2,507 個語言對、約 4.3E+11 詞元），另混入單語、程式碼、論文、指令與書籍資料（§2.1–§2.2）
* **公開**：語料庫、四個 EMMA-500 模型與程式碼公開於 Hugging Face 與 GitHub（`MaLA-LM`）（摘要, p. 18776）
* **出處**：Ji、Li、Paavola、Luo、Tiedemann（University of Helsinki、ELLIS Institute Finland、University of Turku），*Findings of ACL 2026*, pp. 18776–18807

---

## Card 2 ｜ 要解決的問題
大型語言模型對低資源與瀕危語言常因預訓練覆蓋不足而表現不佳（§1, p. 18776）。先前的 LLaMAX 同時用單語與平行資料但只涵蓋百餘種語言，初代 EMMA-500 擴展到 500 多種語言卻只用單語文本（§1）。作者指出三個困難（§1–§3）：

* **單語缺對齊**：只用各語言各自爬取的單語網頁文本，缺乏跨語言的對應，低資源翻譯與跨語遷移的幅度有限（§2.2, p. 18779；Table 3）。
* **平行零碎**：公開平行語料多為單句、分佈極不平均（909 個語言對少於 1M 詞元）；若把平行句拆成獨立單語字串訓練，先前研究顯示會損害翻譯（§2.1–§2.2）。
* **基座難適應**：Llama 3／3.1 已用逾 15T 詞元訓練，沿用原本 0.0003 的學習率會在前 5,000 步出現損失尖峰，續訓後高資源語言與部分基準也更容易退步（§2.3, p. 18780；§3.3）。

這篇的想法：建大規模雙語語料，把平行句整段併入持續預訓練。

---

## Card 3 ｜ 方法流程
原文無編號公式，全篇聚焦語料建構、混合配方與全參數持續預訓練之實證評測。白話步驟：

1. **整理雙語語料**：彙整多個公開平行資料來源，統一語言代碼並去重，得到 MaLA 語料庫。
2. **組成偽文件**：同一語言對每 10 組平行句串成一份訓練樣本，保留對照關係。
3. **配兩種配方**：雙語配方（含 32.3% 平行資料）與單語配方（移除平行資料），其餘資料相同。
4. **全參數持續預訓練**：Llama 3 與 Llama 3.1（8B）不改分詞器，學習率降為 0.0001，各訓練 1 個 epoch。
5. **評測**：7 項任務、12 個基準，比較原始模型與四個 EMMA-500 模型。

細節如下：

### 1. MaLA 雙語翻譯語料庫之標準化與清理（§2.1, p. 18778；Table 1 & Table 6）
* 彙整 OPUS、NLLB、Lego-MT、Tatoeba、AmericasNLP、NusaX-MT 與 Lafand-MT 等多元雙語資料來源（Table 6, p. 18792），執行 ISO 639-3 與 ISO 3166-1 alpha-3 語言／方言代碼統一，以及 ISO 15924 書寫系統識別（GlotScript）。
* 運用 OpusFilter 去重並清除同一詞彙或字元連續重複超過五次之異常句列，最終定版為涵蓋 **500+ 語言、2,507 個語言對、逾 426B 空白切分詞元（`4.3E+11`）**之語料庫（Table 1, p. 18778）。

### 2. 偽文件封裝與單／雙語對照混合配方（§2.2, Fig. 1, p. 18779；Table 8, p. 18794）
* **偽文件（Pseudo-document）串接格式**：將同一語言對每 **10 條平行句對**依 `[{src_lang_code}]: {src_text} [{tgt_lang_code}]: {tgt_text}` 樣板串成一份訓練樣本，避免將平行句拆散而保留跨語言對齊語境（§2.2, p. 18779）。
* **嚴格受控雙組配方（Fig. 1, p. 18779；§B, p. 18791）**：
  * **雙語混合（Bilingual Mix）**：**32.3%** 雙語平行資料、**26.3%** 單語資料、**15.0%** 程式碼、**13.2%** 科學論文、**11.4%** 指令資料、**1.8%** 書籍（中與低資源語言合計佔 **33%**）。
  * **單語混合（Monolingual Mix）**：完全移除雙語資料，保留同一非平行子集再歸一（**38.9%** 單語、**22.1%** 程式碼、**19.5%** 論文、**16.8%** 指令、**2.6%** 書籍；中與低資源語言佔 **19%**）。

### 3. 全參數持續預訓練與學習率穩定化（§2.3, p. 18780；Table 2）
* 於 LUMI 超級電腦（64 計算節點、256 顆 AMD MI250x GPU，共耗逾 800k GPU 小時）對 **Llama 3 8B** 與 **Llama 3.1 8B** 實施**不修改分詞器的全參數因果語言模型持續預訓練**（並非 LoRA 低秩適配）。
* 設定全域批次大小 2,048、序列長度 8,192，並透過 5,000 步（84B tokens）前導比較排除造成劇烈損失尖峰的 `0.0003` 學習率，改用較平穩的 `0.0001` 搭配餘弦排程；Mono 版與 Bi 版分別完成 1 個 epoch（**25,000 步 / 419B tokens** 與 **40,000 步 / 671B tokens**）（Table 2, p. 18780）。

---

## Card 4 ｜ 資料與實驗
* **語言對與詞元總量**：MaLA（**2,507 對** / **`4.3E+11` tokens**）與 Lego-MT（2,508 對 / `2.2E+11`）、NLLB（2,509 對 / `2.8E+11`）語言對相近但詞元總量顯著更高；依資源分層為 very high 4 對（>10B）、high 83 對（>1B）、medium-high 67 對（>500M）、medium 281 對（>100M）、medium-low 508 對（>10M）、low 655 對（>1M）、very low **909 對**（<1M）。

* **訓練規模**：單語版 25,000 步／419B 詞元，雙語版 40,000 步／671B 詞元（Table 2, p. 18780）；LUMI 超級電腦 256 顆 GPU，逾 800k GPU 小時（§2.3）。
* **評測**：7 項任務、12 個基準，包括 FLORES-200 翻譯、Taxi1500 與 SIB-200 分類、XCOPA 與 XStoryCloze 常識推理、BELEBELE 閱讀理解、MGSM 數學等（§3）。沒有人工評分。

---

## Card 5 ｜ 結果

### FLORES-200 機器翻譯（Table 11, p. 18798；Table 3, p. 18782；Table 4, p. 18783）
| 模型 | 訓練配方 | FLORES 全語言 Eng→X (chrF++ / BLEU) | FLORES 全語言 X→Eng (chrF++ / BLEU) | 低資源 Eng→X (chrF++ / BLEU) | 低資源 X→Eng (chrF++ / BLEU) |
|---|---|---:|---:|---:|---:|
| `Llama 3 8B` | 原型基座 | 24.08 / 9.93 | 43.72 / 23.78 | 25.84 / 10.51 | 45.72 / 25.49 |
| `EMMA-500 Llama 3 8B Mono` | 單語混合（419B） | 38.34 / 20.33 | 50.86 / 30.38 | 41.29 / 22.03 | 53.16 / 32.55 |
| **`EMMA-500 Llama 3 8B Bi`** | **雙語混合（671B）** | **42.15 / 24.02** | **54.33 / 34.40** | **45.22 / 25.99** | **56.69 / 36.72** |
| `Llama 3.1 8B` | 原型基座 | 24.69 / 10.11 | 44.10 / 24.19 | 26.46 / 10.66 | 46.13 / 25.91 |
| `EMMA-500 Llama 3.1 8B Mono` | 單語混合（419B） | 37.41 / 19.44 | 48.12 / 27.57 | 40.32 / 21.06 | 50.34 / 29.51 |
| `EMMA-500 Llama 3.1 8B Bi` | 雙語混合（671B） | 42.07 / 23.86 | 53.49 / 33.64 | 45.07 / 25.80 | 55.84 / 35.91 |

* **跨模型競爭力排名（Table 4, p. 18783）**：在 FLORES-200 204 語言對上，`EMMA-500 Llama 3 8B Bi` 有 **88.18%** 語言進入所有受測模型前 3 名、**98.52%** 進入前 5 名，**100.00%** 進入前 10 名（原基座 `Llama 3 8B` 分別僅為 `0.00% / 0.00% / 25.12%`）。

### 分類、理解、常識推理與適應代價（Table 3, p. 18782；Fig. 3 與 Table 5, p. 18783）
1. **分類基準呈分化表現**：在覆蓋 1,502 種語言的 Taxi1500 低資源子集，`EMMA-500 Llama 3 8B Bi` 達 **26.72%** 準確率（全組最高，全語言均分 **25.13%**）；然於 SIB-200 低資源子集，該變體自基座 `65.53%` 滑落至 `39.65%`（全語言平均從 `63.70%` 降至 `39.40%`），同系列僅 `EMMA-500 Llama 3.1 8B Bi` 守住 `63.33%`（全語言 `62.07%`）。
2. **常識推理穩定成長**：在 XCOPA 與 XStoryCloze 上，`EMMA-500 Llama 3.1 8B Bi` 分別達到 **67.25%** 與 **68.47%**（較 Llama 3.1 基座 `61.71%` 與 `63.58%` 提升逾 4.8–5.5 個百分點）。
3. **高資源閱讀退化與基座阻力（Table 5 & Fig. 3）**：在 BELEBELE（Table 5）中，`EMMA-500 Llama 3 8B Bi` 在低資源語言獲益（喀爾喀蒙古語 `khk_Cyrl` `+4.22` 至 `39.33%`、北索托語 `nso_Latn` `+6.00` 至 `35.22%`），高資源語言卻大幅遺忘（英語 `eng_Latn` 自 `74.56%` 降至 `56.78%`、`Δ = -17.78`）。從退化基準總數來看（Fig. 3），Llama 2 Mono 平均僅在 **2** 個基準遜於基座，而 Llama 3 Mono/Bi 增至 **7 / 5** 個，Llama 3.1 Mono/Bi 更達 **6 / 9** 個基準。

---

## Card 6 ｜ 限制與可用性
* **作者說的限制**（Limitations, pp. 18784–18785）：
  1. 數學（MGSM）與閱讀理解（BELEBELE，尤其機器翻譯版題庫）仍弱，單靠雙語持續預訓練在 8B 規模不足以支撐跨語言深層推理。
  2. 受限於算力，無法對資料混合比例與學習率做網格搜尋；為維持 1 個 epoch，雙語版（671B 詞元）與單語版（419B 詞元）的訓練步數不相等。
  3. 模型只做了持續預訓練，尚未經過人類偏好對齊或紅隊測試，作者明言目前不適合直接部署。
* **讀的時候要留意**：雙語版訓練的詞元比單語版多，比較時兩者不完全等量；Llama 3 雙語版在 SIB-200 與英語 BELEBELE 明顯退步（見 05）。
* **公開程度**：MaLA 雙語翻譯語料庫 `MaLA-LM/mala-bilingual-translation-corpus`、四個 EMMA-500 模型 `MaLA-LM/emma-500` 與評測程式 `github.com/MaLA-LM/emma-500` 皆公開；專案網站另有分語言評測結果（摘要, p. 18776）。
* **適合拿來報告的點**：大規模、資料公開的雙語持續預訓練案例，清楚示範「加入平行句」對 500 多種語言翻譯的幫助，也誠實列出高資源語言退步的代價（Wiki 詮釋）。

### 延伸想法
以下為延伸思考（Wiki 推測），不是原文主張。

1. **平行句是低資源續訓的重要訊號**：本文顯示在不改分詞器的全參數持續預訓練中，把平行句以偽文件形式併入並降低學習率，8B 模型也能在大量語言的翻譯上明顯進步；臺灣南島語若有足夠平行句，或可考慮類似配方，但需實驗驗證。
2. **容量與多語覆蓋的取捨**：英語閱讀理解退步 17.78 分，反映有限參數在「高資源表現」與「多語覆蓋」之間的取捨；這與以混合專家路由保留語言邊界的路線（如 Bandarkar 等 2026）形成對照。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Ji, S., Li, Z., Paavola, J., Luo, H., & Tiedemann, J. (2026). Data-Centric Continual Pre-training for 500+ Languages: A New Bilingual Translation Corpus and Multilingual Models. *Findings of the Association for Computational Linguistics: ACL 2026*, pp. 18776–18807. DOI: [10.18653/v1/2026.findings-acl.937](https://doi.org/10.18653/v1/2026.findings-acl.937)
  * 公開模型與語料：[Hugging Face / MaLA-LM/emma-500](https://huggingface.co/collections/MaLA-LM/emma-500)、[Hugging Face / MaLA-LM/mala-bilingual-translation-corpus](https://huggingface.co/datasets/MaLA-LM/mala-bilingual-translation-corpus)、[GitHub / MaLA-LM/emma-500](https://github.com/MaLA-LM/emma-500)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026-data-centric-continual-pretraining-ji.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-data-centric-continual-pretraining-ji.md](../evidence/2026-data-centric-continual-pretraining-ji.md)
