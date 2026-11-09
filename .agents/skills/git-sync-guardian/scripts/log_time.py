#!/usr/bin/env python3
"""log_time.py: 輸出寫日誌標題用的目前時間（臺北時間，UTC+8），格式 YYYY-MM-DD HH:MM。

寫 wiki/log.md 標題前一律先執行本腳本，把輸出原樣貼進 `## [...]`，不得憑估計或記憶填寫。
跨平台（macOS、Linux、Windows）皆可執行，且不受本機時區設定影響：
    python .agents/skills/git-sync-guardian/scripts/log_time.py
"""
from datetime import datetime, timedelta, timezone

TAIPEI = timezone(timedelta(hours=8))  # 臺灣不實施日光節約時間


def now_taipei():
    return datetime.now(TAIPEI)


if __name__ == '__main__':
    print(now_taipei().strftime('%Y-%m-%d %H:%M'))
