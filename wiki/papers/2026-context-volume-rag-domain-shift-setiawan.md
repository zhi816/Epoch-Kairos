---
title: "Context Volume Drives Performance: Tackling Domain Shift in Extremely Low-Resource Translation via RAG"
title_zh: "語境容量驅動效能：透過檢索增強生成攻克極低資源機器翻譯之領域偏移"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "David Samuel Setiawan, Raphaël Merx, Jey Han Lau"
venue: "Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026), 87-101"
domain: "ai"
domain_tags: ["#自然語言處理", "#人工智慧", "#深度學習"]
concepts: ["low-resource-machine-translation"]
status: "published"
verification: "verified"
my_focus: true
focus_role: "llm-assisted"
focus_languages: ["達豪語"]
doi_url: "https://doi.org/10.18653/v1/2026.loresmt-1.7"
hook: "墨爾本大學團隊於 LoResMT 2026 以印尼極低資源達豪語（Dhao）攻克領域偏移：結合微調 NMT 初譯與 Gemini 2.5 Flash RAG 後編輯；實證表明檢索範例容量（Context Volume）是效能主驅動力，詞級模糊檢索可在有效容量達 137 句時恢復至接近域內水準（35.21 chrF++）。"
card_line: "讓大模型參考例句，修補跨領域的達豪語翻譯"
---

# 語境容量驅動效能：透過檢索增強生成攻克極低資源機器翻譯之領域偏移 (Context Volume Drives Performance)

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Setiawan, Merx & Lau（墨爾本大學，The University of Melbourne），*LoResMT 2026*, pp. 87–101。以印尼東部極端低資源南島語達豪語（Dhao）的新約至舊約跨領域翻譯為實證對象。

---

## Card 1 ｜ 一句話看懂
這篇處理「只有新約聖經可訓練，卻要翻譯舊約」的領域轉移問題，對象是印尼東部的達豪語（Dhao）。做法是：先用新約微調的小翻譯模型出初稿，再讓大型語言模型參考檢索來的例句與詞典修稿（§4）。舊約測試上 chrF++ 從 27.11 提高到 35.21，接近新約域內的 36.17；作者發現影響最大的是放進提示的例句數量，而非用哪種檢索方法（表 2, p. 91；§6）。

* **語言**：英語 → 達豪語（使用人口不足 5,000 人的南島語言；除新約外幾乎沒有數位資料；§1）
* **任務**：極低資源跨領域機器翻譯（新約 → 舊約）
* **方法**：微調 NLLB-200 初譯 ＋ 檢索例句與詞典 ＋ Gemini 2.5 Flash 後編輯；比較多種檢索方法與例句數量（§4）
* **資料**：達豪語新約聖經（訓練與檢索）、達豪語語法書例句與詞典；舊約創世記作測試（§3）
* **公開**：原文未提供程式碼連結；聖經譯本為 CC BY-ND 4.0，語法書為開放取用出版品（Ethical Considerations）
* **出處**：Setiawan、Merx、Lau（墨爾本大學），*LoResMT 2026*, pp. 87–101

---

## Card 2 ｜ 要解決的問題
全球許多低資源語言只有聖經譯本這一種大規模數位資源，而且大多只完成新約；舊約佔聖經篇幅約 75%，且新舊約的詞彙與風格差異很大（§1, p. 87）。舊約測試集的未登錄詞率達 25.9%，新約驗證集只有 8.1%（摘要；§1）。

* **換領域就崩**：只用新約微調的 NLLB-200（600M）遇到舊約時，spBLEU 從域內的 25.19 跌到 7.66，chrF++ 從 36.17 跌到 27.11；輸出常有重複迴圈與虛構實體（表 1；§5.4）。
* **語法書微調**：直接把語法書例句加進微調（NMT + Grammar），chrF++ 反而由 27.11 降到 26.62；作者推測是語法書生硬的教學句型干擾了模型的風格表徵（表 1；§5.1, p. 89）。
* **大模型不會**：大型語言模型沒見過達豪語，零樣本直接翻譯只有 2.98 spBLEU／18.84 chrF++（表 1）。

