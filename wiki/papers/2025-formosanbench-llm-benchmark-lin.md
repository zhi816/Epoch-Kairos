---
title: "FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models"
title_zh: "FormosanBench：大型語言模型時代的低資源南島語言評測基準"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Kaiying Kevin Lin, Hsiyu Chen, Haopeng Zhang"
venue: "Findings of the Association for Computational Linguistics: EMNLP 2025, 16527-16539"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#人工智慧"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "published"
verification: "verified"
my_focus: true
focus_role: "international"
focus_languages: ["阿美語", "泰雅語", "排灣語"]
doi_url: "https://doi.org/10.18653/v1/2025.findings-emnlp.897"
hook: "首個涵蓋阿美語、泰雅語、排灣語的多任務基準，評測機器翻譯、語音辨識與摘要：現有大型語言模型在三項任務上都表現很差，10-shot 與微調只帶來有限改善，語音辨識微調後改善最明顯。"
card_line: "出一套族語考題，測大型語言模型懂多少"
---

# FormosanBench：大型語言模型時代的低資源南島語言評測基準 (FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models)

> 「評測基準是一面鏡子：它照出的不是模型能做什麼，而是我們還沒為哪些語言做好準備。」（本頁引言為 Wiki 撰寫，非原文）

**2025 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Lin、Chen（中央研究院語言學研究所）與 Zhang（University of Hawaii at Manoa），*Findings of EMNLP 2025*, pp. 16527–16539。資料與程式碼公開於 GitHub（HsiYuGit/FormosanBench）。

---

## Card 1 ｜ 時代銘文 (The Hook)
作者推出 FormosanBench，稱其為第一個評估大型語言模型在低資源南島語言上表現的多任務基準，涵蓋三種瀕危的臺灣南島語——阿美語、泰雅語、排灣語——與三項任務：機器翻譯、自動語音辨識、文本摘要；並在 zero-shot、10-shot 與微調三種設定下評估（摘要；§1, p. 16527）。三種語言的選擇依據為：合計使用人口超過 10 萬、有既有數位資源、在南島語系內具語言多樣性（§4, p. 16529）。

---

## Card 2 ｜ 世紀瓶頸：語言結構特殊，評測與資料都不足 (The Dilemma)
* **語態系統罕見**：臺灣南島語多為動詞居首，並有類型學上罕見的語態系統。例如排灣語的「Zepulj 吃地瓜」可依動詞標記主事或受事語態而有多種句法實現，名詞組的格標記與位置也隨之改變（§2，圖 1, p. 16528）。
* **先前研究只做翻譯**：既有研究（如 Liao 2023、Zheng et al. 2024）集中在機器翻譯與傳統序列模型，沒有研究系統性評估當代大型語言模型在多項任務上的能力（§3, p. 16529）。
* 原文沒有測量或討論分詞器（tokenizer）將族語詞切碎的程度；本頁不作此主張。

---

## Card 3 ｜ 突破架構與原理：三項任務、三個獨立資料來源 (The Secret)

### 1. 資料（§4，表 1, pp. 16529–16530）
三項任務的資料**分別來自不同來源**，不是同一組資料的多種標注：
| 任務 | 來源 | 規模（訓練／驗證／測試） |
|---|---|---|
| 機器翻譯（族語↔華語） | 原住民族語言線上辭典，經 FormosanBank 前處理 | 每語約 5,000 句對（阿美語 3,259／543／1,631） |
| 語音辨識 | FormosanBank 收錄之族語 E 樂園教材錄音；方言為海岸阿美語、賽考利克泰雅語、中排灣語 | 阿美語 2,567／425／1,288 |
| 摘要 | 族語維基百科條目：以首段作為摘要、其餘內文作為輸入 | 阿美語 77／21／41、泰雅語 672／116／299 |

翻譯資料沒有英語譯文。原文稱各語言依 70:10:20 切分（p. 16531），但表 1 的數字（如阿美語 3,259／543／1,631）約為 60:10:30（依原文數據計算）。

### 2. 模型與設定（§5, pp. 16530–16532）
* **翻譯與摘要**：Mistral-7B、Gemma-1.1-7B、LLaMA-3.1（8B、70B）、NLLB、GPT-4o 等。翻譯以 Mistral-7B v0.3 與 NLLB 做 10-shot 與 LoRA 微調；摘要以 GPT-4o、Mistral、LLaMA 3.1 8B 做 10-shot，後兩者另做微調。
* **語音辨識**：Whisper、SeamlessM4T、MMS-1b-all；只微調 Whisper。MMS 需指定語言，因泰雅語與排灣語不在其預訓練語料中，一律指定為阿美語。

