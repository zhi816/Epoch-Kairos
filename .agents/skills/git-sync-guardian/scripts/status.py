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


def git_out(cwd, *args, default=''):
    r = run_git(cwd, *args)
    return r.stdout.strip() if r.returncode == 0 else default


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

    branch = git_out(repo_path, 'rev-parse', '--abbrev-ref', 'HEAD', default='unknown')
    local_rev = git_out(repo_path, 'rev-parse', 'HEAD', default='unknown')
    remote_rev = git_out(repo_path, 'rev-parse', 'origin/main', default='unknown')
    ahead = git_out(repo_path, 'rev-list', '--count', 'origin/main..HEAD', default='0')
    behind = git_out(repo_path, 'rev-list', '--count', 'HEAD..origin/main', default='0')
    status_res = run_git(repo_path, 'status', '--porcelain')
    status_text = status_res.stdout.rstrip('\r\n') if status_res.returncode == 0 else ''

    print(f'    Branch: {branch}')
    print(f'    Local commit:  {local_rev}')
    print(f'    Remote commit: {remote_rev}' + ('' if fetch_ok else ' (STALE - fetch failed)'))
    print(f'    Ahead: {ahead} | Behind: {behind}' + ('' if fetch_ok else ' (STALE - fetch failed)'))
    if status_text:
        print('    Uncommitted changes:')
        for line in status_text.splitlines():
            print(f'      {line}')
    else:
        print('    Working tree: Clean')

    return fetch_ok or allow_offline


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
        print('ERROR: One or more repositories failed to fetch from origin/main (see WARNING above).', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
