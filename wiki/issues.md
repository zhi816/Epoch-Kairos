# 內容問題清單（Issues）

> 本檔登記查核發現之待修正事項，格式與狀態規則見 [AGENTS.md](../AGENTS.md) 第七章第 4 節。標題五段依序為：編號、狀態（`open` / `fixed` / `wontfix`）、相對於 `wiki/` 之檔案、位置、判定。修正時就地改狀態並追加「處理」行，不得刪除條目；新編號以 `stage_issues.py --next-id` 取得。
>
> 本檔只放尚未結案之問題，不分節，依登記先後排列。已結案（`fixed` / `wontfix`）條目由 `archive_issues.py` 一次搬到 [wiki/issues/closed/](issues/closed/)，一頁一檔，路徑對應 `wiki/` 下之頁面；結案當下只改狀態，不要自行搬移。查某頁之未結問題與舊紀錄，執行 `python .agents/skills/wiki-content-audit/scripts/issues_for.py <slug>`。
>
> EK-001 至 EK-056 係於 2026-11-09 自 [wiki/log.md](log.md) 2026-11-08 21:40 至 23:36 之 audit 條目逐筆轉錄（原查核者均為 Codex by OpenAI，EK-031 例外），問題描述與來源沿用原條目，轉錄時未重新核對原文。修正前須依 `wiki-content-audit` 回原文確認，不得只照本檔描述改寫。EK-057 至 EK-060 為轉錄同日以 `crossref_check.py` 查得之 DOI 問題。EK-061 至 EK-087 於 2026-11-09 00:55 之 audit 逐筆登記（Antigravity by Google DeepMind）。EK-088 至 EK-090 為同日核對證據表採用版本與先前修正引用時發現之錯置（Claude Code / DeepSeek Harness）。EK-091 至 EK-123 為 2026-11-09 至 2026-11-10 第一、二批卡片回填查核登記（Claude Code by Anthropic 等）。EK-130 至 EK-142、EK-150 至 EK-160、EK-170 至 EK-175 為 2026-11-10 第三批卡片回填抽查與概念頁同步登記（A、B、C 組依保留區段取號）。原有 153 筆條目與後續複核新增條目之狀態，以各條標題為準。2026-11-22 起，EK-001 至 EK-233 已結案之 197 筆全數歸檔，原有之論文分節隨之取消。

---

### EK-235 | fixed | evidence/2005-hall-wage-stickiness.md | Card 5 結論列 | 原文未支持
- **問題**：起草稿該列主張「模型在工資從不落到議價集合之外這一點達到嚴格預測力」與「needs to be guided by evidence…」整列來源標為 p. 65 第 1 欄；前半兩句實在 p. 64。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 64 第 2 欄（"strict standard of predictive power"、"never falls outside the bargaining set"）、p. 65 第 1 欄（"needs to be guided by evidence about actual wage determination"）。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 1 輪，Command Code（GLM-5.3 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 將來源改為 pp. 64–65 並分句標頁（迴圈第 2 輪）。

### EK-236 | fixed | papers/2005-hall-wage-stickiness.md | Card 5 末段 | 原文未支持
- **問題**：起草稿 Card 5 末段「嚴格的預測力……（needs to be guided by evidence…）」全段只標 (p. 65)，前半內容實在 p. 64；與 EK-235 同源。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 64 第 2 欄、p. 65 第 1 欄。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 1 輪，Command Code（GLM-5.3 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 改標 pp. 64–65（迴圈第 2 輪）。
- **關聯**：EK-235

### EK-237 | fixed | evidence/2005-hall-wage-stickiness.md | 適應性工資列 | 原文未支持
- **問題**：起草稿適應性工資（式 (25)）列來源寫 pp. 64–65；式 (25)、"The wage becomes a new state variable of the model" 與 "essentially arbitrary and could take many other forms" 全在 p. 64，p. 65 無此內容。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 64 第 1、2 欄。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 2 輪，Command Code（MiniMax M3.1 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 改為 p. 64 並分欄標註（迴圈第 3 輪）。

