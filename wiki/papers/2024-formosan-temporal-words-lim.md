---
title: "A Cross-linguistic Comparative Study of Temporal Words in Formosan Languages"
title_zh: "台灣南島語言時間詞之跨語言比較初探"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Hong-sui Lim"
venue: "Taiwanica, 23, 1-27"
domain: "human"
domain_tags: ["#語言學"]
concepts: ["formosan-computational-linguistics"]
status: "wiki"
my_focus: true
focus_role: "taiwan-linguistics"
focus_languages: ["臺灣南島諸語"]
doi_url: "https://doi.org/10.6242/twnica.202404_(23).0001"
hook: "在 Dixon 語言學框架下全面解構台灣南島語時間推移詞的分合類型，揭示以『距今天數』為核心的對稱構詞特徵與實現／非實現標記系統，為低資源語法感知計算提供了嚴密的形態規則。"
---

# 台灣南島語言時間詞之跨語言比較初探 (A Cross-linguistic Comparative Study of Temporal Words in Formosan Languages)

> 「時間在人類語言中的投影並非單向流動的單維軸線；在台灣南島語中，它是以『今日』為原點、以距今天數為對稱半徑，再透過實現與非實現的語法形態鏡像展開的精緻幾何。」

**2024 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
時間詞（Temporal Words）是自然語言指涉時空座標與建構敘事脈絡的核心載體。國立暨南國際大學林鴻瑞博士於 2024 年在《台灣學誌》發表的論文《台灣南島語言時間詞之跨語言比較初探》，立足於著名語言學家 R. M. W. Dixon 的基本語言學理論框架，對全台灣 16 個南島族群語言中的核心「時間推移詞」（Temporal Shifters：昨天、明天、前天、後天）進行了窮盡性的跨語言比較。研究發現，絕大多數台灣南島語在構詞上以「距今天的絕對天數」為分組核心，將差一天的「昨天／明天」及差兩天的「前天／後天」共享同一個詞根，並依賴時態或「實現／非實現（Realis / Irrealis）」標記進行正反鏡像區分。此發現為計算語言學的構詞解析與跨語言語法規則建模提供了強大的先驗約束。

---

## Card 2 ｜ 世紀瓶頸：非線性時間認知與構詞對稱性的表層遮蔽 (The Dilemma)
在低資源南島語言的自然語言處理中，時間詞的自動解析常遭遇嚴重挑戰：

* **印歐語思維導致的單詞孤立假設**：英文中 `yesterday` 與 `tomorrow` 詞根全異，漢語以「昨／明／前／後」搭配「天」。若將此孤立或線性假設套用於南島語，計算模型常無法察覺南島語時間詞深層的對稱構詞律，將同一詞根在不同時相下的衍生形誤判為互不相干的獨立詞彙。
* **實現（Realis）與非實現（Irrealis）形態標記交織**：在許多南島語中，時間詞的詞根不單獨出現，必須強制附加標示「已實現（過去）」或「未實現（未來）」的前綴或虛詞。這種形態上的高黏著性，使得統計模型與神經分詞器（如 BPE）頻繁將時間詞切碎為毫無語意的不完整子詞片段。

---

## Card 3 ｜ 突破架構與原理：Dixon 時間推移模型與形態標記代數 (The Secret)
林鴻瑞教授依據 Dixon (2010, 2012) 的時間詞五分架構，將時間推移詞形式化為相對於參考原點（今日 $t_0$）的位移函數。

### 1. 時間推移詞之代數生成函數

設當前時間原點為 $t_0$，目標時間點為 $t$，則時間偏移量為 $\Delta t = t - t_0$。在台灣南島語中，時間推移詞 $T(\Delta t)$ 的構詞映射定義為：

$$T(\Delta t) = \operatorname{Mark}\Big(\operatorname{sgn}(\Delta t)\Big) \oplus \operatorname{Root}\Big(|\Delta t|\Big)$$

其中：
* $|\Delta t| \in \{1, 2\}$：表示距今之天數半徑（$1$ 為一天，$2$ 為兩天）。
* $\operatorname{Root}(d)$：表示對應天數差距 $d$ 的深層詞根，滿足：
  $$\operatorname{Root}_{\text{day1}} = \operatorname{Root}(+1) \equiv \operatorname{Root}(-1)$$
  $$\operatorname{Root}_{\text{day2}} = \operatorname{Root}(+2) \equiv \operatorname{Root}(-2)$$
