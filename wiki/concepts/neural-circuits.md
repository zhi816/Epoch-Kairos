---
title: "Neural Circuits & Causal Deconstruction"
title_zh: "神經迴路因果解耦"
domain: "bio"
domain_tags: ["#神經科學", "#生物科技", "#人工智慧"]
papers: ["1982-hopfield-network", "2005-optogenetics", "2017-attention-is-all-you-need", "2025-nerve-mito-cancer"]
related_concepts: ["brain-machine-interface", "programmable-cellular-engineering", "generative-world-models"]
---

# 概念：神經迴路因果解耦 (Neural Circuits & Causal Deconstruction)

> 領域：`#神經科學` `#生物科技` `#人工智慧`

---

## 核心定義
在大腦與生物複雜網絡中，單一行為、記憶或病理狀態往往由多個節點透過突觸相互連結構成的「神經迴路」所驅動。過去傳統技術僅能觀察神經活動的相關性（Correlation）；**因果解耦（Causal Deconstruction）** 則是指透過統計物理模型與分子工程工具，在毫秒與單細胞尺度上選擇性操控特定神經迴路或跨細胞通道，嚴格驗證其是否為特定認知功能或生理過程的「充分且必要條件」。

---

## 關鍵突破支柱
* **Hopfield 聯想記憶網路（1982）**：以統計物理自旋玻璃之李亞普諾夫能量函數 $E = -\frac{1}{2}\sum_{i \neq j} T_{ij} V_i V_j$ 證明記憶與計算可湧現自對稱連接神經元群體的吸引子動力學，奠定計算神經科學對海馬體 CA3 自聯想迴路的理論模型。
  * 詳見核心論文：[Hopfield 神經網絡（1982 發表 ｜ 2024 諾貝爾物理學獎）](../papers/1982-hopfield-network.md)
* **光遺傳學（Optogenetics, 2005）**：由 Nagel、Hegemann 鑑定光控離子通道，Boyden、Deisseroth 等人移植至哺乳動物神經元，結合細胞特異性啟動子，首次實現單一細胞類型的毫秒級精確光控。
  * 詳見核心論文：[光遺傳學（2005 發表 ｜ 2026 諾貝爾生理學或醫學獎）](../papers/2005-optogenetics.md)
* **Transformer 自注意力動態路由（2017）**：在人工神經網路中以縮放點積注意力 $\operatorname{softmax}(QK^\top/\sqrt{d_k})V$ 實現依輸入上下文動態重構的虛擬突觸路由，與現代連續型 Hopfield 網路在數學上嚴格等價。
  * 詳見核心論文：[Attention Is All You Need（2017 發表）](../papers/2017-attention-is-all-you-need.md)
* **腫瘤神經科學與跨細胞粒線體轉移（2025）**：揭示外周與中樞神經系統不僅以電訊號與神經傳導物質調控靶器官，浸潤腫瘤之神經元更會透過隧道奈米管（TNTs）向癌細胞直接輸送粒線體，驅動癌症遠端轉移。
  * 詳見核心論文：[神經元向癌細胞轉移粒線體（2025 發表）](../papers/2025-nerve-mito-cancer.md)

---

## 跨學科交會與延伸
1. **生物神經迴路與人工注意力網絡的對偶**：
   * 生物神經迴路具有高度專一的基因型態、化學受體調控與赫布突觸可塑性；現代 AI 模型的注意力機制（Attention）則可視為一種在數位張量空間中毫秒級重組的「動態軟性神經迴路」。
2. **從中樞認知迴路到全身神經—免疫—腫瘤軸**：
   * 現代神經迴路研究已超越傳統腦區邊界，延伸至自主神經系統對免疫器官與腫瘤微環境的代謝與胞器級別調控。

---

## 關聯概念網絡
* [腦機介面與神經編碼](brain-machine-interface.md)
* [可編程細胞與基因工程](programmable-cellular-engineering.md)
* [生成式世界模型與擴展定律](generative-world-models.md)
