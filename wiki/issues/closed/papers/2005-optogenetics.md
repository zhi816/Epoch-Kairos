# 已結案問題：papers/2005-optogenetics.md

> 本檔收錄 [wiki/papers/2005-optogenetics.md](../../../papers/2005-optogenetics.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-219 | fixed | papers/2005-optogenetics.md | Card 3 展示公式 | 未能核實
- **問題**：2026-11-10 曾以 EK-204 登記此頁多組展示公式未見於 Boyden 等（2005）原文，並在當時修正；提交 `0a17f2f` 回退收錄時同時刪除了該問題與修正。現行頁面再次包含相關公式，須回原文核對其出處與歸屬，並依現行公式規範處理。本條恢復追蹤，不將當時已回退的修正視為現況。
- **來源**：原問題與處理紀錄（提交 `b2dbc80` 版本）見本條「前身」行；回退見提交 `0a17f2f`；原文典藏 `raw/2005-optogenetics.pdf`。
- **發現於**：2026-11-11 日誌與 Git 歷史審查，Codex by OpenAI（GPT-6）；原問題於 2026-11-10 由 Antigravity by Google DeepMind 登記。
- **處理**：原 EK-204 已用於另一問題，依編號不重用原則以 EK-219 恢復追蹤；尚未重新逐式核對原文。
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。逐頁檢視原 PDF 印刷頁 1263–1268，確認原文未列原頁四組展示公式；已移除並以原文 p.1264 與 Fig. 1 的實驗觀察及來源界線取代，建立限於本次查核範圍的證據表。未逐項核實全頁，`verification` 設為 `partial`。
- **前身**：回退前之原條目，2026-11-10 登記並結案，隨提交 `0a17f2f` 自問題清單刪除；2026-11-22 經使用者同意併入本條，內容照原文，僅相對連結換算為本檔位置。原標題為「EK-204（舊號，現已用於另一問題） | fixed | papers/2005-optogenetics.md | Card 3 展示公式未見於原文 | 原文未支持」：
  - **問題**：原論文頁 Card 3 列出光電流方程、三態連續馬可夫動力學與 Hodgkin-Huxley 整合微分方程等三組區塊展示公式，皆非 Boyden et al. (2005) 本文所載之公式；原文為實驗技術報告，全篇無編號數學展示式，上述公式實為後續生物物理學文獻之理論模型。
  - **來源**：[Boyden 等原文](../../../../raw/2005-optogenetics.pdf) Nature Neuroscience 8(9):1263–1268 全文；[論文頁](../../../papers/2005-optogenetics.md) Card 3。
  - **發現於**：2026-11-10，依 TD-017 / 2026-11-10 規則建立證據表與卡片檔，Antigravity by Google DeepMind。
  - **處理**：2026-11-10，Antigravity by Google DeepMind（Gemini 3.8 Flash）。移除論文頁未見於原文之三組展示公式，改以作者對光電流動力學（峰值 $496\text{ pA}$、穩態 $193\text{ pA}$、上升率 $160\text{ pA/ms}$、恢復 $\tau = 5.1\text{ s}$）之實驗數據與測量說明呈現；建立證據表登記 24 列主張，卡片 Card 3 採無公式模式。頁面核實狀態改為 verified。

### EK-220 | fixed | papers/2005-optogenetics.md | Card 3 載體與輔因子 | 歸因／版本錯置
- **問題**：原頁把 AAV 與細胞類型特異性啟動子寫在本篇機制中，未區分本篇實際使用的慢病毒與作者提出的後續方向；對輔因子的表述亦未交代 ChR2 本身仍需全反式視黃醛。
- **來源**：Boyden 等（2005）印刷頁 1264 Results 首段；p.1267 Discussion 與 Methods「Plasmid constructs」。
- **發現於**：2026-11-11 處理 EK-219 時，Codex by OpenAI（GPT-6）回核原 PDF。
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。改寫為本篇使用慢病毒導入培養海馬體神經元；將細胞類型特異性啟動子與活體應用標為作者提出的未來方向，並補充本篇未額外添加、背景及培養基可能提供輔因子；證據表逐項登記。
