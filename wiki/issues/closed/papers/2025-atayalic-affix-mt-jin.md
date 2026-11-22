# 已結案問題：papers/2025-atayalic-affix-mt-jin.md

> 本檔收錄 [wiki/papers/2025-atayalic-affix-mt-jin.md](../../../papers/2025-atayalic-affix-mt-jin.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-066 | fixed | papers/2025-atayalic-affix-mt-jin.md | Card 3 | 原文不符
- **問題**：（1）第 48–49 行稱輸入序列轉為中括號語素標籤 `[PRE:m] [ROOT:qaniq] [SUF:un]`；原文 §2.2–2.3（pp. 11–16）定義之三種格式為「原文形式」、「詞根形式」（搭配 `F1`、`FM002` 等詞綴組合編號）及「詞綴字串形式」（前綴加 `-`、中綴以 `<...>` 標記並移至詞根前、後綴加 `-`，如 `m- osa <m> dayang <n> tatak -an`），無 `[PRE:...]` 等標籤。（2）第 52–68 行與架構圖將模型寫為單一編碼器內執行 LayerNorm 加法融合；原文 §3.1.1（pp. 22–25，圖 5）之最佳架構 `FC_ftr_jnt` 係採用**兩個獨立並聯之 Transformer Encoder**（其一編碼子詞嵌入，其二編碼 26／29／49／62 維布林詞綴特徵向量），再將兩編碼器輸出串接（Concatenate）送入解碼器；且未提及華翻族最佳架構 `CF_bert_base`（§3.2.2，pp. 30–31，圖 14）係以 `bert-base-chinese` 取代華語端編碼器。（3）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/使用詞綴資訊提升泛泰雅語機器翻譯效能_金柏毅.md`（§2.2–2.3 pp. 11–16、§3.1–3.2 pp. 22–31 圖 5、14）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §2.1–2.4、第三章、§4.1–4.3 與第五章逐項確認後重寫 Card 1–4：刪除原文未出現之 `[PRE:m]` 標籤，改列原文三種文本形式與詞綴組合 ID；最佳架構改述為 FC_ftr_jnt 之雙 encoder 串接（布林特徵 49／26／29／62 維），刪除無來源之 LayerNorm 加法式與注意力公式；補述中文翻族語最佳系統 CF_bert_base 以 BERT 取代中文 encoder。另修正同頁未登記之問題：Card 4 補列基線並拆分 BERT 與詞綴字串之貢獻，註明外部測試以原文形式最佳；Card 2 補述詞綴資訊多為解析器預測；刪除 Card 5「推翻高資源偏見」「標準架構管線」等無來源表述。證據表見 wiki/evidence/2025-atayalic-affix-mt-jin.md。
