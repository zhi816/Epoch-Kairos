# 已結案問題：papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md

> 本檔收錄 [wiki/papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md](../../../papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-081 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | Card 1 與 Card 3 | 原文不符
- **問題**：（1）Card 1（第 30 行）將作者寫作「王 reen-cheng 教授」，中英大小寫混雜。（2）Card 3（第 44–53 行）列出雙軌混合檢索線性加權公式（結合餘弦相似度與 BM25），並於第 62 行與架構圖（第 65–69 行）稱辭典模組解析出「詞根＋詞綴焦點＋中文詞條」且與向量庫並聯檢索。原文 §3.1–3.2（pp. 4–5，圖 1–3）全文無任何數學公式、未使用 BM25，亦未由辭典解析詞根與焦點；實際流程（圖 3）為**串聯式條件分支（if-else fallback）**：逐詞先查記憶體內 JSON 雜湊表（`Is it in the hash map? YES -> Word Merge`），僅當詞典未命中（`NO`）時才查詢 Qdrant 向量資料庫。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`（§3.1–3.2 pp. 4–5 圖 1–3）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核實後重寫：Card 1 將作者校正為「王任慶（Reen-Cheng Wang）教授團隊」；Card 3 刪除虛構之餘弦相似度結合 BM25 線性加權公式，改述原文真實採用之串聯條件分支（If-Else Fallback）管線（逐詞查詢記憶體 JSON 雜湊表，命中則 Word Merge，未命中才查詢 Qdrant 向量庫），並澄明詞典模組僅做表面詞字面匹配；Card 4 補齊 250 句評估測試集之 Cosine、BLEU 與 ROUGE-L 對比數據及語法複雜句局限。建立證據表 wiki/evidence/2026-hybrid-dictionary-rag-llm-paiwan-wang.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現論文首頁僅列 Reen-Cheng Wang 為通訊作者並列系所，未標示「教授」職稱；本頁與先前處理記錄使用「教授團隊」，若保留須補校方職稱來源，否則改為「作者團隊／通訊作者王任慶」。方法與測試指標本次抽查符合原文；因作者職稱來源尚未補足，狀態重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文首頁（p. 1）核對作者署名與通訊作者註記，移除頁面與證據表中原文未列出的「教授」職稱，改以作者團隊及通訊作者王任慶呈現。狀態改為 fixed。

### EK-110 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | 證據表第 13 列 | 原文不符
- **問題**：證據表第 13 列列出之模型為「DeepSeek-R1-Distill-Qwen-14B」，出處寫「§3.3, pp. 5–6」。原文為 DeepSeek-R1-Distill-Llama-70B，以 GPT-4o mini 為基準，另比較 Llama 3.1-70B 與 Gemma 3-27B；模型列於 §3.4，後編輯模組在 §3.2（皆 p. 5），§3.3 為語料收集。論文頁第 63、94 行之模型名正確。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`（Eng. Proc. 2025, 120, 52），§3.2 與 §3.4，p. 5。
- **發現於**：第二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改正模型名與節次。

### EK-111 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | Card 5 | 原文未支持
- **問題**：Card 5 第一點（第 115 行）稱「以高精確的靜態詞典解決 80% 的關鍵詞錨定，以向量庫處理 20%」，並稱「向極低資源 NLP 界證實」。原文未見 80%、20% 之分配數字。
- **來源**：同 EK-110 之 PDF，全文搜尋「80%」「20%」無結果。修正時改用原文結果節之實際數據，或刪去比例。
- **發現於**：第二批卡片回填 B 組回報，協調者以全文搜尋確認（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。再次全文搜尋確認無 80%、20% 後，刪去比例、「證實」與第二點「徹底克服」；Card 5 改寫為作者結論（§4–§5, p. 7，並註明原文未報告各模組使用比例）、資料取得條件（p. 8）、作者明列之限制與未來方向（§5, p. 7）。證據表登記。

### EK-160 | fixed | papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md | Frontmatter、Card 1、Card 2 與 Card 6 | 過度表述
- **問題**：（1）`card_line`「翻譯排灣語與華語」暗示雙向，原文只評估排灣語譯華語；`hook` 用「暴升」。（2）Card 1 稱排灣語是「臺灣南部最具歷史深度的南島語言之一」，原文沒有；把文獻中「平行語料少於 10 萬句」之一般說法寫成排灣語之條件，證據表亦然；稱大模型「幻覺頻繁（BLEU 僅 1.7–4.4，§1–§2）」，BLEU 為 §4 之實驗結果，原文未說幻覺頻繁。（3）Card 2 稱純向量檢索會「召回表面詞根相似但焦點語義完全相反的例句，誤導大模型生成顛倒施受關係的幻覺」，原文只說例句稀疏時向量檢索可能失效；稱大模型「根本無法單獨承擔翻譯任務」。（4）Card 6 稱接上構詞解析器後「詞典命中率可由 60% 躍升至 85% 以上」、直接採用辭典譯名「能百分之百防止大模型幻覺」、「論文證實詞典命中時直接 Word Merge 最為穩健」，原文沒有命中率數據，也未做此比較。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`，摘要（p. 1）、§1–§2（pp. 2–3）、§3.4–§3.5（p. 5）、§4（pp. 6–7）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`card_line` 改為「先查辭典再交給大模型，把排灣語譯成華語」，依原文改寫上述各句；Card 6 之推測改標為 Wiki 推測並刪去無出處之數字；Card 4 補記評估範圍之 Wiki 註記（只有自動指標、測試句與辭典語料同源未說明是否排除）；證據表重建。
