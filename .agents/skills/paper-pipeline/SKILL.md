---
name: paper-pipeline
description: >-
  End-to-end pipeline that turns a new raw/ source into a paper published on the Epoch-Kairos homepage: intake and bibliography check, reading the PDF, evidence table, wiki paper page, concept pages and index, two-stage verification, card file, paper-page prototype, homepage star map or my-constellation plus card wall, log and commit. Use it first whenever a new file appears in raw/, the user asks to ingest or "上架" a paper, or a paper must be brought to completion. For every step it names the skill to follow, the files to produce and the command that proves the step is done; pipeline_status.py shows where each paper stands.
---

# 論文收錄總流程（paper-pipeline）

本 Skill 是**收錄一篇論文的總入口**：從 `raw/` 出現一份新原始檔開始，到這篇論文出現在首頁（群星的星圖或我的星系，以及卡片牆）並提交為止，共 11 個步驟（S0 至 S10）。每一步都寫明：

* **做什麼**、**照哪一份 Skill 的哪一節做**、**產出哪些檔案**；
* **怎麼證明做完了**：要執行的指令與應該看到的輸出；
* **做不下去時怎麼辦**。

各步驟的細則分散在其他 Skill（證據與論文頁在 `wiki-content-audit`，卡片與網頁在 `paper-card-writer`，讀 PDF 在 `paper-pdf-parser`，提交在 `git-sync-guardian`），本 Skill 不重複那些細則，而是規定**先後順序、交接點與完成條件**，並補上其他 Skill 沒有寫的部分：新原始檔怎麼發現與命名（`references/intake.md`）、論文頁的骨架（`references/paper-page-template.md`）、概念頁與索引（`references/concepts-and-index.md`）、上架首頁與提交（`references/publish.md`）。

> 寫這份規範的原因：2026-11-09 至 11-10 的卡片回填中，多篇標為 `verified` 的論文頁回原文查出數字、版本、公式與後續研究的錯誤；卡片、論文頁、首頁也常由不同代理分頭做，漏了其中一段就沒人發現。從原始檔到上架必須是**同一條有檢查點的流程**，每一步都可以用指令確認，不靠記憶與自述。

## 一、什麼時候用

1. 使用者在 `raw/` 放入新的原始檔（PDF），或說「收錄」、「整理這篇」、「上架」。
2. `python .agents/skills/paper-pipeline/scripts/pipeline_status.py --new` 列出尚未收錄的原始檔，而使用者要你處理。
3. 既有論文某一步沒做完（`pipeline_status.py` 該篇有 `NG`），要把它補到完成。
4. 不適用：只改卡片文字（直接用 `paper-card-writer`）、只做事實查核（直接用 `wiki-content-audit` 查核模式）、只翻譯論文（`academic-paper-translator`）。這些工作做完後，仍以 `pipeline_status.py <slug>` 確認沒有把其他步驟弄壞。

## 二、硬規則（任何一條違反即不得交付）

