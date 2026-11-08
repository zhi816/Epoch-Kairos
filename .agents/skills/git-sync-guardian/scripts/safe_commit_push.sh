#!/usr/bin/env bash
# scripts/safe_commit_push.sh: Atomic Commit-and-Push Guardian for Epoch-Kairos and Mine-RAW
# Rule 1: Whenever changes are committed, they MUST be pushed immediately.
# Rule 5: Commit ONLY your own changes. Several AIs share one working tree, so this script
#         never runs `git add -A` / `git add .`; every path must be listed explicitly, and
#         wiki/log.md is staged entry by entry (only entries whose 執行代理 matches --agent).
# Zero emoji constraint strictly enforced.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 找一個真的能執行的 Python（Windows 的 python3 可能是微軟商店的空殼，執行後無作用）。
PY=""
for cand in python3 python py; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c "import sys" >/dev/null 2>&1; then PY="$cand"; break; fi
done

usage() {
  echo "Usage: $0 \"<commit_message>\" <main|raw> --agent \"<執行代理名稱>\" [--log-heading \"<exact heading>\"] -- <path> [<path> ...]"
  echo ""
  echo "  main | raw   要提交的倉庫：main 為 Epoch-Kairos，raw 為 raw/ 內的 Mine-RAW。"
  echo "               兩邊都有修改時請分別執行兩次（各自列出自己的檔案）。"
  echo "  --agent      執行代理名稱的一部分（例如 \"Claude Code\"、\"Codex\"、\"Antigravity\"），"
  echo "               用來挑出 wiki/log.md 中自己寫的條目。列出 wiki/log.md 時為必填。"
  echo "  --log-heading  只提交指定的新日誌標題；可重複使用，供同代理多個工作階段並行時精確選取。"
  echo "  -- <path>    只會提交這些路徑（相對於該倉庫根目錄）。不接受 '.'、'-A' 或倉庫根目錄。"
  echo ""
  echo "Example: $0 \"docs(design): update DESIGN.md\" main --agent \"Claude Code\" -- DESIGN.md wiki/log.md"
  echo "Example: $0 \"feat(raw): add translated pdf\" raw --agent \"Codex\" -- my-focus/英文論文/foo.pdf"
  exit 1
}

[ $# -ge 4 ] || usage
COMMIT_MSG="$1"; TARGET="$2"; shift 2
AGENT=""
LOG_HEADINGS=()
while [ $# -gt 0 ] && [ "$1" != "--" ]; do
  case "$1" in
    --agent) AGENT="$2"; shift 2 ;;
    --log-heading) LOG_HEADINGS+=("$2"); shift 2 ;;
    *) echo "Unknown option '$1'."; usage ;;
  esac
done
[ "$1" = "--" ] || usage
shift
[ $# -gt 0 ] || { echo "ERROR: 未列出任何要提交的檔案。"; usage; }
PATHS=("$@")

case "$TARGET" in
  main) REPO_NAME="Epoch-Kairos (Main)"; REPO_PATH="$REPO_ROOT" ;;
  raw)  REPO_NAME="Mine-RAW (Private)";  REPO_PATH="$REPO_ROOT/raw" ;;
  *) echo "Unknown target '$TARGET'. Expected 'main' or 'raw'."; usage ;;
esac

echo "=================================================="
echo "Atomic Commit-and-Push Guardian"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Target: $REPO_NAME"
echo "Agent: ${AGENT:-（未指定）}"
echo "Message: $COMMIT_MSG"
echo "=================================================="

[ -d "$REPO_PATH/.git" ] || { echo "ERROR: Git directory not found at $REPO_PATH."; exit 1; }
cd "$REPO_PATH"

# 0. 索引必須是乾淨的：若已有別人暫存的檔案，提交會把它們一起帶走。
PRESTAGED=$(git diff --cached --name-only)
if [ -n "$PRESTAGED" ]; then
  echo "ERROR: 暫存區已有檔案（可能是其他代理暫存的），為避免誤提交，已中止："
  echo "$PRESTAGED" | sed 's/^/    /'
  echo "請確認這些檔案的歸屬；若確定是自己的，請把它們加入 -- 之後的清單並先執行 git reset 清空暫存區。"
  exit 1
fi

