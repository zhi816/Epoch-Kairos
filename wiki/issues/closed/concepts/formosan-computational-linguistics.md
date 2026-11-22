# 已結案問題：concepts/formosan-computational-linguistics.md

> 本檔收錄 [wiki/concepts/formosan-computational-linguistics.md](../../../concepts/formosan-computational-linguistics.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-086 | fixed | concepts/formosan-computational-linguistics.md | Frontmatter 與關鍵突破支柱 | 原文不符
- **問題**：（1）Frontmatter `papers`（第 13 行）將研究臺灣閩南語（漢藏語系漢語族）之 `2024-taiwanese-mt-resegmentation-tang` 列入「臺灣南島語計算語言學」概念頁。（2）第 48–50 行重述 `2025-atayalic-oov-enumeration-yang.md` 之錯誤，稱楊鈞凱（2025）「利用音韻變化規則與構詞律正向窮舉所有合法衍生形」（實為子字串候選詞根挑選搭配成對隨機森林循環賽投票，且正向書寫形式比對篩選因有害而未執行，見 EK-067）。（3）第 57 行稱 Gagnier（2026）「利用正規化 Levenshtein 編輯距離與多維度對齊，量化臺灣南島語 16 族 42 方言」（漏述 TF-IDF 餘弦與 Jaccard 相似度且原文無多維尺度對齊，見 EK-079）。
- **來源**：同 EK-065、EK-067、EK-079
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic & Antigravity by Google DeepMind。第 (1) 點：已自 `papers` 移除 `2024-taiwanese-mt-resegmentation-tang`，論文頁 `concepts` 同步移除。第 (2) 點：依 EK-067 回原文確認之結果改寫楊鈞凱（2025）段；同時改寫「構詞解析與深層原形還原」段，刪除「未知表面形能準確逆向對映」之過度表述，註明解析需已知詞根。第 (3) 點：依 EK-079 回 Gagnier（2026）原文核對，改述為詞級 TF-IDF 餘弦、頻率 $\ge 5$ Jaccard 相似度與前 500 高頻詞之正規化 Levenshtein 距離，刪除多維度對齊。建立證據表 wiki/evidence/formosan-computational-linguistics.md，概念頁 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現概念頁第 48 行仍稱逐一為已知詞根窮舉深層原形、音韻變化與加中綴形式，再檢查前後綴合法性；這正是本條「問題」欄指出須刪除的正向衍生形描述。雖處理記錄稱已依 EK-067 改寫，實際頁面未完成該處更正；須改為子字串候選詞根挑選與 44 維特徵成對隨機森林循環賽投票，並保留正向書寫形式篩選未納入最終系統的說明後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回楊鈞凱（2025）論文摘要（p. i）、§3.2（pp. 29–32）與 §3.5（pp. 42–45）核對，將概念頁與證據表改為已知詞根集合上的三種子字串比對、合法前後綴檢查及 44 維隨機森林成對投票；並註明書寫形式篩選曾測試但因移除過多正解而未納入最終流程。狀態改為 fixed。
