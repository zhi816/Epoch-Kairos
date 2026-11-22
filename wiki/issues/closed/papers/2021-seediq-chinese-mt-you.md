# 已結案問題：papers/2021-seediq-chinese-mt-you.md

> 本檔收錄 [wiki/papers/2021-seediq-chinese-mt-you.md](../../../papers/2021-seediq-chinese-mt-you.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-061 | fixed | papers/2021-seediq-chinese-mt-you.md | Frontmatter doi_url | 原文不符
- **問題**：包含本篇在內之 7 篇海大碩士論文（`2021-seediq-chinese-mt-you.md`、`2023-atayal-truku-morphology-dai.md`、`2023-atayalic-multilingual-mt-liao.md`、`2024-taiwanese-mt-resegmentation-tang.md`、`2025-atayalic-affix-mt-jin.md`、`2025-atayalic-oov-enumeration-yang.md`、`2025-paiwan-bunun-morphology-mt-wu.md`），Frontmatter `doi_url` 均複製貼上同一個已過期之臺灣博碩士論文知識加值系統臨時查詢 session 網址（`https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=y8Gq.y/record?yes=1`），並非永久連結。
- **來源**：`raw/my-focus/學長姐論文/` 下 7 篇碩士論文原檔
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。7 篇碩士論文頁刪除失效之 `doi_url`（該欄非必填；碩士論文無 DOI，國家圖書館系統之永久連結未能取得）；游景勝頁改於文獻出處註明可依題名於臺灣博碩士論文知識加值系統查詢，並補列構詞解析方法之會議版本 ROCLING 2020（https://aclanthology.org/2020.rocling-1.1/）。

### EK-062 | fixed | papers/2021-seediq-chinese-mt-you.md | Card 3 | 原文不符
- **問題**：（1）第 52–54 行將前綴二元語素模型寫為以詞根為條件之 $P(s_{\text{pre}} \mid r) = \prod P(p_i \mid p_{i-1}, r)$；原文 §3.3（p. 27，式 3）之前綴二元機率模型為 $P(\text{pfx}) = P(x_1 \mid \$)\prod_{i=2}^m P(x_i \mid x_{i-1})$，不以詞根為條件。（2）第 60–68 行與架構圖將 $\mathbf{e}_{\text{word}}(w_t)$ 寫作「由自訓練 Skip-gram / FastText 學習之詞根或詞彙語義表示」；原文 §1.3.1（p. 4）、§4.2–4.3（pp. 30–33）與 §5.3（pp. 37–39，表 11）中，「自訓練詞嵌入」指 Seq2Seq Bi-LSTM 模型內以 one-hot 輸入端到端訓練之 Embedding Layer，而 fastText Skip-gram 屬「預訓練詞嵌入」；且表 11（p. 38）證實預訓練 Skip-gram 結合詞綴特徵會使 BLEU 由 22.28 暴跌至 12.09，改用詞根形式亦跌至 12.32 與 4.49，最佳系統（25.10 BLEU）係使用表面詞形搭配端到端自訓練 Embedding Layer 與 52 維布林詞綴組合特徵。
- **來源**：`raw/my-focus/學長姐論文/.md/賽德克語－中文機器翻譯之研究_游景勝.md`（§1.3.1 p. 4、§3.3 p. 27、§4.2–4.3 pp. 30–33、§5.3 pp. 37–39 表 11）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3.3、§4.1–4.3、§5.1–5.4 逐項確認後重寫 Card 3：前綴公式改為原文式 (2)(3)，刪除無來源之 MAP 式；明確區分預訓練（fastText skip-gram）與自訓練（one-hot 加 embedding layer）詞嵌入。另修正同頁未登記之問題：Card 4 改以表 8 為準並註明摘要 99.52%／85.34% 與結論 99.83%／82.01% 互不一致；補列表 11 完整結果；Card 1、Card 5 與 hook 刪除「首創」「最行之有效」等過度表述；Card 6 標明為個人研究詮釋並刪除「100% 精確」。證據表見 wiki/evidence/2021-seediq-chinese-mt-you.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 p. 27，將一元與二元公式左側的 Wiki 自加下標移除，依原文均寫作 $P(\text{pfx})$；同步修正 Card 3 的公式。

### EK-190 | fixed | papers/2021-seediq-chinese-mt-you.md | Card 3 特徵拼接公式 | 原文未支持
- **問題**：Card 3 將詞嵌入與詞綴特徵的 Wiki 自行形式化寫成區塊公式；頁面已標示「形式化為 Wiki 整理」，但現行規則只允許原文或補充資料的公式置於區塊。這是 EK-062 原先二元前綴公式及詞嵌入歸屬問題以外的新缺口。
- **來源**：[論文頁](../../../papers/2021-seediq-chinese-mt-you.md) Card 3；[原始學位論文](../../../../raw/my-focus/學長姐論文/賽德克語－中文機器翻譯之研究_游景勝.pdf) §4.1、§4.3；[公式規則](../../../../.agents/skills/wiki-content-audit/SKILL.md) 寫作模式第 3 步。
- **發現於**：2026-11-10，使用者提供之分組複核，Codex by OpenAI 再查原文。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 pp. 28–29、33、38，以原文支持的 250、52、302、22、272 維文字敘述保留特徵設計，移除 Wiki 自擬區塊公式與證據表中該公式列；一元模型卡片公式另依原文 p. 27 校正（EK-062）。此頁僅修已登記問題，verification 改為 partial。
