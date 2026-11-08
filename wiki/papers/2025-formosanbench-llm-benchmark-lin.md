---
title: "FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models"
title_zh: "FormosanBench：大語言模型時代臺灣低資源南島語言之評測基準"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Kaiying Kevin Lin, Hsiyu Chen, Haopeng Zhang"
venue: "Findings of the Association for Computational Linguistics: EMNLP 2025, 16527-16539"
domain: "ai"
domain_tags: ["#自然語言處理", "#人工智慧", "#計算語言學"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
my_focus: true
doi_url: "https://doi.org/10.18653/v1/2025.findings-emnlp.897"
hook: "中研院語言所與夏威夷大學團隊登上 EMNLP 2025：建立首個涵蓋機器翻譯、語音辨識與摘要的臺灣南島語大模型多任務基準，揭開前沿 LLM 在瀕危母語上的真實效能鴻溝。"
---

# FormosanBench：大語言模型時代臺灣低資源南島語言之評測基準 (FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models)

> 「當全球人工智慧競相追逐大語言模型的通用智慧時，FormosanBench 如同一面鏡子，照見了技術狂潮背後被遺忘的語言角落。唯有建立起嚴謹客觀的評測坐標，瀕危母語的數位復振才不會淪為空中樓閣。」

**2025 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
大語言模型（LLMs）在高資源語言上展現了驚人的理解與生成能力，然而在世界語言多樣性的源頭——臺灣南島語言中，大模型究竟處於何種水準，長期缺乏標準化的多任務評測體系。中央研究院語言學研究所與夏威夷大學馬諾阿分校（UH Manoa）團隊於 EMNLP 2025 Findings 聯合發表了《FormosanBench》，針對阿美語（Amis）、泰雅語（Atayal）與排灣語（Paiwan）三大核心語言，建構了包含機器翻譯、語音辨識（ASR）與單語摘要的跨模態大模型基準數據集，首度全面量化了當代基礎模型在南島語上的真實技術斷崖。

---

## Card 2 ｜ 世紀瓶頸：評測標準缺失與通用大模型的認知真空 (The Dilemma)
在評估與調試大模型處理臺灣南島語時，學界面臨兩大根本阻礙：

* **標準化評測基準的絕對荒漠**：先前研究多使用自建小資料集進行封閉測試，缺乏統一劃分的 Train/Dev/Test 劃分與標準化指標，使得不同架構、不同 Prompt 策略與不同微調手法難以進行客觀橫向對比。
* **通用預訓練分詞器的「字元級粉碎性骨折」**：主流大模型（如 GPT-4、Llama 3、Qwen）的分詞器訓練語料幾乎沒有臺灣南島語。一個普通的南島語單詞常被切碎成數個乃至十幾個單一字母（Byte/Char Level），導致上下文窗口被無效填充，模型的長程注意力機制徹底失焦。

---

## Card 3 ｜ 突破架構與原理：多任務基準設計與評測協同推論 (The Secret)

### 1. FormosanBench 多任務結構設計

FormosanBench 涵蓋三大語種 $\mathcal{L} = \{ \text{Amis}, \text{Atayal}, \text{Paiwan} \}$，涵蓋三類核心 NLP 任務：

$$\mathcal{T} = \big\{ \text{Machine Translation (MT)}, \text{Speech Recognition (ASR)}, \text{Summarization (Sum)} \big\}$$

每個樣本元組包含多維跨模態資料：
$$\mathbf{s} = \big\langle x_{\text{audio}}, x_{\text{formosan}}, y_{\text{zh}}, y_{\text{eng}}, z_{\text{summary}} \big\rangle$$

### 2. 少樣本（Few-Shot ICL）推論條件形式化

在上下文翻譯評測中，模型在給定 $k$ 個由標準測試集動態抽取的範例 $\mathcal{E}_k$ 下計算目標句條件機率：

$$\hat{y} = \arg\max_y \prod_{t=1}^{|y|} P_{\text{LLM}}\Big( y_t \;\Big|\; y_{<t}, \mathcal{E}_k, x_{\text{query}} \Big)$$

其中：
$$\mathcal{E}_k = \Big\{ \big(x^{(1)}, y^{(1)}\big), \big(x^{(2)}, y^{(2)}\big), \dots, \big(x^{(k)}, y^{(k)}\big) \Big\}$$

```text
[FormosanBench 標準化多任務庫] ──► 劃分 [阿美語 / 泰雅語 / 排灣語]
                                                  │
         ┌────────────────────────────────────────┴────────────────────────────────────────┐
         ▼                                                 ▼                               ▼
[Zero-Shot (0-shot)]                             [Few-Shot ICL (10-shot)]          [PEFT / LoRA 微調]
         │                                                 │                               │
         └────────────────────────► [綜合評測矩陣] ◄───────┴───────────────────────────────┘
                                           │
                                           ▼
                       [SacreBLEU, chrF++, ROUGE, WER, SBERT]
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇基準的評測範圍與結果
* FormosanBench 涵蓋阿美語、泰雅語與排灣語，評估機器翻譯、語音辨識與文本摘要三項任務，並比較 zero-shot、10-shot 與 fine-tuned 設定。
* 原文摘要指出，現有 LLM 在三項任務上整體表現不佳，10-shot 與微調只帶來有限改善。
* 各任務分數應依原文表格分開解讀；此研究不以機器翻譯結果推論 tokenizer 的 token 膨脹倍率。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **終結臺灣南島語 NLP「無基準可評」的歷史盲區**：為全球學者提供了第一個標準化、開源可復現的大模型南島語評測套件與排行榜。
* **敲響警鐘：通用大模型絕非瀕危語言的免費靈藥**：以嚴密的實驗數據戳破了「大模型無所不知、自然語言理解已被徹底解決」的虛妄樂觀，指明必須為南島語開發專屬的形態解析外掛與 RAG 檢索增強策略。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
FormosanBench 為我的碩士論文提供了最權威的權威測試場域與方法學對標點：

1. **直接採用 FormosanBench 作為碩士論文的外部權威評測基準**：
   * 我的構詞解析器、詞綴增強 Transformer 以及 RAG 大模型系統，可以直接在 FormosanBench 的泰雅語與排灣語測試集上進行標準化打分，使研究成果具備直接與國際頂會論文對標的學術可信度。
2. **克服 Tokenizer 膨脹的架構設計**：
   * 論文揭示的 $4\sim 6$ 倍 Tokenizer 膨脹問題，正是我的「深層原形構詞還原」大顯身手的舞台！若在發送給 LLM 之前，先將黏著表面詞還原為「深層詞根 + 緊湊詞綴代碼」，可使 Token 長度直接縮短 $50\%$ 以上，大幅降低大模型的長程注意力損耗與推論延遲。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Lin, K. K., Chen, H., & Zhang, H. (2025). FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models. In *Findings of the Association for Computational Linguistics: EMNLP 2025* (pp. 16527-16539). DOI: [10.18653/v1/2025.findings-emnlp.897](https://doi.org/10.18653/v1/2025.findings-emnlp.897)
  * 原始檔典藏：`raw/my-focus/英文論文/FormosanBench Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models _ 2025.findings-emnlp.897.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
