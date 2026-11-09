---
name: paper-card-writer
description: >-
  Write the text and diagram for every Epoch-Kairos paper card: the homepage cover card (card wall and paper-page Card 1) and the paper-page Cards 2-6, stored as wiki/cards/<slug>.md. Use whenever a paper is ingested, when backfilling or revising card files, or when card_line, hook-derived lead text or Card 3 diagrams change. Every field has hard length limits, source rules and a mandatory check script; do not skip steps.
---

# Paper Card Writer（論文卡片撰寫規範）

本 Skill 規範一篇論文在網站上所有「卡片」的文字與示意圖：首頁卡片牆的封面卡、論文頁 Card 1（封面）與 Card 2 至 6（內頁）。卡片的版面、配色與字體由 [`DESIGN.md`](../../../DESIGN.md) 決定，本 Skill 只管**卡片上寫什麼、從哪裡來、寫多長、怎麼檢查**。

> 寫這份規範的原因：卡片是讀者最先看到、也最常被截圖分享的內容，又是 41 篇以上逐篇手寫的工作，最容易被偷工。過去已出現的問題包括：為了填滿版面硬湊數字、把後續他人成果寫成本篇成果、整段照抄長文塞不進卡片、批次作業時把前一篇的語言名或數字帶進下一篇。本 Skill 的每一條規則都對應這類問題，**不得以「大致符合」為由省略任何一步**。

## 一、適用時機

1. **收錄新論文**（`AGENTS.md` 第六章 Ingest）：論文頁與證據表完成、`lint_wiki.py` 無 ERROR 之後，同一輪內撰寫卡片文字檔。
2. **回填既有論文**：為尚無 `wiki/cards/<slug>.md` 的論文補寫（見 `wiki/todo.md`）。
3. **修訂**：論文頁內容、證據表、`card_line`、`title_zh`、獎項或 `wiki/issues.md` 之修正影響到卡片時，同步修訂卡片文字檔。
4. 不適用：卡片版面、配色、字體的設計討論（屬 `DESIGN.md`）；論文頁長文的撰寫（屬 [`wiki-content-audit`](../wiki-content-audit/SKILL.md)）。

## 二、硬規則（任何一條違反即不得交付）

1. **先有證據表才寫卡片**。`wiki/evidence/<slug>.md` 不存在、或論文頁 `verification` 為 `issues` 且問題影響要寫的內容時，先依 `wiki-content-audit` 補齊或修正，再寫卡片。檢查腳本在缺證據表時直接報 ERROR。
2. **卡片不得出現論文頁與證據表都沒有的事實**。卡片只做「挑選、濃縮、改寫成白話」，不新增數字、年份、人名、機制、因果或評價。改寫後的意思不得比來源更強。
3. **數字只能來自證據表**。Card 4 的每個數字都要在證據表找得到，並寫出第一手來源的頁、表或圖；不得四捨五入到與原文不同的精度，不得把「約」拿掉，也不得自行加上「約」。
4. **公式只能抄自論文頁**。Card 3 的公式必須與論文頁某一條區塊公式（或 `aligned` 中的某一行）逐字相同；論文頁沒有公式時，先依 `wiki-content-audit` 在論文頁補上有出處的公式，再寫卡片。
5. **每篇 Card 3 都必須有示意圖**（2026-11-09 使用者決定），且圖要畫出 Card 3 所講的機制，不得用與內容無關的裝飾圖、不得假裝成數據圖。規格見 [`references/diagram.md`](references/diagram.md)。
6. **歸屬分清楚**。Card 4 只放本篇研究結果（或明確標示的「依原文數據計算」）；後續他人成果只能放 Card 5，且每筆都要有出處；獎項只能用 Frontmatter 的 `honor` 與 `award_year`。作者與得獎者不混寫。
7. **每個欄位都有字數上限**，上限依卡片在手機 330px 寬時不爆版計算，不得以「桌面放得下」為由超過。字數計法見 [`references/style.md`](references/style.md) 第一節。
8. **放不下就換內容，不得硬改事實**。字數超過時，改寫說明、換一個數字或換一個里程碑；不得為了縮短而刪掉語言方向、指標名稱、資料集、條件或限定語。
9. **一篇一篇寫，每篇重開來源**。批次回填時，每寫一篇都重新讀該篇的論文頁與證據表，不得從前一篇的卡片檔複製再改字；寫完立刻跑檢查腳本。
10. **檢查腳本的 ERROR 必須全部排除**才可交付；WARN 須逐條判斷並在交付說明交代處理方式。
11. **不得修改 `raw/`**；需要原文時只讀（`AGENTS.md` 第五章）。
12. **全檔禁止 Emoji、驚嘆號與評價形容詞**（開創性、顛覆性、革命性、劃時代等，完整清單見 `references/style.md`）。
13. **我的關注（`my_focus: true`）論文的 Card 6 不得透露使用者碩論的題目、資料或結果**（`DESIGN.md` 第八章第 13 項），只能連結到公開的研究方向（概念頁名稱）。

