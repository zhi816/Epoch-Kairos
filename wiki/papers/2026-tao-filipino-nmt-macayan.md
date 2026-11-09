---
title: "Tao–Filipino Neural Machine Translation: Strategies for Ultra–Low-Resource Settings"
title_zh: "達悟語－菲律賓語神經機器翻譯：極低資源情境下的策略"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Adrian Denzel Macayan, Luis Andrew Madridijo, Ellexandrei Esponilla, Zachary Mitchell Francisco"
venue: "Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026), 27-36"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
verification: "verified"
my_focus: true
focus_role: "report"
focus_languages: ["達悟語"]
doi_url: "https://doi.org/10.18653/v1/2026.loresmt-1.2"
hook: "以 NLLB-200（600M）做達悟語→菲律賓語翻譯：先以同屬巴丹語群的伊巴丹語預訓練，聖經域內 BLEU 最高（34.85）；加入由辭典例句轉譯的合成會話資料，則改善域外會話的表現。"
---

# 達悟語－菲律賓語神經機器翻譯：極低資源情境下的策略 (Tao–Filipino Neural Machine Translation: Strategies for Ultra–Low-Resource Settings)

> 「當一種語言只剩下聖經譯本與辭典，翻譯系統就得從這些靜態檔案中學會日常對話。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Macayan, Madridijo, Esponilla & Francisco（De La Salle University–Manila），*LoResMT 2026*, pp. 27–36。實驗方向為達悟語→他加祿語（Tagalog，即菲律賓語之基礎）。

---

## Card 1 ｜ 時代銘文 (The Hook)
達悟語（Tao，又稱雅美語）通行於蘭嶼。原文指出，雖然地理上接近臺灣本島，達悟語在系譜上屬於**馬來－玻里尼西亞語族的巴丹語群**，「而非臺灣南島語（Formosan languages）」；類型上屬菲律賓型語言，動詞居首，有豐富的黏著構詞與焦點系統（§3, p. 30）。本文研究如何在監督資料極少的情況下，以 NLLB-200（600M 參數）建立達悟語→他加祿語翻譯系統，結合領域微調、合成資料與跨語言遷移（摘要）。

---

## Card 2 ｜ 世紀瓶頸：只有聖經與辭典 (The Dilemma)
* **平行語料以聖經為主**：主要平行資料是達悟語新約聖經（*Seysyo No Tao*）與他加祿語聖經的經文對齊，另有 Rau & Dong (2006) 收錄的文本（§3–§4.1）。
* **聖經偏誤**：只用聖經訓練，模型會偏向古老的句構與用詞，作者稱之為「禮儀偏誤」（liturgical bias），難以處理日常會話（§2, §4.4）。
* **NLLB 沒有巴丹語**：NLLB-200 預訓練含他加祿語、伊洛卡諾語等菲律賓語言，但沒有任何巴丹語群語言（§4.6）。

---

## Card 3 ｜ 突破架構與原理：三個模型的比較 (The Secret)

### 1. 三個模型（§4.5–4.6, pp. 31–32）
| 模型 | 訓練資料 |
|---|---|
| Model 1 | 只用達悟語－他加祿語聖經平行語料（10,498 句） |
| Model 2 | 聖經＋合成會話資料：原住民族語言研究發展基金會辭典中的達悟語－華語例句（3,966 句），以 Google 翻譯把華語轉成他加祿語；複製 3 倍（11,898 句）使數量與聖經相當，並與聖經資料打散混合 |
| Model 3 | 先以**伊巴丹語→他加祿語**（同屬巴丹語群）預訓練 NLLB-200，再以聖經與合成資料微調達悟語→他加祿語 |

* 作者以表 2 說明，NLLB-200 自身的華語→他加祿語翻譯品質很差（如把「坐下。」原樣輸出），因此改用 Google 翻譯產生合成資料（§4.4）。
* 原文**沒有**在目標函數中加入參數距離懲罰項，也**沒有**訓練構詞感知的子詞分詞器：作者明言因時間限制使用 NLLB-200 的預設分詞器，並把子詞與構詞處理列為未來工作（§7、Limitations, p. 34）。

### 2. 前處理與評估（§3–§4.3）
文字轉小寫、統一空白，經文長度上限 128 個詞元。測試集分兩部分：從聖經隨機抽 200 組（域內），以及從 Rau & Dong (2006) 人工整理、以同源詞比對驗證的 20 組會話句（域外，稱為 Validation 或 Cognate Challenge Set）。指標為 BLEU、chrF（文中寫 chrF++）與 SBERT 中位數。