這篇的想法：讓小模型出初稿，大模型參考大量檢索例句修稿。

---

## Card 3 ｜ 方法流程
原文無編號公式，等號僅見於參數設定（§5）。白話步驟：

1. **小模型初譯**：用新約微調的 NLLB-200 把英文句譯成達豪語初稿。
2. **檢索例句與詞典**：在英文來源端，從新約與語法書例句庫檢索相似例句，並查達豪語詞典（避開沒有達豪語向量模型的問題）。
3. **大模型後編輯**：把來源句、初稿與檢索結果放進提示，請 Gemini 2.5 Flash 只修正重複、幻覺或錯詞。
4. **比較檢索方法與數量**：句級（BM25、BGE 向量、ChrF 多樣性）與詞級模糊比對，各試不同例句數量。

細節如下（§4, pp. 89–90；§5.2）：

### 1. 混合後編輯流程（Hybrid Post-Editing Architecture, 圖 1, p. 89）
1. **NMT 生成初稿**：以新約語料微調之 `NLLB-200-distilled-600M` 接收英文來源句 $x$，輸出帶有南島語詞序與基本構詞骨架的初步譯文草稿 $\hat{y}_{\text{NMT}}$。
2. **動態多來源檢索（RAG）**：自新約語料與語法書合成庫中，針對來源句進行跨領域例句與雙語詞典檢索（檢索均在英文來源端進行，避開缺乏達豪語向量模型的問題）。
3. **LLM 後編輯修正**：將英文來源句、NMT 初稿與檢索到的雙語範例/詞彙表組裝為結構化 Prompt（附錄 C），指示大模型（Gemini 2.5 Flash）比對來源句，僅在識別出重複迴圈、幻覺或明顯錯詞時進行局部修復，而非盲目重譯。

```text
[英文來源句 x] ──────────────────────────────────────────────┐
       │                                                      │
       ├─► [微調 NLLB-200 (NT)] ──► 初譯草稿 y_NMT ───────────┼─► [Gemini 2.5 Flash 後編輯]
       │                                                      │            │
       └─► [來源端動態檢索 RAG] ──► 檢索上下文 (例句 + 詞典) ─┘            ▼
           (NT 語料 + 語法書庫)                                   最終修復譯文 y_final
```

### 2. 檢索策略與語境容量之真實關係（§4.3, §5.2, pp. 90–92）
原文系統性比對了四種檢索策略在不同容量下的表現：
* **句級檢索（固定 $K \in \{5, \dots, 100\}$）**：
  * **BM25（稀疏詞彙）**：依關鍵詞精確重疊排序；在 $K=80$ 時達峰值 34.28 chrF++。
  * **BGE Embeddings（語意稠密）**：使用 `bge-large-en-v1.5` 計算餘弦相似度；在 $K=100$ 時達 34.87 chrF++。
  * **ChrF-Counterweighted（詞元多樣性）**：迭代挑選高字元重疊例句並懲罰已選 $n$-gram，防止重複短語浪費語境；在 $K=60$ 時即達到 34.98 chrF++（佔最優表現之 99%）。
  * **飽和效應**：所有句級檢索策略在 $K \approx 60 \sim 80$ 均出現平台期（Plateau），無法藉由單純堆砌整句進一步突破。
* **詞級模糊匹配（動態 $K$，Word-Level Fuzzy Matching）**：
  * 採用 `RapidFuzz` 計算字元級正規化 Levenshtein 相似度 $\ge 0.5$；針對輸入句的每個詞彙，自檢索庫抽取 $N$ 句相關雙語例句並去重。
  * **容量與雜訊權衡**：詞級策略成功打破了句級檢索的早飽和現象，當 $N=10$（有效句數 $K \approx 137$）時達到全場最高的 **35.28 chrF++**；但當進一步推升至 $N=15$（$K \approx 205$）與 $N=20$（$K \approx 272$）時，過多破碎的背景語境引入雜訊，分數回落至 35.16 與 34.22 chrF++（表 5），證實語境容量並非單調無限上升。
