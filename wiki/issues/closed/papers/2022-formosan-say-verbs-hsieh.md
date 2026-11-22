# 已結案問題：papers/2022-formosan-say-verbs-hsieh.md

> 本檔收錄 [wiki/papers/2022-formosan-say-verbs-hsieh.md](../../../papers/2022-formosan-say-verbs-hsieh.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-069 | fixed | papers/2022-formosan-say-verbs-hsieh.md | Frontmatter 與 Card 3 | 原文不符
- **問題**：（1）Frontmatter `title`（第 2 行）與主標題（第 20 行）將英文標題寫為 `"Semantic Phenomena of Verbs of Saying in Formosan Languages: A Typological Investigation"`；原文末頁（PDF p. 46，期刊 p. 92）之正式英文標題為 `"On the Semantics of SAY Verbs in Formosan Languages"`。（2）Card 3（第 46–63 行）之集合聯集式與連續向量空間線性插值式未見於原文（原文圖 4，p. 83 係以 `X[述說]、[動作]` 語義特徵標記描述語法化鏈），未標明為 Wiki 自行形式化推導。
- **來源**：`raw/my-focus/台灣相關論文/台灣南島語「說」動詞語義現象初探_謝富惠.pdf`（p. 83 圖 4、p. 92 英文摘要頁）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：`title` 與主標題改為英文摘要頁之正式題名 *On the Semantics of SAY Verbs in Formosan Languages*；刪除 Card 3 原文未出現之集合式、語法化分段函數與向量插值式，改述原文圖一至圖四之語義延伸機制與施為動詞假說。另修正同頁未登記之問題：Card 6 原列泛泰雅語例詞 `musa’`、`mhai`、`kema` 有誤（`kema` 為卑南語），改為原文表一、表二之泰雅語 `mha`、賽德克語 `mesa`／`kesa-un`、太魯閣語 `mesa`／`sun`，並補述其兼具「做」義；刪除 Card 5「可顯著提升依存句法分析」等無來源表述，補列作者自述之限制。證據表見 wiki/evidence/2022-formosan-say-verbs-hsieh.md。

### EK-131 | fixed | papers/2022-formosan-say-verbs-hsieh.md | Frontmatter card_line 與 hook | 原文不符
- **問題**：`card_line` 寫「比較族語的「說」，發現多半也能表示「想」」，`hook` 寫「發現它們普遍從「說」延伸到「想」」。原文結論為所有台灣南島語的「說」動詞都有從述說語義場跨到認知語義場（「說」→「想」）的延伸；「多半」「普遍」比原文弱，與原文不符。
- **來源**：`raw/my-focus/台灣相關論文/台灣南島語「說」動詞語義現象初探_謝富惠.pdf`，第 5 節，p. 84（「所有的台灣南島語都同時呈現『同一語義場』以及從『述說語義場』跨到『認知語義場』的語義延伸」）。
- **發現於**：撰寫卡片前回原文抽查時發現（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`card_line` 改為「比較族語的「說」，發現都能表示「想」」，`hook` 之「普遍」改為「都」；證據表增列一列。

### EK-229 | fixed | papers/2022-formosan-say-verbs-hsieh.md | 原 Card 4 研究範圍 | 原文不符
- **問題**：原頁寫「例句取自臺灣南島語言叢書、原住民族語言線上辭典與已出版文獻」。原文寫明語料來自原民會 2018 年再版之十六族語言語法概論、即將出版之詞類及其教學叢書、原住民族語言線上辭典，以及作者本人的田野調查，且未標出處者出自田調；原頁漏記田調並以「已出版文獻」概括。
- **來源**：[原文 PDF](../../../../raw/my-focus/台灣相關論文/台灣南島語「說」動詞語義現象初探_謝富惠.pdf)，第 1 節，p. 55。
- **發現於**：2026-11-20 改寫為我的關注新六章時回原文抽查，Claude Code by Anthropic（Claude Opus 5.5）。
- **處理**：2026-11-20，Claude Code by Anthropic（Claude Opus 5.5）。論文頁 01 速覽、04 語料來源與 06 改依原文 p. 55，證據表新增一列。
