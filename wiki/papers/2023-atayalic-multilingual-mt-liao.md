---
title: "Multilingual Machine Translation between Atayalic Languages and Chinese"
title_zh: "泛泰雅語群與中文之多語言機器翻譯研究"
paper_year: 2023
award_year: 2023
timeline_year: 2023
authors: "Eric Liao"
venue: "Master's Thesis, Department of Computer Science and Engineering, National Taiwan Ocean University"
domain: "ai"
domain_tags: ["#自然語言處理", "#深度學習", "#計算語言學"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
verification: "issues"
my_focus: true
focus_role: "senior-thesis"
focus_languages: ["泰雅語", "賽德克語", "太魯閣語"]
hook: "首創泛泰雅語群（泰雅語、賽德克語、太魯閣語）與中文之多語言 Transformer 機器翻譯框架，以共享 BPE 子詞與語言標籤實現同源語族跨語言正向遷移。"
---

# 泛泰雅語群與中文之多語言機器翻譯研究 (Multilingual Machine Translation between Atayalic Languages and Chinese)

> 「當每一種單一語言的資料量都微弱如風中殘燭，多語言機器翻譯將同源語族的歷史血脈連成一片，讓同源詞素在同一個神經矩陣中彼此借光照明。」

**2023 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
在臺灣南島語言中，泰雅語（Atayal）、賽德克語（Seediq）與太魯閣語（Truku）同屬於「泛泰雅語群（Atayalic Languages）」，具備高度同源的語彙、相近的音韻體系與同構的動詞焦點語法。然而過去的研究大多將各語種獨立切開進行單對單翻譯，加劇了極低資源資料匱乏的瓶頸。國立臺灣海洋大學林川傑教授指導、廖恒慶於 2023 年 3 月完成的碩士論文《泛泰雅語群與中文之多語言機器翻譯研究》，首次打破單語孤島，建構了覆蓋泰雅語、賽德克語、太魯閣語與中文之多語言神經機器翻譯（Multilingual NMT）系統，透過共享 BPE 子詞與跨語言聯合訓練，開創了臺灣南島語跨語言遷移學習的全新範式。

---

## Card 2 ｜ 世紀瓶頸：單語語料極限與同源詞彙割裂 (The Dilemma)
在極低資源語境下，獨立訓練單一語言對中文的神經翻譯模型面臨嚴峻限制：

* **單語資料量的天花板效應**：各單一南島語線上有標註的雙語例句往往僅有數千至一萬多句，單獨訓練的 Transformer 模型極易陷入嚴重過擬合（Overfitting），在未見過的測試句上頻繁生成重複或語無倫次的文字。
* **詞表割裂阻斷跨語言同源性遷移**：若為泰雅語、賽德克語和太魯閣語各自建立獨立的詞彙表（Vocabularies），模型無法識別出不同語言間詞根的高度相似性（Cognates），浪費了親屬語言之間強大的語法與語義先驗資訊。

---

## Card 3 ｜ 突破架構與原理：泛泰雅共享 BPE 與多語言標籤聯合架構 (The Secret)

### 1. 泛泰雅共享子詞空間（Shared Subword BPE）

廖恒慶首先將泛泰雅語群三種語言之文字語料進行合併，共同訓練一套統一的 Byte-Pair Encoding（BPE）子詞辭典。設原始字元集合為 $\mathcal{V}_0$，每次迭代選取在泛泰雅混合語料庫 $\mathcal{C}_{\text{Atayalic}}$ 中共現頻率最高的相鄰子詞對進行合併：

$$(u^*, v^*) = \arg\max_{(u, v)} \sum_{l \in \{\text{tay}, \text{sed}, \text{trv}\}} \operatorname{Count}_l(u, v)$$

透過此機制，同源語素（如主事焦點中綴 `-um-`、名物化標記 `-an`、否定詞 `ini`）被統一映射至相同的子詞 Token，極大化了詞嵌入表示在親屬語言間的參數共享。

### 2. 多語言神經翻譯目標函數方程式

在 Transformer 架構中，系統在來源端序列開頭強制注入目標語言識別標籤（Target Language Tag $\tau \in \{ \langle 2\text{zh} \rangle, \langle 2\text{tay} \rangle, \langle 2\text{sed} \rangle, \langle 2\text{trv} \rangle \}$）。

多語言聯合優化目標函數定義為跨語言對加權交叉熵損失之和：

$$\mathcal{L}_{\text{Multi}}(\theta) = -\sum_{l \in \mathcal{T}_{\text{pairs}}} \sum_{(x, y) \in \mathcal{D}_l} \sum_{t=1}^{|y|} \log P\Big(y_t \mid y_{<t}, [\tau_l \,\|\, x]; \theta\Big)$$

其中：
* $\mathcal{T}_{\text{pairs}} = \{ \text{tay}\leftrightarrow\text{zh}, \text{sed}\leftrightarrow\text{zh}, \text{trv}\leftrightarrow\text{zh} \}$
* $\tau_l$：指導解碼器生成特定目標語言的控制向量。

```text
[泰雅語輸入 / 賽德克語輸入 / 太魯閣語輸入] ──► [<2zh> 語言標籤] 
                             │
                             ▼
              [共享泛泰雅 BPE 子詞嵌入層]
                             │
                             ▼
                  [Transformer 編碼器]
                             │
                             ▼
                  [Transformer 解碼器] ──► [流暢中文翻譯]
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的機器翻譯結果
* 訓練資料取自原住民族語言線上辭典與族語 E 樂園教材，外部測試資料取自《台灣南島語言叢書》；論文比較單語、多語言與遷移式學習系統。
* 原文摘要列出的族語翻中文起始與最佳 BLEU 分數依序為：泰雅語 **17.42 → 20.81**、賽德克語 **15.50 → 19.38**、太魯閣語 **15.48 → 20.84**。
* 中文翻族語方向依序為：泰雅語 **17.44 → 21.98**、賽德克語 **16.15 → 21.97**、太魯閣語 **18.04 → 26.69**。這些數值是摘要列出的系統結果。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **由「單一語言孤軍奮戰」轉為「語群生態系協同運算」**：證實了臺灣南島語雖個別資料極少，但依託語族內部的同源性，多語言模型可實現「一加一加一大於三」的跨語言正向遷移。
* **奠定臺灣南島語多語言神經架構的通用工程標準**：建立的泛泰雅共享 BPE 詞表與語言標籤機制，成為後續研究者通用的數據預處理管線。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
廖恒慶的多語言泛泰雅翻譯研究，對我的碩士論文研究提供了關鍵的架構視野：

1. **共享詞素空間對未知詞與低資源方言的平滑效果**：
   * 在單一語言中極為罕見的生詞，在親屬語言中可能以高頻同源詞形式存在。多語言預訓練使得神經模型能自然習得同源詞的語義連續空間。
2. **現代大模型檢索增強生成（RAG）之跨語言檢索啟示**：
   * 在低資源語言 RAG 系統中，如果目標方言的雙語平行例句極度匱乏，我們可以透過泛泰雅共享語素對齊機制，檢索親屬語言（如以太魯閣語例句作為賽德克語的跨語言上下文 Prompt），讓大語言模型借用親屬語言的語法骨幹完成生成。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 學位論文出處：廖恒慶 (2023)。泛泰雅語群與中文之多語言機器翻譯研究。國立臺灣海洋大學資訊工程學系碩士學位論文，指導教授：林川傑博士。
  * 原始檔典藏：`raw/my-focus/學長姐論文/泛泰雅語群與中文之多語言機器翻譯研究_廖恒慶.pdf`（對應文字檔：`raw/my-focus/學長姐論文/.md/泛泰雅語群與中文之多語言機器翻譯研究_廖恒慶.md`，由私有倉庫 Mine-RAW 版控）
