# 已結案問題：papers/2019-generalized-data-augmentation-xia.md

> 本檔收錄 [wiki/papers/2019-generalized-data-augmentation-xia.md](../../../papers/2019-generalized-data-augmentation-xia.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-074 | fixed | papers/2019-generalized-data-augmentation-xia.md | Card 3 | 原文不符
- **問題**：（1）第 49–53 行稱以「字元級音變轉換模型」或構詞映射將高資源語言轉為低資源語言；原文 §3.1–3.2（pp. 5788–5789）實為透過正交 Procrustes SVD 與 CSLS 雙語詞典歸納進行逐詞替換（Word-by-word Substitution），或結合基於去噪自編碼與迭代回譯之改良無監督機器翻譯（M-UMT）。（2）第 56–59 行將 NMT 訓練寫為帶權重衰減係數 $\alpha_k$ 之加權對數似然；原文 §4.4（pp. 5790–5791）係將真實與偽平行語料直接串接預訓練後進行混合微調（mixed fine-tuning），無 $\alpha_k$ 加權目標式。
- **來源**：`raw/my-focus/英文論文/Generalized Data Augmentation for Low-Resource Translation_P19-1579.pdf`（§3.1–3.2 pp. 5788–5789、§4.4 pp. 5790–5791）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §2–§5 核對後：Card 3 刪除「字元級音變轉換」與 $\alpha_k$ 加權目標式，改述原文之 Procrustes／SVD＋CSLS 詞典歸納逐詞替換、M-UMT 修飾，以及預訓練後混合微調；補列原文四種增強情境。另修正同頁未登記之問題：Card 4 補列表 2 主要列；刪除 Card 5「被 mBART、NLLB 沿用」等無來源表述；Card 6 改為有條件之延伸。證據表見 wiki/evidence/2019-generalized-data-augmentation-xia.md。

### EK-191 | fixed | papers/2019-generalized-data-augmentation-xia.md | 證據表 Card 3 公式列 | 原文不符
- **問題**：[證據表](../../../evidence/2019-generalized-data-augmentation-xia.md) Card 3 的 Procrustes 約束漏掉左側 W 並有不成對的公式分隔符；論文頁與卡片目前使用的約束為 $W^\top W = I$，須同步修正證據表。此為 EK-074 原先方法與加權目標式問題以外的新缺口。
- **來源**：[Xia 等原文](https://aclanthology.org/P19-1579.pdf) §3.1，p. 5788；[論文頁](../../../papers/2019-generalized-data-augmentation-xia.md) Card 3。
- **發現於**：2026-11-10，使用者提供之分組複核，Codex by OpenAI 再查原文。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 §3.1 p. 5788 頁面影像，修正證據表約束為 $W^\top W = I$ 並補齊公式分隔符；論文頁與卡片原已一致。此頁僅修正已登記問題，verification 改為 partial。

### EK-228 | fixed | papers/2019-generalized-data-augmentation-xia.md | 公開程度（原 Card 5、Card 6） | 原文不符
- **問題**：原文第 1 頁註 1 寫明程式碼公開（"Code is available at https://github.com/xiamengzhou/DataAugForLRL"），論文頁與證據表均未記載，讀者會以為未公開。
- **來源**：[原文 PDF](../../../../raw/my-focus/英文論文/Generalized%20Data%20Augmentation%20for%20Low-Resource%20Translation_P19-1579.pdf)，p. 5786 註 1。
- **發現於**：2026-11-20 改寫為我的關注新六章時回原文抽查，Claude Code by Anthropic（Claude Opus 5.5）。
- **處理**：2026-11-20，Claude Code by Anthropic（Claude Opus 5.5）。論文頁 01 速覽與 06 公開程度補記程式碼公開，證據表新增一列。