1. **依序做，不跳步**。S0 到 S10 每一步的完成條件達成，才進下一步。某步之前的步驟被修改（例如寫卡片時發現論文頁錯了而回頭修正），從被修改的那一步重新往下做完。
2. **每一步都要有證據**。完成條件裡的指令要實際執行，交付說明貼上輸出（第七節）。沒有實際執行的步驟，不得寫「已完成」或「已驗證」。
3. **一次一篇**。一篇論文從 S0 做到 S10（含提交）後，才開始下一篇。一篇一個提交（`raw/` 倉庫之提交另計，見 `references/publish.md` 第五節）。
4. **`raw/` 唯讀**（`AGENTS.md` 第五章、`raw/AGENTS.md`）：不得改名、覆寫、刪除其中任何檔案。檔名年份錯誤只在 Wiki 層更正並告知使用者。新增原始檔只限使用者自己放入，或使用者明確指示下載；下載不得繞過付費牆或反自動化關卡。
5. **證據先於文字**。先建證據表（S3），再寫論文頁（S4），再寫卡片（S7）。所有數字、公式、強斷言、後續研究都要能在第一手來源找到位置；不得憑記憶補，也不得以 `raw/` 中之中文譯本或 PDF 抽取文字當證據（只能用來搜尋）。
6. **回應被系統安全機制中止時**：立刻停止該篇，不得換句話重試同一內容；在 `wiki/todo.md` 登記（範圍 `wiki`，寫明篇名與停在哪一步），告知使用者，改做下一篇。已知會觸發的主題（例如部分生物醫學論文）由使用者決定由誰處理，`wiki/todo.md` TD-008 列有目前跳過的篇目。
7. **多個對話平行作業時**，`wiki/todo.md` 該批條目寫的協調規則（可改哪些檔、問題編號區段、誰重建首頁、停下時怎麼回報）優先於本 Skill 中相同事項的指示；協調規則沒寫到的，照本 Skill 做。
8. **不得改工具遷就內容**：不得為了讓檢查通過而修改 `pipeline_status.py`、`lint_wiki.py`、`check_cards.py`、建置腳本、範本、驗證腳本或任何 Skill。認為工具誤判時，登記 `wiki/todo.md`（範圍 `skill`）並告知使用者，該篇停在那一步。
9. **共用檔案只提交自己的部分**：`wiki/log.md`、`wiki/issues.md`、`wiki/todo.md`、`web/index.html` 由多人共用，依 `git-sync-guardian` 逐條暫存，不得 `git add -A`。
10. `AGENTS.md` 之全庫規範（無 Emoji、雙年份、標籤白名單、LaTeX、日誌格式、提交必含推送）全部適用。

## 三、開工前必讀（每次開工都要讀，不得憑記憶）

| 檔案 | 讀什麼 |
|---|---|
| `AGENTS.md` | 全文；特別是第五章（三層權限）、第六章（Ingest、Lint、Handoff）、第七章（Frontmatter、證據表、待辦）、第八章（標籤白名單） |
| 本 Skill 與 `references/` 全部 4 份 | 流程、交接點、論文頁骨架、概念頁與索引、上架與提交 |
| `wiki-content-audit` SKILL.md | S3、S4、S6 的方法（證據表、依證據寫作、先宏觀再微觀） |
| `paper-card-writer` SKILL.md 與其 `references/` 全部 11 份 | S7、S8、S9 的方法（卡片、論文頁網頁、卡片牆） |
| `paper-pdf-parser` SKILL.md | S2 抽取 PDF 文字 |
| `git-sync-guardian` SKILL.md | S0 同步、S10 提交 |
| `wiki/todo.md` 全文 | 是否有平行批次的協調規則、這篇是否已被登記或指派給別人 |
| `DESIGN.md` 第二至五章 | 首頁星圖、我的星系、卡片牆與論文頁的樣子（S9 目視時對照） |

## 四、流程總表

