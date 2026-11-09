#!/usr/bin/env python3
"""safe_commit_push.py: Atomic Commit-and-Push Guardian for Epoch-Kairos and Mine-RAW.

Cross-platform Python equivalent of safe_commit_push.sh (runs natively in Windows
PowerShell, macOS, and Linux without requiring Bash).
Rule 1: Whenever changes are committed, they MUST be pushed immediately.
Rule 5: Commit ONLY your own changes. Several AIs share one working tree, so this script
        never runs `git add -A` / `git add .`; every path must be listed explicitly, and
        wiki/log.md, wiki/issues.md, wiki/todo.md are staged entry by entry.
Zero emoji constraint strictly enforced.
"""
import os
import subprocess
import sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..', '..'))


def usage():
    prog = os.path.basename(sys.argv[0])
    print(f'Usage: python .agents/skills/git-sync-guardian/scripts/{prog} "<commit_message>" <main|raw> --agent "<執行代理名稱>" [--log-heading "<exact heading>"] [--issue EK-NNN ...] [--todo TD-NNN ...] [--allow-stale-log] -- <path> [<path> ...]')
    print('')
    print('  main | raw   要提交的倉庫：main 為 Epoch-Kairos，raw 為 raw/ 內的 Mine-RAW。')
    print('               兩邊都有修改時請分別執行兩次（各自列出自己的檔案）。')
    print('  --agent      執行代理名稱的一部分（例如 "Claude Code"、"Codex"、"Antigravity"），')
    print('               用來挑出 wiki/log.md 中自己寫的條目。列出 wiki/log.md 時為必填。')
    print('  --log-heading  只提交指定的新日誌標題；可重複使用，供同代理多個工作階段並行時精確選取。')
    print('  --issue      提交 wiki/issues.md 時必填：只提交這些編號的條目（可重複）；其他代理的修改留在工作目錄。')
    print('  --todo       提交 wiki/todo.md 時必填：只提交這些編號的條目新增、修改或刪除（可重複）。')
    print('  --allow-stale-log  允許日誌標題時間早於現在 60 分鐘以上（僅限推送失敗後重試等情形）。')
    print('               日誌標題時間一律先以 scripts/log_time.py 取得；晚於現在 5 分鐘以上會被擋下。')
    print("  -- <path>    只會提交這些路徑（相對於該倉庫根目錄）。不接受 '.'、'-A' 或倉庫根目錄。")
    print('')
    print(f'Example: python .agents/skills/git-sync-guardian/scripts/{prog} "docs(design): update DESIGN.md" main --agent "Claude Code" -- DESIGN.md wiki/log.md')
    print(f'Example: python .agents/skills/git-sync-guardian/scripts/{prog} "feat(raw): add translated pdf" raw --agent "Codex" -- my-focus/英文論文/foo.pdf')
    sys.exit(1)


def run_git(cwd, *args, check=False):
    r = subprocess.run(
        ['git', '-C', cwd, *args],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
    )
    if check and r.returncode != 0:
        if r.stderr:
            sys.stderr.write(r.stderr)
        sys.exit(r.returncode)
    return r


def git_out(cwd, *args, default=''):
    r = run_git(cwd, *args)
    return r.stdout.strip() if r.returncode == 0 else default


def run_helper(cwd, script_name, args):
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    r = subprocess.run(
        [sys.executable, os.path.join(SCRIPT_DIR, script_name), *args],
        cwd=cwd,
        env=env,
    )
    return r.returncode == 0


def reset_paths(cwd, paths):
    run_git(cwd, 'reset', '-q', '--', *paths)


def only_log_conflict(cwd):
    return git_out(cwd, 'diff', '--name-only', '--diff-filter=U') == 'wiki/log.md'


def has_unmerged(cwd):
    return bool(git_out(cwd, 'diff', '--name-only', '--diff-filter=U'))


def top_stash_is_autostash(cwd):
    stash_list = git_out(cwd, 'stash', 'list')
    first_line = stash_list.splitlines()[0] if stash_list else ''
    return 'autostash' in first_line


