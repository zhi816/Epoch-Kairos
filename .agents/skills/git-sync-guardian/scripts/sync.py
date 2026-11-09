#!/usr/bin/env python3
"""sync.py: Safe pre-flight synchronization across Epoch-Kairos and Mine-RAW.

Cross-platform Python equivalent of sync.sh (runs natively in Windows PowerShell,
macOS, and Linux without requiring Bash).
Zero emoji constraint strictly enforced.
"""
import os
import subprocess
import sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..', '..'))


def run_git(cwd, *args):
    return subprocess.run(
        ['git', '-C', cwd, *args],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
    )


def git_out(cwd, *args, default=''):
    r = run_git(cwd, *args)
    return r.stdout.strip() if r.returncode == 0 else default


def only_log_conflict(cwd):
    unmerged = git_out(cwd, 'diff', '--name-only', '--diff-filter=U')
    return unmerged == 'wiki/log.md'


def has_unmerged(cwd):
    return bool(git_out(cwd, 'diff', '--name-only', '--diff-filter=U'))


def top_stash_is_autostash(cwd):
    stash_list = git_out(cwd, 'stash', 'list')
    first_line = stash_list.splitlines()[0] if stash_list else ''
    return 'autostash' in first_line


def run_merge_log(cwd):
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    r = subprocess.run(
        [sys.executable, os.path.join(SCRIPT_DIR, 'merge_log.py')],
        cwd=cwd,
        env=env,
    )
    return r.returncode == 0


def merge_remote(cwd, ff_only=False):
    args = ['merge']
    if ff_only:
        args.append('--ff-only')
    args.extend(['--autostash', '--no-edit', 'origin/main'])

    res = subprocess.run(['git', '-C', cwd, *args])
    if res.returncode != 0:
        if only_log_conflict(cwd):
            if not run_merge_log(cwd):
                return False
            if run_git(cwd, 'add', 'wiki/log.md').returncode != 0:
                return False
            subprocess.run(['git', '-C', cwd, 'commit', '-q', '--no-edit'])
        else:
            return False

    if has_unmerged(cwd):
        if only_log_conflict(cwd) and top_stash_is_autostash(cwd):
            if not run_merge_log(cwd):
                return False
            run_git(cwd, 'reset', '-q')
            run_git(cwd, 'stash', 'drop', '-q')
        else:
            print('    ERROR: 放回未提交修改時發生衝突，修改仍保存在 git stash 中，請人工處理。', file=sys.stderr)
            return False

    run_git(cwd, 'reset', '-q')
    return True


def sync_repo(repo_name, repo_path):
    print(f'>>> Checking {repo_name} ({repo_path})...')
    if not os.path.isdir(os.path.join(repo_path, '.git')):
        print(f'    Warning: Git directory not found at {repo_path}. Skipping.')
        return True

    fetch_res = subprocess.run(['git', '-C', repo_path, 'fetch', 'origin', 'main', '--tags'])
    if fetch_res.returncode != 0:
        print(f'    ERROR: git fetch failed in {repo_name} (check network or .git write permissions).', file=sys.stderr)
        return False

    ahead = int(git_out(repo_path, 'rev-list', '--count', 'origin/main..HEAD', default='0') or '0')
    behind = int(git_out(repo_path, 'rev-list', '--count', 'HEAD..origin/main', default='0') or '0')

    print(f'    Current state -> Ahead: {ahead}, Behind: {behind}')

    if behind == 0 and ahead == 0:
        print('    Status: Already up to date with origin/main.')
    elif behind > 0 and ahead == 0:
        print(f'    Status: Fast-forward pull available. Pulling {behind} incoming commit(s)...')
        if not merge_remote(repo_path, ff_only=True):
            return False
        print('    Successfully updated to latest remote commit.')
    elif behind > 0 and ahead > 0:
        print(f'    Status: Divergent branches detected (Local ahead by {ahead}, Remote ahead by {behind}).')
        print('    Attempting automatic merge...')
        if merge_remote(repo_path, ff_only=False):
            print('    Merge completed successfully.')
        else:
            print(f'    ERROR: Merge conflict detected in {repo_name}.', file=sys.stderr)
            print('    Please resolve conflicts manually (e.g. check wiki/log.md for append-only ordering) and commit.', file=sys.stderr)
            return False
    else:
        print(f'    Status: Local branch is ahead by {ahead} commit(s). Ready for push.')

    return True


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print('==================================================')
    print('Starting Dual-Repository Sync Operation')
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('==================================================')

    if not sync_repo('Epoch-Kairos (Main)', REPO_ROOT):
        sys.exit(1)
    if not sync_repo('Mine-RAW (Private)', os.path.join(REPO_ROOT, 'raw')):
        sys.exit(1)

    print('==================================================')
    print('Sync Operation Finished')
    print('==================================================')


if __name__ == '__main__':
    main()
