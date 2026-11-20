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
focus_role: "taiwan-research"
focus_tags: ["llm-assisted"]
focus_direction: "linguistics-eval"
focus_languages: ["阿美語", "泰雅語", "排灣語"]
doi_url: "https://doi.org/10.18653/v1/2025.findings-emnlp.897"
hook: "首個涵蓋阿美語、泰雅語、排灣語的多任務基準，評測機器翻譯、語音辨識與摘要：現有大型語言模型在三項任務上都表現很差，10-shot 與微調只帶來有限改善，語音辨識微調後改善最明顯。"
card_line: "出一套族語考題，測大型語言模型懂多少"
---

# FormosanBench：大型語言模型時代的低資源南島語言評測基準 (FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models)

**2025 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Lin、Chen（中央研究院語言學研究所）與 Zhang（University of Hawaii at Manoa），*Findings of EMNLP 2025*, pp. 16527–16539。資料與程式碼公開於 GitHub（HsiYuGit/FormosanBench）。

---

## Card 1 ｜ 一句話看懂
這篇做了一套考大型語言模型的「族語考題」FormosanBench：用阿美語、泰雅語、排灣語三種語言，測機器翻譯、語音辨識與文本摘要三項任務，並比較零樣本、10 個範例與微調三種設定（摘要；§1, p. 16527）。結果三項都不理想：零樣本翻譯分數幾乎為 0，微調後的翻譯仍多半錯；語音辨識微調後改善最多，但仍未達實用（§6；§7）。作者稱其為第一個評估大型語言模型在低資源南島語言上表現的多任務基準。

* **語言**：阿美語、泰雅語、排灣語（選擇依據為合計使用人口超過 10 萬、有既有數位資源、在南島語系內具語言多樣性；§4, p. 16529）
* **任務**：機器翻譯（族語↔華語）、語音辨識、文本摘要
* **方法**：建立三項任務的評測資料，比較多種大型語言模型、翻譯與語音模型（§4–§5）
* **資料**：翻譯取自原住民族語言線上辭典、語音取自族語 E 樂園教材錄音、摘要取自族語維基百科（§4，表 1）
* **公開**：資料與程式碼公開於 GitHub（HsiYuGit/FormosanBench，p. 16527）
* **出處**：Lin、Chen（中央研究院語言學研究所）與 Zhang（University of Hawaii at Manoa），*Findings of EMNLP 2025*, pp. 16527–16539

---

## Card 2 ｜ 要解決的問題
* **語態罕見**：臺灣南島語多為動詞居首，並有類型學上罕見的語態系統。例如排灣語的「Zepulj 吃地瓜」可依動詞標記主事或受事語態而有多種句法實現，名詞組的格標記與位置也隨之改變（§2，圖 1, p. 16528）。
* **只做翻譯**：既有研究（如 Liao 2023、Zheng et al. 2024）集中在機器翻譯與傳統序列模型，沒有研究系統性評估當代大型語言模型在多項任務上的能力（§3, p. 16529）。
* 原文沒有測量或討論分詞器（tokenizer）將族語詞切碎的程度；本頁不作此主張。

這篇的想法：建一套跨任務的族語評測，檢驗大型語言模型到底懂多少。

---

## Card 3 ｜ 方法流程
原文無編號公式，BLEU、WER、ROUGE 僅引用未列式（§5.3）。

1. **選語言**：依使用人口、既有數位資源與語言多樣性選出阿美語、泰雅語、排灣語（§4, p. 16529）。
2. **建三項任務的資料**（§4，表 1, pp. 16529–16530）——三項任務的資料**分別來自不同來源**，不是同一組資料的多種標注：

| 任務 | 來源 | 規模（訓練／驗證／測試） |
|---|---|---|
| 機器翻譯（族語↔華語） | 原住民族語言線上辭典，經 FormosanBank 前處理 | 每語約 5,000 句對（阿美語 3,259／543／1,631） |
| 語音辨識 | FormosanBank 收錄之族語 E 樂園教材錄音；方言為海岸阿美語、賽考利克泰雅語、中排灣語 | 阿美語 2,567／425／1,288 |
| 摘要 | 族語維基百科條目：以首段作為摘要、其餘內文作為輸入 | 阿美語 77／21／41、泰雅語 672／116／299 |

   翻譯資料沒有英語譯文。原文稱各語言依 70:10:20 切分（p. 16531），但表 1 的數字（如阿美語 3,259／543／1,631）約為 60:10:30（依原文數據計算）。
3. **選模型與設定**（§5, pp. 16530–16532）：翻譯與摘要用 Mistral-7B、Gemma-1.1-7B、LLaMA-3.1（8B、70B）、NLLB、GPT-4o 等；翻譯以 Mistral-7B v0.3 與 NLLB 做 10-shot 與 LoRA 微調；摘要以 GPT-4o、Mistral、LLaMA 3.1 8B 做 10-shot，後兩者另做微調。語音辨識用 Whisper、SeamlessM4T、MMS-1b-all，只微調 Whisper；MMS 需指定語言，因泰雅語與排灣語不在其預訓練語料中，一律指定為阿美語。
4. **評分與人工檢視**（§5.3, p. 16532）：翻譯用 BLEU、語音辨識用 WER、摘要用 ROUGE-2／ROUGE-L；另以 GPT-4o-mini 作為評審（1–5 分；摘要依 G-Eval 四個面向），並請母語者檢視輸出。原文未使用 chrF++ 或 SBERT。

