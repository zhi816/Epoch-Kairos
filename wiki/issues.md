# 內容問題清單（Issues）

> 本檔登記查核發現之待修正事項，格式與狀態規則見 [AGENTS.md](../AGENTS.md) 第七章第 4 節。標題五段依序為：編號、狀態（`open` / `fixed` / `wontfix`）、相對於 `wiki/` 之檔案、位置、判定。修正時就地改狀態並追加「處理」行，不得刪除條目；新編號以 `stage_issues.py --next-id` 取得。
>
> 本檔只放尚未結案之問題，不分節，依登記先後排列。已結案（`fixed` / `wontfix`）條目由 `archive_issues.py` 一次搬到 [wiki/issues/closed/](issues/closed/)，一頁一檔，路徑對應 `wiki/` 下之頁面；結案當下只改狀態，不要自行搬移。查某頁之未結問題與舊紀錄，執行 `python .agents/skills/wiki-content-audit/scripts/issues_for.py <slug>`。
>
> EK-001 至 EK-056 係於 2026-11-09 自 [wiki/log.md](log.md) 2026-11-08 21:40 至 23:36 之 audit 條目逐筆轉錄（原查核者均為 Codex by OpenAI，EK-031 例外），問題描述與來源沿用原條目，轉錄時未重新核對原文。修正前須依 `wiki-content-audit` 回原文確認，不得只照本檔描述改寫。EK-057 至 EK-060 為轉錄同日以 `crossref_check.py` 查得之 DOI 問題。EK-061 至 EK-087 於 2026-11-09 00:55 之 audit 逐筆登記（Antigravity by Google DeepMind）。EK-088 至 EK-090 為同日核對證據表採用版本與先前修正引用時發現之錯置（Claude Code / DeepSeek Harness）。EK-091 至 EK-123 為 2026-11-09 至 2026-11-10 第一、二批卡片回填查核登記（Claude Code by Anthropic 等）。EK-130 至 EK-142、EK-150 至 EK-160、EK-170 至 EK-175 為 2026-11-10 第三批卡片回填抽查與概念頁同步登記（A、B、C 組依保留區段取號）。原有 153 筆條目與後續複核新增條目之狀態，以各條標題為準。2026-11-22 起，EK-001 至 EK-233 已結案之 197 筆全數歸檔，原有之論文分節隨之取消。

---

### EK-248 | fixed | cards/2005-hall-wage-stickiness.md | Card 4 數字 3、4 | 過度表述
- **問題**：Card 4 數字 3 寫「21｜生產力由狀態 3 升到 4，J 每單位 z 的斜率」，省略原文之模型條件「固定工資模型」；數字 3、4 並使用卡片未說明之符號 J 與 z。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 60 第 1 欄（"In the fixed-wage model, when productivity rises from state 3 to state 4, J rises with a slope of 21 units of J for each unit of z"）；J 之定義見 p. 54（"Let J_s be the value the employer associates with a filled job after making the wage payment"）。
- **發現於**：2026-11-28 Hall 卡片重審迴圈第 1 輪，Antigravity by Google DeepMind（Gemini 4 Hydrogen）提出，Claude Code by Anthropic（Claude Opus 5.5）核對。
- **處理**：2026-11-28，Antigravity by Google DeepMind（Gemini 4 Hydrogen）改為「固定工資，狀態 3 升到 4，雇主價值對生產力斜率」與「同一比較改用對稱 Nash 議價，雇主價值對生產力斜率」（重審迴圈第 1 輪）；Antigravity by Google DeepMind（Gemini 3.8 Flash）與 Codex by OpenAI（GPT-6 Luna）審查通過。

### EK-249 | fixed | papers/2005-hall-wage-stickiness.md | Card 3 第 4 點 | 原文不符
- **問題**：正文引原文式 (19) 寫作 $z_t=z_t^{P}z_{st}^{M}$，原式均數復歸成分之下標為 $s_t$；同段名目慣性一句寫「部分漂移就來自有價格水準的漂移」，原文為整體價格水準（overall price level）。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 56 式 (19)；p. 57 第 1 欄（"part of its drift would arise from drift in the overall price level"）。
- **發現於**：2026-11-28 Hall 卡片重審迴圈第 1 輪，Antigravity by Google DeepMind（Gemini 4 Hydrogen）提出，Claude Code by Anthropic（Claude Opus 5.5）以原 PDF 頁面影像核對。
- **處理**：2026-11-28，Claude Code by Anthropic（Claude Opus 5.5）改為 $z_t=z_t^{P}z_{s_t}^{M}$、$z_{s_t}^{M}$ 與「來自整體價格水準的漂移」，並重建論文頁網頁。

### EK-250 | fixed | evidence/2005-hall-wage-stickiness.md | Card 3 名目慣性列、非平穩配置列 | 原文不符
- **問題**：名目慣性列寫「部分漂移即來自有價格水準的漂移」，原文為整體價格水準；非平穩配置列引原文寫「w_st = w」，原文印刷為 $w_{s_t} = w$。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 57 第 1–2 欄（"drift in the overall price level"；"the sticky wage rule w_{s_t} = w has exactly the same allocational consequences"）。
- **發現於**：2026-11-28 Hall 卡片重審迴圈第 1 輪，Antigravity by Google DeepMind（Gemini 4 Hydrogen）提出，Claude Code by Anthropic（Claude Opus 5.5）以原 PDF 頁面影像核對。
- **處理**：2026-11-28，Claude Code by Anthropic（Claude Opus 5.5）改為「來自整體價格水準的漂移」與「w_{s_t} = w」。
