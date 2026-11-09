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
QUERY_FAILED=0

query_git() {
  local DESCRIPTION="$1"
  local DEFAULT="$2"
  shift 2
  if QUERY_VALUE=$(git "$@" 2>&1); then
    :
  else
    local QUERY_CODE=$?
    QUERY_FAILED=1
    echo "    ERROR: $DESCRIPTION failed (exit code $QUERY_CODE)." >&2
    if [ -n "$QUERY_VALUE" ]; then echo "$QUERY_VALUE" | sed 's/^/      /' >&2; fi
    QUERY_VALUE="$DEFAULT"
  fi
}

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
query_git "local commit query" "unknown" rev-parse HEAD; LOCAL_MAIN=$QUERY_VALUE
query_git "origin/main query" "unknown" rev-parse origin/main; REMOTE_MAIN=$QUERY_VALUE
query_git "ahead count query" "unknown" rev-list --count origin/main..HEAD; AHEAD_MAIN=$QUERY_VALUE
query_git "behind count query" "unknown" rev-list --count HEAD..origin/main; BEHIND_MAIN=$QUERY_VALUE
if STATUS_MAIN=$(git status --porcelain 2>&1); then
  STATUS_MAIN_UNKNOWN=0
else
  STATUS_CODE=$?
  QUERY_FAILED=1
  STATUS_MAIN_UNKNOWN=1
  echo "    ERROR: git status failed (exit code $STATUS_CODE); working-tree state is unknown." >&2
  echo "$STATUS_MAIN" | sed 's/^/      /' >&2
fi
STALE_MAIN=""
[ "$FETCH_MAIN_OK" -eq 0 ] && STALE_MAIN=" (STALE - fetch failed)"

query_git "current branch query" "unknown" rev-parse --abbrev-ref HEAD; BRANCH_MAIN=$QUERY_VALUE
echo "    Branch: $BRANCH_MAIN"
echo "    Local commit:  $LOCAL_MAIN"
echo "    Remote commit: $REMOTE_MAIN$STALE_MAIN"
echo "    Ahead: $AHEAD_MAIN | Behind: $BEHIND_MAIN$STALE_MAIN"
if [ "$STATUS_MAIN_UNKNOWN" -eq 1 ]; then
  echo "    Working tree: UNKNOWN (git status failed)"
elif [ -n "$STATUS_MAIN" ]; then
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
  query_git "local commit query" "unknown" rev-parse HEAD; LOCAL_RAW=$QUERY_VALUE
  query_git "origin/main query" "unknown" rev-parse origin/main; REMOTE_RAW=$QUERY_VALUE
  query_git "ahead count query" "unknown" rev-list --count origin/main..HEAD; AHEAD_RAW=$QUERY_VALUE
  query_git "behind count query" "unknown" rev-list --count HEAD..origin/main; BEHIND_RAW=$QUERY_VALUE
  if STATUS_RAW=$(git status --porcelain 2>&1); then
    STATUS_RAW_UNKNOWN=0
  else
    STATUS_CODE=$?
    QUERY_FAILED=1
    STATUS_RAW_UNKNOWN=1
    echo "    ERROR: git status failed (exit code $STATUS_CODE); working-tree state is unknown." >&2
    echo "$STATUS_RAW" | sed 's/^/      /' >&2
  fi
  STALE_RAW=""
  [ "$FETCH_RAW_OK" -eq 0 ] && STALE_RAW=" (STALE - fetch failed)"

  query_git "current branch query" "unknown" rev-parse --abbrev-ref HEAD; BRANCH_RAW=$QUERY_VALUE
  echo "    Branch: $BRANCH_RAW"
  echo "    Local commit:  $LOCAL_RAW"
  echo "    Remote commit: $REMOTE_RAW$STALE_RAW"
  echo "    Ahead: $AHEAD_RAW | Behind: $BEHIND_RAW$STALE_RAW"
  if [ "$STATUS_RAW_UNKNOWN" -eq 1 ]; then
    echo "    Working tree: UNKNOWN (git status failed)"
  elif [ -n "$STATUS_RAW" ]; then
    echo "    Uncommitted changes:"
    echo "$STATUS_RAW" | sed 's/^/      /'
  else
    echo "    Working tree: Clean"
  fi
else
  echo "[2] Private Raw Repository (Mine-RAW): Not detected at $RAW_DIR"
fi

echo "=================================================="
if [ "$QUERY_FAILED" -ne 0 ] || { [ "$FETCH_FAILED" -ne 0 ] && [ "$ALLOW_OFFLINE" -eq 0 ]; }; then
  echo "ERROR: One or more repository checks failed; see the warnings above." >&2
  exit 1
fi
