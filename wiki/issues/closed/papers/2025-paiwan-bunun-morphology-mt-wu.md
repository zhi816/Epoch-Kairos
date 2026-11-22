# 已結案問題：papers/2025-paiwan-bunun-morphology-mt-wu.md

> 本檔收錄 [wiki/papers/2025-paiwan-bunun-morphology-mt-wu.md](../../../papers/2025-paiwan-bunun-morphology-mt-wu.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-068 | fixed | papers/2025-paiwan-bunun-morphology-mt-wu.md | Card 1–3 | 原文不符
- **問題**：（1）Card 1（第 29 行）、Card 2（第 36 行）與 Card 3（第 47–52、65 行）稱本文建立環綴算子、音節週期性自相關檢測，並將「構詞解析器提取之深層詞根與詞綴特徵注入預訓練多語言遷移模型」。原文第 3–6 章（pp. 9–33）中，重疊詞僅以複製詞根末 1–2 個 CV 音節為 `<RED>` 之四步驟字串規則處理；且第 4–5 章之機器翻譯實驗**完全未使用任何詞綴或構詞解析資訊**，第 6 章結論（p. 33）明確將「針對詞綴資訊並將資訊導入模型訓練中」列為未來工作。（2）Card 3（第 58–62 行）列出含 KL 散度正則化項之損失函數；原文 §4.3（pp. 23–24）僅為馬來語／印尼語預訓練後直接微調之兩階段訓練，無 KL 散度正則化項。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/排灣語、布農語的構詞結構自動分析與機器翻譯_吳維中.md`（§3.1–3.2 pp. 9–15、§4.3 pp. 23–24、§6 p. 33）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文第二至六章逐項確認後重寫 Card 1–3 與 hook：刪除原文未出現之環綴、音節週期性自相關檢測與 KL 正則化式；排灣語重疊改述為原文之「重複詞根最後兩音節」字串規則；明確寫出翻譯實驗未使用構詞資訊，作者將其列為未來工作。另修正同頁未登記之問題：Card 4 補列各技術疊加之 BLEU 與前綴組合正確率，註明表 22 與表 24 數值不一致、中文翻族語最終分數含 BERT 之貢獻；刪除「跨語系普適性」「首套開源基礎設施」等無來源表述。證據表見 wiki/evidence/2025-paiwan-bunun-morphology-mt-wu.md。