```text
Model 1：[達悟語－他加祿語聖經] ──────────────────────────────────► NLLB-200 微調
Model 2：[聖經] ＋ [辭典例句：達悟語－華語 ──Google 翻譯──► 達悟語－他加祿語（×3）] ──► NLLB-200 微調
Model 3：[伊巴丹語－他加祿語聖經] ──► 預訓練 NLLB-200 ──► 再以 Model 2 的資料微調
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 達悟語→他加祿語（表 3, p. 33）
| 指標 | Model 1 聖經／域外 | Model 2 聖經／域外 | Model 3 聖經／域外 |
|---|---|---|---|
| BLEU | 32.00／3.12 | 30.97／**6.67** | **34.85**／3.64 |
| chrF | 56.26／28.28 | 55.16／**34.01** | **58.36**／32.29 |
| SBERT 中位數 | 92.26／**82.77** | **92.55**／79.80 | 90.54／77.94 |

* **遷移學習**：Model 3 在聖經域內最好，作者歸因於伊巴丹語與達悟語同屬巴丹語群。
* **合成資料**：Model 2 在聖經上略降，但域外 BLEU 約為 Model 1 的兩倍、chrF 最高。
* **形式偏誤**：Model 3 的域外 SBERT 最低（77.94），作者推測遷移與聖經訓練強化了正式語域。
* 域外測試集只有 20 句，數字波動可能很大（Wiki 註）。

### 原文內部不一致
* 引言與 §3 有幾處寫成「達悟語－英語」翻譯或語料，但實驗與表 3 皆為達悟語－他加祿語。
* 引言與結論稱平行語料少於 5,000 句，但 §4.5 的聖經資料為 10,498 句。
* §5 內文寫 Model 2 域外 BLEU 為 6.61，表 3 為 6.67。
* 相關研究一節引述 FormosanBench（Lin et al. 2025）時，把語言寫成泰雅、賽德克、排灣（實為阿美、泰雅、排灣），並稱大型語言模型在提供詞典定義時展現「顯著的少樣本能力」；FormosanBench 原文並無此結論（見其頁面）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **作者結論**（§6）：平行語料極少時，單靠資料量不夠，利用語言結構與詞彙資源是關鍵；以伊巴丹語遷移最能提高翻譯忠實度，辭典合成資料則能改善泛化。作者建議兩者互補：遷移建立語法骨架，合成資料擴充現代溝通所需的語義範圍。
* **作者自述的限制**：合成資料經機器翻譯產生，仍有偏誤與錯誤；只用 600M 模型與 30 小時 Kaggle GPU；使用預設分詞器；沒有人工評估（Limitations）。
* （Wiki 詮釋）合成資料經「達悟語－華語－他加祿語」轉譯，達悟語端未變，但他加祿語端的品質取決於 Google 翻譯，可能把華語釋義的錯誤帶進訓練資料。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **親屬語言預訓練**：
   * 本文以同屬巴丹語群的伊巴丹語預訓練最有效。對泛泰雅語群而言，三語互為最近的親屬，廖恒慶（2023）的多語言做法即在此方向；而本文與廖恒慶都顯示，與目標語越接近的資料越有幫助。
2. **辭典例句轉成合成資料**：
   * 本文把原民會辭典的族語－華語例句轉成族語－他加祿語。我的研究若做族語－華語翻譯，可直接使用這些例句，不需轉譯；但需注意辭典例句與測試資料的重疊（參見 Zheng et al. 2024 與廖恒慶 2023）。
3. **域外測試與語域**：
   * 本文顯示聖經語料會帶來語域偏誤，且不同模型在域內與域外的排名相反；評估時應同時報告兩者。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Macayan, A. D., Madridijo, L. A., Esponilla, E., & Francisco, Z. M. (2026). Tao–Filipino Neural Machine Translation: Strategies for Ultra–Low-Resource Settings. In *Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026)* (pp. 27-36). DOI: [10.18653/v1/2026.loresmt-1.2](https://doi.org/10.18653/v1/2026.loresmt-1.2)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026.loresmt-1.2.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-tao-filipino-nmt-macayan.md](../evidence/2026-tao-filipino-nmt-macayan.md)
