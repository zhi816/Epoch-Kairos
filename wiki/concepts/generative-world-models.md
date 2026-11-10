---
title: "Generative World Models & Scaling Laws"
title_zh: "生成式世界模型與擴展定律"
domain: "ai"
domain_tags: ["#人工智慧", "#深度學習", "#強化學習", "#計算機視覺"]
papers: ["1982-hopfield-network", "2017-attention-is-all-you-need", "2021-alphafold2", "2024-alphafold3", "2024-sora-world-simulator", "2025-deepseek-r1"]
related_concepts: ["ai-for-structural-biology", "neural-circuits"]
verification: "partial"
---

# 概念：生成式世界模型與擴展定律 (Generative World Models & Scaling Laws)

> 領域：`#人工智慧` `#深度學習` `#強化學習` `#計算機視覺`

---

## 核心定義
**生成式世界模型（Generative World Models）** 是利用資料學習並生成環境相關內容的一類研究方向；本頁並列影片、分子結構與推理模型作為不同研究脈絡。生成結果可用來檢驗模型對場景或任務規律的表現，但不能單憑輸出推定其內部已重建因果規律或三維幾何。不同模型的訓練、推論擴展方式與適用範圍也須分別查證。

---

## 關鍵突破支柱
* **能量地形與統計物理原型（1982, 1985）**：Hopfield（1982）以能量函數分析聯想記憶；[Ackley、Hinton 與 Sejnowski（1985）](https://doi.org/10.1207/s15516709cog0901_7) 研究波茲曼機的隨機學習。這些研究與後來的生成模型都可涉及能量描述；此處僅比較概念，兩篇來源本身不足以建立對分數匹配、擴散模型或 Transformer 的直接歷史影響鏈。
  * 詳見核心論文：[Hopfield 神經網絡（1982 發表 ｜ 2024 諾貝爾物理學獎）](../papers/1982-hopfield-network.md)
* **Transformer 自注意力通用主幹（2017）**：以 $O(1)$ 序列交互距離與全矩陣並行計算打破循環網路枷鎖，成為跨一切模態的通用骨幹架構。
  * 詳見核心論文：[Attention Is All You Need（2017 發表）](../papers/2017-attention-is-all-you-need.md)
* **三維生物分子幾何與全原子擴散生成（2021, 2024）**：從 AlphaFold2 的 Evoformer 幾何注意力到 AlphaFold 3 的全原子擴散生成模組，將生成式模型拓展至微觀生命分子宇宙。
  * 詳見核心論文：[AlphaFold2（2021 發表 ｜ 2024 諾貝爾化學獎）](../papers/2021-alphafold2.md)、[AlphaFold 3（2024 發表）](../papers/2024-alphafold3.md)
* **時空圖塊與視覺世界模擬的初步探索（2024）**：[Sora 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/) 描述以壓縮後的時空圖塊表示影片，並展示部分視角變化與短暫遮擋後物體連貫的生成樣本；報告也列出物理互動及物體狀態可能失敗的例子。這些觀察不能直接證明模型內部學得三維幾何或物理定律。
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
