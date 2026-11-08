---
title: "Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge: Russian-Kyrgyz"
title_zh: "以資料為中心之方法應用於 LoResMT 2026 突厥語翻譯挑戰賽：俄羅斯語至吉爾吉斯語"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Dmitry Novokshanov"
venue: "Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026), 225-230"
domain: "ai"
domain_tags: ["#自然語言處理", "#深度學習", "#人工智慧"]
concepts: ["low-resource-machine-translation"]
status: "wiki"
verification: "issues"
my_focus: true
focus_role: "llm-assisted"
focus_languages: ["吉爾吉斯語"]
doi_url: "https://doi.org/10.18653/v1/2026.loresmt-1.25"
hook: "斬獲 LoResMT 2026 突厥語翻譯競賽第一名桂冠：以 SONAR 跨語言語義過濾與四階段課程學習，確立極低資源神經翻譯『資料純度勝於模型複雜度』的黃金法則。"
---

# 以資料為中心之方法應用於 LoResMT 2026 突厥語翻譯挑戰賽 (Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge)

> 「在低資源機器翻譯的競技場上，最致命的陷阱是試圖用複雜的神經網絡架構去硬吃充斥雜訊的語料。當你將每一道資料流水線清洗至極致純淨，最簡單的架構也能爆發出問鼎冠軍的驚人力量。」

**2026 發表 ｜ 個人核心研究關注**

---

## Card 1 ｜ 時代銘文 (The Hook)
在國際計算語言學頂級低資源競賽——第九屆低資源語言機器翻譯研討會（LoResMT 2026）的突厥語族翻譯挑戰賽中，俄羅斯語至吉爾吉斯語（Russian $\to$ Kyrgyz）翻譯任務吸引了全球眾多頂尖團隊參與角逐。俄羅斯國立高等經濟大學（HSE University）的 Dmitry Novokshanov 摒棄了盲目堆疊模型參數的軍備競賽，提出了一套極致的「以資料為中心（Data-Centric）」解決方案。該方案結合了 FineWeb-2 大規模合成回譯、Meta SONAR 跨語言語義打分過濾、以及精密的「四階段課程學習（Four-Stage Curriculum Learning）」，最終以 **$49.1$ chrF++** 的壓倒性高分力壓群雄，斬獲競賽全場第一名。

---

## Card 2 ｜ 世紀瓶頸：合成資料的毒化效應與混亂訓練進程 (The Dilemma)
在參與極低資源機器翻譯競賽與落地開發時，傳統工程師普遍受困於兩大痛點：

* **爬蟲與合成資料的「毒化陷阱（Data Poisoning）」**：為了擴充低資源語料，研究者常從網路大規模抓取單語文本進行回譯。然而未經嚴格把關的語料充斥著錯位對齊、機器翻譯垃圾（MTese）與非目標語言雜訊，直接訓練會導致神經網路注意力發散，生成文本語法嚴重退化。
* **無差別混洗訓練導致的梯度震盪**：傳統作法將高品質人工句對與粗糙合成句對混在一起隨機洗牌（Shuffle）進行訓練。這種做法忽視了學習規律，使模型在早期容易被雜訊誤導，在晚期又無法專注於核心領域的精細表達。

---

## Card 3 ｜ 突破架構與原理：SONAR 語意門檻過濾與四階段課程排程 (The Secret)

### 1. 基於 SONAR 的跨語言語義相似度品質分級

Novokshanov 採用 Meta 開源的最新多模態多語言語意表示模型 **SONAR**（blaser_2.0）對全量平行句對進行跨語言餘弦相似度打分：

$$S_{\text{SONAR}}(x, y) = \cos\Big( \operatorname{SONAR}(x), \operatorname{SONAR}(y) \Big)$$

依據打分設定嚴格的淘汰與品質分層門檻：
* **硬性淘汰區間**：$S_{\text{SONAR}} < 3.0$（直接剔除，判定為對齊錯位或嚴重幻覺句）；
* **標準品質層（Standard Quality）**：$3.0 \le S_{\text{SONAR}} < 3.7$；
* **黃金品質層（High Quality）**：$S_{\text{SONAR}} \ge 3.7$。

