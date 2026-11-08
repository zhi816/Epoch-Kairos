#!/usr/bin/env bash
# scripts/safe_commit_push.sh: Atomic Commit-and-Push Guardian for Epoch-Kairos and Mine-RAW
# Rule: Whenever changes are committed, they MUST be pushed immediately.
# Zero emoji constraint strictly enforced.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"

usage() {
  echo "Usage: $0 \"<commit_message>\" [main|raw|both]"
  echo "Example: $0 \"docs(wiki): update log for paper ingestion\" main"
  echo "Example: $0 \"feat(raw): add translated pdfs\" raw"
  exit 1
}

if [ -z "$1" ]; then
  usage
fi

COMMIT_MSG="$1"
TARGET="${2:-both}"

commit_and_push_repo() {
  local REPO_NAME="$1"
  local REPO_PATH="$2"

  echo ">>> Processing $REPO_NAME ($REPO_PATH)..."
  if [ ! -d "$REPO_PATH/.git" ]; then
    echo "    Warning: Git directory not found at $REPO_PATH. Skipping."
    return 0
  fi

  cd "$REPO_PATH"

  # Pre-flight check: fetch remote
  git fetch origin main --quiet 2>/dev/null || true
  BEHIND=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "0")
  if [ "$BEHIND" -gt 0 ]; then
    echo "    Notice: Remote has $BEHIND incoming commit(s). Merging before commit/push..."
    git merge origin/main -m "Merge remote-tracking branch 'origin/main' into main (pre-commit sync)"
  fi

  # Check uncommitted changes
  STATUS=$(git status --porcelain)
  AHEAD_EXISTING=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "0")

  if [ -z "$STATUS" ] && [ "$AHEAD_EXISTING" -eq 0 ]; then
    echo "    Status: No modified files and no pending commits. Nothing to do."
    return 0
  fi

  if [ -n "$STATUS" ]; then
    echo "    Staging changes and creating commit..."
    git add -A
    git commit -m "$COMMIT_MSG"
  else
    echo "    Found $AHEAD_EXISTING existing unpushed commit(s). Proceeding to push..."
  fi

  # Atomic push
  echo "    Pushing to origin main..."
  git push origin main

  # Post-push verification
  AHEAD_AFTER=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "0")
  if [ "$AHEAD_AFTER" -eq 0 ]; then
    echo "    Success: Fully synchronized with origin/main (Ahead: 0)."
  else
    echo "    ERROR: Push failed or local still ahead by $AHEAD_AFTER commit(s)."
    return 1
  fi
}

echo "=================================================="
echo "Atomic Commit-and-Push Guardian"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Target: $TARGET"
echo "Message: $COMMIT_MSG"
echo "=================================================="

case "$TARGET" in
  main)
    commit_and_push_repo "Epoch-Kairos (Main)" "$REPO_ROOT"
    ;;
  raw)
    commit_and_push_repo "Mine-RAW (Private)" "$REPO_ROOT/raw"
    ;;
  both)
    commit_and_push_repo "Epoch-Kairos (Main)" "$REPO_ROOT"
    commit_and_push_repo "Mine-RAW (Private)" "$REPO_ROOT/raw"
    ;;
  *)
    echo "Unknown target '$TARGET'. Expected 'main', 'raw', or 'both'."
    usage
    ;;
esac

echo "=================================================="
echo "All Target Repositories Pushed and Synchronized"
echo "=================================================="
