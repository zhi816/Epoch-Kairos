# 已結案問題：papers/2024-formosan-mt-bilingual-lexicon-zheng.md

> 本檔收錄 [wiki/papers/2024-formosan-mt-bilingual-lexicon-zheng.md](../../../papers/2024-formosan-mt-bilingual-lexicon-zheng.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-076 | fixed | papers/2024-formosan-mt-bilingual-lexicon-zheng.md | Card 3 | 原文不符
- **問題**：第 45–68 行稱本文採溫度採樣係數 $\tau$、動態衰減權重 $\beta \in (0, 1]$ 之混合損失函數，並定義交叉注意力香農熵；原文 §4–§5（pp. 11251–11254）全文無任何數學公式，方法一（`+ Lex.`）僅將雙語詞典詞條與平行句直接串接訓練，方法二（`+ PPD`，§5.1）則隨機替換平行句中 20% 族語詞彙合成偽平行資料，方法三為兩者結合。Card 3 完全漏述產生最佳成績（+5.55 BLEU／+10.33 chrF）之方法二 PPD，卻虛構溫度採樣、動態權重與注意力熵公式。
- **來源**：`raw/my-focus/英文論文/Improving Low-Resource Machine Translation for Formosan Languages _ 2024.findings-acl.670v2.pdf`（§4–§5 pp. 11251–11254）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3–§5 核對後：Card 3 刪除原文未出現之溫度採樣、動態衰減權重 $\beta$ 與注意力熵公式，改述原文三種做法——詞典直接作為平行資料、以詞典替換族語端詞彙產生偽平行資料（多以 20% 替換率最佳）、兩者並用。另修正同頁未登記之問題：Card 4 補列表 2（16 種語言全部提升，平均 +3.37 BLEU）、平行句比詞條更有用、外部詞典增益較小，以及多語言預訓練無明確改善之負面結果；刪除 Card 5「登上 ACL 讓臺灣南島語站上世界舞台」等表述；補列作者自述之限制。證據表見 wiki/evidence/2024-formosan-mt-bilingual-lexicon-zheng.md。