### EK-238 | fixed | evidence/2005-hall-wage-stickiness.md | 校準列（x = 0.539） | 原文未支持
- **問題**：起草稿證據表校準列與論文頁「平均職缺失業比 0.539」都標 p. 58；該句在 p. 57 第 2 欄，p. 58 才是 k = 0.986 與 $z_3=1$。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 57 第 2 欄（"the average value of the vacancy/unemployment ratio, x, … was 0.539"）、p. 58 第 1 欄。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 2 輪，Command Code（MiniMax M3.1 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 將證據表來源改為 pp. 57–58 逐句分欄，論文頁拆為 0.539（p. 57）與 k（p. 58）（迴圈第 3 輪）。

### EK-239 | fixed | evidence/2005-hall-wage-stickiness.md | 失業反應列 | 原文未支持
- **問題**：起草稿該列「matches the actual response reasonably closely」標為 p. 62 第 2 欄，實在第 1 欄；第 2 欄才是 11 percentage points 與 one percentage point。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 62 第 1、2 欄。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 2 輪，Command Code（MiniMax M3.1 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 改為分欄標註（迴圈第 3 輪）。

### EK-240 | fixed | evidence/2005-hall-wage-stickiness.md | 彈性比較列（1.7、1.8、7.2、94） | 原文未支持
- **問題**：起草稿該列來源寫「p. 63 第 2 欄至 p. 64 第 1 欄」，漏列 1.7 與 1.8 所在之 p. 63 第 1 欄。審查者原建議把 7.2、0.391 也改標第 1 欄，作者反駁、審查者於下一輪以正規化連字後重測撤回該部分；7.2、0.391、94 確在第 2 欄。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 63 第 1 欄（1.7、1.8）、第 2 欄（7.2、0.391、94）。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 2 輪，Command Code（MiniMax M3.1 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 改為「p. 63 第 1 欄（1.7、1.8）與第 2 欄（7.2、0.391、94）」，未採納 7.2、0.391 改欄之建議（迴圈第 3 輪）。

### EK-241 | fixed | papers/2005-hall-wage-stickiness.md | Card 5 首句 | 原文未支持
- **問題**：起草稿 Card 5 首句「把工資僵固性……當成均衡選擇機制」標 (pp. 50–51、56)；"equilibrium selection" 只出現在 p. 55 與 p. 64，所引頁無此語，且證據表未登記。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 55 第 1 欄（"Nash proposed the celebrated equilibrium selection rule"）、p. 64 第 2 欄（"wage stickiness is an equilibrium selection mechanism"）。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 2 輪，Command Code（MiniMax M3.1 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 改標 pp. 50–51、55–56、64，並於證據表新增一列（迴圈第 3 輪）。

### EK-242 | fixed | evidence/2005-hall-wage-stickiness.md | 校準列（230 units） | 原文未支持
- **問題**：校準列引用 "The worker's career is worth about 230 units of monthly productivity"，來源欄只寫 Table 4 解讀在 p. 58 第 2 欄；該句在 p. 58 第 1 欄。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 58 第 1 欄。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 3 輪，Command Code（MiniMax M3.1 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，DeepSeek Harness（DeepSeek V4.1 Flash） 將該列來源逐句分欄（迴圈第 4 輪）。
- **關聯**：EK-238

