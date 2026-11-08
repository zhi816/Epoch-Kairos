---
title: "Attention Is All You Need"
title_zh: "Attention Is All You Need：開啟生成式 AI 時代的 Transformer 架構"
paper_year: 2017
award_year: 2017
timeline_year: 2017
authors: "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin"
venue: "Advances in Neural Information Processing Systems (NeurIPS), 30, 5998-6008"
domain: "ai"
domain_tags: ["#人工智慧", "#深度學習"]
concepts: ["generative-world-models", "ai-for-structural-biology", "neural-circuits"]
status: "wiki"
my_focus: false
doi_url: "https://arxiv.org/abs/1706.03762"
key_papers:
  - "Bahdanau, D., Cho, K., & Bengio, Y. (2015) Neural Machine Translation by Jointly Learning to Align and Translate. ICLR 2015. https://arxiv.org/abs/1409.0473"
  - "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017) Attention Is All You Need. NeurIPS 30:5998-6008. https://arxiv.org/abs/1706.03762"
hook: "徹底屏棄循環神經網路（RNN）與卷積網路（CNN），僅憑純自注意力機制（Self-Attention）將序列任意兩點之交互路徑縮短為 O(1) 常數步，解放了算力並行化並奠定現代大型語言模型與多模態 AI 的通用基石。"
---

# Attention Is All You Need：開啟生成式 AI 時代的 Transformer 架構

> 「當模型不再被迫一個字一個字地順著時間軸緩慢爬行，而是能在一瞬間用矩陣乘法看清全局脈絡中每一處幽微的張力時，人工智慧的規模化奇點便真正降臨了。」

**2017 發表 ｜ 現代生成式 AI 奠基支柱**

---

## Card 1 ｜ 時代銘文 (The Hook)
在 2017 年之前，自然語言處理與序列建模完全由循環神經網路（RNN、LSTM、GRU）主導。RNN 必須按時間順序從左到右逐字計算隱藏狀態 $h_t = f(h_{t-1}, x_t)$，既無法在現代 GPU 叢集上大規模並行訓練，又會在長序列中遺忘早期資訊。Google Brain 與 Google Research 的八位作者在《Attention Is All You Need》中做出了一個激進的斷捨離：**完全拋棄循環與卷積結構**，提出純基於自注意力機制（Self-Attention）的 **Transformer** 架構，一舉刷新機器翻譯紀錄並將訓練成本降低一個數量級，成為日後 GPT、BERT、AlphaFold2、Sora 與 DeepSeek 等一切現代基礎模型的共同母體。

---

## Card 2 ｜ 世紀瓶頸：序列計算的時間鎖鏈與長程梯度衰減 (The Dilemma)
傳統序列神經網路受困於兩個根本性的結構瓶頸：

* **順序依賴阻斷硬體並行化（Sequential Bottleneck）**：在長度為 $n$ 的序列中，LSTM 計算第 $t$ 個時間步必須等待第 $t-1$ 步完成，順序操作複雜度為 $O(n)$。這使得 GPU 強大的巨量矩陣並行算力無法在時間維度展開，嚴重限制了訓練資料規模的上限。
* **長程依賴的路徑長度衰減（Long-Range Dependency Path Length）**：在 RNN 中，相距為 $n$ 的兩個語詞要交換資訊，信號必須穿越 $O(n)$ 個非線性時間步；在卷積網路（如 ByteNet）中亦需 $O(\log_k n)$ 層。路徑越長，梯度消失與資訊壓縮失真越嚴重，難以捕捉跨段落的語法與語義關聯。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
Transformer 將序列中任意兩個位置之間的交互距離直接壓縮為常數級 **$O(1)$**，並透過三大核心設計兼顧表達力與訓練穩定性：

1. **縮放點積注意力（Scaled Dot-Product Attention）**：
   * 將輸入序列映射為查詢（Query, $Q$）、鍵（Key, $K$）與值（Value, $V$）三個矩陣，透過全序列成對內積直接計算任意兩位置的相關性權重。除以縮放因子 $\sqrt{d_k}$ 則防止高維度內積過大導致 Softmax 進入梯度趨近於零的飽和區。
2. **多頭注意力機制（Multi-Head Attention）**：
   * 將 $d_{\text{model}} = 512$ 維空間投影至 $h = 8$ 個獨立的 $d_k = d_v = 64$ 維子空間並行計算注意力，使模型能同時從句法結構、指代消解、語義修飾等不同表徵子空間捕捉上下文關聯。
