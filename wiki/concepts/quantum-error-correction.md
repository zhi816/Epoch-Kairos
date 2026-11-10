---
title: "Fault-Tolerant Quantum Computation & Error Correction"
title_zh: "容錯量子計算與量子糾錯碼"
domain: "physics"
domain_tags: ["#量子物理", "#統計物理"]
papers: ["1982-hopfield-network", "2024-fault-tolerant-quantum"]
related_concepts: ["multi-messenger-astrophysics", "macroscopic-quantum-circuits"]
verification: "partial"
---

# 概念：容錯量子計算與量子糾錯碼 (Fault-Tolerant Quantum Computation & Error Correction)

> 領域：`#量子物理` `#統計物理`

---

## 核心定義
**容錯量子計算（Fault-Tolerant Quantum Computation, FTQC）** 使用量子糾錯碼將邏輯資訊編碼到多個物理量子位元，透過症候群量測和容錯操作限制錯誤累積。在適當雜訊與資源假設下，閾值定理允許增加編碼資源以提高長時間計算的可靠性。橫向邏輯閘不在同一碼區塊內耦合物理子系統，因而避免錯誤在區塊內擴散；但對能偵測任一單一物理子系統錯誤的碼，橫向閘集合不能同時是通用閘集合。通用容錯計算還需要其他資源，例如魔術態製備與測量（[Eastin & Knill, 2009](https://doi.org/10.1103/PhysRevLett.102.110502)）。

---

## 關鍵突破支柱
* **統計物理與表面碼閾值（1982, 2002）**：Hopfield 網路以能量函數描述聯想記憶；[Dennis 等（2002）](https://doi.org/10.1063/1.1499754) 則研究表面碼的錯誤恢復與統計力學模型。在症候群量測完美的理想情況，其分析對應二維含淬火無序的伊辛模型；量測也可能出錯時，則引入時間維度，以三維含無序的 $Z_2$ 規範理論描述。兩者可作統計物理觀點的類比，不表示 Hopfield 論文直接建立了表面碼映射。
  * 詳見核心論文：[Hopfield 神經網絡（1982 發表 ｜ 2024 諾貝爾物理學獎）](../papers/1982-hopfield-network.md)
* **可重構中性原子陣列之邏輯量子處理器（2024）**：以二維聲光偏轉器（AOD）在計算途中搬運光學鑷子中的中性銣原子，結合分區架構，在最多 280 個物理位元的處理器上操作 40 個色碼邏輯位元，以橫向閘平行作用於邏輯位元，並以三維 $[[8,3,2]]$ 碼執行含 48 個邏輯位元之電路（見論文頁 Card 1、Card 4）。
  * 詳見核心論文：[可重構中性原子陣列之邏輯量子處理器（2024 發表）](../papers/2024-fault-tolerant-quantum.md)

---

## 跨學科交會與延伸
1. **量子糾錯與經典聯想記憶的概念類比**：
   * Hopfield 網路可從部分受擾狀態收斂至記憶吸引子；表面碼則量測錯誤症候群，再由解碼器推定恢復操作。兩者都涉及從受擾狀態恢復資訊，但機制與成功條件不同，這個類比不表示兩者等價或保證修復所有錯誤。
2. **非局域連接與量子低密度奇偶校驗碼（qLDPC）**：
   * [Bluvstein 等（2024）](https://doi.org/10.1038/s41586-023-06927-3) 使用色碼與三維 $[[8,3,2]]$ 碼，並在部分實驗中以四維超立方體圖連接邏輯位元；這個連接圖不等同於實作四維拓撲碼。作者將量子低密度奇偶校驗碼（qLDPC）列為未來提升編碼效率的可能方向，並未在該文證實以 qLDPC 將硬體開銷降低一個數量級。

---

## 關聯概念網絡
* [多信使天體物理與極端宇宙學](multi-messenger-astrophysics.md)
* [超導電路之巨觀量子現象](macroscopic-quantum-circuits.md)
