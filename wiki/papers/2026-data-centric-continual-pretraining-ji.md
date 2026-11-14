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

> 「僅靠單語網頁語料難以撐起低資源語言的跨語言表徵對齊；把平行翻譯句對併入持續預訓練混合配方，才是擴大語言覆蓋版圖的實質槓桿。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Ji、Li、Paavola、Luo（University of Helsinki / ELLIS Institute Finland / University of Turku）與 Tiedemann，*Findings of the Association for Computational Linguistics: ACL 2026*，pp. 18776–18807（DOI: `10.18653/v1/2026.findings-acl.937`）。研究建置 2,507 對語言之 MaLA 雙語翻譯語料庫，於 Llama 3 與 Llama 3.1（8B）進行不修改分詞器之全參數持續預訓練，並在 7 項任務、12 個基準評估四款 EMMA-500 模型。

---

## Card 1 ｜ 時代銘文 (The Hook)

大語言模型雖已推動高資源語言的自然語言處理進展，卻往往因預訓練覆蓋不足而難以為低資源與瀕危語言提供穩健理解與翻譯（§1, p. 18776）。既有大規模持續預訓練（Continual Pre-training, CPT）研究中，LLaMAX 同時納入單語與平行資料但僅涵蓋百餘種語言，初代 EMMA-500 則雖擴展至 500 餘種語言，卻純以單語文本為訓練來源（§1, p. 18776）。在「超過 500 種語言」的極端多語規模下，雙語平行翻譯資料究竟能為全參數持續預訓練帶來多少實質增益，而經過海量高資源語料充分訓練的現代英語導向基座（Llama 3 / 3.1）又會如何回應大規模多語適應，始終缺乏嚴謹的受控消融。

由赫爾辛基大學與 ELLIS Institute Finland 團隊發表的本篇研究，透過「以資料為核心（Data-Centric）」的實驗設計正面回應此問題：作者編纂並開源超過 500 種語言、2,507 個語言對的 **MaLA 雙語翻譯語料庫**，在不更動原有分詞器的前提下對 Llama 3 與 Llama 3.1（8B）執行單語與雙語對照之**全參數持續預訓練**，訓練四款 EMMA-500 模型並於 7 項任務、12 個基準完成系統評估，揭示雙語資料帶來大幅翻譯躍升，也量測出高度過預訓練基座的適應代價（摘要 p. 18776；§2–§3, pp. 18777–18784）。

---

## Card 2 ｜ 世紀瓶頸：單語混編欠對齊與高資源飽和基座的抗拒 (The Dilemma)

研究團隊指出，把大規模英語主力基座擴展至 500 餘種低資源語言時面臨三層結構瓶頸（§1–§3, pp. 18776–18783）：

* **單語混合缺乏顯式跨語對齊訊號**：單純餵入各語言獨立爬取的單語網頁文本（即單語混合配方），雖然能擴增詞彙暴露，卻缺乏語意對應錨點，低資源翻譯與跨語遷移幅度有限（§2.2, p. 18779；Table 3, p. 18782）。
* **平行資料呈現劇烈長尾與短句碎片化**：既有公開平行翻譯語料絕大多數為單句對齊而欠缺長篇文件對齊；若將平行句對直接拆分成獨立單語字串進行訓練，過去研究（Lu et al., 2024）已顯示會折損翻譯表現，而各語言資料量本身又懸殊極大（Table 1 顯示 909 對屬於 <1M tokens 的極低資源級別）（§2.1–§2.2, pp. 18778–18779）。
* **過度預訓練基座的適應阻力與損失震盪**：相較早期以 2T tokens 訓練的 Llama 2，經過逾 15T tokens 充分優化的 Llama 3 與 Llama 3.1 具備更強的語言固化性；沿用原始 `0.0003` 學習率在持續預訓練前 5,000 步即出現急速損失尖峰（fast spikes），且續訓後高資源語言與部分通用基準更易出現退化（§2.3, p. 18780；§3.3, p. 18782）。

---

## Card 3 ｜ 突破原理：MaLA 雙語翻譯語料庫與全參數對照持續預訓練 (The Secret)

本研究全文聚焦語料建構、混合配方設計與全參數持續預訓練之實證評測，並未提出額外的模型層級數學公式。核心工程方法由三道環節組成：

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

## Card 4 ｜ 決定性數據：7 任務 12 基準與跨語資源分級結果 (The Evidence)

