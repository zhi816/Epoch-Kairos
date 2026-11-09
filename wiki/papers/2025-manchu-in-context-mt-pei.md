---
title: "Understanding In-Context Machine Translation for Low-Resource Languages: A Case Study on Manchu"
title_zh: "理解低資源語言之上下文機器翻譯：以滿語為例的實證研究"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Renhao Pei, Yihong Liu, Peiqin Lin, François Yvon, Hinrich Schütze"
venue: "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025), 8767-8788"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#人工智慧"]
concepts: ["low-resource-machine-translation"]
status: "wiki"
verification: "verified"
my_focus: true
focus_role: "report"
focus_languages: ["滿語"]
doi_url: "https://doi.org/10.18653/v1/2025.acl-long.429"
hook: "以滿語譯英語逐一檢驗上下文翻譯的各項資源：高品質詞典與相似的平行例句最有幫助，語法書幾乎沒有幫助，思維鏈提示反而使分數下降；字母替換實驗顯示模型主要依賴上下文學習。"
card_line: "找出哪些參考資料，最能幫大模型翻譯滿語"
---

# 理解低資源語言之上下文機器翻譯：以滿語為例的實證研究 (Understanding In-Context Machine Translation for Low-Resource Languages: A Case Study on Manchu)

> 「大語言模型並非通曉萬物的先知，在面對預訓練語料庫中幾近空白的極低資源語言時，它更像一位手握外掛參考書的高速解碼員。」（本頁引言為 Wiki 撰寫，非原文）

**2025 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Pei, Liu, Lin, Yvon & Schütze（LMU Munich、MCML、Sorbonne Université），*ACL 2025 (Long Papers)*, pp. 8767–8788。除特別註明外，第 4 節數字皆為 GPT-4o 在 337 句滿英測試集上的結果。

---

## Card 1 ｜ 時代銘文 (The Hook)
滿語是原生於中國東北、極度瀕危的**通古斯語**（Tungusic），曾為清代官方語言之一；因歷史地位重要，詞典、語法書與部分平行例句等語言學資源相當豐富，適合作為研究案例（§3, p. 8769）。本文系統檢驗上下文機器翻譯中各類資源——構詞分析、詞典、平行例句、語法書與思維鏈（CoT）提示——對翻譯品質的影響；並以字母替換「加密」滿語，區分大型語言模型對滿語的既有知識與其上下文學習能力（摘要；§1）。

---

## Card 2 ｜ 世紀瓶頸：各類資源的相對重要性不明 (The Dilemma)
* 田野語言學家已為全球六成以上語言留下語法描述或詞典，但這些語言在資料驅動的機器翻譯中仍屬低資源，因為缺乏平行語料（§1, p. 8767）。
* 先前研究把詞典、平行例句、語法書放進提示中，但**各類資源的相對重要性並不清楚**（摘要）；模型的表現也可能部分來自預訓練時見過該語言，而非上下文學習。

---

## Card 3 ｜ 突破架構與原理：逐一加入組件與字母替換加密 (The Secret)

### 1. 提示組件（§4, pp. 8769–8772）
以 $\pi(\cdot)$ 表示提示，$x$ 為待譯滿語句。由於窮舉所有組合在計算上不可行，作者**依序加入**各組件，每一步選出最佳變體作為下一步的新基線，順序為：構詞分析 $\mu(x)$ → 詞典 $D$ → 平行例句 $P$ → 語法 $G$ → CoT $C$。
* **構詞分析**：滿語只用後綴，作者以規則式分析器從詞尾遞迴剝除後綴，直到剩下已知詞幹；有多種分析時全部放入提示，由模型選擇（§4.1）。
* **詞典**：$D_l$（只有詞條）、$D_{l+s}$（加後綴說明）、$D_{l+s+c}$（再加搭配詞）。
* **平行例句**：$P_r$（隨機 10 句）、$P_d$（依詞典詞條取例句）、$P_{bm}$（以 BM25 檢索 10 句）。
* **語法**：依句中語法特徵，從短版或長版語法書擷取相關段落（$G_s$、$G_l$、$G_{l+p}$）。
* **CoT**：$C_a$（先標注每個詞的語法語義特徵）、$C_{a+s}$（再分析句法結構）。

最終流程為 $\pi(\mu(x), D_{l+s+c}, P_{bm})$，語法與 CoT 未納入（§4.5）。

### 2. 字母替換加密（§5.2, p. 8773）
把滿語中每個母音換成序列 (a, e, i, o, u) 中的下一個（如 a → e、u → a），子音也依序列 (b, c, d, …, z) 替換，例如 `amban` 變成 `encep`。加密同時套用到輸入句、詞典與例句中的滿語，英文部分不變，使模型只能依賴提示中的資訊。

### 3. 生成設定（附錄 C, pp. 8781–8782）
Llama3 以溫度 0.9、top-p 0.9 生成；GPT-4o 與 DeepSeek-V3 使用 API 預設值（溫度 1.0、top-p 1.0）。

