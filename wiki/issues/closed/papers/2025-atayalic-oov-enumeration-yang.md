# 已結案問題：papers/2025-atayalic-oov-enumeration-yang.md

> 本檔收錄 [wiki/papers/2025-atayalic-oov-enumeration-yang.md](../../../papers/2025-atayalic-oov-enumeration-yang.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-067 | fixed | papers/2025-atayalic-oov-enumeration-yang.md | Card 3 | 原文不符
- **問題**：（1）第 45–52 行與第 66 行架構圖稱系統以音韻轉換函數 $\Phi_{\text{phon}}(p \oplus \text{Infix}(i, r) \oplus s) = w_{\text{unk}}$ 正向生成表面形，並將「第二階段：候選詞根篩選」標為「保留率 > 94%」。原文 §3.2、§3.3、§4.2、§4.3（pp. 29–35、47–57、73）中，94.08%／94.33%／95.74% 召回率屬「第一階段：候選詞根挑選」（直接檢查詞根或其刪母音／中綴變體是否為未知詞子字串，且前後剩餘子串為合法前後綴）；而利用書寫形式轉換規則比對之「第二階段：候選詞根篩選」因過濾掉過多正解詞根、對猜測有害，作者於 p. 73 明言**最終系統決定不執行該步驟**。（2）第 57–64 行將隨機森林寫為對單一候選詞根獨立打分之單點分類器；原文 §3.5（pp. 42–45）實為**成對比較（Pairwise）二元分類器**，對任意兩候選詞根 $(x, y)$ 抽取 44 維特徵（$x$ 13 維、$y$ 13 維、差值 13 維、比值 5 維）進行 $\binom{n}{2}$ 循環賽投票選出最高票詞根。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/以構詞規則窮舉來解決泛泰雅語未知詞問題_楊鈞凱.md`（§3.2–3.5 pp. 29–45、§4.2–4.3 pp. 47–57、§5 p. 73）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文第三至五章逐項確認後重寫 Card 3：刪除無來源之 $\Phi_{\text{phon}}$ 與集合式；94.08%／94.33%／95.74% 改歸「候選詞根挑選」階段；明確寫出原規劃之書寫形式篩選因濾掉過多正解而不執行；隨機森林改述為 44 個特徵之成對比較分類器，以兩兩配對投票選出詞根。另修正同頁未登記之問題：Card 4 補列表 38 之規則策略與隨機森林答對數及表 15 之詞根集合上限；Card 3、Card 5 註明中文語意特徵依賴含未知詞句子之中文翻譯；刪除「首創」「徹底扭轉」等過度表述。證據表見 wiki/evidence/2025-atayalic-oov-enumeration-yang.md。