### 3. 評估指標（§5.3, p. 16532）
翻譯用 BLEU、語音辨識用 WER、摘要用 ROUGE-2／ROUGE-L；另以 GPT-4o-mini 作為評審（1–5 分；摘要依 G-Eval 四個面向），並請母語者檢視輸出。原文未使用 chrF++ 或 SBERT。

```text
[原住民族語言線上辭典] ──► 翻譯資料（族語↔華語）──► zero-shot／10-shot／LoRA 微調（Mistral、NLLB 等）──► BLEU、LLM 評審、人工檢視
[族語 E 樂園教材錄音] ──► 語音辨識資料 ──► Whisper／Seamless／MMS（微調 Whisper）──► WER
[族語維基百科] ──► 摘要資料（首段＝摘要）──► 10-shot／微調 ──► ROUGE、G-Eval
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 機器翻譯（表 2–3, pp. 16532–16534）
* Zero-shot 下所有模型的 BLEU 都接近 0，包括 GPT-4o 系列；族語→華語三種語言全為 0。
* 最佳結果來自微調後的 NLLB，例如華語→阿美語 0.1506、華語→泰雅語 0.1137、排灣語→華語 0.0759。表 2 的 BLEU 看來以 0–1 尺度表示（0.1506 約相當於常見 0–100 尺度的 15.06；Wiki 推論）。作者表示只有 NLLB 微調的部分結果略高於 Zheng et al. (2024) 的基線（圖 5）。
* **人工檢視**：排灣語估計不到 40% 的輸出傳達有意義的內容；泰雅語完全正確的句子少於 10%，許多泰雅語名詞甚至動詞被譯成「子」或「草」；阿美語常出現看似合理、實際沒有詞根的詞（p. 16533）。
* **LLM 評審**（表 3）：族語→華語 1.08–1.43 分，華語→族語 1.55–1.91 分。原文據此稱「譯入族語比譯出更難」，但表中譯入族語的分數反而較高，原文的解讀與數字方向不一致。

### 語音辨識（表 4, p. 16534）
* Zero-shot 以 MMS 最佳（阿美語 WER 0.522，泰雅語 0.937，排灣語 0.893）；微調 Whisper 後降至 0.296／0.315／0.373。

### 摘要（§6.3，表 5–6, pp. 16534–16535）
* Zero-shot 的 ROUGE 普遍低於 20，輸出常夾雜華語。Mistral 與 LLaMA 經 10-shot 或微調後，ROUGE 在多數語言反而下降。
* GPT-4o 在 10-shot 下對泰雅語（ROUGE-2／L 38.36／50.41）與阿美語明顯改善，但人工檢視發現事實錯誤，作者認為改善多來自表面模式的複製，而非真正理解。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **作者結論**（§7）：臺灣南島語仍是當前大型語言模型的明顯盲點；翻譯與摘要結果顯示模型缺乏對這些語言的理解，常產生與輸入無關的輸出；語音辨識相對較好但仍未達實用；調適使語音辨識 WER 大幅下降，翻譯 BLEU 的改善則很有限。
* **作者自述的限制**：只涵蓋少數語言與任務，擴充需大量人工標注（Limitations）。
* （Wiki 詮釋）作者指出資料量是主要瓶頸（§6.1），並未提出構詞解析或 RAG 等具體解法；這些方向需要另外的研究支持。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **可作為外部評測資料**：
   * FormosanBench 的泰雅語、排灣語翻譯測試集公開，可用來與本文及 Zheng et al. (2024) 的結果比較。但翻譯資料同樣來自線上辭典例句，若我的系統也使用辭典資料，需檢查訓練與測試是否重疊（參見廖恒慶 2023 的覆蓋度分析）。
2. **人工檢視揭示的錯誤類型**：
   * 本文母語者指出的問題——詞彙缺口、虛構詞根、動詞構詞與格標記誤譯——正是構詞資訊與詞典檢索可能幫上忙的地方。是否真的有效，需在相同測試集上實驗驗證。
3. **注意分數尺度**：
   * 比較不同論文的 BLEU 時，須確認尺度（0–1 或 0–100）與分詞方式是否一致。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Lin, K. K., Chen, H., & Zhang, H. (2025). FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models. In *Findings of the Association for Computational Linguistics: EMNLP 2025* (pp. 16527-16539). DOI: [10.18653/v1/2025.findings-emnlp.897](https://doi.org/10.18653/v1/2025.findings-emnlp.897)
  * 原始檔典藏：`raw/my-focus/英文論文/FormosanBench Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models _ 2025.findings-emnlp.897.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2025-formosanbench-llm-benchmark-lin.md](../evidence/2025-formosanbench-llm-benchmark-lin.md)
