---
title: "Language Model Priors and Data Augmentation Strategies for Low-resource Machine Translation: A Case Study Using Finnish to Northern Sámi"
title_zh: "語言模型先驗與資料增強策略在低資源機器翻譯之應用：以芬蘭語至北薩米語為例"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Jonne Sälevä, Constantine Lignos"
venue: "Findings of the Association for Computational Linguistics: ACL 2024, 12949-12956"
domain: "ai"
domain_tags: ["#自然語言處理", "#深度學習"]
concepts: ["low-resource-machine-translation"]
status: "wiki"
verification: "verified"
my_focus: true
focus_role: "report"
focus_languages: ["北薩米語"]
doi_url: "https://doi.org/10.18653/v1/2024.findings-acl.768"
hook: "以約 2.5 萬句平行語料的芬蘭語→北薩米語為例，比較回譯、標記回譯、正譯與語言模型先驗：充分訓練的基線即比前人高近 8 BLEU，最佳回譯模型達 41.75 BLEU，但各技術的效果隨測試領域而不同。"
---

# 語言模型先驗與資料增強策略在低資源機器翻譯之應用：以芬蘭語至北薩米語為例 (Language Model Priors and Data Augmentation Strategies for Low-resource Machine Translation)

> 「在低資源機器翻譯的漫長探索中，合成資料（Synthetic Data）是一把雙刃劍：若未經標記與結構約束，它會稀釋真實語言的分佈；若賦予清晰的來源感知標籤，它能成為模型抵禦領域偏移的最堅固護盾。」（本頁引言為 Wiki 撰寫，非原文）

**2024 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Sälevä & Lignos（Brandeis University），*Findings of ACL 2024*, pp. 12949–12956。本文延伸 Aulamo et al. (2021) 的北薩米語－芬蘭語翻譯研究。

---

## Card 1 ｜ 時代銘文 (The Hook)
北薩米語約有 25,000 名使用者，是薩米語中使用者最多的一種（§1, p. 12949）。本文研究如何利用來源語與目標語兩端的單語資料，改善芬蘭語→北薩米語翻譯。作者列出四項貢獻：
1. 大型多語模型 MADLAD-400（3B）在此語言對的品質「無法使用」，翻成北薩米語僅 1.92 BLEU（表 1）；
2. Aulamo et al. (2021) 的純平行語料基線訓練不足，充分訓練後提升近 8 BLEU；
3. 試驗多種正譯與回譯組合，發現好的表現與大資料量、以及在回譯資料中加入規則式翻譯系統（RBMT）輸出有關；
4. 將以含雜訊目標端回譯訓練的模型與語言模型先驗等既有技術結合（§1）。

---

## Card 2 ｜ 世紀瓶頸：平行語料極少，合成資料又可能喧賓奪主 (The Dilemma)
* **平行語料只有 25,106 句**（表 2）；回譯與正譯可擴充到約 190 萬句，作者擔心大量合成資料「排擠」真實平行資料，因此嘗試在合成句前加 `<BT>` 標記（§3.1, p. 12950）。
* **域外表現差距大**：UiT 測試集（域內，網頁、多為政治文本）與 YLE 測試集（域外，新聞，151 句）的分數差距很大，例如基線分別為 26.86 與 8.43 BLEU（表 3–5）。
* **大型多語模型無法直接解決**：作者以 QLoRA 微調 MADLAD-400 的初步實驗仍低於 10 BLEU（註 2, p. 12950）。

---

## Card 3 ｜ 突破架構與原理：回譯、正譯、標記與語言模型先驗 (The Secret)

### 1. 資料增強（§3.1, p. 12950；附錄圖 1）
* **回譯**：先訓練北薩米語→芬蘭語的反向 Transformer。反向模型的訓練資料除平行語料外，另加入 Aulamo et al. 的 RBMT 系統所產生的合成回譯（即以合成輸出作為訓練目標）。再以兩個反向模型把北薩米語單語資料譯成芬蘭語，得到兩組回譯。
* **正譯**：以芬蘭語→北薩米語模型，把 mC4 語料中約 95 萬句**芬蘭語**單語資料譯成北薩米語。
* **標記回譯**：在合成句前加上 `<BT>` 作為第一個詞元。

### 2. 語言模型先驗（§3.2, p. 12950）
依 Baziotis et al. (2020)，以北薩米語單語資料訓練自迴歸 Transformer 語言模型，作為 $p_{\text{NMT}}(y_t \mid x, y_{<t})$ 的弱資訊先驗。在詞元層級的翻譯對數概似損失上加一項 KL 散度正則項（原文式）：

$$J(\theta) = -\log P_{\text{NMT}}(y \mid x) + \lambda\, D_{\text{KL}}\big(p_{\text{LM}}(y) \,\|\, p_{\text{NMT}}(y \mid x)\big)$$