## 三、開工前必讀（每次都要讀，不得憑記憶）

| 檔案 | 讀什麼 |
|---|---|
| `AGENTS.md` 第三章、第七章第 1、3、4 節 | LaTeX 規範、Frontmatter 欄位、`card_line` 規則、六張卡節奏、證據表格式 |
| `DESIGN.md` 第二章第 3 節、第五章 | 封面卡 F 版型、論文頁版面與卡組丁 |
| 本 Skill 全部 `references/` | 各卡欄位、字數、範例與反例 |
| `wiki/papers/<slug>.md` 全文 | 卡片內容的唯一文字來源 |
| `wiki/evidence/<slug>.md` 全文 | 數字與強斷言的唯一依據 |
| `wiki/issues.md` 中本頁條目 | 是否有尚未修正的問題影響卡片 |
| 範例 `wiki/cards/1982-hopfield-network.md` | 完整格式範例；只看格式，**內容不得套用到其他論文** |

## 四、卡片總覽

| 卡片 | 用途（讀者要得到什麼） | 內容來源 | 細則 |
|---|---|---|---|
| 封面卡（卡片牆）與 Card 1 時代銘文 | 一眼知道這篇做了什麼 | Frontmatter：`card_line`、`title_zh`、`domain`、`domain_tags`、年份與獎項；卡片檔：封面斷行、導語 | [`references/cover.md`](references/cover.md) |
| Card 2 世紀瓶頸 | 這篇之前大家卡在哪裡 | 論文頁 Card 2 | [`references/card-02-dilemma.md`](references/card-02-dilemma.md) |
| Card 3 突破原理 | 這篇怎麼解決（機制＋公式＋示意圖） | 論文頁 Card 3 與其公式 | [`references/card-03-secret.md`](references/card-03-secret.md)、[`references/diagram.md`](references/diagram.md) |
| Card 4 決定性數據 | 證明它有效的關鍵數字（或結論） | 證據表中「本篇研究結果」 | [`references/card-04-evidence.md`](references/card-04-evidence.md) |
| Card 5 典範轉移 | 之後發生了什麼 | 論文頁 Card 4「後續」與 Card 5、Frontmatter 獎項 | [`references/card-05-revolution.md`](references/card-05-revolution.md) |
| Card 6 Kairos | 跨領域的一句啟發 | 論文頁 Card 6 | [`references/card-06-kairos.md`](references/card-06-kairos.md) |

檔案格式（區段、欄位名稱、分隔符號、公式與 SVG 寫法）見 [`references/file-format.md`](references/file-format.md)；用字、標點、字數計法與禁用詞見 [`references/style.md`](references/style.md)。

## 五、作業流程

每篇論文依序完成下列步驟，不得跳步或合併：

1. **預檢**：依 `git-sync-guardian` 執行 `git fetch origin main` 並確認狀態。確認 `wiki/papers/<slug>.md` 與 `wiki/evidence/<slug>.md` 都存在，且 `python .agents/skills/wiki-content-audit/scripts/lint_wiki.py` 對本頁無 ERROR。
2. **通讀來源**：完整讀論文頁與證據表（不得只讀 Card 段落）。寫下一句話回答「這篇做了什麼、怎麼做、證據是什麼、限制是什麼」，作為後續每張卡的對照基準（不需存檔）。
3. **建立素材對照**：逐張卡列出準備使用的句子或數字，以及它在論文頁或證據表的位置。找不到位置的素材一律捨棄。
4. **撰寫卡片檔**：依 `references/file-format.md` 建立 `wiki/cards/<slug>.md`，依序寫封面、Card 2 至 6。每寫完一張卡，就對照該卡細則的「自我檢查」清單核一次。
5. **繪製 Card 3 示意圖**：依 `references/diagram.md` 先寫「圖要表達的一句話」，再畫圖；畫完逐項核對圖的規則。
6. **跑檢查腳本**：`python .agents/skills/paper-card-writer/scripts/check_cards.py <slug>`。ERROR 全部修正後重跑，直到 ERROR 為 0；WARN 逐條判斷。
7. **兩階段複核**（沿用 `wiki-content-audit` 的「先宏觀、再微觀」）：
   * **宏觀**：只看六張卡，問自己：讀者看完得到的印象，是否和論文摘要與結論一致？有沒有哪張卡比原文更誇張？Card 4 與 Card 5 的歸屬是否分清？
   * **微觀**：每個欄位對回素材對照，確認數字、方向、指標、條件逐字正確；再做吸引子檢查（本 Skill 第六節）。
