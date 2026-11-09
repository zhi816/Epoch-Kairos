# 待辦清單（Todo）

> 本檔登記尚未完成之工作：交接事項、做到一半的任務、須等使用者確認才能動工的工作。格式與規則見 [AGENTS.md](../AGENTS.md) 第七章第 5 節，接手順序見第六章第 4 節。標題四段依序為：編號、狀態（`open` / `waiting` / `doing`）、範圍（`wiki` / `web` / `raw` / `rule` / `skill`）、標題。完成或放棄之條目直接刪除，並於當次日誌條目寫明編號；新增前以 `stage_todo.py --next-id` 取號。
>
> 不收：Wiki 內容與原文不符之處（登記於 [issues.md](issues.md)）、美術方向之選擇題（登記於 [DESIGN.md](../DESIGN.md) 第八章）。

### TD-001 | open | wiki | 收錄原始 PDF 已入 raw/ 之 8 個立案條目
- **內容**：[index.md](index.md) 中下列 `[planned]` 條目之原始 PDF，已於 2026-11-09 由 Antigravity 標準化檔名後置於 `raw/` 根目錄，可依第六章 Ingest 逐篇收錄（Crossref 核驗、證據表、論文頁、概念頁、`card_line`）：Soai 不對稱自催化（`1995-soai-asymmetric-autocatalysis.pdf`）、MOFs（`1999-metal-organic-frameworks-mof5.pdf`）、超導電路巨觀量子穿隧（`1985-macroscopic-quantum-tunneling.pdf`）、Treg（`1995-treg-immune-tolerance.pdf`、`2001-foxp3-scurfin.pdf`）、microRNA（`1993-microrna-lin4-ambros.pdf`、`1993-microrna-lin14-ruvkun.pdf`）、GLP-1（`1987-glp1-receptor-agonist.pdf`）、水稻 QT12（`2025-rice-qt12-thermotolerance.pdf`）、鹼基編輯療法（`2025-in-vivo-base-editing.pdf`）。這些條目在 index.md 中仍註記「`raw/` 暫無原始檔」，收錄時一併更正。
- **完成條件**：8 個條目皆有 `wiki/papers/` 頁，index.md 對應註記已更正，`lint_wiki.py` 無 ERROR。可逐篇進行，每收錄一篇即從本條內容移除該篇。
- **來源**：wiki/log.md [2026-11-09 09:18] git（raw/ 檔名標準化）與 index.md 原「待辦與已知問題」一節；2026-11-09 登記，Claude Code by Anthropic。

### TD-002 | waiting | web | 產出 web/ 展示層並將論文頁升級為 published
- **內容**：`web/` 目前只有 `prototypes/` 樣稿（mobile-v1、mobile-v2）與空的 `papers/`，尚無 `web/index.html` 與任何 `web/papers/<slug>/index.html`；41 篇論文頁皆為 `status: "wiki"`，Lint 第 3 條三層對齊因而未通過。依第六章 Ingest 第 4 步與第七章第 3 節產出首頁時間線與各論文雙欄頁後，將對應論文頁改為 `published`。首頁首版（知識星圖）已於 2026-11-09 完成（原 TD-006，由 `tools/build_home.py` 產生），本條以論文頁為主。
- **完成條件**：`web/index.html` 與各論文之 `web/papers/<slug>/index.html` 產出，對應論文頁 `status` 改為 `published`，`lint_wiki.py` 無 ERROR。
- **等待**：[DESIGN.md](../DESIGN.md) 第八章待決事項定案。第 9 項（論文頁視覺）已於 2026-11-09 定案為樣稿「論文頁 F」（DESIGN.md 第五章），第 10 項已隨首版首頁完成；第 14 項（卡組丁深色重點色）亦已定案；第 1 項（首頁主案 v4）已於 2026-11-09 由使用者表示暫定。論文頁正式產出仍待 TD-008 卡片文字檔，並請使用者確認何時動工；在此之前以 `tools/build_paper_prototype.py` 產生之 `web/prototypes/paper-v1/` 原型代替。實作時將深色重點色寫入 `theme.css`（`--deep-<domain>`）並同步 AGENTS.md 第二章色表（DESIGN.md 第七章）。
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

