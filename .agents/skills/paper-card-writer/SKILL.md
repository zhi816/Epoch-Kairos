---
name: paper-card-writer
description: >-
  Write the text and diagram for every Epoch-Kairos paper card: the homepage cover card (card wall and paper-page Card 1) and the paper-page Cards 2-6, stored as wiki/cards/<slug>.md, then build and browser-verify both the paper page and the homepage card wall. Use whenever a paper is ingested, when backfilling or revising card files, or when card_line, hook-derived lead text or Card 3 diagrams change. Every field has hard length limits, source rules and mandatory check scripts; do not skip steps.
---

# Paper Card Writer（論文卡片撰寫規範）

本 Skill 規範一篇論文在網站上所有「卡片」的文字與示意圖：首頁卡片牆的封面卡、論文頁 Card 1（封面）與 Card 2 至 6（內頁）。卡片的版面、配色與字體由 [`DESIGN.md`](../../../DESIGN.md) 決定，本 Skill 只管**卡片上寫什麼、從哪裡來、寫多長、怎麼檢查**，以及寫完後如何把它建成論文頁、放上首頁卡片牆並驗證。**一篇卡片的完整流程，是卡片檔、論文頁與首頁卡片牆三者都完成、驗證並提交**；只完成其中一部分不算完成。

> 寫這份規範的原因：卡片是讀者最先看到、也最常被截圖分享的內容，又是 41 篇以上逐篇手寫的工作，最容易被偷工。過去已出現的問題包括：為了填滿版面硬湊數字、把後續他人成果寫成本篇成果、整段照抄長文塞不進卡片、批次作業時把前一篇的語言名或數字帶進下一篇。本 Skill 的每一條規則都對應這類問題，**不得以「大致符合」為由省略任何一步**。

## 一、適用時機

1. **收錄新論文**（`AGENTS.md` 第六章 Ingest）：論文頁與證據表完成、`lint_wiki.py` 無 ERROR 之後，同一輪內撰寫卡片文字檔。收錄的整體順序依 [`paper-pipeline`](../paper-pipeline/SKILL.md)：本 Skill 是其 S7（卡片檔）、S8（論文頁網頁）與 S9（卡片牆部分）；星圖或我的星系之上架驗證與整篇提交清單見該 Skill 之 `references/publish.md`。
2. **回填既有論文**：為尚無 `wiki/cards/<slug>.md` 的論文補寫（見 `wiki/todo.md`）。
3. **修訂**：論文頁內容、證據表、`card_line`、`title_zh`、獎項、`venue_short` 或 `wiki/issues.md` 之修正影響到卡片或論文頁時，同步修訂卡片文字檔，並重新建置與驗證該篇論文頁與首頁卡片牆（第五節第 7 步）。
4. 不適用：卡片版面、配色、字體的設計討論（屬 `DESIGN.md`）；論文頁長文的撰寫（屬 [`wiki-content-audit`](../wiki-content-audit/SKILL.md)）。

## 二、硬規則（任何一條違反即不得交付）

