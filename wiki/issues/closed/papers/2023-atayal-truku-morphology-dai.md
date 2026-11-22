# 已結案問題：papers/2023-atayal-truku-morphology-dai.md

> 本檔收錄 [wiki/papers/2023-atayal-truku-morphology-dai.md](../../../papers/2023-atayal-truku-morphology-dai.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-063 | fixed | papers/2023-atayal-truku-morphology-dai.md | Card 3–4 | 原文不符
- **問題**：（1）Card 3（第 45–60 行）寫出正向書寫轉換函數 $\Phi_{\text{ortho}}(\sigma) = w$ 並稱「雙唇音弱化（$p \to b$ 或 $p \to v$）」；原文 §3.4（pp. 27–28）明確指出無法歸納出泰雅語與太魯閣語的書寫形式轉換規則，故不再產生真正的書寫形式，而是對「詞根＋中綴＋後綴」制定三條比對規則（直接比對、保留最後兩母音、刪去全部母音）後，再以一元／二元模型挑選前綴；且 §3.1.2（p. 21）僅列泰雅語 $p \to b$ 及太魯閣語 $k \to b$、$t \to d$，無 $p \to v$。（2）Card 4（第 82 行）僅引結論章稱考慮邊界的二元模型在太魯閣語獲最佳 85.71%，漏未交代 §4.2.2（p. 36，表 21 對照表 22）中太魯閣語測試集上考慮邊界之一元模型（91.84%）實高於二元模型（85.71%），以及泰雅語測試集不考慮邊界之二元模型達 100.00%（表 20）。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/泰雅語與太魯閣語構詞結構之自動解析_戴晟哲.md`（§3.1.2 p. 21、§3.4 pp. 27–28、§4.2.2 p. 36 表 20–22）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3.1–3.5、§4.1–4.2 逐項確認後重寫 Card 3：刪除無來源之 $\Phi_{\text{ortho}}$、音韻交替算子與 argmax 目標式，改述原文四模組、十個詞根還原條件與三條書寫比對規則；結尾規則改列原文之 `p`→`b`、`k`→`b`、`t`→`d`。Card 4 改列表 14–23 完整結果，並註明泰雅語不考慮邊界之二元模型（100.00%）與太魯閣語一元模型（91.84%）測試正確率高於摘要所稱之最佳系統。另修正同頁未登記之 Card 5「僅需替換音變規則矩陣」與 Card 6「深層原形還原準確率可達 90%」等無來源表述。證據表見 wiki/evidence/2023-atayal-truku-morphology-dai.md。

### EK-130 | fixed | papers/2023-atayal-truku-morphology-dai.md | Card 3 | 原文不符
- **問題**：Card 3 之前綴機率公式寫作 $P_{\text{uni}}(\text{pfx}) = \prod_{i=1}^{m} P(x_i), \qquad P_{\text{bi}}(\text{pfx}) = \cdots$。原文兩式皆寫作 $P(\mathit{pfx})$，以「一元機率」「二元機率」文字區分；uni、bi 下標為 Wiki 所加，與原文寫法不同。式子內容（上下限與條件機率）與原文相同。
- **來源**：`raw/my-focus/學長姐論文/泰雅語與太魯閣語構詞結構之自動解析_戴晟哲.pdf`，§3.5，p. 29（PDF 頁面影像）。
- **發現於**：撰寫卡片前回原文抽查時發現（Claude Code by Anthropic，第三批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改為與原文相同之 $P(\mathit{pfx})$ 兩行 aligned，並以文字註明第一行為一元機率、第二行為二元機率；證據表該列同步改寫。
