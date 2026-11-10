# 概念頁與索引（S5）

本檔規範 SKILL.md 第五節 S5：把新論文接進知識網絡。概念頁決定首頁星圖上論文之間的連線與概念星，`wiki/index.md` 是全庫目錄；漏了任何一處，`lint_wiki.py` 會報孤島或雙向不一致，首頁也會少一條連線。Frontmatter 之基本規定見 `AGENTS.md` 第七章第 2 節。

## 一、選概念頁

1. 先讀 `wiki/index.md` 第五節「跨領域概念頁」的清單與各概念頁的「核心定義」，找出本篇的研究**直接屬於**的概念（不是字面相似）。
2. 每篇連一至三個概念頁。我的關注論文通常連 `formosan-computational-linguistics`（臺灣南島語計算語言學）或 `low-resource-machine-translation`（低資源機器翻譯），依本篇內容決定，不得一律兩個都連。我的星系只畫篇數最多的兩個概念作為左右中心，論文依所連概念排在左欄、右欄或中間（`DESIGN.md` 第四章）；我的關注論文若要連到第三個概念，`build_home.py` 會報「我的關注涉及 N 個概念」之 WARN，且可能改變星系的兩個中心，**先問使用者**再連。
3. 既有概念頁都不合適時才新建（本檔第二節第 3 點）。新建前在交付說明寫明：為什麼既有概念都不合適、新概念的定義、預計還有哪些論文會連到它。只有一篇論文的概念頁，先考慮能否併入既有概念。

## 二、更新概念頁

### 1. 雙向登記（必做）

* 論文頁 `concepts` 列出概念 slug。
* 該概念頁 Frontmatter 之 `papers` 加入本篇 slug（不含 `.md`），依年份排序。
* 兩邊必須一致；`lint_wiki.py` 與 `pipeline_status.py`（S5）都會檢查。

### 2. 概念頁正文（必做）

在概念頁「關鍵突破支柱」（或同性質之段落，例如「關鍵技術路徑與核心突破」）加入一條，格式與該頁既有條目相同，例如：

```markdown
* **<本篇要點，10 至 20 字>（<簡稱>, <paper_year>）**：<一至兩句說明本篇在這個概念中的位置，只寫論文頁與證據表支持的內容>
  * 詳見核心論文：[<title_zh 冒號前>（<paper_year> 發表 ｜ <獎項簡稱或期刊簡稱>）](../papers/<slug>.md)
```

* 寫進概念頁的每一句，都要能在本篇論文頁或證據表找到；不得在概念頁寫出論文頁沒有的數字或斷言。
* 概念頁其他段落若因本篇而需要改寫（例如定義範圍擴大），依 `wiki-content-audit` 修改，並檢查有沒有把既有錯誤擴散（`wiki-content-audit`「頁面間的傳播」）。
* 概念頁的 `verification` 不因加入一條而自動維持；新加的內容未經核對時，概念頁 `verification` 改為 `partial`（原為 `verified` 時），在交付說明寫明。

### 3. 新建概念頁（只在第一節第 3 點成立時）

檔名 `wiki/concepts/<英文小寫連字號 slug>.md`，骨架：

```markdown
---
title: "<英文名稱>"
title_zh: "<中文名稱>"
domain: "<六值擇一>"
domain_tags: ["#<白名單標籤>"]
papers: ["<slug>"]
related_concepts: ["<只能列已存在之概念頁 slug>"]
verification: "unverified"
---

# 概念：<中文名稱> (<英文名稱>)

> 領域：`#<標籤>` `#<標籤>`

---

## 核心定義
<兩至四句，附出處>

---

## 關鍵突破支柱
* **<……>**
  * 詳見核心論文：[<……>](../papers/<slug>.md)

---

## 跨學科交會與延伸
<一至三點；屬 Wiki 詮釋者標明>

---

## 關聯概念網絡
* [<相關概念中文名>](<相關概念 slug>.md)
```

新建後：在 `wiki/index.md` 第五節加一行（本檔第三節第 3 點）；`related_concepts` 列到的概念頁，其 `related_concepts` 也加回本概念（雙向）。

## 三、登記 `wiki/index.md`

### 1. 放在哪一區段

| 論文 | 區段 | 排序 |
|---|---|---|
| 群星，`timeline_year` 為 2026、2025、2024 | 「一、2026 年諾貝爾獎與重大突破」、「二、2025 年……」、「三、2024 年……」中年份相同者 | 區段內依 `timeline_year` 由新到舊；同年者加在該年最後一條之後 |
| 群星，`timeline_year` 為 2023 | 「三、2024 年諾貝爾獎與重大突破」之末（目前慣例） | 同上 |
| 群星，`timeline_year` 為 2022 以前 | 「四、歷史重大奠基支柱」 | 由新到舊 |
| 我的關注 | 「六、個人核心關注研究」 | 依 `paper_year` 由新到舊 |
| `timeline_year` 晚於所有既有區段（例如 2027） | 停下來問使用者要新增區段還是放入既有區段；不得自行重排區段編號 | — |

原本已有 `[planned]` 條目者（例如待收錄之諾貝爾獎題目）：**改寫該條目**，不要另加一條。

### 2. 條目格式（與既有條目一致）

群星、有獎項：

```markdown
* `<timeline_year>` ｜ [<title_zh>](papers/<slug>.md) ｜ `#<標籤>` `#<標籤>` ｜ *<paper_year> 發表 ｜ <award_year> <獎項全名>* ｜ `[wiki]`
  * 得獎者：<laureates>。原始文獻：`raw/<檔名>.pdf`（<第一作者> et al. (<年份>) *<期刊>* <卷>(<期>):<頁>，https://doi.org/<DOI>）。
```

群星、無獎項：同上，刪去 `*…*` 一段與「得獎者：」。

我的關注：

```markdown
* `<paper_year>` ｜ [<title_zh>](papers/<slug>.md) ｜ `#<標籤>` `#<標籤>` ｜ *<期刊或會議簡稱與年份，學位論文寫「<年份> 海大碩士論文」之類>* ｜ `[wiki]`
  * 原始文獻：`raw/my-focus/<子資料夾>/<檔名>.pdf`（<作者> (<年份>) <發表處>, <頁>）。
```

* 標籤與論文頁 `domain_tags` 相同、順序相同。
* 狀態標 `[wiki]`；`[published]` 只在正式論文頁產出後使用。

### 3. 新概念頁

在「五、跨領域概念頁」加一行：

```markdown
* [<title_zh>](concepts/<slug>.md) ｜ `#<標籤>` `#<標籤>`
```

## 四、完成條件

1. `python .agents/skills/paper-pipeline/scripts/pipeline_status.py <slug>`：S5 為 OK。
2. `python .agents/skills/wiki-content-audit/scripts/lint_wiki.py`：沒有「雙向對應」、「孤島頁」、「連結失效」之 ERROR 或 WARN 指向本篇或你改過的概念頁。
3. 首頁是否多了連線，在 S9 重建首頁後於星圖上目視確認（`publish.md` 第三節）。
