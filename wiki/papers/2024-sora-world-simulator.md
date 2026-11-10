---
title: "Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models"
title_zh: "Sora 與世界模型時空物理模擬：基於擴散轉換器（DiT）與時空圖塊的視覺生成湧現"
paper_year: 2024
award_year: 2024
timeline_year: 2024
authors: "Yixin Liu, Kai Zhang, Yuan Li, Zhiling Yan, Chujie Gao, Ruoxi Chen, Zhengqing Yuan, Yue Huang, Hanchi Sun, Jianfeng Gao, Lifang He, Lichao Sun"
venue: "arXiv preprint, arXiv:2402.17177"
domain: "ai"
domain_tags: ["#計算機視覺", "#人工智慧", "#深度學習"]
concepts: ["generative-world-models"]
status: "published"
verification: "issues"
my_focus: false
doi_url: "https://arxiv.org/abs/2402.17177"
key_papers:
  - "Peebles, W., & Xie, S. (2023) Scalable Diffusion Models with Transformers (DiT). Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 4195-4205. https://doi.org/10.1109/ICCV51070.2023.00387"
  - "Brooks, T., Peebles, B., Holmes, C., DePue, W., Guo, Y., Jing, L., Schnurr, D., Taylor, J., Luhman, T., Luhman, E., Ng, C., Wang, R., & Ramesh, A. (2024) Video generation models as world simulators. OpenAI Technical Report. https://openai.com/research/video-generation-models-as-world-simulators"
  - "Liu, Y. et al. (2024) Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models. arXiv:2402.17177. https://arxiv.org/abs/2402.17177"
hook: "將不同時長、解析度與長寬比的影片統一壓縮為三維「時空圖塊（Spacetime Patches）」，以擴散轉換器（DiT）取代傳統 U-Net 骨幹，展現出隨訓練算力擴展而湧現的三維視角一致性與物理世界模擬能力。"
card_line: "把影片切成時空小塊，生成連貫的長影片"
---

# Sora 與世界模型時空物理模擬：基於擴散轉換器（DiT）與時空圖塊的視覺生成湧現

> 「當大型語言模型將人類知識統一為一維文字 Token 時，Sora 將流動的三維光影與時間切分成時空圖塊（Spacetime Patches），讓神經網路在去噪過程中自發領悟透視、遮擋與運動的直覺物理。」

**2024 發表 ｜ 視覺世界模型與擴散轉換器突破**

> **本頁範圍說明**：OpenAI 於 2024 年 2 月發布 Sora 及其技術簡報《Video generation models as world simulators》（Brooks, Peebles et al., 2024），未提供獨立長篇 PDF。本庫 `raw/2024-sora-world-simulator.pdf` 典藏之原始檔為 Lehigh University 與 Microsoft Research 團隊（Liu et al., 2024, arXiv:2402.17177）針對 Sora 架構逆向拆解與大型視覺模型技術演進所撰寫之系統性綜述，並以 Peebles & Xie (2023) 之擴散轉換器（Diffusion Transformer, DiT）與 OpenAI 官方技術報告為核心理論基礎。三篇文獻一併列於 `key_papers`。

---

## Card 1 ｜ 時代銘文 (The Hook)
OpenAI 報告指出，過去的圖像與影片生成做法通常把訓練影片縮放、裁切或截短成標準尺寸，例如 4 秒、$256 \times 256$ 解析度（§Variable durations, resolutions, aspect ratios）。2024 年 2 月，OpenAI 發布 **Sora** 與技術報告（Brooks, Peebles et al., 2024；Peebles 亦為擴散轉換器 DiT 之第一作者），展示可生成長達一分鐘、具動態攝影機運鏡的高畫質影片，且常能（但並非總是）在人物或物體被短暫遮擋後維持其存在（Object Permanence）。其核心做法是把大語言模型「Token 化 ＋ Transformer 擴展」的路線遷移到影片：先壓縮成時空潛在表示、切成時空圖塊，再交給擴散轉換器處理；報告同時列舉其作為世界模擬器的局限，例如無法準確模擬玻璃碎裂，吃東西時物體狀態不一定正確改變（§Discussion）。

---