| 步驟 | 做什麼 | 照什麼做 | 產出 | 完成條件（指令 → 應見結果） |
|---|---|---|---|---|
| S0 同步與領件 | 同步兩個倉庫；找出要收錄的原始檔；確認沒有別人在做 | `git-sync-guardian`；`references/intake.md` 第一節 | 無 | `git fetch origin main`、`git status -sb` 不落後；`pipeline_status.py --new` 列出這份檔案；`wiki/todo.md` 沒有別人 `doing` 這篇 |
| S1 收件與書目 | 驗證原始檔、決定 slug 與年份、核對書目、判斷群星或我的關注 | `references/intake.md` 第二至四節 | 收件紀錄（寫進交付說明） | slug、`paper_year`、作者、期刊卷期頁、DOI 皆已以 Crossref 或原文首頁核對；我的關注者 `focus_role` 已依資料夾決定 |
| S2 讀原文 | 抽出全文文字，通讀原文，記下問題、方法、結果、限制與公開資源 | `paper-pdf-parser`；`references/intake.md` 第六節 | 抽取文字（只放 scratchpad，不進倉庫） | 能寫出四句：做了什麼、怎麼做、證據是什麼、限制是什麼，各附原文頁碼 |
| S3 證據表 | 把要寫的強主張逐條對應到原文頁、表、圖 | `wiki-content-audit` 寫作模式第 1、2 步 | `wiki/evidence/<slug>.md` | 檔案存在；數值逐一寫出；每條預定的區塊公式都有式號或頁碼；`pipeline_status.py <slug>` 之 S3 為 OK |
| S4 論文頁 | 依骨架寫 Frontmatter 與正文六段 | `references/paper-page-template.md`；`wiki-content-audit` 寫作模式第 3 步 | `wiki/papers/<slug>.md` | `lint_wiki.py` 對本頁無 ERROR；S4 為 OK（`card_line` 切得成封面斷行） |
| S5 概念頁與索引 | 連結或建立概念頁（雙向）；登記 `wiki/index.md` | `references/concepts-and-index.md` | 更新之 `wiki/concepts/*.md`、`wiki/index.md` | S5 為 OK；`lint_wiki.py` 無雙向對應與孤島 ERROR |
| S6 核對與核實狀態 | 先宏觀、再微觀，回原文逐項核對；查到的問題修正並登記；設定 `verification` | `wiki-content-audit` 寫作模式第 4、5 步；`crossref_check.py` | `wiki/issues.md` 條目（若有）；`verification` | 本頁沒有 open 問題；`verification` 為 `verified`（或 `partial` 並寫明未核對範圍）；S6 為 OK |
| S7 卡片檔 | 寫封面、Card 2 至 6 與 Card 3 示意圖 | `paper-card-writer` 第五節第 1 至 6 步（含第 2-1 步回原文抽查） | `wiki/cards/<slug>.md` | `check_cards.py <slug>` ERROR 0，WARN 逐條交代；S7 為 OK |
| S8 論文頁網頁 | 建置論文頁原型並以瀏覽器驗證 | `paper-card-writer` 第五節第 7-1 步、`references/paper-page.md` | `web/prototypes/paper-v1/<slug>.html` | 建置自我檢查 ERROR 0；`verify_page.js` 結果 PASS；截圖目視無拆詞折行、無重疊 |
| S9 上架首頁 | 重建首頁，確認這篇出現在星圖或我的星系，封面卡出現在卡片牆 | `references/publish.md` 第一至四節；`paper-card-writer` 第五節第 7-2 步 | `web/index.html` | `build_home.py --card <slug>` 卡片牆自我檢查 ERROR 0；`verify_wall.js` 與 `verify_star.js` 結果皆 PASS |
| S10 日誌與提交 | 寫日誌、一次提交本篇所有檔案、推送；`raw/` 有新檔時另行提交 | `references/publish.md` 第五、六節；`git-sync-guardian` | 一個主倉庫提交（必要時加一個 `raw/` 提交） | 推送成功（`Ahead: 0`）；`build_home.py --check` 一致；`pipeline_status.py <slug>` 全部 OK、結束碼 0 |

**怎麼知道一篇做到哪裡**：

```bash
python .agents/skills/paper-pipeline/scripts/pipeline_status.py            # 全庫總表：每篇各步驟 ok／NG／!，與下一步
python .agents/skills/paper-pipeline/scripts/pipeline_status.py <slug>     # 單篇：逐步列出每項檢查與原因，並指出下一步
python .agents/skills/paper-pipeline/scripts/pipeline_status.py --new      # raw/ 中尚未收錄之原始檔，以及 raw/ 未提交之變動
```

`ok` 是完成，`NG` 是未完成（必須處理），`!` 是有 WARN（必須在交付說明逐條交代處理方式），`--` 是本機無法判斷（例如沒有 `raw/`）。S2 讀原文無法機械檢查，不在表中；它的證據是交付說明的四句與頁碼。**`pipeline_status.py` 只檢查做了沒有與可機械判斷的形式，不檢查內容是否忠於原文**；全部 `ok` 也不代表內容正確，S3、S6、S7 的人工核對一步都不能省。

## 五、各步驟細則

### S0 同步與領件