def parse_cli(argv):
    if len(argv) < 4:
        usage()
    commit_msg = argv[0]
    target = argv[1]
    rest = argv[2:]

    agent = ''
    log_headings = []
    allow_stale = False
    issues = []
    todos = []

    idx = 0
    while idx < len(rest) and rest[idx] != '--':
        opt = rest[idx]
        if opt == '--agent' and idx + 1 < len(rest):
            agent = rest[idx + 1]
            idx += 2
        elif opt == '--log-heading' and idx + 1 < len(rest):
            log_headings.append(rest[idx + 1])
            idx += 2
        elif opt == '--allow-stale-log':
            allow_stale = True
            idx += 1
        elif opt == '--issue' and idx + 1 < len(rest):
            issues.append(rest[idx + 1])
            idx += 2
        elif opt == '--todo' and idx + 1 < len(rest):
            todos.append(rest[idx + 1])
            idx += 2
        else:
            print(f"Unknown option '{opt}'.")
            usage()

    if idx >= len(rest) or rest[idx] != '--':
        usage()
    paths = rest[idx + 1:]
    if not paths:
        print('ERROR: 未列出任何要提交的檔案。')
        usage()

    return commit_msg, target, agent, log_headings, allow_stale, issues, todos, paths


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass

    commit_msg, target, agent, log_headings, allow_stale, issues, todos, paths = parse_cli(sys.argv[1:])

    if target == 'main':
        repo_name = 'Epoch-Kairos (Main)'
        repo_path = REPO_ROOT
    elif target == 'raw':
        repo_name = 'Mine-RAW (Private)'
        repo_path = os.path.join(REPO_ROOT, 'raw')
    else:
        print(f"Unknown target '{target}'. Expected 'main' or 'raw'.")
        usage()

    print('==================================================')
    print('Atomic Commit-and-Push Guardian')
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f'Target: {repo_name}')
    print(f"Agent: {agent or '（未指定）'}")
    print(f'Message: {commit_msg}')
    print('==================================================')

    if not os.path.isdir(os.path.join(repo_path, '.git')):
        print(f'ERROR: Git directory not found at {repo_path}.')
        sys.exit(1)

    # 0. 索引必須是乾淨的：若已有別人暫存的檔案，提交會把它們一起帶走。
    prestaged = git_out(repo_path, 'diff', '--cached', '--name-only')
    if prestaged:
        print('ERROR: 暫存區已有檔案（可能是其他代理暫存的），為避免誤提交，已中止：')
        for line in prestaged.splitlines():
            print(f'    {line}')
        print('請確認這些檔案的歸屬；若確定是自己的，請把它們加入 -- 之後的清單並先執行 git reset 清空暫存區。')
        sys.exit(1)

    # 1. 只暫存明確列出的路徑；共用檔案逐條暫存。
    for p in paths:
        norm_p = p.replace('\\', '/')
        if norm_p in ('.', './', '-A', '--all', '*'):
            reset_paths(repo_path, paths)
            print(f"ERROR: 不接受 '{p}'；請逐一列出自己的檔案。")
            sys.exit(1)
        if norm_p == 'wiki/log.md' and target == 'main':
            if not agent:
                reset_paths(repo_path, paths)
                print('ERROR: 提交 wiki/log.md 時必須以 --agent 指定執行代理名稱。')
                sys.exit(1)
            stage_args = [agent]
            for h in log_headings:
                stage_args.extend(['--heading', h])
            if allow_stale:
                stage_args.append('--allow-stale')
            if not run_helper(repo_path, 'stage_log.py', stage_args):
                reset_paths(repo_path, paths)
                print('ERROR: 日誌暫存失敗（見上方訊息），已還原本次暫存，未提交任何內容。')
                sys.exit(1)
        elif norm_p == 'wiki/issues.md' and target == 'main':
            if not issues:
                reset_paths(repo_path, paths)
                print('ERROR: 提交 wiki/issues.md 時必須以 --issue EK-NNN 列出自己修改的問題編號（可重複），已還原本次暫存。')
                sys.exit(1)
            if not run_helper(repo_path, 'stage_issues.py', issues):
                reset_paths(repo_path, paths)
                print('ERROR: 問題清單暫存失敗（見上方訊息），已還原本次暫存，未提交任何內容。')
                sys.exit(1)
        elif norm_p == 'wiki/todo.md' and target == 'main':
            if not todos:
                reset_paths(repo_path, paths)
                print('ERROR: 提交 wiki/todo.md 時必須以 --todo TD-NNN 列出自己新增、修改或刪除的待辦編號（可重複），已還原本次暫存。')
                sys.exit(1)
            if not run_helper(repo_path, 'stage_todo.py', todos):
                reset_paths(repo_path, paths)
                print('ERROR: 待辦清單暫存失敗（見上方訊息），已還原本次暫存，未提交任何內容。')
                sys.exit(1)
        else:
            r = run_git(repo_path, 'add', '--', p)
            if r.returncode != 0:
                reset_paths(repo_path, paths)
                if r.stderr:
                    sys.stderr.write(r.stderr)
                sys.exit(r.returncode)

    print('    即將提交的檔案：')
    stat_out = git_out(repo_path, 'diff', '--cached', '--stat')
    if stat_out:
        for line in stat_out.splitlines():
            print(f'    {line}')

    # 2. 先提交自己的修改。
    if run_git(repo_path, 'diff', '--cached', '--quiet').returncode == 0:
        print('    暫存區沒有變更，不建立新提交。')
    else:
        run_git(repo_path, 'commit', '-q', '-m', commit_msg, check=True)
        print(f"    已建立提交：{git_out(repo_path, 'log', '--oneline', '-1')}")

    # 3. 再與遠端合流。--autostash 會暫時收起工作目錄中其他代理尚未提交的修改，合流後放回。
    run_git(repo_path, 'fetch', 'origin', 'main', '--quiet', check=True)
    behind = int(git_out(repo_path, 'rev-list', '--count', 'HEAD..origin/main', default='0') or '0')
    if behind > 0:
        print(f'    遠端領先 {behind} 個提交，進行三方合併...')
        merge_res = subprocess.run(['git', '-C', repo_path, 'merge', '--autostash', '--no-edit', 'origin/main'])
        if merge_res.returncode != 0:
            if target == 'main' and only_log_conflict(repo_path):
                print('    只有 wiki/log.md 衝突，依 append-only 原則自動合併（保留所有條目、依時間排序）...')
                if not run_helper(repo_path, 'merge_log.py', []):
                    sys.exit(1)
                run_git(repo_path, 'add', 'wiki/log.md', check=True)
                subprocess.run(['git', '-C', repo_path, 'commit', '-q', '--no-edit'])
            else:
                print('ERROR: 合併衝突。請依 SKILL.md SOP-3 人工排解並完成合併提交後再執行 git push origin main。')
                print('       若有 autostash，請以 git stash list 確認並還原。')
                sys.exit(1)

        if has_unmerged(repo_path):
            if only_log_conflict(repo_path) and top_stash_is_autostash(repo_path):
                print('    放回其他代理的未提交修改時 wiki/log.md 衝突，自動併入...')
                if not run_helper(repo_path, 'merge_log.py', []):
                    sys.exit(1)
                run_git(repo_path, 'reset', '-q')
                run_git(repo_path, 'stash', 'drop', '-q')
            else:
                print('ERROR: 放回未提交修改時發生衝突，修改仍保存在 git stash 中；請人工處理後再推送。')
                sys.exit(1)

        run_git(repo_path, 'reset', '-q')

    # 4. 推送並確認對齊。
    ahead = int(git_out(repo_path, 'rev-list', '--count', 'origin/main..HEAD', default='0') or '0')
    if ahead > 0:
        print(f'    推送 {ahead} 個提交到 origin main...')
        push_res = subprocess.run(['git', '-C', repo_path, 'push', 'origin', 'main'])
        if push_res.returncode != 0:
            sys.exit(push_res.returncode)

    run_git(repo_path, 'fetch', 'origin', 'main', '--quiet', check=True)
    ahead_after = int(git_out(repo_path, 'rev-list', '--count', 'origin/main..HEAD', default='0') or '0')
    if ahead_after == 0:
        print('    Success: Fully synchronized with origin/main (Ahead: 0).')
    else:
        print(f'    ERROR: Push failed or local still ahead by {ahead_after} commit(s).')
        sys.exit(1)

    remaining = git_out(repo_path, 'status', '--porcelain')
    if remaining:
        print('    工作目錄仍有未提交的修改（可能屬於其他代理，本腳本不會處理）：')
        for line in remaining.splitlines():
            print(f'    {line}')
    print('==================================================')


if __name__ == '__main__':
    main()
