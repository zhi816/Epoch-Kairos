# Epoch-Kairos ｜ 人類群星閃耀時

> **"The Kairos of human thought and research horizons."**  
> 在漫長的客觀時間（Chronos）中，唯有那些改變人類文明軌跡的決定性時刻（Kairos），宛如夜空中驟然閃耀的群星。

本專案是一個**跨領域時代權威論文與諾貝爾獎導讀庫**，基於 **Andrej Karpathy 的 LLM Wiki 架構** 打造，具備自組織、持續積累與知識生長特性的智慧研究花園。全專案嚴格維持出版級學術風格，全站無任何表情符號。

> **完整規範請見 [`AGENTS.md`](./AGENTS.md)**：本 README 僅提供專案概覽；Frontmatter 欄位、標籤白名單、LaTeX 準則、日誌格式與 Lint 檢查項之唯一權威定義皆在 `AGENTS.md`，兩者若有出入，以 `AGENTS.md` 為準。

---

## 參考原型與設計來源

1. **Andrej Karpathy - LLM Wiki 架構**（[gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)）：三層資料架構，不可變原始資料 `raw/`、結構化編譯知識 `wiki/`、代理人運作規範 `AGENTS.md`。
2. **Evil Rabbit - Deimos Designer Encyclopedia**（[官方網站](https://deimos.evilrabbit.com/)、[設計收錄](https://recent.design/i/i50sj5g-deimos-designer-encyclopedia)）：雜誌編排級審美、黑曜石底色、極細半透明邊框、襯線大標題。
3. **Shopify - Editions Fall '26 (Expo Mode)**（[官方網站](https://www.shopify.com/editions/fall2026)）：跑道時間線（Runway Timeline）與跨學科專屬色碼微光系統。

---

## 系統架構

```text
Epoch-Kairos/
├── AGENTS.md              # 【Schema】專案規則手冊（AI 協作指南與作業核心）
├── raw/                   # 【Raw Sources】不可變原始素材層（獨立私有倉庫 Mine-RAW，本倉庫不追蹤）
│   └── my-focus/          # [個人專屬關注區] 個人精選研究、私人筆記與核心關注資料
├── wiki/                  # 【The Wiki】AI 維護之知識核心（Markdown）
│   ├── index.md           # 內容總索引（按年份與領域組織，含條目狀態與待辦）
│   ├── log.md             # 操作日誌（Append-only，逐筆記載執行代理與模型版本）
│   ├── papers/            # 結構化論文知識頁（檔名以實際發表年份為前綴）
│   └── concepts/          # 跨學科概念頁（與論文頁雙向連結）
└── web/                   # 【Web Presentation】GitHub Pages 成果展示層
    ├── index.html         # 人類重大突破時間線總覽頁（含「我的關注」一鍵切換）
    ├── assets/            # CSS、JS（theme.css 為全站色碼唯一真實來源）
    └── papers/            # 每篇論文之「3:4 豎版圖卡 ＋ KaTeX 學術長文」雙欄網頁
```

### 原始層採雙倉庫分離（Dual-Repository Split）

`raw/` 已於本倉庫 `.gitignore` 全目錄排除，**不隨本倉庫公開**。自 2026-11-08 起，該層改由獨立私有倉庫 [`zhi816/Mine-RAW`](https://github.com/zhi816/Mine-RAW) 版控，在 `raw/` 目錄內自成一個 Git 工作區（並非 submodule，兩倉庫彼此完全獨立）。

| | Epoch-Kairos（本倉庫） | Mine-RAW |
|---|---|---|
| 可見性 | 公開 | 私有 |
| 內容 | `AGENTS.md`、`wiki/`、`web/` | `raw/` 之原始 PDF 與個人筆記 |
| 規範來源 | 本倉庫 [`AGENTS.md`](./AGENTS.md) | 同左；其倉庫內 `AGENTS.md` 僅為指回本倉庫之摘要 |

**給 AI 代理與協作者的重要提醒**：在本倉庫執行任何 Git 指令永遠不會觸及 `raw/`。若 `raw/` 內容有變動，須另行 `cd raw` 單獨提交與推送，兩邊無自動連動。完整規範見 [`AGENTS.md`](./AGENTS.md) 第五章。

新機器完整還原兩層：

```bash
git clone https://github.com/zhi816/Epoch-Kairos.git
cd Epoch-Kairos
git clone https://github.com/zhi816/Mine-RAW.git raw
```

僅 clone 本倉庫者缺少 `raw/`，無法執行 [`AGENTS.md`](./AGENTS.md) 第六章第 3 節 Lint 之第 3 項（三層對齊檢查）。

---

## 核心工作流

1. **Ingest（收錄）**：新來源放入 `raw/` 後，AI 先以 Crossref 核驗 DOI 之年份、作者與卷期，再撰寫論文頁、更新概念頁雙向連結、編譯前台網頁，並登記索引與日誌。
2. **Query（查詢）**：AI 優先透過 `wiki/index.md` 與 `wiki/concepts/` 進行跨領域綜合檢索，具長期價值之洞見可沉澱為新概念頁。
3. **Lint（健康檢查）**：共 8 項，涵蓋孤島頁面、觀點衝突、三層對齊、表情符號、LaTeX 合規、年份作者真實性、標籤白名單與連結有效性。

---

## 知識條目的關鍵規則

* **雙年份標註**：`paper_year`（實際發表年份，決定檔名）與 `award_year`（獲獎年份）分開記載，前台並列呈現，例如「2005 發表 ｜ 2026 諾貝爾獎」。
* **作者與得獎者分離**：`authors` 僅記該篇論文之實際作者，獎項得獎者另記於 `laureates`；獎項表彰多篇工作時，奠基論文列入 `key_papers`。
* **條目狀態三態**：`planned`（僅立案）、`wiki`（已有 Wiki 頁）、`published`（已產出網頁）。
* **兩層標籤制**：`domain` 單選，決定配色（`bio` 生醫綠、`ai` 電能青、`physics` 宇宙紫、`econ` 琥珀金、`chem` 珊瑚橙、`human` 玫瑰粉）；`domain_tags` 多選，限用 `AGENTS.md` 第八章白名單。
* **LaTeX 為最高技術標準**：全站以 KaTeX 向量排版公式，化學離子用 `\mathrm{}` 正體，長公式以 `aligned` 斷行並具行動端橫向防溢出。

---

## 成果瀏覽

* **GitHub Repository**：[https://github.com/zhi816/Epoch-Kairos](https://github.com/zhi816/Epoch-Kairos)
* **GitHub Pages 成果展示**：*(部署完成後連結：https://zhi816.github.io/Epoch-Kairos/)*
* **目前收錄進度**：見 [`wiki/index.md`](./wiki/index.md)。
