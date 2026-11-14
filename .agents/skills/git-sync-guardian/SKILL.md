---
name: git-sync-guardian
description: >-
  Guard version control synchronization in a multi-AI collaborative environment across dual repositories (Epoch-Kairos and Mine-RAW). Ensures pre-flight fetch checks, atomic commit-and-push operations, and conflict-free log merges.
---

# Git Sync Guardian（多 AI 協同開發與雙倉庫版本同步守護技能）

## 一、協作背景與核心痛點

本專案採用開創性的多代理人（Multi-AI）異步協同開發架構：
- **協同主體**：Anthropic Claude Code、OpenAI Codex / GPT、Google Antigravity / Gemini 等多個前沿 AI 系統同時參與本專案之程式開發、論文翻譯與知識庫維護。
- **雙倉庫拓撲**：
  1. 公開主倉庫：`Epoch-Kairos`（本機根目錄，版控展示層、Wiki 層與系統規範）。
  2. 私有資料倉庫：`Mine-RAW`（位於 `raw/`，獨立 Git 倉庫，版控原始不可變文獻與論文全譯本 PDF）。

### 核心痛點：
1. **本機遺留 Commit 未推送（Dangling Unpushed Commits）**：AI 預設將 `commit` 視為本機操作，若無強制要求，常在完成任務後未執行 `git push`；隨後其他 AI 在遠端推送新節點，導致本機與遠端形成分支分岔（Divergent branches）。
2. **提取時的分岔中斷（Pull Divergence Abortion）**：在未設定預設合流策略時，`git pull` 遇分岔會引發 `fatal: Need to specify how to reconcile divergent branches`，造成自動化流程卡死。
3. **雙倉庫操作脫節（Dual-Repo Desynchronization）**：操作主倉庫時遺忘 `raw/` 私有倉庫，或在 `raw/` 增修文獻後未推送到 `Mine-RAW` 遠端。
4. **誤提交他人修改（Cross-Agent Commit Contamination）**：多個 AI 共用同一個工作目錄，Git 又以「檔案」為單位暫存。只要有人整檔加入 `wiki/log.md`，或以 `git add -A` 暫存全部檔案，就會把其他代理尚未提交的條目與檔案（例如 `work/` 內的審查截圖）一起提交，造成歸屬錯誤，甚至把私人工作檔推上公開倉庫。2026-11-08 已實際發生：Claude Code 整檔加入 `wiki/log.md`，誤帶入 Codex 尚未提交的 4 筆審查紀錄。
5. **寫了日誌卻遲未提交（Logged but Uncommitted）**：代理寫入日誌後，若使用者沒有另外說「提交」就不提交，條目會滯留在共用的 `wiki/log.md`，被他人誤帶、阻擋大家同步，或在他人「讀取後整檔寫回」時被覆蓋；出問題時也找不到對應的提交。

---

## 二、六大鐵律規範

所有參與專案之 AI 代理人，在執行任何版本控制操作時必須嚴格遵守以下六項鐵律：

### 1. 提交必含推送（Commit Implies Push）
- 只要使用者指示「提交」、「commit」或當 AI 完成階段性任務進行版本固化時，**必須將 `commit` 與 `push` 視為單一不可分割的原子操作（Atomic Operation）**。
- 嚴格禁止任何僅執行 `git commit` 而留滯未推送 commit 於本機的行為。回報任務完成時，本機與遠端必須處於完全對齊狀態（`Ahead: 0`）。

### 2. 動工與提取前必先檢查遠端（Pre-flight Fetch Check）
- 在開始任何實質檔案編輯、或執行 pull 操作前，必須先執行 `git fetch origin main` 檢查遠端最新動態。
- 若遠端領先（Behind），優先進行安全合流；若發現分岔，依規定執行三方合併（3-way merge），絕不以強制覆蓋（force push）抹除他人提交。

