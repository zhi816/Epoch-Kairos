# 已結案問題：papers/2023-low-resource-nmt-survey-ranathunga.md

> 本檔收錄 [wiki/papers/2023-low-resource-nmt-survey-ranathunga.md](../../../papers/2023-low-resource-nmt-survey-ranathunga.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-075 | fixed | papers/2023-low-resource-nmt-survey-ranathunga.md | Card 1、Card 3 與 Card 6 | 原文不符
- **問題**：Card 1（第 17 行）與 Card 3（第 43–63 行）稱綜述建立四大支柱（含「語言學先驗融合：詞綴特徵拼接／投影、句法樹與詞典注入」及「輕量化 Adapter、參數高效微調 PEFT」）並列出含 $L_2$ 錨定項之遷移學習公式；Card 6（第 87 行）稱「綜述指出：在資料量小於一萬句的極端低資源語境中……真正的突破口在於構詞感知與外部符號知識庫的在線檢索（RAG）」。原文（ACM CSUR 2023，§3–§11，圖 1、2、7）將低資源 NMT 分為六類技術（資料增強、無監督、半監督、多語言、遷移學習、零樣本／樞紐），全文僅有一條 Google Scholar 離群值檢定公式（p. 229:22，式 1），決策流程圖（圖 7）以 50 萬句為低資源分界，且全文從未提及 RAG、LLM、Adapter 或 PEFT。
- **來源**：`raw/my-focus/英文論文/Neural Machine Translation for Low-resource Languages A Survey_3567592.pdf`（§3–§11 pp. 229:5–229:22 圖 1、2、7）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：Card 1、3 刪除「四大支柱」（含語言學先驗融合、Adapter、PEFT）與 $L_2$ 錨定遷移式，改列原文六類技術（資料增強、無監督、半監督、多語言、遷移學習、零樣本）與圖 7 選擇流程；Card 6 刪除「綜述指出一萬句以下應以構詞感知與 RAG 為突破口」，註明綜述資料截至 2021–2022 年，未涵蓋 LLM 與 RAG。另修正同頁未登記之問題：原 Card 4 稱「原文沒有提出語料門檻」不精確，改述原文以 50 萬／10 萬句為參考門檻並明言非絕對。證據表見 wiki/evidence/2023-low-resource-nmt-survey-ranathunga.md。
