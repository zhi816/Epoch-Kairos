# 首頁卡片牆：卡片檔如何上首頁，以及如何驗證

本檔規範 SKILL.md 第五節第 7 步之二「放上首頁卡片牆並驗證」。每寫完或修訂一篇卡片檔，論文頁原型驗證完成後，都要重建首頁 `web/index.html`，確認這篇的封面卡出現在「群星檔案」（我的關注論文則在「我的星系檔案」），並通過兩道檢查。**不得以「論文頁原型已驗證」代替本步驟**：首頁卡片的大小、字級與論文頁 Card 1 不同，而且只有已提交的卡片檔才會上牆。

## 一、為什麼一定要另外驗證

| 會出的問題 | 原因 | 由誰抓 |
|---|---|---|
| 寫完卡片、首頁卻沒有這張卡 | 首頁只收已提交之卡片檔；尚未提交又沒加 `--card` | 建置輸出清單、`verify_wall.js`（指定 slug） |
| 把別人尚未完成的卡片帶上首頁並提交 | 舊做法讀工作目錄之全部卡片檔 | 建置腳本只讀 Git 已提交版本（第三節） |
| 封面斷行在 Card 1 放得下，在手機卡片牆折成兩行 | 卡片牆卡片寬約 166px，比論文頁小 | `verify_wall.js`（一句話自動折行） |
| 論文名在卡片牆被截斷 | 卡片牆論文名字級相對較大，兩行約 9 至 18 字 | `verify_wall.js`（WARN） |
| `card_line` 被改過，牆上仍是舊的斷行 | 封面斷行未同步 | 建置自我檢查（ERROR） |
| 點卡片打不開 | 論文頁原型未建置或未提交 | 建置自我檢查（ERROR）、`verify_wall.js`（連結） |

## 二、卡片牆上每個位置從哪裡來

版型為 `DESIGN.md` 第二章第 3 節之 F「星窗＋一句話」：桌面 3 欄（右欄較窄時 2 欄）、手機 2 欄，卡片固定 3:4。群星為學科星光色底、深墨字；我的關注為深色卡＋藍框（`human` 學科玫瑰粉）。

| 位置 | 內容 | 來源 | 誰負責 |
|---|---|---|---|
| 左上 | 編號 `No.07`（我的關注 `F.23`） | `tools/build_home.py` 之 `card_numbers()`，與論文頁 Card 1 相同 | 自動 |
| 右上 | 學科短名（我的關注為角色名） | `domain`／`focus_role` | 自動 |
| 星窗小星 | 14 顆小星，與論文頁 Card 1 同一組 | `cover_sky()`，由 `paper_year` 與 `card_line` 決定 | 自動 |
| 星窗代表星 | 有獎項者帶光環；我的關注為空心星 | `honor`、`my_focus` | 自動 |
| 星窗左上（僅我的關注） | 研究語言，或研究類型 | `focus_languages`；為空時卡片檔「研究類型」 | Frontmatter／卡片檔（`cover.md` 第七節） |
| 星窗下方 | 一句話（學科色、宋體，最多三行） | 卡片檔「封面斷行」，去掉 `／` 須等於 `card_line` | **你寫**（`cover.md` 第三節） |
| 星窗下 | 論文名（最多兩行，超過以省略號截斷） | 卡片檔「封面標題」；未填時取 `title_zh` 短名 | **你確認**（`cover.md` 第四節） |
| 底線下 | 雙年份「1982 發表 ｜ 2024 諾貝爾獎」；未獲獎者為期刊簡稱 | `years_line()`：`paper_year`、`honor`／`award_year`、`venue_short` 或 `venue` | 自動，但 `honor` 格式要對（`cover.md` 第六節） |
| 點卡片 | 開該篇論文頁原型 `prototypes/paper-v1/<slug>.html` | 正式論文頁（`wiki/todo.md` TD-002）產出前之暫定（2026-11-10 使用者決定） | 自動，原型須已建置 |
| 篩選 | 群星：點學科後，只顯示本身學科或帶該學科標籤之卡片（與星圖相同）；我的星系：依角色或概念 | `domain`、`domain_tags`、`focus_role`、`concepts` | 自動 |

**你不寫網頁。** `web/index.html` 只由 `python tools/build_home.py` 產生，不得手改。

## 三、哪些卡片會上牆（一定要懂）

