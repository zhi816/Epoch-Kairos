# 證據表：generative-world-models

本表記錄 [wiki/concepts/generative-world-models.md](../concepts/generative-world-models.md) 各項主張在第一手文獻與支柱論文中的出處與核驗結果。

- **核心支柱來源**：
  1. Hopfield, J. J. (1982). *PNAS*, 79(8), 2554–2558; Ackley, D. H., Hinton, G. E., & Sejnowski, T. J. (1985). *Cognitive Science*, 9(1), 147–169.
  2. Vaswani, A. et al. (2017). Attention Is All You Need. *NeurIPS 30*.
  3. Jumper, J. et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature*, 596, 583–589; Abramson, J. et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*, 630, 493–500.
  4. Brooks, T., Peebles, B. et al. (2024). Video generation models as world simulators. *OpenAI Technical Report*; Peebles, W., & Xie, S. (2023). Scalable Diffusion Models with Transformers. *ICCV 2023*.
  5. DeepSeek-AI (Guo, D. et al.) (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *Nature*, 645, 633–638 (原預印本: *arXiv:2501.12948*).

---

| 概念區塊 | 主張／陳述 | 來源文獻出處 | 核驗結果與說明 |
|---|---|---|---|
| 關鍵突破支柱 | 能量地形與統計物理原型（1982, 1985） | Hopfield (1982); Ackley, Hinton, & Sejnowski (1985) | 核實更正。分開標註 Hopfield (1982) 李亞普諾夫能量函數與 Ackley et al. (1985) 波茲曼機學習演算法之年代；將擴散模型、分數匹配與 Transformer 注意力之聯繫界定為統計物理能量景觀與連續狀態空間之深層理論類比與現代聯想記憶等價性，糾正直接線性歷史奠基之錯誤（關閉 EK-045）。 |
| 關鍵突破支柱 | 時空圖塊與視覺物理世界模擬初步探索（2024） | Brooks et al. (2024); Liu et al. (2024) | 核實更正。依 OpenAI 技術報告將 Sora 定位為時空圖塊之初步探索，明確指出其湧現之三維視角與連貫性仍基於高維統計關聯擬合，在涉及因果狀態改變與嚴格物理規律時頻繁穿模與失真，保留其能力局限觀察（關閉 EK-056）。 |
| 關鍵突破支柱 | 純強化學習與推理運算擴展定律（2025） | Guo et al. (2025) §2.1, §2.3 | 核實更正。明確將「無須人工示範」限定於 R1-Zero 純 RL 模型，說明完整版 R1 結合冷啟動、多階段 SFT 與二次 RL，並將可驗證獎勵（RLVR）向任意領域驗證器與自主科學探索代理之推廣標明為重大未來展望（關閉 EK-046）。 |
| 核心定義 | 生成式世界模型與擴展定律之雙向架構定義 | 各篇核心論文綜述 | 核實符合。涵蓋預訓練（文字、影片、分子座標）與後訓練強化學習推論思考之擴展範式。 |