1. 依 `git-sync-guardian` 執行 `git fetch origin main` 與 `git status -sb`；第一行出現 `behind` 時先執行 `python .agents/skills/git-sync-guardian/scripts/sync.py`。
2. 執行 `pipeline_status.py --new`，看要收錄的檔案屬於哪一類（`新檔案`、`已列待辦`、`已引用`），依 `references/intake.md` 第一節處理。最後幾行若列出 `raw/` 有未提交之變動，依 `references/intake.md` 第五節處理。
3. 整份讀 `wiki/todo.md`：這篇若已有條目，狀態為 `waiting` 時不得動工（等使用者），`doing` 且負責人不是你時不得接手；平行批次有協調規則時照規則做。
4. 啟動本機伺服器（S8、S9 要用）：`python -m http.server 8781 --bind 127.0.0.1 --directory web`（埠號依協調規則；不可用 `file://` 開檔）。

### S1 收件與書目

依 `references/intake.md` 第二至四節，決定並寫下（寫進交付說明的「收件紀錄」）：

1. 原始檔是真的 PDF（檔頭 `%PDF-`）、可以抽出文字或需要 OCR。
2. 書目：英文原題、作者（依署名順序）、發表年份、期刊或會議與卷期頁、DOI；有 DOI 者以 Crossref 核對，學位論文以封面與書名頁核對。
3. slug（`YYYY-<小寫英文連字號>`，年份為實際發表年份）。
4. 群星或我的關注：原始檔在 `raw/my-focus/` 之下者為我的關注，`focus_role` 依子資料夾決定；其餘為群星。
5. 獎項：有獎項者查官方紀錄（得獎者、年份、事由）；得獎者不一定是本篇作者。
6. 這份原始檔是否其實是既有論文頁的奠基論文（`key_papers`），而不必另立新頁（`references/intake.md` 第三節）。

### S2 讀原文

1. 依 `paper-pdf-parser` 抽出全文（預設 PyMuPDF），輸出放在 scratchpad，**不得**放進倉庫或 `raw/`。
2. 完整讀一遍原文（不是只讀摘要）。表格、圖、雙欄順序或公式抽取有疑問時，回看 PDF 頁面影像。
3. 寫下四句話：這篇做了什麼、怎麼做、證據是什麼、限制是什麼，各附原文頁碼。寫不出限制，代表還沒讀完。
4. 同時記下 `references/intake.md` 第六節列的事項：公開的程式、資料與模型；作者明列的限制與未來工作；原文的編號公式與所在頁；主要結果表的表號。

### S3 證據表

1. 依 `wiki-content-audit` 寫作模式第 2 步建立 `wiki/evidence/<slug>.md`（格式見 `AGENTS.md` 第七章第 4 節）。
2. 要列的主張：論文頁與卡片會用到的每個數字（逐一寫出數值與表列、欄位，不得只寫「表 3 各數值」）、每條區塊公式（式號或頁碼）、「首次／證明／導致／所有」等強斷言、獎項與後續研究之歸屬。
3. 後續研究：每筆打開該研究本身（DOI 頁、摘要），確認它做了你要寫的事；書目以 Crossref 核對。不得把作者自述的未來工作寫成他人後續成果。
4. 「類型」只能取五類之一：本篇研究結果、後續研究、作者解釋、依原文數據計算、Wiki 詮釋。
5. 完成條件：`pipeline_status.py <slug>` 之 S3 為 OK；若為 `!`，依原因補齊或在交付說明交代。

### S4 論文頁

1. 依 `references/paper-page-template.md` 複製骨架，逐欄填寫 Frontmatter，逐段寫正文。每一句事實都能在證據表或原文找到位置。
2. 區塊公式只放原文公式（`wiki-content-audit` 寫作模式第 3 步）；原文沒有公式的研究不放區塊公式。
3. 完成條件：`python .agents/skills/wiki-content-audit/scripts/lint_wiki.py` 對本頁無 ERROR；`pipeline_status.py <slug>` 之 S1、S3、S4 為 OK（`card_line` 切不成封面斷行時 S4 為 `!`，必須改寫 `card_line`）。

### S5 概念頁與索引

1. 依 `references/concepts-and-index.md` 第一、二節，把本篇連到一至三個概念頁（必要時新建），論文頁 `concepts` 與概念頁 `papers` 雙向列出；概念頁「關鍵突破支柱」加入本篇一條。
2. 依同檔第三節在 `wiki/index.md` 正確的區段加入本篇條目；原本是 `[planned]` 條目者改寫為連結並改標 `[wiki]`。
3. 完成條件：`pipeline_status.py <slug>` 之 S5 為 OK；`lint_wiki.py` 沒有雙向對應或孤島之 ERROR。