1. **先有證據表才寫卡片**。`wiki/evidence/<slug>.md` 不存在、或論文頁 `verification` 為 `issues` 且問題影響要寫的內容時，先依 `wiki-content-audit` 補齊或修正，再寫卡片。檢查腳本在缺證據表時直接報 ERROR。論文頁標 `verified` 不代表內容正確（2026-11-10 第二批回填時，兩篇標 `verified` 的論文頁回原文查出 13 處不符），仍須依第 17 條抽查。
2. **卡片不得出現論文頁與證據表都沒有的事實**。卡片只做「挑選、濃縮、改寫成白話」，不新增數字、年份、人名、機制、因果或評價。改寫後的意思不得比來源更強。
3. **數字只能來自證據表**。Card 4 的每個數字都要在證據表找得到，並寫出第一手來源的頁、表或圖；不得四捨五入到與原文不同的精度，不得把「約」拿掉，也不得自行加上「約」。
4. **公式只能抄自論文頁**。Card 3 的公式必須與論文頁某一條區塊公式（或 `aligned` 中的某一行）逐字相同。論文頁沒有公式時，回原文確認：原文有表達本篇機制的公式，先依 `wiki-content-audit` 補進論文頁再寫卡片；原文只有評估指標公式、只有資料處理公式（篩選、切分、統計用）或完全沒有公式，才可用無公式模式（`references/card-03-secret.md` 第四節第 5 條）。論文頁的公式本身也要回原文確認出處（式號或頁碼）；不是原文公式（Wiki 自擬的流程式、改過符號或漏項的式子）時不得取用，依 `card-03-secret.md` 第四節第 6 條處理。
5. **每篇 Card 3 都必須有示意圖**（2026-11-09 使用者決定），且圖要畫出 Card 3 所講的機制，不得用與內容無關的裝飾圖、不得假裝成數據圖。規格見 [`references/diagram.md`](references/diagram.md)。
6. **歸屬分清楚**。Card 4 只放本篇研究結果（或明確標示的「依原文數據計算」）；後續他人成果只能放 Card 5，且每筆都要有出處；獎項只能用 Frontmatter 的 `honor` 與 `award_year`。作者與得獎者不混寫。
7. **每個欄位都有字數上限**，上限依卡片在手機 330px 寬時不爆版計算，不得以「桌面放得下」為由超過。字數計法見 [`references/style.md`](references/style.md) 第一節。
8. **放不下就換內容，不得硬改事實**。字數超過時，改寫說明、換一個數字或換一個里程碑；不得為了縮短而刪掉語言方向、指標名稱、資料集、條件或限定語。
9. **一篇一篇寫，每篇重開來源**。批次回填時，每寫一篇都重新讀該篇的論文頁與證據表，不得從前一篇的卡片檔複製再改字；寫完立刻跑檢查腳本。
10. **檢查腳本的 ERROR 必須全部排除**才可交付；WARN 須逐條判斷並在交付說明交代處理方式。
11. **不得修改 `raw/`**；需要原文時只讀（`AGENTS.md` 第五章）。
12. **全檔禁止 Emoji、驚嘆號與評價形容詞**（開創性、顛覆性、革命性、劃時代等，完整清單見 `references/style.md`）。
13. **我的關注（`my_focus: true`）論文的 Card 6 不得透露使用者碩論的題目、資料或結果**（`DESIGN.md` 第八章第 13 項），只能連結到公開的研究方向（概念頁名稱）。
14. **每篇都要建出論文頁、放上首頁卡片牆，兩者都要驗證**（第五節第 7 步，細則見 [`references/paper-page.md`](references/paper-page.md) 與 [`references/card-wall.md`](references/card-wall.md)）：論文頁建置自我檢查與卡片牆自我檢查 ERROR 皆為 0；有瀏覽器工具時，`verify_page.js` 與 `verify_wall.js` 結果皆須為 PASS。沒有實際執行就不得宣稱已驗證。`web/index.html` 只能由 `python tools/build_home.py` 產生，不得手改。
15. **不得改檢查工具去遷就內容**：撰寫卡片時不得修改 `check_cards.py`、`tools/build_paper_prototype.py`、`tools/paper_template.html`、`verify_page.js`、`tools/build_home.py`、`tools/home_template.html`、`web/assets/css/starmap.css`、`web/assets/js/starmap.js`、`verify_wall.js`、本 Skill 的 `references/` 與兩份範例卡片檔，也不得調高門檻或加例外。認為工具誤判時，登記 `wiki/todo.md`（範圍 `skill`）並告知使用者，該篇維持未交付。
16. **不得為了讓卡片過關而改來源**：論文頁、證據表、`card_line`、`title_zh` 只能依 `wiki-content-audit`（或 `AGENTS.md` 對應規則）修改，且修改本身須有第一手來源支持並在交付說明交代。第 4 條「論文頁沒有公式時先補公式」也必須走 `wiki-content-audit`：公式要有原文頁碼與式號、登記於證據表。不得未經這套流程，就為了讓 Card 3 公式比對通過而在論文頁加公式，或為了讓 Card 4 數字通過而在證據表加列。
17. **寫卡片前回原文抽查**（2026-11-10 起）：Card 3 公式、Card 4 每個數字、Card 5 每筆里程碑的出處，都要親自打開第一手來源（`raw/` 原文 PDF、補充資料、後續研究的 DOI 或正式頁面）確認一次，並把抽查紀錄貼進交付說明（第八節第 4 項）。只信論文頁、證據表或 `verified` 標記而沒有抽查，不得交付。抽查發現不符時依第五節第 2-1 步處理，不得改寫卡片去遷就錯的論文頁。

## 三、開工前必讀（每次都要讀，不得憑記憶）