## Card 2 ｜ 世紀瓶頸：U-Net 算力天花板與固定裁切導致的空間碎裂 (The Dilemma)
在 Sora 之前，視覺生成模型長期受困於兩大歷史包袱：

* **卷積 U-Net 架構的擴展瓶頸**：自 DDPM 與 Stable Diffusion 以來，擴散模型普遍採用卷積 U-Net 作為去噪主幹。然而，卷積核感受野受限於局部空間，難以維持跨越數百幀（數十秒）的長程時間一致性；且當模型參數與算力放大時，U-Net 缺乏如 LLM Transformer 般平滑且可預測的性能冪律躍升。
* **固定解析度與正方形強行裁切（Cropping Bias）的毒害**：傳統影片訓練管線為了拼成固定形狀張量，強制將所有訓練影片剪裁為固定時長（如 16 幀）、固定正方形比例。這導致大量訓練畫面中的主體被截斷，模型無法學習完整的構圖美學、廣角鏡頭運動與跨時間尺度的因果物理。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
Sora 建構於三大核心技術支柱之上：**三維時空潛在壓縮**、**時空圖塊化（Spacetime Patchification）**與**擴散轉換器（Diffusion Transformer, DiT）**。在架構解讀上，需明確區分 OpenAI 官方報告已公開機制與學界（Liu et al. 2024）之分析推測：

1. **時空潛在壓縮網路（Video Compression Network）**：
   * 官方報告指出，模型訓練一個在時間維度 $T$ 與空間維度 $H \times W$ 同步降維的網路，將高維原始像素影片 $X \in \mathbb{R}^{T \times H \times W \times 3}$ 映射為緊湊的低維三維潛在張量 $Z \in \mathbb{R}^{t \times h \times w \times c}$，解碼器則負責將潛在向量映射回像素空間。學界（Liu et al. 2024）推測其為基於 3D 卷積或因果時間卷積的時空 VAE 架構（如 MagViT-v2 風格）。
2. **時空圖塊（Spacetime Patches）作為視覺 Token**：
   * 借鏡 Vision Transformer（ViT）與 ViViT 思想，將三維潛在張量 $Z$ 切分為固定體積為 $p_t \times p_h \times p_w$ 的三維圖塊序列並展平為一維序列。正因為輸入是一維序列，無論原始影片是橫屏、豎屏、單張靜態圖片（$T=1$）還是 60 秒長片，皆能以**原生解析度與長寬比（Native Aspect Ratio）**直接打包進同一個 Transformer 進行訓練。
3. **擴散轉換器（DiT）與乾淨圖塊預測目標**：
   * 以純 Transformer 骨幹取代 U-Net。**關鍵差異在於**：經典 DiT（Peebles & Xie 2023）採用噪聲預測（$\epsilon$-prediction），而 OpenAI 官方報告明確指出 Sora 訓練於**給定噪聲圖塊與條件資訊下直接預測原始乾淨圖塊（Predict the original clean patches）**。DiT 經典設計中的自適應層正規化（adaLN-Zero）與密集影片重標註（Recaptioning）共同引導去噪生成。

### 1. 時空潛在壓縮與圖塊序列映射 (Spacetime Patch Tokenization)

給定原始影片 $X \in \mathbb{R}^{T \times H \times W \times 3}$，經時空壓縮網路映射至潛在空間 $Z \in \mathbb{R}^{t \times h \times w \times c}$（下採樣倍率分別為 $r_t, r_s, r_s$）。接著以體積為 $p_t \times p \times p$ 的三維圖塊將 $Z$ 切分為 $N$ 個時空 Token：

$$\begin{aligned}
N &= \frac{t}{p_t} \cdot \frac{h}{p} \cdot \frac{w}{p} \\
u_i &= W_{\text{patch}}\,\operatorname{vec}(Z_i) + \mathbf{p}_i^{\text{3D}} \in \mathbb{R}^d, \quad i \in \{1, \dots, N\}
\end{aligned}$$

其中 $\mathbf{p}_i^{\text{3D}}$ 為三維時空座標 $(t_i, y_i, x_i)$ 之位置編碼（OpenAI 未公開具體編碼形式，學界綜述推測可採 3D-RoPE 或正弦時空編碼），使模型在任意解析度與時長下皆能感知圖塊間的相對時空位置。

