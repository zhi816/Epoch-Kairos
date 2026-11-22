# 已結案問題：concepts/neural-circuits.md

> 本檔收錄 [wiki/concepts/neural-circuits.md](../../../concepts/neural-circuits.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-042 | fixed | concepts/neural-circuits.md | 2017 支柱 | 歸因／版本錯置
- **問題**：把 Transformer 注意力與 Hopfield 網路等價列在 2017 支柱；等價結果來自連續／現代 Hopfield 之後續工作（Ramsauer et al. 2021），不應歸給 1982 原始網路或 2017 Transformer 原文。
- **來源**：[Ramsauer et al.](https://arxiv.org/abs/2008.02217)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂神經迴路因果解耦概念頁：明確將縮放點積注意力與現代連續型 Hopfield 網路之數學等價性歸因於 Ramsauer et al. (2020/2021) 之理論推導，糾正原先將後續等價結果混入 2017 Vaswani et al. 原始論文之歸因錯置。建立證據表 wiki/evidence/neural-circuits.md。

### EK-055 | fixed | concepts/neural-circuits.md | Hopfield 支柱 | 歸因／版本錯置
- **問題**：與 EK-043、EK-045 同源，將 Hopfield 1982 吸引子延伸為後續多個領域之直接歷史基礎；22:44 審查指出此錯誤於多個概念頁重述，修正時須同步。
- **來源**：同 EK-042
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂神經迴路因果解耦概念頁 Hopfield 支柱：明確定界 Hopfield (1982) 為二值自旋玻璃李亞普諾夫能量函數，容量上限約 0.15N，係為海馬體 CA3 自聯想迴路提供經典物理抽象原型；跨學科對偶段落客觀劃分生物化學突觸調控、經典循環吸引子與現代張量注意力機制之異同，消除將離散吸引子泛化為後續多領域直接歷史基礎之過度表述。建立證據表 wiki/evidence/neural-circuits.md。