| 檔案 | 讀什麼 |
|---|---|
| `AGENTS.md` 第三章、第七章第 1、3、4 節 | LaTeX 規範、Frontmatter 欄位、`card_line` 規則、六張卡節奏、證據表格式 |
| `DESIGN.md` 第二章第 3 節、第五章 | 封面卡 F 版型、論文頁版面與卡組丁 |
| 本 Skill 全部 `references/`（共 11 份，含 `paper-page.md` 與 `card-wall.md`） | 各卡欄位、字數、範例與反例；論文頁與首頁卡片牆如何產生與驗證 |
| `wiki/papers/<slug>.md` 全文 | 卡片內容的唯一文字來源 |
| `wiki/evidence/<slug>.md` 全文 | 數字與強斷言的唯一依據 |
| `wiki/issues.md` 中本頁條目 | 是否有尚未修正的問題影響卡片 |
| 範例 `wiki/cards/1982-hopfield-network.md`（群星）、`wiki/cards/2021-seediq-chinese-mt-you.md`（我的關注） | 完整格式範例；只看格式，**內容不得套用到其他論文** |
| 參考網頁 `web/papers/1982-hopfield-network/index.html`、`2021-seediq-chinese-mt-you/index.html` | 上述兩份卡片檔實際做成論文頁的樣子（`python tools/build_paper_prototype.py <slug>` 產生）。開工前在瀏覽器打開看過，知道每個欄位最後出現在哪裡、多大；寫完自己那篇**必須**用同一指令建置並驗證（第五節第 7 步） |
| 首頁 `web/index.html` 下方「群星檔案」與 `#my-constellation`「我的星系檔案」 | 封面卡在首頁卡片牆上的樣子（桌面 3 欄、手機 2 欄，比論文頁 Card 1 小）。開工前以本機伺服器打開看過；寫完自己那篇**必須**以 `python tools/build_home.py --card <slug>` 放上牆並驗證（第五節第 7 步） |

## 四、卡片總覽

| 卡片 | 用途（讀者要得到什麼） | 內容來源 | 細則 |
|---|---|---|---|
| 封面卡（卡片牆）與 Card 1 時代銘文 | 一眼知道這篇做了什麼 | Frontmatter：`card_line`、`title_zh`、`domain`、`domain_tags`、年份與獎項；卡片檔：封面斷行、導語 | [`references/cover.md`](references/cover.md)；上牆與驗證見 [`references/card-wall.md`](references/card-wall.md) |
| Card 2 世紀瓶頸 | 這篇之前大家卡在哪裡 | 論文頁 Card 2 | [`references/card-02-dilemma.md`](references/card-02-dilemma.md) |
| Card 3 突破原理 | 這篇怎麼解決（機制＋公式＋示意圖） | 論文頁 Card 3 與其公式 | [`references/card-03-secret.md`](references/card-03-secret.md)、[`references/diagram.md`](references/diagram.md) |
| Card 4 決定性數據 | 證明它有效的關鍵數字（或結論） | 證據表中「本篇研究結果」 | [`references/card-04-evidence.md`](references/card-04-evidence.md) |
| Card 5 典範轉移 | 之後發生了什麼 | 論文頁 Card 4「後續」與 Card 5、Frontmatter 獎項 | [`references/card-05-revolution.md`](references/card-05-revolution.md) |
| Card 6 Kairos | 跨領域的一句啟發 | 論文頁 Card 6 | [`references/card-06-kairos.md`](references/card-06-kairos.md) |

檔案格式（區段、欄位名稱、分隔符號、公式與 SVG 寫法）見 [`references/file-format.md`](references/file-format.md)；用字、標點、字數計法與禁用詞見 [`references/style.md`](references/style.md)。

## 五、作業流程

每篇論文依序完成下列步驟，不得跳步或合併：

