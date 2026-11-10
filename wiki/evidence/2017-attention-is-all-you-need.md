# 證據表：2017-attention-is-all-you-need
- **採用版本**：*Advances in Neural Information Processing Systems (NeurIPS)*, Vol. 30, pp. 5998–6008, 2017；arXiv:1706.03762；封存版本見 `raw/2017-attention-is-all-you-need.pdf`
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 作者 Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin；NeurIPS 30 | 本篇研究結果 / 官方事實 | NeurIPS 30 首頁；arXiv:1706.03762 | 符合來源 |
| Card 1 | 提出純自注意力 Transformer 架構，完全屏棄 RNN 與 CNN，實現 O(1) 交互路徑與高並行度 | 本篇研究結果 | 摘要與引言，pp. 1–2 | 符合來源 |
| Card 2 | 傳統 RNN 順序依賴阻斷並行計算與長程依賴梯度衰減瓶頸 | 作者解釋 / 背景 | §1, §2，Table 1 | 符合來源 |
| Card 3 | 縮放點積注意力除以 $\sqrt{d_k}$ 防止 Softmax 飽和、多頭注意力子空間投影、正弦幾何級數位置編碼 | 本篇研究結果 | §3.2, §3.5，pp. 3–6 | 符合來源 |
| Card 4 | 交互路徑長度 $O(1)$ vs RNN $O(n)$；WMT 2014 EN-DE 28.4 BLEU；EN-FR 的 NeurIPS 定稿 Table 2 與正文均為 41.0，表中最佳集成模型為 41.29 | 本篇研究結果 | [NeurIPS 定稿](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) §4、Table 1；§6.1、Table 2，p. 8 | 回看原始頁面；41.0 超過表內單一模型，但低於最佳集成模型（EK-018）。 |
| Card 4 | EN-FR 版本差異：arXiv v7 摘要及 Table 2 為 41.8、正文為 41.0；NeurIPS 網站摘要為 41.1 | 本篇研究結果 | [arXiv v7](https://arxiv.org/abs/1706.03762v7) 摘要、Table 2 與 §6.1；[NeurIPS 網站摘要](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) | 分開標示版本與同一版本內的差異，不把 arXiv 的 Table 2 誤歸為 NeurIPS 定稿（EK-018）。 |
| Card 4 | 8 張 NVIDIA P100 訓練 12 小時（base）/ 3.5 天（big，算力 $2.3 \times 10^{19}$ FLOPs），WSJ 句法剖析 91.3/92.7 F1 | 本篇研究結果 | §5.2 (p. 7)；§6.1，Table 2；§6.3 (p. 9)，Table 4（節次修正 EK-108） | 符合來源 |
| Card 4 | 後續 BERT/GPT 分流、擴展定律（Kaplan 2020; Chinchilla 2022）、跨模態（ViT、AlphaFold2、DiT） | 後續研究 | 各引文標註出處 | 符合來源 |
| Card 5 | 矩陣運算高並行度；原文硬體為 8 張 P100（Pascal 架構），隨後與 Volta 架構首代 Tensor Cores 及現代算力集群產生強大共振 | 後續硬體發展 / 詮釋 | 標記 P100 原文事實與後續 Tensor Cores 演進（修正 EK-019） | 符合來源 |
| Card 6 | 大幅放寬順序歸納偏置（但保留位置編碼與遮罩等先驗）；與 Hopfield 網路等價閉環 | Wiki 詮釋 / 文獻對照 | 哲學反思，精確修正歸納偏置陳述（修正 EK-020） | 不適用 |
