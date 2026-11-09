---
title: "Improving Taiwanese Machine Translation Systems by Word Re-Segmentation"
title_zh: "利用重斷詞改善台語機器翻譯系統"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Hsih-Min Tang"
venue: "Master's Thesis, Department of Computer Science and Engineering, National Taiwan Ocean University"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "wiki"
verification: "issues"
my_focus: true
focus_role: "senior-thesis"
focus_languages: ["台語"]
hook: "針對本土低資源語言語料庫斷詞標準不一的痛點，提出基於華語跨語言詞對齊與 BERT 預訓練模型的台語重斷詞管線，顯著改善台華神經機器翻譯效能。"
---

# 利用重斷詞改善台語機器翻譯系統 (Improving Taiwanese Machine Translation Systems by Word Re-Segmentation)

> 「斷詞是語意理解的第一塊骨牌。在歷史書寫規範分歧的本土語言中，校準文字切分的邊界，本質上就是在梳理兩種語言在深層思維結構上的平行對應。」

**2024 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
台語（臺灣閩南語）作為臺灣本土重要的低資源語言，近年雖累積了部分雙語語料庫，但因歷史書寫習慣、漢字與羅馬字拼寫多樣性以及缺乏統一的斷詞規範，現存資料集中存在嚴重的斷詞不一致與任意切分問題。國立臺灣海洋大學林川傑教授指導、湯景閔於 2024 年 7 月完成的碩士論文《利用重斷詞改善台語機器翻譯系統》，針對 TGB 通訊與 iCorpus 等核心台華平行語料庫，首創結合華語跨語言詞對齊導向與 BERT 預訓練斷詞模型的「台語重斷詞（Re-Segmentation）」管線，有效校準了雙語切分顆粒度，為本土語言機器翻譯消除了因預處理瑕疵引發的系統性雜訊。

---

## Card 2 ｜ 世紀瓶頸：斷詞規範漂移與雙語顆粒度錯位 (The Dilemma)
在建立高品質台語－華語機器翻譯系統時，資料層面存在兩大結構性障礙：

* **非標準化標註引發的斷詞噪音**：不同作者在撰寫台語文本時未遵循統一標準，有時將多字詞拆為單字，有時將整個片語連寫為不可分割的長詞。這種切分邊界的漂移直接導致詞彙表（Vocabulary）膨脹，出現大量人工製造的偽未登錄詞（Pseudo-OOVs）。
* **台華雙語切分顆粒度不對稱（Granularity Mismatch）**：華語端以現代漢語規範詞切分，而台語端若切分過粗或過細，會導致注意力矩陣在跨語言對齊時無法形成清晰的單射或雙射關聯，迫使神經網路消耗大量參數去擬合斷詞雜訊。

---

## Card 3 ｜ 突破架構與原理：雙語對齊約束與 BERT 重斷詞引擎 (The Secret)

### 1. 雙語平行對齊引導之重斷詞數學模型

湯景閔利用平行句對中高品質的華語端切分作為參考坐標，透過統計詞對齊模型（如 IBM Model 或 fast_align）反向優化台語端切分邊界。

給定台語未切分或粗切分字元序列 $\mathbf{c} = (c_1, c_2, \dots, c_m)$ 及對應華語標準分詞序列 $\mathbf{t}_{\text{zh}} = (t_1, t_2, \dots, t_n)$，最優重斷詞劃分 $\mathcal{S}^*$ 形式化為雙語互資訊與單語語言模型先驗的聯合最大化：

$$\mathcal{S}^* = \arg\max_{\mathcal{S} \in \Pi(\mathbf{c})} \left[ \sum_{(w_i, t_j) \in \mathcal{A}(\mathcal{S}, \mathbf{t}_{\text{zh}})} \operatorname{PMI}(w_i, t_j) + \alpha \sum_{i=1}^{|\mathcal{S}|} \log P_{\text{BERT}}(w_i \mid w_{<i}) \right]$$