1. **預檢**：依 `git-sync-guardian` 執行 `git fetch origin main` 並確認狀態。確認 `wiki/papers/<slug>.md` 與 `wiki/evidence/<slug>.md` 都存在，且 `python .agents/skills/wiki-content-audit/scripts/lint_wiki.py` 對本頁無 ERROR。查 `wiki/issues.md` 中本頁之 `open` 條目，逐條判斷是否影響要寫的內容，結論寫進交付說明。
2. **通讀來源**：完整讀論文頁與證據表（不得只讀 Card 段落）。寫下四句話分別回答「這篇做了什麼、怎麼做、證據是什麼、限制是什麼」，每句附論文頁段落或證據表列位置，**寫進交付說明**（第八節第 2 項）。這四句是後續每張卡的對照基準；寫不出限制，代表還沒讀完。
   * **2-1 回原文抽查**（第二節第 17 條）：先選定 Card 3 要用的公式、Card 4 要用的數字、Card 5 要用的里程碑，再逐項打開第一手來源確認：
     * 公式：在原文（或補充資料）找到同一條式子，記下式號與頁碼，確認符號、各項與條件相同。
     * 數字：在原文的表、圖或正文找到同一個值，記下頁碼與表列、欄位名稱（例如「Table 2，NLLB 54B 列，AVERAGE 欄」），確認語言方向、指標、資料集、基線與「約」相同；同一篇有預印本與正式版時，以論文頁 `doi_url` 指向之版本為準。
     * 里程碑：打開該後續研究的 DOI 或正式頁面，確認作者、年份、發表處，以及卡片要寫的那件事確實是它做的；新論文模式的「本篇」列，在原文找到對應的節或頁。
     * 新論文模式另查：原文公開的資料、程式或模型，作者明列的限制與未來工作，論文頁是否都有記載；原文有而論文頁沒有時，視同論文頁有缺漏。
     * **全部相符**：把抽查紀錄寫進交付說明，繼續第 3 步。
     * **發現不符或缺漏**：不得改寫卡片去遷就錯的論文頁，也不得自行在卡片寫上正確值而不改來源。依 `wiki-content-audit` 修正論文頁與證據表，並在 `wiki/issues.md` 登記（含已當場修正者），修正後重跑 `lint_wiki.py`，再從第 1 步重新開始。`wiki/todo.md` 之平行批次協調規則禁止修改論文頁時，停下該篇，在最後回報寫明檔案、行號、原文位置與原文數值，由協調者處理。
3. **建立素材對照**：逐張卡、逐欄位列出準備使用的句子或數字，以及它在論文頁（段落標題＋第幾點或第幾段）或證據表（第幾列）的位置。找不到位置的素材一律捨棄。素材對照表**寫進交付說明**（第八節第 3 項），不得事後補寫。
4. **撰寫卡片檔**：依 `references/file-format.md` 建立 `wiki/cards/<slug>.md`，依序寫封面、Card 2 至 6。每寫完一張卡，就對照該卡細則的「自我檢查」清單核一次。
5. **繪製 Card 3 示意圖**：依 `references/diagram.md` 先寫「圖要表達的一句話」，再畫圖；畫完逐項核對圖的規則。
6. **跑檢查腳本**：`python .agents/skills/paper-card-writer/scripts/check_cards.py <slug>`。ERROR 全部修正後重跑，直到 ERROR 為 0；WARN 逐條判斷，每條都要寫出判斷依據（例如「『證明』一詞：證據表第 3 列，原文 p. 2556 寫 "we show"，保留」），不得只寫「可接受」。
7. **建置論文頁與首頁卡片牆，並驗證**（兩部分都要做，依序進行）：
   * **7-1 論文頁**（細則見 [`references/paper-page.md`](references/paper-page.md)）：
     * `python tools/build_paper_prototype.py <slug>`：自我檢查 ERROR 須為 0，WARN 依 `paper-page.md` 第七節處理。
     * 有瀏覽器工具時：以本機伺服器開啟該頁，執行 `scripts/verify_page.js`，結果須為 PASS；再依 `paper-page.md` 第六節第 3 步目視與操作檢查。
     * 沒有瀏覽器工具時：交付說明與日誌寫明「未以瀏覽器驗證」，並登記 `wiki/todo.md`（`paper-page.md` 第六節第 2 步）。
   * **7-2 首頁卡片牆**（細則見 [`references/card-wall.md`](references/card-wall.md)，7-1 通過後才做）：
     * 先同步遠端（`card-wall.md` 第四節第 1 步），再執行 `python tools/build_home.py --card <slug>`：輸出清單中須有本篇一行、斷行與卡片檔相同，「卡片牆自我檢查：ERROR 0」；再以 `python tools/build_home.py --check --card <slug>` 確認一致。
     * 有瀏覽器工具時：開首頁 `index.html`，先執行 `var EK_SLUG = '<slug>';` 再執行 `scripts/verify_wall.js`，結果須為「結果：PASS（首頁卡片牆，指定 <slug>）」；再依 `card-wall.md` 第四節第 4 步目視與操作檢查。
     * 沒有瀏覽器工具時：同 7-1，寫明首頁卡片牆未以瀏覽器驗證並登記待補驗（`card-wall.md` 第四節第 3 步）。
     * 平行批次中 `wiki/todo.md` 之協調規則禁止重建首頁時，略過 7-2，交付說明寫明「首頁卡片牆：依協調規則未重建，由協調者處理」（`card-wall.md` 第五節）。
   * 驗證發現問題而修改卡片檔後，從第 6 步重跑，7-1 與 7-2 都要重做。
