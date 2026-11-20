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
focus_tags: ["llm-assisted"]
focus_direction: "morphology"
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

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：Lumbantobing（Bandung Fe Institute / InaAI）與 Situngkir（AI Research Center IT Del / Bandung Fe Institute），*arXiv:2602.06998v1*（版本日期 2026 年 1 月 27 日，arXiv 上架 2026 年 1 月 28 日）。本研究提出模擬印尼傳統 *aksara* 書寫體系的拉丁字母音節分詞器，僅以印尼大辭典（KBBI）建立 2,843 個詞元之音節詞表，並於 NusaX-MT 1,000 筆平行句上對照 GPT-2 BPE 檢驗每字元詞元數（TPC）與跨語言序列相似度（未執行下游生成或微調訓練）。

---

## Card 1 ｜ 一句話看懂
這篇提出一套以「音節」為單位的分詞方法，把印尼群島地方語的文字切成音節詞元；詞表只靠印尼語大辭典（KBBI）建立，共 2,843 個詞元。作者把它和 GPT-2 的子詞分詞放在 NusaX-MT 的 1,000 句平行語料上比，看哪一種切法比較能保住跨語言的音節結構。結果是音節切法在十種地方語上維持約 0.4 的每字元詞元數，跨語的詞元序列相似度平均比 GPT-2 高約 21%（摘要, p. 1；§4.4, pp. 10–11）。

* **語言**：印尼十種地方語（亞齊語 `ace`、峇里語 `ban`、班查語 `bjn`、多巴巴塔克語 `bbc`、布吉語 `bug`、爪哇語 `jav`、馬都拉語 `mad`、米南佳保語 `min`、恩加朱語 `nij`、巽他語 `su`），另加印尼語與英語對照（§4.2, pp. 7–8）
* **任務**：分詞，也就是把文字切成模型內部運算用的詞元；不是翻譯或生成
* **方法**：模擬傳統 *aksara*（音節文字）的三階段音節切分，加上高頻音節詞表與字元退回（§3–§4.1, pp. 5–7）
* **資料或測試**：詞表取自印尼大辭典（KBBI）詞條的音節頻率；測試用 NusaX-MT 全部 1,000 句平行句（§4.1–§4.2, pp. 6–8）
* **公開**：原文沒有提及程式、詞表或資料是否公開，全文也沒有資料可得性（Data Availability）聲明（全文核查）
* **出處**：Lumbantobing 與 Situngkir（Bandung Fe Institute、AI Research Center IT Del），arXiv:2602.06998v1，2026 年 1 月 27 日版

---

## Card 2 ｜ 要解決的問題
南島語系的詞根多為雙音節（`CV(C)CVC`），又常用前綴、後綴、中綴、環綴與重疊造詞，一個衍生詞常有三、四個音節（§2, pp. 2–3）。現代大語言模型的分詞多採 BPE、WordPiece、Unigram 這類子詞方法，詞表由訓練語料的統計規律決定；語料若以英語為主，詞表自然反映英語的字頻與拼寫習慣（§1, pp. 1–2）。作者指出三種做法各有問題：

* **統計子詞法**：如 GPT-2 的 BPE（位元組對編碼，依字頻反覆合併字元的子詞法；詞表 50,257），是為了壓縮英語的高頻字串而設計；用到語料稀少的地方語時，會切出與音節、構詞邊界無關的碎片（§1, pp. 1–2；§4.4, p. 10）。
* **純音素切分**：只用單一音素或字母當詞元，雖然不會遇到詞表沒有的符號，卻抓不到南島語以音節為核心的韻律，也看不出雙音節詞根的骨架（§2, p. 3）。
* **整詞詞表**：黏著構詞讓詞形大量增生，詞表大小有限時會出現大量未登錄詞（OOV，詞表裡沒有的詞）（§2, p. 3）。

作者因此把**音節**當成設計單位：在雙音節詞根加上黏著詞綴的語言裡，音節是穩定又基本的組織層次（§2, p. 3）。這篇的想法：借傳統音節文字的規則切出音節詞元，讓同一份詞表跨語共用。

---

## Card 3 ｜ 方法流程
原文的流程是先做三段音節切分，再查詞表；整篇沒有訓練模型，也沒有下游實驗（§3–§4.1, pp. 5–7）。