其中：
* $\Pi(\mathbf{c})$：字元序列 $\mathbf{c}$ 的所有可能合法切分集合。
* $\mathcal{A}(\mathcal{S}, \mathbf{t}_{\text{zh}})$：台語詞候選與華語詞之跨語言雙向最佳對齊路徑。
* $\operatorname{PMI}(w_i, t_j) = \log \frac{P(w_i, t_j)}{P(w_i)P(t_j)}$：雙語詞對之點互資訊。
* $P_{\text{BERT}}$：基於台語預訓練 BERT 提取之上下文流暢度得分。

### 2. BERT 序列標註重斷詞架構

針對缺乏平行對齊的單語台語句，採用 BERT 搭配 $\text{B-I-E-S}$ 標註體系進行字級序列標註：

$$y_k^* = \arg\max_{y \in \{\text{B}, \text{I}, \text{E}, \text{S}\}} \operatorname{softmax}\big( W_{\text{cls}} \mathbf{h}_k + \mathbf{b} \big)_y$$

其中 $\mathbf{h}_k$ 為 BERT 第 $k$ 個字元的頂層隱藏狀態表示。

```text
[台語原始句子] ──► [台語 BERT 序列標註器 (B-I-E-S)] ──┐
                                                    ├──► [規範化台語分詞] ──► [Transformer NMT] ──► [高品質華語譯文]
[平行華語句子] ──► [跨語言統計對齊約束 (fast_align)] ─┘
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的重斷詞與翻譯結果
* **TGB 通訊語料**：直接對原始台語斷詞重斷詞後，台語翻華語 BLEU 為 **42.82**（較原始斷詞 **+7.56**），華語翻台語為 **43.93**（**+5.74**）。
* **先以 BERT 斷詞再重斷詞**：TGB 上華語翻台語／台語翻華語分別為 **50.09／43.47 BLEU**；iCorpus 上分別為 **78.92／79.02 BLEU**。
* 原文以翻譯 BLEU 評估重斷詞效益；此卡依資料集與翻譯方向列出分數。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **凸顯「資料品質與預處理」在極低資源領域的決定性價值**：證明了在低資源翻譯中，盲目擴大模型參數或套用複雜注意力機制，遠不如在前端精雕細琢「斷詞與對齊品質」所帶來的效益直接。
* **為非標準化本土語言建立跨語言引導斷詞之方法論範本**：該方法可直接推廣至客語、原住民語等存在書寫規範歷史包袱的低資源語言。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
湯景閔在台語重斷詞上的研究，對我的臺灣南島語機器翻譯與構詞解析研究提供了深刻反思：

1. **南島語構詞切分與斷詞的對齊標準**：
   * 臺灣南島語目前大部分以羅馬拼音書寫，單詞邊界通常以空格分開。但由於構詞高度黏著，一個表面詞往往對應中文的一個完整短語。
   * **啟發**：我們在構詞解析時，不能只把南島語拆成「詞根 + 詞綴」，還必須考慮中文端的對應切分顆粒度。將中文端適度以多字詞進行組合，使「南島語焦點動詞」與「中文動賓結構」在語意長度上達到平衡，能極大化降低神經機器的跨語言注意力發散。
2. **預訓練語言模型在符號校準中的角色**：
   * 利用 BERT 等模型作為約束正則項，能有效結合先驗統計知識與上下文動態語境，這可借鑒於我的未知詞（OOV）排序器設計中。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 學位論文出處：湯景閔 (2024)。利用重斷詞改善台語機器翻譯系統。國立臺灣海洋大學資訊工程學系碩士學位論文，指導教授：林川傑博士。
  * 原始檔典藏：`raw/my-focus/學長姐論文/利用重斷詞改善台語機器翻譯系統_湯景閔.pdf`（對應文字檔：`raw/my-focus/學長姐論文/.md/利用重斷詞改善台語機器翻譯系統_湯景閔.md`，由私有倉庫 Mine-RAW 版控）