8. **兩階段複核**（沿用 `wiki-content-audit` 的「先宏觀、再微觀」）：
   * **宏觀**：只看建好的網頁上的六張卡，問自己：讀者看完得到的印象，是否和論文摘要與結論一致？有沒有哪張卡比原文更誇張？Card 4 與 Card 5 的歸屬是否分清？
   * **微觀**：每個欄位對回素材對照，確認數字、方向、指標、條件逐字正確；再做吸引子檢查（本 Skill 第六節）與偷工自查（本 Skill 第十一節）。
9. **交付與提交**：依本 Skill 第八節交代結果，依 `AGENTS.md` 第六章寫日誌，依 `git-sync-guardian` 以 `safe_commit_push.py`（Windows）或 `safe_commit_push.sh` 提交卡片檔、該篇論文頁、`web/index.html` 與日誌（略過 7-2 者不列 `web/index.html`）；一篇一個提交。推送後不加 `--card` 執行 `python tools/build_home.py --check`，須為「一致」（`card-wall.md` 第四節第 5 步，含 `web/index.html` 衝突時之處理）。

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

1. 一次只處理一篇，該篇完成步驟 1 至 9（含提交）後才開始下一篇。一篇一個提交、一筆日誌，不得把多篇合併成一個提交，讓使用者可以逐篇檢視與退回。
2. 每篇單獨跑檢查腳本、單獨建置與驗證，並記錄結果；不得最後一次跑完全部再回頭修。
3. 同一批次每完成五篇，重讀本 Skill 第二節與 `references/style.md` 一次，防止規則在長時間作業中被淡忘。
4. 同一批次中，Card 2 標題、Card 5 標題與 Card 6 結語不得出現相同句型（檢查腳本會提示）。
5. 中途停止時，把已完成與未完成的篇目登記在 `wiki/todo.md`，不得留下半寫的卡片檔而不交代。
6. 撰寫某一篇時，除兩份範例外不得打開其他論文的卡片檔，避免套用句型或把別篇的專名帶進來。
7. 預估剩餘的工作時間或用量不足以完成一整篇的步驟 1 至 9 時，不開始新的一篇；寧可少寫一篇，也不得為了趕完而省略步驟。
8. 回填多篇時，數量以「做完並通過驗證的篇數」計算；只寫了卡片檔、沒有建置驗證與提交的篇目，不算完成，不得在日誌或 `wiki/todo.md` 標為完成。
9. 多個對話平行回填時，`wiki/todo.md` 該批條目所寫的協調規則（可改哪些檔、問題編號區段、誰重建首頁、停下時怎麼回報）優先於本 Skill 中「登記 `wiki/todo.md`、`wiki/issues.md`」與「重建首頁」等指示。開工前整段讀過；規則沒寫到的情況，照本 Skill 做，並在最後回報寫明。

## 八、交付說明（每篇都要）

交付訊息（給使用者看的回覆）依下列格式逐項填寫，**每一項都要有內容**；某項不適用時寫「不適用」並說明原因，不得刪項：

