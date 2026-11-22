# 已結案問題：papers/2026-epark-formosan-dialectometry-gagnier.md

> 本檔收錄 [wiki/papers/2026-epark-formosan-dialectometry-gagnier.md](../../../papers/2026-epark-formosan-dialectometry-gagnier.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-059 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.dialres-1.13` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：同 EK-057
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 DialRes 2026 原文首頁與 ELRA 核對：本篇由 ELRA 出版，正式註冊之 DOI 為 `10.63317/4scoopyavtvi`，經 Crossref 與 doi.org 解析確認無誤並更新頁面。

### EK-079 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 3 | 原文不符
- **問題**：第 43–62 行與架構圖稱方言距離係「對共享同一個語義概念的詞彙集合 $\mathcal{V}_{AB}$」計算編輯距離並執行「多維尺度分析（MDS）」。原文 §2.3（p. 125）並未對齊同義概念詞表亦未使用 MDS，而是直接對語料庫表面詞形計算三項指標：（1）詞級 TF-IDF 餘弦相似度（`min_df=2`、`sublinear_tf=True`）、（2）頻率 $\ge 5$ 詞型之未加權 Jaccard 相似度、（3）各方言前 500 高頻詞型雙向平均之字元級正規化 Levenshtein 距離。Card 3 完全漏述前兩項核心指標（TF-IDF 餘弦與 Jaccard），且虛構概念對齊詞表與 MDS。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`（§2.3 p. 125）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 刪除虛構之語義概念對齊詞表與 MDS 分析，改述原文真實採用之三項詞彙相似度指標（詞級 TF-IDF 餘弦、詞頻 $\ge 5$ 詞型 Jaccard 相似度、前 500 高頻詞之字元級正規化 Levenshtein 距離）與 Bootstrap 500 次抽樣信心區間檢驗；Card 4 補齊 Table 1–3 全語料特徵（Hapax 率 72%–79%）、多方言語言核心共有詞比例與分群發現（賽德克語 0.820 最緊密、布農語重現經典三分群、泰雅語 0.605 與魯凱語 0.648 分化最深）。建立證據表 wiki/evidence/2026-epark-formosan-dialectometry-gagnier.md，頁面 verification 改為 verified。

### EK-092 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 5 | 過度表述
- **問題**：Card 5 第 1 點（第 122 行）寫「證實簡單的詞彙相似度指標即可自動重現語言學家耗時數十年構擬的分群假說」，未保留原文限定。原文結論為「Among most groups, our results are extremely close to prior scholarship」（PDF p. 7），並明言排灣語「unable to make conclusions regarding the subgrouping」（PDF p. 5），萬山魯凱語兩種指標結果分歧（摘要，PDF p. 1）；同頁 Card 4 第 112–113 行亦已列出這些例外。建議改為「在多數語言中重現既有分群，排灣語無法判定、萬山方言指標分歧」。另第 35 行「開創性研究」屬評價用詞（「首次」為作者自述 first evaluation／first large-scale analysis，可保留並標明為作者主張）。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`（摘要，PDF p. 1；§4.1 Paiwan，PDF p. 5；§5 結論，PDF p. 7）
- **發現於**：wiki/log.md [2026-11-09 23:33] audit（Claude Code by Anthropic；第一批卡片回填 C 組只讀論文頁時提出，本代理回原文核對）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。Card 5 第 1 點改為「在多數語言中與既有分群研究結果相當接近，排灣語無法判定、萬山魯凱語兩指標分歧」，並附原文頁碼（摘要 p. 124、排灣語 p. 128、§5 p. 130）；第 35 行刪除「開創性」，「首次」改寫為作者自述。證據表增列對應主張，頁面 verification 改回 verified。

### EK-118 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 3 | 原文未支持
- **問題**：Card 3 第 64 行之 $D_{\text{norm}}(s_1, s_2) = \operatorname{LD}(s_1, s_2) / \max(|s_1|, |s_2|)$ 寫明除以較長字串之長度。原文只說「normalized by word length」，未指明取較長者，也未寫出公式；證據表第 12 列未登記此式。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`，§2.3（PDF 第 2 頁，論文集 p. 125）。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。回原文確認全文無編號公式後，刪除該區塊公式，改以文字照原文寫「以詞長正規化，原文未指明以哪一個詞的長度」；行內之 Jaccard 與 sublinear_tf 式改為文字並註明原文未列式。頁面已無區塊公式，卡片改用無公式模式。證據表登記。

### EK-119 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | Card 5 | 過度表述
- **問題**：Card 5 第二點（第 123 行）稱「證明南島語各語族不能一概而論」，排灣語與賽德克語「極適合進行多方言聯合訓練與跨方言遷移」，泰雅語與魯凱語「跨方言遷移容易引發負遷移」。原文為共有核心詞比例高者是「good candidates for cross-dialect model transfer」、「transfer learning should be tested」，獨有詞比例高者建議方言專屬模型或微調；未稱證明，也未談負遷移。
- **來源**：同 EK-118 之 PDF，PDF 第 3 頁（§3.1）、第 7 頁（§4）。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。Card 5 第二點改照原文：共有核心詞高者「是跨方言模型遷移的好候選」「應測試遷移學習」，獨有詞高者建議方言專屬模型或微調，並註明原文未做遷移實驗、未談負遷移（§3.1, p. 126；§4.1, p. 130）。另依新論文需求補記公開程式碼、作者明列之限制、四點建議與 §5 未來方向，各附位置。

### EK-157 | fixed | papers/2026-epark-formosan-dialectometry-gagnier.md | hook、Card 1、Card 2、Card 4 與 Card 6 | 過度表述
- **問題**：（1）`hook` 稱「首度」分析並「客觀量化 16 族南島語親緣分支」，原文為作者自述首次，且成對比較只做 7 個多方言族語。（2）Card 1 稱臺灣南島語是南島語系「發源樞紐」、ePark 是「全球規模最完整」的資源庫、作者為「美國學者」；原文為 primary branch、high-quality comprehensive resource，作者單位為高中。（3）Card 2 稱過去分類「多依賴定性音變構擬與有限詞彙調查」、布農語次方言「存在長期爭論」，原文未如此描述，且本篇結果與布農語既有三分群相符。（4）Card 3 前處理寫保留 `^`，原文該字元在 PDF 文字層無法顯示，無法核實。（5）Card 4 稱最少詞元之 46,177 為「泰雅語四季」，表 1 為 Plngawan；稱主題差異「會壓過方言語言學差異」，原文只說須以相同篇章比較；未說明 ± 為標準差。（6）Card 6 稱直接混合訓練「必然遭遇」71% 獨有詞 OOV 衝擊，為 Wiki 推測卻寫成必然。
- **來源**：`raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`，摘要與 §1（p. 124）、§2.1–§2.3（p. 125）、§3.1–§3.2（pp. 125–128）、表 1–3（pp. 127–128）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句；Card 6 該句改標為 Wiki 推測並改為「可能」；證據表重建，表 1 至表 3 數值逐一寫出列與欄。
