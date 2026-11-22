# 已結案問題：papers/2026-tokenizations-austronesian-lms-lumbantobing.md

> 本檔收錄 [wiki/papers/2026-tokenizations-austronesian-lms-lumbantobing.md](../../../papers/2026-tokenizations-austronesian-lms-lumbantobing.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-232 | fixed | papers/2026-tokenizations-austronesian-lms-lumbantobing.md | 原 Card 1、Card 5、Card 6 | 原文未支持
- **問題**：原 Card 1 寫傳統 aksara「原本已失落」，原文 §2 只說 aksara 曾是群島主要書寫系統，沒有「失落」之說；原 Card 5 稱「零樣本音節相容性」，原文沒有 zero-shot 用語，只說詞表取自印尼語辭典（KBBI）、再於十種地方語上計算 TPC；原 Card 6 標題「群島神經分詞密碼」及「注意力機制看見哪些共享符號」「觸發同源共享注意力與梯度遷移」，但全篇沒有訓練任何神經模型，只比較分詞後的表層統計。
- **來源**：[原文 PDF](../../../../raw/my-focus/報告論文題材/2026-tokenizations-austronesian-lms-lumbantobing.pdf)，§2, pp. 2–3；§4.1, p. 7；§4.4, pp. 10–11；§5, p. 12。
- **發現於**：2026-11-20 改寫為我的關注新六章時回原文抽查，DeepSeek Harness（DeepSeek V4.1 Flash）提出，Claude Code by Anthropic（Claude Opus 5.5）核對。
- **處理**：2026-11-20，Claude Code by Anthropic（Claude Opus 5.5）。論文頁改為新六章，刪除上述說法；06 寫明只比較表層分詞、未接模型測下游；英語 TPC 的數值原文正文未給，論文頁標明依 Fig. 2 判讀，卡片不放。