8. **交付與提交**：依本 Skill 第八節交代結果，依 `AGENTS.md` 第六章寫日誌，依 `git-sync-guardian` 以 `safe_commit_push.sh` 提交卡片檔與日誌。

## 六、卡片專屬的吸引子檢查

除 `wiki-content-audit` 的吸引子表外，卡片特別容易出現下列問題，微觀複核時逐項檢查：

| 類型 | 典型表現 | 怎麼查 |
|---|---|---|
| 版型填空 | Card 4 一定要湊四個大數字；Card 5 一定要寫成「改變世界」；Card 6 一定要有金句 | 原文只有兩個硬數字就放兩個；理論論文改用結論模式；沒有後續成果就只放獎項與實際存在的後續研究 |
| 套模板 | 每篇 Card 2 結語都是「缺的是……」、每篇 Card 5 標題都是「從 A 到 B」 | 檢查腳本會對跨檔重複句型報 WARN；換成貼合本篇的寫法 |
| 鄰近內容 | 批次時把前一篇的語言、資料集、指標或年份帶進來 | 每個專名回本篇論文頁搜尋，搜不到即錯 |
| 白話失真 | 為了白話把「在 30 個神經元的模擬中」寫成「實驗中」，把「某語→中文」寫成「翻譯」 | 條件與方向不可省略；放不下就換說明方式 |
| 示意圖造假 | 為了好看畫出看似數據的曲線、刻度或柱狀高低 | 示意圖不得有刻度與數值；要畫數據就必須標為數據圖並附圖表出處 |
| 誇飾 | 「首次」、「證明」、「徹底解決」、「所有」 | 搜尋這些詞，證據表沒有同等強度的支持就改寫 |

## 七、批次回填規則

1. 一次只處理一篇，該篇完成步驟 1 至 7 後才開始下一篇。
2. 每篇單獨跑檢查腳本並記錄結果；不得最後一次跑完全部再回頭修。
3. 同一批次每完成五篇，重讀本 Skill 第二節與 `references/style.md` 一次，防止規則在長時間作業中被淡忘。
4. 同一批次中，Card 2 標題、Card 5 標題與 Card 6 結語不得出現相同句型（檢查腳本會提示）。
5. 中途停止時，把已完成與未完成的篇目登記在 `wiki/todo.md`，不得留下半寫的卡片檔而不交代。

## 八、交付說明（每篇都要）

交付訊息與日誌須包含：

* 寫了哪一篇、檔案路徑。
* 檢查腳本結果（ERROR 數、WARN 數），以及每條 WARN 的處理方式。
* 各卡使用的來源位置摘要（例如「Card 4 四個數字取自證據表第 8、9、10 列」）。
* 宏觀與微觀複核發現並修正了什麼；沒有發現時寫明檢查範圍。
* 未決事項（例如原文缺少某數字、示意圖無法簡化等），不以假設補齊。

日誌動作取 `ingest`（隨新論文收錄）或 `update`（回填、修訂），領域標籤取該論文之 `domain_tags`；跨多篇時填 `全域`（`AGENTS.md` 第六章）。

## 九、檢查腳本

`python .agents/skills/paper-card-writer/scripts/check_cards.py [slug ...]`（Python 3.7 以上、只用標準函式庫，於倉庫根目錄執行）：

* 不帶參數時檢查 `wiki/cards/` 全部檔案；`--missing` 另列出尚無卡片檔的論文。
* 檢查項目：區段與欄位是否齊全且依序、每個欄位的字數上限、封面斷行與 `card_line` 是否一致、`title_zh` 短名與導語長度、禁用詞與 Emoji、半形標點、Card 3 公式是否逐字出自論文頁、示意圖 SVG 的元素與屬性白名單與標籤、Card 4 數字是否出現在證據表且附來源位置、Card 5 年份順序與出處作者是否出現在論文頁、我的關注之研究類型欄位、跨檔重複句。
* ERROR 須修正；WARN 為啟發式提醒，須人工判斷。腳本只能檢查形式與可機械比對的部分，**不能代替第五節第 7 步的人工複核**。

## 十、與其他規範的關係

* 規範衝突時的優先順序：`AGENTS.md` > `DESIGN.md` > 本 Skill。發現衝突時不得自行選邊，登記於 `wiki/todo.md`（範圍 `skill`）並告知使用者。
* `card_line` 的基本規則以 `AGENTS.md` 第七章第 1 節為準，本 Skill 的 `references/cover.md` 為補充細則，不得放寬。
* 證據表的建立與查核依 `wiki-content-audit`；本 Skill 只使用證據表，不另立證據格式。
* 修改本 Skill 時只改本正本，`.claude/skills/paper-card-writer/SKILL.md` 為轉介檔，不寫規則（`AGENTS.md` 第六章）。
