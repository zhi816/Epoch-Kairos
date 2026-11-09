# 證據表：1982-hopfield-network
- **採用版本**：PNAS 正式期刊版本（Proc. Natl. Acad. Sci. USA, Vol. 79, pp. 2554–2558, April 1982），封存於 `raw/1982-hopfield-network.pdf`；DOI: https://doi.org/10.1073/pnas.79.8.2554
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 單篇作者 John J. Hopfield；2024 年諾貝爾物理學獎由 Hopfield 與 Geoffrey E. Hinton 共同獲獎 | 本篇研究結果 / 官方事實 | PNAS 首頁，p. 2554；NobelPrize.org 官方公告 | 符合來源 |
| Card 1 | 借鏡自旋玻璃模型，提出具李亞普諾夫能量函數的內容可尋址聯想記憶 | 本篇研究結果 | 摘要與引言，pp. 2554–2555 | 符合來源 |
| Card 2 | 克服生物神經網路無序/脆弱性與感知器後期理論停滯 | 作者解釋 | pp. 2554–2556，引言與相關研究討論 | 符合來源 |
| Card 3 | 二元狀態 $V_i \in \{0, 1\}$、赫布對稱矩陣 $T_{ij} = \sum_s (2V_i^s - 1)(2V_j^s - 1)$ 且 $T_{ii} = 0$ | 本篇研究結果 | §The model system, p. 2555, 式 (2) | 符合來源 |
| Card 3 | 非同步隨機更新規則：$\sum_{j \neq i} T_{ij} V_j > U_i$ 則 $V_i \to 1$；$< U_i$ 則 $V_i \to 0$ | 本篇研究結果 | §The model system, p. 2555, 式 (1) | 符合來源 |
| Card 3 | 全局李亞普諾夫能量泛函 $E = -\frac{1}{2}\sum_{i \neq j} T_{ij} V_i V_j + \sum_i U_i V_i$，且每次狀態翻轉 $\Delta E \le 0$ 單調遞減收斂 | 本篇研究結果 | §Studies of the collective behaviors, p. 2556, 式 (7)–(8) | 符合來源 |
| Card 3 | 局部極小值不等於全是儲存記憶；存在全零穩定態（$0000\dots$），$N=30, n=5$ 隨機初態約 85% 落入指定記憶、10% 落入無意義偽穩定態、5% 落在記憶附近 | 本篇研究結果 | p. 2557，左欄第 2 段與右欄倒數第 2 段（修正 EK-001） | 符合來源 |
| Card 4 | 儲存型態具偽正交性（pseudoorthogonality），嚴重誤差前之名義容量約 $0.15N$；$N=100$ 時 $n=5$ 幾乎無錯，$n=10, 15$ 出現位元誤差，$n=15$ 約半數記憶良好保留、其餘嚴重偏離 | 本篇研究結果 | pp. 2556–2557，左欄底與 Fig. 2（修正 EK-002） | 符合來源 |
| Card 4 | 信噪比解析解：單一位元期望信號為 $\pm N/2$，交叉干擾雜訊為高斯分佈，均值為 0、標準差 $\sigma = \sqrt{(n-1)N/2}$，單一位元錯誤率為高斯尾部積分式 (10) | 本篇研究結果 | p. 2556，右欄式 (10) | 符合來源 |
| Card 4 | 系統具平緩退化（fail-soft）特性，隨突觸失效信噪比與錯誤率緩慢平滑上升；非對稱突觸連接使信噪比下降 $1/\sqrt{2}$ | 本篇研究結果 | p. 2557，右欄第 4 段（修正 EK-002） | 符合來源 |
| Card 4 | Amit et al. (1985) 統計力學臨界容量 $\alpha_c \approx 0.138$ | 後續研究 | Amit, Gutfreund & Sompolinsky, PRL 55:1530–1533 (1985) | 符合來源 |
| Card 4 | Ackley, Hinton & Sejnowski (1985) 波茲曼機率分佈 | 後續研究 | Ackley, Hinton & Sejnowski, Cogn. Sci. 9:147–169 (1985) | 符合來源 |
| Card 4 | Ramsauer et al. (2021) 現代 Hopfield 網絡與 Transformer 注意力機制等價性 | 後續研究 | Ramsauer et al., ICLR 2021, arXiv:2008.02217 | 符合來源 |
| Card 5 | 凝聚態自旋玻璃理論與機器學習合流、計算神經科學海馬體 CA3 自聯想迴路典範 | 後續研究 / Wiki 詮釋 | 頁面已標記為領域典範轉移 | 符合來源 |
| Card 6 | 物理多體系統即計算機、局部對稱規則湧現全局吸引子幾何 | Wiki 詮釋 | 跨界思維反思，已標明為哲學啟發 | 不適用 |