### 3. 雙倉庫最新同步與一體化覆蓋（Dual-Repo Freshness & Parity）
- **每個任務都先更新兩邊**：無論本次工作是否會修改 `raw/`，開始實質編輯前一律執行 `status.py`，確認主倉庫（`Epoch-Kairos`）與私有倉庫（`Mine-RAW`，位於 `raw/`）都已向遠端 fetch。任一倉庫若落後，執行 `sync.py` 更新兩邊，再跑一次 `status.py`，確認兩邊 `Behind: 0` 後才開始編輯。主倉庫已最新不代表 Mine-RAW 已最新，不得因此略過 raw 倉庫。
- **修改內容分倉庫提交**：主倉庫檔案在 `Epoch-Kairos` 提交推送；`raw/` 檔案在 `Mine-RAW` 提交推送。任務只修改其中一邊時，另一邊仍須完成前述遠端同步檢查。

### 4. 日誌並行合流原則（Log Append-Only Concurrency）
- `wiki/log.md` 為追加模式（Append-only）。當多個 AI 同時在日誌末尾追加紀錄而產生 Git 合併衝突時，一律按時間戳記先後排序並保留所有條目，嚴禁覆蓋或抹除其他 AI 的工作紀錄。`scripts/merge_log.py` 可自動完成：已提交的條目順序不動，對方獨有的條目依時間插入。

### 5. 只提交自己的修改（Commit Only Your Own Changes）
- 嚴禁 `git add -A`、`git add .`、`git commit -a`。提交前先看 `git diff --stat`，只暫存自己修改的檔案；未追蹤的資料夾（如他人的 `work/`）一律不得加入。
- `wiki/log.md` 只提交「執行代理」為自己的條目：用 `scripts/stage_log.py "<代理名稱>"` 逐條暫存。它以「HEAD 版日誌＋自己的新條目」組出提交內容，工作目錄的檔案不變，別人的條目留給他們自己提交。條目順序與條目之間的空行都跟隨工作目錄，提交後不會留下只差空行的修改。
- `wiki/issues.md` 同樣是共用檔案，只提交自己修改的問題條目：`safe_commit_push.sh` 列出 `wiki/issues.md` 時必須以 `--issue EK-NNN`（可重複）指定編號，由 `scripts/stage_issues.py` 以「HEAD 版問題清單＋指定條目的工作目錄版本」組出提交內容；未指定的條目（例如其他代理剛改成 `fixed` 的狀態）留在工作目錄。背景：2026-11-09 Claude Code 整檔提交問題清單，誤把 Antigravity 尚未提交的 EK-008 至 EK-011 狀態變更帶入。
- `wiki/todo.md` 同樣是共用檔案：`safe_commit_push.sh` 列出 `wiki/todo.md` 時必須以 `--todo TD-NNN`（可重複）指定自己新增、修改或刪除的條目，由 `scripts/stage_todo.py` 組出提交內容。與問題清單不同，待辦完成即刪，故指定的編號若已從工作目錄刪除，即暫存其刪除。
- 追加日誌時，新條目與前一條之間只留一個空行（即寫入 `\n## [...]`，前一條已以換行結尾）。多打的空行雖會被一併提交，但會讓日誌格式不一致。
- 合流遠端時用 `git merge --autostash`，讓他人未提交的修改暫時收起、合流後放回，且放回後維持「未暫存」。
- 若暫存區在你動手前就已有檔案，代表可能是別人暫存的，先確認歸屬，不要直接提交。

