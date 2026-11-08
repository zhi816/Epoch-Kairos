---
title: "Automatic Analysis of Morphological Structure in Atayal and Truku"
title_zh: "泰雅語與太魯閣語構詞結構之自動解析"
paper_year: 2023
award_year: 2023
timeline_year: 2023
authors: "Cheng-Che Dai"
venue: "Master's Thesis, Department of Computer Science and Engineering, National Taiwan Ocean University"
domain: "ai"
domain_tags: ["#計算語言學", "#自然語言處理", "#人工智慧"]
concepts: ["formosan-computational-linguistics"]
status: "wiki"
my_focus: true
doi_url: "https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=y8Gq.y/record?yes=1"
hook: "將南島語構詞自動解析體系由單一賽德克語跨越至泰雅語與太魯閣語，建立音韻縮減與深層原形歸納規則，實現高精度構詞結構與焦點語素自動解耦。"
---

# 泰雅語與太魯閣語構詞結構之自動解析 (Automatic Analysis of Morphological Structure in Atayal and Truku)

> 「語言學語法書記錄的是語言的靜態切片，而計算解析系統必須學會動態還原音素在喉嚨與齒唇間流轉時被壓縮、弱化甚至抹去的深層原形。」

**2023 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
繼游景勝 (2021) 成功建立賽德克語構詞解析系統後，如何將該技術體系遷移並適配至泛泰雅語群的其他重要分支，成為低資源計算語言學的關鍵挑戰。國立臺灣海洋大學林川傑教授指導、戴晟哲於 2023 年 1 月完成的碩士論文《泰雅語與太魯閣語構詞結構之自動解析》，針對泰雅語（Atayal）與太魯閣語（Truku）各自獨特的音韻交替規律與縮減律（Phonological Contraction），首次建立了專屬於兩語種的深層原形歸納與構詞自動解析系統，大幅克服了語法教學書籍與線上辭典表面標記不一致的難題，為泛泰雅語群的機器翻譯與智慧辭典提供了強大的底層支持。

---

## Card 2 ｜ 世紀瓶頸：語法書表層切分缺陷與跨方言音韻交替壁壘 (The Dilemma)
在處理泰雅語與太魯閣語的構詞時，傳統計算模型面臨兩大核心瓶頸：

* **語法教材之表層切分不符計算需求**：現行《泰雅語語法概論》與詞類教學書籍中所提供的構詞範例，大多僅標記表層書寫形式的切分片段，並未將經歷音變（如母音省略、喉塞音脫落或鼻音同化）後的詞根還原為真正的「深層原形（Underlying Form）」，導致計算模型無法直接將切分結果與線上辭典的標準詞根進行關聯。
* **語種間構詞律之異質性**：泰雅語與太魯閣語雖同屬泛泰雅語群，但其音韻弱化模式（Vowel Weakening）、中綴插入優先級與重疊構詞（Reduplication）規則存在顯著差異，直接套用賽德克語的二元轉移機率模型會產生嚴重的誤切與召回率驟降。

---

## Card 3 ｜ 突破架構與原理：深層原形音韻逆向還原代數 (The Secret)

### 1. 音韻交替與構詞合成運算子

戴晟哲將一個複合詞的表面生成過程形式化為結合詞根、前綴、中綴與後綴的多階段音韻變換系統：

$$w_{\text{surface}} = \pi_{\text{phon}}\Big( a_{\text{pre}} \circ (r \odot a_{\text{in}}) \circ a_{\text{suf}} \Big)$$

其中：
* $r \in \mathcal{R}_{\text{deep}}$：深層原形詞根。
* $a_{\text{pre}}, a_{\text{in}}, a_{\text{suf}}$：分別為前綴、中綴與後綴語素。
* $\odot$：中綴嵌入運算子（通常插入於深層詞根首個輔音之後）。
* $\pi_{\text{phon}}(\cdot)$：音韻交替算子，包含三大微觀音變函數之複合：
  $$\pi_{\text{phon}} = \phi_{\text{assim}} \circ \phi_{\text{del}} \circ \phi_{\text{vshift}}$$
  分別為母音弱化移位 $\phi_{\text{vshift}}$、輔音與喉塞音省略 $\phi_{\text{del}}$、以及鼻音部位同化 $\phi_{\text{assim}}$。

### 2. 逆向構詞解析架構

解析系統由表面詞 $w_{\text{surface}}$ 逆向尋找最優語素分解組配 $\langle r^*, \mathbf{a}^* \rangle$：

$$\langle r^*, \mathbf{a}^* \rangle = \arg\max_{\langle r, \mathbf{a} \rangle \in \Omega(w)} \Big[ S_{\text{rule}}(r, \mathbf{a}) + \lambda \log P_{\text{bigram}}(a_{\text{pre}} \mid r) \Big]$$

其中 $\Omega(w)$ 為依據反音變規則生成的所有合法候選集，$S_{\text{rule}}$ 為基於語法約束之符號相容性得分，$P_{\text{bigram}}$ 為前綴鏈之轉移機率。

```text
[輸入表面詞 w] ──► [反向音變候選生成] ──► {候選深層原形 r_cand}
                                             │
      ┌──────────────────────────────────────┘
      ▼
[詞典檢索與深層原形驗證] ──► [中後綴對齊過濾] ──► [前綴二元轉移排序] ──► 最優構詞解析結果
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的構詞解析結果
* **中綴與後綴解析**：泰雅語與太魯閣語的實驗中，精確率均高於 **95%**，召回率落在 **90–95%**。
* **前綴解析**：納入邊界資訊並使用 smoothing 的二元機率模型，在泰雅語測試集 accuracy 為 **96.43%**，太魯閣語為 **85.71%**。


---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **由單一語言走向語群模組化設計**：證明了以「深層原形 + 音韻交替算子 + 統計轉移排序」為核心的構詞解析框架，具備高度的跨語言可擴展性（Scalability），無須為每種南島語重寫整套演算法，僅需替換語種特異性之音變規則矩陣。
* **學術語法與計算系統的無縫橋接**：建立了將傳統田野語言學調查語法書轉化為可執行計算規則庫的標準化工程範例。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
戴晟哲的研究為我的碩士論文研究奠定了極為關鍵的計算語言學模組基礎：

1. **構詞分析器是所有下游南島語 NLP 任務的第一道濾網**：
   * 機器翻譯與檢索增強生成（RAG）若直接處理未切分的表面詞，會因資料稀疏而產生災難性的注意力發散。戴晟哲證明了深層原形還原準確率可達 $90\%$ 上下，這意味著我們可以在預處理階段將整個南島語輸入序列分解為乾淨的「深層詞根序列 + 語法標籤序列」。
2. **對未知詞（OOV）解析之反思**：
   * 戴晟哲的方法高度依賴線上辭典之詞根庫。然而在實際翻譯任務中，有相當比例的詞根連辭典都未曾記載。這啟發了我後續必須結合構詞窮舉、字元級語言模型與語意向量空間檢索，補齊「辭典外未知詞根」的預測閉環。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
* **原始權威文獻**：
  * 學位論文出處：戴晟哲 (2023)。泰雅語與太魯閣語構詞結構之自動解析。國立臺灣海洋大學資訊工程學系碩士學位論文，指導教授：林川傑博士。
  * 原始檔典藏：`raw/my-focus/學長姐論文/泰雅與太魯閣 構詞結構之自動解析_戴成哲.pdf`（對應文字檔：`raw/my-focus/學長姐論文/.md/泰雅與太魯閣 構詞結構之自動解析_戴成哲.md`，由私有倉庫 Mine-RAW 版控）
