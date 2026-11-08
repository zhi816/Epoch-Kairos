---
title: "Semantic Phenomena of Verbs of Saying in Formosan Languages: A Typological Investigation"
title_zh: "台灣南島語「說」動詞語義現象初探"
paper_year: 2022
award_year: 2022
timeline_year: 2022
authors: "Fuhui Hsieh"
venue: "Journal of Taiwanese Languages and Literature, 17(1), 47-92"
domain: "human"
domain_tags: ["#語言學"]
concepts: ["formosan-computational-linguistics"]
status: "wiki"
my_focus: true
focus_role: "taiwan-linguistics"
focus_languages: ["臺灣南島諸語"]
doi_url: "https://doi.org/10.6710/JTLL.202204_17(1).0002"
hook: "揭開台灣南島語「說」動詞跨越述說、認知、施為與語法化的多義演化路徑，證明述說動詞源自兼具『說』與『做』的原始施為動詞，並為計算語法解析提供了深層跨語言類型學先驗。"
---

# 台灣南島語「說」動詞語義現象初探 (Semantic Phenomena of Verbs of Saying in Formosan Languages)

> 「在南島語言的深層演化中，『說』從來不只是被動地傳遞語言符號，它本身就是一種具備模仿性與指示性的施為行動，並在漫長的言談互動中凝結為引導子句與標記語法的骨架結構。」

**2022 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
在傳統語言學與自然語言處理的詞彙語義標註中，「說」（Verbs of Saying）通常被視為單純引導言談或直接／間接引述的述說動詞。然而，大同大學謝富惠教授於 2022 年發表的《台灣南島語「說」動詞語義現象初探》針對 16 個台灣南島語言進行全面類型學考察，揭示了獨特的多義現象：台灣南島語的「說」動詞不僅普遍向「思考、相信」等認知語義場延伸，更在本質上兼具「如此、像、做、去」等多重施為語義，並進一步語法化為補語標記（Complementizer）、示證標記（Evidential）與言談標記（Discourse Marker）。這項研究為台灣南島語的語法分析與計算語言學模型提供了關鍵的深層構詞與句法轉化基礎。

---

## Card 2 ｜ 世紀瓶頸：跨語言語義場混淆與低資源斷詞標記困境 (The Dilemma)
在低資源語言的計算處理與語法標註任務中，研究者長期面臨兩大瓶頸：

* **句法標記與動詞詞根的多義性混淆**：在許多南島語文本中，同一個詞形（例如邵語 `mzai` 或賽夏語 `komoSa'`）有時作為主要述說動詞（「說」），有時作為認知動詞（「認為」），有時卻扮演從屬子句的補語連詞（「...說要如何去」）或引述引導詞。若缺乏類型學演化路徑，機器翻譯與語法剖析器會頻繁發生詞性標註錯誤與結構切分錯位。
* **孤立動詞假設的失效**：傳統計算模型常假設「述說動詞」是獨立的詞彙單元，忽略了南島語中「說」與「做」（Action）在概念結構上的原始同源性，導致跨語言詞彙對齊時遺失深層動態語義。

---

## Card 3 ｜ 突破架構與原理：施為動詞演化路徑與語法化模型 (The Secret)
謝富惠教授提出，台灣南島語的「說」動詞本質上源自語義較廣泛的**原始施為動詞（Performative Action Verb $X$）**，其演化涵蓋三個連續階段：

1. **施為語義共現（Performative Co-occurrence）**：
   * 原始動詞 $X$ 同時具備述說（Saying）與動作（Doing）的語義成分：
     $$X \approx \langle \text{Say}, \text{Do} \rangle$$
2. **情境增添與語義特化（Contextual Enrichment）**：
   * 當動詞 $X$ 頻繁與直接引述句（Direct Quote）共現時，引述伴隨的面部表情、語氣模仿或肢體動作為該動詞增添了「模仿性（Iconicity）」與「指示性（Indexicality）」，演化為兼具「像（Like）」、「如此（Thus）」與「去（Go）」之複合述說動詞：
     $$\begin{aligned}
     \mathcal{S}_{\text{enriched}}(X) &= \mathcal{S}_{\text{base}}(X) \cup \{ \text{Manner}, \text{Similarity}, \text{Direction} \} \\
     &= \{ \text{Say}, \text{Think}, \text{Thus}, \text{Like}, \text{Go} \}
     \end{aligned}$$
