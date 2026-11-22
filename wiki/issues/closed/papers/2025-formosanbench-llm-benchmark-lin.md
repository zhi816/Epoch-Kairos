# 已結案問題：papers/2025-formosanbench-llm-benchmark-lin.md

> 本檔收錄 [wiki/papers/2025-formosanbench-llm-benchmark-lin.md](../../../papers/2025-formosanbench-llm-benchmark-lin.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-077 | fixed | papers/2025-formosanbench-llm-benchmark-lin.md | Card 2、Card 3 與 Card 6 | 原文不符
- **問題**：（1）Card 3（第 50 行）將資料點寫為含英語譯文與語音對齊之五元組；原文 §4（pp. 16529–16530，表 1）之三項任務取自三個彼此獨立之資料源（MT 取自原民會線上辭典族華句對且無英語譯文、ASR 取自族語 E 樂園教材音檔、摘要取自族語維基百科條目與首段），並非同源五元組。（2）Card 3 架構圖（第 72 行）列出 `chrF++` 與 `SBERT` 指標；原文 §5.3（p. 16532）僅使用 BLEU、WER、ROUGE-2／ROUGE-L、GPT-4o-mini 評分（1–5 分）與人工評估，未使用 `chrF++` 或 `SBERT`。（3）Card 2（第 37 行）與 Card 6（第 99 行）稱「論文揭示的 4~6 倍 Tokenizer 膨脹問題」；誠如 Card 4（第 81 行）已註明，原文並未測量或報告 Tokenizer 膨脹倍率。
- **來源**：`raw/my-focus/英文論文/FormosanBench Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models _ 2025.findings-emnlp.897.pdf`（§4 pp. 16529–16530 表 1、§5.3 p. 16532）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：Card 3 刪除「同源五元組」與 ICL 公式，改列三項任務之獨立資料來源（線上辭典、族語 E 樂園、族語維基百科）；評估指標改為原文之 BLEU、WER、ROUGE-2／L、GPT-4o-mini 評審與人工檢視；Card 2、Card 6 刪除原文未報告之「4~6 倍 Tokenizer 膨脹」。另修正同頁未登記之問題：Card 4 補列表 2–6 主要數值與母語者人工檢視結果；註明原文三處不一致：表 1 切分約 60:10:30 而非文稱 70:10:20、表 2 BLEU 看似 0–1 尺度、§6.1 對 LLM 評審分數方向之解讀與表 3 相反；刪除 Card 5「終結無基準可評」「指明必須開發形態解析外掛」等表述。證據表見 wiki/evidence/2025-formosanbench-llm-benchmark-lin.md。
