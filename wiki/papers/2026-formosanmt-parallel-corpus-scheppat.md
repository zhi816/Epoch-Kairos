---
title: "FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family"
title_zh: "FormosanMT：臺灣南島語言家族多語言平行語料庫"
paper_year: 2026
award_year: 2026
timeline_year: 2026
authors: "Hunter Scheppat, Joshua K. Hartshorne, Sema Koc, Éric Le Ferrand, Emily Prud'hommeaux"
venue: "Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026), 3445-3455"
domain: "ai"
domain_tags: ["#自然語言處理", "#計算語言學", "#深度學習"]
concepts: ["formosan-computational-linguistics", "low-resource-machine-translation"]
status: "published"
verification: "partial"
my_focus: true
focus_role: "international"
focus_languages: ["臺灣南島諸語"]
doi_url: "https://doi.org/10.63317/3ut33xim33nt"
hook: "波士頓學院等團隊於 LREC 2026 發布 FormosanMT：涵蓋臺灣 15 種原住民族語言、近 50 萬句對之族語與華語、英語平行語料，並公開抽取與過濾腳本、相容 NLLB 之繁體中文分詞器，以及雙向基準模型。"
card_line: "彙整各族語與中文的對照句，建成翻譯語料庫"
---

# FormosanMT：臺灣南島語言家族多語言平行語料庫 (FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family)

> 「平行語料是低資源翻譯研究的起點。FormosanMT 把散在辭典、教材、田野紀錄與影片字幕裡的族語對照句，整理成可以直接拿來訓練的語料，連整理的腳本也一起公開。」（本頁引言為 Wiki 撰寫，非原文）

**2026 發表 ｜ 個人核心研究關注**

