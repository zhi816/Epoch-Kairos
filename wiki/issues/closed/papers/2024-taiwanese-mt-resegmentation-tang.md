# 已結案問題：papers/2024-taiwanese-mt-resegmentation-tang.md

> 本檔收錄 [wiki/papers/2024-taiwanese-mt-resegmentation-tang.md](../../../papers/2024-taiwanese-mt-resegmentation-tang.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-065 | fixed | papers/2024-taiwanese-mt-resegmentation-tang.md | Card 3 | 原文不符
- **問題**：（1）第 43–56 行與架構圖稱使用 `IBM Model`／`fast_align` 統計詞對齊、點互資訊 $\operatorname{PMI}(w_i, t_j)$ 與 BERT 語言模型流暢度先驗進行全局最佳化；原文 §3.3（pp. 26–36）完全未使用統計詞對齊、PMI 或 BERT 流暢度打分，而是以最大二分匹配（Maximum Bipartite Matching，依同字 1.0、台華辭典翻譯 0.8、同義詞詞林 0.6 與最小子詞分數設定權重）執行四階段規則重斷詞（連續未對齊詞連接、部分對齊切分與同義詞重斷詞）。（2）第 59–62 行稱 BERT 台語斷詞器採用四分類 `B-I-E-S` 標籤；原文 §3.2（pp. 24–25，圖 14）明言「斷詞標記工作採用 BI 標籤模式」，僅有 `B` 與 `I` 二類標籤。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061），且 `concepts` 誤掛入 `formosan-computational-linguistics`（台語屬漢藏語系閩南語，非臺灣南島語）。
- **來源**：`raw/my-focus/學長姐論文/.md/利用重斷詞改善台語機器翻譯系統_湯景閔.md`（§3.2 pp. 24–25 圖 14、§3.3 pp. 26–36）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3.1–3.3、§4.1、§4.3 逐項確認後重寫 Card 3：刪除無來源之 IBM Model／fast_align、PMI 與 BERT 流暢度目標式，改述原文之最大二分匹配（1／0.8／0.6 與子詞最小分）與四步驟重斷詞；BERT 斷詞改為原文之 BI 兩類標籤。`concepts` 移除 `formosan-computational-linguistics`，並同步自該概念頁 `papers` 移除本頁。另修正同頁未登記之問題：Card 4 註明摘要「+7.56」為不同評估欄位之差值（同欄為 +9.19 或 +1.36），並補列字級 BLEU 與作者「不太能直接相比較」之說明；刪除 Card 1「首創」與 Card 5 無來源之概括。證據表見 wiki/evidence/2024-taiwanese-mt-resegmentation-tang.md。
