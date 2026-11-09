#!/usr/bin/env bash
# scripts/status.sh: Dual-repository status inspector for Epoch-Kairos and Mine-RAW
# Zero emoji constraint strictly enforced.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"

ALLOW_OFFLINE=0
if [ "${1:-}" = "--allow-offline" ]; then
  ALLOW_OFFLINE=1
fi
FETCH_FAILED=0

echo "=================================================="
echo "Dual-Repository Status Check"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo "=================================================="

# 1. Main Repository (Epoch-Kairos)
echo "[1] Main Repository (Epoch-Kairos): $REPO_ROOT"
cd "$REPO_ROOT"

FETCH_MAIN_OK=1
if ! FETCH_ERR=$(git fetch origin main --quiet 2>&1); then
  FETCH_MAIN_OK=0
  FETCH_FAILED=1
  echo "    WARNING: git fetch origin main failed!"
  if [ -n "$FETCH_ERR" ]; then
    echo "$FETCH_ERR" | sed 's/^/      /'
  fi
  echo "    WARNING: Remote commit and Ahead/Behind counts below are STALE (check network or .git write permissions)."
fi
LOCAL_MAIN=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
REMOTE_MAIN=$(git rev-parse origin/main 2>/dev/null || echo "unknown")
AHEAD_MAIN=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "0")
BEHIND_MAIN=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "0")
STATUS_MAIN=$(git status --porcelain)
STALE_MAIN=""
[ "$FETCH_MAIN_OK" -eq 0 ] && STALE_MAIN=" (STALE - fetch failed)"

echo "    Branch: $(git rev-parse --abbrev-ref HEAD)"
echo "    Local commit:  $LOCAL_MAIN"
echo "    Remote commit: $REMOTE_MAIN$STALE_MAIN"
echo "    Ahead: $AHEAD_MAIN | Behind: $BEHIND_MAIN$STALE_MAIN"
if [ -n "$STATUS_MAIN" ]; then
  echo "    Uncommitted changes:"
  echo "$STATUS_MAIN" | sed 's/^/      /'
else
  echo "    Working tree: Clean"
fi

echo "--------------------------------------------------"

# 2. Private Repository (Mine-RAW in raw/)
RAW_DIR="$REPO_ROOT/raw"
if [ -d "$RAW_DIR/.git" ]; then
  echo "[2] Private Raw Repository (Mine-RAW): $RAW_DIR"
  cd "$RAW_DIR"

  FETCH_RAW_OK=1
  if ! FETCH_RAW_ERR=$(git fetch origin main --quiet 2>&1); then
    FETCH_RAW_OK=0
    FETCH_FAILED=1
    echo "    WARNING: git fetch origin main failed!"
    if [ -n "$FETCH_RAW_ERR" ]; then
      echo "$FETCH_RAW_ERR" | sed 's/^/      /'
    fi
    echo "    WARNING: Remote commit and Ahead/Behind counts below are STALE (check network or .git write permissions)."
  fi
  LOCAL_RAW=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
  REMOTE_RAW=$(git rev-parse origin/main 2>/dev/null || echo "unknown")
  AHEAD_RAW=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "0")
  BEHIND_RAW=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "0")
  STATUS_RAW=$(git status --porcelain)
  STALE_RAW=""
  [ "$FETCH_RAW_OK" -eq 0 ] && STALE_RAW=" (STALE - fetch failed)"

  echo "    Branch: $(git rev-parse --abbrev-ref HEAD)"
  echo "    Local commit:  $LOCAL_RAW"
  echo "    Remote commit: $REMOTE_RAW$STALE_RAW"
  echo "    Ahead: $AHEAD_RAW | Behind: $BEHIND_RAW$STALE_RAW"
  if [ -n "$STATUS_RAW" ]; then
    echo "    Uncommitted changes:"
    echo "$STATUS_RAW" | sed 's/^/      /'
  else
    echo "    Working tree: Clean"
  fi
else
  echo "[2] Private Raw Repository (Mine-RAW): Not detected at $RAW_DIR"
fi

echo "=================================================="
if [ "$FETCH_FAILED" -ne 0 ] && [ "$ALLOW_OFFLINE" -eq 0 ]; then
  echo "ERROR: One or more repositories failed to fetch from origin/main (see WARNING above)." >&2
  exit 1
fi
