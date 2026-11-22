# 已結案問題：papers/2026-malm-backtranslation-indic-mt-rao.md

> 本檔收錄 [wiki/papers/2026-malm-backtranslation-indic-mt-rao.md](../../../papers/2026-malm-backtranslation-indic-mt-rao.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-226 | fixed | papers/2026-malm-backtranslation-indic-mt-rao.md | Card 6 第 1–2 點 | 過度表述
- **問題**：第 1 點稱 MALM 的設計「證明」詞幹濾網能攔截偏離句並保留有效合成訊號；第 2 點稱四種語料規模「證明」約 50,000 句是資源轉折門檻，並把結果歸因於反向模型有限精度造成的分佈偏差。原文表 5 與 §5 比較「MALM 過濾回譯加官方語料」和「僅官方語料」，可支持這兩種訓練配置的結果差異，不能單獨驗證濾網辨識噪聲的能力或其因果貢獻；作者也將「未過濾合成資料」與「MALM 過濾資料」的直接比較列為未來工作。四個方向的結果亦不足以證明普遍適用的 50,000 句門檻或未經測量的有限精度／分佈偏差機制。
- **來源**：[原文 PDF](../../../../raw/my-focus/報告論文題材/2026.wmt-main.160.pdf)，印刷頁 2211（PDF p. 5），§5、Table 5、§6。
- **發現於**：wiki/log.md [2026-11-14 15:38] audit（Codex by OpenAI）。
- **處理**：2026-11-20，DeepSeek Harness（DeepSeek V4.1 Flash）改寫、Command Code（MiniMax M3.1 Flash、GLM-5.3 Flash）審查，Claude Code by Anthropic（Claude Opus 5.5）回原文核對。論文頁改為我的關注新六章：06「讀的時候要留意」寫明表 5 只比較加過濾回譯與僅官方語料、未比未過濾回譯；「官方語料夠大後合成資料反而加噪聲」改為作者依阿薩姆與米佐結果之推測（原文 suggest）；刪除「證明」、50,000 句普遍門檻與有限精度、分佈偏差等原文沒有的斷言；證據表新增兩列。
