# Epoch-Kairos ｜ 人類群星閃耀時

> **"The Kairos of human thought and research horizons."**  
> 在漫長的客觀時間（Chronos）中，唯有那些改變人類文明軌跡的決定性時刻（Kairos），宛如夜空中驟然閃耀的群星。

本專案是一個**跨領域時代權威論文、諾貝爾獎導讀與個人研究關注知識庫**，基於 **Andrej Karpathy 的 LLM Wiki 架構** 打造，由多 AI 代理人協同維護，結合可追溯第一手來源的證據審查、KaTeX 公式排版與互動式網頁展示。全專案嚴格維持出版級學術風格，全站禁止任何表情符號。

> **完整規範請見 [`AGENTS.md`](./AGENTS.md)**：本 README 僅提供專案概覽；Frontmatter 欄位、標籤白名單、LaTeX 準則、證據表與待辦格式、日誌格式、Lint 檢查項與多 AI 版控協定之唯一權威定義皆在 `AGENTS.md`，美術方向紀錄見 [`DESIGN.md`](./DESIGN.md)。各文件與 `AGENTS.md` 若有出入，一律以 `AGENTS.md` 為準。

---

## 參考原型與設計來源

1. **Andrej Karpathy - LLM Wiki 架構**（[gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)）：三層資料架構——不可變原始資料 `raw/`、結構化編譯知識 `wiki/`、代理人運作規範 `AGENTS.md`。
2. **Evil Rabbit - Deimos Designer Encyclopedia**（[官方網站](https://deimos.evilrabbit.com/)、[設計收錄](https://recent.design/i/i50sj5g-deimos-designer-encyclopedia)）：雜誌編排級審美、黑曜石底色、極細半透明邊框、襯線大標題與整張一色的卡片質感。
3. **Shopify - Editions Fall '26 (Expo Mode)**（[官方網站](https://www.shopify.com/editions/fall2026)）：跑道時間線靈感與跨學科專屬色碼微光系統。

---

## 系統架構

```text
Epoch-Kairos/
├── AGENTS.md                  # 【Schema】專案總規範（AI 協作指南、格式標準與多 AI 版控協定）
├── DESIGN.md                  # 美術方向紀錄（已定、暫定、待決與否決之視覺決策）
├── .agents/skills/            # 專屬作業技能正本（收錄、查核、寫卡、PDF 解析、繁中翻譯、雙倉庫同步）
├── .claude/skills/            # 供 Claude Code 載入之轉介檔（指向 .agents/skills/ 正本）
├── raw/                       # 【Raw Sources】不可變原始素材層（獨立私有倉庫 Mine-RAW，本倉庫不追蹤）
│   └── my-focus/              # [個人專屬關注區] 六類來源資料夾、私人筆記與私有索引 my-index.md
├── wiki/                      # 【The Wiki】AI 維護之知識核心（Markdown）
│   ├── index.md               # 群星論文與概念頁公開總目錄（按時間線年份與領域組織）
│   ├── log.md                 # 操作日誌（Append-only，逐筆記載執行代理、模型版本與變更）
│   ├── issues.md              # 內容問題清單（查核發現與修正狀態追蹤）
│   ├── todo.md                # 待辦清單（交接事項、未完成任務與待確認工作）
│   ├── evidence/              # 證據表（每頁一檔，強主張、數值與公式逐項對應原文頁碼與表圖）
│   ├── cards/                 # 卡片文字檔（首頁封面斷行、導語、六張卡文字與 Card 3 SVG 示意圖）
│   ├── papers/                # 結構化論文知識頁（檔名以實際發表年份為前綴）
│   └── concepts/              # 跨學科概念頁（與論文頁雙向連結）
├── tools/                     # 建置腳本（不上站）
│   ├── build_home.py          # 自 wiki/ Frontmatter 與已提交卡片檔產生 web/index.html
│   ├── build_paper_prototype.py # 自 wiki/cards/ 與 wiki/papers/ 編譯 web/papers/<slug>/index.html
│   ├── home_template.html     # 首頁 HTML 範本
│   ├── paper_template.html    # 論文頁 HTML 範本（「論文頁 F」雙欄與手機版）
│   ├── wiki_redirects.py      # 舊路徑轉介檔辨識輔助
│   └── tests/                 # 建置與流程回歸測試
└── web/                       # 【Web Presentation】GitHub Pages 成果展示層
    ├── index.html             # 知識星圖首頁（群星知識星圖＋卡片牆；隱藏機關進入「我的星系」#my-constellation）
    ├── assets/                # CSS、JS（theme.css 為全站色碼唯一真實來源；starmap.css、starmap.js 為首頁樣式與互動）
    ├── papers/                # 每篇論文之「3:4 豎版知識圖卡 ＋ KaTeX 學術長文」雙欄網頁
    └── prototypes/            # 樣稿與手機原型（不上站）
```

首頁與論文頁皆由資料自動編譯，不手寫條目內容：

```bash
# 編譯指定論文頁（或省略 slug 全部重建），內含 check_cards 與結構自我檢查
python tools/build_paper_prototype.py <slug>

# 重建首頁 web/index.html（卡片牆僅收錄 Git 已提交之 wiki/cards/；未提交之新卡以 --card 帶入）
python tools/build_home.py [--card <slug>]

# 檢查現有 web/index.html 是否與 wiki/ 資料一致（不寫檔）
python tools/build_home.py --check
```

若修改 `web/assets/` 內的 CSS 或 JS，亦須重跑 `build_home.py` 以更新首頁引用的內容雜湊參數（`?v=`）。

### 原始層採雙倉庫分離（Dual-Repository Split）

`raw/` 已於本倉庫 `.gitignore` 全目錄排除，**不隨本倉庫公開**。自 2026-11-08 起，該層改由獨立私有倉庫 [`zhi816/Mine-RAW`](https://github.com/zhi816/Mine-RAW) 版控，在 `raw/` 目錄內自成一個 Git 工作區（並非 submodule，兩倉庫彼此完全獨立）。

| | Epoch-Kairos（本倉庫） | Mine-RAW |
|---|---|---|
| 可見性 | 公開 | 私有 |
| 內容 | `AGENTS.md`、`DESIGN.md`、`.agents/skills/`、`wiki/`、`tools/`、`web/` | `raw/` 之原始 PDF、繁中翻譯 PDF、個人筆記與 `my-focus/my-index.md` |
| 規範來源 | 本倉庫 [`AGENTS.md`](./AGENTS.md) | 同左；其倉庫內 `AGENTS.md` 僅為指回本倉庫之摘要 |

**給 AI 代理與協作者的重要提醒**：在本倉庫執行任何 Git 指令永遠不會觸及 `raw/`。若 `raw/` 內容有變動，須另行對 `raw/` 倉庫單獨提交與推送，兩邊無自動連動。專案內建 [`git-sync-guardian`](./.agents/skills/git-sync-guardian/SKILL.md) 工具鏈（`status.py`、`sync.py`、`safe_commit_push.py`）可同時檢查並同步雙倉庫，且嚴格只暫存自己修改的檔案。完整規範見 [`AGENTS.md`](./AGENTS.md) 第五、十章。

新機器完整還原兩層：

```bash
git clone https://github.com/zhi816/Epoch-Kairos.git
cd Epoch-Kairos
git clone https://github.com/zhi816/Mine-RAW.git raw
```

僅 clone 本倉庫者缺少 `raw/`，無法執行 [`AGENTS.md`](./AGENTS.md) 第六章第 3 節 Lint 之第 3 項（三層對齊檢查）與原文查核。

---

## 專屬作業技能與核心工作流

專案於 [`.agents/skills/`](./.agents/skills) 維護 6 套標準化作業技能，覆蓋從論文進件到上站發布的全生命週期：

| 技能 | 職責 |
|---|---|
| [`paper-pipeline`](./.agents/skills/paper-pipeline/SKILL.md) | 論文收錄總入口（S0 至 S10 檢查點流程，附 `pipeline_status.py` 進度追蹤與 `verify_star.js`） |
| [`wiki-content-audit`](./.agents/skills/wiki-content-audit/SKILL.md) | 證據表起草與兩階段（巨觀＋微觀）原文事實查核（附 `lint_wiki.py`、`crossref_check.py`） |
| [`paper-card-writer`](./.agents/skills/paper-card-writer/SKILL.md) | 撰寫 `wiki/cards/` 封面、六張卡與 Card 3 SVG 示意圖（附 `check_cards.py`、`verify_page.js`、`verify_wall.js`） |
| [`paper-pdf-parser`](./.agents/skills/paper-pdf-parser/SKILL.md) | 以 PyMuPDF（或本機 MinerU）抽取附頁碼草稿供查核主張出處 |
| [`academic-paper-translator`](./.agents/skills/academic-paper-translator/SKILL.md) | 學術論文繁體中文翻譯與高還原排版 PDF 重建（支援雙欄原版與手機單欄版） |
| [`git-sync-guardian`](./.agents/skills/git-sync-guardian/SKILL.md) | 雙倉庫預檢、日誌時間戳與自動合流、共用檔逐條暫存、原子提交與推送 |

### 四大核心工作流（見 [`AGENTS.md`](./AGENTS.md) 第六章）

1. **Ingest（收錄，S0–S10）**：由 `paper-pipeline` 統一編排。從雙倉庫同步領件、Crossref 與原文首頁核對書目、解析 PDF 全文、先建立 `wiki/evidence/` 證據表再起草論文頁、建立或更新 `wiki/concepts/` 雙向連結與索引（群星入 `wiki/index.md`、我的關注入 `raw/my-focus/my-index.md`）、兩階段核對並更新 `verification`、撰寫 `wiki/cards/` 卡片檔、編譯論文頁並重建首頁、完成桌面／手機瀏覽器驗證，最後追加 `wiki/log.md` 並原子提交推送。
2. **Query（查詢）**：AI 優先透過 `wiki/index.md`、`wiki/concepts/` 與 `wiki/evidence/` 進行跨領域綜合檢索與引文追溯；具長期價值之洞見可沉澱為新概念頁。
3. **Lint（健康檢查，共 11 項）**：涵蓋孤島頁面與概念雙向對應、觀點衝突與技術迭代、三層對齊一致性、零表情符號、LaTeX 公式與正體化學式合規、年份與作者真實性、標籤與個人關注欄位白名單、相對連結有效性、核實狀態與 `issues.md`／`evidence/` 一致性、`todo.md` 格式、以及卡片文字檔合規。
4. **Handoff（交接與多 AI 協同）**：接手一律依 `git log --oneline -10`、閱讀 `wiki/todo.md` 與 `wiki/issues.md`，並以 `log_tail.py` 擷取日誌近況（禁止整份讀取 `wiki/log.md`）；支援多代理平行 worktree 作業與 `safe_commit_push.py` 逐條暫存共用檔案（`log.md`、`issues.md`、`todo.md`），日誌寫入即完成該回合原子提交推送。

---

## 知識條目的關鍵規則

* **雙年份標註**：`paper_year`（實際發表年份，決定檔名）與 `award_year`（獲獎年份）分開記載，前台並列呈現，例如「2005 發表 ｜ 2026 諾貝爾生理學或醫學獎」（首頁簡稱「諾貝爾獎」）。
* **作者與得獎者分離**：`authors` 僅記該篇論文之實際作者，獎項得獎者另記於 `laureates`；獎項表彰多篇工作時，奠基論文列入 `key_papers`，並為多得主各自收錄代表性論文。
* **條目產出與核實雙狀態**：
  * `status` 三態：`planned`（僅立案）、`wiki`（已有 Wiki 頁）、`published`（已產出網頁）。
  * `verification` 四態：`unverified`（未查核）、`partial`（部分核對且無未結問題）、`issues`（`wiki/issues.md` 尚有 `open` 問題）、`verified`（強主張與公式已於 `wiki/evidence/<slug>.md` 逐項對應原文且無未結問題）。
* **兩層標籤與六大學科**：`domain` 單選，決定群星配色與幾何標記（`bio` 生醫冷翠綠、`ai` 電能青、`physics` 宇宙紫、`econ` 香檳金、`chem` 珊瑚橙、`human` 玫瑰粉）；`domain_tags` 多選，限用 `AGENTS.md` 第八章白名單。
* **「我的星系」個人關注體系（`my_focus: true`）**：
  * Frontmatter 另設 `focus_role`（六類主分類：`senior-thesis` 學長姐論文、`report` 報告題材、`taiwan-research` 國內研究、`international` 國際文獻、`llm-assisted` 大模型LLM、`daily-picks` 每日推介）、`focus_tags`（選填兼屬角色）、`focus_direction`（五大優化方向決定星圖環狀分團：`morphology`、`data-corpus`、`transfer-align`、`llm-rag`、`linguistics-eval`）與 `focus_languages`。
  * 前台與論文頁卡片統一採專屬主題色 `--color-focus`（目前暫定晴空藍 `#5AAEFF`）。
* **雙模式 3:4 六張卡架構**：
  * **群星論文**：經典六章——Card 1 時代銘文、Card 2 世紀瓶頸、Card 3 突破架構與原理、Card 4 決定性數據、Card 5 時代典範轉移、Card 6 跨界思維與啟發（原文無核心理論公式時，Card 3 改用無公式示意圖模式，不自編公式）。
  * **我的關注論文**：快速導讀新六章——01 一句話看懂、02 要解決的問題、03 方法流程、04 資料與實驗、05 結果、06 限制與可用性（長文末附「延伸想法」小節）。
* **LaTeX 為最高技術標準**：全站以 KaTeX 向量排版公式，化學元素與離子一律用 `\mathrm{}` 正體，長公式以 `aligned` 斷行並具行動端橫向防溢出，金額須轉義 `\$`。

---

## 常用檢查指令

```bash
# 檢查雙倉庫遠端狀態與同步
python .agents/skills/git-sync-guardian/scripts/status.py

# 查看全庫（或指定論文）S0-S10 收錄進度與未收錄原始檔
python .agents/skills/paper-pipeline/scripts/pipeline_status.py
python .agents/skills/paper-pipeline/scripts/pipeline_status.py --new

# 執行知識庫健康檢查、卡片檢查與工具測試
python .agents/skills/wiki-content-audit/scripts/lint_wiki.py
python .agents/skills/paper-card-writer/scripts/check_cards.py
python -m unittest discover -s tools/tests -p "test_*.py"
```

---

## 成果瀏覽

* **GitHub Repository**：[https://github.com/zhi816/Epoch-Kairos](https://github.com/zhi816/Epoch-Kairos)
* **GitHub Pages 成果展示**：[https://zhi816.github.io/Epoch-Kairos/](https://zhi816.github.io/Epoch-Kairos/)（由 `.github/workflows/pages.yml` 於 `web/` 變動推送至 `main` 時自動發布，`web/prototypes/` 不上站）
* **目前收錄進度**：群星公開目錄見 [`wiki/index.md`](./wiki/index.md)，待辦與查核問題見 [`wiki/todo.md`](./wiki/todo.md) 與 [`wiki/issues.md`](./wiki/issues.md)；全庫即時步驟狀態可執行 `pipeline_status.py`。
