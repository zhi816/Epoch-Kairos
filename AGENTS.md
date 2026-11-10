# AGENTS.md - Epoch-Kairos（人類群星閃耀時）維護手冊

> **專案核心精神**：
> 「在漫長的時間長河（Chronos）中，唯有那些改變人類文明軌跡的決定性時刻（Kairos），宛如夜空中驟然閃耀的群星。」
> 本專案以 Andrej Karpathy 的 **LLM Wiki** 模式為核心架構，建立一套能夠隨時間**持續累積、自我演進、跨領域交織**的時代里程碑論文與個人研究關注知識庫。
> **格式硬性規範**：全專案文件、日誌、卡片與代碼中，嚴格禁止使用任何表情符號（Emoji）。

---

## 一、參考原型與設計來源 (Design Inspirations & References)
本專案之資料架構與視覺風格明確參考並融合以下三個開創性設計：

1. **Andrej Karpathy - LLM Wiki 架構**：
   - 來源網址：`https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`
   - 核心精髓：三層資料架構（`raw/` 原始不可變來源、`wiki/` 結構化長青知識、`AGENTS.md` 代理人綱領）。
2. **Evil Rabbit - Deimos Designer Encyclopedia**：
   - 官方網站：`https://deimos.evilrabbit.com/`
   - 設計收錄：`https://recent.design/i/i50sj5g-deimos-designer-encyclopedia`
   - 核心精髓：雜誌編排級審美（Editorial Minimalism）、沉靜黑曜石底色、極細半透明邊框、精緻襯線大標題與深邃排版層次。
3. **Shopify - Editions Fall '26 (Expo Mode)**：
   - 官方網站：`https://www.shopify.com/editions/fall2026`
   - 核心精髓：未來感 3D 跑道時間線（Runway Timeline）、跨學科專屬色碼微光系統（Color-Coded Sections），滾動時具備空間光影過渡。

---

## 二、視覺設計與高階色彩系統 (Color Design Tokens)

> **唯一真實來源（Single Source of Truth）**：所有色碼之實際數值一律以 [`web/assets/css/theme.css`](./web/assets/css/theme.css) 之 CSS 變數為準。本章之「參考色值」欄僅供閱讀時快速辨識，若與 `theme.css` 不一致，一律以 `theme.css` 為準。修改配色時以 `theme.css` 為主，並同步更新本表參考色值。

> **美術方向紀錄**：首頁、星圖、卡片、索引與「我的星系」等視覺方向之已定、暫定、待決與否決事項，統一記於 [`DESIGN.md`](./DESIGN.md)。設計或實作 `web/` 前須先閱讀該檔，且不得重提其「否決紀錄」所列方案。

### 1. 基礎畫布與文字色彩（源自 Deimos）

| 用途 | CSS 變數 | 設計意圖 | 參考色值（以 `theme.css` 為準） |
|---|---|---|---|
| 背景底色 | `--bg-canvas` | 黑曜石冷灰暗黑底，深度低噪聲 | `#0B0C0E` |
| 卡片本體 | `--bg-surface` | 高階精裝書表面，物理浮起感 | `#161618` |
| 卡片懸浮層 | `--bg-surface-raised` | 懸停與彈出層 | `#202023` |
| 公式容器底色 | `--bg-surface-sunken` | 深邃下沉感，承載區塊公式 | `#101012` |
| 極細邊框 | `--border-hairline` | 1px 半透明髮絲線 | `rgba(255, 255, 255, 0.08)` |
| 強調邊框 | `--border-strong` | 區塊分隔與聚焦 | `rgba(255, 255, 255, 0.16)` |
| 懸停邊框 | `--border-hover` | 滑鼠懸停回饋 | `rgba(255, 255, 255, 0.28)` |
| 標題文字 | `--text-primary` | 柔和象牙白，高易讀性 | `#EDEDED` |
| 次要文字 | `--text-muted` | 內文輔助資訊 | `#8E8E93` |
| 極淡標籤 | `--text-subtle` | 後設資料與標籤 | `#55555A` |
| 反白文字 | `--text-inverted` | 置於亮色底之文字 | `#0B0C0E` |

### 2. 跨學科專屬色碼微光系統（源自 Shopify Editions）
各學科分配專屬色碼與微光（Glow），用於首頁知識星圖、卡片標籤與公式光暈。Frontmatter 之 `domain` 欄位即取下表之鍵值：

> **2026-11-09 起改用柔和「星光色」**（經使用者確認，見 [`DESIGN.md`](./DESIGN.md) 第七章）：`--color-*`、`--glow-*`、`--border-*` 取星光色；原霓虹色保留於 `theme.css` 之備用變數 `--neon-color-*`、`--neon-glow-*`、`--neon-border-*`，切回時將前者改指向後者即可。`human` 之星光色與十字形為暫定。

| `domain` 鍵值 | 學科範疇 | 色彩意象 | CSS 變數 | 參考色值：星光色，現行（以 `theme.css` 為準） | 霓虹色（備用 `--neon-*`） |
|---|---|---|---|---|---|
| `bio` | 生醫與生命科技 | 冷翠綠 | `--color-bio` / `--glow-bio` / `--border-bio` | `#9BDCB1` / `rgba(155, 220, 177, 0.16)` / `rgba(155, 220, 177, 0.35)` | `#00E599` / `rgba(0, 229, 153, 0.16)` / `rgba(0, 229, 153, 0.35)` |
| `ai` | 人工智慧、計算與數學 | 電能青 | `--color-ai` / `--glow-ai` / `--border-ai` | `#8FD5FD` / `rgba(143, 213, 253, 0.16)` / `rgba(143, 213, 253, 0.35)` | `#00F0FF` / `rgba(0, 240, 255, 0.16)` / `rgba(0, 240, 255, 0.35)` |
| `physics` | 物理、天文與地球科學 | 宇宙紫 | `--color-physics` / `--glow-physics` / `--border-physics` | `#D3BEFD` / `rgba(211, 190, 253, 0.20)` / `rgba(211, 190, 253, 0.40)` | `#8B5CF6` / `rgba(139, 92, 246, 0.20)` / `rgba(139, 92, 246, 0.40)` |
| `econ` | 宏觀經濟與治理 | 香檳金 | `--color-econ` / `--glow-econ` / `--border-econ` | `#E6C686` / `rgba(230, 198, 134, 0.16)` / `rgba(230, 198, 134, 0.35)` | `#FFB800` / `rgba(255, 184, 0, 0.16)` / `rgba(255, 184, 0, 0.35)` |
| `chem` | 化學、材料與能源 | 珊瑚橙 | `--color-chem` / `--glow-chem` / `--border-chem` | `#FFB6A3` / `rgba(255, 182, 163, 0.16)` / `rgba(255, 182, 163, 0.35)` | `#FF5722` / `rgba(255, 87, 34, 0.16)` / `rgba(255, 87, 34, 0.35)` |
| `human` | 語言、心理與社會 | 玫瑰粉 | `--color-human` / `--glow-human` / `--border-human` | `#F2B3D6` / `rgba(242, 179, 214, 0.16)` / `rgba(242, 179, 214, 0.35)` | `#FF4FD8` / `rgba(255, 79, 216, 0.16)` / `rgba(255, 79, 216, 0.35)` |

> **學科邊界**：`ai` 含純數學與計算理論；`physics` 含地球科學與氣候物理（生態與生物多樣性歸 `bio`、氣候政策歸 `econ`、能源技術歸 `chem`）；`human` 收語言學、心理與行為、社會與文化研究（研究大腦機制之神經科學仍歸 `bio`，經濟學、政治與治理仍歸 `econ`）。條目同時涉及多個學科時，`domain` 取其主要研究方法與貢獻所在，其餘以 `domain_tags` 跨色系標註。

---

## 三、LaTeX 數學與物理公式極致適配準則 (LaTeX Mathematical Excellence Standard)

> **最高優先級核心技術指標**：本知識庫以「完美適配 LaTeX 數學/物理/工程符號」為絕對重點。全站一律採用標準 KaTeX 向量排版，嚴禁使用低解析度圖片替代公式。

