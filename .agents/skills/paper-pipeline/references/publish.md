# 上架首頁與提交（S9、S10）

本檔規範 SKILL.md 第五節 S9、S10：讓這篇論文出現在首頁，並把所有檔案一次提交。卡片牆的細則以 `paper-card-writer` 之 `references/card-wall.md` 為準，本檔補上星圖與我的星系的驗證，以及整篇收錄的提交清單。

## 一、首頁上有哪三處

| 位置 | 誰會出現 | 資料從哪來 | 什麼時候出現 |
|---|---|---|---|
| 星圖（群星模式，首頁開場） | `my_focus: false` 之論文 | 論文頁 Frontmatter（`domain`、`domain_tags`、`concepts`、`card_line`、雙年份） | 論文頁存在、首頁重建後 |
| 我的星系（網址 `#my-constellation`） | `my_focus: true` 之論文 | 同上，加 `focus_role`、`focus_languages` | 同上 |
| 卡片牆（群星檔案、我的星系檔案） | 有**已提交**卡片檔之論文 | `wiki/cards/<slug>.md` 封面區段；連到論文頁網頁 | 卡片檔已提交（或以 `--card` 帶入）、首頁重建後 |

三處都由 `python tools/build_home.py` 產生 `web/index.html`，**不得手改**。版面改 `tools/home_template.html`、`web/assets/css/starmap.css`、`web/assets/js/starmap.js`，那是設計工作，不屬本流程。

## 二、建置首頁（S9 第 1 步）

1. 同步：`git fetch origin main`，`git status -sb` 不得 `behind`（`card-wall.md` 第四節第 1 步）。
2. 建置：
   ```bash
   python tools/build_home.py --card <slug>
   ```
   逐項確認輸出（整段貼進交付說明）：
   * 第一行「卡片牆：群星 N 張、我的關注 M 張」，清單有本篇一行，編號與論文頁網頁 Card 1 左上相同，斷行與卡片檔「封面斷行」逐字相同。
   * 「卡片牆自我檢查：ERROR 0」。有 ERROR 時腳本不寫檔，依 `card-wall.md` 第六節處理。
   * 最後一行「已寫入 web/index.html（群星 a、標籤 b、概念 c、我的關注 d）」：新收錄之群星論文，`a` 比收錄前多 1；我的關注論文，`d` 多 1。新建概念頁時 `c` 多 1。
3. 一致性：`python tools/build_home.py --check --card <slug>`，最後一行「web/index.html 與建置結果一致」。
4. **編號後移之他篇論文頁**（S9 第 4 步）：清單中排在本篇之後的論文，編號各加一（群星 `No.`、我的關注 `F.` 各自排序；`tools/build_home.py` 之 `card_numbers()`），但它們的論文頁仍是舊編號。
   * 執行 `python .agents/skills/paper-pipeline/scripts/pipeline_status.py`（全庫總表），S8 為 NG 且原因為「編號與首頁卡片牆不同」者，逐篇重建：`python tools/build_paper_prototype.py <slug> ...`。自我檢查須為 ERROR 0；`git diff -U0 -- web/papers/` 每檔應只有編號一行改變，有其他差異時停下查明原因（多半是他人修改了範本），不得一併提交。
   * `git status` 顯示 `tools/paper_template.html` 或 `tools/build_paper_prototype.py` 有他人未提交之修改時，不得在工作目錄重建（會把別人未完成的範本產生進論文頁），改以 HEAD 之暫時 worktree 重建再複製：
     ```bash
     git worktree add --detach <scratchpad>/wt-head HEAD
     (cd <scratchpad>/wt-head && python tools/build_paper_prototype.py <slug> ...)
     cp <scratchpad>/wt-head/web/papers/<slug>/index.html web/papers/<slug>/
     git worktree remove --force <scratchpad>/wt-head
     ```
     本篇尚未提交時，worktree 裡沒有本篇論文頁，算出的編號仍是舊的；此時先完成 S10 提交本篇，再以 worktree 重建並另行提交（日誌動作 `fix`）。
   * 重建之他篇論文頁與本篇同一提交（第五節第 2 點）。`web/papers/` 是多人共用之產生檔，未提交的重建結果可能被他人重建或還原；提交後以 `git show HEAD:web/papers/<slug>/index.html` 確認編號已進入提交。

## 三、瀏覽器驗證與目視（S9 第 2、3 步）

### 1. 執行兩支驗證腳本

以本機伺服器（`python -m http.server 8781 --bind 127.0.0.1 --directory web`）開啟 `http://127.0.0.1:8781/index.html`，分頁保持在前景（背景分頁計時器會變慢）。

