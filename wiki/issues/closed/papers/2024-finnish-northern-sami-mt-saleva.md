# 已結案問題：papers/2024-finnish-northern-sami-mt-saleva.md

> 本檔收錄 [wiki/papers/2024-finnish-northern-sami-mt-saleva.md](../../../papers/2024-finnish-northern-sami-mt-saleva.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-071 | fixed | papers/2024-finnish-northern-sami-mt-saleva.md | Card 3 與 Card 5 | 原文不符
- **問題**：（1）Card 3（第 55 行）將語言模型先驗正則化項之 KL 散度方向寫反為 $\mathcal{D}_{\text{KL}}(P_{\text{NMT}} \,\|\, P_{\text{LM}})$；原文 §3.2（p. 12950）定義之目標函數為由固定 LM 指向 NMT 之正向 KL 散度 $D_{\text{KL}}(p_{\text{LM}}(y) \,\|\, p_{\text{NMT}}(y \mid x))$。（2）Card 3 架構圖（第 63 行）將芬蘭語與北薩米語單語語料庫一併送入「逆向神經翻譯模型」；原文 §3.1（p. 12950）中，北薩米語單語資料由逆向模型回譯，而芬蘭語單語資料由正向模型正譯（forward translation）。（3）Card 5（第 80 行）稱「當回譯資料量充足時，必須全面採用 Tagged BT」；原文 §4.3（p. 12952，表 5）明確指出 `<BT>` 標記效果不一，在僅用回譯時使域內 UiT 測試集 BLEU 微降（41.75 至 41.71），結合正譯與回譯時使 UiT（38.96 至 38.84）與 YLE（17.91 至 17.36）之 BLEU 均下降。
- **來源**：`raw/my-focus/報告論文題材/2024.findings-acl.768.pdf`（§3.1–3.2 p. 12950、§4.3 p. 12952 表 5）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文 §3–§5 與表 1–5 核對後：KL 散度改為原文式 $D_{\text{KL}}(p_{\text{LM}}(y) \| p_{\text{NMT}}(y \mid x))$；架構圖改為北薩米語單語經反向模型回譯、芬蘭語單語（mC4）經正向模型正譯；Card 5 刪除「必須全面採用 Tagged BT」，改述原文「標記在某些情況有益、在其他情況沒有」並列出各設定數值。另修正同頁未登記之問題：題名改為原文之 *Northern Sámi*；Card 4 補列表 5 完整結果並註明內文 33.80 與表 5 之 33.30 不一致；補列作者自述之單一語言對與單次執行限制。證據表見 wiki/evidence/2024-finnish-northern-sami-mt-saleva.md。

### EK-170 | fixed | papers/2024-finnish-northern-sami-mt-saleva.md | Card 3 與 Card 5 | 原文不符
- **問題**：（1）Card 3 區塊公式之 KL 項寫作雙豎線 D_KL(p_LM(y) ‖ p_NMT(y|x))，原文 §3.2 為單豎線 DKL(pLM(y)|pNMT(y|x))，且該式為正文內嵌式、無式號，論文頁未註明位置。（2）Card 5 漏記原文公開之資源與作者所述之方向：原文 §1 寫明全部程式與資料（含正譯與回譯輸出）公開於 GitHub `j0ma/sami-translation`；§5 指出方法能否推廣到其他語言為關鍵問題、因運算資源所限未能回答；§4.3 推測調整超參數後語言模型先驗與正譯或可並用。論文頁與證據表均未記載。另證據表第 16 列只寫「表中各 BLEU／chrF」，未逐一列出數值。
- **來源**：`raw/my-focus/報告論文題材/2024.findings-acl.768.pdf`，§1（p. 12949）、§3.2（p. 12950）、§4.3 與 §5（p. 12953）、表 1、3、4、5（pp. 12950–12953）。
- **發現於**：第二批卡片回填 C 組回報與第三批撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。回原文核對後：公式改照原文作單豎線，拆成兩行 aligned 並註明「§3.2 正文內嵌式，無式號，p. 12950」；Card 5 補列公開資源（§1）與作者所述之未來方向（§5、§4.3），作者自述限制補頁碼；證據表逐一列出表 1、3、4、5 數值並補登上述各項。另依 `cover.md` 第二節第 7 條改寫 `card_line`（原句切不出 3 行以內之封面斷行）。頁面 `verification` 改為 `partial`。
