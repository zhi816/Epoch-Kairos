---
title: "Tokenizations for Austronesian Language Models: study on languages in Indonesia Archipelago"
title_zh: "南島語系語言模型的音節分詞法：印尼群島地方語言研究"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Andhika Bernard Lumbantobing, Hokky Situngkir"
venue: "arXiv preprint arXiv:2602.06998"
domain: "ai"
domain_tags: ["#人工智慧", "#自然語言處理", "#計算語言學"]
concepts: ["low-resource-machine-translation"]
status: "published"
verification: "verified"
my_focus: true
focus_role: "report"
focus_languages: ["印尼南島諸語"]
doi_url: "https://arxiv.org/abs/2602.06998"
hook: "借鏡印尼群島傳統音素音節文字（aksara / abugida）的消元音（virama）與複輔音書寫規則，建構僅 2,843 詞元的音節切分框架，在 NusaX 十種印尼南島語上以 ~0.4 穩定字元詞元比大幅降低碎片化，並使跨語言局部序列相似度較 GPT-2 BPE 平均高出約 21%。"
card_line: "借傳統書寫邏輯，依音節單位切分南島語詞元"
key_papers:
  - "Ali et al. (2024) Tokenizer choice for LLM training: Negligible or crucial? NAACL 2024 Findings / arXiv:2310.08754"
  - "Winata et al. (2023) NusaX: Multilingual parallel sentiment dataset for 10 Indonesian local languages. EACL 2023"
  - "Smith & Waterman (1981) Identification of common molecular subsequences. Journal of Molecular Biology 147(1):195-197"
  - "Blust (2013) The Austronesian languages (rev. ed.). Asia-Pacific Linguistics"
---

# 南島語系語言模型的音節分詞法：印尼群島地方語言研究 (Tokenizations for Austronesian Language Models)

> 「依英語網路語料統計壓縮出來的子詞詞表，往往會把南島語的黏著詞綴與雙音節詞根切得支離破碎；與其硬套純頻率演算法，不如回到群島傳統文字原本的音節切分邏輯。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Lumbantobing（Bandung Fe Institute / InaAI）與 Situngkir（AI Research Center IT Del / Bandung Fe Institute），*arXiv:2602.06998v1*（版本日期 2026 年 1 月 27 日，arXiv 上架 2026 年 1 月 28 日）。本研究提出模擬印尼傳統 *aksara* 書寫體系的拉丁字母音節分詞器，僅以印尼大辭典（KBBI）建立 2,843 個詞元之音節詞表，並於 NusaX-MT 1,000 筆平行句上對照 GPT-2 BPE 檢驗每字元詞元數（TPC）與跨語言序列相似度（未執行下游生成或微調訓練）。

---

## Card 1 ｜ 時代銘文 (The Hook)

分詞（Tokenization）決定了語言模型如何把連續文字離散化為內部運算符號（§1, p. 1）。當代大語言模型幾乎全面採用基於統計壓縮的 BPE、WordPiece 或 Unigram 子詞切分；一旦訓練語料高度向英語傾斜，產生的子詞詞表就會反映英語字頻與音節規則，移植到構詞黏著且語料稀缺的南島語系語言時，容易把雙音節詞根與前綴、中綴、後綴拆成缺乏語義或音韻一致性的零散字元片段（§1, pp. 1–2）。

Lumbantobing 與 Situngkir（2026）於預印本提出一條語言家族導向的解決路線：把原本已失落卻仍保留在印尼爪哇、峇里、巽他、巴塔克與雷讓等傳統 *aksara*（元音附標音節文字，*abugida*）中的**音節劃分與元音抑制規則**，形式化為可執行於現代拉丁拼音南島語文本的確定性切分程序。僅以標準印尼語詞典（KBBI）高頻音節建置僅 **2,843 個詞元**的精簡詞表，在 NusaX 十種印尼地方語言的跨語言遷移試驗中展現出一致的字元壓縮比（~0.4）與更高的跨語序列幾何保真度（摘要 p. 1；§3–§4, pp. 5–11）。

---

## Card 2 ｜ 世紀瓶頸：統計壓縮詞表、音素碎片與整詞詞表爆炸 (The Dilemma)

研究指出，針對具雙音節（`CV(C)CVC`）詞根傾向與高黏著詞綴變化的南島語系語言，既有分詞設計卡在三重兩難之中（§1–§2, pp. 1–3）：

* **統計子詞法受英語語料偏斜主導**：如 GPT-2 的 BPE（50,257 詞元）為了壓縮英語高頻長詞串而生，面對語料量稀少的印尼群島地方語言時，傾向將實詞拆成短碎片與散落位元組，雖表面上未必極度拉高詞元數，卻掩蓋了真實的構詞與音節邊界（§1, pp. 1–2；§4.4, p. 10）。
* **純音素切分遺失韻律結構**：以單一音素或字母字元作為詞元雖能免於未登錄詞，卻無法承載南島語以「音節」為核心的韻律節奏與雙音節詞根骨架（§2, p. 3）。
* **整詞詞表引發未登錄詞爆炸**：南島語言透過前綴、後綴、中綴、環綴與重疊大量衍生詞形，若直接使用整詞切分，在有限詞表預算下會觸發極高的未登錄詞（OOV）比率，迫使系統難以收斂（§2, p. 3）。

