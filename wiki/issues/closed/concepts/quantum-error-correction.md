# 已結案問題：concepts/quantum-error-correction.md

> 本檔收錄 [wiki/concepts/quantum-error-correction.md](../../../concepts/quantum-error-correction.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-047 | fixed | concepts/quantum-error-correction.md | 支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 列為表面碼／色碼隨機鍵 Ising 映射之直接來源；映射可追溯至 Dennis et al. 2002，其原文未引用 Hopfield，須分開數學類比與歷史來源。
- **來源**：[Dennis et al. 2002](https://arxiv.org/abs/quant-ph/0110143)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂容錯量子計算與量子糾錯碼概念頁：明確將拓撲表面碼容錯閾值向 2D 隨機鍵伊辛模型（RBIM）Nishimori 線相變之精確數學映射歸因於 Dennis et al. (2002) 之理論工作，將 Hopfield 能量景觀與量子糾錯釐清為統計物理相變理論在神經計算與量子拓撲之平行應用，糾正直接歷史繼承之歸因錯置。建立證據表 wiki/evidence/quantum-error-correction.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。現行句子的文法主詞為伊辛與自旋玻璃理論，不能直接引述成「Hopfield 直接構成映射」；但該段標題為 1982 且只連 Hopfield，未在正文區分表面碼映射研究的歷史來源與概念類比，仍須澄清並定位 Dennis 等研究的適用條件。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。引用 Dennis 等（2002）並分清完美症候群量測的二維無序伊辛模型與量測出錯時的三維規範理論；Hopfield 比較明標為類比，證據表同步改正。

### EK-048 | fixed | concepts/quantum-error-correction.md | 定義段 | 原文不符
- **問題**：稱以橫向閘即可阻止錯誤擴散並實現「任意深度」演算法；依 Eastin–Knill 定理，可偵測錯誤之非平凡量子碼不存在通用橫向邏輯閘集合，須說明其他非橫向或測量型資源。
- **來源**：[Eastin–Knill](https://arxiv.org/abs/0811.4262)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:00] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂容錯量子計算概念頁核心定義：依據 Eastin–Knill 定理，說明任何可偵測錯誤之非平凡量子碼均不存在通用橫向邏輯閘集合；補列魔術態蒸餾（Magic State Distillation）、格子手術或代碼切換以注入非橫向非 Clifford 資源之機制，糾正原先「單憑橫向閘即可實現任意深度演算法」之定理違背。建立證據表 wiki/evidence/quantum-error-correction.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。定義仍可能使讀者理解為只靠橫向閘即可通用容錯計算，缺少非橫向或測量型資源。Eastin–Knill 限制的是通用橫向閘集合；不可把「任意深度」本身等同於通用性。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Eastin–Knill 說明可偵測任一單一子系統錯誤之碼不能有通用橫向閘集合，並說明通用計算需要其他資源；區分通用性與計算深度，證據表同步更新。

### EK-049 | fixed | concepts/quantum-error-correction.md | 跨學科延伸 | 過度表述
- **問題**：稱可重構中性原子陣列已能直接實作 3D／4D 拓撲碼與常數編碼率 qLDPC；所引 2024 實驗將 qLDPC 列為後續方向，未報告已實作。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂容錯量子計算概念頁跨學科延伸：客觀交代中性原子處理器實驗實作之編碼為色碼與三維 [[8,3,2]] 碼，將常數編碼率 qLDPC 碼標明為該實驗展望之核心未來方向，刪除「已在實驗室直接實作 qLDPC」之過度表述。建立證據表 wiki/evidence/quantum-error-correction.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。概念頁仍將可重構原子陣列之 3D／4D 拓撲碼與常數編碼率 qLDPC 寫成已在實驗室直接實作；所引 Bluvstein 等研究將 qLDPC 作為未來改善編碼效率的方向。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 Bluvstein 等（2024）區分已用的色碼、三維碼與四維連接圖，將 qLDPC 記為該文的未來方向，刪除未獲支持的硬體節省量；證據表同步更正。

### EK-141 | fixed | concepts/quantum-error-correction.md | 關鍵突破支柱（容錯量子計算） | 過度表述
- **問題**：條目稱本篇「首次在單一處理器同時編碼 48 個邏輯量子位元」並提「高編碼率超立方體碼」。論文頁已修正（EK-120、EK-121、EK-158、EK-159）：最多 280 個物理位元、40 個色碼邏輯位元，48 個邏輯位元之電路以三維 $[[8,3,2]]$ 碼執行，原文未稱首次。
- **來源**：`wiki/papers/2024-fault-tolerant-quantum.md` Card 1、Card 4（依正式版修正後）。
- **發現於**：第三批卡片回填 B 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依修正後論文頁改寫條目與連結文字；概念頁 `verification` 改為 partial。
