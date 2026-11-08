#!/usr/bin/env bash
# scripts/sync.sh: Safe pre-flight synchronization across Epoch-Kairos and Mine-RAW
# Zero emoji constraint strictly enforced.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY=""
for cand in python3 python py; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c "import sys" >/dev/null 2>&1; then PY="$cand"; break; fi
done

# 合流時以 --autostash 暫收工作目錄中其他代理尚未提交的修改；若 wiki/log.md 衝突，依 append-only 自動合併。
merge_remote() {
  local MODE="$1"
  local only_log='[ "$(git diff --name-only --diff-filter=U)" = "wiki/log.md" ]'
  if ! git merge $MODE --autostash --no-edit origin/main; then
    if [ -n "$PY" ] && eval "$only_log"; then
      PYTHONIOENCODING=utf-8 "$PY" "$SCRIPT_DIR/merge_log.py" && git add wiki/log.md && { git commit -q --no-edit || true; }
    else
      return 1
    fi
  fi
  if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
    if [ -n "$PY" ] && eval "$only_log" && git stash list | head -1 | grep -q 'autostash'; then
      PYTHONIOENCODING=utf-8 "$PY" "$SCRIPT_DIR/merge_log.py" && git reset -q && git stash drop -q
    else
      echo "    ERROR: 放回未提交修改時發生衝突，修改仍保存在 git stash 中，請人工處理。"
      return 1
    fi
  fi
  git reset -q
}

sync_repo() {
  local REPO_NAME="$1"
  local REPO_PATH="$2"

  echo ">>> Checking $REPO_NAME ($REPO_PATH)..."
  if [ ! -d "$REPO_PATH/.git" ]; then
    echo "    Warning: Git directory not found at $REPO_PATH. Skipping."
    return 0
  fi

  cd "$REPO_PATH"

  # Fetch latest remote information
  git fetch origin main --tags

  AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "0")
  BEHIND=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "0")

  echo "    Current state -> Ahead: $AHEAD, Behind: $BEHIND"

  if [ "$BEHIND" -eq 0 ] && [ "$AHEAD" -eq 0 ]; then
    echo "    Status: Already up to date with origin/main."
  elif [ "$BEHIND" -gt 0 ] && [ "$AHEAD" -eq 0 ]; then
    echo "    Status: Fast-forward pull available. Pulling $BEHIND incoming commit(s)..."
    merge_remote --ff-only || return 1
    echo "    Successfully updated to latest remote commit."
  elif [ "$BEHIND" -gt 0 ] && [ "$AHEAD" -gt 0 ]; then
    echo "    Status: Divergent branches detected (Local ahead by $AHEAD, Remote ahead by $BEHIND)."
    echo "    Attempting automatic merge..."
    if merge_remote ""; then
      echo "    Merge completed successfully."
    else
      echo "    ERROR: Merge conflict detected in $REPO_NAME."
      echo "    Please resolve conflicts manually (e.g. check wiki/log.md for append-only ordering) and commit."
      return 1
    fi
  else
    echo "    Status: Local branch is ahead by $AHEAD commit(s). Ready for push."
  fi
}

echo "=================================================="
echo "Starting Dual-Repository Sync Operation"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo "=================================================="

# 1. Sync Main Repo
sync_repo "Epoch-Kairos (Main)" "$REPO_ROOT"

# 2. Sync Raw Repo
sync_repo "Mine-RAW (Private)" "$REPO_ROOT/raw"

echo "=================================================="
echo "Sync Operation Finished"
echo "=================================================="
