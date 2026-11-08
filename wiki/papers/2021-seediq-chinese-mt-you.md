---
title: "A Study of Seediq-Chinese Machine Translation"
title_zh: "賽德克語－中文機器翻譯之研究"
paper_year: 2021
award_year: 2021
timeline_year: 2021
authors: "Jing-Sheng You"
venue: "Master's Thesis, Department of Computer Science and Engineering, National Taiwan Ocean University"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
my_focus: true
focus_role: "senior-thesis"
focus_languages: ["賽德克語"]
doi_url: "https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=y8Gq.y/record?yes=1"
hook: "奠定泛泰雅語群神經機器翻譯的開創性基石：提出深層原形構詞解析二元模型，結合自訓練詞嵌入與多維詞綴特徵向量拼接，突破極端低資源南島語翻譯難關。"
---

# 賽德克語－中文機器翻譯之研究 (A Study of Seediq-Chinese Machine Translation)

> 「當一種瀕危的南島語言在數位時代面臨語料荒漠時，計算語言學的使命不是盲目等待大數據的恩賜，而是深入其構詞紋理，以符號規則與神經嵌入的雙重骨架，重新架起通往母語理解的橋樑。」

**2021 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
賽德克語（Seediq）作為台灣高山南島語言之一，擁有高度繁複的構詞形態與動態焦點系統，但其現存雙語平行語料極度稀缺，且市售字典與線上教材均未提供結構化構詞標註。國立臺灣海洋大學林川傑教授指導、游景勝於 2021 年完成的碩士論文《賽德克語－中文機器翻譯之研究》，是實驗室在泛泰雅語群機器翻譯領域的開山奠基之作。該研究首創了一套從表面形還原「深層原形（Underlying Root）」的自動構詞解析流程，並將解析出的詞綴語法特徵向量化，與詞嵌入向量拼接送入神經機器翻譯網路，開啟了符號語言學與神經翻譯在台灣南島語上的深度整合。

---

## Card 2 ｜ 世紀瓶頸：雙重語料乾涸與焦點詞綴引發的 OOV 爆炸 (The Dilemma)
在建立賽德克語機器翻譯系統時，研究者面臨兩大核心瓶頸：

* **表面形極度分散導致的未登錄詞（OOV）氾濫**：賽德克語動詞具有多重前綴（如 `m-`、`p-`）、中綴（如 `-um-`、`-in-`）與後綴（如 `-an`、`-un`），同一個深層詞根可衍生出數十種表面形態。傳統統計機器翻譯或未經構詞處理的神經模型，會將這些衍生形視為彼此獨立的生詞，使得原本就極小的訓練集有效詞頻進一步被稀釋。
* **字典僅收錄靜態詞根與規則不透明**：原民會辭典多數僅提供孤立詞根，缺乏表面衍生形如何逆向還原為深層原形的演算法對照表，使深度學習模型難以捕捉焦點與時貌的語法實體。

---

## Card 3 ｜ 突破架構與原理：深層原形還原與詞綴向量拼接機制 (The Secret)

### 1. 構詞結構逆向解析管線

游景勝將構詞解析分為「中後綴匹配與原形還原」與「前綴二元轉移預測」兩大階段：

1. **候選深層原形生成與規則映射**：
   * 給定輸入詞 $w$，透過音韻變化逆向規則剝離可能的後綴與中綴，還原候選深層詞根 $r \in \mathcal{R}_{\text{cand}}$。
   * 將候選詞根 $r$ 重新組合測試，推導出前綴字串部分 $s_{\text{pre}}$。
2. **前綴組合之二元機率模型（Bigram Transition Model）**：
   * 賽德克語前綴常由多個語素依特定層次連續附加。建立前綴字串的 Bigram 轉移機率：
     $$P(s_{\text{pre}} \mid r) = \prod_{i=1}^{k} P(p_i \mid p_{i-1}, r)$$
   * 透過最大後驗機率（MAP）選取最優構詞切分結構：
     $$\langle r^*, \mathbf{a}^* \rangle = \arg\max_{r, \mathbf{a}} P(\mathbf{a} \mid r) \cdot \mathbb{I}(f_{\text{surface}}(r, \mathbf{a}) = w)$$