### S6 核對與核實狀態

1. 依 `wiki-content-audit` 寫作模式第 4 步，**先宏觀、再微觀**：先對照原文摘要與結論看整頁方向，再逐句對回證據表與原文，並做吸引子檢查。
2. 有 DOI 者執行 `python .agents/skills/wiki-content-audit/scripts/crossref_check.py <slug>`，結果須一致。
3. 查到的問題：自己剛寫的頁面直接改正即可；修改既有頁面時，每項依 `AGENTS.md` 第七章第 4 節登記於 `wiki/issues.md`（含已當場修正者），編號依協調規則或流水號。
4. 設定 `verification`：Card 1 至 6 與正文的強主張都已逐項核對並登記於證據表者標 `verified`；只核對了一部分者標 `partial`，並在交付說明寫明未核對範圍。有 open 問題時為 `issues`，不得進入 S7。
5. 完成條件：`pipeline_status.py <slug>` 之 S6 為 OK；`lint_wiki.py` 無 ERROR。

### S7 卡片檔

1. 依 `paper-card-writer` 第五節第 1 至 6 步撰寫 `wiki/cards/<slug>.md`。第 2-1 步「回原文抽查」不得省略：即使 S3 至 S6 是你自己剛做的，也要在動筆前重新打開原文確認 Card 3 公式、Card 4 數字與 Card 5 出處。
2. 我的關注論文：Card 6 不得透露使用者碩論的題目、資料或結果（`paper-card-writer` 第二節第 13 條）；`focus_languages` 為空者在卡片檔填「研究類型」（`paper-card-writer` 之 `references/cover.md` 第七節）。
3. 完成條件：`python .agents/skills/paper-card-writer/scripts/check_cards.py <slug>` ERROR 0，WARN 逐條寫出判斷依據；`pipeline_status.py <slug>` 之 S7 為 OK 或 `!`（已交代）。

### S8 論文頁網頁

1. `python tools/build_paper_prototype.py <slug>`：自我檢查 ERROR 0，WARN 依 `paper-card-writer` 之 `references/paper-page.md` 第七節處理。
2. 以本機伺服器開啟 `http://127.0.0.1:8781/prototypes/paper-v1/<slug>.html`，執行 `paper-card-writer` 之 `scripts/verify_page.js`，結果須為「結果：PASS」。
3. 依 `references/paper-page.md` 第六節第 3 步截圖目視（桌面 1440 x 900、手機 375 x 812）：沒有拆詞折行、沒有只剩一兩字的行、示意圖標籤不重疊。改了卡片檔就從 S7 的檢查腳本重跑。
4. 完成條件：上述三項都達成；`pipeline_status.py <slug>` 之 S8 為 OK。

### S9 上架首頁

依 `references/publish.md` 第一至四節：

1. 同步遠端後執行 `python tools/build_home.py --card <slug>`：輸出清單須有本篇一行、斷行與卡片檔相同，「卡片牆自我檢查：ERROR 0」；再以 `--check --card <slug>` 確認一致。
2. 開 `http://127.0.0.1:8781/index.html`，依序執行 `verify_wall.js`（`var EK_SLUG = '<slug>';`）與本 Skill 之 `scripts/verify_star.js`（同樣先設 `EK_SLUG`），兩份報告最後一行都須為「結果：PASS」。
3. 截圖目視：群星論文在星圖上看得到這顆星、點了說明框顯示雙年份與一句話；我的關注論文在 `#my-constellation` 看得到；卡片牆上的封面卡斷行、論文名、雙年份正常；點卡片開到本篇論文頁、按返回回到首頁。
4. 平行批次的協調規則禁止組員重建首頁時，略過本步，交付說明寫明「首頁：依協調規則未重建，由協調者處理」；協調者在該批結束時依 `references/publish.md` 第四節統一上架。
5. 完成條件：上述各項達成。卡片檔提交前 `pipeline_status.py` 之 S9 會顯示「卡片檔尚未提交」，提交後才會轉為 OK（S10 第 4 步確認）。

### S10 日誌與提交

依 `references/publish.md` 第五、六節：

