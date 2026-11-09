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

### 3. 雙倉庫一體化覆蓋（Dual-Repo Parity）
- 凡任務涉及 `raw/` 內之任何原始素材、文獻剪藏或新生成之 PDF 譯本，檢查與提交推送操作必須在主倉庫（`Epoch-Kairos`）與私有倉庫（`Mine-RAW`，位於 `raw/`）兩處同時執行。

### 4. 日誌並行合流原則（Log Append-Only Concurrency）
- `wiki/log.md` 為追加模式（Append-only）。當多個 AI 同時在日誌末尾追加紀錄而產生 Git 合併衝突時，一律按時間戳記先後排序並保留所有條目，嚴禁覆蓋或抹除其他 AI 的工作紀錄。`scripts/merge_log.py` 可自動完成：已提交的條目順序不動，對方獨有的條目依時間插入。

### 5. 只提交自己的修改（Commit Only Your Own Changes）
- 嚴禁 `git add -A`、`git add .`、`git commit -a`。提交前先看 `git diff --stat`，只暫存自己修改的檔案；未追蹤的資料夾（如他人的 `work/`）一律不得加入。
- `wiki/log.md` 只提交「執行代理」為自己的條目：用 `scripts/stage_log.py "<代理名稱>"` 逐條暫存。它以「HEAD 版日誌＋自己的新條目」組出提交內容，工作目錄的檔案不變，別人的條目留給他們自己提交。條目順序與條目之間的空行都跟隨工作目錄，提交後不會留下只差空行的修改。
- 追加日誌時，新條目與前一條之間只留一個空行（即寫入 `\n## [...]`，前一條已以換行結尾）。多打的空行雖會被一併提交，但會讓日誌格式不一致。
- 合流遠端時用 `git merge --autostash`，讓他人未提交的修改暫時收起、合流後放回，且放回後維持「未暫存」。
- 若暫存區在你動手前就已有檔案，代表可能是別人暫存的，先確認歸屬，不要直接提交。

### 6. 寫入日誌即提交（Log Implies Commit）
- 日誌條目代表一項工作已完成。在 `wiki/log.md` 追加自己的條目後，**必須在同一回合內**以 `safe_commit_push.sh` 提交並推送該條目與本項工作修改的檔案，不需等待使用者另外說「提交」；僅在使用者明確要求暫緩時例外。這是使用者對所有代理的常設授權：本專案以自動化為目標，每筆日誌都對應一個已推送的提交，多 AI 協作出問題時才能立即追查。
- 工作尚未完成、或使用者要求先不提交時，**先不要寫日誌**；進度留在工作檔，完成後一次寫入、一次提交。
- 寫日誌一律**追加於檔尾**（例如以附加模式開檔），不得把整份日誌讀進來再整檔寫回，以免覆蓋他人剛追加、尚未提交的條目；亦不得改動他人條目。

---

## 三、自動化工具鏈指令（Automated Toolchain）

本技能於 `scripts/` 目錄內建三個強健之自動化腳本，供 AI 與使用者直接調用：

### 1. 雙倉庫狀態審計
```bash
./.agents/skills/git-sync-guardian/scripts/status.sh
```
* **功能**：同時對主倉庫與 `raw/` 私有倉庫執行 `fetch`，報告當前分支、本機與遠端 commit 雜湊、領先（Ahead）與落後（Behind）數值，以及未暫存之修改檔案。

### 2. 安全合流提取（Safe Sync & Pull）
```bash
./.agents/skills/git-sync-guardian/scripts/sync.sh
```
* **功能**：依序對主倉庫與 `raw/` 私有倉庫進行遠端更新檢查：
  - 若雙方一致：回報 `Already up to date`。
  - 若遠端領先且本機無新 commit：執行 `git merge --ff-only --autostash origin/main` 安全快進。
  - 若兩端分岔（Divergent）：執行 `git merge --autostash origin/main` 三方合併。
  - `--autostash` 會暫收工作目錄中其他代理尚未提交的修改，合流後放回並維持未暫存；只有 `wiki/log.md` 衝突時自動以 `merge_log.py` 排解，其他衝突則警示並引導人工排解。