### 6. 寫入日誌即提交（Log Implies Commit）
- 日誌條目代表一項工作已完成。在 `wiki/log.md` 追加自己的條目後，**必須在同一回合內**以 `safe_commit_push.sh` 提交並推送該條目與本項工作修改的檔案，不需等待使用者另外說「提交」；僅在使用者明確要求暫緩時例外。這是使用者對所有代理的常設授權：本專案以自動化為目標，每筆日誌都對應一個已推送的提交，多 AI 協作出問題時才能立即追查。
- 工作尚未完成、或使用者要求先不提交時，**先不要寫日誌**；進度與交接事項登記於 `wiki/todo.md`（`AGENTS.md` 第七章第 5 節），完成後再寫日誌、一次提交。不得以日誌條目充當交接清單。
- 寫日誌一律**追加於檔尾**（例如以附加模式開檔），不得把整份日誌讀進來再整檔寫回，以免覆蓋他人剛追加、尚未提交的條目；亦不得改動他人條目。
- **標題時間一律以指令取得**：寫標題前先執行 `python .agents/skills/git-sync-guardian/scripts/log_time.py`，把輸出的臺北時間原樣填入 `## [YYYY-MM-DD HH:MM]`，不得憑估計、記憶或對話中的時間推算。`stage_log.py` 會擋下晚於現在 5 分鐘以上或早於現在 60 分鐘以上的自己的新條目，`safe_commit_push.sh` 隨即還原本次暫存並中止；僅在條目確實早已寫好（例如推送失敗後重試）時，加 `--allow-stale-log` 放行。被擋下時，修正工作目錄中自己那筆尚未提交的條目標題即可。

---

## 三、自動化工具鏈指令（Automated Toolchain）

本技能於 `scripts/` 目錄內建強健之自動化腳本，同時提供**跨平台 Python 版（`.py`）**與 **Bash 版（`.sh`）**，參數與行為完全一致。
- **Windows / PowerShell 或沙盒環境（如 Codex、Antigravity）**：**優先直接以 `python ...py` 呼叫**，無須啟動 WSL Bash 或 Git Bash，可避開沙盒攔截外部 `bash.exe` 的權限耗時。
- **沙盒 `.git` 寫入權限提醒**：`git fetch`、`git commit`、`git push` 需要寫入 `.git/`（如 `.git/FETCH_HEAD`、`.git/index.lock`）與存取網路。若沙盒預設封鎖 `.git/` 寫入，請於第一步執行 `status.py` 時一併申請 `.git` 寫入與網路權限。

### 1. 雙倉庫狀態審計
```bash
# 跨平台 Python 版（Windows PowerShell 首選）
python .agents/skills/git-sync-guardian/scripts/status.py

# Bash 版（macOS / Linux / Git Bash）
./.agents/skills/git-sync-guardian/scripts/status.sh
```
* **功能**：同時對主倉庫與 `raw/` 私有倉庫執行 `fetch`，報告當前分支、本機與遠端 commit 雜湊、領先（Ahead）與落後（Behind）數值，以及未暫存之修改檔案。
* **防靜默過期與查詢失敗保護**：若 `git fetch origin main` 失敗，會印出 Git 錯誤訊息、標示 `STALE - fetch failed` 並回傳非零代碼；若分支、ahead/behind 或 `git status` 查詢失敗，欄位會標示未知而不會假報 `0` 或 `Clean`，同樣以非零代碼結束。只有明確離線檢視時可加 `--allow-offline`，但它不會忽略本機 Git 查詢失敗。

### 2. 安全合流提取（Safe Sync & Pull）
```bash
# 跨平台 Python 版（Windows PowerShell 首選）
python .agents/skills/git-sync-guardian/scripts/sync.py

# Bash 版
./.agents/skills/git-sync-guardian/scripts/sync.sh
```
* **功能**：依序對主倉庫與 `raw/` 私有倉庫進行遠端更新檢查：
  - 若雙方一致：回報 `Already up to date`。
  - 若遠端領先且本機無新 commit：執行 `git merge --ff-only --autostash origin/main` 安全快進。
  - 若兩端分岔（Divergent）：執行 `git merge --autostash origin/main` 三方合併。
  - `--autostash` 會暫收工作目錄中其他代理尚未提交的修改，合流後放回並維持未暫存；只有 `wiki/log.md` 衝突時自動以 `merge_log.py` 排解。若日誌合併提交失敗，腳本會回報失敗並保留現況；其他衝突則警示並引導人工排解。

