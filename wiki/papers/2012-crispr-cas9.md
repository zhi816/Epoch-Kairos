---
title: "A Programmable Dual-RNA–Guided DNA Endonuclease in Adaptive Bacterial Immunity"
title_zh: "CRISPR-Cas9 基因剪刀誕生：可編程雙 RNA 引導之 DNA 核酸內切酶"
paper_year: 2012
award_year: 2020
timeline_year: 2012
authors: "Martin Jinek, Krzysztof Chylinski, Ines Fonfara, Michael Hauer, Jennifer A. Doudna, Emmanuelle Charpentier"
laureates: "Emmanuelle Charpentier, Jennifer A. Doudna"
venue: "Science, 337(6096), 816-821"
honor: "2020 諾貝爾化學獎（表彰基因組編輯方法之開發）"
domain: "bio"
domain_tags: ["#基因工程", "#生物科技"]
concepts: ["programmable-cellular-engineering", "ai-for-structural-biology"]
status: "wiki"
verification: "issues"
my_focus: false
doi_url: "https://doi.org/10.1126/science.1225829"
key_papers:
  - "Deltcheva, E. et al. (2011) CRISPR RNA maturation by trans-encoded small RNA and host factor RNase III. Nature 471:602-607. https://doi.org/10.1038/nature09886"
  - "Jinek, M., Chylinski, K., Fonfara, I., Hauer, M., Doudna, J. A., & Charpentier, E. (2012) A Programmable Dual-RNA–Guided DNA Endonuclease in Adaptive Bacterial Immunity. Science 337(6096):816-821. https://doi.org/10.1126/science.1225829"
  - "Cong, L. et al. (2013) Multiplex Genome Engineering Using CRISPR/Cas Systems. Science 339(6121):819-823. https://doi.org/10.1126/science.1231143"
  - "Mali, P. et al. (2013) RNA-Guided Human Genome Engineering via Cas9. Science 339(6121):823-826. https://doi.org/10.1126/science.1232033"
hook: "揭示細菌免疫蛋白 Cas9 僅需一段人工合成的單鏈引導 RNA（sgRNA），即可在任意指定序列位置精準剪斷雙股 DNA，將基因工程從繁瑣的蛋白質設計轉化為簡單的 RNA 序列編程。"
---

# CRISPR-Cas9 基因剪刀誕生：可編程雙 RNA 引導之 DNA 核酸內切酶

> 「生命演化了三十億年的細菌抗病毒防衛武器，在被解構為『單一核酸酶 ＋ 單一引導 RNA』的瞬間，成為人類改寫生命法典的通用文字處理器。」

**2012 發表 ｜ 2020 諾貝爾化學獎**

> **本頁範圍說明**：2020 年諾貝爾化學獎頒予 Emmanuelle Charpentier 與 Jennifer A. Doudna，表彰兩人開發 CRISPR-Cas9 基因組編輯方法。本頁以 Jinek et al. (2012) 發表於《Science》之生化機制與單鏈引導 RNA（sgRNA）工程化奠基論文為主軸，並於 `key_papers` 列出 Deltcheva et al. (2011) 發現 tracrRNA 之先驅工作，以及 Cong et al. (2013) 與 Mali et al. (2013) 首次在真核與人類細胞實現基因組編輯之關鍵延伸論文。

---

## Card 1 ｜ 時代銘文 (The Hook)
在 2012 年之前，若想修改生物體內的某個特定基因，科學家必須針對每一段目標 DNA 重新設計並改造一顆全新的蛋白質（如 ZFN 或 TALEN），耗時數月且成本高昂。Jinek、Doudna 與 Charpentier 團隊在 2012 年證明，化膿性鏈球菌（*Streptococcus pyogenes*）的第 II 型 CRISPR-Cas9 系統是一個由雙 RNA 引導的 DNA 內切酶，並進一步將兩條 RNA 融合成單一嵌合引導 RNA（sgRNA）。從此，靶向任意基因只需更換一段 20 個核苷酸的 RNA 序列。

---

## Card 2 ｜ 世紀瓶頸：蛋白質識別密碼的工程死局 (The Dilemma)
早期靶向基因組編輯技術受困於「蛋白質—DNA 構型識別」的高昂門檻：

* **鋅指核酸酶（ZFNs）與類轉錄激活因子效應物核酸酶（TALENs）的剛性束縛**：這兩類工具依賴蛋白質結構域與 DNA 鹼基對的物理結合。每更換一個目標基因位點，就必須重新進行複雜的蛋白質工程組裝、篩選與結構驗證，無法實現高通量或普及化應用。
* **細菌 CRISPR 系統的機制迷霧**：雖然科學家自 1987 年起便在細菌基因組發現規律成簇間隔短回文重複序列（CRISPR），並於 2007 年確認其為細菌適應性免疫系統，但第 II 型系統中 Cas9 蛋白究竟如何協同 crRNA 與 tracrRNA 識別並切割雙股 DNA，其最小充要生化組件始終未被拆解。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
作者透過純化重組 Cas9 蛋白與體外（in vitro）切割實驗，完整拆解了 Cas9 的分子機制，並完成決定性的工程簡化：