> **本頁範圍**：波士頓學院 Hunter Scheppat、Joshua K. Hartshorne 等人，*Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)*, pp. 3445–3455（ELRA 出版，DOI: [10.63317/3ut33xim33nt](https://doi.org/10.63317/3ut33xim33nt)）。以臺灣原住民族 15 種南島語言（含雅美/達悟語）與華語／英語之平行語料構建與雙向神經翻譯基準評測為核心。

---

## Card 1 ｜ 時代銘文 (The Hook)
瀕危語言往往缺少書寫傳統與足夠的說話人口，難以產生文字資源；缺乏合適的平行語料，也阻礙了專為極低資源情境設計之翻譯方法的發展（摘要；§1, p. 3445）。波士頓學院（Boston College）、MGH 衛生職業學院與紐約州立大學水牛城分校的研究者於第 15 屆語言資源與評測大會（LREC 2026）發表 **FormosanMT**：一組可直接用於機器翻譯訓練（MT-ready）的平行語料，涵蓋臺灣 15 種原住民族語言與華語、英語之對照，合計 **493,519 句對**（摘要；§3.4, p. 3449）。

研究團隊同時公開語料之抽取、正規化、過濾與切分腳本，一個相容 NLLB 架構的繁體中文分詞器，更新後的 NLLB 微調程式，以及族語與華語、英語之間的 NLLB 與 OpenNMT 雙向基準模型（§1, pp. 3445–3446）。

---

## Card 2 ｜ 世紀瓶頸：族語平行語料少，又散在各處 (The Dilemma)
原文指出的困難（§1–§4, pp. 3445–3451）：

* **瀕危語言難以產生平行語料**：瀕危語言往往缺乏書寫傳統與足夠的說話人口，平行語料因此稀少，阻礙了專為極低資源情境設計之翻譯方法的發展（§1, p. 3445）。前人為臺灣南島語所做的翻譯研究只用 ILRDF 辭典資料之子集，並各自篩選與切分，結果無法與本篇比較（§2, p. 3446）。
* **公開來源分散、品質不一**：可用資料散在 ILRDF 線上辭典、族語 E 樂園（ePark）、臺大田野語料（NTU Corpus）、總統道歉文與 ILRDF 影片字幕等處；辭典與教材原為書面參考資料，影片轉寫與田野紀錄的品質則較不穩定，田野譯文常夾帶語言學家的評註、問題與筆記（§3.2–§3.3, pp. 3447–3448）。聖經雖有多種族語譯本，作者因其領域與文體差異可能增加翻譯幻覺而不收錄（§2, p. 3446）。
* **現成工具不支援繁體中文**：NLLB 目前只支援簡體中文（§1, p. 3445）；網路上常見之 NLLB 新增語言教學依賴特定版本的變通寫法，先前的修正已與新版 `tokenizers` 函式庫不相容（§4.2.1, p. 3450；§4.2.2, p. 3451）。

---

## Card 3 ｜ 突破架構與原理：正規化、啟發式過濾與 NLLB 繁中分詞調適 (The Secret)

### 1. 正規化與過濾（§3.3, p. 3448）
FormosanBank 與 ILRDF 影片字幕兩類來源各有抽取腳本，正規化與過濾則共用同一流程。過濾全靠正則規則、結構特徵與長度比，未使用語言識別器或神經語意對齊模型；原文全文沒有編號公式，以下規則皆為文字敘述。

1. **文字正規化**：可用時套用 Moses 標點正規化，再做 Unicode NFKC、移除 ASCII 控制字元與多餘空白。之後依序：
   * 移除行首說話者標籤（一個大寫拉丁字母接冒號，如 `A:`）；
   * 刪除括號內長度 1 至 10 個字元、屬評註而非譯文的短註；
   * 移除已知的中文假影字串（原文以英譯描述，意為 "full text record"、"Chinese record"、"woman's full name"）；
   * 刪除句尾逗號（半形或全形）、修剪游離引號與括號、修正標點前與括號引號內側之異常空白。
2. **非平行內容排除**：捨棄下列句對——華語端為舞台指示語（原文英譯為 "switch to the next item"、"I will stop here"）；華語端只是頁碼標記、單純編號或年份標題；華語端只有重複標點，或由臺灣合作者整理之語氣詞（如相當於 "ha"、"oh" 者）組成、超過兩個字元的字串；族語端含有漢字。
3. **長度比過濾**：兩側皆有兩個以上詞元時，計算目標詞元數對來源詞元數之比 $r$，捨棄 $r \le 0.2$ 或 $r > 8.0$ 者；任一側少於兩個詞元時（多為辭典詞條），改以字元數計算比值，捨棄 $r \le 0.05$ 或 $r > 20.0$ 者。門檻經反覆嘗試訂定，目標是盡量少丟句對、只剔除明顯不平行者；作者承認過濾偏嚴、部分規則帶有臨時性，因此一併公開腳本，所有參數皆可由命令列調整。

### 2. 切分（§3.4, pp. 3448–3449）
* 完全重複之句對只留一份；一側與既有句對重複者、一側為辭典詞條者，一律歸入訓練集。
* 每個資料來源各自以固定亂數種子切成 80/10/10 之訓練、開發、測試集，以便依文類細看表現。

### 3. 涵蓋之語言（表 1，§3.1, p. 3447）
表 1 列出臺灣官方認定之原住民族語言及其 ISO 639-3 代碼，共 16 種語言、15 個代碼：阿美語（`ami`）、泰雅語（`tay`）、布農語（`bun`）、卡那卡那富語（`xnb`）、噶瑪蘭語（`ckv`）、排灣語（`pwn`）、卑南語（`pyu`）、魯凱語（`dru`）、拉阿魯哇語（`sxr`）、賽夏語（`xsy`）、撒奇萊雅語（`szy`）、賽德克語與太魯閣語（同為 `trv`）、邵語（`ssf`）、鄒語（`tsu`）、雅美／達悟語（`tao`）。賽德克語與太魯閣語政治上分立，語言學上歸為同一語言、共用代碼，語料合併處理；雅美語不屬臺灣南島語群，但同屬南島語系且為臺灣原住民族語言，故一併收錄。

### 4. 基準模型與 NLLB 分詞器調適（§4, pp. 3449–3451）
原文為每個語言對分別訓練一個雙向模型，而非 15 語聯合訓練；以全部語料繼續預訓練列為未來工作（§6, p. 3453）。

1. **OpenNMT-py**：2 層 LSTM 編碼器與解碼器（input feeding、general global attention、word_vec_size 256、rnn_size 512），Adam 學習率 $10^{-3}$、梯度裁切 2，以 2048 詞元分批、accum_count 2，dropout 0.3。雙向語料串成單一資料流，每行來源句前加目標語言標記；與 NLLB 共用同一 SentencePiece 模型（§4.1, pp. 3449–3450）。
2. **NLLB-200**：微調 `facebook/nllb-200-distilled-600M`（§4.2, p. 3450）。
   * **分詞器重建**：保留原有語言代碼與特殊符號，新增 `ami_Latn` 等族語代碼，並讓 `<mask>` 維持為最後一個附加特殊符號；採 sentencepiece-merge 模式，把以本語料訓練之 SentencePiece 片段併入 NLLB 之模型，使繁體中文（`zho_Hant`）的切分較乾淨（§4.2.1, p. 3450）。
   * **嵌入初始化**：調整詞表後只重設一次嵌入矩陣大小；新子詞以舊分詞下各分解片段之嵌入平均暖啟動，新增之族語代碼列以 `eng_Latn` 之嵌入為種子，而非隨機初始化（§4.2.1, p. 3450；§4.2.2, p. 3451）。
   * **雙向訓練**：每步以 $p = 0.5$ 機率抽取翻譯方向並即時設定 `tokenizer.src_lang`；Adafactor、學習率 $10^{-4}$、1,000 步暖身、batch size 8、雙側最大長度 128（§4.2.2, p. 3451）。

```text
[FormosanBank 各來源 + ILRDF 影片字幕] ──► [正規化與正則清洗] ──► [非平行內容與長度比過濾]
                                                                        │
       ┌────────────────────────────────────────────────────────────────┘
       ▼
[各來源分別切分 80/10/10] ──► [每個語言對一個雙向模型] ──► (1) OpenNMT-py 2 層 LSTM
                                                       └──► (2) NLLB-200（分詞器重建 + 雙向微調）
```

---

## Card 4 ｜ 可核實的原文證據 (The Evidence)

### 1. 語料規模（§3.4, p. 3449；表 2, p. 3450）
* **總規模**：過濾與切分後合計 **493,519 句對**，其中族語－華語 **397,710** 句對、族語－英語 **95,809** 句對（§3.4, p. 3449）。
* **依切分**（表 2 合計列）：族語－華語訓練 333,984、開發 31,854、測試 31,872；族語－英語訓練 81,400、開發 7,197、測試 7,212。
* **英語模型**：表 2 每種語言都列有族語－英語句對，但只有阿美語、布農語、魯凱語、泰雅語四種的英語資料足以訓練模型（§1, p. 3445；§5, p. 3452）；四者之族語－英語訓練集分別為 9,600、9,351、11,810、10,380 句對（表 2）。
* **表 2 標示**：表 2 有兩組皆標為 `xnb`、未見 `ckv`，原文標示如此。

### 2. 翻譯基準結果（表 3、表 4, p. 3451）
評估以 SacreBLEU 計算 BLEU 與 chrF++，華語目標使用內建 zh 分詞（§5, p. 3452）。
* **整體**：NLLB 微調整體優於 OpenNMT；明顯例外為阿美語與英語之間，尤其阿美語→英語，OpenNMT 的 BLEU 與 chrF++ 皆高出數點（§5, p. 3452）。
* **族語→華語（BLEU，NLLB／OpenNMT）**：卡那卡那富語 26.90／15.40（為 15 個族語→華語方向中 NLLB 之最高者）；布農語 25.08／19.70；邵語 25.09／14.10；魯凱語 19.97／21.70（此方向 OpenNMT 較高）。
* **華語→族語**：作者指出兩種架構譯入族語整體都比譯入華語或英語弱得多，如華語→布農語 NLLB BLEU 7.85、華語→魯凱語 5.77；chrF++ 則相對較高，如華語→卡那卡那富語 51.79（OpenNMT 35.10）、華語→噶瑪蘭語 48.88（28.70）、華語→邵語 47.28（32.70）。作者推測 chrF++ 以字元 n-gram 計算重疊，較能容許構詞上的小差異（§5, p. 3452）。
* **族語→英語（表 4）**：布農語→英語 NLLB BLEU 43.08（chrF++ 53.55）；泰雅語→英語 41.02（49.19）；阿美語→英語 OpenNMT 33.50（NLLB 25.02）。作者指出譯入英語的分數偏高，可能是族語－英語資料之領域與詞彙有限所致（§5, p. 3452）。
* **輸出例**：表 5 之阿美語→英語例句顯示兩種模型都會產生幻覺，OpenNMT 輸出較不通順（§5, p. 3452）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
> 本篇發表於 2026 年，尚無後續研究；以下記錄原文公開之資源、作者明列之限制與未來工作。

* **本篇公開之資源**：族語與華語、英語之平行語料；抽取、正規化、過濾與切分腳本（參數可由命令列調整）；相容 NLLB 之繁體中文分詞器與更新後之 NLLB 微調程式；訓練好的 NLLB 與 OpenNMT 模型，全部置於 GitHub `FormosanBank/FormosanBank-MT`（§1, p. 3446，註 1）。ILRDF 影片字幕因授權未明，不直接散布，改提供抓取腳本（§3.2, p. 3447；§8, p. 3453）。
* **作者自述之限制**（§7, p. 3453）：只用兩種翻譯架構訓練基準模型；切分、訓練與測試都未考慮方言資訊，而方言之間可能有不小的詞彙差異。§3.3 另承認過濾偏嚴、部分規則帶有臨時性（p. 3448）。
* **作者所述之未來工作**（§6, p. 3453）：在 NLLB 等多語預訓練架構上以全部 FormosanMT 語料繼續預訓練，借助親屬語資料；以資料增強改善特定來源與文類之表現；恢復以大型語言模型翻譯之初步工作。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)