### TD-005 | waiting | web | 以 GitHub Actions 將 web/ 發布至 GitHub Pages
- **內容**：GitHub Pages 之「Deploy from a branch」只接受倉庫根目錄或 `/docs`，無法直接發布 `web/`，且主倉庫目前尚無 `.github/` 目錄。新增 `.github/workflows/pages.yml`：推送至 `main` 且 `web/**` 有變動時觸發（另加 `workflow_dispatch` 供手動重新發布），依序以 `actions/checkout`、`actions/configure-pages`、`actions/upload-pages-artifact`（`path: web`）、`actions/deploy-pages` 發布，只公開 `web/` 之內容，`wiki/`、`AGENTS.md` 等不上站；寫入前先確認各 action 之最新主版本號。首頁檔名維持 `web/index.html`、論文頁維持 `web/papers/<slug>/index.html`，網址即 `https://zhi816.github.io/Epoch-Kairos/` 與 `https://zhi816.github.io/Epoch-Kairos/papers/<slug>/`。發布後將 README.md「GitHub Pages 成果展示」一行之暫定連結改為正式連結。
- **完成條件**：工作流程首次執行成功（倉庫 Actions 分頁顯示成功），首頁網址可正常開啟，`assets/` 與 KaTeX 資源載入無誤，README 連結已更新。
- **等待**：首頁加入群星檔案卡片牆（TD-009）、使用者確定首頁 `web/index.html` 後再發布（首頁其餘部分已於 2026-11-09 暫定）；屆時由使用者至倉庫 Settings → Pages 將 Source 改為「GitHub Actions」，並確認倉庫為公開（私有倉庫之 Pages 需付費方案）。
- **進度**：使用者已於 2026-11-09 同意我的星系公開其研究主題（臺灣南島語計算語言學、低資源機器翻譯）與 24 篇關注論文；碩論題目、資料與結果仍不公開（DESIGN.md 第八章第 13 項、paper-card-writer 第二節第 13 條）。
- **來源**：使用者指示（首頁確定後再發布）；2026-11-09 登記，Claude Code by Anthropic。

### TD-007 | open | wiki | 建立證據表「類型」欄白名單並清點違規列
- **內容**：`wiki/evidence/` 各表之「類型」欄目前混用組合值與白名單外描述，例如 [1992-creative-destruction-aghion.md](evidence/1992-creative-destruction-aghion.md) 之「本篇研究結果 / 官方事實」、[2001-colonial-origins-acemoglu.md](evidence/2001-colonial-origins-acemoglu.md) 之「本篇研究結果 / 作者解釋」與「後續研究 / 政策推論」，不符 AGENTS.md 第七章第 4 節所定五類（本篇研究結果、後續研究、作者解釋、依原文數據計算、Wiki 詮釋）。應先全庫清點所有不合規列並列出清單與建議類型，再決定處置方式；每一列須回原文判斷主張歸屬，不得機械拆解組合值或批次改寫。
- **完成條件**：清單列畢且經使用者確認處置方式（逐列修正，或於 AGENTS.md 明訂組合值之使用規則），必要時 `lint_wiki.py` 增列檢查；未經確認前不動任何證據表。
- **來源**：使用者指示（2026-11-09 交接，承接 EK-090 之證據表類型觀察）；2026-11-09 登記，DeepSeek Harness（DeepSeek-V4.1-Flash）。