```markdown
### <slug> 卡片交付

1. 檔案：wiki/cards/<slug>.md、web/papers/<slug>/index.html、web/index.html（提交 <commit>；略過 7-2 者寫明原因）
2. 四句對照基準（第五節第 2 步）：
   - 做了什麼：……（論文頁 Card 1 第 1 段）
   - 怎麼做：……（論文頁 Card 3 第 2 點）
   - 證據：……（證據表第 4、5 列）
   - 限制：……（論文頁 Card 4 第 3 點）
3. 素材對照（第五節第 3 步）：
   | 卡片 | 欄位 | 卡片上的文字或數字 | 來源位置 |
   |---|---|---|---|
   | 封面 | 導語 | …… | hook；論文頁 Card 1 第 2 段 |
   | Card 2 | 對照 1 | …… | 論文頁 Card 2 第 1 點 |
   （每個欄位一列，Card 4 數字與 Card 5 里程碑逐筆列出）
4. 原文抽查（第五節第 2-1 步）：
   | 卡片 | 項目 | 卡片上的公式、數字或出處 | 第一手來源位置 | 原文所見 | 結果 |
   |---|---|---|---|---|---|
   | Card 3 | 公式 | …… | 原文式 (N)，p. N | 符號與各項相同 | 相符 |
   | Card 4 | 數字 1 | …… | 表 N，p. N，「<列名>」列「<欄名>」欄 | 原文該格之值 | 相符 |
   | Card 5 | 里程碑 1 | <作者> <年份> | doi:…… | 作者、年份、發表處；卡片所寫之事在該文何處 | 相符 |
   （每個公式、數字、里程碑一列；「原文所見」寫你在來源上實際看到的值或內容，不得照抄證據表；不符者寫明如何處理與登記之 EK 編號）
5. check_cards.py：ERROR 0、WARN n；逐條 WARN 與判斷依據
6. 建置自我檢查：
   - 論文頁：貼上 build_paper_prototype.py 輸出最後兩行；逐條 WARN 與處理
   - 卡片牆：貼上 build_home.py --card <slug> 輸出全文（含本篇一行與「卡片牆自我檢查」一行）；推送後 build_home.py --check 之最後一行
7. 瀏覽器驗證：
   - 論文頁：貼上 verify_page.js 報告全文
   - 卡片牆：貼上 verify_wall.js 報告全文（EK_SLUG 設為本篇）；逐條 WARN 依 card-wall.md 第六節之處理
   - 或「未以瀏覽器驗證（無瀏覽器工具），已登記 TD-NNN」
8. 目視與操作檢查：paper-page.md 第六節第 3 步十二項、card-wall.md 第四節第 4 步八項，逐項寫「通過」或發現的問題
9. 複核：宏觀與微觀各發現並修正了什麼；沒有發現時寫明看了哪些
10. 本頁問題（wiki/issues.md）：撰寫前之 open 條目逐條寫是否影響卡片；本次修正或新登記之 EK 編號；論文頁最後之 verification
11. 未決事項：原文缺少的數字、無法簡化的示意圖、工具疑似誤判等，不以假設補齊
```

日誌條目精簡為：檔案、各檢查之結果數字（check_cards、論文頁與卡片牆之建置自我檢查、兩支瀏覽器驗證）、各卡來源位置摘要（例如「Card 4 四個數字取自證據表第 8、9、10 列」）、複核發現、未決事項。素材對照表全文只放交付訊息，不寫入日誌。

日誌動作取 `ingest`（隨新論文收錄）或 `update`（回填、修訂），領域標籤取該論文之 `domain_tags`；跨多篇時填 `全域`（`AGENTS.md` 第六章）。

## 九、檢查腳本

`python .agents/skills/paper-card-writer/scripts/check_cards.py [slug ...]`（Python 3.7 以上、只用標準函式庫，於倉庫根目錄執行）：

* 不帶參數時檢查 `wiki/cards/` 全部檔案；`--missing` 另列出尚無卡片檔的論文。
* 檢查項目：區段與欄位是否齊全且依序、每個欄位的字數上限、封面斷行與 `card_line` 是否一致、`title_zh` 短名與導語長度、禁用詞與 Emoji、半形標點、Card 3 公式是否逐字出自論文頁（無公式模式：論文頁確實沒有區塊公式、理由欄格式）、示意圖 SVG 的元素與屬性白名單與標籤、Card 4 數字是否出現在證據表且附來源位置、Card 5 年份順序與出處作者是否出現在論文頁（新論文模式：發表兩年內、本篇列附位置且年份等於發表年、註記寫明出自本篇；一般模式不得全部出自本篇）、我的關注之研究類型欄位、跨檔重複句。
* ERROR 須修正；WARN 為啟發式提醒，須人工判斷。腳本只能檢查形式與可機械比對的部分，**不能代替第五節第 8 步的人工複核**。

`python tools/build_paper_prototype.py [slug ...]`（倉庫根目錄執行）：

* 先跑 `check_cards.py`（ERROR 即中止），再產生 `web/papers/<slug>/index.html`，最後做靜態自我檢查並印出「自我檢查 <slug>：ERROR n、WARN m」；有 ERROR 時結束代碼為 1。不帶參數時建置全部已有卡片檔的論文。
* 自我檢查項目與處理方式見 `references/paper-page.md` 第六、七節。

`scripts/verify_page.js`（瀏覽器執行）：

