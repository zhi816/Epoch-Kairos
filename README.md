# Epoch-Kairos ｜ 人類群星閃耀時

> **"The Kairos of human thought and research horizons."**  
> 在漫長的客觀時間（Chronos）中，唯有那些改變人類文明軌跡的決定性時刻（Kairos），宛如夜空中驟然閃耀的群星。

本專案是一個**跨領域時代權威論文與諾貝爾獎導讀庫**，基於 **Andrej Karpathy 的 LLM Wiki 架構** 打造，具備自組織、持續積累與知識生長特性的智慧研究花園。全專案嚴格維持出版級學術風格，全站無任何表情符號。

---

## 參考原型與設計來源 (References & Design Inspirations)

本專案融合三大開創性設計理念：

1. **Andrej Karpathy - LLM Wiki 架構**：
   - 來源網址：`https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`
   - 核心精髓：三層資料架構（不可變原始資料 `raw/`、結構化編譯知識 `wiki/`、代理人運作規範 `AGENTS.md`）。
2. **Evil Rabbit - Deimos Designer Encyclopedia**：
   - 官方網站：`https://deimos.evilrabbit.com/`
   - 設計收錄：`https://recent.design/i/i50sj5g-deimos-designer-encyclopedia`
   - 核心精髓：雜誌編排級審美（Editorial Minimalism）、沉靜黑曜石底色、極細半透明邊框、精緻襯線大標題。
3. **Shopify - Editions Fall '26 (Expo Mode)**：
   - 官方網站：`https://www.shopify.com/editions/fall2026`
   - 核心精髓：未來感跑道時間線（Runway Timeline）、跨學科專屬色碼微光系統（Color-Coded Sections）。

---

## 系統架構（LLM Wiki Pattern）

本專案落實了 Karpathy 提出的經典三層架構加上前端展示層：

```text
Epoch-Kairos/
├── AGENTS.md              # 【Schema】專案規則手冊（AI 協作指南與作業核心）
├── raw/                   # 【Raw Sources】不可變原始素材層（論文筆記、摘要、使用者文件）
│   └── my-focus/          # [個人專屬關注區] 存放個人精選研究、私人筆記與核心關注資料
├── wiki/                  # 【The Wiki】AI 維護之知識核心（Markdown）
│   ├── index.md           # 內容總索引（按年份與領域交織分類）
│   ├── log.md             # 操作日誌（Append-only 時間流動記錄）
│   ├── papers/            # 結構化論文知識卡片
│   └── concepts/          # 跨學科概念與實體
└── web/                   # 【Web Presentation】GitHub Pages 成果展示層
    ├── index.html         # 人類重大突破時間線總覽頁（含「我的關注」一鍵切換）
    ├── assets/            # CSS、JS 與樣式代碼
    └── papers/            # 每篇論文之「3:4 豎版圖卡左右輪播 ＋ 深入長文（支援 KaTeX LaTeX）」網頁
```

---

## 核心工作流（Operations）

1. **Ingest（收錄流）**：當新來源放入 `raw/`，AI 依據 [`AGENTS.md`](./AGENTS.md) 自動提煉結構化知識、更新 `wiki/` 雙向鏈結，並同步編譯為前台雙欄互動網頁。
2. **Query（查詢流）**：AI 優先透過 `wiki/index.md` 進行跨領域綜合檢索，沉澱高價值思考。
3. **Lint（健康檢查）**：定期審查孤島頁面、知識衝突與過期假說，並確保全文無表情符號。

---

## 成果瀏覽

* **GitHub Repository**：[https://github.com/zhi816/Epoch-Kairos](https://github.com/zhi816/Epoch-Kairos)
* **GitHub Pages 成果展示**：*(部署完成後連結：https://zhi816.github.io/Epoch-Kairos/)*
