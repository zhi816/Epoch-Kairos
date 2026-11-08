#!/usr/bin/env bash
# scripts/sync.sh: Safe pre-flight synchronization across Epoch-Kairos and Mine-RAW
# Zero emoji constraint strictly enforced.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"

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
    git pull --ff-only origin main
    echo "    Successfully updated to latest remote commit."
  elif [ "$BEHIND" -gt 0 ] && [ "$AHEAD" -gt 0 ]; then
    echo "    Status: Divergent branches detected (Local ahead by $AHEAD, Remote ahead by $BEHIND)."
    echo "    Attempting automatic merge..."
    if git merge origin/main -m "Merge remote-tracking branch 'origin/main' into main (auto-sync)"; then
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
