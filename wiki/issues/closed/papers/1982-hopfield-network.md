# 已結案問題：papers/1982-hopfield-network.md

> 本檔收錄 [wiki/papers/1982-hopfield-network.md](../../../papers/1982-hopfield-network.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-001 | fixed | papers/1982-hopfield-network.md | Card 3 | 過度表述
- **問題**：把所有局部能量極小值等同預先寫入的記憶吸引子。原文指出零閾值下全零狀態亦為穩定態，高能穩定態不必是儲存記憶；p. 5 隨機初態模擬（N=30、n=5）約 85% 落入已指定記憶、10% 落入無明顯意義之穩定態、5% 落在記憶附近。
- **來源**：[封存原文](../../../../raw/1982-hopfield-network.pdf)，PNAS 79:2554–2558
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 p. 2556–2557 逐項確認後重寫 Card 3：明記並非所有局部極小值皆為名義記憶吸引子，零閾值下全零態（$0000\dots$）亦為穩定態，且隨機初態約有 10% 試驗落入無意義偽穩定態（Spurious States）、5% 停留在目標記憶鄰近態。證據表見 wiki/evidence/1982-hopfield-network.md。

### EK-002 | fixed | papers/1982-hopfield-network.md | Card 4 | 原文不符
- **問題**：寫作「隨機正交型態」並稱 N=100 可穩定檢索 15 個完整記憶。原文稱隨機型態具 pseudoorthogonality，容量約 0.15N 是誤差變嚴重前之近似容量，不保證完整無誤檢索。另「隨機切除相當比例突觸或損毀神經元仍可正確重建」在原文無定量結果，須降格或另引直接實驗。
- **來源**：[封存原文](../../../../raw/1982-hopfield-network.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit、[2026-11-08 23:36] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 p. 2556–2557 逐項確認後重寫 Card 4：改述隨機型態具「偽正交性（pseudoorthogonality）」而非嚴格正交；容量 0.15N 註明為嚴重錯誤前之近似上限，並列出 N=100 時 n=5/10/15 之誤差分佈實況；補列信噪比高斯尾部單一位元錯誤率積分式 (10)；將突觸損毀定量表述降格為原文之非對稱突觸（信噪比降 $1/\sqrt{2}$）、二值截斷（信噪比降 $\sqrt{2/\pi}$）及隨突觸失效平緩退化之 fail-soft 質性分析。證據表見 wiki/evidence/1982-hopfield-network.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核論文頁 Card 4 與 PNAS p. 2557：非對稱連結及權重截斷的信噪比分析有原文依據，但「隨突觸失效增加而平緩退化」未見隨機失效實驗支持；建議重開為 open。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。更正前一行回核理由：Hopfield 原文 p. 2557 右欄確實以分析描述隨突觸失效而呈現 fail-soft，不能因未報不同失效比例的實驗而稱原文完全未支持此質性描述。同段原文寫信噪比與錯誤率皆緩慢上升，與前述信噪比下降以及 Wiki 現寫的下降方向存在待釐清差異；修訂時保留分析與實驗的區分，不應直接刪除有來源的 fail-soft。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。回看原文 pp. 2556–2557 及 Fig. 2，將 $n=5$ 的「零錯誤」改為原文的「幾乎總是」；區分單向連接模擬與平緩退化分析，記錄原文信噪比方向的內部張力，不推定作者原意；同步更新證據表及卡片用詞。頁面 verification 改為 partial。

### EK-201 | fixed | papers/1982-hopfield-network.md | Card 3 能量公式與 Card 4 後續研究 | 原文不符
- **問題**：頁面及卡片在 Hopfield 原文零閾值的能量式及能量變化式中加入閾值項；此外，頁面把 Amit 等 1985 年以副本對稱理論得到的 0.138 近似值，誤寫為以副本對稱破缺方法得到的嚴格解。
- **來源**：[Hopfield 原文](../../../../raw/1982-hopfield-network.pdf) p. 2556，式 (7)–(8)；[Amit 等原文](https://doi.org/10.1103/PhysRevLett.55.1530) pp. 1531–1532。
- **發現於**：2026-11-10，處理 TD-011 公式出處及抽查卡片後續成果，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Hopfield 原式及零閾值條件修正論文頁與卡片，逐式登記來源；Amit 等之結果標為副本對稱近似，並記下作者對對稱破缺影響的討論。