### MaLA 雙語翻譯語料庫規模比較（Table 1, p. 18778）
* **語言對與詞元總量**：MaLA（**2,507 對** / **`4.3E+11` tokens**）與 Lego-MT（2,508 對 / `2.2E+11`）、NLLB（2,509 對 / `2.8E+11`）語言對相近但詞元總量顯著更高；依資源分層為 very high 4 對（>10B）、high 83 對（>1B）、medium-high 67 對（>500M）、medium 281 對（>100M）、medium-low 508 對（>10M）、low 655 對（>1M）、very low **909 對**（<1M）。

### FLORES-200 機器翻譯與低資源比較（Table 11, p. 18798；Table 3, p. 18782；Table 4, p. 18783）

| 模型 | 訓練配方 | FLORES 全語言 Eng→X (chrF++ / BLEU) | FLORES 全語言 X→Eng (chrF++ / BLEU) | 低資源 Eng→X (chrF++ / BLEU) | 低資源 X→Eng (chrF++ / BLEU) |
|---|---|---:|---:|---:|---:|
| `Llama 3 8B` | 原型基座 | 24.08 / 9.93 | 43.72 / 23.78 | 25.84 / 10.51 | 45.72 / 25.49 |
| `EMMA-500 Llama 3 8B Mono` | 單語混合（419B） | 38.34 / 20.33 | 50.86 / 30.38 | 41.29 / 22.03 | 53.16 / 32.55 |
| **`EMMA-500 Llama 3 8B Bi`** | **雙語混合（671B）** | **42.15 / 24.02** | **54.33 / 34.40** | **45.22 / 25.99** | **56.69 / 36.72** |
| `Llama 3.1 8B` | 原型基座 | 24.69 / 10.11 | 44.10 / 24.19 | 26.46 / 10.66 | 46.13 / 25.91 |
| `EMMA-500 Llama 3.1 8B Mono` | 單語混合（419B） | 37.41 / 19.44 | 48.12 / 27.57 | 40.32 / 21.06 | 50.34 / 29.51 |
| `EMMA-500 Llama 3.1 8B Bi` | 雙語混合（671B） | 42.07 / 23.86 | 53.49 / 33.64 | 45.07 / 25.80 | 55.84 / 35.91 |

* **跨模型競爭力排名（Table 4, p. 18783）**：在 FLORES-200 204 語言對上，`EMMA-500 Llama 3 8B Bi` 有 **88.18%** 語言進入所有受測模型前 3 名、**98.52%** 進入前 5 名，**100.00%** 進入前 10 名（原基座 `Llama 3 8B` 分別僅為 `0.00% / 0.00% / 25.12%`）。

### 分類、理解、常識推理與適應性代價（Table 3, p. 18782；Fig. 3 & Table 5, p. 18783；Table 10, p. 18797）
1. **分類基準呈分化表現**：在覆蓋 1,502 種語言的 Taxi1500 低資源子集，`EMMA-500 Llama 3 8B Bi` 達 **26.72%** 準確率（全組最高，全語言均分 **25.13%**）；然於 SIB-200 低資源子集，該變體自基座 `65.53%` 滑落至 `39.65%`（全語言平均從 `63.70%` 降至 `39.40%`），同系列僅 `EMMA-500 Llama 3.1 8B Bi` 守住 `63.33%`（全語言 `62.07%`）。
2. **常識推理穩定成長**：在 XCOPA 與 XStoryCloze 上，`EMMA-500 Llama 3.1 8B Bi` 分別達到 **67.25%** 與 **68.47%**（較 Llama 3.1 基座 `61.71%` 與 `63.58%` 提升逾 4.8–5.5 個百分點）。
3. **高資源閱讀退化與基座阻力（Table 5 & Fig. 3）**：在 BELEBELE（Table 5）中，`EMMA-500 Llama 3 8B Bi` 在低資源語言獲益（喀爾喀蒙古語 `khk_Cyrl` `+4.22` 至 `39.33%`、北索托語 `nso_Latn` `+6.00` 至 `35.22%`），高資源語言卻大幅遺忘（英語 `eng_Latn` 自 `74.56%` 降至 `56.78%`、`Δ = -17.78`）。從退化基準總數來看（Fig. 3），Llama 2 Mono 平均僅在 **2** 個基準遜於基座，而 Llama 3 Mono/Bi 增至 **7 / 5** 個，Llama 3.1 Mono/Bi 更達 **6 / 9** 個基準。

