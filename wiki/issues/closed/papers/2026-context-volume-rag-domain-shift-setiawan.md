# 已結案問題：papers/2026-context-volume-rag-domain-shift-setiawan.md

> 本檔收錄 [wiki/papers/2026-context-volume-rag-domain-shift-setiawan.md](../../../papers/2026-context-volume-rag-domain-shift-setiawan.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-084 | fixed | papers/2026-context-volume-rag-domain-shift-setiawan.md | Card 3 | 原文不符
- **問題**：第 54–60 行稱論文證明 $\operatorname{chrF++}$ 與語境容量呈精確對數線性公式，且第 48 行稱使用「稠密檢索器」召回上下文。原文 §4.3 與 §5.2–5.3（pp. 90–93，表 2、4、5、6）全文無此對數線性公式；表現最佳之平行句檢索策略並非稠密向量檢索，而是基於 `rapidfuzz` 字元級正規化 Levenshtein 相似度 $\ge 0.5$ 之**詞級模糊匹配（Word-Level Fuzzy Matching）**；且句級檢索（BM25、BGE、ChrF-RAG）於 $K \approx 60$ 即飽和，詞級檢索於每詞 $n = 10$（有效句數 $K \approx 137$，35.28 chrF++）達峰值後，於 $n = 15, 20$（$K \approx 205, 272$）因語境雜訊回落至 35.16 與 34.22 chrF++（表 5），並非單調無限上升。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Context Volume Drives Performance Tackling Domain Shift in Extremely.pdf`（§4.3 p. 90、§5.2–5.3 pp. 91–93、附錄 E p. 100 表 4–6）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 刪除虛構之對數線性公式與單一稠密檢索器表述，改述真實之四種檢索策略（BM25、BGE、ChrF-RAG 以及基於 RapidFuzz 之詞級模糊匹配）；交代句級檢索在 $K \approx 60 \sim 80$ 飽和與詞級檢索在 $N=10$（eff. $K \approx 137$）達峰值 35.28 chrF++ 後因語境雜訊回落之實證消融數據；補列詞典檢索單調線性增長特性與完整詞典取得 31.32 chrF++；Card 4 補齊 Table 1、2、4、5、6 詳細數據與 Table 7 三大定性失敗修復案例。建立證據表 wiki/evidence/2026-context-volume-rag-domain-shift-setiawan.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現原文 §4.3.2（印刷頁 90）稱詞典共 2,375 條，附錄表 6（印刷頁 100）則列 2,377 條；證據表只採 2,377 並判為完全符合，未記錄原文內部差異。其餘檢索策略與容量結果本次抽查符合原文；須在證據表註明筆數差異後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文 §3.1（p. 89）、§4.3.2（p. 90）與附錄表 6（p. 100）核對，確認文內分別列 2,377 與 2,375 條詞典，未解釋該差異；已在論文頁與證據表並列兩個數值，並將表述限定為單調提升，移除線性增長之無來源描述。狀態改為 fixed。

### EK-093 | fixed | papers/2026-context-volume-rag-domain-shift-setiawan.md | Frontmatter card_line | 過度表述
- **問題**：`card_line`「參考例句給得越多，達豪語翻譯得越好」暗示例句越多效果越好、單調上升。原文表 5 顯示詞級檢索在 N=10（有效例句約 137 句）達 35.28 chrF++ 後，N=15、N=20 回落至 35.16 與 34.22；原文主張的是「語境容量比檢索演算法更影響效能」，並非越多越好。同頁 Card 3 第 75 行亦已寫明「語境容量並非單調無限上升」。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Context Volume Drives Performance Tackling Domain Shift in Extremely.pdf`（表 5，p. 100；§6 結論，p. 94）
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`card_line` 改為「讓大模型參考例句，修補跨領域的達豪語翻譯」（19 字，描述本篇做了什麼，不含單調之斷言），重建首頁。
