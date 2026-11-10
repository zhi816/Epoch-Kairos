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
**容錯量子計算（Fault-Tolerant Quantum Computation, FTQC）** 與 **量子糾錯碼（Quantum Error Correction, QEC）** 透過將單一邏輯量子位元（Logical Qubit）非局域地編碼於多個物理量子位元的高維度多體糾纏穩定子子空間（Stabilizer Subspace）中，在不直接坍縮量子資訊的前提下持續提取錯誤症候群（Error Syndrome），並以橫向邏輯閘（Transversal Gates）阻斷局部退相干錯誤的雪崩擴散，實現任意深度量子演算法的可靠執行。

---

## 關鍵突破支柱
* **自旋晶格統計物理與能量吸引子基礎（1982）**：伊辛自旋交互作用與無序自旋玻璃相變理論，不僅奠定了 Hopfield 聯想記憶網路，亦直接構成拓撲量子糾錯碼（如表面碼與色碼）之「統計力學映射定理」——量子糾錯碼的容錯閾值在數學上嚴格對應於隨機鍵伊辛模型（Random-Bond Ising Model）的鐵磁—順磁相變臨界點。
  * 詳見核心論文：[Hopfield 神經網絡（1982 發表 ｜ 2024 諾貝爾物理學獎）](../papers/1982-hopfield-network.md)
* **可重構中性原子陣列之邏輯量子處理器（2024）**：以二維聲光偏轉器（AOD）在計算途中搬運光學鑷子中的中性銣原子，結合分區架構，在最多 280 個物理位元的處理器上操作 40 個色碼邏輯位元，以橫向閘平行作用於邏輯位元，並以三維 $[[8,3,2]]$ 碼執行含 48 個邏輯位元之電路（見論文頁 Card 1、Card 4）。
  * 詳見核心論文：[可重構中性原子陣列之邏輯量子處理器（2024 發表）](../papers/2024-fault-tolerant-quantum.md)

---

## 跨學科交會與延伸
1. **量子糾錯與經典聯想記憶的深層對偶**：
   * 在 Hopfield 網路中，受雜訊干擾的二元自旋狀態透過能量極小化滑回正確的記憶吸引子；在拓撲量子糾錯碼中，受環境退相干干擾的量子態透過穩定子投影測量與最小權重完美匹配（或神經網路解碼器）消除錯誤激發（Anyonic Excitations），將系統拉回無錯編碼空間。
2. **非局域連接與量子低密度奇偶校驗碼（qLDPC）**：
   * 動態可重構原子陣列使三維、四維拓撲碼與常數編碼率 qLDPC 碼得以在實驗室直接實作，將未來百萬物理位元級容錯量子電腦的硬體開銷壓縮一個數量級。

---

## 關聯概念網絡
* [多信使天體物理與極端宇宙學](multi-messenger-astrophysics.md)
* [超導電路之巨觀量子現象](macroscopic-quantum-circuits.md)
