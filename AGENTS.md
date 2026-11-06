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

### 1. 基礎畫布與文字色彩（源自 Deimos）
* 背景底色（Background）：`#0B0C0E`（黑曜石冷灰暗黑底，深度低噪聲）
* 卡片本體（Card Surface）：`#161618`（高階精裝書表面，物理浮起感）
* 卡片懸浮層（Surface Raised）：`#202023`
* 極細邊框（Hairline Border）：`rgba(255, 255, 255, 0.08)`（1px 半透明髮絲線）
* 強調邊框（Border Strong）：`rgba(255, 255, 255, 0.16)`
* 標題文字（Primary Text）：`#EDEDED`（柔和象牙白，高易讀性）
* 次要文字（Muted Text）：`#888888` / `#A1A1A6`
* 極淡標籤（Subtle Meta）：`#55555A`

### 2. 跨學科專屬色碼微光系統（源自 Shopify Editions）
各學科分配專屬色碼與微光（Glow），用於卡片標籤、公式光暈與跑道時間線：
* **[生醫與生命科技]**：冷翠螢光綠 `#00E599`，微光 `rgba(0, 229, 153, 0.15)`
* **[人工智慧與計算]**：霓虹電能青 `#00F0FF`，微光 `rgba(0, 240, 255, 0.15)`
* **[物理、天文與量子]**：深邃宇宙紫 `#8B5CF6`，微光 `rgba(139, 92, 246, 0.18)`
* **[宏觀經濟與治理]**：香檳琥珀金 `#FFB800`，微光 `rgba(255, 184, 0, 0.15)`
* **[清潔能源與新材料]**：等離子珊瑚橙 `#FF5722`，微光 `rgba(255, 87, 34, 0.15)`

---

## 三、LaTeX 數學與物理公式極致適配準則 (LaTeX Mathematical Excellence Standard)

> **最高優先級核心技術指標**：本知識庫以「完美適配 LaTeX 數學/物理/工程符號」為絕對重點。全站一律採用標準 KaTeX 向量排版，嚴禁使用低解析度圖片替代公式。

1. **行內公式 (Inline Math)**：
   - 採用單錢字號 `$...$` 封裝（例如：離子符號 `$Na^+$`、能量動量關係 `$E^2 = p^2 c^2 + m^2 c^4$`）。
   - 必須確保垂直對齊正文文字基線，避免文字跳動。
2. **區塊公式 (Display Block Math)**：
   - 採用雙錢字號 `$$...$$` 獨立成段展示（例如：膜電位 Hodgkin-Huxley 微分方程、Transformer 自注意力權重矩陣）。
   - 水平垂直居中展示，字型清晰平滑。
3. **3:4 豎版圖卡與行動端防溢出 (Responsive Math Container)**：
   - 前端樣式強制對公式容器設定 `overflow-x: auto; -webkit-overflow-scrolling: touch;`，在手機窄螢幕與 3:4 豎版圖卡中提供平滑水平捲動，絕對不破版、不截斷。
   - 長公式強制使用 `\begin{aligned} ... \end{aligned}` 進行等號對齊與斷行。
4. **視覺微光整合 (Editorial Math Aesthetics)**：
   - 區塊公式容器採用 `#101012` 深邃黑曜石背景，並施加對應學科專屬微光（如物理紫、生醫綠），營造高階學術期刊特寫感。

---

## 四、系統架構（Three Layers + Presentation）

本專案由嚴格的三層結構與一個前端展示層組成：

```text
Epoch-Kairos/
├── AGENTS.md                  # 【第三層：Schema】本規範文件，指導 AI 如何維護與擴充知識庫
├── README.md                  # 專案介紹與 GitHub Pages 瀏覽入口說明
│
├── raw/                       # 【第一層：Raw Sources】原始資料層（不可變，Immutable）
│   ├── my-focus/              # 【使用者專屬關注區】存放個人精選研究、私人筆記與核心關注資料
│   └── (存放論文原始摘要、筆記草稿、新聞、外部文獻剪藏)
│
├── wiki/                      # 【第二層：The Wiki】知識庫核心層（由 AI 讀寫與維護）
│   ├── index.md               # 內容目錄索引（Content Catalog，按年份與領域組織）
│   ├── log.md                 # 時間流水帳日誌（Append-only，記錄所有操作）
│   ├── papers/                # 結構化論文知識頁（Markdown）
│   └── concepts/              # 跨領域核心概念與實體頁（Markdown）
│
└── web/                       # 【展示層：Web Presentation】供 GitHub Pages 部署之成果
    ├── index.html             # 人類重大突破時間線（Timeline）總覽頁（含「我的關注」一鍵切換）
    ├── assets/                # 前端靜態資源（CSS、JS、字體）
    │   ├── css/
    │   │   ├── theme.css      # Deimos 與 Shopify 配色體系與全域變數
    │   │   ├── timeline.css   # 時間線與首頁樣式
    │   │   └── cards.css      # 3:4 知識圖卡與學術長文雙欄樣式
    │   └── js/
    │       ├── timeline.js    # 篩選、過濾與時間線動畫
    │       └── cards.js       # 3:4 卡片左右切換與 KaTeX 連動引擎
    └── papers/                # 每篇論文之專屬雙欄互動頁（HTML 格式）
```