1. 執行 `lint_wiki.py`（ERROR 須為 0），以 `python .agents/skills/git-sync-guardian/scripts/log_time.py` 取得時間，在 `wiki/log.md` 檔尾追加一筆日誌（動作 `ingest`；新收錄以外之補完用 `update`）。
2. 以 `safe_commit_push.py` 一次提交本篇所有檔案：論文頁、證據表、卡片檔、論文頁網頁、首頁、改動的概念頁、`wiki/index.md`、`wiki/issues.md`（以 `--issue` 逐條列出）、`wiki/todo.md`（以 `--todo` 逐條列出）、日誌（以 `--log-heading` 指定自己的標題）。檔案清單見 `references/publish.md` 第五節。
3. `raw/` 有使用者新放入、尚未提交的原始檔時，依 `references/intake.md` 第五節在 `raw/` 另行提交與推送。
4. 推送後：不加 `--card` 執行 `python tools/build_home.py --check`，須為「一致」；執行 `pipeline_status.py <slug>`，九步全部 OK（或 `!` 已交代）、結束碼 0。不是的話回到該步處理，處理完再提交一次。

## 六、多篇與批次

1. 先執行 `pipeline_status.py` 看全庫總表，或 `--new` 看待收錄清單，排出順序後一篇一篇做；每篇 S0 至 S10 完成後才開下一篇。
2. 同一批次每完成五篇，重讀本 Skill 第二節、`paper-card-writer` 第二節與其 `references/style.md`。
3. 預估剩下的時間或用量不足以把一篇做到 S10 時，不開新的一篇；做到一半必須停下時，在 `wiki/todo.md` 登記停在哪一步、哪些檔案已改但未提交，不得留下未交代的半成品。
4. 多個對話平行作業：協調者在 `wiki/todo.md` 寫明每組篇目、可改哪些檔、`wiki/issues.md` 編號區段、預覽埠、誰重建首頁；各組依規則做到 S8 或 S10，回報後由協調者統一上架（`references/publish.md` 第四節）。
5. 批次結束後，執行 `pipeline_status.py` 全庫總表，把仍為 `NG` 的篇目與原因寫進回報。

## 七、交付說明（每篇都要，逐項填寫，不得刪項）

```markdown
### <slug> 收錄交付

1. 收件紀錄（S1）：原始檔路徑；slug；書目（英文題名、作者、年份、期刊卷期頁、DOI）與 Crossref 核對結果；群星或我的關注（focus_role 與依據之資料夾）；獎項與官方出處
2. 四句（S2）：做了什麼／怎麼做／證據／限制，各附原文頁碼
3. 證據表（S3）：列數；數字、公式、強斷言、後續研究各幾列；採用版本
4. 論文頁（S4）：Frontmatter 各欄之決定與依據（domain、domain_tags、concepts、card_line、hook、雙年份）；正文六段各取自原文哪幾節
5. 概念頁與索引（S5）：連到哪些概念頁、是否新建、index.md 放在哪一區段
6. 核對（S6）：宏觀與微觀各發現並修正了什麼；登記之 EK 編號；crossref_check.py 結果；verification 與理由
7. 卡片（S7）：依 paper-card-writer 第八節之交付說明全文（含原文抽查表、check_cards.py 結果）
8. 網頁（S8）：build_paper_prototype.py 最後兩行；verify_page.js 報告全文；目視結果
9. 上架（S9）：build_home.py --card 輸出全文；verify_wall.js 與 verify_star.js 報告全文；目視結果
10. 提交（S10）：提交編號；raw/ 是否另行提交；推送後 build_home.py --check 最後一行；pipeline_status.py <slug> 全文
11. 未決事項：原文缺少的資料、無法核實的主張、工具疑似誤判（已登記之 TD 編號）
```

日誌條目精簡為：產出檔案、各步驟檢查結果之數字、登記之 EK 編號、未決事項；交付說明全文只放回覆，不寫入日誌。

## 八、偷工自查表（交付前逐項核對）