3. **正弦位置編碼（Sinusoidal Positional Encoding）與殘差層正規化**：
   * 由於純自注意力對序列排列具有置換等變性（Permutation Equivariance），作者注入不同頻率之正弦與餘弦波長編碼，使位置偏移 $k$ 可表示為任意位置 $pos$ 的線性變換矩陣，並搭配殘差連接（Residual Connection）與層正規化（LayerNorm）確保深層網路梯度暢通。

### 1. 縮放點積注意力矩陣方程 (Scaled Dot-Product Attention)

給定查詢矩陣 $Q \in \mathbb{R}^{n \times d_k}$、鍵矩陣 $K \in \mathbb{R}^{m \times d_k}$ 與值矩陣 $V \in \mathbb{R}^{m \times d_v}$，縮放點積注意力輸出定義為：

$$\operatorname{Attention}(Q, K, V) = \operatorname{softmax}\left( \frac{QK^\top}{\sqrt{d_k}} \right) V$$

為什麼必須除以 $\sqrt{d_k}$？假設 $q, k \in \mathbb{R}^{d_k}$ 之各分量為獨立同分佈、均值為 $0$、方差為 $1$ 的隨機變數，則其內積 $q \cdot k = \sum_{i=1}^{d_k} q_i k_i$ 之均值與方差為：

$$\begin{aligned}
\mathbb{E}[q \cdot k] &= 0 \\
\operatorname{Var}(q \cdot k) &= d_k
\end{aligned}$$

因此除以標準差 $\sqrt{d_k}$ 可將內積方差嚴格標準化回 $1$，防止當 $d_k$ 較大時 Softmax 分佈退化為單點極端值（One-Hot）而切斷反向傳播梯度。

### 2. 多頭子空間並行注意力 (Multi-Head Attention)

通過 $h$ 組可學習投影矩陣 $W_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}$、$W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$、$W_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$ 及輸出融合矩陣 $W^O \in \mathbb{R}^{h d_v \times d_{\text{model}}}$，多頭注意力表示為：

$$\begin{aligned}
\operatorname{MultiHead}(Q, K, V) &= \operatorname{Concat}\left( \text{head}_1, \text{head}_2, \dots, \text{head}_h \right) W^O \\
\text{where} \quad \text{head}_i &= \operatorname{Attention}\left( Q W_i^Q, K W_i^K, V W_i^V \right)
\end{aligned}$$

### 3. 幾何級數波長之正弦位置編碼 (Sinusoidal Positional Encoding)

在位置 $pos$ 與維度分量 $2i, 2i+1$ 處，位置編碼定義為波長從 $2\pi$ 到 $10000 \cdot 2\pi$ 成幾何級數分佈的三角函數：

$$\begin{aligned}
PE_{(pos, 2i)} &= \sin\left( \frac{pos}{10000^{2i / d_{\text{model}}}} \right) \\
PE_{(pos, 2i+1)} &= \cos\left( \frac{pos}{10000^{2i / d_{\text{model}}}} \right)
\end{aligned}$$

根據三角和角公式，對任意固定相對距離 $k$，$[PE_{(pos+k, 2i)}, PE_{(pos+k, 2i+1)}]^\top$ 恆為 $[PE_{(pos, 2i)}, PE_{(pos, 2i+1)}]^\top$ 的正交旋轉線性變換，使模型能輕鬆學習相對位置關係。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Vaswani et al. 2017）之核心證據
* **路徑長度與計算複雜度對比**：自注意力層的最大交互路徑長度為 $O(1)$、順序操作數為 $O(1)$，每層計算複雜度為 $O(n^2 \cdot d)$；相比之下，循環層（Recurrent Layer）的最大路徑長度與順序操作數皆高達 $O(n)$，每層計算複雜度為 $O(n \cdot d^2)$。在自然語言常見之序列長度 $n < d$（例如 $n \ll 512$）區間，自注意力不僅完全可並行，且單層浮點運算量更低。
* **WMT 2014 英德與英法機器翻譯雙破紀錄**：
  * **英譯德（EN-DE）**：Transformer (big) 達到 **$28.4$ BLEU**，超越當時包括集成模型（Ensembles）在內的所有既有最佳系統超過 $2.0$ BLEU。
  * **英譯法（EN-FR）**：單一 Transformer (big) 模型達到 **$41.8$ BLEU**，創下單模型最高紀錄。