1. **三元複合物充要性與雙 RNA 協同機制（crRNA + tracrRNA）**：
   * 僅需 Cas9 蛋白、成熟的 CRISPR RNA（crRNA，含 20 nt 與目標互補之導向序列）以及反式激活 crRNA（tracrRNA）三者，在鎂離子（$\mathrm{Mg}^{2+}$）存在下即可精準切割目標雙股 DNA（dsDNA），無需任何其他細菌宿主因子。
2. **雙結構域分工切割（HNH 與 RuvC-like 結構域）**：
   * Cas9 包含兩個不同的核酸酶催化結構域：**HNH 結構域**負責切割與 crRNA 互補配對的目標股（Complementary Strand），**RuvC-like 結構域**則負責切割非互補股（Noncomplementary Strand），共同在距離 PAM 上游 3 個鹼基對處產生平末端雙股斷裂（Blunt-ended DSB）。
3. **PAM 位點識別與單鏈嵌合 RNA（sgRNA）工程化**：
   * 切割啟動的絕對前提是非互補股目標序列 3' 端緊鄰一個簡短的原間隔序列鄰近基序（PAM，化膿性鏈球菌 Cas9 為 $\text{5'-NGG-3'}$）。作者將 crRNA 的 3' 端與 tracrRNA 的 5' 端以四核苷酸環（Tetraloop, $\text{GAAA}$）連接，創造出單一嵌合引導 RNA（Single-Guide RNA, sgRNA），將三元系統簡化為「Cas9 蛋白 ＋ sgRNA」二元可編程系統。

### 1. R-Loop 形成之熱力學自由能判準 (Thermodynamics of R-Loop Formation)

Cas9-sgRNA 核糖核蛋白（RNP）首先透過蛋白質結構域識別非互補股上的 $\text{5'-NGG-3'}$ PAM 基序，隨後自 PAM 鄰近之種子區（Seed Region，第 1 至 10–12 個核苷酸）定向解旋雙股 DNA 並形成 RNA-DNA 雜交 R-Loop。其構型轉換自由能 $\Delta G_{\text{total}}$ 可表為：

$$\begin{aligned}
\Delta G_{\text{total}}(n) = &\;\Delta G_{\text{PAM}} + \sum_{k=1}^{n} \left( \Delta G_{\text{RNA:DNA}, k} - \Delta G_{\text{DNA:DNA}, k} \right) \\
&+ \Delta G_{\text{conf}}(\text{Cas9})
\end{aligned}$$

其中 $n \le 20$ 為已配對之鹼基數，$\Delta G_{\text{PAM}}$ 為 PAM 結合能，$\Delta G_{\text{conf}}(\text{Cas9})$ 為激活 HNH 與 RuvC 結構域所需的蛋白變構自由能。當種子區出現錯配（Mismatch）時，自由能壁壘急劇上升，阻斷後續催化切割。

### 2. 雙催化結構域反應動力學方程 (Dual-Domain Cleavage Kinetics)

在 $\mathrm{Mg}^{2+}$ 作為催化二價陽離子輔因子的條件下，Cas9-sgRNA（記為 $E$）與含 PAM 之目標雙股 DNA 底物（記為 $S$）結合形成活性 R-Loop 複合物 $ES^*$，並分別由 HNH 與 RuvC 結構域以一階速率常數 $k_{\text{HNH}}$ 與 $k_{\text{RuvC}}$ 切割互補股與非互補股：

$$\begin{aligned}
\frac{d[ES^*]}{dt} &= k_{\text{on}}[E][S] - \left( k_{\text{off}} + k_{\text{cleave}} \right) [ES^*] \\
\frac{d[P_{\text{DSB}}]}{dt} &= k_{\text{cleave}} [ES^*]
\end{aligned}$$