| 偷工方式 | 為什麼不行 | 對應步驟 |
|---|---|---|
| 沒跑 `pipeline_status.py`，憑記憶說某步做完了 | 多個代理分頭作業時，最常漏的是別人以為你做了的那一步 | 第四節 |
| 只讀摘要就寫論文頁，或用中文譯本當證據 | 數字、條件、限制多在正文與表格；譯本可能譯錯 | S2、S3 |
| 先寫論文頁再回頭補證據表 | 事後補的證據表只是替寫好的句子找藉口 | S3、S4 |
| 證據表只寫「表 3 各數值」 | 卡片檢查只能逐字比對數字，查核者也無從核對 | S3 |
| 為了讓論文頁好看而自擬公式，或把原文公式改寫成教科書形式 | 卡片會把它當原文公式；讀者會以為那是作者的式子 | S4 |
| `card_line` 沒試切封面斷行 | 寫卡片時才發現切不出 3 行，回頭改又要重跑 S4 至 S6 | S4 |
| 只把論文頁連到概念頁，沒在概念頁 `papers` 反向登記，或忘了 `index.md` | 星圖連線與索引都會缺這篇，lint 會報孤島 | S5 |
| 沒有逐項核對就標 `verified` | `verified` 會在網頁顯示「已逐項對照原文查核」 | S6 |
| 寫卡片時只信自己剛寫的論文頁，不回原文抽查 | 第二批回填時，自己寫的頁面也查出錯誤 | S7 |
| 只建論文頁網頁，沒上架首頁；或只驗卡片牆，沒驗星圖或我的星系 | 使用者要的是「出現在首頁」；三處都要看到 | S9 |
| 分好幾個提交，或漏提交首頁、概念頁、索引 | 使用者無法逐篇檢視與退回；別人重建首頁時才發現不一致 | S10 |
| `raw/` 有使用者新放入的檔案卻沒提交 | 原始檔只存在本機，換一台機器就不見 | S10、`intake.md` 第五節 |
| 回應被安全機制中止後，換個說法重試 | 不得以改寫規避；停下、登記、告知使用者 | 第二節第 6 條 |
| 交付說明只寫「已完成」，沒有貼指令輸出 | 使用者無從檢查 | 第七節 |

## 九、檢查工具一覽

| 工具 | 在哪一步 | 做什麼 |
|---|---|---|
| `python .agents/skills/paper-pipeline/scripts/pipeline_status.py [--new｜<slug> ...]` | 每一步之後 | 全庫總表、單篇逐項原因、待收錄原始檔；只用標準函式庫，會呼叫下列三支 Python 腳本 |
| `python .agents/skills/wiki-content-audit/scripts/lint_wiki.py` | S4、S5、S6、S10 | Frontmatter、標籤、雙向對應、連結、公式、控制字元、核實狀態一致性 |
| `python .agents/skills/wiki-content-audit/scripts/crossref_check.py <slug>` | S1、S6 | 書目與 Crossref 一致（需網路） |
| `python .agents/skills/paper-card-writer/scripts/check_cards.py <slug>` | S7 | 卡片檔欄位、字數、來源比對 |
| `python tools/build_paper_prototype.py <slug>` | S8 | 產生論文頁網頁並自我檢查 |
| `paper-card-writer` 之 `scripts/verify_page.js` | S8 | 瀏覽器量測論文頁（桌面與手機） |
| `python tools/build_home.py [--check] [--card <slug>]` | S9、S10 | 重建或比對首頁（星圖、我的星系、卡片牆） |
| `paper-card-writer` 之 `scripts/verify_wall.js` | S9 | 瀏覽器量測卡片牆（四種組合） |
| 本 Skill 之 `scripts/verify_star.js` | S9 | 瀏覽器確認這篇在星圖或我的星系看得見、點得開 |
| `python .agents/skills/git-sync-guardian/scripts/log_time.py`、`safe_commit_push.py` | S10 | 日誌時間、只提交自己的檔案並推送 |

修改本 Skill 時只改本正本，`.claude/skills/paper-pipeline/SKILL.md` 為轉介檔，不寫規則（`AGENTS.md` 第六章）。規範衝突時：`AGENTS.md` > `DESIGN.md` > 各 Skill；發現衝突時登記 `wiki/todo.md`（範圍 `skill`）並告知使用者，不得自行選邊。
