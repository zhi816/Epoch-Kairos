# 已結案問題：concepts/ai-for-structural-biology.md

> 本檔收錄 [wiki/concepts/ai-for-structural-biology.md](../../../concepts/ai-for-structural-biology.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-052 | fixed | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文不符
- **問題**：稱 DrugCLIP 可「數秒」篩選百億級分子；原文為 6 billion 分子檢索少於 10,000 秒，GenomeScreenDB 規模約 10,000 個人類蛋白質、5 億化合物，全基因組篩選約 24 小時（8 張 A100）。
- **來源**：[DrugCLIP 封存原文](../../../../raw/2023-drugclip.pdf)、[論文紀錄](https://pubmed.ncbi.nlm.nih.gov/41505557/)、[計算配置](https://www.biorxiv.org/content/10.1101/2024.09.02.610777v3.full)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit、[2026-11-08 23:21] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 AI 驅動之結構生物學與分子設計概念頁：更正 DrugCLIP 單靶點 60 億 Enamine 分子檢索耗時為小於 10,000 秒（約 2.78 小時），刪除「數秒內完成百億級初篩」之誇大陳述，並客觀交代 GPU 叢集一日內完成全基因組尺度篩選之實況。建立證據表 wiki/evidence/ai-for-structural-biology.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。舊的數秒篩百億分子已刪，概念頁的「小於 2.8 小時」是由小於 10,000 秒換算出的保守上界，數學上成立；但未註明預先編碼並存於記憶體的條件、換算依據，也未交代原文同句括註約 30 小時與秒數矛盾。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Gao 等（2023）§4.3 寫明分子預先編碼並存於記憶體的條件，並並列少於 10,000 秒與約 30 小時的原文矛盾；Jia 等（2026）的八張 A100、約 24 小時配對評分另作後續研究，證據表逐項登記。

### EK-053 | fixed | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文未支持
- **問題**：把 AlphaFold 3＋FEP 描述成已實證之全原子誘導契合精排管線；AF3 原文報告的是複合體結構預測基準，應標為待驗證提案並另引直接驗證研究。
- **來源**：[AlphaFold 3 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 AI 驅動之結構生物學與分子設計概念頁：明確將 AlphaFold 3 複合體預測與自由能微擾（FEP）結合標明為計算生物學界正在探索的前沿整合策略，刪除將其寫成已實證成熟精排管線之過度表述。建立證據表 wiki/evidence/ai-for-structural-biology.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。概念頁已將成熟管線降為探索，但其「計算生物學界正在探索」AF3 與 FEP 結合的主張仍只由 AF3 原文及一般 FEP 文獻支撐，缺少直接例證；不得因此推定這類研究不存在，應補合適的一手研究或明確標為提案。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。將 AF3 與 FEP 的串接明標為 Wiki 提案，刪除未以直接來源支持的『研究界正在探索』及成熟精排暗示；證據表同步說明來源範圍。
