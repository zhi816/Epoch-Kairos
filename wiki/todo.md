# 待辦清單（Todo）

> 本檔登記尚未完成之工作：交接事項、做到一半的任務、須等使用者確認才能動工的工作。格式與規則見 [AGENTS.md](../AGENTS.md) 第七章第 5 節，接手順序見第六章第 4 節。標題四段依序為：編號、狀態（`open` / `waiting` / `doing`）、範圍（`wiki` / `web` / `raw` / `rule` / `skill`）、標題。完成或放棄之條目直接刪除，並於當次日誌條目寫明編號；新增前以 `stage_todo.py --next-id` 取號。
>
> 不收：Wiki 內容與原文不符之處（登記於 [issues.md](issues.md)）、美術方向之選擇題（登記於 [DESIGN.md](../DESIGN.md) 第八章）。

### TD-001 | open | wiki | 收錄原始 PDF 已入 raw/ 之 8 個立案條目
- **內容**：[index.md](index.md) 中下列 `[planned]` 條目之原始 PDF，已於 2026-11-09 由 Antigravity 標準化檔名後置於 `raw/` 根目錄，可依第六章 Ingest 逐篇收錄（Crossref 核驗、證據表、論文頁、概念頁、`card_line`）：Soai 不對稱自催化（`1995-soai-asymmetric-autocatalysis.pdf`）、MOFs（`1999-metal-organic-frameworks-mof5.pdf`）、超導電路巨觀量子穿隧（`1985-macroscopic-quantum-tunneling.pdf`）、Treg（`1995-treg-immune-tolerance.pdf`、`2001-foxp3-scurfin.pdf`）、microRNA（`1993-microrna-lin4-ambros.pdf`、`1993-microrna-lin14-ruvkun.pdf`）、GLP-1（`1987-glp1-receptor-agonist.pdf`）、水稻 QT12（`2025-rice-qt12-thermotolerance.pdf`）、鹼基編輯療法（`2025-in-vivo-base-editing.pdf`）。這些條目在 index.md 中仍註記「`raw/` 暫無原始檔」，收錄時一併更正。
- **完成條件**：8 個條目皆有 `wiki/papers/` 頁，index.md 對應註記已更正，`lint_wiki.py` 無 ERROR。可逐篇進行，每收錄一篇即從本條內容移除該篇。
- **來源**：wiki/log.md [2026-11-09 09:18] git（raw/ 檔名標準化）與 index.md 原「待辦與已知問題」一節；2026-11-09 登記，Claude Code by Anthropic。

### TD-002 | waiting | web | 產出 web/ 展示層並將論文頁升級為 published
- **內容**：`web/` 目前只有 `prototypes/` 樣稿（mobile-v1、mobile-v2）與空的 `papers/`，尚無 `web/index.html` 與任何 `web/papers/<slug>/index.html`；41 篇論文頁皆為 `status: "wiki"`，Lint 第 3 條三層對齊因而未通過。依第六章 Ingest 第 4 步與第七章第 3 節產出首頁時間線與各論文雙欄頁後，將對應論文頁改為 `published`。
- **完成條件**：`web/index.html` 與各論文之 `web/papers/<slug>/index.html` 產出，對應論文頁 `status` 改為 `published`，`lint_wiki.py` 無 ERROR。
- **等待**：[DESIGN.md](../DESIGN.md) 第八章待決事項定案，至少第 1 項（首頁主案 v4 定稿）、第 9 項（論文頁視覺）與第 10 項（樣稿移植至 `web/`）。
- **來源**：wiki/log.md [2026-11-07 22:47] audit「延後處理」與 index.md 原「待辦與已知問題」一節；2026-11-09 登記，Claude Code by Anthropic。

### TD-003 | waiting | raw | 取得光遺傳學頁奠基論文 Nagel et al. (2002) 原始 PDF
- **內容**：[2005-optogenetics](papers/2005-optogenetics.md) 之 `key_papers` 列有 Nagel et al. (2002) *Science* 296:2395-2398（https://doi.org/10.1126/science.1072068），`raw/` 尚無原始檔（Nagel et al. (2003) *PNAS* 已存為 `raw/2003-channelrhodopsin2.pdf`）。依第五章，AI 不得擅自寫入 `raw/`。
- **完成條件**：原始 PDF 置於 `raw/` 並推送至 Mine-RAW。
- **等待**：使用者自行放入 PDF，或明確指示下載。
- **來源**：wiki/log.md [2026-11-08 21:37] git「仍待補」與 index.md 原「待辦與已知問題」一節；2026-11-09 登記，Claude Code by Anthropic。

### TD-004 | waiting | wiki | 補填 6 筆日誌條目之「模型版本」欄
- **內容**：下列日誌條目之「模型版本」欄為佔位文字「本次工作階段之平台政策禁止將模型型號寫入版控檔案，請使用者自行補填」，不符第九章須載明模型版本之規定：[2026-11-06 22:12] rule、[2026-11-07 22:47] 四筆（rule、fix、update、audit）、[2026-11-08 14:14] git。
- **完成條件**：依使用者決定補填或註記完畢；若決定維持原樣，經同意後刪除本條。
- **等待**：使用者提供當時之模型型號，並決定直接補入原條目（屬修改舊條目，須使用者明示同意）、另追加更正條目，或維持原樣。
- **來源**：wiki/log.md [2026-11-07 22:47] audit「待使用者處理」第 1 項；2026-11-09 登記，Claude Code by Anthropic。
