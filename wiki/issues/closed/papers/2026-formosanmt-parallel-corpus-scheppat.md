# 已結案問題：papers/2026-formosanmt-parallel-corpus-scheppat.md

> 本檔收錄 [wiki/papers/2026-formosanmt-parallel-corpus-scheppat.md](../../../papers/2026-formosanmt-parallel-corpus-scheppat.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-060 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.lrec-1.273` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 LREC 2026 論文集原文首頁核對
- **發現於**：同 EK-057
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 LREC 2026 原文首頁與 ELRA 核對：本篇由 ELRA 出版，正式註冊之 DOI 為 `10.63317/3ut33xim33nt`，經 Crossref 與 doi.org 解析確認無誤並更新頁面。

### EK-080 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 3 與 Card 6 | 原文不符
- **問題**：（1）Card 3（第 47 行與第 62 行架構圖）稱資料清洗採語言識別器与語義對齊過濾 $\operatorname{AlignScore}(x_i, y_i) \ge \tau$；原文 §3.3（p. 3448）係使用正則表達式與詞／字元長度比門檻（2 詞以上剔除 $r \le 0.2$ 或 $r > 8.0$；少於 2 詞剔除字元比 $r \le 0.05$ 或 $r > 20.0$），無語義對齊模型或語言識別器。（2）Card 3（第 49 行）所列 15 語言代碼含錯誤代碼 `puy`、`ruk`、`cou`、`sai`、`kan`、`sed` 且同時列出 `sed` 與 `trv`（漏列噶瑪蘭語 `ckv` 與撒奇萊雅語 `szy`）；原文表 1（p. 3447）之 ISO 639-3 代碼為 `ami, bun, ckv, dru, pwn, pyu, ssf, sxr, szy, tao, tay, trv, tsu, xnb, xsy`。（3）Card 3（第 53–59 行）稱對 NLLB-200 進行 15 語多語言聯合微調；原文 §4.2（p. 3450）明言係針對各族語－華語及 4 個族語－英語**分別訓練獨立之雙向雙語模型**，並於 §6（p. 3453）將多語言聯合預訓練列為未來工作。（4）Card 6（第 90 行）寫「30 萬高品質句對」，與 Card 4 之總量 493,519 句不一致。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`（§3.3 p. 3448、表 1 p. 3447、§4.2 p. 3450、§6 p. 3453）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 刪除虛構之語言識別器與 AlignScore 模型，改述原文真實採用之正則清洗與詞/字元長度比例過濾門檻；校正 15 個 ISO 639-3 語言代碼並補齊 ckv 與 szy；澄清模型訓練為獨立之雙向雙語基準，而非 15 語聯合多語言預訓練；Card 6 校正語料總量為 49.3 萬句對（含 39.7 萬族語－華語句對），消除數據矛盾。建立證據表 wiki/evidence/2026-formosanmt-parallel-corpus-scheppat.md，頁面 verification 改為 verified。

### EK-122 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 3 | 原文未支持
- **問題**：Card 3 第 53–58 行之 $\mathcal{D}_{\text{clean}} = \{ (x_i, y_i) \mid \operatorname{ValidText} \land \operatorname{RatioFilter} \}$ 為 Wiki 自擬，原文沒有編號公式；且拆成兩行 aligned 片段，各行都不完整。原文過濾規則為文字敘述：兩側皆有兩個以上詞元時計算目標對來源之詞元比 r，r ≤ 0.2 或 r > 8.0 者捨棄。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`，PDF 第 4 頁（LREC 2026 論文集 p. 3448）。
- **發現於**：第二批卡片回填 C 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪除 Card 3 自擬之 $\mathcal{D}_{\text{clean}}$ 集合式，過濾規則依 §3.3（p. 3448）改以文字敘述；同章另一條自擬之語言代碼集合式一併改為文字列表（EK-174）。卡片 Card 3 採無公式模式。證據表登記原文無編號公式。

### EK-123 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 1、Card 5 與 Card 6 | 過度表述
- **問題**：Card 1 第 33 行稱本篇「具有里程碑意義」；Card 5 第 131 行稱「徹底解決了國際研究團隊無法取得標準化臺灣南島語資料的歷史痛點」並稱「首度大規模」；Card 6 第 147 行稱「完美聯動」、將產出「全球第一套」標註語料庫並「直接將研究成果推向頂會高度！」。原文無上述評價，「完美」屬禁用評價詞，驚嘆號亦不合學術語氣。另第 145–147 行寫到使用者之研究規劃，撰寫卡片時須依 `paper-card-writer` 第二節第 13 條，不得透露碩論題目、資料或結果。
- **來源**：同 EK-122 之 PDF 全文。
- **發現於**：第二批卡片回填 C 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。Card 1 刪去「里程碑意義」，改照摘要與 §1；Card 5 依新論文模式改記原文公開之資源、§7 限制與 §6 未來工作，刪去「徹底解決……歷史痛點」「首度大規模」「標準化工程範本」；Card 6 刪去「完美聯動」「全球第一套」「推向頂會高度！」與第一人稱之研究規劃，改寫為研究方向之延伸思考，不寫碩論題目、資料或結果。卡片 Card 6 不提碩論。

### EK-174 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | Card 2、Card 3 與 Card 4 | 原文不符
- **問題**：（1）Card 4 稱族語－英語 95,809 句對「涵蓋 4 種具備英語對齊之語言：阿美語 36,039、布農語 25,627、魯凱語 13,010、泰雅語 21,133 句對」，並稱族語－華語「從阿美語 64,888 句對至邵語 21,795 句對」，原文表 2 無這些數字；表 2 每種語言都列有英語句對，只有四種語言之英語資料足以訓練模型。表 2 位置誤記為 p. 3449（實為 p. 3450）。（2）Card 2 將「宗教文獻」列為來源，原文 §2 明言不收錄聖經；稱各來源「在格式、拼寫標點、檔案編碼上互不相容」「直接訓練會導致大量的錯位幻覺」，稱 NLLB 新增語言之變通寫法「極易引發崩潰」、隨機初始化語言代碼「會嚴重損害預訓練權重的表徵遷移」，原文無這些說法。（3）Card 3 另有一條自擬之語言代碼集合式 $\mathcal{L}_{15}$，原文為表 1；「連續兩個以上之語氣助詞」原文為「more than two characters」；三種假影字串與舞台指示語之中文為 Wiki 回譯，原文僅有英譯描述。（4）Card 4 稱 NLLB「顯著勝過」OpenNMT，原文為「generally outperforms」，未做顯著性檢定；未記作者對譯入英語分數偏高之保留說明。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`，§2（p. 3446）、表 1 與 §3.2（p. 3447）、§3.3（p. 3448）、§3.4（p. 3449）、表 2（p. 3450）、表 3 與表 4（p. 3451）、§5（p. 3452）。
- **發現於**：第三批卡片回填 C 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。以表 2、表 3、表 4 之頁面影像核對後：Card 4 改記表 2 合計列與四種英語模型語言之訓練集句數，註明表 2 有兩組標為 xnb；Card 2 依 §1–§3 改寫並註明不收聖經；Card 3 語言代碼改為文字列表，語氣詞條件與假影字串照原文；Card 4 改為「整體優於」並補作者之保留說明。證據表逐一列出數值與位置。

### EK-175 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | hook、Card 1 與證據表 | 過度表述
- **問題**：`hook` 稱本篇為「首個涵蓋全臺 15 種南島語之標準化平行語料庫」，Card 1 稱「全球首個完整涵蓋臺灣 15 種官方南島語言……之標準化多語言平行語料庫」，證據表 Card 5 列稱「建立全球首個涵蓋全臺 15 種南島語之標準化 MT 基準」並判定符合來源；原文未稱首個，§2 僅說同一語族或地區之多語翻譯資料集較少。開頭引言（Wiki 撰寫）稱語料「高純度」，原文無此評價，且作者自承過濾帶有臨時性。
- **來源**：`raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`，摘要與 §1（pp. 3445–3446）、§2（p. 3446）、§3.3（p. 3448）。
- **發現於**：第三批卡片回填 C 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。`hook` 與 Card 1 刪去「首個」，改照摘要；開頭引言改寫，不作品質評價；證據表該列刪除，另立一列註明原文未稱首個。

### EK-233 | fixed | papers/2026-formosanmt-parallel-corpus-scheppat.md | 原 Card 4、本頁範圍 | 過度表述
- **問題**：原頁寫「表 2 每種語言都列有族語－英語句對」，但表 2 有兩組皆標為 xnb、未見 ckv；寫 NLLB 整體優於 OpenNMT、例外只有阿美語，但表 3 中魯凱語→華語亦為 OpenNMT 較高（21.70 對 19.97）；本頁範圍寫「15 種南島語言（含雅美／達悟語）」，原文 §3.1 明言雅美語不屬臺灣南島語群，表 1 為 16 個語言名、15 個 ISO 639-3 代碼。
- **來源**：[原文 PDF](../../../../raw/my-focus/英文論文/FormosanMT%20A%20Multilingual%20Parallel%20Corpus_2026.lrec-1.273.pdf)，表 1 與 §3.1, p. 3447；表 2, p. 3450；表 3, p. 3451。
- **發現於**：2026-11-20 改寫為我的關注新六章時，DeepSeek Harness（DeepSeek V4.1 Flash）與 Command Code（MiniMax M3.1 Flash）提出，Claude Code by Anthropic（Claude Opus 5.5）核對。
- **處理**：2026-11-20，Claude Code by Anthropic（Claude Opus 5.5）。論文頁三處依原文改寫，證據表同步。