### EK-243 | fixed | evidence/2005-hall-wage-stickiness.md | Pissarides 後續研究列 | 原文未支持
- **問題**：Pissarides 列寫「§1 並稱 as Hall (2005a) notes…」；該句在 CEP DP 839 之無編號引言（PDF 第 4 頁），§1 始於 PDF 第 6 頁。
- **來源**：Pissarides (2007) CEP Discussion Paper No. 839，PDF 第 4 頁（引言）、第 6 頁（§1 標題）；正式版 Econometrica 77(5):1339–1369，https://doi.org/10.3982/ecta7562 。
- **發現於**：2026-11-28 收錄本篇之互審迴圈第一階段第 4 輪，Command Code（MiniMax M3.1 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對（下載 CEP DP 839 確認）。
- **處理**：2026-11-28，Claude Code by Anthropic（Claude Opus 5.5） 改為「引言（PDF 第 4 頁；§1 始於 PDF 第 6 頁）」，並將第 6 行核對範圍說明同步改為「引言」。

### EK-244 | fixed | evidence/2005-hall-wage-stickiness.md | Card 5 獎項列 | 原文未支持
- **問題**：獎項列「類型」寫成「後續研究（機構頒獎事實）」，不在證據表規定之五類內。
- **來源**：AGENTS.md 第七章第 4 節證據表格式；NobelPrize.org 2026 年經濟科學獎 press release，https://www.nobelprize.org/prizes/economic-sciences/2026/press-release/ 。
- **發現於**：2026-11-28 收錄本篇之互審迴圈卡片階段第 1 輪，Command Code（GLM-5.3 Flash） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，Antigravity by Google DeepMind（Gemini 3.8 Flash） 將類型改為「後續研究」，保留官方來源（卡片迴圈第 1 輪）。

### EK-245 | fixed | cards/2005-hall-wage-stickiness.md | Card 3 說明 | 原文未支持
- **問題**：Card 3 說明末步只寫「中位 Nash 校準」，沒有交代原文產生 Card 4 數字的設定：固定工資取中位狀態之 Nash 議價工資，再解固定工資模型。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 58（"Then I set the fixed wage to the Nash-bargain wage for the median state and solve the fixed-wage model"）。
- **發現於**：2026-11-28 收錄本篇之互審迴圈卡片階段第 1 輪，Codex by OpenAI（GPT-6 Luna） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，Antigravity by Google DeepMind（Gemini 3.8 Flash） 改為「取中位 Nash 工資解模型」（卡片迴圈第 2 輪）。

### EK-246 | fixed | cards/2005-hall-wage-stickiness.md | Card 4 數字 2 | 過度表述
- **問題**：Card 4 寫「50%｜2000 至 2003 年，招募努力由峰到谷的跌幅」；原文 50% 是求才廣告（help-wanted advertising）的峰谷跌幅，作者稱 "Recruiting effort as measured by advertising"，卡片省略了測量指標。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 52 第 1 欄（"It is not uncommon for advertising to fall by 50 percent from peak to trough, as it did from 2000 to 2003"）。
- **發現於**：2026-11-28 收錄本篇之互審迴圈卡片階段第 1 輪，Codex by OpenAI（GPT-6 Luna） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，Antigravity by Google DeepMind（Gemini 3.8 Flash） 改為「求才廣告指數 2000 至 2003 年峰至谷跌幅」（卡片迴圈第 2 輪）。

### EK-247 | fixed | cards/2005-hall-wage-stickiness.md | Card 6 結語 | 過度表述
- **問題**：Card 6 結語與論文頁 Card 6 第 1 點寫「工資不調整在議價集合外是無效率」，省略原文之條件：雙方本可藉調整工資而都更好。
- **來源**：Hall (2005) AER 95(1):50–65，https://doi.org/10.1257/0002828053828482，p. 56（"under conditions where both worker and employer could have been better off with a wage adjustment"）。
- **發現於**：2026-11-28 收錄本篇之互審迴圈卡片階段第 1 輪，Codex by OpenAI（GPT-6 Luna） 提出，Claude Code by Anthropic（Claude Opus 5.5） 核對。
- **處理**：2026-11-28，Antigravity by Google DeepMind（Gemini 3.8 Flash） 將卡片改為「在議價集合外會阻礙互利配對」，論文頁同步補入「會阻礙本可互利的配對成立或存續」（卡片迴圈第 2 輪）。