1. **線性掃描**：由左往右讀字母序列，先認出二合字母（如 th、dh）與可當介音的流音、半元音（r、l、w），標出每個音節的聲母（onset，音節開頭的子音）與韻核（nucleus，音節核心，通常是元音）；後面沒有接元音的輔音，先記成缺韻核的單位（§3, pp. 5–6，式 (1)–(2)）。
2. **消元音回溯**：由右往左掃，模擬傳統文字用 *virama*（消元音符號，如爪哇語的 pangkon）去掉字母原有元音的做法，把缺韻核的單位併進前一個音節，當作韻尾（coda，收尾的子音）（§3, p. 6，式 (3)）。
3. **複輔音前向**：剩下沒有韻核的多半是現代借詞的複輔音，改由左往右，把這些單位併進下一個音節的聲母（§3, p. 6，式 (4)）。
4. **查詞表退回**：把 KBBI 詞條切出的音節按出現頻率排序，挑高頻音節加上基礎字元組成詞表；詞表沒有的音節，拆回單一字元，避免出現未知符號（§4.1, p. 7，式 (6)）。

原文把前三個階段寫成一個合成算子（§3, p. 6，式 (5)）：

$$P = (\phi_{\mathrm{clus}} \circ \phi_{\mathrm{vir}} \circ \phi_{\mathrm{scan}})$$

其中第二、三階段處理缺韻核單位的規則是（§3, p. 6，式 (3)–(4)）：

$$
\begin{aligned}
\nu(u_i) = \varnothing &\Rightarrow \kappa(u_{i-1}) \leftarrow \kappa(u_{i-1}) + \omega(u_i) \\
\nu(u_i) = \varnothing &\Rightarrow \omega(u_{i+1}) \leftarrow \omega(u_i) + \omega(u_{i+1})
\end{aligned}
$$

切完音節後，再接上詞表與退回函式 $f_\Sigma$，成為完整的分詞映射（§4.1, p. 7，式 (6)）：

$$\tau_\Sigma = (f_\Sigma \circ P)$$

詞表大小訂為 2,843 個詞元。KBBI 的音節出現頻率服從冪律 $p(x) \sim x^{-\alpha}$，$\alpha \approx 1.87$（Fig. 1, p. 7）。

---

## Card 4 ｜ 資料與實驗
* **詞表來源**：印尼大辭典（KBBI, Kamus Besar Bahasa Indonesia）的詞條。先把詞條切成音節、統計音節頻率，再挑高頻音節與基礎字元，詞表定為 2,843 個詞元（§4.1, p. 7，Fig. 1）。
* **測試語料**：NusaX-MT 平行語料全部 1,000 句（500 訓練、100 驗證、400 測試），涵蓋十種印尼地方語，加上印尼語與英語共十二語（§4.2, pp. 7–8；Table 4）。
* **比較對象**：GPT-2 的子詞分詞器（BPE，位元組對編碼；詞表 50,257），代表靠統計壓縮、不帶語言學假設的做法（§4.1, p. 7）。音節詞表僅約為它的 5.66%。
* **評分方式**：兩個自動指標。每字元詞元數（TPC）＝詞元數除以字母數，看碎片化程度（§4.3.1, p. 8，式 (7)）：

  $$\mathrm{TPC}(S) = \frac{|\tau_\Sigma(S)|}{|S|}$$

  跨語相似度則用 Smith-Waterman 局部序列比對（精確匹配 $+2$、錯配 $-1$、空位懲罰 $-1$），取最高分後除以兩句詞元數的幾何平均（§4.3.2, p. 9，式 (8)–(11)）：

  $$\mathrm{sim}(S_1, S_2) = \frac{\max(H)}{2 \times \sqrt{|\tau_\Sigma(S_1)| |\tau_\Sigma(S_2)|}}$$

  兩個指標都是自動計算，沒有人工或母語者評分（§4.3–§4.4, pp. 8–11）。

---

## Card 5 ｜ 結果
| 評估指標 | 音節分詞（KBBI 詞表 2,843） | GPT-2 BPE（詞表 50,257） | 論文來源位置 |
|---|---|---|---|
| **印尼語與十種地方語 TPC** | **集中在約 0.4**（反映 2–3 個音素的 CV(C) 音節結構） | 與音節分詞相近（原文 "relatively comparable"），但來自高頻字元串的壓縮併合 | 摘要 p. 1；§4.4, p. 10, Fig. 2 |
| **英語對照組 TPC** | **明顯偏高**（英語音節多不在印尼語詞表內，觸發字元退回；正文未給數值，依 Fig. 2 判讀約在 0.6 以上） | **最低**（高度向英語壓縮；依 Fig. 2 判讀約 0.2–0.25） | §4.4, p. 10, Fig. 2 |
| **語言對相似度的跨方法相關** | 線性相關 **$r = 0.9956$**、單調相關 **$\rho = 0.9895$** | 作為比較基準 | §4.4, p. 11 |
| **跨語序列相似度** | 全部地方語的語言對都高於 GPT-2，迴歸斜率 **$m \approx 1.21$**（平均約 +21%） | 作為比較基準 | 摘要 p. 1；§4.4, p. 11, Fig. 3a |

