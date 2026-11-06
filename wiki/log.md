# Epoch-Kairos 知識庫操作日誌 (Operation Log)

> 本日誌為嚴格按時間追加（Append-only）之紀錄，完整追蹤知識庫的每一次 Ingest（收錄）、Query（綜述）與 Lint（健康檢查）。

---

## [2026-11-04] init | Epoch-Kairos 知識庫與架構初始化
- **架構設計**：導入 Andrej Karpathy 之 **LLM Wiki 三層模式**（`raw/`、`wiki/`、`AGENTS.md`、`web/`）。
- **規範制定**：完成中文維護手冊 [`AGENTS.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/AGENTS.md)，定義 Ingest 流程、Frontmatter 元資料格式、6 頁 Web PPT 投影片規範與標籤系統。
- **目錄建立**：建立 `raw/` 素材層、`wiki/papers/`、`wiki/concepts/`、以及 `web/` 前端展示結構。

## [2026-11-04] update | 使用者建立 raw/my-focus/ 專屬關注目錄
- **使用者操作**：於原始素材層建立 `raw/my-focus/`，作為存放個人精選研究、私人筆記與核心關注資料之專屬唯讀目錄。
- **規則同步**：同步更新 `AGENTS.md` 與架構圖，確立其作為 `my_focus: true` 論文與筆記的原始真相來源。

## [2026-11-04] ingest | 光遺傳學（Optogenetics） | #神經科學 #腦科學
- **來源處理**：讀取不可變原始素材 [`raw/2026-optogenetics.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/raw/2026-optogenetics.md)。
- **Wiki 產出**：成功編譯結構化論文卡片 [`wiki/papers/2026-optogenetics.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/wiki/papers/2026-optogenetics.md)。
- **概念網絡**：建立跨領域概念頁 [`wiki/concepts/neural-circuits.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/wiki/concepts/neural-circuits.md)，完成概念雙向鏈結。
- **目錄同步**：完成 `wiki/index.md` 狀態更新。

## [2026-11-04] lint | 校準雙年份標註規範 (paper_year & award_year)
- **規範升級**：於 [`AGENTS.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/AGENTS.md) 確立「雙年份標註規則」，嚴格區分 `paper_year`（實際發表時間）與 `award_year`（榮譽獲獎時間）。
- **條目校正**：更新 [`wiki/papers/2026-optogenetics.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/wiki/papers/2026-optogenetics.md) Frontmatter（標註 2025 發表 ｜ 2026 諾獎）。
- **索引同步**：[`wiki/index.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/wiki/index.md) 同步並列呈現雙年份。

## [2026-11-04] lint | 檔名規範校準（以實際發表年份 paper_year 為前綴）
- **檔案重命名**：將檔案正式校準為 [`raw/2025-optogenetics.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/raw/2025-optogenetics.md) 與 [`wiki/papers/2025-optogenetics.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/wiki/papers/2025-optogenetics.md)。
- **規則更新**：[`AGENTS.md`](file:///C:/MyAdapter/Company/Epoch-Kairos/AGENTS.md) 明確定義：檔名一律以 `paper_year` 為前綴，維護學術真實性。
- **全域鏈結修復**：同步更新 `wiki/concepts/neural-circuits.md` 與 `wiki/index.md` 的內部雙向連結。

## [2026-11-04] update | 前端展示層升級：3:4 豎版小紅書風卡片輪播 ＋ 深入長文雙層架構
- **行動端體驗升級**：將展示層全面重構為「行動優先（Mobile-First）」的雙層閱讀體驗。
- **上半部（30 秒極速吸收）**：3:4 豎版知識卡片輪播（CSS Scroll-Snap，維持 6 張黃金節奏：Hook、Dilemma、Secret、Evidence、Revolution、Kairos）。
- **下半部（深度學術推導）**：完整 Markdown 長文解析，強制支援 KaTeX 高精度 LaTeX 數學公式渲染（行內 `$...$`, 塊級 `$$...$$`）。

## [2026-11-04] update | 前端響應式 Split-View 設計（電腦左圖右文 ＋ 手機上下疊加）
- **電腦桌面端**：左欄黏性固定 3:4 卡片（支援水平左右交互）；右欄長文獨立垂直上下滑動，對照閱讀體驗極佳。
- **手機行動端**：自動折疊為上下單欄流，上半部卡片橫滑、下半部長文縱滑。