當對任一催化位點進行單點突變——即 $\text{D10A}$（使 RuvC 失活）或 $\text{H840A}$（使 HNH 失活）時，對應速率常數歸零（$k_{\text{RuvC}} = 0$ 或 $k_{\text{HNH}} = 0$），系統即從雙股內切酶轉變為單股切口酶（Nickase, nCas9）；若兩者同時突變（$\text{dCas9}$），則有 $k_{\text{cleave}} = 0$，但仍保留高親和力之序列特異性 DNA 結合能力（$K_d = k_{\text{off}}/k_{\text{on}} \sim \text{nM}$ 量級）。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Jinek et al. 2012）之核心證據
* **雙催化位點點突變驗證（$\text{D10A}$ 與 $\text{H840A}$）**：在質體與寡核苷酸體外切割實驗中，野生型 Cas9 產生線性化雙股斷裂（DSB）；$\text{Cas9(D10A)}$ 僅切割互補股、$\text{Cas9(H840A)}$ 僅切割非互補股，均只產生開環單股切口質體（Nicked Open Circular Plasmid）；雙突變體 $\text{Cas9(D10A/H840A)}$ 則完全喪失切割活性，嚴格鎖定兩結構域的催化分工。
* **切割位點鹼基級定位（PAM 上游 3 bp）**：透過高解析度變性聚丙烯醯胺凝膠電泳（Denaturing PAGE）定序，確認 HNH 與 RuvC 均精準在距離 $\text{5'-NGG-3'}$ PAM 上游第 3 個核苷酸處切斷磷酸二酯鍵。
* **種子區（Seed Sequence）特異性窗口測試**：系統性掃描目標序列單點突變，證實距離 PAM 最近的 8–12 個鹼基對（種子區）對錯配極度敏感，單一鹼基錯配即可完全廢除切割活性；而遠離 PAM 的 5' 端前幾個鹼基則具一定容錯度。
* **多目標編程與 GFP 基因家族精準切割**：作者設計 5 條針對綠色螢光蛋白（GFP）基因不同位點的嵌合 sgRNA（Chimera A），在無須更動 Cas9 蛋白的情況下，100% 在預期位置切出對應長度的 DNA 片段，直接證明其通用可編程性。

> **範圍界定**：本篇論文（Jinek et al. 2012）之實驗全數為純化蛋白與體外（in vitro）DNA 切割驗證，並在文末明確預見並提出將此嵌合 sgRNA-Cas9 系統用於真核生物基因組編輯之構想。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **哺乳動物與人類細胞基因組編輯之首次實現**：Cong et al. (2013)（張鋒團隊）,*Science* 339:819-823 與 Mali et al. (2013)（George Church 團隊）,*Science* 339:823-826，於 2013 年 1 月同步證明將 Cas9 與 sgRNA 導入人類與小鼠細胞後，可高效誘發非同源末端接合（NHEJ）或同源重組修復（HDR），實現多基因同步編輯。
* **鹼基編輯（Base Editing）與先導編輯（Prime Editing）**：Komor et al. (2016), *Nature* 533:420-424 與 Anzalone et al. (2019), *Nature* 576:149-157（David Liu 團隊），利用本篇發現之 $\text{Cas9(D10A)}$ 單股切口酶（Nickase）融合脫氨酶或反轉錄酶，在不產生雙股斷裂（DSB）的前提下實現單一鹼基轉換與任意序列寫入。
* **首款獲批上市之 CRISPR 臨床基因療法**：Frangoul et al. (2021), *NEJM* 384:252-260，基於 CRISPR-Cas9 編輯 *BCL11A* 增強子之療法 Casgevy（exagamglogene autotemcel）於 2023 年底獲英國、美國 FDA 批准治療鐮刀型紅血球疾病與輸血依賴型 $\beta$-地中海貧血。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **生命科學研究的民主化與普及化**：將基因敲除、敲入與全基因組功能篩選（CRISPR KO/CRISPRi/CRISPRa 篩選庫）的時間從數月縮短至數天，成本降至數十美元，重塑了全球每一個分子生物學實驗室的日常工作流。
* **衍生工具生態系的爆發**：本篇建立的 $\text{dCas9}$（去催化活性 Cas9）與 $\text{nCas9}$（單股切口酶）成為萬用分子底盤，衍生出表觀遺傳調控、活細胞染色質成像、鹼基編輯與先導編輯等完整技術家族。
* **農業育種與臨床遺傳病根治**：從抗病耐旱作物的非轉基因精準育種，到鐮刀型貧血、轉甲狀腺素蛋白澱粉樣變性（ATTR）及罕見代謝疾病之體內（in vivo）基因療法，人類正式邁入「可編寫基因組」時代。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
CRISPR-Cas9 的誕生展示了科學史上最優雅的**「軟硬體解耦（Hardware-Software Decoupling）」**：

1. **從「專用硬體」到「通用處理器 ＋ 軟體腳本」**：ZFN 與 TALEN 時代如同早期每算一道題就要重新焊接電路的專用機；Cas9 則是通用 CPU，而 20 nt 的 sgRNA 就是可隨時載入的軟體程式碼。
2. **基礎微生物學的無用之用**：這項改寫人類醫學與農業的萬億級技術，最初只是為了回答一個純粹的好奇心問題：「優格裡的細菌與鏈球菌究竟如何記住並抵抗噬菌體病毒的入侵？」

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [可編程細胞與基因工程](../concepts/programmable-cellular-engineering.md)
  * [AI 驅動之結構生物學與分子設計](../concepts/ai-for-structural-biology.md)
* **原始權威文獻**：
  * 官方學術出處：Jinek, M., Chylinski, K., Fonfara, I., Hauer, M., Doudna, J. A., & Charpentier, E. (2012). Science, 337(6096), 816-821. DOI: [10.1126/science.1225829](https://doi.org/10.1126/science.1225829)
  * 原始檔典藏：`raw/2012-crispr-cas9.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 獎項通告：[The Nobel Prize in Chemistry 2020](https://www.nobelprize.org/prizes/chemistry/2020/)