### 2. 四階段課程學習排程代數（Four-Stage Curriculum Learning）

系統不進行隨機混合，而是按照「由粗到精、由噪到純」嚴格劃分訓練階段：

$$\mathcal{L}_{\text{curriculum}}^{(k)}(\theta) = -\sum_{(x, y) \in \mathcal{D}_k} \sum_{t=1}^{|y|} \log P(y_t \mid y_{<t}, x; \theta), \quad k \in \{1, 2, 3, 4\}$$

1. **第 1 階段（通用預熱）**：在大規模 FineWeb-2 合成回譯語料庫（50 萬句）上進行粗預訓練；
2. **第 2 階段（多源混合）**：納入經過 SONAR 過濾之標準品質資料聯合訓練；
3. **第 3 階段（高質量微調）**：僅使用 $S_{\text{SONAR}} \ge 3.7$ 之高純度黃金平行句對進行退火微調；
4. **第 4 階段（領域內收斂）**：在受限之官方競賽真實驗證集上進行極低學習率正則化收斂。

```text
[FineWeb-2 50 萬吉爾吉斯語單語] ──► [大模型回譯生成] ──┐
                                                        ├──► [Meta SONAR 語義打分] ──► 剔除 S < 3.0
[官方俄吉平行訓練集]             ────────────────────────┘                                    │
                                                                                             ▼
[第 4 階段：域內收斂] ◄── [第 3 階段：黃金微調] ◄── [第 2 階段：混合過渡] ◄── [第 1 階段：合成預熱] ◄─┘
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 本篇論文的共享任務結果
* 本文描述 LoResMT 2026 突厥語翻譯挑戰賽的俄語至吉爾吉斯語系統，採用平行資料、合成翻譯、資料過濾與四階段課程式訓練。
* 作者報告最終系統在競賽測試資料達 **49.1 chrF++**、**69.7 xCOMET-XXL**，並在俄語至吉爾吉斯語賽道排名第一。
* 本卡依原文摘要與共享任務測試結果，列出競賽的主要評估指標。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **實踐「以資料為中心（Data-Centric AI）」的終極勝利**：向整個 NLP 界展示了：在低資源機器翻譯中，資料的「純度（Purity）」與學習排程的「次序（Order）」遠比模型架構的修修改改更具決定性威力。
* **普及了現代語義過濾器（如 SONAR）在低資源任務中的黃金標準地位**：宣告了傳統單純依賴長度比、字典重合率等粗糙啟發式規則過濾時代的終結。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

### 對個人碩士論文研究之映射與啟發
Novokshanov 奪得 LoResMT 冠軍的資料中心管線，為我的碩士論文研究提供了極高指導價值的落地實踐手冊：

1. **南島語平行語料庫的嚴格語義過濾**：
   * 在使用原民會線上辭典例句、族語 E 樂園或網路爬取的南島語教材時，我們常常直接將資料送進模型。
   * **啟發**：必須引入現代跨語言嵌入評估工具（如微調後的跨語言模型或字串語素對齊度量），將對齊錯誤或譯文嚴重意譯失真的髒數據堅決剔除。少而精的黃金資料，能讓構詞解析器與翻譯模型學得更加精確。
2. **為臺灣南島語客製化「三階段課程學習」**：
   * 第一階段：以 Zheng (2024) 提出的辭典擴展全形態合成詞對進行基礎詞素預熱；
   * 第二階段：引入 FormosanMT 跨方言多語言平行資料進行語法泛化；
   * 第三階段：以目標方言之高品質人工校驗句進行收斂微調。此課程設計將使模型具備極強的抗噪能力與生成穩定度。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Novokshanov, D. (2026). Data-Centric Approach at the LoResMT 2026 Turkic Translation Challenge: Russian-Kyrgyz. In *Proceedings for the Ninth Workshop on Technologies for Machine Translation of Low Resource Languages (LoResMT 2026)* (pp. 225-230). DOI: [10.18653/v1/2026.loresmt-1.25](https://doi.org/10.18653/v1/2026.loresmt-1.25)
  * 原始檔典藏：`raw/my-focus/英文論文/llm 輔助/Data-Centric Approach at the LoResMT 2026 Turkic Translation.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