* **詞典檢索（Lexicon Retrieval）**：
  * 詞典檢索隨容量增加呈單調提升。論文對全量詞典筆數有內部差異：§3.1（p. 89）與附錄表 6（p. 100）列 2,377 條，§4.3.2（p. 90）則稱 2,375 條；表 6 的全量詞典結果為 31.32 chrF++ / 16.27 spBLEU。原文未解釋這項差異。

---

## Card 4 ｜ 資料與實驗
* **訓練與檢索資料**：達豪語新約聖經（Dhao Alkitab，CC BY-ND 4.0）；達豪語語法書（Balukh 2020，開放取用）之例句與詞典（§3；Ethical Considerations）。
* **測試**：舊約創世記（域外）；新約驗證集作域內參考（§3；表 1）。
* **比較方式**：只用翻譯模型、加語法書微調、大型語言模型直接翻譯（0／5-shot）、後編輯（無檢索、加詞典、加例句、兩者合併）；句級與詞級檢索在不同例句數量下比較（表 1–6）。
* **評分方式**：spBLEU 與 chrF++；另做重複迴圈、實體幻覺等質性分析（表 7）。沒有人工評分。

---

## Card 5 ｜ 結果
### 1. 基線與領域偏移數據（表 1, p. 89）
* **域內參考（新約 NT）**：NLLB 基線為 **25.19 spBLEU / 36.17 chrF++**。
* **域外測試（舊約創世記 OT，表 1）**：
  * NMT Only 基線：**7.66 spBLEU / 27.11 chrF++**（暴跌 8.06 BLEU、9.06 chrF++）。
  * NMT + Grammar 微調：**7.67 spBLEU / 26.62 chrF++**（chrF++ 反而劣化）。
  * LLM 直接翻譯（0-shot）：**2.98 spBLEU / 18.84 chrF++**。
  * LLM 直接翻譯（5-shot）：**7.37 spBLEU / 22.95 chrF++**。
  * LLM 後編輯（無 RAG，0-shot）：**10.65 spBLEU / 27.94 chrF++**。
  * LLM 後編輯（無 RAG，5-shot）：**12.54 spBLEU / 29.62 chrF++**。

### 2. 核心系統實驗成果（表 2, p. 91）
* **組件貢獻分解（舊約測試集）**：
  * Baseline (NMT Only)：$7.66 \text{ spBLEU} \;/\; 27.11 \text{ chrF++}$
  * + Lexicon (Full; 表 6 列 2,377 條、§4.3.2 列 2,375 條)：$16.27 \text{ spBLEU} \;(\uparrow 8.61) \;/\; 31.32 \text{ chrF++} \;(\uparrow 4.21)$
  * + Sentences (Word-Level, $N=10$, eff. $K \approx 137$)：$18.93 \text{ spBLEU} \;(\uparrow 11.27) \;/\; 35.28 \text{ chrF++} \;(\uparrow 8.17)$
  * **+ Combined (最終系統：詞級例句 ＋ 完整詞典)**：**$19.88 \text{ spBLEU} \;(\uparrow 12.22) \;/\; 35.21 \text{ chrF++} \;(\uparrow 8.10)$**，接近域內基準的 36.17 chrF++。

### 3. 詳細消融數據（附錄 E，表 4–6, p. 100）
* **句級檢索消融（表 4）**：BGE（$K=100$ 時 34.87）、BM25（$K=80$ 時 34.28）、ChrF-RAG（$K=60$ 時 34.98）。各演算法在同等容量下表現收斂在 0.5 分差距內。
* **詞級模糊檢索消融（表 5）**：$N=1$（eff. $K \approx 14$, 32.87 chrF++）$\to N=3$（$K \approx 42$, 34.42）$\to N=5$（$K \approx 70$, 35.00）$\to N=10$（$K \approx 137$, **35.28**）$\to N=15$（$K \approx 205$, 35.16）$\to N=20$（$K \approx 272$, 34.22）。
* **檢索語料消融（§5.2.1）**：若完全剔除語法書、僅在新約語料庫中檢索，最佳詞級模型僅由 35.28 微降至 35.01 chrF++（18.93 降至 18.47 spBLEU），表示即使沒有語法書，方法仍大致有效（Wiki 依表 5 與 §5.2.1 描述）。

