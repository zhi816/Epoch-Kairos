# Epoch-Kairos 知識庫操作日誌 (Operation Log)

> 本日誌為嚴格按時間追加（Append-only）之紀錄，完整追蹤知識庫的每一次 Ingest（收錄）、Query（綜述）、Lint（健康檢查）與架構更新。
> **日誌追溯規範**：每一次日誌寫入，均必須在第一條明確標註執行操作之「AI 代理身分名稱」與「底層模型版本型號」，以維持知識演進歷史的透明度、學術可信度與可追溯性。全篇嚴格禁止使用任何表情符號。

---

## [2026-11-04 18:30] init | Epoch-Kairos 知識庫與架構初始化
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **架構設計**：導入 Andrej Karpathy 之 LLM Wiki 三層模式（raw/、wiki/、AGENTS.md、web/）。
- **規範制定**：完成中文維護手冊 AGENTS.md，定義 Ingest 流程、Frontmatter 元資料格式、投影片規範與標籤系統。
- **目錄建立**：建立 raw/ 素材層、wiki/papers/、wiki/concepts/、以及 web/ 前端展示結構。

## [2026-11-04 19:15] update | 使用者建立 raw/my-focus/ 專屬關注目錄
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **使用者操作**：於原始素材層建立 raw/my-focus/，作為存放個人精選研究、私人筆記與核心關注資料之專屬唯讀目錄。
- **規則同步**：同步更新 AGENTS.md 與架構圖，確立其作為 my_focus: true 論文與筆記的原始真相來源。

## [2026-11-04 19:40] ingest | 光遺傳學（Optogenetics） | #神經科學 #腦科學
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **來源處理**：讀取不可變原始素材 raw/2026-optogenetics.md。
- **Wiki 產出**：成功編譯結構化論文卡片 wiki/papers/2026-optogenetics.md。
- **概念網絡**：建立跨領域概念頁 wiki/concepts/neural-circuits.md，完成概念雙向鏈結。
- **目錄同步**：完成 wiki/index.md 狀態更新。

## [2026-11-04 20:10] lint | 校準雙年份標註規範 (paper_year & award_year)
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **規範升級**：於 AGENTS.md 確立「雙年份標註規則」，嚴格區分 paper_year（實際發表時間）與 award_year（榮譽獲獎時間）。
- **條目校正**：更新 wiki/papers/2026-optogenetics.md Frontmatter（標註 2025 發表 ｜ 2026 諾獎）。
- **索引同步**：wiki/index.md 同步並列呈現雙年份。

## [2026-11-04 20:30] lint | 檔名規範校準（以實際發表年份 paper_year 為前綴）
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **檔案重命名**：將檔案正式校準為 raw/2025-optogenetics.md 與 wiki/papers/2025-optogenetics.md。
- **規則更新**：AGENTS.md 明確定義檔名一律以 paper_year 為前綴，維護學術真實性。
- **全域鏈結修復**：同步更新 wiki/concepts/neural-circuits.md 與 wiki/index.md 的內部雙向連結。

## [2026-11-04 21:00] update | 前端展示層升級：3:4 豎版知識圖卡輪播 ＋ 深入長文雙層架構
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **體驗升級**：將展示層全面重構為行動優先（Mobile-First）的雙層閱讀體驗。
- **上半部（30 秒吸收）**：3:4 豎版知識卡片輪播（CSS Scroll-Snap，維持 6 張黃金節奏：Hook、Dilemma、Secret、Evidence、Revolution、Kairos）。
- **下半部（深度學術推導）**：完整 Markdown 長文解析，強制支援 KaTeX 高精度 LaTeX 數學公式渲染（行內 $...$, 塊級 $$...$$）。
- **桌面響應式 Split-View**：電腦端自動呈現左圖（左右橫滑）右文（上下縱滑）獨立視窗。

## [2026-11-04 21:35] design | 導入 Deimos 與 Shopify Expo Mode 高級配色系統
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **來源爬取與提取**：深入提取 Evil Rabbit 之 Deimos Designer Encyclopedia 與 Shopify Editions Fall '26 (Expo Mode) 之色彩變數。
- **樣式建立**：建立 web/assets/css/theme.css，奠定 #0B0C0E 黑曜石底色、#161618 書本卡片表面、1px 髮絲邊框與跨學科發光色碼系統。
- **規範更新**：將設計來源與色碼完整收錄至 PROJECT_SPEC.md、AGENTS.md 與 README.md。

## [2026-11-06 20:48] config | 建立 .gitignore 徹底隔離 raw/ 原始目錄
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **使用者操作**：指示建立專案根目錄 .gitignore 並將 raw/ 目錄排除於 Git 追蹤之外。
- **快取清理**：執行 git rm --cached -r raw/，解除先前已追蹤檔案之快取，本機 PDF 檔案與素材完好無損，遠端倉庫維持極致輕量。
- **檔案優化**：使用者主動移除 raw/2025-optogenetics.md，以 raw/2025-optogenetics.pdf 原始論文作為單一真實來源。

## [2026-11-06 20:57] git | 解決 README.md 雲端與本機同步衝突
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **衝突調解**：手動排除 my-focus 目錄說明之 Rebase 衝突，保留無表情符號且最詳盡之說明版本。
- **歷史重置**：順利完成 git rebase --continue，恢復乾淨線性提交歷史。

## [2026-11-06 21:03] math | 確立 LaTeX 數學適配為最高技術標準並全面升級光遺傳學
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **規則確立**：於 PROJECT_SPEC.md 與 AGENTS.md 設立獨立專章，將「完美適配 LaTeX 數學/物理/生物符號」定為全庫最高優先級技術標準。
- **模型升級**：在 wiki/papers/2025-optogenetics.md 中補齊 ChR2 光敏通道光電流微分方程與 Hodgkin-Huxley 膜電位整合方程。
- **節奏補齊**：補入第 6 節「跨界思維與啟發（The Kairos）」與修正原始來源路徑。
- **提交推送**：通過 100% 零表情符號檢查，成功推送至 GitHub 遠端倉庫（Commit: cc6caf8）。

## [2026-11-06 21:30] rule | 確立 wiki/log.md 必須標明 AI 身分名稱與模型版本型號
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **新規確立**：於 AGENTS.md 與 PROJECT_SPEC.md 中正式寫入硬性要求：未來任何 AI 在寫入或追加 wiki/log.md 時，第一條必須完整載明執行的 AI 代理名稱（如 Antigravity by Google DeepMind）與底層 LLM 版本型號（如 Gemini 3.8 Flash）。
- **歷史回溯**：全面回溯並標準化既有歷史日誌條目，確保全庫日誌格式嚴格對齊統一。

## [2026-11-06 21:35] fix | 校正日誌模型型號為真實版本 Gemini 3.8 Flash
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **校正事項**：經使用者精準糾正，修正先前日誌條目中誤植之模型型號，全面校準為真實運行的 Gemini 3.8 Flash，維持知識庫審計紀錄之絕對真實性。