* 以本機伺服器開啟論文頁後，在 Console 執行全文；以隱藏 iframe 同時量測 1440 x 900 與 375 x 812，輸出逐項 PASS／FAIL／WARN 與「結果：PASS」或「結果：FAIL n 項」。量測項目見 `references/paper-page.md` 第六節第 2 步。
* 只量版面，不判斷內容對錯；PASS 不代表卡片內容正確。

`python tools/build_home.py [--check] [--card <slug> ...]`（倉庫根目錄執行）：

* 重建首頁 `web/index.html`（知識星圖與卡片牆）。卡片牆只收 Git 已提交之卡片檔；自己這篇尚未提交時以 `--card <slug>` 帶入（先跑 `check_cards.py`，ERROR 即中止）。
* 輸出卡片牆清單（編號、slug、封面斷行）、未上牆之卡片檔（INFO）與「卡片牆自我檢查：ERROR n、WARN m」；有 ERROR 時不寫檔、結束代碼為 1。`--check` 只比對不寫檔。細則見 `references/card-wall.md`。

`python .agents/skills/paper-card-writer/scripts/venue_short_lookup.py [slug ...] [--long] [--no-net]`（只用標準函式庫，查 Crossref 需要網路）：

* 列出論文頁目前顯示之期刊簡稱、論文頁資訊欄行數與首頁卡片牆雙年份之截斷風險，以及 Crossref 之 `container-title`、`short-container-title`；`--long` 列出全庫可能被截斷者。只提供候選、不寫檔，採用規則見 `references/paper-page.md` 第三節。

`scripts/verify_wall.js`（瀏覽器執行）：

* 以本機伺服器開啟首頁 `index.html` 後，在 Console 先執行 `var EK_SLUG = '<slug>';` 再執行全文；以隱藏 iframe 量測 1440 x 900 與 375 x 812、群星與我的星系兩種模式，輸出逐項結果與「結果：PASS」或「結果：FAIL n 項」。量測項目見 `references/card-wall.md` 第四節第 3 步。
* 同樣只量版面與一致性，不判斷內容對錯。

## 十、與其他規範的關係

* 規範衝突時的優先順序：`AGENTS.md` > `DESIGN.md` > 本 Skill。發現衝突時不得自行選邊，登記於 `wiki/todo.md`（範圍 `skill`）並告知使用者。
* `card_line` 的基本規則以 `AGENTS.md` 第七章第 1 節為準，本 Skill 的 `references/cover.md` 為補充細則，不得放寬。
* 證據表的建立與查核依 `wiki-content-audit`；本 Skill 只使用證據表，不另立證據格式。
* 修改本 Skill 時只改本正本，`.claude/skills/paper-card-writer/SKILL.md` 為轉介檔，不寫規則（`AGENTS.md` 第六章）。

## 十一、偷工自查表（交付前逐項核對）

下列是撰寫卡片時最常見的偷工方式。交付前逐項問自己「我有沒有這樣做」，有任何一項就回到對應步驟重做。使用者會依此表抽查。