1. **卡片牆**：先執行 `var EK_SLUG = '<slug>';`，再執行 `.agents/skills/paper-card-writer/scripts/verify_wall.js` 全文，最後一行須為「結果：PASS（首頁卡片牆，指定 <slug>）」。
2. **星圖或我的星系**：先執行 `var EK_SLUG = '<slug>';`，再執行 `.agents/skills/paper-pipeline/scripts/verify_star.js` 全文，最後一行須為「結果：PASS（首頁星圖，指定 <slug>）」。它會依首頁資料判斷這篇在群星或我的星系，在桌面 1440 x 900 與手機 375 x 812 各確認：首頁資料有這篇、星點存在且看得見、無障礙標籤含論文名、點擊後為選取狀態且說明框顯示論文名（群星另查一句話）。
3. 兩份報告**全文原樣**貼進交付說明，不得改寫成「全部通過」。

代理以瀏覽器 JavaScript 工具執行時，可把腳本暫時複製到 `web/` 下（例如 `web/_verify_star.js`）再以 `fetch` 讀入執行；**驗證完立刻刪除，不得提交**。瀏覽器窗格隱藏時計時器會變慢，腳本可能超過工具的等待時間：改為把結果存到 `window` 變數，稍後再讀，例如 `var EK_SLUG = '<slug>'; (async () => { window.__ekStar = await eval(await (await fetch('/verify_star.js')).text()); })();`，約 20 秒後讀 `window.__ekStar`。

macOS 上倉庫位於「文件」等受保護資料夾時，桌面 app 之預覽伺服器可能因 `PermissionError: Operation not permitted` 無法從倉庫啟動（`card-wall.md` 第四節第 3 步）：把 `web/` 複製到 scratchpad（如 `rsync -a --delete web/ <scratchpad>/webcopy/`），三支驗證腳本也複製進去，再從該處啟動伺服器。腳本留在 scratchpad，不會誤入提交；每次重建論文頁或首頁後都要重新複製，否則驗到的是舊檔。

### 2. 目視（截圖，桌面 1440 x 900 與手機 375 x 812）

| 項目 | 群星論文 | 我的關注論文 |
|---|---|---|
| 星點 | 在星圖上看得到本篇的星（實心發光點），顏色為本篇 `domain` 之學科色 | 進入 `#my-constellation` 後看得到本篇的星（空心星），在 `paper_year` 那一列；欄位依 `concepts`：只連臺灣南島語計算語言學者在左欄、只連低資源機器翻譯者在右欄、兩者都連或都不連者在中間（`DESIGN.md` 第四章） |
| 說明框 | 點星後顯示論文名、雙年份（有獎項者「YYYY 發表 ｜ YYYY 諾貝爾獎」）與一句話 | 點星後顯示論文名、年份與角色 |
| 連線 | 本篇與其概念星（`concepts`）之間有連線 | 本篇與其概念中心之間有連線 |
| 篩選 | 點本篇學科之篩選鈕，本篇的星仍在 | 點本篇角色之篩選鈕，本篇的星仍在 |
| 卡片牆 | 依 `card-wall.md` 第四節第 4 步八項 | 同左（在我的星系檔案） |
| 連結 | 點卡片開到本篇論文頁網頁；論文頁左上返回回到首頁星圖，標示「回到群星」 | 同左，但返回到首頁我的星系（`#my-constellation`），標示「回到我的星系」（`paper-card-writer` 之 `paper-page.md` 第二節） |

發現版面問題（重疊、超出、看不到）而不是本篇資料造成的，登記 `wiki/todo.md`（範圍 `web`）並告知使用者；本篇照常交付並在交付說明寫明。

## 四、平行批次：協調者統一上架

`wiki/todo.md` 之協調規則禁止組員重建首頁時，組員略過 S9，提交時不列 `web/index.html`。協調者在各組提交後：

1. 同步遠端，執行 `python tools/build_home.py`（不加 `--card`），清單須包含本批所有已提交之卡片、自我檢查 ERROR 0。
2. 執行 `verify_wall.js`（不設 `EK_SLUG`，一次驗全部卡片），結果 PASS；WARN 依 `card-wall.md` 第六節處理。
3. 對本批每一篇執行 `verify_star.js`（每次設該篇之 `EK_SLUG`），結果皆 PASS。
4. 依本檔第三節第 2 點目視本批新上架之星與卡片。
5. 本批有新收錄之論文時，依本檔第二節第 4 點重建編號後移之論文頁。
6. 單獨提交 `web/index.html`、第 5 步重建之論文頁與日誌（本檔第五節），日誌列出本批上架之 slug 與兩支腳本的結果。
7. 執行 `python .agents/skills/paper-pipeline/scripts/pipeline_status.py`，本批各篇之 S9 應為 OK，全庫沒有 S8 編號不一致之 NG。

## 五、提交（S10）

### 1. 日誌