* **親屬語分支的增益最大（Fig. 3b, p. 11）**：差值熱圖上，馬來語支近親的語言對差距最明顯（班查—米南佳保 `+0.062`、印尼—米南佳保 `+0.060`、印尼—班查 `+0.059`），爪哇—峇里—巽他這一群也偏高。作者解釋，詞表取自印尼語，對馬來語支同源詞較敏感（§4.4, p. 11）。
* **作者自己的讀法**：跨語相似度在地方語語言對都較高，代表音節切分較能保住同源詞與詞綴的對應；英語的 TPC 偏高則反映它與印尼群島語言的音節結構差異（§4.4, pp. 10–11）。
* **要注意的是**：這些數字都只描述分詞後的詞元序列，不是翻譯或生成任務的成績（§4.2–§4.4, pp. 7–11）。

---

## Card 6 ｜ 限制與可用性
* **作者說的限制**：作者自己指出，這套為音節黏著語設計的分詞法「對英語效果低」（§5, p. 12）；文中也把本研究定位成這條路線的初步一步（§5, p. 12）。
* **讀的時候要留意**：整篇只比較分詞後的表層統計（TPC 與詞元序列相似度），沒有把分詞器接上語言模型做預訓練、翻譯或分類，所以「相似度較高」不等於下游任務一定變好（§4.2–§4.4, pp. 7–11；Wiki 註記）。詞表只來自印尼語辭典，英語等非南島語退回字元的比例高，混語部署時要另外處理（§4.4, p. 10）。指標都是自動計算，沒有母語者或人工評分（§4.3–§4.4）。
* **公開程度**：原文沒有提及程式、詞表或資料是否公開；全文也沒有資料可得性（Data Availability）一節（全文核查）。
* **作者的下一步**：把方法擴到更廣的南島語系語言，並構想與古文獻手稿掃描影像的字形辨識結合（§5, pp. 11–12）。
* **適合拿來報告的點**：切分規則只有三步、講得清楚，適合當「用語言學規則設計低資源分詞」的入門案例；它用 TPC 加序列相似度對照 GPT-2 的方式，也可當分詞評估的示例（Wiki 詮釋）。
* **引用本篇之後續研究**：（尚無可附出處之後續研究）

### 延伸想法
以下為延伸思考（Wiki 推測），不是原文主張。

1. **音節詞元可與構詞解析互補**：這篇以音節為詞元單位，好處是跨語共用；南島語的詞綴本身也常是一個音節，若在音節詞元之外再標出前綴、中綴、環綴與重疊，檢索或翻譯系統就多一層線索。原文沒有做這個組合，也沒有報告詞綴的切分正確率。
2. **評估可以再往下游走**：把同一批語料的分詞結果接上小型語言模型做翻譯或分類，才能回答「音節切法是否真的幫到下游」。這需要另一套實驗設計，超出本篇範圍。
3. **臺灣南島語的對照**：原文提到原始南島語（PAn）推定源於臺灣地區（§2, p. 2）。臺灣族語同樣以雙音節詞根與黏著構詞為主，但書寫系統與印尼群島不同、語料更少；本篇規則能否直接套用，得先逐語檢查音節結構與正字法（Wiki 推測）。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Lumbantobing, A. B., & Situngkir, H. (2026). Tokenizations for Austronesian Language Models: study on languages in Indonesia Archipelago. *arXiv preprint arXiv:2602.06998v1*（2026-01-27 版）. [https://arxiv.org/abs/2602.06998](https://arxiv.org/abs/2602.06998)
  * 原始檔典藏：`raw/my-focus/報告論文題材/2026-tokenizations-austronesian-lms-lumbantobing.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-tokenizations-austronesian-lms-lumbantobing.md](../evidence/2026-tokenizations-austronesian-lms-lumbantobing.md)
