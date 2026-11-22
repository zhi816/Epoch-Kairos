# 已結案問題：papers/2023-atayalic-multilingual-mt-liao.md

> 本檔收錄 [wiki/papers/2023-atayalic-multilingual-mt-liao.md](../../../papers/2023-atayalic-multilingual-mt-liao.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-064 | fixed | papers/2023-atayalic-multilingual-mt-liao.md | Card 2–4 | 原文不符
- **問題**：（1）Card 2（第 36 行）稱「泰雅語的 m-qaniq（吃）、賽德克語的 m-ekan 與太魯閣語的 m-ekan 在傳統詞級切分下被視為三個完全無關的獨立詞彙 ID」；泰雅語「吃」之主事焦點形為 `maniq`（詞根 `qaniq`），且賽德克語與太魯閣語同形詞 `mekan` 合併時字串完全相同。（2）Card 3（第 59–65 行）稱句首僅加目標語標籤 `<2zh>`、`<2tay>`、`<2trv>`、`<2sdq>`；原文 §4.1（p. 16）與 §4.3.2（p. 21）定義之標籤格式為同時編碼來源語與目標語之 `<X2Y>`（以單字母 `A`、`S`、`T`、`C`、`M`、`I` 表示，如 `<S2C>`、`<M2C>`）。（3）Card 1–3 僅描述泛泰雅三語聯合訓練（`|V|=10,000`，對應表 15 之 18.97／17.61／19.92 BLEU），完全漏述 §4.3 與 §5.4 之馬來語／印尼語遷移式學習（`|V|=15,000` 或 `20,000`），致與 Card 4 所列最佳分數（表 21–22 之 20.81／19.38／20.84 與 21.98／21.97／26.69）脫節。（4）Frontmatter `doi_url` 為過期 session 網址（同 EK-061）。
- **來源**：`raw/my-focus/學長姐論文/.md/泛泰雅語群與中文之多語言機器翻譯研究_廖恒慶.md`（§4.1 p. 16、§4.3 p. 21、§5.2 p. 27 表 15、§5.4 pp. 31–32 表 21–22）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §2.1、§4.1–4.3、§5.2–5.5 逐項確認後重寫 Card 1–4：刪除原文未出現之 `m-qaniq`／`m-ekan` 例子，改用原文表 2 之三語例句；語言別標籤改為原文之 `<X2Y>`（如 `<S2C>`）；補述馬來語、印尼語遷移式學習（BPE 15,000／20,000），使 Card 4 最佳分數與方法對應，並標明各最佳值之父語言與單一或多語言系統。另修正同頁未登記之問題：刪除無來源之 BPE 與損失函數公式及「首次」「一加一加一大於三」「通用工程標準」等表述；補述原文 §5.5.2 外部測試因叢書例句被辭典例句覆蓋而偏高、作者以交叉驗證為準。證據表見 wiki/evidence/2023-atayalic-multilingual-mt-liao.md。