---

## Card 5 ｜ 典範轉移：開源五百語資產、實驗取捨與未解邊界 (The Revolution)

### 本篇公開資源與可重現架構（Abstract, p. 18776）
* **MaLA 雙語翻譯語料庫**：釋出標準化 2,507 對多語平行資料集 `MaLA-LM/mala-bilingual-translation-corpus`。
* **EMMA-500 Llama 3 系列四款 8B 模型與程式碼庫**：公開發布於 Hugging Face `MaLA-LM/emma-500` 與 GitHub `MaLA-LM/emma-500`，專案網站匯整分語言完整評測結果（`https://mala-lm.github.io/emma-500-gen2.html`）。

### 作者明列之研究限制與開放挑戰（Limitations, pp. 18784–18785）
1. **數學與深度閱讀理解仍脆弱**：MGSM 與 BELEBELE（尤其機器翻譯版題庫）得分仍弱，單靠雙語持續預訓練在 8B 規模不足以撐起跨語言深層推理與數學解題（p. 18784；§D.7–D.8）。
2. **受限算力之混合比例與步數妥協**：儘管總算力達 800k GPU 小時，團隊仍無法對資料混合權重與學習率進行網格搜尋；因維持 1 epoch，雙語（671B tokens）與單語（419B tokens）訓練總步數亦不等長（§2.3, p. 18780；Limitations, p. 18785）。
3. **尚未具備實務部署安全性**：四款模型僅完成持續預訓練，尚未經歷人類偏好對齊（RLHF/DPO）或對抗性紅隊測試，作者明言目前不可直接用於實際應用部署（Limitations, pp. 18784–18785）。

---

## Card 6 ｜ KAIROS：大規模多語資料工程與過飽和基座的結構張力 (Cross-Disciplinary Inspiration)

> **本段為 Wiki 詮釋與跨領域啟發分析**：以下聯繫低資源機器翻譯與模型擴展實務，屬知識庫策展詮釋，非原論文作者所主張。

1. **平行句對是低資源全參數續訓的關鍵訊號，但必須尊重超參數敏感度**：在[低資源神經機器翻譯](../concepts/low-resource-machine-translation.md)領域，許多模型擴充方案常將焦點放在詞表擴增或 LoRA 微調。本篇清楚顯示：在不更動分詞器的全參數持續預訓練下，只要將雙語句對按偽文件形式與高質單語、程式碼與論文混編並把學習率下調至 `0.0001`，即便僅是 8B 模型也能在超過兩百種語言翻譯上實現結構性躍遷；反之，若沿用高資源基座原本的較大學習率，極易在初期便觸發數值尖峰與表徵震盪。
2. **高資源「過度預訓練」揭示有限參數的零和擠壓**：Llama 3 / 3.1 在導入 500 餘種語言後展現的 BELEBELE 英語退化（`-17.78` 分）與 SIB-200 分化，映照出密集單一矩陣模型（Dense Transformer）在「高資源專精」與「長尾多語覆蓋」之間的容量張力。這也正好與跨語言混合專家（MoE）路由對齊等路線形成互補——究竟該透過更豐富的雙語平行資料配方、還是結合稀疏條件路由保留語言邊界，成為低資源多語基礎模型下一階段的核心設計命題。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Ji, S., Li, Z., Paavola, J., Luo, H., & Tiedemann, J. (2026). Data-Centric Continual Pre-training for 500+ Languages: A New Bilingual Translation Corpus and Multilingual Models. *Findings of the Association for Computational Linguistics: ACL 2026*, pp. 18776–18807. DOI: [10.18653/v1/2026.findings-acl.937](https://doi.org/10.18653/v1/2026.findings-acl.937)
  * 公開模型與語料：[Hugging Face / MaLA-LM/emma-500](https://huggingface.co/collections/MaLA-LM/emma-500)、[Hugging Face / MaLA-LM/mala-bilingual-translation-corpus](https://huggingface.co/datasets/MaLA-LM/mala-bilingual-translation-corpus)、[GitHub / MaLA-LM/emma-500](https://github.com/MaLA-LM/emma-500)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026-data-centric-continual-pretraining-ji.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-data-centric-continual-pretraining-ji.md](../evidence/2026-data-centric-continual-pretraining-ji.md)