1. **行內公式 (Inline Math)**：
   - 採用單錢字號 `$...$` 封裝（例如：能量動量關係 `$E^2 = p^2 c^2 + m^2 c^4$`）。
   - 必須確保垂直對齊正文文字基線，避免文字跳動。
   - **化學元素與離子一律使用正體**：須寫作 `$\mathrm{Na}^+$`、`$\mathrm{Ca}^{2+}$`，嚴禁寫作 `$Na^+$`（後者會被 KaTeX 排為斜體變數 $N$ 乘以 $a$，為典型錯誤）。
   - **金額須轉義**：正文出現貨幣金額時一律寫作 `\$` 或改用「美元」字樣，避免與行內公式之錢字號衝突導致全段解析錯亂。
2. **區塊公式 (Display Block Math)**：
   - 採用雙錢字號 `$$...$$` 獨立成段展示（例如：膜電位 Hodgkin-Huxley 微分方程、Transformer 自注意力權重矩陣）。
   - 水平垂直居中展示，字型清晰平滑。
3. **3:4 豎版圖卡與行動端防溢出 (Responsive Math Container)**：
   - 前端樣式強制對公式容器設定 `overflow-x: auto; -webkit-overflow-scrolling: touch;`，在手機窄螢幕與 3:4 豎版圖卡中提供平滑水平捲動，絕對不破版、不截斷。
   - 長公式強制使用 `\begin{aligned} ... \end{aligned}` 進行等號對齊與斷行。
4. **視覺微光整合 (Editorial Math Aesthetics)**：
   - 3:4 知識圖卡內之區塊公式容器採用 `--bg-surface-sunken`（參考色值 `#101012`，見第二章第 1 節）深邃黑曜石背景，並施加對應學科專屬微光或細框（如物理紫、生醫綠），營造高階學術期刊特寫感。
   - 論文頁右側長文之區塊公式不加容器外觀（無底色、邊框與微光），直接置中排版，以免打斷閱讀；第 3 條之水平捲動防溢出仍適用（2026-11-09 使用者確認，見 [`DESIGN.md`](./DESIGN.md) 第五章第 3 節）。

---

## 四、系統架構（Three Layers + Presentation）

本專案由嚴格的三層結構與一個前端展示層組成：

```text
Epoch-Kairos/
├── AGENTS.md                  # 【第三層：Schema】本規範文件，指導 AI 如何維護與擴充知識庫
├── README.md                  # 專案介紹與 GitHub Pages 瀏覽入口說明
├── DESIGN.md                  # 美術方向紀錄（已定、待決與否決之視覺決策）
├── .agents/skills/            # 專屬 Skill 正本（見第六章開頭之 Skill 一覽）
├── .claude/skills/            # 供 Claude Code 載入之轉介檔，內容指向 .agents/skills/ 正本
├── tools/                     # 建置腳本（不隨 GitHub Pages 公開）
│   ├── build_home.py          # 自 wiki/ Frontmatter 與已提交之卡片檔產生 web/index.html（知識星圖與卡片牆首頁）
│   ├── home_template.html     # 首頁 HTML 範本（資料由 build_home.py 內嵌）
│   ├── build_paper_prototype.py # 自 wiki/cards/ 與 wiki/papers/ 產生論文頁參考原型 web/prototypes/paper-v1/<slug>.html，附自我檢查
│   └── paper_template.html    # 論文頁 HTML 範本（樣稿「論文頁 F」）
│
├── raw/                       # 【第一層：Raw Sources】原始資料層（不可變，Immutable）
│   ├── my-focus/              # 【使用者專屬關注區】存放個人精選研究、私人筆記與核心關注資料
│   └── (存放論文原始摘要、筆記草稿、新聞、外部文獻剪藏)
│
├── wiki/                      # 【第二層：The Wiki】知識庫核心層（由 AI 讀寫與維護）
│   ├── index.md               # 內容目錄索引（Content Catalog，按年份與領域組織）
│   ├── log.md                 # 時間流水帳日誌（Append-only，記錄所有操作）
│   ├── issues.md              # 內容問題清單（查核發現之待修正事項與處理狀態，見第七章第 4 節）
│   ├── todo.md                # 待辦清單（交接事項、未完成任務、待使用者確認之工作，見第七章第 5 節）
│   ├── papers/                # 結構化論文知識頁（Markdown）
│   ├── concepts/              # 跨領域核心概念與實體頁（Markdown）
│   ├── evidence/              # 證據表（每頁一檔，記錄主張與第一手來源之對應，見第七章第 4 節）
│   └── cards/                 # 卡片文字檔（每篇一檔：封面斷行、導語、Card 2–6 與 Card 3 示意圖，見 paper-card-writer）
│
└── web/                       # 【展示層：Web Presentation】供 GitHub Pages 部署之成果
    ├── index.html             # 知識星圖首頁（由 tools/build_home.py 產生，勿手改；含隱藏機關進入「我的星系」#my-constellation）
    ├── assets/                # 前端靜態資源（CSS、JS、字體）
    │   ├── css/
    │   │   ├── theme.css      # 配色體系與全域變數（色碼唯一真實來源）
    │   │   ├── starmap.css    # 首頁樣式：星空、左欄懸星索引、知識星圖、群星檔案卡片牆與手機版
    │   │   └── cards.css      # 3:4 知識圖卡與學術長文雙欄樣式（尚未建立）
    │   └── js/
    │       ├── starmap.js     # 首頁互動：星圖與卡片牆篩選、說明框、我的星系與星空背景
    │       └── cards.js       # 3:4 卡片左右切換與 KaTeX 連動引擎（尚未建立）
    ├── prototypes/            # 樣稿與手機原型（非正式頁面）
    └── papers/                # 每篇論文之專屬雙欄互動頁（HTML 格式）
```

---

## 五、三層職責與權限劃分

