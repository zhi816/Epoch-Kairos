# AGENTS.md - Epoch-Kairos（人類群星閃耀時）維護手冊

> **專案核心精神**：
> 「在漫長的時間長河（Chronos）中，唯有那些改變人類文明軌跡的決定性時刻（Kairos），宛如夜空中驟然閃耀的群星。」
> 本專案以 Andrej Karpathy 的 **LLM Wiki** 模式為核心架構，建立一套能夠隨時間**持續累積、自我演進、跨領域交織**的時代里程碑論文與個人研究關注知識庫。

---

## 一、系統架構（Three Layers + Presentation）

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
    │   │   ├── timeline.css   # 時間線與首頁樣式
    │   │   └── slides.css     # 投影片共用樣式與自適應縮放
    │   └── js/
    │       ├── timeline.js    # 篩選、過濾與時間線動畫
    │       └── slides.js      # 鍵盤/觸控投影片切換引擎
    └── papers/                # 每篇論文之專屬互動 Web PPT（HTML 格式）
```

---

## 二、三層職責與權限劃分

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
   * **性質**：將 `wiki/` 的知識編譯為可在 GitHub Pages 上流暢瀏覽的時間線與 6 頁互動式 Web PPT。

---

## 三、AI 核心作業流程（Core Operations）

AI 在協作時，必須嚴格遵循以下三大標準作業程序（SOP）：

### 1. Ingest（收錄新來源）
當使用者在 `raw/` 放入新文件或指令收錄一篇論文時，AI 必須依序執行以下 5 個步驟：
1. **讀取來源**：分析原始文本，提取核心命題、年代、期刊/榮譽、以及作者團隊。
2. **撰寫論文頁**：檔案命名一律以論文實際發表年份（`paper_year`）為前綴：`wiki/papers/YYYY-<slug>.md`（例如：`2025-optogenetics.md`）。若獲獎年份不同，則在 Frontmatter 中以 `award_year` 與 `honor` 完整標註。
3. **萃取/關聯概念**：檢查是否觸及跨領域概念（如同時涉及 AI 與結構生物學），同步更新或建立 `wiki/concepts/<concept>.md`。
4. **編譯網頁成果**：
   * 在 `web/papers/YYYY-<slug>/index.html` 產生對應之 6 頁互動式 Web PPT。
   * 在 `web/index.html` 的時間線上插入卡片，正確標註標籤與 `data-focus` 屬性。
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

---

## 四、內容與格式規範

### 1. Wiki 論文頁標準 Frontmatter 規範 (`wiki/papers/`)
每篇 Markdown 檔案頭部必須包含 YAML 元資料。針對諾貝爾獎等重大獎項與論文發表存在時間差之情況，一律採取**「雙年份標註規則（Dual-Year Rule）」**：

```yaml
---
title: "論文完整英文標題"
title_zh: "中文通俗譯名"
paper_year: 2025              # 原始論文發表年份（真實學術發表時間）
award_year: 2026              # 榮譽表彰或獲獎年份（如諾貝爾獎頒發年，無則填同 paper_year）
timeline_year: 2026           # 時間線歸檔節點（預設依重大影響/獲獎年 award_year 排序）
authors: "主要作者團隊"
venue: "Nature / Science / 諾貝爾獎頒獎通告"
honor: "🏆 2026 諾貝爾醫學獎"
domain_tags: ["#神經科學", "#腦科學"]
my_focus: false               # 若為使用者特別關注則標記為 true
doi_url: "https://doi.org/..."
---
```

> **雙年份呈現原則**：
> 在前台時間線卡片與 Web PPT 封面上，必須同時清晰並列標記 **「2025 發表 ｜ 2026 諾貝爾獎」**，兼顧科學史發表真實性與當代獲獎影響力。

### 2. 論文 6 頁 Web PPT 投影片結構規範 (`web/papers/`)
每一篇論文轉換為網頁投影片時，固定遵守 6 頁節奏：
* **Slide 1｜時代銘文（Cover）**：標題、發表年代、期刊/會議、榮譽徽章、一句話本質貢獻。
* **Slide 2｜世紀瓶頸（The Bottleneck）**：在該研究出現前，全人類科學家面臨的核心難題與困境。
* **Slide 3｜突破性架構與原理（The Breakthrough）**：核心理論模型、架構圖解、關鍵公式（以標準 LaTeX 語法渲染，行內 `$...$`, 區塊 `$$...$$`）。
* **Slide 4｜決定性實驗數據（The Evidence）**：關鍵實驗對比數據、震撼世界的驗證指標。
* **Slide 5｜時代典範轉移（The Impact）**：該突破對後續學術界與全球產業帶來的深遠變革。
* **Slide 6｜跨界思維與啟發（Reflection）**：特別留給研究者的跨學科省思（若 `my_focus: true` 則深入探討與個人研究之映射）。

---

## 五、專業領域標籤（Domain Tags）標準

為保持時間線篩選的一致性，標籤必須統一使用以下命名：
* `#人工智慧`、`#深度學習`、`#強化學習`、`#計算機視覺`
* `#生物科技`、`#結構生物學`、`#基因工程`、`#分子生物`、`#免疫學`、`#神經科學`
* `#天體物理`、`#量子物理`、`#宇宙學`、`#材料科學`、`#清潔能源`
* `#制度經濟學`、`#宏觀經濟學`、`#古人類學`、`#農業科技`

---

## 六、使用者原則最高條款
* **尊重使用者的審核權限**：未經使用者明確指示或確認，不可擅自批量竄改核心檔案。
* **保持專案輕量**：一律不收納原始 PDF 大檔案，所有原文一律採用 DOI/arXiv 官方超連結跳轉。
