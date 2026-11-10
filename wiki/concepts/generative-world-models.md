---
title: "Generative World Models & Scaling Laws"
title_zh: "生成式世界模型與擴展定律"
domain: "ai"
domain_tags: ["#人工智慧", "#深度學習", "#強化學習", "#計算機視覺"]
papers: ["1982-hopfield-network", "2017-attention-is-all-you-need", "2021-alphafold2", "2024-alphafold3", "2024-sora-world-simulator", "2025-deepseek-r1"]
related_concepts: ["ai-for-structural-biology", "neural-circuits"]
verification: "issues"
---

# 概念：生成式世界模型與擴展定律 (Generative World Models & Scaling Laws)

> 領域：`#人工智慧` `#深度學習` `#強化學習` `#計算機視覺`

---

## 核心定義
**生成式世界模型（Generative World Models）** 指透過自監督或強化學習，在大規模多模態序列（文字、時空影像圖塊、三維分子原子座標、推理思維鏈）上學習外部物理與邏輯世界之聯合機率分佈或能量地形，從而在內部表徵中隱式重建因果規律、三維幾何與推理規則的基礎神經架構。其演進受**擴展定律（Scaling Laws）**支配：包含預訓練算力擴展（Pre-Training Scaling）與後訓練強化學習及推論時思考擴展（Post-Training & Test-Time Scaling）。

---

## 關鍵突破支柱
* **能量地形與統計物理原型（1982, 1985）**：Hopfield (1982) 引入的李亞普諾夫能量函數，以及 Ackley、Hinton 與 Sejnowski (1985) 基於波茲曼機率分佈的隨機學習演算法，為神經網路建立了能量景觀（Energy Landscapes）與吸引子記憶範式；此概念視角隨後在統計物理與生成模型的交叉演進中，啟發了能量模型、分數匹配（Score Matching）與現代聯想記憶（如 Dense Associative Memory / 現代 Hopfield 網絡與 Transformer 注意力之數學等價性），奠定了連續狀態空間生成模擬的深層理論類比。
  * 詳見核心論文：[Hopfield 神經網絡（1982 發表 ｜ 2024 諾貝爾物理學獎）](../papers/1982-hopfield-network.md)
* **Transformer 自注意力通用主幹（2017）**：以 $O(1)$ 序列交互距離與全矩陣並行計算打破循環網路枷鎖，成為跨一切模態的通用骨幹架構。
  * 詳見核心論文：[Attention Is All You Need（2017 發表）](../papers/2017-attention-is-all-you-need.md)
* **三維生物分子幾何與全原子擴散生成（2021, 2024）**：從 AlphaFold2 的 Evoformer 幾何注意力到 AlphaFold 3 的全原子擴散生成模組，將生成式模型拓展至微觀生命分子宇宙。
  * 詳見核心論文：[AlphaFold2（2021 發表 ｜ 2024 諾貝爾化學獎）](../papers/2021-alphafold2.md)、[AlphaFold 3（2024 發表）](../papers/2024-alphafold3.md)
* **時空圖塊與視覺物理世界模擬初步探索（2024）**：Sora 與擴散轉換器（DiT）將高維度影片壓縮為統一的時空圖塊（Spacetime Patches），在算力擴展下自發湧現出動態攝影機三維透視、短暫遮擋連貫性與直覺物理互動畫面；然而此類純視覺擴散模型仍基於高維統計關聯擬合，在涉及因果狀態改變與嚴格物理規律（如碰撞、破碎）時頻繁出現穿模與失真，指明了融合顯式物理約束與交互式世界模型之長期挑戰。
  * 詳見核心論文：[Sora 與世界模型時空物理模擬（2024 發表）](../papers/2024-sora-world-simulator.md)
* **以規則獎勵之純強化學習訓練推理（2025）**：DeepSeek-R1-Zero 不先做監督微調，直接對 DeepSeek-V3-Base 以群體相對策略優化（GRPO）與基於規則之獎勵做大規模強化學習，模型在訓練中逐漸產生長思維鏈、自我反思與驗證等行為；DeepSeek-R1 再加入冷啟動資料與多階段訓練改善可讀性與語言一致，並蒸餾給較小模型。作者亦列出結構化輸出與工具使用、過度思考、語言混雜等限制，並指出難以驗證之任務如何擴大純強化學習仍是開放問題（見論文頁 Card 5）。
  * 詳見核心論文：[DeepSeek-R1（2025 發表）](../papers/2025-deepseek-r1.md)

---

## 跨學科交會與延伸
1. **三大擴展範式的合流（Pre-Training + Diffusion + RL Reasoning）**：
   * 自迴歸/擴散預訓練負責將人類知識與物理世界規律「壓縮」為直覺快思考（System 1）；而基於可驗證獎勵的強化學習（RLVR）則在推論階段開啟長鏈搜索與反覆驗證的慢思考（System 2）。
2. **從被動觀察到科學發現閉環**：
   * 當世界模型同時具備「模擬三維物理/分子環境」與「長鏈邏輯推理」能力時，AI 得以從資料擬合工具升級為能自主提出假說、設計實驗並驗證物理約束的科學探索代理。

---

## 關聯概念網絡
* [AI 驅動之結構生物學與分子設計](ai-for-structural-biology.md)
* [神經迴路因果解耦](neural-circuits.md)