1. `python .agents/skills/wiki-content-audit/scripts/lint_wiki.py`：ERROR 0（他人正在修改之頁面造成的 ERROR，確認不是你的檔案後在交付說明寫明）。
2. `python .agents/skills/git-sync-guardian/scripts/log_time.py` 取得時間，在 `wiki/log.md` **檔尾追加**一筆（不得讀整檔後寫回）：
   ```markdown
   ## [YYYY-MM-DD HH:MM] ingest | <收錄某篇之一句話標題> | <本篇 domain_tags，空格分隔>
   - **執行代理**：<代理名稱與機構>
   - **模型版本**：<模型與版本>
   - **具體變更**：<依 SKILL.md 第七節之精簡版：產出檔案、各步驟檢查結果數字、EK 編號、未決事項>
   ```
   新收錄用 `ingest`；補完既有論文用 `update`；只修正錯誤用 `fix`。含 LaTeX 的內容不得用 shell heredoc 寫入（`wiki-content-audit` 寫作模式第 3 步）。

### 2. 提交清單（一個提交，列出本篇所有檔案）

| 檔案 | 什麼時候要列 | 共用檔案之暫存方式 |
|---|---|---|
| `wiki/papers/<slug>.md` | 一定 | — |
| `wiki/evidence/<slug>.md` | 一定 | — |
| `wiki/cards/<slug>.md` | 一定 | — |
| `web/papers/<slug>/index.html` | 一定 | — |
| `web/index.html` | 有執行 S9 時（協調規則禁止時不列） | 首頁衝突時依 `card-wall.md` 第四節第 5 步重建，不得手改 |
| `web/papers/<他篇>/index.html` | 第二節第 4 點重建之編號後移者 | 每檔只應有編號一行改變 |
| `wiki/concepts/<概念>.md` | 有改動的每一個 | — |
| `wiki/index.md` | 一定 | 只改自己的條目 |
| `wiki/issues.md` | 有新增或修改問題條目時 | `--issue EK-NNN`，每個編號一次 |
| `wiki/todo.md` | 有新增、修改或刪除條目時 | `--todo TD-NNN`，每個編號一次 |
| `wiki/log.md` | 一定 | `--log-heading "<自己的完整標題行>"` |

```bash
python .agents/skills/git-sync-guardian/scripts/safe_commit_push.py "feat(wiki): ingest <slug> from raw source to homepage" main --agent "<代理名稱>" --log-heading "## [YYYY-MM-DD HH:MM] ingest | <標題> | <標籤>" --issue EK-NNN --todo TD-NNN -- wiki/papers/<slug>.md wiki/evidence/<slug>.md wiki/cards/<slug>.md web/papers/<slug>/index.html web/index.html wiki/concepts/<概念>.md wiki/index.md wiki/issues.md wiki/todo.md wiki/log.md
```

參數順序固定為「訊息、倉庫、選項、`--`、檔案」；沒有用到的選項與檔案刪去。不得 `git add -A`、`git add .`。驗證用的暫存檔（`web/_verify_*.js`、`web/papers/_verify_page.js`、`.claude/launch.json`）不得提交。

### 3. `raw/` 倉庫

使用者新放入之原始檔，依 `intake.md` 第五節在 `raw/` 另行提交與推送。

### 4. 推送後確認

1. `safe_commit_push.py` 回報 `Ahead: 0`。
2. `python tools/build_home.py --check`（不加 `--card`），最後一行「web/index.html 與建置結果一致」。不一致而差異只來自別人剛提交的卡片時，重建並單獨提交 `web/index.html`。
3. `python .agents/skills/paper-pipeline/scripts/pipeline_status.py <slug>`：九步皆 OK（或 `!` 已在交付說明交代），結束碼 0。把全文貼進交付說明。

## 六、做不下去時

| 情況 | 處理 | 不得 |
|---|---|---|
| `build_home.py` 報 ERROR | 依 `card-wall.md` 第六節逐條處理（多半是封面斷行、封面標題或論文頁未建置） | 改建置腳本；手改 `web/index.html` |
| `verify_star.js` 報「不在首頁資料」 | 論文頁未提交或首頁未重建：重跑本檔第二節 | 改 `EK_SLUG` 為別篇 |
| `verify_star.js` 報「星點不存在」或「看不見」 | 首頁未重建，或星圖程式問題：重建後仍失敗則登記 `wiki/todo.md`（範圍 `web`）並告知使用者 | 改 CSS 或程式讓它看起來通過 |
| `verify_wall.js` 報 FAIL | 依 `card-wall.md` 第六節 | 改字級、改 CSS |
| 推送時 `web/index.html` 合併衝突 | 依 `card-wall.md` 第四節第 5 步第 3 點重建 | 手動編輯衝突標記 |
| `pipeline_status.py` 最後仍有 NG | 回到該步處理，處理完再提交一次 | 宣稱完成 |