```text
[滿語句 x] ──► 規則式構詞分析 μ(x) ──► 詞典（詞條＋後綴＋搭配）──┐
                                └──► BM25 檢索 10 句平行例句 ─┴──► 提示 ──► LLM ──► 英文譯文
（語法書與 CoT 經測試後不納入）
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 逐步加入組件（GPT-4o；BLEU／chrF／SBERT；表 1–4, pp. 8771–8772）
| 設定 | BLEU | chrF | SBERT |
|---|---|---|---|
| 直接提示 $\pi(x)$ | 3.44 | 21.86 | 34.21 |
| ＋構詞分析 | 3.10 | 21.68 | 33.49 |
| ＋詞典 $D_{l+s+c}$ | 7.55 | 32.71 | 61.07 |
| ＋BM25 例句 $P_{bm}$ | **8.84** | 33.72 | 61.35 |
| ＋語法 $G_{l+p}$ | 8.90 | 33.77 | 60.40 |
| ＋CoT $C_{a+s}$ | 8.49 | 33.43 | 59.01 |

* **顯著性**（附錄 G，表 10, p. 8783；bootstrap 1,000 次）：加入詞典的提升在三項指標都顯著（p = 0.0009）；BM25 例句在 BLEU 與 chrF 顯著（p = 0.04、0.03），SBERT 不顯著；**語法**的微幅提升不顯著（BLEU、chrF 皆 p = 0.4），**CoT** 亦不顯著。原文的結論是「語法書幾乎沒有幫助」，CoT「使兩種變體都明顯下降」（§4.4–4.5）。
* **不同模型**（表 5）：最佳設定下 DeepSeek-V3 達 **12.35 BLEU／65.64 SBERT**，Llama3 由 1B 到 70B 依序提升（0.27 → 6.31 BLEU）。

### 加密與人工評估（圖 2、表 7, pp. 8773–8775）
* 所有模型在加密後分數都略降，顯示它們預訓練時見過一些滿語；DeepSeek-V3 下降最多，作者推測與其大量中文訓練資料有關。
* 三位滿語專家對 33 句進行直接評分（DA）：直接提示 29.04、加密版 56.12、原版 64.47；兩個增強版都顯著優於直接提示（p < 0.001），加密版與原版的差異不顯著（p = 0.27）。作者據此認為模型「主要依賴上下文學習」，但並非完全不依賴既有知識。

### 合成資料訓練 NMT（§6, p. 8775；圖 3）
以 DeepSeek-V3 的最佳設定，把 42,240 句滿語單語資料譯成英文，與 3,520 句真實平行語料一起微調 mT5-small（約 3 億參數）。只用真實資料時幾乎無法翻譯（0.15 BLEU）；合成資料為真實資料的 12 倍時達 7.84 BLEU／55.96 SBERT，接近 Llama3-70B 的上下文翻譯結果。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **作者結論**（§7）：高品質詞典與適當檢索的平行例句是最有影響的因素，語法與 CoT 看不出明顯幫助；模型雖有一些滿語知識，但翻譯主要依賴上下文學習；上下文翻譯可用來產生合成平行資料。
* **作者自述的限制**：只研究滿語一種語言；滿語是詞素界線清楚的黏著語，結論是否適用於其他類型的語言尚不清楚（Limitations）。另外，平行語料原為滿漢對照，英文是以 Google 翻譯從中文轉譯而來（§3）。
* （Wiki 詮釋）BLEU 與 chrF 可能低估語義正確的譯文（表 6 的例句 BLEU 4.99、SBERT 62.42），作者因此另做人工評估。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **提示內容的優先順序**：
   * 本文顯示詞典（含詞綴說明與搭配）與 BM25 相似例句的貢獻明顯，語法段落與 CoT 則沒有顯著幫助。在臺灣南島語的 RAG 提示中，可以優先投入詞典與例句檢索的品質；但臺灣南島語有前綴、中綴與重疊，構詞比只用後綴的滿語複雜，結論是否適用仍需實驗驗證（作者也提醒此限制）。
2. **構詞分析本身不夠**：
   * 只把句子切成詞素並不會提升分數（3.44 → 3.10），要搭配詞典說明才有效。構詞解析在 RAG 中的價值，在於把詞根與詞綴對上詞典條目。
3. **評估方式**：
   * 除了 BLEU、chrF，可加入語義相似度指標，並在可行時做小規模人工評估。
4. **合成資料**：
   * 第 6 節的做法（以上下文翻譯把單語資料轉為平行資料，再訓練小模型）也可用於臺灣南島語，但需注意合成資料的錯誤會傳遞到小模型。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Pei, R., Liu, Y., Lin, P., Yvon, F., & Schütze, H. (2025). Understanding In-Context Machine Translation for Low-Resource Languages: A Case Study on Manchu. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 8767-8788). DOI: [10.18653/v1/2025.acl-long.429](https://doi.org/10.18653/v1/2025.acl-long.429)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2025.acl-long.429.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2025-manchu-in-context-mt-pei.md](../evidence/2025-manchu-in-context-mt-pei.md)