### 3. 原子提交並推送（Atomic Safe Commit and Push）
```bash
# 主倉庫（跨平台 Python 版，Windows PowerShell 首選）：明確列出自己的檔案；列出 wiki/log.md 時只會提交 --agent 指定代理的條目
python .agents/skills/git-sync-guardian/scripts/safe_commit_push.py "<提交訊息>" main --agent "Claude Code" -- DESIGN.md wiki/log.md

# 同時提交日誌、問題清單與待辦時：順序固定為「訊息、倉庫、選項、--、檔案」；--log-heading、--issue、--todo 皆可重複，每個編號各寫一次旗標
python .agents/skills/git-sync-guardian/scripts/safe_commit_push.py "fix(wiki): correct <slug> against its source" main --agent "Claude Code by Anthropic" --log-heading "## [YYYY-MM-DD HH:MM] fix | <標題> | <標籤>" --issue EK-150 --issue EK-151 --todo TD-012 -- wiki/papers/<slug>.md wiki/evidence/<slug>.md wiki/issues.md wiki/todo.md wiki/log.md

# 私有 raw/ 倉庫：路徑相對於 raw/
python .agents/skills/git-sync-guardian/scripts/safe_commit_push.py "<提交訊息>" raw --agent "Codex" -- my-focus/英文論文/foo.pdf

# Bash 版（參數完全相同）
./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<提交訊息>" main --agent "Claude Code" -- DESIGN.md wiki/log.md
```
* **功能**：
  1. 確認暫存區原本是空的（否則中止，避免帶走他人已暫存的檔案）。
  2. 只暫存 `--` 之後列出的**單一相對檔案路徑**；拒絕資料夾、絕對路徑、路徑跳脫與 pathspec magic，並用 literal pathspec 防止萬用字元展開。`wiki/log.md` 交給 `stage_log.py`、`wiki/issues.md` 交給 `stage_issues.py`（`--issue`）、`wiki/todo.md` 交給 `stage_todo.py`（`--todo`）逐條暫存。若同一代理的多個工作階段同時追加日誌，可重複傳入 `--log-heading "## [YYYY-MM-DD HH:MM] ..."` 精確挑選自己的標題，避免同代理身分造成誤暫存；被選取的條目會依時間插入暫存版，已提交條目順序不變。
  3. 確認目前分支為 `main`，先 `git fetch`，成功後才暫存與建立提交。提交後以 `git merge --autostash` 與遠端合流；若遠端在前置 fetch 後又前進，push 仍可能被拒，腳本會回報錯誤並保留本機提交供後續同步。
  4. 日誌衝突由 `merge_log.py` 排解；合併提交失敗會明確中止，不回報成功。推送後確認 `Ahead: 0`，並列出工作目錄中仍未提交（屬於他人）的檔案。
* 兩個倉庫都有修改時，分別執行 `main` 與 `raw` 各一次（各自列出檔案），以滿足雙倉庫一體化。
* 需要 Python 3.7 以上（僅用標準函式庫）。`.py` 版直接以當前 Python 執行並自動將標準輸出設為 UTF-8；`.sh` 版會自動依序試 `python3`、`python`、`py`，取第一個成功者。