3. **語法化脫落與標記化（Grammaticalization & Decathexation）**：
   * 隨著述說語義逐步虛化（Semantic Bleaching），該動詞脫離主要動詞位置，受格位或焦點綴化修飾後退化為功能性標記：
     $$\text{Verb}(X) \xrightarrow{\text{Grammaticalization}} \begin{cases} \operatorname{Comp}(X) & \text{(Complementizer)} \\ \operatorname{Evid}(X) & \text{(Evidential)} \\ \operatorname{DM}(X) & \text{(Discourse Marker)} \end{cases}$$

### 語法化轉換過程之數學形式化

若將動詞之語義空間定義為有限維特徵向量 $\mathbf{v} \in \mathbb{R}^d$，語法化過程可表徵為語義權重向量隨語法化進程 $\tau \in [0, 1]$ 的動態衰減與功能權重轉移：

$$\mathbf{v}(\tau) = (1 - \tau) \mathbf{v}_{\text{lexical}} + \tau \mathbf{v}_{\text{functional}}$$

其中，當 $\tau \to 1$ 時，詞彙性語義能量 $\|\mathbf{v}_{\text{lexical}}\|$ 被漂白，句法連接度與約束度則單調遞增。

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的語言分析結果
* 研究分析 **16 種**台灣南島語言的「說」動詞。原文摘要指出，其中 **12 種**的「說」動詞除述說義外，也具有「如此、像、做或去」等語義；布農語、鄒語、卡那卡那富語與拉阿魯哇語不屬於這 12 種。
* 論文追蹤各語言「說」動詞的語義延伸與語法化，討論補語標記、示證標記及言談標記等功能。原文沒有報告「認知義出現率 100%」等量化指標。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **突破印歐語言中心主義**：打破了傳統印歐語系「說動詞就是單純引述詞」的狹隘認知，證明在南島語系中，言談行為與動態施為在概念層級上具有高度同源性。
* **為南島語計算句法分析提供理論先驗**：解釋了為何自動剖析器在處理南島語子句邊界時常將補語標記誤判為主動詞；將語言學的語法化路徑作為先驗歸納偏置，可顯著提升依存句法分析（Dependency Parsing）與機器翻譯對齊的準確率。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
謝富惠教授對台灣南島語「說」動詞的類型學解析，為我的碩士論文研究（臺灣南島語構詞解析、低資源機器翻譯與檢索增強生成）帶來了深層的架構性啟示：

1. **構詞解析模組不能孤立於句法上下文**：
   * 在泰雅語、賽德克語與太魯閣語中，像 `musa'`、`mhai`、`kema` 這類詞彙，既可能作為帶有焦點中綴或前綴的獨立動詞，也可能是虛化後的連詞或示證語。構詞分析器若僅在單詞層級進行靜態規則比對，必然產生大量偽歧義。
   * **啟發**：構詞解析引擎必須結合雙向序列特徵（如 BiLSTM 或淺層 Transformer），在判斷深層詞根的同時，輸出其是否發生「語法化詞性漂白」的機率分佈。
2. **多語言機器翻譯與 RAG 檢索中的精準對齊**：
   * 當利用大型語言模型進行檢索增強生成（RAG）翻譯時，若直接檢索辭典中的「說」，往往會產出不自然的中文直譯。若系統能透過 prompt 明確提示該詞在目標語中兼具「如此」或「引述補語」的功能，大語言模型將能生成更通順自然的譯文。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
* **原始權威文獻**：
  * 官方學術出處：謝富惠 (2022)。台灣南島語「說」動詞語義現象初探。《臺灣語文研究》，17(1)，47-92。DOI: [10.6710/JTLL.202204_17(1).0002](https://doi.org/10.6710/JTLL.202204_17(1).0002)
  * 原始檔典藏：`raw/my-focus/台灣相關論文/台灣南島語「說」動詞語義現象初探_謝富貴.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
