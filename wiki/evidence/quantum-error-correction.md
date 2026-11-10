# 證據表：quantum-error-correction
- **概念頁面**：[wiki/concepts/quantum-error-correction.md](../concepts/quantum-error-correction.md)
- **查核者**：Antigravity by Google DeepMind，2026-11-09

| 位置 | 主張／陳述 | 類型 | 第一手來源與精確位置 | 核驗結果與說明 |
|---|---|---|---|---|
| 核心定義 | 橫向邏輯閘與通用容錯量子計算之資源需求 | 本篇研究結果 | [Eastin & Knill (2009)](https://doi.org/10.1103/PhysRevLett.102.110502) 摘要；[Dennis et al. (2002)](https://doi.org/10.1063/1.1499754) §IX.2 | 橫向閘不在同一碼區塊內傳播錯誤；可偵測任一單一子系統錯誤的碼不存在通用橫向閘集合。表面碼通用計算可使用態純化等額外資源；任意深度與通用性是不同概念（EK-048）。 |
| 關鍵突破支柱 | Hopfield 能量函數與表面碼錯誤恢復的統計力學描述 | Wiki 詮釋 | Hopfield (1982) *PNAS* 79:2554–2558；[Dennis et al. (2002)](https://doi.org/10.1063/1.1499754) §I、§IV | Hopfield 與表面碼的比較是概念類比；Dennis 等在完美症候群量測下討論二維含無序伊辛模型，在量測有誤時討論三維含無序 $Z_2$ 規範理論，不把兩種條件混為同一映射（EK-047）。 |
| 關鍵突破支柱 | 中性銣原子陣列 48 個邏輯量子位元電路實作 | 奠基論文實驗結果 | Bluvstein et al. (2024) *Nature* 626:58–65, Figs. 1–5 | 符合來源。實作 40 個色碼量子位元（20 個橫向 CNOT）與 48 個三維 $[[8,3,2]]$ 碼邏輯量子位元取樣電路。 |
| 跨學科延伸 | qLDPC 與中性原子陣列的研究範圍 | 作者解釋 | [Bluvstein et al. (2024)](https://doi.org/10.1038/s41586-023-06927-3) Fig. 5、Outlook | 實驗使用色碼與三維 $[[8,3,2]]$ 碼；四維超立方體是邏輯位元的連接圖。該文將 qLDPC 列為未來提升編碼效率的方向，未證實所述一個數量級之硬體節省（EK-049）。 |
