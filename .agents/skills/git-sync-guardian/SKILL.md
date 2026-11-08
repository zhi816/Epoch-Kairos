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

---

## 二、四大鐵律規範

所有參與專案之 AI 代理人，在執行任何版本控制操作時必須嚴格遵守以下四項鐵律：

### 1. 提交必含推送（Commit Implies Push）
- 只要使用者指示「提交」、「commit」或當 AI 完成階段性任務進行版本固化時，**必須將 `commit` 與 `push` 視為單一不可分割的原子操作（Atomic Operation）**。
- 嚴格禁止任何僅執行 `git commit` 而留滯未推送 commit 於本機的行為。回報任務完成時，本機與遠端必須處於完全對齊狀態（`Ahead: 0`）。

### 2. 動工與提取前必先檢查遠端（Pre-flight Fetch Check）
- 在開始任何實質檔案編輯、或執行 pull 操作前，必須先執行 `git fetch origin main` 檢查遠端最新動態。
- 若遠端領先（Behind），優先進行安全合流；若發現分岔，依規定執行三方合併（3-way merge），絕不以強制覆蓋（force push）抹除他人提交。

### 3. 雙倉庫一體化覆蓋（Dual-Repo Parity）
- 凡任務涉及 `raw/` 內之任何原始素材、文獻剪藏或新生成之 PDF 譯本，檢查與提交推送操作必須在主倉庫（`Epoch-Kairos`）與私有倉庫（`Mine-RAW`，位於 `raw/`）兩處同時執行。

### 4. 日誌並行合流原則（Log Append-Only Concurrency）
- `wiki/log.md` 為追加模式（Append-only）。當多個 AI 同時在日誌末尾追加紀錄而產生 Git 合併衝突時，一律按時間戳記先後排序並保留所有條目，嚴禁覆蓋或抹除其他 AI 的工作紀錄。

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
  - 若遠端領先且本機無新 commit：執行 `git pull --ff-only origin main` 安全快進。
  - 若兩端分岔（Divergent）：自動執行安全合併 `git merge origin/main`，若遇內容衝突則警示並引導人工排解。

### 3. 原子提交並推送（Atomic Safe Commit and Push）
```bash
# 同時提交並推送主倉庫與私有倉庫
./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<提交訊息>" both

# 僅提交並推送主倉庫
./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<提交訊息>" main

# 僅提交並推送私有 raw/ 倉庫
./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<提交訊息>" raw
```
* **功能**：先檢查遠端是否已有新 commit（若有則先合流），接著暫存檔案、產生 commit，並立即執行 `git push origin main`，最後確認 `Ahead: 0`。

---

## 四、標準作業程序 (SOP)

### SOP-1：開始新任務或提取更新
1. 執行 `./.agents/skills/git-sync-guardian/scripts/status.sh` 查看狀態。
2. 若落後遠端，執行 `./.agents/skills/git-sync-guardian/scripts/sync.sh` 同步最新成果。

### SOP-2：完成任務並固化成果
1. 確認全專案無任何表情符號（Zero-Emoji）。
2. 在 `wiki/log.md` 結尾追加符合 `AGENTS.md` 規範之條目（標明執行代理、底層模型、白名單標籤與具體變更）。
3. 執行 `./.agents/skills/git-sync-guardian/scripts/safe_commit_push.sh "<符合 Conventional Commits 格式之訊息>" both`，確保兩處倉庫均推送成功。

### SOP-3：遭遇 wiki/log.md 衝突時之排解
1. 檢視衝突區塊（`<<<<<<< HEAD` 與 `>>>>>>> origin/main`）。
2. 提取兩側之日誌條目，依 `[YYYY-MM-DD HH:MM]` 時間戳記先後排序重新拼接。
3. 刪除所有 Git 衝突標記（`<<<<<<<`, `=======`, `>>>>>>>`）。
4. 提交合併：`git commit -m "Merge remote-tracking branch 'origin/main' into main"` 並立即 `git push origin main`。