---

## 五、三層職責與權限劃分

1. **第一層：Raw Sources (`raw/`)**
   * **性質**：專案的「唯一真實來源（Single Source of Truth）」，**嚴禁 AI 擅自覆寫或刪除**。
   * **來源**：由使用者親自放入的論文文字、筆記草稿，以及專屬個人研究資料夾 `raw/my-focus/`。
   * **AI 權限**：**唯讀（Read-Only）**。

2. **第二層：The Wiki (`wiki/`)**
   * **性質**：知識的「編譯結果與累積實體（Compounding Artifacts）」。
   * **特點**：每一篇新來源的加入，不僅是新增一頁，更會自動更新關聯的概念、修正舊論述、建立雙向交叉引用（Cross-References）。
   * **AI 權限**：**完全讀寫與維護（Read & Write）**。

3. **第三層：The Schema (`AGENTS.md`)**
   * **性質**：定義 AI 的作業規範、格式標準與操作工作流（Workflows）。
   * **更新機制**：由使用者與 AI 共同隨需求演進與調整。

4. **展示層：Web Presentation (`web/`)**
   * **性質**：將 `wiki/` 的知識編譯為可在 GitHub Pages 上流暢瀏覽的跑道時間線與 3:4 豎版知識圖卡＋深度學術長文。

---

## 六、AI 核心作業流程（Core Operations）

AI 在協作時，必須嚴格遵循以下三大標準作業程序（SOP）：

### 1. Ingest（收錄新來源）
當使用者在 `raw/` 放入新文件或指令收錄一篇論文時，AI 必須依序執行以下 5 個步驟：
1. **讀取來源**：分析原始文本，提取核心命題、年代、期刊/榮譽、以及作者團隊。
2. **撰寫論文頁**：檔案命名一律以論文實際發表年份（`paper_year`）為前綴：`wiki/papers/YYYY-<slug>.md`（例如：`2025-optogenetics.md`）。若獲獎年份不同，則在 Frontmatter 中以 `award_year` 與 `honor` 完整標註。
3. **萃取/關聯概念**：檢查是否觸及跨領域概念（如同時涉及 AI 與結構生物學），同步更新或建立 `wiki/concepts/<concept>.md`。
4. **編譯網頁成果**：
   * 在 `web/papers/YYYY-<slug>/index.html` 產生對應之雙欄互動頁（左側 3:4 知識圖卡，右側 KaTeX 長文）。
   * 在 `web/index.html` 的時間線上插入卡片，正確標註領域標籤與 `data-focus` 屬性。
5. **更新索引與日誌**：
   * 在 `wiki/index.md` 登記該論文之摘要與連結。
   * 在 `wiki/log.md` 結尾追加一筆紀錄：
     `## [YYYY-MM-DD] ingest | <論文名稱> | <領域標籤>`

### 2. Query（知識綜合檢索）
當使用者針對知識庫提問時：
1. AI 優先閱讀 `wiki/index.md` 與相關的 `wiki/concepts/`，而非盲目搜尋。
2. 串聯多篇跨學科論文，產出具有明確引用來源（Citations）的深度綜合解答。
3. 若提問產生了具備長期價值的洞見或對比分析，AI 應主動詢問是否將其存入 `wiki/concepts/` 或歸檔為新的知識卡片。

### 3. Lint（知識庫健康檢查）
定期或於使用者要求時執行：
1. **檢查孤島頁面**：標記沒有任何反向連結（Inbound Links）的條目。
2. **檢查觀點衝突與技術迭代**：標記被後續新突破推翻或修正的舊論述。
3. **檢查索引一致性**：確保 `raw/`、`wiki/papers/` 與 `web/` 三者的條目與數量嚴格對齊。
4. **檢查符號合規性**：確保全文無任何表情符號（Emoji）。
5. **檢查 LaTeX 公式完整度**：確保公式排版合規，無截斷或解析錯誤。

---

## 七、內容與格式規範

### 1. Wiki 論文頁標準 Frontmatter 規範 (`wiki/papers/`)
每篇 Markdown 檔案頭部必須包含 YAML 元資料。針對諾貝爾獎等重大獎項與論文發表存在時間差之情況，一律採取**「雙年份標註規則（Dual-Year Rule）」**，且嚴禁包含任何 Emoji：

