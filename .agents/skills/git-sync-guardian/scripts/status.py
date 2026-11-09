#!/usr/bin/env python3
"""status.py: Dual-repository status inspector for Epoch-Kairos and Mine-RAW.

Cross-platform Python equivalent of status.sh (runs natively in Windows PowerShell,
macOS, and Linux without requiring Bash). Does not silently swallow `git fetch`
errors: if fetching remote state fails (e.g. sandbox blocking .git/FETCH_HEAD or
network offline), it prints a clear warning with the Git error and exits with code 1
after reporting local status, so agents never mistake stale cached refs for fresh ones.
Zero emoji constraint strictly enforced.
"""
import argparse
import os
import subprocess
import sys
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))


def run_git(cwd, *args):
    return subprocess.run(
        ['git', '-C', cwd, *args],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
    )


def checked_git_out(cwd, description, *args, default='unknown'):
    r = run_git(cwd, *args)
    if r.returncode == 0:
        return r.stdout.strip(), True
    err_msg = (r.stderr or r.stdout or '').strip()
    print(f'    ERROR: {description} failed (exit code {r.returncode}).')
    if err_msg:
        for line in err_msg.splitlines():
            print(f'      {line}')
    return default, False


def inspect_repo(index, label, repo_path, allow_offline=False):
    print(f'[{index}] {label}: {repo_path}')
    if not os.path.isdir(os.path.join(repo_path, '.git')):
        print(f'    Not detected at {repo_path}')
        return True

    fetch_ok = True
    fetch_res = run_git(repo_path, 'fetch', 'origin', 'main', '--quiet')
    if fetch_res.returncode != 0:
        fetch_ok = False
        err_msg = (fetch_res.stderr or fetch_res.stdout or '').strip()
        print(f'    WARNING: git fetch origin main failed (exit code {fetch_res.returncode})!')
        if err_msg:
            for line in err_msg.splitlines():
                print(f'      {line}')
        print('    WARNING: Remote commit and Ahead/Behind counts below are STALE (check network or .git write permissions).')

    inspection_ok = True
    branch, ok = checked_git_out(repo_path, 'current branch query', 'rev-parse', '--abbrev-ref', 'HEAD')
    inspection_ok = inspection_ok and ok
    local_rev, ok = checked_git_out(repo_path, 'local commit query', 'rev-parse', 'HEAD')
    inspection_ok = inspection_ok and ok
    remote_rev, ok = checked_git_out(repo_path, 'origin/main query', 'rev-parse', 'origin/main')
    inspection_ok = inspection_ok and ok
    ahead, ok = checked_git_out(repo_path, 'ahead count query', 'rev-list', '--count', 'origin/main..HEAD')
    inspection_ok = inspection_ok and ok
    behind, ok = checked_git_out(repo_path, 'behind count query', 'rev-list', '--count', 'HEAD..origin/main')
    inspection_ok = inspection_ok and ok
    status_res = run_git(repo_path, 'status', '--porcelain')
    if status_res.returncode == 0:
        status_text = status_res.stdout.rstrip('\r\n')
    else:
        inspection_ok = False
        status_text = None
        err_msg = (status_res.stderr or status_res.stdout or '').strip()
        print(f'    ERROR: git status failed (exit code {status_res.returncode}); working-tree state is unknown.')
        if err_msg:
            for line in err_msg.splitlines():
                print(f'      {line}')

    print(f'    Branch: {branch}')
    print(f'    Local commit:  {local_rev}')
    print(f'    Remote commit: {remote_rev}' + ('' if fetch_ok else ' (STALE - fetch failed)'))
    print(f'    Ahead: {ahead} | Behind: {behind}' + ('' if fetch_ok else ' (STALE - fetch failed)'))
    if status_text is None:
        print('    Working tree: UNKNOWN (git status failed)')
    elif status_text:
        print('    Uncommitted changes:')
        for line in status_text.splitlines():
            print(f'      {line}')
    else:
        print('    Working tree: Clean')

    return inspection_ok and (fetch_ok or allow_offline)


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass

    ap = argparse.ArgumentParser(description='Dual-repository status inspector for Epoch-Kairos and Mine-RAW')
    ap.add_argument('--allow-offline', action='store_true',
                    help='Return exit code 0 even if git fetch fails (warnings are still printed)')
    args = ap.parse_args()

    print('==================================================')
    print('Dual-Repository Status Check')
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('==================================================')

    ok_main = inspect_repo(1, 'Main Repository (Epoch-Kairos)', REPO_ROOT, args.allow_offline)
    print('--------------------------------------------------')
    raw_dir = os.path.join(REPO_ROOT, 'raw')
    if os.path.isdir(os.path.join(raw_dir, '.git')):
        ok_raw = inspect_repo(2, 'Private Raw Repository (Mine-RAW)', raw_dir, args.allow_offline)
    else:
        print(f'[2] Private Raw Repository (Mine-RAW): Not detected at {raw_dir}')
        ok_raw = True

    print('==================================================')
    if not (ok_main and ok_raw):
        print('ERROR: One or more repository checks failed; see the warnings above.', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