# 1. 只暫存明確列出的路徑；日誌逐條暫存。
for P in "${PATHS[@]}"; do
  case "$P" in
    .|./|-A|--all|'*') echo "ERROR: 不接受 '$P'；請逐一列出自己的檔案。"; exit 1 ;;
  esac
  if [ "$P" = "wiki/log.md" ] && [ "$TARGET" = "main" ]; then
    [ -n "$AGENT" ] || { echo "ERROR: 提交 wiki/log.md 時必須以 --agent 指定執行代理名稱。"; exit 1; }
    [ -n "$PY" ] || { echo "ERROR: 找不到 python，無法逐條暫存日誌。"; exit 1; }
    STAGE_ARGS=("$AGENT")
    for H in "${LOG_HEADINGS[@]}"; do STAGE_ARGS+=(--heading "$H"); done
    PYTHONIOENCODING=utf-8 "$PY" "$SCRIPT_DIR/stage_log.py" "${STAGE_ARGS[@]}"
  else
    git add -- "$P"
  fi
done

echo "    即將提交的檔案："
git diff --cached --stat | sed 's/^/    /'

# 2. 先提交自己的修改。
if git diff --cached --quiet; then
  echo "    暫存區沒有變更，不建立新提交。"
else
  git commit -q -m "$COMMIT_MSG"
  echo "    已建立提交：$(git log --oneline -1)"
fi

# 3. 再與遠端合流。--autostash 會暫時收起工作目錄中其他代理尚未提交的修改，合流後放回。
git fetch origin main --quiet
BEHIND=$(git rev-list --count HEAD..origin/main)
only_log_conflict() { [ "$(git diff --name-only --diff-filter=U)" = "wiki/log.md" ]; }
if [ "$BEHIND" -gt 0 ]; then
  echo "    遠端領先 $BEHIND 個提交，進行三方合併..."
  if ! git merge --autostash --no-edit origin/main; then
    if [ "$TARGET" = "main" ] && [ -n "$PY" ] && only_log_conflict; then
      echo "    只有 wiki/log.md 衝突，依 append-only 原則自動合併（保留所有條目、依時間排序）..."
      PYTHONIOENCODING=utf-8 "$PY" "$SCRIPT_DIR/merge_log.py"
      git add wiki/log.md
      git commit -q --no-edit || true   # 結束合併；Git 會在此嘗試放回 autostash
    else
      echo "ERROR: 合併衝突。請依 SKILL.md SOP-3 人工排解並完成合併提交後再執行 git push origin main。"
      echo "       若有 autostash，請以 git stash list 確認並還原。"
      exit 1
    fi
  fi
  # 放回 autostash（其他代理未提交的修改）時若在日誌上衝突，同樣依 append-only 合併，
  # 並清空暫存區，讓那些修改維持「未暫存」，留給它們的主人自己提交。
  if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
    if [ -n "$PY" ] && only_log_conflict && git stash list | head -1 | grep -q 'autostash'; then
      echo "    放回其他代理的未提交修改時 wiki/log.md 衝突，自動併入..."
      PYTHONIOENCODING=utf-8 "$PY" "$SCRIPT_DIR/merge_log.py"
      git reset -q
      git stash drop -q
    else
      echo "ERROR: 放回未提交修改時發生衝突，修改仍保存在 git stash 中；請人工處理後再推送。"
      exit 1
    fi
  fi
  git reset -q   # 放回的修改可能被加入暫存區，一律清空，避免下次提交誤帶他人檔案
fi

# 4. 推送並確認對齊。
AHEAD=$(git rev-list --count origin/main..HEAD)
if [ "$AHEAD" -gt 0 ]; then
  echo "    推送 $AHEAD 個提交到 origin main..."
  git push origin main
fi
git fetch origin main --quiet
AHEAD_AFTER=$(git rev-list --count origin/main..HEAD)
if [ "$AHEAD_AFTER" -eq 0 ]; then
  echo "    Success: Fully synchronized with origin/main (Ahead: 0)."
else
  echo "    ERROR: Push failed or local still ahead by $AHEAD_AFTER commit(s)."
  exit 1
fi

REMAINING=$(git status --porcelain)
if [ -n "$REMAINING" ]; then
  echo "    工作目錄仍有未提交的修改（可能屬於其他代理，本腳本不會處理）："
  echo "$REMAINING" | sed 's/^/    /'
fi
echo "=================================================="