### 2. 擴散轉換器之乾淨圖塊預測目標 (Clean Patch Diffusion Objective)

在連續潛在空間中，將真實影片圖塊序列 $U_0 = [u_1, \dots, u_N]$ 與標準高斯雜訊 $\epsilon \sim \mathcal{N}(0, I)$ 依擴散時間步 $\tau \in [0, 1]$ 進行加噪：$U_\tau = \alpha_\tau U_0 + \sigma_\tau \epsilon$。與經典 DiT 預測雜訊 $\epsilon$ 不同，OpenAI 技術報告明示 Sora 訓練目標為預測原始「乾淨」圖塊 $\hat{U}_0$：

$$\begin{aligned}
\mathcal{L}_{\text{Sora}}(\theta) &= \mathbb{E}_{U_0, \epsilon, \tau, c_{\text{text}}} \left[ \left\| \hat{U}_0(U_\tau, \tau, c_{\text{text}}) - U_0 \right\|_2^2 \right]
\end{aligned}$$

在作為基礎參考的經典 DiT 架構（Peebles & Xie 2023）中，條件注入機制採自適應層正規化（adaLN-Zero），由條件向量 $(c_{\text{text}}, \tau)$ 動態調製正規化特徵：

$$\operatorname{adaLN}(h, \tau, c) = \gamma(\tau, c) \odot \frac{h - \mu(h)}{\sigma(h)} + \beta(\tau, c)$$

### 3. 算力與生成品質 (Compute and Sample Quality)