> 以下為對使用者關注之研究方向的延伸思考（Wiki 詮釋），非原文主張。

### 對臺灣南島語翻譯研究之映射與啟發

1. **可重建的語料**：FormosanMT 連同抽取、正規化、過濾與切分腳本一起公開，來源資料增加時可重新產生語料，過濾門檻也可依需求調整（§1, p. 3445；§3.3, p. 3448）。對資料仍在增加的族語而言，能重建的語料比一次釋出的語料更耐用。
2. **使用時須留意之處**：賽德克語與太魯閣語共用 `trv`、語料合併；方言標記未用於切分與訓練，但保留在來源 CSV（§3.1, p. 3447；§3.4, p. 3449；§7, p. 3453）。研究個別語言或方言時，須依標記自行重新切分。ILRDF 影片字幕不隨語料散布，須以腳本自行抓取（§3.2, p. 3447）。
3. **構詞資訊之延伸**：FormosanMT 的文本為表層詞形；若以構詞解析器（如本庫收錄之 [戴晟哲 2023](2023-atayal-truku-morphology-dai.md)、[楊鈞凱 2025](2025-atayalic-oov-enumeration-yang.md)）為族語端加註詞根與語綴，可得帶構詞資訊之平行語料，其對翻譯是否有幫助仍待驗證。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [臺灣南島語計算語言學與構詞解析](../concepts/formosan-computational-linguistics.md)
  * [低資源神經機器翻譯與檢索增強生成](../concepts/low-resource-machine-translation.md)
* **原始權威文獻**：
  * 官方學術出處：Scheppat, H., Hartshorne, J. K., Koc, S., Le Ferrand, É., & Prud'hommeaux, E. (2026). FormosanMT: A Multilingual Parallel Corpus of the Formosan Language Family. In *Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)* (pp. 3445-3455). DOI: [10.63317/3ut33xim33nt](https://doi.org/10.63317/3ut33xim33nt)
  * 開源語料、程式與模型：[github.com/FormosanBank/FormosanBank-MT](https://github.com/FormosanBank/FormosanBank-MT)
  * 原始檔典藏：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`（不納入主倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2026-formosanmt-parallel-corpus-scheppat.md](../evidence/2026-formosanmt-parallel-corpus-scheppat.md)