```text
[原住民族語言線上辭典] ──► 翻譯資料（族語↔華語）──► zero-shot／10-shot／LoRA 微調（Mistral、NLLB 等）──► BLEU、LLM 評審、人工檢視
[族語 E 樂園教材錄音] ──► 語音辨識資料 ──► Whisper／Seamless／MMS（微調 Whisper）──► WER
[族語維基百科] ──► 摘要資料（首段＝摘要）──► 10-shot／微調 ──► ROUGE、G-Eval
```

---

## Card 4 ｜ 資料與實驗
* **翻譯**：原住民族語言線上辭典例句，每語約 5,000 句對，族語↔華語，無英語譯文（表 1）。
* **語音辨識**：族語 E 樂園教材錄音；海岸阿美語、賽考利克泰雅語、中排灣語（§4）。
* **摘要**：族語維基百科條目，阿美語只有 77／21／41 篇，泰雅語 672／116／299 篇（表 1）。
* **比較方式**：零樣本、10 個範例、微調三種設定；多種大型語言模型與專門翻譯、語音模型（§5）。
* **評分方式**：BLEU、WER（錯字率，越低越好）、ROUGE；GPT-4o-mini 評審；母語者人工檢視（§5.3）。

---

## Card 5 ｜ 結果

### 機器翻譯（表 2–3, pp. 16532–16534）
* Zero-shot 下所有模型的 BLEU 都接近 0，包括 GPT-4o 系列；族語→華語三種語言全為 0。
* 最佳結果來自微調後的 NLLB，例如華語→阿美語 0.1506、華語→泰雅語 0.1137、排灣語→華語 0.0759。表 2 的 BLEU 看來以 0–1 尺度表示（0.1506 約相當於常見 0–100 尺度的 15.06；Wiki 推論）。作者表示只有 NLLB 微調的部分結果略高於 Zheng et al. (2024) 的基線（圖 5）。
* **人工檢視微調後 NLLB 的翻譯輸出**：排灣語估計不到 40% 的輸出傳達有意義的內容；泰雅語完全正確的句子少於 10%，許多泰雅語名詞甚至動詞被譯成「子」或「草」；阿美語常出現看似合理、實際沒有詞根的詞（§6.1，p. 16533）。
* **LLM 評審**（表 3）：族語→華語 1.08–1.43 分，華語→族語 1.55–1.91 分。原文據此稱「譯入族語比譯出更難」，但表中譯入族語的分數反而較高，原文的解讀與數字方向不一致。

### 語音辨識（表 4, p. 16534）
* Zero-shot 以 MMS 最佳（阿美語 WER 0.522，泰雅語 0.937，排灣語 0.893）；微調 Whisper 後降至 0.296／0.315／0.373。

### 摘要（§6.3，表 5–6, pp. 16534–16535）
* Zero-shot 的 ROUGE 普遍低於 20，輸出常夾雜華語。Mistral 與 LLaMA 經 10-shot 或微調後，ROUGE 在多數語言反而下降。
* GPT-4o 在 10-shot 下對泰雅語（ROUGE-2／L 38.36／50.41）與阿美語明顯改善，但人工檢視發現事實錯誤，作者認為改善多來自表面模式的複製，而非真正理解。

### 作者結論（§7）
臺灣南島語仍是當前大型語言模型的明顯盲點；翻譯與摘要結果顯示模型缺乏對這些語言的理解，常產生與輸入無關的輸出；語音辨識相對較好但仍未達實用；調適使語音辨識 WER 大幅下降，翻譯 BLEU 的改善則很有限。

---

## Card 6 ｜ 限制與可用性
* **作者說的限制**：只涵蓋少數語言與任務，擴充需大量人工標注（Limitations）。
* **讀的時候要留意**：表 2 的 BLEU 為 0–1 尺度，和其他論文比較時要換算；表 1 的切分比例與內文不一致；LLM 評審的解讀與分數方向不一致（見 05）。翻譯資料同樣來自線上辭典例句，若自己的系統也用辭典資料，需檢查訓練與測試是否重疊（Wiki 註記）。作者指出資料量是主要瓶頸（§6.1），並未提出構詞解析或檢索增強生成等具體解法。
* **公開程度**：資料與程式碼公開於 GitHub（HsiYuGit/FormosanBench，p. 16527）。
* **適合拿來報告的點**：用公開資料一次測三項任務、三種設定，人工檢視又具體指出錯誤類型（虛構詞根、名詞動詞被譯成「子」或「草」），適合拿來說明大型語言模型在族語上的現況（Wiki 詮釋）。

### 延伸想法
以下為延伸思考（Wiki 推測），不是原文主張。

1. **可作為外部評測資料**：FormosanBench 的泰雅語、排灣語翻譯測試集公開，可用來與 Zheng et al. (2024) 等結果比較；但需先檢查與自己訓練資料是否重疊（參見廖恒慶 2023 的覆蓋度分析）。
2. **人工檢視揭示的錯誤類型**：母語者指出的問題——詞彙缺口、虛構詞根、動詞構詞與格標記誤譯——正是構詞資訊與詞典檢索可能幫上忙的地方。是否真的有效，需在相同測試集上實驗驗證。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Lin, K. K., Chen, H., & Zhang, H. (2025). FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models. In *Findings of the Association for Computational Linguistics: EMNLP 2025* (pp. 16527-16539). DOI: [10.18653/v1/2025.findings-emnlp.897](https://doi.org/10.18653/v1/2025.findings-emnlp.897)
  * 原始檔典藏：`raw/my-focus/台灣相關論文/FormosanBench Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models _ 2025.findings-emnlp.897.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2025-formosanbench-llm-benchmark-lin.md](../evidence/2025-formosanbench-llm-benchmark-lin.md)
