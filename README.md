# Epoch-Kairos ｜ 人類群星閃耀時

> **"The Kairos of human thought and research horizons."**  
> 在漫長的客觀時間（Chronos）中，唯有那些改變人類文明軌跡的決定性時刻（Kairos），宛如夜空中驟然閃耀的群星。

本專案是一個**跨領域時代權威論文與諾貝爾獎導讀庫**，基於 **Andrej Karpathy 的 LLM Wiki 架構** 打造，具備自組織、持續積累與知識生長特性的智慧研究花園。

---

## 🏛️ 系統架構（LLM Wiki Pattern）

本專案落實了 Karpathy 提出的經典三層架構 ＋ 前端展示層：

```text
Epoch-Kairos/
├── AGENTS.md              # 【Schema】專案規則手冊（AI 協作指南與作業核心）
├── raw/                   # 【Raw Sources】不可變原始素材層（論文筆記、摘要、使用者文件）
│   └── my-focus/          #  個人資料區
├── wiki/                  # 【The Wiki】AI 維護之知識核心（Markdown）
│   ├── index.md           # 內容總索引（按年份與領域交織分類）
│   ├── log.md             # 操作日誌（Append-only 時間流動記錄）
│   ├── papers/            # 結構化論文知識卡片
│   └── concepts/          # 跨學科概念與實體
└── web/                   # 【Web Presentation】GitHub Pages 互動時間線與 6 頁 Web PPT 講義
```

---

## ⚙️ 核心工作流（Operations）

1. **Ingest（收錄流）**：當新來源放入 `raw/`，AI 依據 [`AGENTS.md`](./AGENTS.md) 自動提煉結構化知識、更新 `wiki/` 雙向鏈結，並同步編譯為前台 Web 簡報卡片。
2. **Query（查詢流）**：AI 優先透過 `wiki/index.md` 進行跨領域綜合檢索，沉澱高價值思考。
3. **Lint（健康檢查）**：定期審查孤島頁面、知識衝突與過期假說。

---

## 🌐 成果瀏覽

* **GitHub Repository**：[https://github.com/zhi816/Epoch-Kairos](https://github.com/zhi816/Epoch-Kairos)
* **GitHub Pages 成果展示**：*(部署完成後連結：https://zhi816.github.io/Epoch-Kairos/)*