### 4. LLM 安全網修復實例（表 7, p. 101）
* **重複迴圈修復**：GEN 7:12 中 NMT 陷入 `Hèia bèli-camèd’a bèli-camèd’a...` 無窮重複，後編輯成功生成正確語句 `Èj’i bhori ètu rai èpa nguru lod’o mèu-mèda.`。
* **實體幻覺修復**：GEN 11:5 英文為 "The Lord"，NMT 依訓練集高頻模式幻覺出大衛王 `dhèu aae Daud`（King David），後編輯對照英文與詞彙表更正為神之稱謂 `Lamatua`。
* **複雜成語重構**：GEN 11:17 中「became the father of」被 NMT 錯誤直譯並崩潰，後編輯依檢索例句重構出達豪語親族成語 `matana`。

* **作者結論**（§6, p. 94）：一般翻譯模型在未見過的領域會嚴重退步，而翻譯模型加大型語言模型後編輯的混合架構能把失去的品質大致補回；放進提示的例句數量是主要因素，不同檢索方法在數量相同時表現相近。作者也建議低資源研究以整卷書或整部聖經作為測試，而不是把聖經經文隨機切分，以免高估表現（§5.5）。

---

## Card 6 ｜ 限制與可用性
* **作者說的限制**（Limitations, p. 95）：只做英語→達豪語一個語言對、新約→舊約一種領域轉移，換成其他語言或宗教→世俗等轉移是否成立仍待驗證；詞典與例句合併時 spBLEU 最高、chrF++ 卻略降，兩種資料的搭配尚待更細的消融。
* **讀的時候要留意**：詞典條目數原文前後不一（2,377 與 2,375）；例句數量並非越多越好，詞級檢索在約 137 句達峰值後回落（表 5）。原文沒有人工評分。
* **公開程度**：原文未提供程式碼連結；所用聖經譯本為 CC BY-ND 4.0、語法書為開放取用出版品（Ethical Considerations）。
* **適合拿來報告的點**：清楚示範「小模型初稿＋大模型參考例句修稿」如何補回跨領域翻譯的失分，並指出例句數量比檢索方法重要；也提醒聖經語料測試要按整卷書切分（Wiki 詮釋）。

### 延伸想法
以下為延伸思考（Wiki 推測），不是原文主張。

1. **南島語聖經與日常會話的領域轉移**：泰雅語、太魯閣語、賽德克語的現存語料中，聖經譯本佔很高比重。將模型用在族語新聞、文化教材或日常會話時，可能遇到類似的領域轉移；可參考本文的後編輯架構，但效果需實驗驗證。
2. **辭典與語法教材的用法**：本文顯示語法書例句直接加入微調反而略差，放在檢索庫供後編輯參考則較好。原民會線上辭典與族語語法書或可同樣作為檢索來源，而非直接加入微調。
3. **控制例句數量**：例句不是越多越好，設計提示時可設定上限並去除重複。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Setiawan, D. S., Merx, R., & Lau, J. H. (2026). Context Volume Drives Performance: Tackling Domain Shift in Extremely Low-Resource Translation via RAG. In *Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026)* (pp. 87-101). DOI: [10.18653/v1/2026.loresmt-1.7](https://doi.org/10.18653/v1/2026.loresmt-1.7)
  * 原始檔典藏：`raw/my-focus/大模型輔助/Context Volume Drives Performance Tackling Domain Shift in Extremely.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-context-volume-rag-domain-shift-setiawan.md](../evidence/2026-context-volume-rag-domain-shift-setiawan.md)