| 偷工方式 | 為什麼不行 | 對應步驟 |
|---|---|---|
| 只讀論文頁的 Card 段落，沒讀證據表與 `issues.md` | 證據表才是數字與強斷言的依據；`open` 問題可能正好在要寫的地方 | 第五節第 1、2 步 |
| 論文頁標 `verified` 或證據表寫「符合來源」，就不回原文抽查 | 第二批回填時，標 `verified` 的頁面查出數字、版本、公式與後續研究多處不符；證據表也記過「已更正」而頁面沒改 | 第二節第 17 條、第五節第 2-1 步 |
| 抽查紀錄的「原文所見」照抄證據表或論文頁 | 等於沒有抽查；要寫在原文上實際看到的值與位置 | 第八節第 4 項 |
| 發現論文頁與原文不符，只在卡片上寫正確值，論文頁照舊 | 卡片與長文同頁並列，讀者會看到兩個數字；問題也沒人追蹤 | 第五節第 2-1 步 |
| 論文頁的公式找不到原文出處，照樣抄進 Card 3；或因頁面有自擬公式，就不走無公式模式 | 自擬公式等同捏造原文內容；應先依 `wiki-content-audit` 處理論文頁 | `card-03-secret.md` 第四節第 6 條 |
| 先寫卡片，事後才補素材對照表 | 事後補的對照只是替已寫好的句子找藉口，查不出新增或誇大的事實 | 第五節第 3 步 |
| 把範例卡片檔複製過來改字 | 句型、比喻與欄位長度會被帶進來；範例只看格式 | 第二節第 9 條、第七節第 6 條 |
| 把 `hook` 截短當導語、把 `card_line` 加幾個字當導語 | `hook` 多為術語長句；導語要補充 `card_line` 沒說的內容 | `cover.md` 第五節 |
| Card 4 湊滿四個數字 | 原文只有兩個硬數字就放兩個，或改結論模式 | `card-04-evidence.md` 第一節 |
| 數字照抄了，但刪掉條件、方向或「約」 | 改變了原文意思；放不下就換數字或移到範圍欄 | 第二節第 3、8 條 |
| Card 5 寫「影響深遠」之類沒有出處的里程碑 | 每個里程碑都要有出處，出處作者須在論文頁 | `card-05-revolution.md` 第二節 |
| 原文有機制公式，卻嫌麻煩改填「公式：無」 | 無公式模式只給原文確實沒有機制公式的研究；誤用等同捏造來源狀態 | `card-03-secret.md` 第四節第 5 條 |
| 較早的論文沒有後續研究，就套用新論文模式，或把 Wiki 詮釋寫成「作者的下一步」 | 新論文模式只限兩年內；本篇列必須是原文寫了的事並附位置 | `card-05-revolution.md` 第六節 |
| Card 6 寫換到任何一篇都成立的金句 | 必須具體到本篇 | `card-06-kairos.md` 第三節 |
| 示意圖畫成裝飾，或畫出看似數據的曲線刻度 | 示意圖要畫出 Card 3 的機制，不得假裝數據 | `diagram.md` |
| WARN 一律寫「可接受」 | 每條 WARN 都要寫出判斷依據與來源位置 | 第五節第 6 步 |
| 改檢查腳本、模板或門檻讓 ERROR 消失 | 工具是用來抓錯的，不是被修到不抓錯 | 第二節第 15 條 |
| 為了讓檢查通過，在論文頁加公式或在證據表加列 | 來源只能依第一手來源修改 | 第二節第 16 條 |
| 只跑 `check_cards.py`，沒建網頁或沒用瀏覽器驗證 | 版面問題只有建出網頁才看得到 | 第五節第 7 步 |
| 論文頁驗證完就提交，沒有放上首頁卡片牆 | 封面卡在首頁比 Card 1 小，斷行與論文名可能放不下；首頁也不會自己出現這張卡 | 第五節第 7-2 步 |
| 執行 `build_home.py` 沒加 `--card`，卻宣稱已上牆 | 未提交之卡片檔不會上牆；輸出清單裡沒有自己的 slug | `card-wall.md` 第三節 |
| 用 `--card` 帶入別人的卡片檔，或把別人的卡片檔、論文頁一起提交 | 等於替別人交出未完成的工作 | `card-wall.md` 第三節、第七節 |
| 手改 `web/index.html`，或手動合併它的衝突標記 | 首頁是產生檔；衝突時重跑建置即可 | `card-wall.md` 第四節第 5 步 |
| `verify_wall.js` 沒設 `EK_SLUG`，或只驗群星沒驗我的星系 | 無法證明自己的卡片在牆上；腳本一次驗四組，報告要原樣貼上 | `card-wall.md` 第四節第 3 步 |
| 提交時漏了 `web/index.html`，或推送後沒跑 `--check` | 首頁與已提交內容不一致，別人重建時才發現 | 第五節第 9 步 |
| 返回鍵標示與目的地不符，卻在單篇網頁手改標示或自行改模板 | 群星論文應為「回到群星」、我的關注論文應為「回到我的星系」，由模板與建置腳本統一決定；不符是模板問題，登記 `wiki/todo.md` 並告知使用者 | `paper-page.md` 第二節、第七節 |
| 只驗桌面、沒驗手機；或驗證報告改寫成「全部通過」 | `verify_page.js` 一次量兩種尺寸，報告要原樣貼上 | `paper-page.md` 第六節 |
| 沒有實際執行，卻在交付說明寫「已驗證」 | 等同捏造結果 | 第二節第 14 條 |
| 多篇一起寫、一起檢查、一起提交 | 錯誤會互相傳染，使用者也無法逐篇退回 | 第七節第 1、2 條 |
| 用量快用完時加速收尾、省略步驟 | 寧可少寫一篇 | 第七節第 7 條 |
| 交付說明只寫「已完成」，沒有逐項填第八節格式 | 使用者無從檢查 | 第八節 |
