# 已結案問題：papers/2012-crispr-cas9.md

> 本檔收錄 [wiki/papers/2012-crispr-cas9.md](../../../papers/2012-crispr-cas9.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-012 | fixed | papers/2012-crispr-cas9.md | Card 1 | 過度表述
- **問題**：寫更換 20 nt 即可「靶向任意基因」，省略 S. pyogenes Cas9 所需之 NGG PAM。
- **來源**：[封存原文](../../../../raw/2012-crispr-cas9.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Science 2012 pp. 816–817 查核後修訂 Frontmatter hook 與 Card 1：明確補列化膿性鏈球菌 Cas9 靶向序列必須緊鄰 5'-NGG-3' PAM 基序之絕對前提條件，消除「任意基因」無約束靶向之過度表述。證據表見 wiki/evidence/2012-crispr-cas9.md。

### EK-013 | fixed | papers/2012-crispr-cas9.md | Card 4 | 原文不符
- **問題**：把 PAM 近端錯配效應寫成單一錯配即可完全廢除切割，與原文對連續配對需求及遠端錯配容忍度之結果不符。
- **來源**：[原文](https://doi.org/10.1126/science.1225829)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 pp. 818–819 及 Figure 3D–E 查核修訂 Card 4：改述種子區特異性窗口，精確說明高效切割係要求緊鄰 PAM 之原間隔序列 3' 端維持「至少 13 個連續鹼基對完全互補」，而遠端（5' 端）可容忍多達 6 個連續錯配，更正原先「單一錯配即可完全廢除切割」之錯誤陳述。證據表見 wiki/evidence/2012-crispr-cas9.md。

### EK-014 | fixed | papers/2012-crispr-cas9.md | Card 3 | 原文未支持
- **問題**：R-loop 自由能、切割速率常數與 K_d 等符號模型未見於原文，卻呈現為本文模型；可保留為教學推導，但須標明推導者、假設與來源。
- **來源**：[封存原文](../../../../raw/2012-crispr-cas9.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 3 公式小節：在 R-loop 自由能與雙結構域反應動力學公式前加註理論模型說明，明確標註此二公式為後續生物物理學文獻（如 Sternberg et al., 2014 等）對 Cas9 靶向機制的標準教學量化模型，非 2012 原文之直接方程。證據表見 wiki/evidence/2012-crispr-cas9.md。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：高，平台未提供可核對的 effort 欄位）。重新回核 Card 3 公式與 wiki-content-audit 現行公式規則：頁面雖標示後續教學模型，仍以區塊公式呈現非 2012 原文方程，且證據表未逐式列明直接來源位置；建議重開為 open。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。移除無直接來源的自由能、速率與親和力模型，改以原文對辨識、可能 R-loop 與兩催化結構域分工的定性結果說明；同步修訂證據表，verification 改為 partial。

### EK-015 | fixed | papers/2012-crispr-cas9.md | Card 5 | 歸因／版本錯置
- **問題**：把 dCas9、nCas9 及鹼基／先導編輯工具家族寫成本篇建立；2012 原文報告的是雙 RNA 引導與嵌合單 RNA 切割，dCas9 調控平台見 2013 年後續研究。
- **來源**：[封存原文](../../../../raw/2012-crispr-cas9.pdf)、[Qi et al. 2013](https://doi.org/10.1016/j.cell.2013.02.022)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂 Card 5 衍生工具生態系段落：精確說明 2012 本文係透過 D10A 與 H840A 突變完成催化結構域生化驗證，而將 dCas9 作為通用轉錄調控平台（CRISPRi，引 Qi et al., 2013 Cell）以及融合衍生之鹼基/先導編輯（David Liu 團隊 2016, 2019）明確標註為後續工具生態之重大延伸。證據表見 wiki/evidence/2012-crispr-cas9.md。

### EK-196 | fixed | papers/2012-crispr-cas9.md | Card 4 | 原文不符
- **問題**：頁面稱本篇實驗全數在體外，並把五組 GFP 切割測試寫成 100% 切割效率；原文也有細菌細胞內質體維持試驗，五項 GFP 測試報告正確位置的有效切割，未給出 100% 的切割效率。
- **來源**：[封存作者手稿](../../../../raw/2012-crispr-cas9.pdf) pp. 4、6，Figures 3D、5D。
- **發現於**：2026-11-10，修正 EK-014 時交叉複核，Codex by OpenAI。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。區分細菌細胞內試驗與體外嵌合 RNA 切割實驗，移除 100% 效率主張，並同步證據表。