1. 建置腳本**只讀 Git 已提交（精確說是 Git 索引中）之卡片檔**。多個代理共用同一個工作目錄，工作目錄裡常有別人寫到一半的卡片檔；只讀已提交版本，才不會把別人未完成的內容產生進 `web/index.html` 又被你提交出去。
2. **自己這篇尚未提交時，一律加 `--card <slug>`**，腳本改用工作目錄中這篇的版本。多篇時重複寫：`--card a --card b`（批次回填仍是一篇一個提交，見 SKILL.md 第七節）。
3. 加了 `--card` 的那篇，腳本會先跑 `check_cards.py`，有 ERROR 即不寫檔；也會確認 `web/prototypes/paper-v1/<slug>.html` 存在。
4. 不得用 `--card` 帶入別人的卡片檔。建置輸出中「尚未提交，未放上卡片牆」的 INFO 若不是你的 slug，不要理會，也不要把那些檔案加入提交。
5. 你重建並提交的 `web/index.html` 裡會有別人**已提交**的卡片，這是正常的，可以提交。
6. 修訂已提交之卡片檔時同樣加 `--card <slug>`（輸出會提示「工作目錄有未提交之修改，牆上用的是已提交版本」）。

## 四、作業步驟（每篇必做，不得省略）

### 第 1 步：同步

`web/index.html` 是共用檔案。先確認本機不落後遠端，否則重建出的首頁會缺少別人剛提交的卡片：

```bash
git fetch origin main
git status -sb
```

`git status -sb` 第一行出現 `behind` 時，依 `git-sync-guardian` 執行 `python .agents/skills/git-sync-guardian/scripts/sync.py`，成功後再繼續。

### 第 2 步：建置與自我檢查

```bash
python tools/build_home.py --card <slug>
```

輸出格式如下（範例），**整段貼進交付說明**：

```text
卡片牆：群星 5 張、我的關注 5 張（卡片取自Git 已提交版本；--card：1982-hopfield-network）
  No.07  1982-hopfield-network  讓神經網路／從殘缺線索／想起完整記憶
  ...
INFO  wiki/cards/xxxx.md 尚未提交，未放上卡片牆。……
卡片牆自我檢查：ERROR 0、WARN 0
已寫入 web/index.html（群星 17、標籤 16、概念 8、我的關注 24）
```

逐項確認：

- [ ] 清單中有你的 slug 一行，編號與論文頁原型 Card 1 左上相同，斷行與卡片檔「封面斷行」逐字相同。
- [ ] 「卡片牆自我檢查：ERROR 0」。有 ERROR 時腳本不寫檔、結束代碼為 1，依本檔第六節處理後重跑。WARN 逐條處理。
- [ ] 最後一行為「已寫入 web/index.html」或「未變更 web/index.html」。
- [ ] 再執行 `python tools/build_home.py --check --card <slug>`，最後一行為「web/index.html 與建置結果一致」。

自我檢查項目（ERROR）：封面斷行去掉 `／` 後與 `card_line` 不同；斷行超過 3 行、任一行超過 9 字或有空行；論文名超過 22 字而未填封面標題；我的關注論文缺研究語言與研究類型；論文頁原型不存在（未建置或未提交）；卡片檔沒有對應論文頁；卡片檔有未解決之合併衝突；`--card` 那篇之 `check_cards.py` 有 ERROR。

### 第 3 步：瀏覽器驗證（有瀏覽器工具者必做）

1. 於倉庫根目錄啟動本機伺服器（可與論文頁驗證共用同一個）：
   ```bash
   python -m http.server 8781 --bind 127.0.0.1 --directory web
   ```
   macOS 上若倉庫位於「文件」等受保護資料夾，伺服器可能因 `PermissionError: Operation not permitted`（讀不到目前目錄）而無法啟動：把 `web/` 複製到暫存資料夾再從該處啟動，每次重建後須重新複製；`verify_wall.js` 亦可複製進該資料夾，以 `await eval(await (await fetch('/verify_wall.js')).text())` 執行。
2. 開 `http://127.0.0.1:8781/index.html`，分頁保持在前景。
3. 在 Console（或代理的瀏覽器 JavaScript 工具）先執行 `var EK_SLUG = '<slug>';`，再貼上 `.agents/skills/paper-card-writer/scripts/verify_wall.js` **全文**執行，約 25 秒後輸出報告。兩段可放在同一次執行。
4. 最後一行必須是「結果：PASS（首頁卡片牆，指定 <slug>）」。任何 FAIL 都不得交付；WARN 依本檔第六節逐條處理。
5. **報告全文原樣貼進交付說明**，不得改寫成「全部通過」，不得刪去別人卡片的列。

量測項目：桌面 1440 x 900 與手機 375 x 812、群星與我的星系兩種模式，共四組。每組量：顯示張數與本模式卡片數相同；指定之 slug 在牆上恰好一張且未被隱藏；每張卡 3:4；卡片內任何元素未超出卡片或星窗；一句話每行未自動折行、最多三行、與 `card_line` 逐字相同、未壓到代表星或語言標籤；手機卡片內字級不小於 10px；欄數（桌面 3、手機 2）；頁面無橫向捲動；點學科（或角色）篩選後只顯示該篩選之卡片、再點一次恢復；每張卡之連結回應 200。另以 WARN 列出被截斷之論文名、雙年份與語言標籤。