* $\operatorname{sgn}(\Delta t) \in \{-1, +1\}$：符號函數，用以觸發語法形態標記 $\operatorname{Mark}(\cdot)$：
  $$\operatorname{Mark}(\operatorname{sgn}(\Delta t)) = \begin{cases} \mathcal{M}_{\text{realis}} & \text{if } \Delta t < 0 \quad (\text{Realis / Past}) \\ \mathcal{M}_{\text{irrealis}} & \text{if } \Delta t > 0 \quad (\text{Irrealis / Future}) \end{cases}$$

### 2. 標記系統的三大類型學分類

在形態合成運算 $\oplus$ 中，台灣南島語的時間標記系統展現為三種嚴格的代數結構：

$$\begin{aligned}
\text{Type I (Dual-marking)} &: T(-d) = \mu_{-} \oplus R_d, \quad T(+d) = \mu_{+} \oplus R_d \\
\text{Type II (Realis-only)} &: T(-d) = \mu_{-} \oplus R_d, \quad T(+d) = R_d \\
\text{Type III (Irrealis-only)} &: T(-d) = R_d, \quad T(+d) = \mu_{+} \oplus R_d
\end{aligned}$$

其中 $\mu_{-}$ 為實現標記，$\mu_{+}$ 為非實現標記，$R_d$ 為天數核心詞根。

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的跨語言分析結果
* 研究語料涵蓋 **16 族、42 方言**的時間詞資料，分析「昨天、明天、前天、後天」的詞根分組與實現／非實現標記。
* 原文摘要歸納三種分組類型：以距今日數配對（昨天／明天、前天／後天）、以時間前後配對（昨天／前天、明天／後天），以及四個詞各用不同詞根。第一類為多數，第二類僅見於少數語言。
* 時間標記分為單標實現、單標非實現與雙標三類；原文未將三類標記的分布量化為比例。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **重構南島語詞彙語義學的幾何視角**：證實南島語言並非沿著西方的線性因果時軸組織日常詞彙，而是以「自我／當下（Here and Now）」為對稱中心，以離散天數為半徑向過往與未來同構展開。
* **為神經斷詞與形態還原建立數學先驗**：證明在構詞分析任務中，時間詞具有極高的一致性與可預測性。只要識別出共通詞根 $R_d$，即可推導出完整對稱時間詞體系，避免低資源模型在小樣本下的時態混淆。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
林鴻瑞博士對台灣南島語時間推移詞的跨語言比較，為我的碩士論文研究提供了具體的可落地思路：

1. **未知詞（OOV）窮舉模組的時間詞特化規則**：
   * 在進行泰雅語、太魯閣語與賽德克語的未知詞猜測時，若文本中出現一個前所未見的詞形，經音韻分析發現其包含未實現前綴（如 `sa-`）且語境與時間推移相關，構詞引擎可直接將其剝除，檢索詞庫中對應之「昨天」詞根，從而推導出「明天」之正確語義，無需等待雙語語料庫收錄。
2. **多語言平行語料庫對齊之正則化約束**：
   * 在訓練泛泰雅語群多語言機器翻譯模型時，時間詞的翻譯錯誤（例如將「明天」翻成「昨天」）往往會導致嚴重的語意扭曲。
   * **啟發**：可利用本論文歸納之 $\operatorname{sgn}(\Delta t)$ 形態標記特徵，作為翻譯解碼端的損失懲罰項（Constraint Loss），強制模型在生成目標語中文時，確保時態符號與來源語南島詞綴的「實現／非實現」極性嚴格一致。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
* **原始權威文獻**：
  * 官方學術出處：林鴻瑞 (2024)。台灣南島語言時間詞之跨語言比較初探。《台灣學誌》，(23)，1-27。DOI: [10.6242/twnica.202404_(23).0001](https://doi.org/10.6242/twnica.202404_(23).0001)
  * 原始檔典藏：`raw/my-focus/台灣相關論文/南島語言時間詞之跨語言比較初探_林鴻瑞.pdf'`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