* **訓練算力與時間大幅下降**：基礎模型（Base Model）在 8 顆 NVIDIA P100 GPU 上僅需訓練 **12 小時**（10 萬步），大型模型（Big Model）僅需訓練 **3.5 天**（30 萬步，總算力 $2.3 \times 10^{19}$ FLOPs），僅為當時頂尖競爭模型（如 ConvS2S Ensemble、GNMT+RL Ensemble）訓練算力成本的四分之一至數十分之一。
* **英語句法成分剖析（Constituency Parsing）遷移能力**：在 WSJ 測試集上，僅用 WSJ 訓練集達到 $91.3$ F1，半監督設置下達到 $92.7$ F1，證明自注意力機制無須專門針對句法樹設計即可自動習得深層語法結構。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **雙向編碼與自迴歸解碼的雙雄分流（BERT 與 GPT）**：Devlin et al. (2019), *NAACL* (arXiv:1810.04805) 取 Transformer 編碼器開創遮罩語言模型 BERT；Radford et al. (2018–2019) 與 Brown et al. (2020), *NeurIPS* 33:1877-1901 (GPT-3) 取 Transformer 解碼器並擴展至 1,750 億參數，驗證上下文少樣本學習（In-Context Learning）之湧現。
* **神經擴展定律（Scaling Laws）**：Kaplan et al. (2020), arXiv:2001.08361 與 Hoffmann et al. (2022, Chinchilla), arXiv:2203.15556，證明 Transformer 的交叉熵測試損失隨模型參數規模 $N$、資料量 $D$ 與訓練算力 $C$ 跨越七個數量級呈現精確的冪律下降關係。
* **跨模態大一統（ViT、AlphaFold2、DiT）**：Dosovitskiy et al. (2021, *ICLR*, Vision Transformer) 將影像切分為 $16 \times 16$ 圖塊直接輸入 Transformer；Jumper et al. (2021, *Nature*, AlphaFold2) 以 Evoformer 注意力解開蛋白質摺疊；Peebles & Xie (2023, *ICCV*, Diffusion Transformer) 將注意力與擴散模型結合，成為 Sora 物理世界模擬器的骨幹。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **演算法與 GPU 硬體的完美共振（Hardware Lottery Winner）**：Transformer 將原本細碎的序列時序操作全部轉化為高密度的通用矩陣乘法（GEMM），完美契合 GPU Tensor Cores 的硬體特性，直接開啟了萬卡算力集群時代。
* **模態壁壘的消融（Universal Modality Agnosticism）**：只要能將資訊離散化或投影為向量序列（Tokens）——無論是文字、程式碼、影像圖塊、音訊頻譜、胺基酸序列、DNA 鹼基或機器人關節動作——皆可由同一套 Transformer 架構統一建模。
* **動態路由與可解釋表徵**：注意力權重矩陣 $\operatorname{softmax}(QK^\top/\sqrt{d_k})$ 相當於根據每次輸入內容即時生成的「動態軟性連線（Dynamic Soft Wiring）」，突破了傳統神經網路推論時權重固定不變的限制。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
《Attention Is All You Need》是科學與工程史上**「減法哲學」**的巔峰之作：

1. **拿掉人為強加的歸納偏置（Inductive Bias），讓資料與規模說話**：在 2017 年以前，研究者總是把注意力機制當作 RNN 或 CNN 的附屬配件；Vaswani 等人敢於問出「如果把 RNN 整個拆掉，只留注意力會怎樣？」，證明過度精密的順序結構反而束縛了模型的全局視野。
2. **與統計物理 Hopfield 網路的跨時空閉環**：1982 年 Hopfield 用二次能量函數定義聯想記憶，35 年後 Transformer 的縮放點積注意力被證明正是「指數型能量函數之現代連續 Hopfield 網路」的單步自由能極小化更新，完成了物理學與深度學習的完美閉環。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [生成式世界模型與擴展定律](../concepts/generative-world-models.md)
  * [AI 驅動之結構生物學與分子設計](../concepts/ai-for-structural-biology.md)
  * [神經迴路因果解耦](../concepts/neural-circuits.md)
* **原始權威文獻**：
  * 官方學術出處：Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Advances in Neural Information Processing Systems (NeurIPS), 30, 5998-6008. arXiv: [1706.03762](https://arxiv.org/abs/1706.03762)
  * 原始檔典藏：`raw/2017-attention-is-all-you-need.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
