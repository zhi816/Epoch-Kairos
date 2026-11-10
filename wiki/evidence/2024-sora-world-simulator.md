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
| Card 4 | 訓練算力對照：基礎、4 倍、32 倍訓練算力之樣本，品質隨算力明顯提升 | OpenAI 報告 §Scaling transformers for video generation | 核實更正（2026-11-10，EK-095）。報告影片標籤只有 Base compute、4x compute、32x compute 三組，原文僅寫「Sample quality improves markedly as training compute increases」；原頁之 16× 與各級畫面描述無出處，已刪除。 |
| Card 4 | 零樣本模擬《Minecraft》畫面與物理局限 | OpenAI 報告 §Simulating digital worlds, §Discussion (Limitations) | 核實更正。原文僅展示以提示詞激發零樣本渲染《Minecraft》之玩家動態畫面，並在 Discussion 明確列舉常見失敗模式（如玻璃碎裂無物理反應、吃漢堡無咬痕、物體憑空出現等）。更正將其寫為具備即時互動與完備狀態記憶世界引擎之過度表述。 |
| Card 5, 6 | 世界模型與直覺物理模擬之本質解讀 | OpenAI 報告 §Discussion; Kang et al. (2024) | 核實更正。保留為隨算力擴展而展現出之有限模擬能力觀察，強調其本質仍為高維視覺統計擬合，距離真正具備因果推理與物理封閉性的世界模型仍具本質差距。 |
| Card 1 | 過去做法把影片縮放、裁切或截短成標準尺寸（例如 4 秒、$256 \times 256$）；Sora 可生成一分鐘影片；報告署名 Brooks、Peebles 等 | OpenAI 報告 §Variable durations, resolutions, aspect ratios；摘要段（「capable of generating a minute of high fidelity video」）；作者列 | 核實更正（2026-11-10，EK-098）。原頁點名 Runway Gen-2、Pika「2 至 4 秒」無出處，改依報告原文。 |
| Card 3 §3、Card 4 | DiT 12 種設定（0.3 至 118.6 Gflops）之模型 Gflops 與 FID-50K 相關係數 $-0.93$ | Peebles & Xie (2023) 圖 8，p. 8；§4 模型設定，p. 5 | 核實更正（2026-11-10，EK-094、EK-099）。原頁寫「訓練算力」「三個數量級」「冪律」「逾 $-0.95$」與驗證損失對訓練算力之冪律公式，兩來源皆無此冪律或參數，已改寫並刪除該公式。複核發現目前論文頁仍列 patch 數量、patch embedding 與 clean-patch diffusion 公式；OpenAI 報告未提供其模型實作細節，需標為 Wiki 推導並補來源或移除（EK-099 重開）。 |
| Card 4 | DiT-XL/2 於 256 將 FID-50K 由 LDM 之 3.60 降至 2.27；512 為 3.04（ADM-G、ADM-U 為 3.94） | Peebles & Xie (2023) §5，p. 8；表 3，p. 9 | 核實符合 |
| Card 4 | 原生長寬比之構圖比較：方形裁切版本有時主體只部分入鏡，Sora 取景較佳；質性比較 | OpenAI 報告 §Improved framing and composition；Liu et al. (2024) 圖 6，p. 7 | 核實更正（2026-11-10，EK-096）。原頁「主體完整居中率」「顯著躍升」無量化依據，已改寫。 |
| Card 4 後續 | Kang et al. 為 arXiv:2411.02385（2024 年 11 月），ICML 2025；二維運動與碰撞模擬，分布內完美泛化、分布外失敗、模仿最相近案例 | arXiv 2411.02385 摘要與 comment 欄（「ICML 2025」） | 核實更正（2026-11-10，EK-097）。原頁「2024, ICML」與「動量守恆、流體質量守恆、穿模」不見於摘要，已依摘要改寫。 |
| Card 4 後續 | 後續影片模型技術報告：CogVideoX 以擴散 Transformer 為基礎、3D VAE 壓縮時空並公開權重；Movie Gen 最大模型 300 億參數 Transformer、上下文 73K 影片詞元、16 fps 16 秒；HunyuanVideo 逾 130 億參數、開源程式碼；Wan 建立於擴散 Transformer 範式、開源 1.3B 與 14B | Yang et al. (2024) arXiv:2408.06072；Polyak et al. (2024) arXiv:2410.13720；Kong et al. (2024) arXiv:2412.03603；Wan Team (2025) arXiv:2503.20314（皆為 arXiv 摘要） | 後續研究；符合來源（EK-100 修正：刪除無技術報告之 Kling、「同一範式」「全面驗證」等原頁說法） |
| 卡片 Card 4、5 | 本篇限制：吃餅乾未留咬痕等物理因果、混淆左右、最長一分鐘且多為數十秒；以原尺寸訓練改善取景 | Liu et al. (2024) §5.1，p. 23；圖 6，p. 7 | 核實符合（2026-11-10，卡片文字檔用） |