### 4. 日誌與待辦工具
```bash
# 取得日誌標題時間（臺北時間，不受本機時區影響）；寫標題前必先執行
python .agents/skills/git-sync-guardian/scripts/log_time.py

# 依條目讀取日誌最後幾筆（日誌只寫不讀，不得整份讀取）；--grep 查特定事項，-n 0 不限筆數
python .agents/skills/git-sync-guardian/scripts/log_tail.py -n 3
python .agents/skills/git-sync-guardian/scripts/log_tail.py --grep TD-004 -n 0

# 新增待辦前取得下一個編號；提交 wiki/todo.md 時由 safe_commit_push.py / .sh 的 --todo 自動調用
python .agents/skills/git-sync-guardian/scripts/stage_todo.py --next-id
python .agents/skills/git-sync-guardian/scripts/stage_todo.py TD-003 --dry-run

# 只暫存自己修改的問題條目（提交 wiki/issues.md 時由 safe_commit_push.py / .sh 的 --issue 自動調用）
python .agents/skills/git-sync-guardian/scripts/stage_issues.py EK-069 EK-070 --dry-run

# 只暫存自己的日誌條目（--dry-run 只列出不寫入）
python .agents/skills/git-sync-guardian/scripts/stage_log.py "Claude Code" --dry-run

# wiki/log.md 在 merge 或 stash pop 時衝突：依 append-only 自動排解（只寫檔，不 git add）
python .agents/skills/git-sync-guardian/scripts/merge_log.py
```

---

## 四、標準作業程序 (SOP)

### SOP-1：開始新任務或提取更新
1. 每個新任務在實質編輯前，執行 `python .agents/skills/git-sync-guardian/scripts/status.py`（或 `status.sh`）；該指令會 fetch 主倉庫與 Mine-RAW 兩邊。不得只查主倉庫，即使本次工作不涉及 `raw/` 也一樣。
2. 任一倉庫落後遠端時，執行 `python .agents/skills/git-sync-guardian/scripts/sync.py`（或 `sync.sh`）；腳本會檢查並同步兩邊。完成後再跑 `status.py`，確認兩邊 `Behind: 0`；fetch 或同步失敗時，先排除原因並重跑，不以舊狀態視為已更新。
3. 接手脈絡依 `AGENTS.md` 第六章第 4 節取得：`git log --oneline -10`、整份閱讀 `wiki/todo.md`，仍需細節時以 `scripts/log_tail.py` 讀日誌最後幾筆；不得整份讀取 `wiki/log.md`。

### SOP-2：完成任務並固化成果
1. 確認全專案無任何表情符號（Zero-Emoji）。
2. 在 `wiki/log.md` 結尾**追加**符合 `AGENTS.md` 規範之條目（標明執行代理、底層模型、白名單標籤與具體變更）。本項工作若完成某筆待辦，同時從 `wiki/todo.md` 刪除該條目，並於日誌寫明編號。寫入日誌後立即進行第 3 步，不等使用者指示（鐵律 6）。
3. 以 `git diff --stat` 確認哪些檔案是自己改的，再執行 `python .agents/skills/git-sync-guardian/scripts/safe_commit_push.py "<符合 Conventional Commits 格式之訊息>" main --agent "<代理名稱>" -- <自己的檔案> wiki/log.md`（或 `safe_commit_push.sh`；涉及待辦時加上 `--todo TD-NNN` 並列出 `wiki/todo.md`）；若 `raw/` 也有自己的修改，再以 `raw` 執行一次，確保兩處倉庫均推送成功。
4. 確認腳本最後列出的「仍未提交的修改」都不是自己的；若有自己的檔案遺漏，補上後再執行一次。最後再跑 `status.py`，確認主倉庫與 Mine-RAW 的 `Behind` 皆為 0。

### SOP-3：遭遇 wiki/log.md 衝突時之排解
`safe_commit_push.py` / `.sh` 與 `sync.py` / `.sh` 遇到「只有 `wiki/log.md` 衝突」時會自動呼叫 `merge_log.py` 排解。若需人工處理：
1. 檢視衝突區塊（`<<<<<<< HEAD` 與 `>>>>>>> origin/main`），或直接執行 `python .agents/skills/git-sync-guardian/scripts/merge_log.py`。
2. 提取兩側之日誌條目，依 `[YYYY-MM-DD HH:MM]` 時間戳記先後排序重新拼接。
3. 刪除所有 Git 衝突標記（`<<<<<<<`, `=======`, `>>>>>>>`）。
4. 提交合併：`git commit -m "Merge remote-tracking branch 'origin/main' into main"` 並立即 `git push origin main`。
