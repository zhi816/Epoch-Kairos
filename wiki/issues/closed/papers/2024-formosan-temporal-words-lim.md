# 已結案問題：papers/2024-formosan-temporal-words-lim.md

> 本檔收錄 [wiki/papers/2024-formosan-temporal-words-lim.md](../../../papers/2024-formosan-temporal-words-lim.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-070 | fixed | papers/2024-formosan-temporal-words-lim.md | Frontmatter、Card 3 與 Card 6 | 原文不符
- **問題**：（1）Frontmatter `title`（第 2 行）與主標題（第 20 行）將英文標題寫為 `"A Preliminary Cross-Linguistic Comparison of Temporal Words in Formosan Languages"`；原文末頁（PDF p. 27）之正式英文標題為 `"A Preliminary Comparative Study of Formosan Temporal Words"`。（2）Card 3（第 45–57 行）之代數分解式未見於原文，未標明為 Wiki 自行推導。（3）Card 6（第 93 行）稱泰雅語「包含未實現前綴（如 `sa-`）卻帶有過去時間詞根……檢索詞庫中對應之『昨天』詞根，從而推導出『明天』之正確語義」；原文表 12（p. 14）明確標示賽考利克泰雅語 `sa`（如 `sa knwan` 過去何時、`sa kaxa'` 前天）為**實現（realis，過去）**標記而非未實現標記，且表 3（p. 7）顯示泰雅語「昨天」（`shera'/hera'`）與「明天」（`suxan`）屬異根（類型 1.2）。
- **來源**：`raw/my-focus/台灣相關論文/台灣南島語言時間詞之跨語言比較初探_林鴻瑞.pdf`（p. 7 表 3、p. 14 表 12、p. 27 英文摘要頁）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：`title` 與主標題改為英文摘要頁之正式題名 *A Preliminary Comparative Study of Formosan Temporal Words*；刪除 Card 3 原文未出現之 $T(\Delta t)$、$\operatorname{Root}$ 與三類代數式，改列表九之五個次類型與表十一之三種標記類型；Card 6 改正：賽考利克泰雅語 `sa` 為實現標記（表十二），且泛泰雅語「昨天」與「明天」詞根不同（表三），改以「前天＝後天＝`kaxa’`、靠標記區分」為延伸重點。另修正同頁未登記之問題：Card 4 註明原文表九與表十三對賽夏語歸類不一致；刪除 Card 5「重構幾何視角」「建立數學先驗」等無來源表述。證據表見 wiki/evidence/2024-formosan-temporal-words-lim.md。
