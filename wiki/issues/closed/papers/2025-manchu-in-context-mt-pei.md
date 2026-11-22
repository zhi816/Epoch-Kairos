# 已結案問題：papers/2025-manchu-in-context-mt-pei.md

> 本檔收錄 [wiki/papers/2025-manchu-in-context-mt-pei.md](../../../papers/2025-manchu-in-context-mt-pei.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-031 | fixed | papers/2025-manchu-in-context-mt-pei.md | Card 1 | 原文不符
- **問題**：第 27 行語族寫作「阿爾泰阿爾泰通古斯語族」，字詞重複，且「阿爾泰語系」歸類有爭議，宜依原文寫作通古斯語族（Tungusic）。
- **來源**：[封存原文](../../../../raw/my-focus/報告論文題材/2025.acl-long.429.pdf) §3（p. 8769）；處理行已回原文核對
- **發現於**：wiki/log.md [2026-11-08 22:06] audit（Claude Code by Anthropic）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。原文 §3（p. 8769）稱滿語為 critically endangered Tungusic language；Card 1 改為「通古斯語」，刪除重複且有爭議之「阿爾泰阿爾泰」。

### EK-072 | fixed | papers/2025-manchu-in-context-mt-pei.md | Frontmatter、Card 3 與 Card 5–6 | 原文不符
- **問題**：（1）Frontmatter `hook`（第 17 行）、引言（第 22 行）、Card 5（第 83 行）與 Card 6（第 95 行）稱注入語法書會導致翻譯效能「推理衰退／下降」；原文 §4.3（p. 8772，表 3）與附錄 E（p. 8783，表 10）顯示加入語法書段落使分數微幅上升但統計上不顯著（$p = 0.4$），原文結論為「語法書幾乎無助益（grammars hardly help）」，而非造成衰退。（2）Card 3（第 45–53 行）將提示組合寫為「五大獨立組件的笛卡爾積」並以 $\arg\max$ 解碼；原文 §4（p. 8770）明言窮舉所有組合不可行，故採依序貪婪疊加（sequential greedy integration），且實驗使用溫度 0.9／1.0 採樣。（3）Card 3（第 62 行）稱加密實驗將滿文轉寫為「模型完全未見過的對應符號」；原文 §5.2（p. 8773）實為拉丁字母循環位移密碼（如 `a -> e`、`amban -> encep`）。
- **來源**：`raw/my-focus/報告論文題材/2025.acl-long.429.pdf`（§4 p. 8770、§4.3 p. 8772 表 3、§5.2 p. 8773、附錄 E p. 8783 表 10）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：hook 與 Card 1、5、6 改述原文結論「語法書幾乎沒有幫助」（微幅提升且不顯著，附錄 G 表 10 p = 0.4），下降者為 CoT；Card 3 刪除「笛卡爾積」與 argmax 式，改述依序加入組件之流程與溫度 0.9／1.0 採樣；加密改述為原文之字母位移替換（`amban`→`encep`）。另修正同頁未登記之問題：Card 4 補列各步驟數值、顯著性、人工評估與 §6 合成資料訓練 mT5 之結果；顯著性所在之附錄為 G（非 E）；註明英文平行語料由 Google 翻譯自中文。證據表見 wiki/evidence/2025-manchu-in-context-mt-pei.md。