---

## Card 3 ｜ 突破原理：模擬傳統音節文字規則的三階段切分與字元退回 (The Secret)

作者從印尼多種傳統 *aksara* 文字系統抽取共通的聲母（onset $\omega$）、韻核（nucleus $\nu$）與韻尾（coda $\kappa$）處理法則（Table 1–3, pp. 4–5），定義切分程序 $P: \Sigma^* \to T^*$ 將輸入字母序列 $S$ 映射為音節三元組序列 $U = (u_1 \dots u_k)$（§3, pp. 5–6）：

1. **階段一 $\phi_{\mathrm{scan}}$（線性掃描與二合輔音／介音組合）**：辨識雙字母單音輔音 $D = \{th, dh, \dots\}$ 與傳統字體允許進入介音的流音／半元音 $M = \{r, l, w, \dots\}$，並標出含特殊韻尾附加符號之集合 $H = \{ng, h, l, \dots\}$；若某輔音後不緊接元音，先標為暫缺韻核之單元 $u = (\omega, \varnothing, \varnothing)$（§3, pp. 5–6，式 (1)–(2)）。
2. **階段二 $\phi_{\mathrm{vir}}$（模擬 *virama* 消元音回溯歸併）**：由右向左掃描，模擬傳統文字用 *pangkon / adeg-adeg / pangolat* 消去基底字母固有元音的作用，將無韻核單元併入前一音節的韻尾；**階段三 $\phi_{\mathrm{clus}}$（借詞複輔音前向歸併）**則由左向右處理殘留之現代借詞複輔音，併入下一音節的聲母（§3, p. 6，式 (3)–(4)）：

$$
\begin{aligned}
\nu(u_i) = \varnothing &\Rightarrow \kappa(u_{i-1}) \leftarrow \kappa(u_{i-1}) + \omega(u_i) \\
\nu(u_i) = \varnothing &\Rightarrow \omega(u_{i+1}) \leftarrow \omega(u_i) + \omega(u_{i+1})
\end{aligned}
$$

三階段合成之完整音節切分算子寫為（§3, p. 6，式 (5)）：

$$P = (\phi_{\mathrm{clus}} \circ \phi_{\mathrm{vir}} \circ \phi_{\mathrm{scan}})$$

接著在印尼大辭典（KBBI）統計出音節出現頻率（服從冪律 $p(x)\sim x^{-\alpha}$，$\alpha\approx 1.87$，Fig. 1, p. 7）後，挑出高頻音節連同單字元基礎符號構成詞表 $\Sigma$（$|\Sigma| = 2,843$）。對罕見未收錄於 $\Sigma$ 的音節片段，由退回映射 $f_\Sigma$ 拆回單一字元避免未知符號，形成完整分詞映射（§4.1, p. 7，式 (6)）：

$$\tau_\Sigma = (f_\Sigma \circ P)$$

為比較跨語言相容性與片段保守度，作者進一步定義**每字元詞元數** $\mathrm{TPC}(S)$（§4.3.1, p. 8，式 (7)）與基於動態規劃（匹配 $+2$、錯配 $-1$、空位懲罰 $-1$）的 **Smith-Waterman 正規化詞元序列相似度**（§4.3.2, p. 9，式 (8)–(11)）：

$$\mathrm{TPC}(S) = \frac{|\tau_\Sigma(S)|}{|S|}$$

$$\mathrm{sim}(S_1, S_2) = \frac{\max(H)}{2 \times \sqrt{|\tau_\Sigma(S_1)| |\tau_\Sigma(S_2)|}}$$

---

## Card 4 ｜ 決定性數據：NusaX-MT 十種地方語言之 TPC 與序列對齊表現 (The Evidence)

實驗以印尼語大辭典（KBBI）訓出僅 **2,843** 詞元之音節詞表（對照組 **GPT-2 BPE** 為 **50,257** 詞元，相差近 18 倍），並於 **NusaX-MT** 平行語料全部 **1,000 筆**樣本上跨 10 種印尼地方語（亞齊語 `ace`、峇里語 `ban`、班查語 `bjn`、多巴巴塔克語 `bbc`、布吉語 `bug`、爪哇語 `jav`、馬都拉語 `mad`、米南佳保語 `min`、恩加朱語 `nij`、巽他語 `su`）加上印尼語 `id` 與英語 `en` 進行無訓練評估（§4.1–§4.4, pp. 7–11）：