KL 散度的方向是由語言模型分布指向翻譯模型分布。語言模型在訓練中凍結，只更新翻譯模型。

### 3. 模型設定（§4.1, p. 12951）
Transformer-base（編碼器、解碼器各 6 層，512 維嵌入，2048 維前饋層），標籤平滑 0.1；SentencePiece unigram 子詞，來源與目標分開，詞彙 8,000（語言模型實驗為 5,000）。

```text
[北薩米語單語] ──► 反向模型（北薩米語→芬蘭語；部分以 RBMT 合成資料訓練）──► 回譯句對 ──┐
[芬蘭語單語（mC4）] ──► 正向模型（芬蘭語→北薩米語）──► 正譯句對 ─────────────────────┤（可加 <BT>）
[25,106 句平行語料] ─────────────────────────────────────────────────────────────┴──► 芬蘭語→北薩米語 Transformer
（另一路線：不擴充資料，改以凍結的北薩米語語言模型作 KL 正則項）
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 芬蘭語→北薩米語（表 3–5, pp. 12952–12953）
| 系統 | UiT BLEU／chrF | YLE BLEU／chrF |
|---|---|---|
| 基線（純平行語料；Aulamo 報告 18.9 BLEU） | 26.86／58.60 | 8.43／35.67 |
| ＋正譯 | 25.93／59.52 | 9.01／36.99 |
| ＋語言模型先驗 | 31.26／62.99 | 8.60／37.41 |
| Transformer-BT（RBMT） | 37.22／67.89 | **16.34**／47.46 |
| Transformer-BT（combined） | **41.75**／70.12 | 14.96／45.93 |
| combined ＋標記 | 41.71／70.33 | **19.20**／**48.60** |
| combined ＋正譯 | 38.96／69.16 | 17.91／48.60 |
| combined ＋正譯＋標記 | 38.84／69.10 | 17.36／48.19 |
| combined ＋語言模型先驗 | 33.30／65.69 | 14.51／45.52 |

* 最佳 UiT 模型比 Aulamo 報告的最佳 40.1 BLEU 高 1.65（§4.2）。
* **標記的效果不一致**：作者明言「在某些情況有益、在其他情況沒有」（§4.3）。UiT 上 BLEU 微降（41.75 → 41.71）、chrF 微升；YLE 上提升 4.24 BLEU；與正譯併用時，UiT 與 YLE 的 BLEU 反而都比不加標記略低。
* **原文數字不一致**：§4.3 內文寫最佳模型加語言模型先驗後為 33.80 BLEU，表 5 為 33.30。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **作者的結論**：已展示多種以合成資料擴充極小平行語料的方法；在缺乏大型公開單語資料時，語言模型先驗可能是另一種正則化途徑（§5）。對最佳回譯模型而言，加語言模型先驗反而大幅降低 UiT 分數，作者推測回譯資料可能已提供足夠的正則化。
* **正譯在域內有害、域外有益**：作者推測與領域不符有關（UiT 多為政治文本，正譯資料較一般），不應據此全面否定正譯（§4.3）。
* **作者自述的限制**：只研究單一語言對，且每個實驗只跑一次；作者特別提醒讀者不要過度外推結果（Limitations）。
* 本文沒有主張「回譯資料量充足時必須全面採用標記回譯」。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為使用者個人研究之延伸思考（Wiki 詮釋），非原文主張。

### 對個人碩士論文研究之映射與啟發

1. **回譯與標記值得在臺灣南島語上對照實驗**：
   * 本文顯示 `<BT>` 標記在域外測試集上有明顯幫助、在域內幾乎沒有差別，而與正譯併用時甚至略降。若在臺灣南島語上做回譯，應同時比較有無標記，並分開報告域內與域外結果，而不是預設一律加標記。
2. **建立域外測試集**：
   * 本文的 UiT／YLE 對比說明單一域內測試集可能高估效果。臺灣南島語研究常以辭典例句交叉驗證（參見廖恒慶 2023 的覆蓋度問題），可考慮另建不同來源的測試集。
3. **規則式系統的價值**：
   * 本文的回譯資料加入 RBMT 輸出後表現較好。臺灣南島語若已有規則式或構詞規則系統，也可能作為合成資料的來源之一。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Sälevä, J., & Lignos, C. (2024). Language Model Priors and Data Augmentation Strategies for Low-resource Machine Translation: A Case Study Using Finnish to Northern Sámi. In *Findings of the Association for Computational Linguistics: ACL 2024* (pp. 12949-12956). DOI: [10.18653/v1/2024.findings-acl.768](https://doi.org/10.18653/v1/2024.findings-acl.768)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2024.findings-acl.768.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2024-finnish-northern-sami-mt-saleva.md](../evidence/2024-finnish-northern-sami-mt-saleva.md)