### 3. 原子提交並推送（Atomic Safe Commit and Push）
```bash
# 主倉庫：明確列出自己的檔案；列出 wiki/log.md 時只會提交 --agent 指定代理的條目
./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<提交訊息>" main --agent "Claude Code" -- DESIGN.md wiki/log.md

# 私有 raw/ 倉庫：路徑相對於 raw/
./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<提交訊息>" raw --agent "Codex" -- my-focus/英文論文/foo.pdf
```
* **功能**：
  1. 確認暫存區原本是空的（否則中止，避免帶走他人已暫存的檔案）。
  2. 只暫存 `--` 之後列出的路徑；`wiki/log.md` 交給 `stage_log.py` 逐條暫存。不接受 `.`、`-A`。若同一代理的多個工作階段同時追加日誌，可重複傳入 `--log-heading "## [YYYY-MM-DD HH:MM] ..."` 精確挑選自己的標題，避免同代理身分造成誤暫存；被選取的條目會依時間插入暫存版，已提交條目順序不變。
  3. 先提交自己的修改，再 `git fetch` 並以 `git merge --autostash` 與遠端三方合流；只有 `wiki/log.md` 衝突時自動以 `merge_log.py` 排解，放回他人修改時的日誌衝突亦同。
  4. 清空暫存區，讓他人修改維持未暫存；`git push origin main` 後確認 `Ahead: 0`，並列出工作目錄中仍未提交（屬於他人）的檔案。
* 兩個倉庫都有修改時，分別執行 `main` 與 `raw` 各一次（各自列出檔案），以滿足雙倉庫一體化。
* 需要 Python 3.7 以上（僅用標準函式庫）。腳本會自動尋找可執行的 Python：依序試 `python3`、`python`、`py`，每個實際執行一次，取第一個成功者；不寫死任何路徑，Mac、Linux、Windows 皆適用（Windows 的 `python3` 可能是微軟商店的空殼，會被略過）。三者都不可用時腳本會報錯，請告知使用者安裝 Python。

### 4. 日誌工具
```bash
# 只暫存自己的日誌條目（--dry-run 只列出不寫入）
python .agents/skills/git-sync-guardian/scripts/stage_log.py "Claude Code" --dry-run

# wiki/log.md 在 merge 或 stash pop 時衝突：依 append-only 自動排解（只寫檔，不 git add）
python .agents/skills/git-sync-guardian/scripts/merge_log.py
```

---

## 四、標準作業程序 (SOP)

### SOP-1：開始新任務或提取更新
1. 執行 `./.agents/skills/git-sync-guardian/scripts/status.sh` 查看狀態。
2. 若落後遠端，執行 `./.agents/skills/git-sync-guardian/scripts/sync.sh` 同步最新成果。

### SOP-2：完成任務並固化成果
1. 確認全專案無任何表情符號（Zero-Emoji）。
2. 在 `wiki/log.md` 結尾**追加**符合 `AGENTS.md` 規範之條目（標明執行代理、底層模型、白名單標籤與具體變更）。寫入日誌後立即進行第 3 步，不等使用者指示（鐵律 6）。
3. 以 `git diff --stat` 確認哪些檔案是自己改的，再執行 `./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<符合 Conventional Commits 格式之訊息>" main --agent "<代理名稱>" -- <自己的檔案> wiki/log.md`；若 `raw/` 也有自己的修改，再以 `raw` 執行一次，確保兩處倉庫均推送成功。
4. 確認腳本最後列出的「仍未提交的修改」都不是自己的；若有自己的檔案遺漏，補上後再執行一次。

### SOP-3：遭遇 wiki/log.md 衝突時之排解
`safe_commit_push.sh` 與 `sync.sh` 遇到「只有 `wiki/log.md` 衝突」時會自動呼叫 `merge_log.py` 排解。若需人工處理：
1. 檢視衝突區塊（`<<<<<<< HEAD` 與 `>>>>>>> origin/main`），或直接執行 `python .agents/skills/git-sync-guardian/scripts/merge_log.py`。
2. 提取兩側之日誌條目，依 `[YYYY-MM-DD HH:MM]` 時間戳記先後排序重新拼接。
3. 刪除所有 Git 衝突標記（`<<<<<<<`, `=======`, `>>>>>>>`）。
4. 提交合併：`git commit -m "Merge remote-tracking branch 'origin/main' into main"` 並立即 `git push origin main`。