| 評估指標 | 音節式分詞（KBBI 詞表 2,843） | GPT-2 BPE（詞表 50,257） | 論文來源位置 |
|---|---|---|---|
| **印尼語與十地方語 TPC** | **集中穩定於 ~0.4**（反映 2–3 音素 CV(C) 結構） | 分佈偏高（約 0.4 上下）且源於字元統計併合 | Abstract p. 1；§4.4, p. 10 Fig. 2 |
| **英語對照組 TPC** | 攀升至 **> 0.6**（英語音節觸發大量單字元退回） | **最低**（僅約 0.2–0.25，高度向英語壓縮） | §4.4, p. 10 Fig. 2 |
| **語言對相似度跨方法相關性** | Pearson **$r = 0.9956$**、Spearman **$\rho = 0.9895$** | —（作為比較基準） | §4.4, p. 11 |
| **跨語言序列相似度增益** | 全部地方語言對皆勝過 GPT-2，迴歸斜率 **$m \approx 1.21$（平均 +21%）** | — | Abstract p. 1；§4.4, p. 11 Fig. 3a |

* **親屬語分支對齊放大效果（Fig. 3b, p. 11）**：即使音節詞表僅來自印尼語 KBBI，與馬來語支近親（`IND–MIN +0.060`、`BJN–MIN +0.062`、`IND–BJN +0.059`）以及爪哇—峇里—巽他語群的局部同源音節對齊增益最為突出，展現跨語族共有的音節互換相容性（Internal compatibility）。

---

## Card 5 ｜ 典範轉移：語系共享音節詞表的啟示與當前驗證邊界 (The Revolution)

### 本篇技術位置與未來推進方向（ToBA-LM 路線，§5, pp. 11–12）
* **不依賴地方語數位文本訓練的零樣本音節相容性**：傳統子詞壓縮需蒐集目標地方語海量網頁語料才能學出合理合併表；藉共享同語族祖語音韻結構與傳統正字法邏輯，單靠印尼語辭典建立的精簡詞表即能對十種未見地方語保持一致的字元詞元比。
* **從單語語庫擴及古手稿與泛南島諸語**：作者指出此構架（定位為 ToBA-LM 路線之延伸步驟）未來可進一步擴及更廣泛的南島語系語言，並構想與印尼古文獻手稿掃描影像的傳統文字識別相結合（§5, p. 12）。

### 當前預印本研究邊界（v1 尚未驗證部分）
1. **僅止於分詞幾何與序列相似度量測**：論文於 NusaX 語料只進行了 TPC 統計與平行句對的 Smith-Waterman 比對，**尚未將此音節分詞器實際接入 Transformer 進行預訓練或下游機器翻譯（BLEU/chrF++）、情緒分析微調實驗**。
2. **純印尼語詞表限制與非南島外語懲罰**：英語詞彙大量退回為單字母導致 TPC 偏高（>0.6），顯示在多語混合實際部署時，若未納入跨語詞彙擴增或混合子詞策略，可能拖慢英語或其他非南島分析語的序列吞吐長度（§4.4, p. 10；§5, p. 12）。

---

## Card 6 ｜ KAIROS：傳統正字法裡的群島神經分詞密碼 (Cross-Disciplinary Inspiration)

> **本段為 Wiki 詮釋與跨領域啟發分析**：以下聯繫南島語機器翻譯與構詞研究，屬知識庫策展詮釋，非原論文作者所主張。

1. **當數位語料稀缺時，百年傳統文字早已寫好最優的分詞先驗**：在臺灣南島語與印尼南島語的[低資源神經機器翻譯](../concepts/low-resource-machine-translation.md)任務中，現代研究者常煩惱 BPE 找不到足夠語料來統計可靠的詞素邊界，因而轉向昂貴的手工標註或詞典窮舉。Lumbantobing 與 Situngkir（2026）揭示了一個精妙的文化演算法橋樑：祖先發展數百年的 *aksara* 元音附標體系，本身就是一套為當地語音結構度身定做的「天然音節切分器」。即使現代書寫已改為拉丁拼音，仍可用極少量的確定性規則還原這層音節視角，讓 2,843 個詞元在親屬語之間共用統一符號底座。
2. **詞元序列相似度的「同源詞顯影」效應**：分詞不僅影響推論速度，更決定了注意力機制看見哪些共享符號。把同源雙音節詞根與詞綴穩定切分成相同音節詞元（而非切入不同位置的任意位元組片段），能讓模型在跨方言或跨親屬語平行訓練時（如同臺灣泛泰雅語群、排灣語與魯凱語等多語共訓情境）更容易觸發同源共享注意力與梯度遷移——當然，這一正面效益在未來能否直接轉化為下游翻譯品質提升，仍待端對端預訓練實驗補完驗證。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Lumbantobing, A. B., & Situngkir, H. (2026). Tokenizations for Austronesian Language Models: study on languages in Indonesia Archipelago. *arXiv preprint arXiv:2602.06998v1*（2026-01-27 版）. [https://arxiv.org/abs/2602.06998](https://arxiv.org/abs/2602.06998)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026-tokenizations-austronesian-lms-lumbantobing.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-tokenizations-austronesian-lms-lumbantobing.md](../evidence/2026-tokenizations-austronesian-lms-lumbantobing.md)
