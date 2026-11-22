# 已結案問題：papers/2017-attention-is-all-you-need.md

> 本檔收錄 [wiki/papers/2017-attention-is-all-you-need.md](../../../papers/2017-attention-is-all-you-need.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-018 | fixed | papers/2017-attention-is-all-you-need.md | Card 4 | 歸因／版本錯置
- **問題**：41.8 BLEU 符合 arXiv 版，NeurIPS 定稿 PDF 報 41.0（官方摘要頁 41.1）；頁面同時標 NeurIPS venue 與 arXiv 連結，須註明採用版本。
- **來源**：[NeurIPS 定稿 PDF](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 NeurIPS 30 定稿 PDF 查核修訂 Card 4：明確標註英譯法（EN-FR）在 NeurIPS 定稿正文第 8 頁報告為 41.0 BLEU，在 Table 2 與 arXiv 版中標註為 41.8 BLEU（官方摘要頁載為 41.1），完整呈現版本數值差異。證據表見 wiki/evidence/2017-attention-is-all-you-need.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核 NeurIPS 定稿 PDF Table 2 與 arXiv v7：定稿正文及 Table 2 均為 41.0，41.8 見於 arXiv v7；目前頁面、卡片與證據表仍把定稿 Table 2 標為 41.8；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看 NeurIPS 定稿與 arXiv v7 的 Table 2 頁面影像，論文頁與卡片以定稿 41.0 為主，分別註明 arXiv v7 的摘要／表格 41.8 與正文 41.0，以及會議網站摘要 41.1；同步更正證據表，並指出定稿表中集成模型 41.29 高於 41.0。頁面 verification 改為 partial。

### EK-019 | fixed | papers/2017-attention-is-all-you-need.md | Card 5 | 原文不符
- **問題**：稱原始 Transformer 訓練「完美契合 Tensor Cores」；原文使用 8 張 P100（Pascal），首代 Tensor Cores 出現於 Volta。
- **來源**：[NeurIPS 原文](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need.pdf)、[NVIDIA Volta 白皮書](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-product-literature/volta-architecture-whitepaper.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 硬體共振段落：精確指出 2017 原文係在 8 張 NVIDIA P100（Pascal 架構，無 Tensor Cores）上訓練，其高度並行之 GEMM 矩陣運算特性隨後與 Volta 架構（首代 Tensor Cores）及現代萬卡叢集產生共振，更正時代錯置。證據表見 wiki/evidence/2017-attention-is-all-you-need.md。

### EK-020 | fixed | papers/2017-attention-is-all-you-need.md | Card 6 | 過度表述
- **問題**：「拿掉歸納偏置」過於絕對；原模型仍使用位置編碼與遮罩等結構先驗。
- **來源**：同 EK-019
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 6 減法哲學段落：將原先「拿掉歸納偏置」改述為精確的「大幅放寬結構性歸納偏置」，明確交代模型仍保留位置編碼與因果遮罩等基礎先驗，修正絕對化表述。證據表見 wiki/evidence/2017-attention-is-all-you-need.md。

### EK-108 | fixed | papers/2017-attention-is-all-you-need.md | 證據表第 11–12 列 | 原文不符
- **問題**：證據表第 11 列把 WMT 2014 翻譯結果與路徑長度比較之出處寫作「§5.1, §5.2」，第 12 列把 WSJ 句法剖析寫作「§5.3」。原文 §5 為訓練設定（§5.1 訓練資料、§5.2 硬體與排程、§5.3 最佳化器）；路徑長度比較在 §4 Table 1，翻譯結果在 §6.1 Table 2，句法剖析在 §6.3 Table 4。
- **來源**：`raw/2017-attention-is-all-you-need.pdf`（Vaswani et al. 2017），§4 p. 6、§5.2 p. 7、§6.1 p. 8、§6.3 p. 9。
- **發現於**：第二批卡片回填 C 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。兩列改為正確節次與頁碼，數值不變。

### EK-109 | fixed | papers/2017-attention-is-all-you-need.md | 開頭引言 | 歸因／版本錯置
- **問題**：標題下之開頭引言「當模型不再被迫一個字一個字地順著時間軸緩慢爬行……」加了引號，卻未註明為 Wiki 撰寫，讀者會以為出自原文；原文無此句。`paper-card-writer` 之 `references/paper-page.md` 第四節第 1 條要求加註。
- **來源**：`raw/2017-attention-is-all-you-need.pdf` 全文無此句（引言為中文修辭，原文為英文）。
- **發現於**：第二批卡片回填 C 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。引言後加「（本頁引言為 Wiki 撰寫，非原文）」，重建論文頁原型。

### EK-200 | fixed | papers/2017-attention-is-all-you-need.md | Card 3 公式與卡片 | 原文未支持
- **問題**：原頁將作者以文字敘述的內積均值與方差另寫為展示公式，卡片沿用該自擬方差式；頁面另把縮放防止 Softmax 極端值說得比作者的推測更強，並將位置編碼有助學習相對位置的假設寫成確定效果。
- **來源**：[NeurIPS 定稿](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) §3.2–3.5，pp. 4–6，p. 4 註 4。
- **發現於**：2026-11-10，處理 TD-011 公式出處，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。以原文註 4 的內積式取代自擬方差展示式，保留作者以文字給出的均值與方差；縮放及位置編碼的解釋還原為作者推測，卡片同步修正，並逐式登記原文位置。