### TD-008 | doing | wiki | 依 paper-card-writer 回填其餘 39 篇論文之卡片文字檔
- **內容**：目前只有 [1982-hopfield-network](cards/1982-hopfield-network.md) 與 [2021-seediq-chinese-mt-you](cards/2021-seediq-chinese-mt-you.md) 有卡片文字檔。其餘 39 篇依 [`paper-card-writer`](../.agents/skills/paper-card-writer/SKILL.md) 逐篇撰寫 `wiki/cards/<slug>.md`（封面斷行、導語、Card 2 至 6、Card 3 示意圖）。每篇都要完成該 Skill 第五節第 1 至 9 步，**包括第 7 步建置論文頁原型並驗證**（`python tools/build_paper_prototype.py <slug>` 自我檢查 ERROR 0；有瀏覽器工具者 `verify_page.js` 結果 PASS，細則見 `references/paper-page.md`），交付說明依第八節格式逐項填寫，一篇一個提交。須遵守該 Skill 第七節批次規則：一次一篇、每篇重開論文頁與證據表、每五篇重讀硬規則、用量不足以做完一整篇時不開新篇；交付前逐項核對第十一節偷工自查表。`2005-optogenetics` 與 `2016-ligo-gravitational-waves` 尚無證據表，須先依 `wiki-content-audit` 建立證據表才能寫卡片；論文頁 `verification` 為 `issues` 者，先確認問題是否影響卡片內容。我的關注論文之內頁配色已暫定與群星相同之學科色底（DESIGN.md 第五章第 2 節），不影響文字撰寫。另：`tools/build_home.py` 之 `STUDY_TYPE` 對照表日後改讀卡片檔「研究類型」，論文頁建置（TD-002）改讀 `wiki/cards/`。
- **完成條件**：41 篇論文皆有卡片文字檔與 `web/prototypes/paper-v1/<slug>.html`，`python .agents/skills/paper-card-writer/scripts/check_cards.py --missing` 無 ERROR、無 INFO（缺檔）列，`python tools/build_paper_prototype.py`（不帶參數）全部自我檢查 ERROR 0，WARN 逐條處理或於日誌交代；未以瀏覽器驗證之篇目列於 `wiki/todo.md` 待補驗。可分批進行，每篇一筆日誌與一個提交；只寫了卡片檔而未建置驗證之篇目不算完成。
- **負責**：第一批由三個對話分工（見進度），各做 6 篇；第二批由協調者（Claude Code，本條登記者）於第一批完成後分配。
- **進度**：2026-11-09 第一批分配（以 `random.Random(20261109)` 自 37 篇可寫論文隨機抽 18 篇；`2005-optogenetics`、`2016-ligo-gravitational-waves` 尚無證據表，不列入）。A 組（Claude Code 協調者所在對話，預覽埠 8781）：`2024-sora-world-simulator`、`2013-icecube-neutrino`、`2025-nerve-mito-cancer`、`2026-data-centric-russian-kyrgyz-mt-novokshanov`、`2024-finnish-northern-sami-mt-saleva`、`2021-alphafold2`。B 組（預覽埠 8782）：`2024-formosan-mt-bilingual-lexicon-zheng`、`2007-woodford-inflation-dynamics`、`2025-deepseek-r1`、`2001-colonial-origins-acemoglu`、`2025-indigenous-tek-ai-revitalization-wang`、`2023-jwst-massive-galaxies`。C 組（預覽埠 8783）：`2026-epark-formosan-dialectometry-gagnier`、`2025-fragment-shot-reasoning-mt-frontull`、`2025-atayalic-oov-enumeration-yang`、`2023-low-resource-nmt-survey-ranathunga`、`2025-atayalic-affix-mt-jin`、`2024-taiwanese-mt-resegmentation-tang`。其餘 19 篇待第二批分配，第一批期間不得接手。第一批結果（2026-11-09 23:35）：A 組完成 `2013-icecube-neutrino`、`2021-alphafold2`；`2024-sora-world-simulator`（Card 5 附出處之後續研究僅一筆、Card 4 部分說法未見於證據表）、`2026-data-centric-russian-kyrgyz-mt-novokshanov`（論文頁無區塊公式）、`2024-finnish-northern-sami-mt-saleva`（論文頁無後續研究）停止，`2025-nerve-mito-cancer` 撰寫時對話中止而未完成；C 組 6 篇皆因論文頁無區塊公式或無外部事件而停止，並提出兩頁疑點，經協調者回原文核對後登記 EK-091、EK-092（另一項 GPT-4o 23.03 → 21.18 經核對為 Gherdëina → Italian 列，數字正確）；B 組進行中（已提交 `2001-colonial-origins-acemoglu`）。停止與未完成之篇目放回待分配，待使用者決定 Card 3 無公式、Card 5 無後續研究之處理方式後，與其餘篇目一併重新分配。並行協調規則（優先於 Skill 中登記 `wiki/todo.md` 與 `wiki/issues.md` 之指示）：只碰自己組別之 `wiki/cards/<slug>.md` 與 `web/prototypes/paper-v1/<slug>.html`；`build_paper_prototype.py` 一律帶 slug 執行；不重建首頁、不改 `wiki/todo.md`、`wiki/issues.md`、論文頁與證據表，發現來源問題或無法以瀏覽器驗證時，該篇於最後回報中寫明，由協調者統一處理；提交以 `safe_commit_push.py` 並加 `--log-heading` 精確指定自己的日誌標題。
- **來源**：使用者指示（2026-11-09，建立卡片撰寫 Skill）；2026-11-09 登記，Claude Code by Anthropic。

### TD-009 | waiting | web | 首頁加入群星檔案卡片牆
- **內容**：依 [DESIGN.md](../DESIGN.md) 第二章第 3 節實作首頁下方之群星檔案卡片牆：F 版型「星窗＋一句話」，桌面 3 欄、手機 2 欄，群星為學科色底，我的關注為深色卡＋藍框。由 `tools/build_home.py` 讀取 `wiki/cards/<slug>.md` 之「封面斷行」與 Frontmatter 產生，不手寫資料、不得以程式自動切行（paper-card-writer 之 `references/cover.md` 第三節）；首頁卡片之雙年份用簡稱「諾貝爾獎」。點卡片進入論文頁：正式論文頁（TD-002）產出前連到 `web/prototypes/paper-v1/<slug>.html` 或暫不連結，動工時請使用者決定。完成後將 DESIGN.md 第二章第 0 節「首版不做卡片牆」改為已實作。
- **完成條件**：`web/index.html` 卡片牆列出全部已收錄論文，每張卡之封面斷行取自卡片檔，`python tools/build_home.py --check` 一致；桌面 1440 x 900 與手機 375 x 812 截圖確認無溢出與重疊；DESIGN.md、AGENTS.md 第四章首頁描述同步。
- **等待**：TD-008 完成（卡片牆每張卡之封面斷行須取自卡片檔，目前 41 篇只有 2 篇）；是否先以已完成之卡片檔做出部分卡片牆，待使用者決定。
- **來源**：使用者指示（2026-11-09：首頁目前已暫定，剩下方卡片牆要加入，但卡片尚未完成）；2026-11-09 登記，Claude Code by Anthropic。
