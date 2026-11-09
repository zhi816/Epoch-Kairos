# 證據表：quantum-error-correction
- **概念頁面**：[wiki/concepts/quantum-error-correction.md](../concepts/quantum-error-correction.md)
- **查核者**：Antigravity by Google DeepMind，2026-11-09

| 位置 | 主張／陳述 | 類型 | 第一手來源與精確位置 | 核驗結果與說明 |
|---|---|---|---|---|
| 核心定義 | 橫向邏輯閘與通用容錯量子計算之資源需求 | 物理定理與計算架構 | Eastin & Knill (2009) *Phys. Rev. Lett.* 102:110502; Bravyi & Kitaev (2005) *Phys. Rev. A* 71:022316 | 核實更正。依據 Eastin–Knill 定理，說明任何可偵測錯誤之非平凡量子碼均不存在通用橫向邏輯閘集合；補列魔術態蒸餾（Magic State Distillation）、格子手術或代碼切換以注入非橫向非 Clifford 資源之絕對必要性，糾正原先「單憑橫向閘即可實現任意深度演算法」之定理違背（關閉 EK-048）。 |
| 關鍵突破支柱 | 自旋晶格統計力學與拓撲表面碼隨機鍵伊辛模型（RBIM）之映射來源 | 理論模型與歷史源流 | Dennis, Kitaev, Landahl, & Preskill (2002) *J. Math. Phys.* 43:4452; Hopfield (1982) *PNAS* 79:2554–2558 | 核實更正。明確指出表面碼容錯閾值與 2D RBIM Nishimori 線相變之精確數學映射係由 Dennis et al. (2002) 基於規範理論獨立建立，並未引用 Hopfield (1982)；將 Hopfield 能量景觀與量子糾錯映射釐清為統計物理相變理論在神經計算與量子拓撲之平行應用，糾正直接歷史繼承之歸因錯置（關閉 EK-047）。 |
| 關鍵突破支柱 | 中性銣原子陣列 48 個邏輯量子位元電路實作 | 奠基論文實驗結果 | Bluvstein et al. (2024) *Nature* 626:58–65, Figs. 1–5 | 符合來源。實作 40 個色碼量子位元（20 個橫向 CNOT）與 48 個三維 $[[8,3,2]]$ 碼邏輯量子位元取樣電路。 |
| 跨學科延伸 | 常數編碼率量子低密度奇偶校驗碼（qLDPC）在原子陣列上之實作狀態 | 實驗成果與技術展望 | Bluvstein et al. (2024) *Nature* 626:58–65, Outlook (p. 8) | 核實更正。明確指出該論文實作之編碼為色碼與三維 $[[8,3,2]]$ 碼，qLDPC 碼僅為原文展望中未來進一步降低百萬物理量子位元開銷之核心發展方向，刪除「已在實驗室直接實作 qLDPC」之過度表述（關閉 EK-049）。 |