1. **第一層：Raw Sources (`raw/`)**
   * **性質**：專案的「唯一真實來源（Single Source of Truth）」，**嚴禁 AI 擅自覆寫或刪除**。
   * **來源**：由使用者親自放入的論文文字、筆記草稿，以及專屬個人研究資料夾 `raw/my-focus/`。
   * **AI 權限**：**唯讀（Read-Only）**。嚴禁覆寫、刪除或重新命名其中任何檔案；若發現 `raw/` 檔名年份有誤，一律僅在 `wiki/` 層校正並於日誌提出建議，實際更名須由使用者親自執行。
   * **Git 追蹤狀態（雙倉庫架構）**：`raw/` 已於主倉庫之 `.gitignore` 全目錄排除，故原始素材不隨主倉庫公開。自 2026-11-08 起，`raw/` 改由獨立私有倉庫 [`zhi816/Mine-RAW`](https://github.com/zhi816/Mine-RAW) 版控，在該目錄內自成一個 Git 工作區（並非 submodule，兩倉庫彼此完全獨立）。
   * **雙倉庫操作準則**：在主倉庫執行任何 Git 指令永遠不會觸及 `raw/`。若 `raw/` 內容有變動（使用者放入新文獻，或 AI 經明確指示下載），須另行 `cd raw` 後單獨提交與推送。兩邊無自動連動，完成主倉庫作業後須主動確認 `raw/` 是否也需提交。
   * **殘留代價**：`raw/` 雖已取得版控與離機備份，但因不在主倉庫內，僅 clone 主倉庫的機器仍無法執行 Lint 第 3 條之三層對齊檢查，須同時將 `Mine-RAW` clone 至 `raw/` 才具備完整檢查能力。

2. **第二層：The Wiki (`wiki/`)**
   * **性質**：知識的「編譯結果與累積實體（Compounding Artifacts）」。
   * **特點**：每一篇新來源的加入，不僅是新增一頁，更會自動更新關聯的概念、修正舊論述、建立雙向交叉引用（Cross-References）。
   * **AI 權限**：**完全讀寫與維護（Read & Write）**。

3. **第三層：The Schema (`AGENTS.md`)**
   * **性質**：定義 AI 的作業規範、格式標準與操作工作流（Workflows）。
   * **更新機制**：由使用者與 AI 共同隨需求演進與調整。

4. **展示層：Web Presentation (`web/`)**
   * **性質**：將 `wiki/` 的知識編譯為可在 GitHub Pages 上流暢瀏覽的知識星圖首頁與 3:4 豎版知識圖卡＋深度學術長文。
   * **首頁由資料產生**：`web/index.html` 一律由 `python tools/build_home.py` 讀取 `wiki/papers/`、`wiki/concepts/` 之 Frontmatter 與 `wiki/cards/` 中**已提交**之卡片檔（卡片牆）產生，頁面不手寫任何論文資料；自己尚未提交之卡片檔以 `--card <slug>` 帶入（`paper-card-writer` 之 `references/card-wall.md`）；版面改 `tools/home_template.html`，樣式與互動改 `web/assets/css/starmap.css`、`web/assets/js/starmap.js`，不得直接修改 `web/index.html`。`python tools/build_home.py --check` 可確認現有首頁與資料一致。美術方向見 [`DESIGN.md`](./DESIGN.md) 第二至四章。

---

## 六、AI 核心作業流程（Core Operations）

AI 在協作時，必須嚴格遵循以下四大標準作業程序（SOP）：

> **專屬 Skill 一覽**：正本一律置於 `.agents/skills/<名稱>/SKILL.md`，各 AI 於對應工作開始前須先完整讀取。Claude Code 只會自動載入 `.claude/skills/`，故另於該處放置同名轉介檔，內容僅指向正本；修改時只改正本，轉介檔不得另寫規則。
>
> | Skill | 何時使用 |
> |---|---|
> | [`paper-pipeline`](./.agents/skills/paper-pipeline/SKILL.md) | **收錄論文之總入口**：`raw/` 出現新原始檔、使用者要求收錄或上架、或要把某篇補到完成時，先讀此 Skill。依 S0 至 S10 規定每一步照哪份 Skill 做、產出哪些檔案、以哪個指令證明完成（從收件、證據表、論文頁、概念頁與索引、核對、卡片、論文頁網頁，到首頁星圖或我的星系與卡片牆、提交）；附 `pipeline_status.py`（全庫與單篇進度、待收錄原始檔）與 `verify_star.js`（瀏覽器確認星圖或我的星系已上架） |
> | [`wiki-content-audit`](./.agents/skills/wiki-content-audit/SKILL.md) | Ingest 起草前（寫作模式）、Lint 第 2 條與任何事實查核（查核模式）；附 `lint_wiki.py` 與 `crossref_check.py` 兩支檢查腳本 |
> | [`academic-paper-translator`](./.agents/skills/academic-paper-translator/SKILL.md) | 將論文譯為繁體中文或重建 PDF 時 |
> | [`paper-pdf-parser`](./.agents/skills/paper-pdf-parser/SKILL.md) | Ingest 第 1 步與查核時，將 `raw/` 論文 PDF 抽成附頁碼標記之文字，以搜尋主張出處；預設用 PyMuPDF，MinerU 僅用於純圖片、亂碼 PDF 或抄寫長公式；輸出一律只當草稿，須回原 PDF 核對，且只可在本機解析 |
> | [`git-sync-guardian`](./.agents/skills/git-sync-guardian/SKILL.md) | 任何 Git 同步、提交與推送（見第十章） |
> | [`paper-card-writer`](./.agents/skills/paper-card-writer/SKILL.md) | Ingest 第 4 步、回填或修訂卡片時：撰寫 `wiki/cards/<slug>.md`（首頁封面卡與論文頁 Card 1–6 之文字、Card 3 示意圖），並建置論文頁原型、放上首頁卡片牆且兩者皆驗證；`references/` 須逐份讀完，附 `check_cards.py` 檢查腳本、`venue_short_lookup.py` 期刊簡稱查詢腳本與 `verify_page.js`、`verify_wall.js` 瀏覽器驗證腳本 |

### 1. Ingest（收錄新來源）
當使用者在 `raw/` 放入新文件或指令收錄一篇論文時，AI 必須依 [`paper-pipeline`](./.agents/skills/paper-pipeline/SKILL.md) 之 S0 至 S10 逐步執行，每一步以其完成條件之指令確認後才進下一步；`python .agents/skills/paper-pipeline/scripts/pipeline_status.py <slug>` 九步皆 OK 才算收錄完成。以下 5 個步驟為該流程之摘要：
1. **讀取來源**：分析原始文本，提取核心命題、年代、期刊/榮譽、以及作者團隊。
   * **事實核驗為前置強制步驟**：凡有 DOI 者，一律先以 Crossref API（`https://api.crossref.org/works/<DOI>`）核對發表年份、作者名單、期刊名稱與卷期頁碼，嚴禁僅憑記憶或原始檔名推定年份。
   * **作者與得獎者必須分離**：`authors` 僅記載該篇論文之實際作者；獎項得獎者另記於 `laureates`，嚴禁混寫（諾貝爾獎常表彰一系列工作，得獎者未必為某單篇之作者）。
   * **證據歸屬必須分離**：撰寫決定性數據時，須嚴格區分「本篇論文之實驗結果」與「後續他人延伸成果」，後者必須逐筆標註原始出處與年份。
   * **起草前先建證據表**：依 `wiki-content-audit` 寫作模式，將要寫的強主張（數值、公式、「首次／證明／導致」等斷言、後續成果歸屬）逐條對應至第一手來源之頁碼、表或圖，存為 `wiki/evidence/<slug>.md`（格式見第七章第 4 節）。以原文為準，不得以 `raw/` 中之中文譯本作為證據。
   * **書目以腳本核對**：Crossref 核驗可執行 `python .agents/skills/wiki-content-audit/scripts/crossref_check.py <slug>`。
2. **撰寫論文頁**：檔案命名一律以論文實際發表年份（`paper_year`）為前綴：`wiki/papers/YYYY-<slug>.md`（例如 2005 年發表、2026 年獲獎之光遺傳學，檔名為 `2005-optogenetics.md`）。若獲獎年份不同，則在 Frontmatter 中以 `award_year` 與 `honor` 完整標註，並由 `timeline_year` 決定其在前台時間線之位置。
3. **萃取/關聯概念**：檢查是否觸及跨領域概念（如同時涉及 AI 與結構生物學），同步更新或建立 `wiki/concepts/<concept>.md`（Frontmatter 依第七章第 2 節），並將本篇檔名登記於該概念頁之 `papers` 欄位。
4. **編譯網頁成果**：
   * **先寫卡片文字**：依 `paper-card-writer` 撰寫 `wiki/cards/<slug>.md`（封面斷行、導語、Card 2–6 與 Card 3 示意圖），執行 `python .agents/skills/paper-card-writer/scripts/check_cards.py <slug>`，ERROR 須為 0。卡片上的數字只能取自證據表，公式只能取自論文頁。
   * **建置論文頁原型並驗證**：執行 `python tools/build_paper_prototype.py <slug>`，自我檢查 ERROR 須為 0；有瀏覽器工具者再以 `verify_page.js` 驗證桌面與手機版面（`paper-card-writer` 第五節第 7 步）。正式論文頁產出前（`wiki/todo.md` TD-002），以此原型代替。
   * 在 `web/papers/YYYY-<slug>/index.html` 產生對應之雙欄互動頁（左側 3:4 知識圖卡，右側 KaTeX 長文）。
   * 執行 `python tools/build_home.py --card <slug>` 重建首頁 `web/index.html`，新論文即依 Frontmatter（`domain`、`domain_tags`、`concepts`、`card_line`、雙年份與 `my_focus` 等欄位）出現在知識星圖或我的星系，其封面卡出現在卡片牆；卡片牆只收已提交之卡片檔，`--card` 帶入自己這篇尚未提交之卡片檔。有瀏覽器工具者以 `verify_wall.js` 驗證（`paper-card-writer` 第五節第 7-2 步）。不得手改 `web/index.html`。
5. **更新索引與日誌**：
   * 在 `wiki/index.md` 登記該論文之摘要與連結。
   * 寫日誌前執行 `python .agents/skills/wiki-content-audit/scripts/lint_wiki.py`，錯誤（ERROR）須全數排除後才可提交。
   * 在 `wiki/log.md` 結尾追加一筆符合規範之紀錄，**第一條與第二條必須明確寫清 AI 身分名稱與底層模型版本型號**：
     ```markdown
     ## [YYYY-MM-DD HH:MM] <動作> | <標題> | <領域標籤>
     - **執行代理**：<AI 名稱與所屬機構>（例如：Claude Code by Anthropic）
     - **模型版本**：<底層 LLM 型號與版本>（例如：Claude Opus 5）
     - **具體變更**：<簡述操作要點與產出檔案>
     ```
   * **標題第三段（`<領域標籤>`）**：操作對象為單一論文或概念頁時，填其 `domain_tags`（須取自第八章白名單，以空格分隔）；涉及多個條目或全庫之操作（如 `init`、`config`、`rule`、`audit`、`lint`、`git`）一律填 `全域`，不得改用 `多領域` 等其他寫法。本規則於 2026-11-08 合併入 main 後生效；此前之條目（含於其他分支並行寫入者）缺漏第三段、使用 `多領域` 或白名單外標籤者維持原樣，不回溯修改，以維持日誌 append-only 之完整性。
   * **動作類型（`<動作>`）一律取自下列詞彙**，不得自創：
     `init`（初始化）、`ingest`（收錄新來源）、`query`（綜述檢索）、`lint`（健康檢查）、`audit`（規範審查）、`fix`（錯誤修正）、`rule`（規範變更）、`design`（視覺設計）、`math`（公式修訂）、`update`（內容更新）、`config`（組態變更）、`git`（版本控管）。
   * **標題時間一律以指令取得，嚴禁憑估計或記憶填寫**：寫入標題前先執行 `python .agents/skills/git-sync-guardian/scripts/log_time.py`，將輸出之臺北時間（UTC+8，格式 `YYYY-MM-DD HH:MM`）原樣填入 `## [...]`。此腳本不受本機時區影響，Windows、macOS 與雲端環境皆適用。`stage_log.py` 會擋下晚於現在 5 分鐘以上、或早於現在 60 分鐘以上之自己的新條目（後者僅於推送失敗後重試等情形，可以 `--allow-stale-log` 放行）。背景：2026-11-09 曾有代理憑估計把 09:26 寫成 09:42，只能另追加更正條目。
   * **日誌連結一律使用相對路徑**，嚴禁寫入 `file:///C:/...` 等本機絕對路徑，以確保在 GitHub 與他台機器上皆不失效。
   * **寫入日誌即提交**：日誌條目代表一項工作已完成。追加自己的條目後，須在同一回合內依第十章以 `safe_commit_push.sh` 提交並推送該條目與本項工作修改的檔案，無須等待使用者另行指示（使用者明確要求暫緩時除外）。工作尚未完成、或使用者要求先不提交時，先不寫日誌；需記下進度或交接者，登記於 `wiki/todo.md`（見本章第 4 節）。寫入一律追加於檔尾，不得讀取後整檔覆寫，亦不得改動他人條目。

### 2. Query（知識綜合檢索）
當使用者針對知識庫提問時：
1. AI 優先閱讀 `wiki/index.md` 與相關的 `wiki/concepts/`，而非盲目搜尋。
2. 串聯多篇跨學科論文，產出具有明確引用來源（Citations）的深度綜合解答。
3. 若提問產生了具備長期價值的洞見或對比分析，AI 應主動詢問是否將其存入 `wiki/concepts/` 或歸檔為新的知識卡片。

### 3. Lint（知識庫健康檢查）
定期或於使用者要求時執行：
1. **檢查孤島頁面**：標記沒有任何反向連結（Inbound Links）的條目，並比對論文頁 `concepts` 與概念頁 `papers` 兩欄位是否雙向對應。
2. **檢查觀點衝突與技術迭代**：標記被後續新突破推翻或修正的舊論述。
3. **檢查索引一致性**：確保 `raw/`、`wiki/papers/` 與 `web/` 三者的條目與 `status` 標記嚴格對齊（`status: published` 者必須存在對應之 `web/papers/` 目錄）。
4. **檢查符號合規性**：確保全文無任何表情符號（Emoji）。
5. **檢查 LaTeX 公式完整度**：確保公式排版合規，無截斷或解析錯誤；逐項確認化學離子使用 `\mathrm{}` 正體、長公式使用 `aligned` 斷行、公式內不含中文字元、金額已轉義。
6. **檢查年份與作者真實性**：抽查 Frontmatter 之 `paper_year` 與 `authors` 是否與 Crossref 元資料一致，並確認 `authors` 未混入 `laureates`。
7. **檢查標籤合規性**：確認 `domain` 為六大色系之一、`domain_tags` 全數落在第八章白名單內；`my_focus: true` 者須具備 `focus_role` 與 `focus_languages`，且 `focus_role` 取自第七章第 1 節之五個鍵值。
8. **檢查連結有效性**：確認所有相對路徑連結指向實際存在之檔案，且全庫無 `file:///` 本機絕對路徑與殘留之 `[[...]]` 語法。
9. **檢查核實狀態一致性**：論文頁與概念頁之 `verification` 須與 `wiki/issues.md` 及 `wiki/evidence/` 一致（規則見第七章第 4 節）。
10. **檢查待辦清單格式**：`wiki/todo.md` 之標題、狀態、範圍與必填欄位合規，且編號不重複（規則見第七章第 5 節）。
11. **檢查卡片文字檔**：`wiki/cards/` 各檔之欄位、字數、封面斷行、禁用詞、公式出處、示意圖規格、Card 4 數字與證據表、Card 5 出處，均符合 `paper-card-writer`。

> **工具分工**：第 1、3、4、5、7、8、9、10 條之可機械判斷部分由 `python .agents/skills/wiki-content-audit/scripts/lint_wiki.py` 執行（公式、化學式與長公式為啟發式檢查，警告須人工判斷）；第 6 條由 `crossref_check.py` 執行（需網路）；第 11 條由 `python .agents/skills/paper-card-writer/scripts/check_cards.py` 執行（`--missing` 另列出尚無卡片檔之論文）；第 2 條與內容事實查核依 `wiki-content-audit` 查核模式人工進行，發現之問題一律登記於 `wiki/issues.md`，不得只寫在日誌。每篇論文從原始檔到上架首頁之各步驟是否完成，以 `python .agents/skills/paper-pipeline/scripts/pipeline_status.py` 檢查（`--new` 列出 `raw/` 中尚未收錄之原始檔）。

### 4. Handoff（接手與交接）
多個 AI 輪流接手同一專案。交接脈絡一律從下列來源取得，不從日誌整份讀取：
1. **接手順序**：
   1. `git log --oneline -10`：最近完成的工作。每筆日誌條目皆對應一個已推送之提交（第十章第 6 條），提交清單即日誌之精簡目錄。
   2. 整份閱讀 `wiki/todo.md`：尚未完成之工作與等待使用者確認之事項。本檔完成即刪，篇幅維持精簡，可整份讀取。
   3. 視任務需要，閱讀 `wiki/issues.md` 之 `open` 條目與 `DESIGN.md` 第八章待決事項。
   4. 仍需日誌細節時，執行 `python .agents/skills/git-sync-guardian/scripts/log_tail.py`：預設輸出最後 3 筆，`-n` 調整筆數，`--grep <關鍵字>` 查特定事項。
2. **日誌只寫不讀**：不得整份讀取 `wiki/log.md`。日誌為歷史紀錄，其中已被取代之規則與決策不得視為現行指示；現行規範一律以 `AGENTS.md`、`DESIGN.md` 為準。查特定事項以 `log_tail.py --grep` 或搜尋工具取得相關條目。
3. **交接寫入待辦，不寫入日誌**：工作做到一半、需要他人接手，或須等使用者確認才能動工時，登記於 `wiki/todo.md`（格式見第七章第 5 節），不得以日誌條目充當交接清單。完成時刪除該條目，並於當次日誌條目寫明編號（例如「完成 TD-003」）。
4. **讀檔編碼**：全庫文字檔一律為 UTF-8（無 BOM）。Windows PowerShell 5.1 之 `Get-Content` 預設以系統碼頁讀檔，須加 `-Encoding UTF8`，否則中文顯示為亂碼；以行數截尾（`tail -n`、`Get-Content -Tail`）亦會切在條目中間，讀日誌一律改用 `log_tail.py`。

> 背景：2026-11-09 日誌已達 1,059 行、124 筆，且曾以日誌條目充當交接清單（[2026-11-08 22:06] 一筆列出待確認事項與工作順序），接手者須讀入大量歷史才能找到待辦，已被取代之舊決策亦可能被誤當現行指示。

---

## 七、內容與格式規範

### 1. Wiki 論文頁標準 Frontmatter 規範 (`wiki/papers/`)
每篇 Markdown 檔案頭部必須包含 YAML 元資料。針對諾貝爾獎等重大獎項與論文發表存在時間差之情況，一律採取**「雙年份標註規則（Dual-Year Rule）」**，且嚴禁包含任何 Emoji：

```yaml
---
title: "論文完整英文標題"
title_zh: "中文通俗譯名"
paper_year: 2005              # 原始論文發表年份（須經 Crossref 核驗之真實學術發表時間）
award_year: 2026              # 榮譽表彰或獲獎年份（如諾貝爾獎頒發年，無則填同 paper_year）
timeline_year: 2026           # 時間線歸檔節點（預設依重大影響/獲獎年 award_year 排序）
authors: "該篇論文之實際作者名單（依期刊署名順序）"
laureates: "獎項得獎者名單（若與作者不同；無獎項則省略此欄）"
venue: "Nature Neuroscience, 8(9), 1263-1268"   # 僅記期刊與卷期，不混入獎項
venue_short: "PNAS"           # 選填：期刊或會議簡稱，供論文頁資訊欄與首頁顯示；僅限通用縮寫或 Crossref short-container-title（規則見下方說明）
honor: "2026 諾貝爾生理學或醫學獎（表彰事由）"      # 不加顯示層前綴，呈現樣式由前端決定
domain: "bio"                 # 單選，對應 theme.css 六大色系：bio / ai / physics / econ / chem / human
domain_tags: ["#神經科學", "#生物科技"]            # 多選，須取自第八章標籤白名單
concepts: ["neural-circuits"] # 關聯之 wiki/concepts/ 頁，供 Lint 檢查反向連結
status: "wiki"                # planned（僅立案）/ wiki（已有 Wiki 頁）/ published（已產出網頁）
verification: "unverified"    # 內容核實狀態：unverified / partial / issues / verified（見第七章第 4 節）
hook: "一句話摘要本篇做了什麼與為何重要"   # 網站不顯示，只作為撰寫卡片檔「導語」之素材；仍不得擴大研究結論
card_line: "用一道藍光，開關大腦裡特定的神經元"     # 首頁卡片星窗內之短句，20 字以內（規則見下方說明）
key_papers:                   # 獎項表彰多篇工作時，逐筆列出奠基論文與 DOI
  - "Nagel et al. (2003) ... PNAS 100:13940-13945. https://doi.org/10.1073/pnas.1936192100"
my_focus: false               # 若為使用者特別關注則標記為 true
doi_url: "https://doi.org/10.1038/nn1525"
---
```

> **雙年份呈現原則**：
> 在前台首頁（知識星圖之說明框）與每篇論文的封面卡片上，必須同時清晰並列標記 **「2005 發表 ｜ 2026 諾貝爾獎」**（以光遺傳學為例），兼顧科學史發表真實性與當代獲獎影響力。首頁一律簡稱「諾貝爾獎」；論文頁（Card 1 底部與長文頂部）寫 `honor` 括號前之獎項全名，如「2005 發表 ｜ 2026 諾貝爾生理學或醫學獎」（2026-11-09 使用者確認，依樣稿「論文頁 F」）。

> **期刊簡稱（`venue_short`，選填）**：
> 論文頁資訊欄與首頁顯示期刊或會議簡稱；未填時由 `venue` 自動縮短（取括號內縮寫或第一個逗號前之全名）。自動結果在論文頁資訊欄超過兩行（建置自我檢查會提示）或首頁卡片牆雙年份被截斷時（`verify_wall.js` 會提示），依序填期刊或學會自己通用的縮寫（`PNAS`、`AER`、`PRL`）或 Crossref 之 `short-container-title`；兩者皆無則不填；學會縮寫查不到第一手出處者，須經使用者確認才可填。不得自創縮寫或以中文意譯。修改後須重建首頁（`python tools/build_home.py`）。細則見 `paper-card-writer` 之 `references/paper-page.md` 第三節。

> **單篇頁容納多篇工作之原則**：
> 諾貝爾獎常表彰橫跨數年的一系列論文。此時以最具代表性之單篇為主軸建立頁面，其餘奠基論文一律列入 `key_papers`，並於頁首加註本頁範圍說明，嚴禁將多篇成果混記為單篇之貢獻。

> **卡片一句話（`card_line`，論文頁必填）**：
> 首頁卡片牆採 F 版型「星窗＋一句話」（見 [`DESIGN.md`](./DESIGN.md) 第二章第 3 節），星窗內以學科色顯示 `card_line`，分行位置寫在卡片檔之「封面斷行」。論文頁 Card 1 用卡片檔中 60 字以內之「導語」（`hook` 多半過長且多術語，2026-11-09 起）；論文頁長文開頭用論文頁內文標題下之開頭引言（`> 「……」`）。`hook` 不在網站任何位置顯示，只作為撰寫導語之素材（2026-11-09 使用者確認），故不刪除，仍為必填且須忠於原文。`card_line`、導語、`hook` 三者不得互相代用。補充細則、斷行規則與範例見 `paper-card-writer` 之 `references/cover.md`，不得與下列規則衝突。撰寫規則：
> * 20 字以內，全形標點計入字數。
> * 主詞是「這篇做了什麼」，寫出具體的動作與對象，讓非本領域讀者一眼看懂。
> * 不用「開創性」、「顛覆性」、「革命性」等評價形容詞，不用縮寫與術語（如 NMT、RAG、Transformer）；研究對象之語言名、物質名可保留。
> * 不放數值與公式；「第一次」、「證明」等強斷言須有論文頁正文或 `wiki/evidence/` 證據表支持。
> * 須能切成封面斷行：全形逗號必在行尾、每行 9 字以內、最多 3 行（`paper-card-writer` 之 `references/cover.md` 第三節）；`lint_wiki.py` 會估算最少行數並提示。
> * 範例：光遺傳學「用一道藍光，開關大腦裡特定的神經元」、Attention「不再逐字讀句子，讓每個字同時看見整句」、LIGO「第一次直接測到黑洞相撞發出的重力波」、Aghion「新技術淘汰舊技術，經濟才能長期成長」、賽德克語機器翻譯「讓電腦在賽德克語與中文之間翻譯」。

> **個人關注欄位（僅 `my_focus: true` 者填寫）**：
> 前台「我的星系」以下列兩欄位分類與呈現使用者之研究關注，置於 `my_focus` 之後：
> ```yaml
> my_focus: true
> focus_role: "senior-thesis"        # 單選，此篇在使用者研究中的角色，取下表鍵值
> focus_languages: ["泰雅語", "太魯閣語"]   # 研究對象之低資源語言
> ```
> * **`focus_role`** 依 `raw/my-focus/` 之來源分類，僅能取下列五值之一：
>
>   | 鍵值 | 名稱 | 對應 `raw/my-focus/` 來源 |
>   |---|---|---|
>   | `senior-thesis` | 學長姐論文 | `學長姐論文/` |
>   | `report` | 報告題材 | `報告論文題材/` |
>   | `taiwan-linguistics` | 臺灣語言學 | `台灣相關論文/` |
>   | `international` | 國際文獻 | `英文論文/`（不含 `llm 輔助/`） |
>   | `llm-assisted` | 大模型輔助 | `英文論文/llm 輔助/` |
>
> * **`focus_languages`** 列出研究所針對之低資源語言，以中文語言名稱書寫（如 `賽德克語`、`北薩米語`），不列中文、英文、義大利語、俄語等高資源對照或樞紐語言。涵蓋同一語族五種以上語言之綜合研究，以語族名稱代之（臺灣南島語一律寫作 `臺灣南島諸語`）。綜述或非以特定語言為研究對象者填空陣列 `[]`。

### 2. Wiki 概念頁標準 Frontmatter 規範 (`wiki/concepts/`)
概念頁檔名一律為英文小寫連字號之 slug：`wiki/concepts/<concept>.md`，該 slug 即論文頁 `concepts` 欄位所引用之鍵值。每篇概念頁頭部必須包含以下 YAML 元資料，且嚴禁包含任何 Emoji：

```yaml
---
title: "Neural Circuits & Causal Deconstruction"   # 概念英文名稱
title_zh: "神經迴路因果解耦"                         # 中文名稱
domain: "bio"                 # 單選，取概念之主要學科，決定前台配色
domain_tags: ["#神經科學", "#生物科技"]            # 多選，須取自第八章標籤白名單
papers: ["2005-optogenetics"] # 引用本概念之 wiki/papers/ 檔名（不含 .md）
related_concepts: []          # 相關之其他概念頁 slug，僅可列出已存在之頁面
verification: "unverified"    # 內容核實狀態，同論文頁（見第七章第 4 節）
---
```

> **雙向對應原則**：論文頁 `concepts` 列出某概念 slug 時，該概念頁之 `papers` 必須反向列出該論文，反之亦然。任一端新增、刪除或更名時，須同步更新另一端。

### 3. 前端展示層雙欄與響應式架構規範 (`web/papers/`)
為確保在行動裝置與桌面端均具備最高水準的閱讀體驗，每篇論文之網頁採用**「自適應雙欄/上下切換」**響應式佈局：

#### 電腦桌面端佈局（Desktop Split-View 雙欄視圖）：
* **左側固定欄（Left Column，3:4 豎版卡片區）**：
  * 居中展示 3:4 豎版知識卡片，支援點擊左右箭頭按鈕、進度圓點或鍵盤 `←` / `→` **進行水平左右切換**。
  * 採黏性固定定位（Sticky / Fixed），使讀者在右側滾動長文時，左側卡片依然可隨時交互對照。
* **右側滾動欄（Right Column，學術長文區）**：
  * 獨立視窗，支援滑鼠滾輪**上下流暢垂直滾動（Vertical Scroll）**。
  * 完整展示由 `wiki/papers/*.md` 編譯的高級學術內容，公式部分全面啟用 KaTeX 向量級 LaTeX 渲染。

> 桌面版之細部版面（左側窄導軌、右側資訊欄、卡片與長文捲動同步）與六張卡之配色（卡組丁），以 [`DESIGN.md`](./DESIGN.md) 第五章為準。

#### 行動手機端佈局（Mobile Stacked View 上下疊加視圖）：
* **上半部**：3:4 豎版卡片佔滿視覺黃金區，手指自然左右水平滑動（CSS Scroll-Snap）。
* **下半部**：長文自然順暢往下滑動閱讀，字體自動適配手機閱讀字號。長文上方有「隨卡片｜全文」開關：預設「隨卡片」只顯示目前卡片對應之段落，滑卡片即換段；「全文」顯示完整長文，與卡片互不連動（2026-11-09 使用者確認，細節見 [`DESIGN.md`](./DESIGN.md) 第五章第 1 節）。

---

#### 3:4 豎版知識圖卡之 6 張節奏規範：
> 各卡之欄位、字數上限、內容來源與 Card 3 示意圖規格，以 `paper-card-writer` 為準；卡片文字存於 `wiki/cards/<slug>.md`。

* **Card 1｜時代銘文（The Hook）**：論文大標題、發表/獲獎雙年份、領域標籤、一句話白話直擊（「這項研究到底幫全人類解決了什麼？」）。
* **Card 2｜世紀瓶頸（The Dilemma）**：視覺化痛點對比（Before vs. Problem），呈現過去科學家為什麼集體卡關。
* **Card 3｜突破架構與原理（The Secret）**：核心突破原理與理論機制，**強制採用標準 LaTeX 渲染數學/物理/生醫公式**（如矩陣、衰減常數、能量泛函）。例外：原文只有通用評估指標公式、只有資料處理公式（篩選、切分、統計用；2026-11-10 使用者確認新增）或完全沒有公式（語言描寫、系統架構、描述性綜述等）時，不得自編公式，改用無公式模式，只放示意圖與說明（2026-11-09 使用者確認，見 `paper-card-writer` 之 `references/card-03-secret.md` 第四節）。
* **Card 4｜決定性數據（The Evidence）**：決定性實驗的大數字指標（如 100% 激發率、0.7ms 抖動、5.1σ 信號值、78% 增產）。
* **Card 5｜時代典範轉移（The Revolution）**：後續引發的產業革命、臨床藥物突破或學術典範轉移。發表兩年內、尚無後續研究之論文改用新論文模式，寫本篇公開之資源與作者明列之限制、下一步，不得編造影響（2026-11-09 使用者確認，見 `references/card-05-revolution.md` 第六節）。
* **Card 6｜跨界思維與啟發（The Kairos）**：跨領域哲學反思與結尾金句（若為 `my_focus: true` 則深入探討個人研究之映射）。

### 4. 內容核實：核實狀態、問題清單與證據表
查核發現若只寫在日誌，便無人追蹤修正（2026-11-08 起多輪審查之發現截至 2026-11-09 均未修正）。故內容核實以下列三者記錄，`lint_wiki.py` 會檢查三者一致：

1. **`verification` 欄位（論文頁與概念頁必填）**：

   | 值 | 意義 | 條件 |
   |---|---|---|
   | `unverified` | 尚未依 `wiki-content-audit` 查核 | 無 |
   | `partial` | 部分卡片或主張已查核，目前無未結問題 | `wiki/issues.md` 中本頁無 `open` 問題 |
   | `issues` | 已查出問題且尚未全部修正 | `wiki/issues.md` 中本頁至少一筆 `open` 問題 |
   | `verified` | Card 1–6 與正文之強主張已逐項對應來源 | 本頁無 `open` 問題，且 `wiki/evidence/<slug>.md` 存在 |

   新收錄之頁面，若已依寫作模式完成證據表並逐項核對，可直接標 `verified`；否則標 `unverified`。

2. **問題清單 `wiki/issues.md`**：查核模式之每項發現登記一筆，格式如下，編號流水不重用：
   ```markdown
   ### EK-001 | open | papers/1982-hopfield-network.md | Card 3 | 過度表述
   - **問題**：頁面寫法與原文差異（引用原句或行號）。
   - **來源**：第一手來源連結與頁／節／表／圖。
   - **發現於**：wiki/log.md [YYYY-MM-DD HH:MM] audit（執行代理）
   ```
   * 第二段狀態取 `open`（待修正）、`fixed`（已修正）、`wontfix`（經使用者同意保留，須加註理由）。第三段為相對於 `wiki/` 之檔案路徑；第五段判定取 `wiki-content-audit` 之六種判定。
   * 修正時將狀態改為 `fixed`，並追加一行 `- **處理**：日期、執行代理、修正方式`。問題清單非日誌，可就地更新狀態，但不得刪除條目。
   * 頁面最後一筆 `open` 問題修正後，同步將 `verification` 改為 `partial`（或於證據表完成後改為 `verified`）。

3. **證據表 `wiki/evidence/<slug>.md`**：每頁一檔，slug 與論文頁或概念頁檔名相同，格式如下：
   ```markdown
   # 證據表：<slug>
   - **採用版本**：正式版／預印本／勘誤，並附連結
   - **查核者**：執行代理與模型版本，日期

   | 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
   |---|---|---|---|---|
   | Card 4 | 容量約 0.15N | 本篇研究結果 | Hopfield 1982, p. 2556 | 符合來源 |
   ```
   * 「類型」取 `wiki-content-audit` 之五類：本篇研究結果、後續研究、作者解釋、依原文數據計算、Wiki 詮釋。
   * 證據表只收強主張（數值、公式、「首次／證明／導致」等斷言、後續成果歸屬、臨床或監管狀態），敘事性背景句無須逐句列入。
   * 數值須逐一寫出並附表列與欄位，不得只寫「表 N 各數值」；論文頁每一條區塊公式須登記原文式號或頁碼，原文沒有的公式不得以區塊公式呈現（細則見 `wiki-content-audit` 寫作模式第 2、3 步）。`verified` 只代表當時已逐項核對，之後撰寫卡片者仍須回原文抽查（`paper-card-writer` 第二節第 17 條）。

### 5. 待辦清單 `wiki/todo.md`
登記尚未完成之工作：交接事項、做到一半的任務、須等使用者確認才能動工的工作。各檔分工如下，不得混記：

| 檔案 | 記錄對象 |
|---|---|
| `wiki/log.md` | 已完成之工作（歷史，只追加） |
| `wiki/issues.md` | Wiki 內容與第一手來源不符之處（查核發現） |
| `DESIGN.md` 第八章 | 美術方向之選擇題本身（選項、建議與否決理由） |
| `wiki/todo.md` | 其餘尚未完成之工作；美術待決定案後之實作工作亦登記於此 |

1. **條目格式**：不分節，條目依編號排列，格式如下：
   ```markdown
   ### TD-001 | open | web | 一句話說明要做什麼
   - **內容**：要做什麼、涉及哪些檔案、怎麼做。
   - **完成條件**：做到什麼程度算完成。
   - **等待**：須等使用者決定之事項（狀態為 waiting 時必填）。
   - **負責**：執行代理（狀態為 doing 時必填）。
   - **進度**：已完成與卡住之處（選填，做到一半時填寫）。
   - **來源**：wiki/log.md [YYYY-MM-DD HH:MM] 或使用者指示；登記日期與執行代理。
   ```
2. **狀態**：`open`（可直接接手）、`waiting`（等使用者決定，不得自行動工）、`doing`（某代理進行中，他人不得重複接手；中斷時改回 `open` 並寫明進度）。完成或放棄（放棄須經使用者同意）時直接刪除條目，不設完成狀態，歷史由日誌與 Git 保存。
3. **範圍**：`wiki`（`wiki/` 內容）、`web`（展示層）、`raw`（原始資料，實際操作仍受第五章限制）、`rule`（`AGENTS.md`、`DESIGN.md`、`README.md` 等規範文件）、`skill`（`.agents/skills/` 與其腳本）。
4. **編號**：`TD-` 加三位數流水號，不重用。新增前執行 `python .agents/skills/git-sync-guardian/scripts/stage_todo.py --next-id` 取得下一號（取本檔與日誌中出現過之最大編號加一，故刪除條目時當次日誌須寫明編號）。
5. **更新與提交**：本檔非日誌，狀態、進度與內容可就地修改，完成即刪；提交時只暫存自己這次新增、修改或刪除之條目，以 `safe_commit_push.sh --todo TD-NNN` 逐條暫存（第十章第 5 條）。
6. **不必寫日誌的情形**：只新增或更新待辦條目、而無其他已完成工作時，可直接提交，不另寫日誌。

---

## 八、專業領域標籤（Domain Tags）標準

標籤採**兩層制**，以兼顧色彩一致性與檢索彈性：

1. **`domain`（單選，必填）**：決定該條目在前台的配色，僅能取 `bio`、`ai`、`physics`、`econ`、`chem`、`human` 六值之一（見第二章對應表與學科邊界說明）。
2. **`domain_tags`（多選，必填）**：供知識星圖連線與篩選之細分標籤，一律取自下方白名單。

### 標籤白名單與色系歸屬

| 所屬 `domain` | 可用標籤 |
|---|---|
| `ai` | `#人工智慧`、`#深度學習`、`#強化學習`、`#計算機視覺`、`#計算生物`、`#自然語言處理`、`#計算語言學`、`#數學` |
| `bio` | `#生物科技`、`#結構生物學`、`#基因工程`、`#分子生物`、`#免疫學`、`#神經科學`、`#農業科技`、`#古人類學` |
| `physics` | `#天體物理`、`#量子物理`、`#宇宙學`、`#統計物理`、`#地球科學`、`#氣候科學` |
| `econ` | `#制度經濟學`、`#宏觀經濟學` |
| `chem` | `#材料科學`、`#清潔能源`、`#化學合成` |
| `human` | `#語言學`、`#心理學`、`#社會學` |

> **白名單維護規則**：
> 若新收錄之論文確實無任何既有標籤可用，不得逕自新增。須先在本章表格中正式登記新標籤並指定其所屬 `domain`，再於論文頁使用，且須於 `wiki/log.md` 留下一筆 `rule` 紀錄。此舉確保前台篩選器與配色永不出現無主標籤。
>
> **已收斂之舊標籤**：早期條目曾使用 `#腦科學`、`#有機化學`、`#臨床醫學`、`#AI-for-Science`、`#代謝醫學`、`#量子計算`、`#腫瘤生物學`、`#創新經濟學`、`#精準醫療`、`#世界模型`、`#氣候韌性` 等白名單外標籤，已於 2026-11-06 索引重建時收斂至上表；概念頁曾使用之 `#計算神經學`、`#腦機介面` 亦於 2026-11-07 收斂。上列標籤後續收錄不得再使用。
>
> **2026-11-07 調整（經使用者確認）**：`#統計物理` 正式登記為 `physics` 標籤，並自上述收斂清單移出；`#古人類學` 由 `physics` 改歸 `bio`；`#化學合成` 由 `physics` 改歸 `energy`。
>
> **2026-11-08 調整（經使用者確認）**：配合 `raw/my-focus/` 碩士論文研究主題（臺灣南島語與低資源機器翻譯），於 `ai` 色系白名單正式登記 `#自然語言處理` 與 `#計算語言學`。
>
> **2026-11-08 學科重劃（經使用者確認）**：`domain` 由五值擴為六值。`energy`（清潔能源與新材料）更名為 `chem`（化學、材料與能源），原有三個標籤隨之移轉，使諾貝爾化學獎類條目有對應色系；新增 `human`（語言、心理與社會），登記 `#語言學`、`#心理學`、`#社會學`；`ai` 擴為「人工智慧、計算與數學」並登記 `#數學`；`physics` 擴為「物理、天文與地球科學」並登記 `#地球科學`、`#氣候科學`。上限原則：`domain` 以不超過七值為度，以維持色彩可辨識度，細分需求一律交由 `domain_tags` 承擔。

---

## 九、使用者原則最高條款
* **尊重使用者的審核權限**：未經使用者明確指示或確認，不可擅自批量竄改核心檔案。
* **日誌身分與模型型號硬性標註**：每次寫入 `wiki/log.md` 時，必須在條目中如實載明當前操作之「AI 代理身分名稱」（例如：Antigravity by Google DeepMind）與「底層模型版本型號」（例如：Gemini 3.8 Flash），嚴禁匿名或省略，以確保知識庫長期演進之審計透明度。
* **「提交必含推送」原子操作**：凡使用者要求「提交」、「commit」或階段任務完成時，AI 必須將 `commit` 與 `push` 視為單一原子操作，嚴禁留滯本機 commit 不推送；動工前一律先檢查遠端動態（詳見第十章）。
* **LaTeX 完美適配為絕對重點**：每一篇論文之理論推導、動力學方程與關鍵參數，必須提供完整合規的 KaTeX 向量排版，並確保在手機與 3:4 豎版卡片上具備橫向防溢出與自適應換行能力，嚴禁截圖代替公式。原文沒有公式的研究不得為了湊公式而自編（見第七章第 3 節 Card 3 之例外）。
* **拒絕任何表情符號（Emoji）**：全庫一律採用文字、中括號標籤或純幾何符號，維持嚴謹典雅的學術出版風格。
* **保持專案輕量**：主倉庫一律不收納原始 PDF 大檔案，原始 PDF 僅存於私有倉庫 Mine-RAW（見第五章）；`wiki/` 與 `web/` 引用原文時一律採用 DOI/arXiv 官方超連結跳轉。

---

## 十、多 AI 協同開發與雙倉庫版本控制協定（Multi-AI Git Protocol）

> **協作背景**：
> 本專案採用多代理人（Multi-AI）異步協同開發架構，包括 Anthropic Claude Code、OpenAI Codex / GPT、Google Antigravity / Gemini 等多個前沿 AI 系統同時參與本專案之程式開發、論文翻譯與知識庫維護。
> 同時，專案存在嚴格的雙倉庫拓撲：公開主倉庫（`Epoch-Kairos`）與私有原始資料倉庫（`raw/` 內的 `Mine-RAW`）。
> 由於多個 AI 在不同環境提交內容，為徹底根絕「分支分岔（Divergent branches）」、「本機遺留 commit 未推送導致狀態脫節」、「遠端衝突覆蓋」、「誤提交他人修改」、「日誌寫入後遲未提交」等結構性混亂，全專案所有 AI 代理人必須嚴格遵守以下六項鐵律：

1. **「提交必含推送（Commit Implies Push）」原子操作鐵律**：
   - 只要使用者指示「提交」、「commit」或當 AI 完成某一階段性任務進行版本固化時，**必須將 `git commit` 與 `git push` 視為單一不可分割的原子操作**。
   - 嚴格禁止任何僅執行 `git commit` 而將 commit 留滯於本機不推送的行為。AI 在回報任務完成時，必須確認本地分支與遠端分支完全對齊（`Ahead: 0`）。
2. **「動工與提取前必先檢查遠端（Pre-flight Fetch Check）」防分岔機制**：
   - 在開始任何實質性的檔案修改、或在執行 `git pull` 前，AI 必須主動執行 `git fetch origin main`，檢查遠端是否有其他 AI 剛剛推送的新 commit。
   - 若遠端領先（Behind）且無衝突，優先透過快速前進或合流整合；若發現本機與遠端已分岔（Divergent），必須立即進行三方合併（3-way merge），且在合併時完整保留各方日誌。
3. **「雙倉庫一體化覆蓋（Dual-Repo Parity）」**：
   - 若當前任務涉及 `raw/` 內的任何原始素材、文獻剪藏或新生成之 PDF 譯本，檢查與提交推送操作必須在主倉庫（`Epoch-Kairos`）與私有倉庫（`Mine-RAW`，位於 `raw/`）兩邊皆完整執行。不可顧此失彼。
4. **「日誌並行合流原則（Log Append-Only Concurrency）」**：
   - `wiki/log.md` 為追加模式（Append-only）。當多個 AI 同時在日誌末尾追加紀錄而產生 Git 合併衝突時，一律按時間戳記先後排序並保留所有條目，嚴禁覆蓋或抹除其他 AI 的工作紀錄。
5. **「只提交自己的修改（Commit Only Your Own Changes）」**：
   - 多個 AI 共用同一個工作目錄，工作目錄中常同時存在其他代理尚未提交的修改。嚴禁使用 `git add -A`、`git add .` 或 `git commit -a`；提交前須以 `git diff --stat` 逐檔確認，只暫存自己修改的檔案，未追蹤之資料夾（如他人的 `work/`）一律不得加入。
   - `wiki/log.md` 只可提交「執行代理」為自己的條目，其他代理尚未提交的條目須留在工作目錄，由其主人自行提交；以 `scripts/stage_log.py` 逐條暫存。
   - `wiki/issues.md` 亦為共用檔案，只可提交自己修改的問題條目：`safe_commit_push.sh` 列出該檔時須以 `--issue EK-NNN` 指定編號，由 `scripts/stage_issues.py` 逐條暫存。
   - `wiki/todo.md` 亦為共用檔案：`safe_commit_push.sh` 列出該檔時須以 `--todo TD-NNN` 指定自己新增、修改或刪除之條目，由 `scripts/stage_todo.py` 逐條暫存（含刪除）。
   - 合流遠端時以 `git merge --autostash` 暫收他人未提交的修改，合流後放回並維持未暫存狀態；不得把他人的修改併入自己的提交。
   - 背景：2026-11-08 曾發生 Claude Code 以整檔加入 `wiki/log.md`，誤將 Codex 尚未提交的 4 筆審查紀錄帶入自己的提交；舊版 `safe_commit_push.sh` 亦以 `git add -A` 暫存全部檔案。
6. **「寫入日誌即提交（Log Implies Commit）」**：
   - 在 `wiki/log.md` 追加自己的條目後，必須在同一回合內以 `safe_commit_push.sh` 提交並推送該條目與本項工作修改的檔案，無須等待使用者另行說「提交」；僅在使用者明確要求暫緩時例外。
   - 工作尚未完成、或使用者要求先不提交時，先不要寫日誌；進度與交接事項登記於 `wiki/todo.md`（見第六章第 4 節），完成後再寫日誌並提交。
   - 寫日誌一律追加於檔尾，不得讀取整份日誌後整檔寫回（會覆蓋他人剛追加、尚未提交的條目），亦不得改動他人條目。
   - 標題時間一律先執行 `scripts/log_time.py` 取得，不得憑估計填寫（規則見第六章 Ingest 第 5 步；`stage_log.py` 會機械檢查）。
   - 目的：日誌是共用檔案，條目滯留在工作目錄會被他人誤帶、阻擋同步，甚至遭覆寫；每筆日誌都對應一個已推送的提交，多 AI 協作出問題時才能立即追查。
7. **專屬輔助技能與工具鏈調用**：
   - 專案已建立專屬 Skill `.agents/skills/git-sync-guardian/`，內建狀態審計、安全合流與推送腳本（同時提供跨平台 Python 版 `scripts/status.py`、`scripts/sync.py`、`scripts/safe_commit_push.py` 與 Bash 版 `scripts/status.sh`、`scripts/sync.sh`、`scripts/safe_commit_push.sh`；Windows PowerShell 或沙盒環境優先使用 `.py` 版以省去啟動外部 Bash 之權限耗時）及日誌工具（`scripts/log_time.py` 取得日誌標題時間、`scripts/stage_log.py` 逐條暫存自己的日誌、`scripts/stage_issues.py` 逐條暫存自己修改的問題條目、`scripts/stage_todo.py` 逐條暫存自己修改的待辦條目並提供下一個編號、`scripts/log_tail.py` 依條目讀取日誌最後幾筆、`scripts/merge_log.py` 依 append-only 自動排解日誌衝突），各 AI 應主動調用該工具鏈以確保版控一致性。`safe_commit_push.py` / `safe_commit_push.sh` 須明確列出要提交的檔案並以 `--agent` 指定執行代理名稱。`stage_log.py` 暫存之條目順序一律跟隨工作目錄，不依時間重排，以免提交後日誌持續顯示為已修改。其餘專屬 Skill 見第六章開頭之 Skill 一覽。
   - `safe_commit_push.py` / `.sh` 只接受倉庫內單一相對檔案路徑，拒絕資料夾與路徑跳脫，並以 literal pathspec 暫存；執行前須確認目前分支為 `main`，且先成功 fetch 才能暫存或建立提交。`status.py` / `.sh` 的本機 Git 查詢失敗必須回報未知狀態及非零退出碼；日誌衝突的合併提交失敗不得回報成功。