```yaml
---
title: "論文完整英文標題"
title_zh: "中文通俗譯名"
paper_year: 2025              # 原始論文發表年份（真實學術發表時間）
award_year: 2026              # 榮譽表彰或獲獎年份（如諾貝爾獎頒發年，無則填同 paper_year）
timeline_year: 2026           # 時間線歸檔節點（預設依重大影響/獲獎年 award_year 排序）
authors: "主要作者團隊"
venue: "Nature / Science / 諾貝爾獎頒獎通告"
honor: "[榮譽] 2026 諾貝爾生理學或醫學獎"
domain_tags: ["#神經科學", "#腦科學"]
my_focus: false               # 若為使用者特別關注則標記為 true
doi_url: "https://doi.org/..."
---
```

> **雙年份呈現原則**：
> 在前台時間線總覽與每篇論文的封面卡片上，必須同時清晰並列標記 **「2025 發表 ｜ 2026 諾貝爾獎」**，兼顧科學史發表真實性與當代獲獎影響力。

### 2. 前端展示層雙欄與響應式架構規範 (`web/papers/`)
為確保在行動裝置與桌面端均具備最高水準的閱讀體驗，每篇論文之網頁採用**「自適應雙欄/上下切換」**響應式佈局：

#### 電腦桌面端佈局（Desktop Split-View 雙欄視圖）：
* **左側固定欄（Left Column，3:4 豎版卡片區）**：
  * 居中展示 3:4 豎版知識卡片，支援點擊左右箭頭按鈕、進度圓點或鍵盤 `←` / `→` **進行水平左右切換**。
  * 採黏性固定定位（Sticky / Fixed），使讀者在右側滾動長文時，左側卡片依然可隨時交互對照。
* **右側滾動欄（Right Column，學術長文區）**：
  * 獨立視窗，支援滑鼠滾輪**上下流暢垂直滾動（Vertical Scroll）**。
  * 完整展示由 `wiki/papers/*.md` 編譯的高級學術內容，公式部分全面啟用 KaTeX 向量級 LaTeX 渲染。

#### 行動手機端佈局（Mobile Stacked View 上下疊加視圖）：
* **上半部**：3:4 豎版卡片佔滿視覺黃金區，手指自然左右水平滑動（CSS Scroll-Snap）。
* **下半部**：長文自然順暢往下滑動閱讀，字體自動適配手機閱讀字號。

---

#### 3:4 豎版知識圖卡之 6 張節奏規範：
* **Card 1｜時代銘文（The Hook）**：論文大標題、發表/獲獎雙年份、領域標籤、一句話白話直擊（「這項研究到底幫全人類解決了什麼？」）。
* **Card 2｜世紀瓶頸（The Dilemma）**：視覺化痛點對比（Before vs. Problem），呈現過去科學家為什麼集體卡關。
* **Card 3｜突破架構與原理（The Secret）**：核心突破原理與理論機制，**強制採用標準 LaTeX 渲染數學/物理/生醫公式**（如矩陣、衰減常數、能量泛函）。
* **Card 4｜決定性數據（The Evidence）**：決定性實驗的大數字指標（如 100% 激發率、0.7ms 抖動、5.1σ 信號值、78% 增產）。
* **Card 5｜時代典範轉移（The Revolution）**：後續引發的產業革命、臨床藥物突破或學術典範轉移。
* **Card 6｜跨界思維與啟發（The Kairos）**：跨領域哲學反思與結尾金句（若為 `my_focus: true` 則深入探討個人研究之映射）。

---

## 八、專業領域標籤（Domain Tags）標準

為保持時間線篩選的一致性，標籤必須統一使用以下命名：
* `#人工智慧`、`#深度學習`、`#強化學習`、`#計算機視覺`
* `#生物科技`、`#結構生物學`、`#基因工程`、`#分子生物`、`#免疫學`、`#神經科學`
* `#天體物理`、`#量子物理`、`#宇宙學`、`#材料科學`、`#清潔能源`
* `#制度經濟學`、`#宏觀經濟學`、`#古人類學`、`#農業科技`

---

## 九、使用者原則最高條款
* **尊重使用者的審核權限**：未經使用者明確指示或確認，不可擅自批量竄改核心檔案。
* **LaTeX 完美適配為絕對重點**：每一篇論文之理論推導、動力學方程與關鍵參數，必須提供完整合規的 KaTeX 向量排版，並確保在手機與 3:4 豎版卡片上具備橫向防溢出與自適應換行能力，嚴禁截圖代替公式。
* **拒絕任何表情符號（Emoji）**：全庫一律採用文字、中括號標籤或純幾何符號，維持嚴謹典雅的學術出版風格。
* **保持專案輕量**：一律不收納原始 PDF 大檔案，所有原文一律採用 DOI/arXiv 官方超連結跳轉。
