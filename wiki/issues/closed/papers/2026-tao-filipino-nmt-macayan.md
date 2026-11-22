# 已結案問題：papers/2026-tao-filipino-nmt-macayan.md

> 本檔收錄 [wiki/papers/2026-tao-filipino-nmt-macayan.md](../../../papers/2026-tao-filipino-nmt-macayan.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-073 | fixed | papers/2026-tao-filipino-nmt-macayan.md | Card 3 與 Card 6 | 原文不符
- **問題**：（1）Card 3（第 45–51 行與第 60 行架構圖）稱在菲律賓語（Tagalog）大規模預訓練並加上參數距離懲罰項；原文 §4.6（p. 32）中，Tagalog（Filipino）即為目標語言，Model 3 係先將 `NLLB-200 (600M)` 於巴丹語群親屬語 **Ivatan-to-Tagalog（伊巴丹語－菲律賓語）**平行語料微調，再於 Yami-to-Tagalog（達悟語－菲律賓語）微調，且無任何 $L_2$ 參數距離懲罰項。（2）Card 3（第 53–57 行與第 63 行架構圖）與 Card 6（第 90 行）稱本文訓練「構詞感知子詞正則化（Morphology-Aware Subword BPE），將語言學詞綴字典注入分詞優先級，確保 `mi-`、`ma-`、`om-` 不被截斷」；原文 §7（p. 34）明確指出**受限於研究時程，本文直接使用 NLLB-200 預設分詞器**，並將子詞／構詞分詞列為未來工作建議。
- **來源**：`raw/my-focus/報告論文題材/2026.loresmt-1.2.pdf`（§4.6 p. 32、§7 p. 34）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。回原文全文核對後：Card 3 刪除「於菲律賓語大規模預訓練」與 $L_2$ 參數距離懲罰項，改述原文三個模型（Model 3 為伊巴丹語→他加祿語預訓練後再微調）；刪除「構詞感知子詞 BPE」，改述原文明言因時間限制使用 NLLB-200 預設分詞器、子詞處理列為未來工作。另修正同頁未登記之問題：Card 1 改依原文寫明達悟語屬巴丹語群「而非臺灣南島語」；補列合成資料之產生方式與表 3 完整數值；註明原文四處內部不一致（達悟語－英語／他加祿語混用、少於 5,000 句與 10,498 句、6.61 與 6.67、對 FormosanBench 之錯誤引述）。證據表見 wiki/evidence/2026-tao-filipino-nmt-macayan.md。

### EK-171 | fixed | papers/2026-tao-filipino-nmt-macayan.md | Card 5 與證據表第 17 列 | 原文不符
- **問題**：（1）證據表第 17 列只寫「表 3 各數值」，未逐一列出數值與表列、欄位。（2）Card 5 漏記原文所述之未來工作與部分限制：原文 §7 Recommendations 列出進階正規化、更好硬體與更大模型、子詞斷詞處理罕見詞與構詞、與母語者及專家合作；Limitations 另指出只研究達悟語→他加祿語一個語言對、經文不能代表一般句構、未做人工評估且指標測不到比喻與偏誤。論文頁亦未說明原文是否公開資料或程式（原文未提及）。
- **來源**：`raw/my-focus/報告論文題材/2026.loresmt-1.2.pdf`，表 3（p. 33）、§7 與 Limitations（p. 34）。
- **發現於**：第二批卡片回填 C 組回報與第三批撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。回原文核對後：證據表第 17 列改為逐一列出表 3 之 BLEU、chrF、Median SBERT 各 6 格數值（皆與論文頁 Card 4 表相符）；Card 5 補列 §7 未來工作、Limitations 所列限制與頁碼，並註明原文未提及公開資源；證據表同步補登。頁面 `verification` 改為 `partial`。