Peebles & Xie (2023) 以 12 種 DiT 設定（0.3 至 118.6 Gflops）測試，發現模型單次前向運算量（Gflops）與 FID-50K 呈強負相關（相關係數 $-0.93$，圖 8，p. 8）：運算量越大，生成品質越好。OpenAI 報告則以固定種子與輸入，比較基礎、4 倍與 32 倍訓練算力下的樣本，指出樣本品質隨訓練算力增加而明顯提升（§Scaling transformers for video generation），但未公布定量的擴展曲線或冪律參數。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇綜述（Liu et al. 2024）與底層基礎論文（Peebles & Xie 2023; Brooks et al. 2024）之核心證據
* **DiT 奠基數據（Peebles & Xie 2023）**：在 ImageNet 類別條件生成基準上，DiT-XL/2（$118.6\,\text{Gflops}$）搭配無分類器引導，於 $256 \times 256$ 將 FID-50K 降至 **$2.27$**（此前最佳為 LDM 的 $3.60$，p. 8），於 $512 \times 512$ 達 **$3.04$**（表 3，p. 9；ADM-G、ADM-U 為 $3.94$），作者稱其優於先前所有擴散模型；12 種設定之模型 Gflops 與 FID-50K 相關係數為 $-0.93$（圖 8，p. 8）。
* **訓練算力對照（Brooks et al. 2024）**：OpenAI 以固定種子與輸入，展示同一模型在基礎算力、4 倍與 32 倍訓練算力下的樣本，指出樣本品質隨訓練算力增加而明顯提升（§Scaling transformers for video generation）。報告只提供影片樣本，未給定量指標。
* **原生長寬比的構圖比較**：OpenAI 將 Sora 與一個把所有訓練影片裁成正方形的版本比較，後者有時生成主體只部分入鏡的畫面，Sora 的取景較佳（§Improved framing and composition）；Liu et al. (2024) 亦據此指出以原尺寸訓練改善構圖與取景（圖 6，p. 7）。此為樣本之質性比較，沒有量化指標。
* **零樣本多任務渲染與物理模擬局限（Brooks et al. 2024）**：無須針對特定下游任務微調，同一模型可直接執行圖片轉影片動畫化、前後時間時空延展、迴圈無縫影片生成與風格編輯；提示詞包含特定名稱時，甚至能以零樣本渲染類似《Minecraft》之玩家視角遊戲動態畫面。然而，OpenAI 報告在討論章節明言其作為世界模擬器存在眾多局限：模型無法準確模擬許多基礎物理交互（例如玻璃碎裂動力學），且涉及實體狀態改變的互動（如吃食物時常未能留下咬痕）往往無法維持因果一致性，並伴隨長影片主體漂移或物件憑空出現等典型失敗模式。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **後續公開技術報告之大型影片生成模型**：2024–2025 年間，數個團隊發表影片生成模型之技術報告。CogVideoX 以擴散 Transformer 為基礎，以 3D VAE 在空間與時間兩個維度壓縮影片，並公開模型權重（Yang et al. 2024, arXiv:2408.06072）；Meta 之 Movie Gen 最大影片模型為 300 億參數之 Transformer，上下文長度 73K 個影片詞元，對應每秒 16 幀、長 16 秒之影片（Polyak et al. 2024, arXiv:2410.13720）；騰訊 HunyuanVideo 為逾 130 億參數之開源影片模型，並公開程式碼（Kong et al. 2024, arXiv:2412.03603）；阿里 Wan 建立於主流之擴散 Transformer 範式，開源 1.3B 與 14B 兩種規模（Wan Team 2025, arXiv:2503.20314）。以上僅依各報告摘要所述；各摘要未稱沿用 Sora 之架構，Sora 之技術細節亦未公開，故不據此推論兩者之承接關係。
* **以物理定律檢驗影片生成模型（Kang et al. 2024）**：Kang et al.（arXiv:2411.02385，2024 年 11 月；ICML 2025，"How Far is Video Generation from World Model: A Physical Law Perspective"）以二維物體運動與碰撞的模擬資料訓練擴散式影片生成模型，發現模型在訓練分布內可完美泛化、組合泛化隨規模改善，但在分布外情境失敗；模型並未抽象出一般物理規律，而是模仿最相近的訓練案例。作者據此認為，單靠擴大規模不足以讓影片生成模型發現基本物理定律（摘要）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **視覺與語言架構的徹底大一統**：繼 LLM 將文字化為 1D Token 後，Sora 證明連續的四維時空（3D 空間 ＋ 1D 時間）同樣可以被離散/連續圖塊化並交由標準 Transformer 統治，打通了原生多模態世界模型的任督二脈。
* **朝向「直覺物理模擬」的初步探索與長程挑戰**：為了在數萬個時空圖塊之間極小化預測誤差，模型在隱藏層呈現出對三維視角與光影運動的隱式關聯建模。然而，這種基於高維視覺統計關聯的模擬與顯式因果物理引擎仍有本質區別，模型常在缺乏足夠數據先驗的非典型物理交互中失效，距離真正具備可靠因果推理與物理封閉性的世界模型仍具巨大差距。
* **影視工業、模擬訓練與具身智能（Embodied AI）的合成數據引擎**：自動駕駛與人形機器人訓練長期受限於真實世界長尾極端場景（Corner Cases）數據不足；高保真生成式世界模型可作為可交互的虛擬物理沙盒，為強化學習代理提供無限合成環境。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
Sora 與時空 DiT 的崛起印證了資訊理論與認知科學的深層交會：

1. **壓縮即理解，預測即模擬**：要在時間維度上準確預測下一秒的千萬個像素如何變化，神經網路被迫在潛在空間中重演柏拉圖的「洞穴寓言」——透過觀察二維牆壁上的光影投影（訓練影片），反推出背後三維真實世界的幾何與物理規則。
2. **表徵的靈活性決定規模的上限**：放棄刻板的正方形裁剪、擁抱可變長度的時空圖塊序列，看似只是一個資料前處理的工程改進，實則解開了束縛視覺模型讀取全人類原生影像遺產的枷鎖。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [生成式世界模型與擴展定律](../concepts/generative-world-models.md)
* **原始權威文獻**：
  * 官方技術報告：Brooks, T., Peebles, B. et al. (2024). Video generation models as world simulators. OpenAI Technical Report.
  * 奠基架構文獻：Peebles, W., & Xie, S. (2023). Scalable Diffusion Models with Transformers. ICCV 2023, 4195-4205. DOI: [10.1109/ICCV51070.2023.00387](https://doi.org/10.1109/ICCV51070.2023.00387)
  * 系統綜述文獻：Liu, Y. et al. (2024). Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models. arXiv: [2402.17177](https://arxiv.org/abs/2402.17177)
  * 原始檔典藏：`raw/2024-sora-world-simulator.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2024-sora-world-simulator.md](../evidence/2024-sora-world-simulator.md)