**沒有瀏覽器工具時**：不得宣稱已驗證。交付說明與日誌寫明「首頁卡片牆未以瀏覽器驗證（無瀏覽器工具）」，並在 `wiki/todo.md` 之「待瀏覽器驗證之論文頁原型」條目追加此 slug 並註明「含首頁卡片牆」（沒有該條目時新增一條，範圍 `web`）。

### 第 4 步：目視與操作檢查（有瀏覽器工具者必做）

腳本量不到「好不好讀」。以 1440 x 900 與 375 x 812 各截一張含自己卡片的畫面（我的關注論文先進入我的星系：網址加 `#my-constellation`），逐項在交付說明回報「通過」或發現的問題：

- [ ] 自己的卡片出現在正確的牆（群星檔案或我的星系檔案），順序依編號
- [ ] 一句話的每一行都是完整意群，斷行處與卡片檔相同，沒有只剩一兩個字的行
- [ ] 一句話與代表星、語言標籤之間留有空隙
- [ ] 論文名在兩行內；被截斷時已依第六節處理
- [ ] 雙年份完整可讀；被截斷時已依第六節處理
- [ ] 點自己的卡片，開到的是自己這篇的論文頁原型；按論文頁左上返回，回到首頁
- [ ] 點自己卡片所屬學科（我的關注：角色）篩選，自己的卡片仍在；再點一次恢復全部
- [ ] 與牆上其他卡片相比，沒有明顯的版面異常

### 第 5 步：提交

1. `web/index.html` 與卡片檔、論文頁原型、日誌**同一個提交**：
   ```bash
   python .agents/skills/git-sync-guardian/scripts/safe_commit_push.py "feat(cards): add <slug> card file" main --agent "<代理名稱>" --log-heading "<自己的日誌標題>" -- wiki/cards/<slug>.md web/prototypes/paper-v1/<slug>.html web/index.html wiki/log.md
   ```
2. 推送成功後，**不加 `--card`** 執行 `python tools/build_home.py --check`，最後一行須為「web/index.html 與建置結果一致」，且清單中有你的 slug。這證明你的卡片檔已提交、首頁與已提交內容一致。不一致時，重跑 `python tools/build_home.py`，確認差異只來自別人剛提交的卡片後，單獨提交 `web/index.html`。
3. **`safe_commit_push.py` 回報合併衝突且衝突檔案含 `web/index.html` 時**，不得手動編輯衝突標記，依下列順序處理：
   1. `git status` 列出衝突檔案。除了 `web/index.html` 與 `wiki/log.md` 還有其他檔案衝突時，停止，告知使用者。
   2. `wiki/log.md` 也衝突時：`python .agents/skills/git-sync-guardian/scripts/merge_log.py`，再 `git add wiki/log.md`。
   3. 執行 `python tools/build_home.py`（**不加** `--card`：合併中的 Git 索引已含雙方提交之卡片），確認清單中同時有你的卡片與對方新提交之卡片、ERROR 0。
   4. `git add web/index.html`，`git commit --no-edit`，`git push origin main`。
   5. `git stash list` 有 autostash 項目時，`git stash pop` 放回他人未提交之修改（`git-sync-guardian` 第三章第 2 節）；放回又衝突時停止，告知使用者。
   6. 回到本步第 2 項，以 `--check` 確認一致。

## 五、平行批次：由協調者統一上牆

`wiki/todo.md` 之協調規則禁止組員重建首頁時（例如 TD-008 分組回填），組員**略過本檔第四節第 1 至 4 步**，提交時不列 `web/index.html`，並在交付說明寫明「首頁卡片牆：依協調規則未重建，由協調者處理」。協調者在組員的卡片檔與論文頁原型提交後：

1. 依第四節第 1 步同步。
2. 執行 `python tools/build_home.py`（不加 `--card`），確認清單包含本批所有已提交之 slug、ERROR 0。
3. 執行 `verify_wall.js`（不設 `EK_SLUG`，一次驗全部卡片），結果須為 PASS；並依第四節第 4 步逐張目視本批新卡。
4. 單獨提交 `web/index.html` 與日誌，日誌列出本批上牆之 slug 與驗證結果。

因為卡片牆只讀已提交之卡片檔，協調者重建時不會帶上組員尚未完成的卡片。

## 六、看到 ERROR、FAIL 或 WARN 時怎麼處理