### 2. 神經機器翻譯端之詞綴特徵融合方程式

在翻譯編碼器（Encoder）端，游景勝捨棄單一表面詞向量，改採「語意向量」與「語法詞綴向量」的拼接結構：

$$\mathbf{x}_t = [\mathbf{e}_{\text{word}}(w_t) \,\|\, \mathbf{v}_{\text{affix}}(w_t)] \in \mathbb{R}^{d_{\text{word}} + d_{\text{affix}}}$$

其中：
* $\mathbf{e}_{\text{word}}(w_t) \in \mathbb{R}^{d_{\text{word}}}$：由自訓練 Skip-gram / FastText 學習之詞根或詞彙語義表示。
* $\mathbf{v}_{\text{affix}}(w_t) \in \{0, 1\}^{d_{\text{affix}}}$：由構詞解析器提取之多熱編碼（Multi-hot Encoding），精確標記主事焦點（AF）、受事焦點（PF）、完成貌（Perf）等構詞特徵。

```text
[輸入表面詞 w_t] ──► [構詞解析模組] ──► 詞綴特徵 a(w_t) ──┐
             └──► [自訓練 Skip-gram] ──► 詞嵌入 e(w_t)   ──┴──► [拼接 x_t] ──► [Encoder-Decoder NMT] ──► [中文譯文]
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的實驗結果
* **中綴與後綴結構辨識**：原文摘要報告精確率（precision）為 **99.52%**、召回率為 **85.34%**。99.52% 是 precision，不是 accuracy。
* **前綴結構預測**：含 back-off 與 Lidstone smoothing 的最佳二元機率模型，accuracy 為 **80.28%**。
* **機器翻譯**：最佳賽德克語翻中文系統 BLEU 為 **25.10**；中文翻賽德克語最佳系統為 **18.53**。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **開啟泛泰雅語群計算語言學研究脈絡**：本論文確立了實驗室後續數屆學長姐（戴晟哲、廖恒慶、楊鈞凱、金柏毅、吳維中）在臺灣南島語構詞解析與機器翻譯上的技術演進主軸。
* **證實「構詞先驗」對神經翻譯的救贖作用**：在算力與資料極端匱乏的世界角落，純端到端（Pure End-to-End）神經網絡往往會因過擬合而崩潰；將符號構詞規則轉化為特徵向量顯式注入網絡，是低資源 NLP 最行之有效的方法論。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
游景勝的奠基性工作為我的碩士論文研究帶來了深刻的第一手啟示：

1. **構詞特徵與現代 Transformer / LLM 架構的適配**：
   * 游景勝採用的是早期的向量拼接方法（Concatenation）。在現代以 Transformer 和大型語言模型為核心的架構下，詞綴資訊除了以數值向量輸入之外，更可以被顯式序列化為語意前綴 Prompt（例如：`[AF][Perf] 詞根`），使大語言模型在零樣本或檢索增強生成（RAG）時能直接「讀懂」語法標記。
2. **深層原形對檢索增強生成（RAG）語意對齊的關鍵價值**：
   * 當構詞解析器成功將表面形還原為深層原形 $r$ 時，RAG 模組便不再需要去模糊匹配龐大的表面變形，而是能以精準的深層原形為 Key，在辭典與文化知識庫中進行 $100\%$ 精確的向量與符號混合檢索，從根源消解低資源翻譯的幻覺問題。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 學位論文出處：游景勝 (2021)。賽德克語－中文機器翻譯之研究。國立臺灣海洋大學資訊工程學系碩士學位論文，指導教授：林川傑博士。
  * 原始檔典藏：`raw/my-focus/學長姐論文/賽德克族中文機器翻譯之研究_游景勝.pdf`（對應文字檔：`raw/my-focus/學長姐論文/.md/賽德克族中文機器翻譯之研究_游景勝.md`，由私有倉庫 Mine-RAW 版控）
