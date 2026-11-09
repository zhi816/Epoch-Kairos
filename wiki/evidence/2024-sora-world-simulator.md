# 證據表：2024-sora-world-simulator

本表記錄 [wiki/papers/2024-sora-world-simulator.md](../papers/2024-sora-world-simulator.md) 各項主張在第一手文獻中的出處與核驗結果。

- **主要第一手來源**：Brooks, T., Peebles, B., Holmes, C., DePue, W., Guo, Y., Jing, L., Schnurr, D., Taylor, J., Luhman, T., Luhman, E., Ng, C., Wang, R., & Ramesh, A. (2024). Video generation models as world simulators. *OpenAI Technical Report*. [https://openai.com/research/video-generation-models-as-world-simulators](https://openai.com/research/video-generation-models-as-world-simulators)
- **奠基架構來源**：Peebles, W., & Xie, S. (2023). Scalable Diffusion Models with Transformers. *ICCV 2023*, 4195–4205. DOI: [10.1109/ICCV51070.2023.00387](https://doi.org/10.1109/ICCV51070.2023.00387)
- **技術綜述來源**：Liu, Y. et al. (2024). Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models. *arXiv:2402.17177*. [https://arxiv.org/abs/2402.17177](https://arxiv.org/abs/2402.17177)
- **封存原文**：`raw/2024-sora-world-simulator.pdf`

---

| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |
|---|---|---|---|
| Card 1 | 生成長達 60 秒高畫質影片，能常態（但非總是）維持短暫遮擋後之物體存在性 | OpenAI 報告 §Emergent simulation capabilities (Long-range coherence and object permanence) | 核實更正。原文載明「Sora is often—though not always—able to effectively model both short- and long-range dependencies... persist people, animals and objects even when they are obscured」。更正 Card 1 寫成絕對化穩定能力的過度表述，並補充報告明列之物理交互失敗局限。 |
| Card 3 | 時空潛在壓縮網路與原生多長寬比時空圖塊（Spacetime Patches）Token 化 | OpenAI 報告 §Turning visual data into patches, §Video compression network, §Spacetime latent patches | 核實符合。時空 VAE 將原始影片在時間與空間進行維度壓縮，切分成時空圖塊作為 Transformer 輸入 Token，支援任意解析度、時長與長寬比。 |
| Card 3 | 去噪擴散目標：預測原始乾淨圖塊（Clean Patches）而非標準雜訊 | OpenAI 報告 §Scaling transformers for video generation | 核實更正。OpenAI 原文明言「given input noisy patches... it is trained to predict the original “clean” patches」，即採 $x_0$-預測目標，而非 Peebles & Xie (2023) 經典 DiT 之 $\epsilon$-預測目標。公式與內文予以明確對比並修正。 |
| Card 3 | adaLN-Zero、3D-RoPE 與具體 VAE 結構之屬性界定 | Peebles & Xie (2023) §3; Liu et al. (2024) §3.2 | 核實更正。OpenAI 未公開 Sora 之具體正規化（如 adaLN-Zero 或 Cross-Attention）與位置編碼細節。明確標註 adaLN-Zero 來自底層奠基架構 DiT（Peebles & Xie 2023），3D-RoPE 與特定 3D 卷積 VAE 結構為學界綜述（Liu et al. 2024）之推測與常見實作。 |
| Card 4 | 算力擴展對照實驗（$1\times$ 至 $32\times$ Compute）湧現物理規律與三維視角連貫性 | OpenAI 報告 §Scaling transformers for video generation, §3D consistency | 核實符合。在完全相同架構下，隨訓練算力增加，樣本品質與時空一致性顯著提升。 |
| Card 4 | 零樣本模擬《Minecraft》畫面與物理局限 | OpenAI 報告 §Simulating digital worlds, §Discussion (Limitations) | 核實更正。原文僅展示以提示詞激發零樣本渲染《Minecraft》之玩家動態畫面，並在 Discussion 明確列舉常見失敗模式（如玻璃碎裂無物理反應、吃漢堡無咬痕、物體憑空出現等）。更正將其寫為具備即時互動與完備狀態記憶世界引擎之過度表述。 |
| Card 5, 6 | 世界模型與直覺物理模擬之本質解讀 | OpenAI 報告 §Discussion; Kang et al. (2024) | 核實更正。保留為隨算力擴展而展現出之有限模擬能力觀察，強調其本質仍為高維視覺統計擬合，距離真正具備因果推理與物理封閉性的世界模型仍具本質差距。 |