| 訊息 | 原因 | 正確處理 | 禁止的處理 |
|---|---|---|---|
| 封面斷行去掉「／」後須與 card_line 逐字相同 | 卡片檔封面斷行寫錯，或 `card_line` 後來被改過 | 依 `cover.md` 第三節重寫封面斷行，重建論文頁原型與首頁 | 改 `card_line` 去遷就斷行 |
| 封面斷行須為 1 至 3 行、每行 9 字以內 | 斷行太長或太多行 | 依 `cover.md` 第三節重切 | 刪字、改字級 |
| 論文名超過 22 字，須填「封面標題」 | 短名太長 | 依 `cover.md` 第四節填封面標題（只刪減、不加資訊） | 改 `title_zh` |
| 我的關注論文須填「研究類型」 | `focus_languages` 為空且卡片檔沒寫 | 依 `cover.md` 第七節填研究類型 | 在 `focus_languages` 隨便填語言 |
| 尚無論文頁原型 | 未執行或未提交 `build_paper_prototype.py` 之產出 | 執行 `python tools/build_paper_prototype.py <slug>`，與卡片檔一起提交 | 手寫 HTML、拿掉連結 |
| --card：check_cards.py ERROR | 卡片檔本身有錯 | 回 SKILL.md 第五節第 6 步修正 | 不加 `--card` 讓卡片「看起來」通過 |
| 卡片檔有未解決之合併衝突 | 合併中 | 先依 `git-sync-guardian` 解決卡片檔衝突 | 刪掉別人的版本 |
| FAIL 指定之 slug 在牆上 0 張 | 未加 `--card`、改完未重跑、或 `EK_SLUG` 打錯 | 重跑第 2 步再驗 | 改 `EK_SLUG` 為別篇讓它通過 |
| FAIL 一句話自動折行 | 某一行在手機卡片放不下 | 依 `cover.md` 第三節重切成較短的行 | 改字級、改 CSS |
| FAIL 一句話與 card_line 不同 | 首頁未重建，或論文頁 `card_line` 已改 | 重跑第 2 步；仍不同則修封面斷行 | 手改 `web/index.html` |
| FAIL 一句話壓到代表星或語言標籤 | 論文名兩行加一句話三行，星窗太擠 | 在卡片檔改用兩行之封面斷行（仍須合 `cover.md` 第三節），或依 `cover.md` 第四節填較短之封面標題；兩者都不可行時告知使用者 | 改 CSS |
| FAIL 連結回應 404 | 原型不在 `web/prototypes/paper-v1/` | 建置原型後重驗 | 改連結去指向別篇 |
| FAIL 張數、欄數、篩選、頁面寬、字級 | 首頁範本或程式之問題，不是卡片問題 | 登記 `wiki/todo.md`（範圍 `web`）並告知使用者；該篇卡片照常交付，交付說明寫明 | 自行修改 `home_template.html`、`starmap.css`、`starmap.js` |
| WARN 論文名超過兩行，被截斷 | 短名太長 | 卡片檔未填封面標題且短名超過 16 字：依 `cover.md` 第四節填封面標題，重建原型與首頁再驗。否則保留，交付說明寫明截斷位置 | 為了不截斷而改 `title_zh` |
| WARN bot 被截斷（雙年份） | 期刊或會議名稱太長 | 依 `paper-page.md` 第三節：先跑 `scripts/venue_short_lookup.py <slug>` 查候選；有期刊自己通用的縮寫（須有第一手出處，查不到出處者經使用者確認）或 Crossref `short-container-title` 才填 `venue_short`，填後重建論文頁原型與首頁再驗；兩者都沒有就保留，交付說明寫明「期刊無通用縮寫，卡片牆雙年份以省略號截斷」 | 自創縮寫、以中文意譯、未查證之縮寫未經使用者確認即填 |
| WARN tag 被截斷（研究語言） | 研究語言多 | 保留，交付說明寫明；`focus_languages` 只能依 `AGENTS.md` 第七章第 1 節之規則修改 | 為了放得下刪減語言 |

## 七、禁止事項

1. 不得手改 `web/index.html`。
2. 不得為了讓卡片上牆或通過驗證而修改 `tools/build_home.py`、`tools/home_template.html`、`web/assets/css/starmap.css`、`web/assets/js/starmap.js`、`scripts/verify_wall.js`，或調高門檻、加例外。認為工具誤判時，登記 `wiki/todo.md`（範圍 `skill`）並告知使用者，該篇維持未交付。
3. 不得用 `--card` 帶入別人的卡片檔，不得提交別人的卡片檔或論文頁原型。
4. 不得只驗桌面、只驗手機或只驗一種模式；`verify_wall.js` 一次量四組，報告原樣貼上。
5. 不得在沒有實際執行的情況下宣稱「已上牆」「已驗證」；交付說明必須貼出 `build_home.py` 輸出與 `verify_wall.js` 報告全文。
6. 提交後必須以 `python tools/build_home.py --check`（不加 `--card`）確認一致，不得省略。
