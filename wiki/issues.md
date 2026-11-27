# 內容問題清單（Issues）

> 本檔登記查核發現之待修正事項，格式與狀態規則見 [AGENTS.md](../AGENTS.md) 第七章第 4 節。標題五段依序為：編號、狀態（`open` / `fixed` / `wontfix`）、相對於 `wiki/` 之檔案、位置、判定。修正時就地改狀態並追加「處理」行，不得刪除條目；新編號以 `stage_issues.py --next-id` 取得。
>
> 本檔只放尚未結案之問題，不分節，依登記先後排列。已結案（`fixed` / `wontfix`）條目由 `archive_issues.py` 一次搬到 [wiki/issues/closed/](issues/closed/)，一頁一檔，路徑對應 `wiki/` 下之頁面；結案當下只改狀態，不要自行搬移。查某頁之未結問題與舊紀錄，執行 `python .agents/skills/wiki-content-audit/scripts/issues_for.py <slug>`。
>
> EK-001 至 EK-056 係於 2026-11-09 自 [wiki/log.md](log.md) 2026-11-08 21:40 至 23:36 之 audit 條目逐筆轉錄（原查核者均為 Codex by OpenAI，EK-031 例外），問題描述與來源沿用原條目，轉錄時未重新核對原文。修正前須依 `wiki-content-audit` 回原文確認，不得只照本檔描述改寫。EK-057 至 EK-060 為轉錄同日以 `crossref_check.py` 查得之 DOI 問題。EK-061 至 EK-087 於 2026-11-09 00:55 之 audit 逐筆登記（Antigravity by Google DeepMind）。EK-088 至 EK-090 為同日核對證據表採用版本與先前修正引用時發現之錯置（Claude Code / DeepSeek Harness）。EK-091 至 EK-123 為 2026-11-09 至 2026-11-10 第一、二批卡片回填查核登記（Claude Code by Anthropic 等）。EK-130 至 EK-142、EK-150 至 EK-160、EK-170 至 EK-175 為 2026-11-10 第三批卡片回填抽查與概念頁同步登記（A、B、C 組依保留區段取號）。原有 153 筆條目與後續複核新增條目之狀態，以各條標題為準。2026-11-22 起，EK-001 至 EK-233 已結案之 197 筆全數歸檔，原有之論文分節隨之取消。

---
