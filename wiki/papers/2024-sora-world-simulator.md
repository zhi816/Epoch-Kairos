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
verification: "partial"
my_focus: false
doi_url: "https://arxiv.org/abs/2402.17177"
key_papers:
  - "Peebles, W., & Xie, S. (2023) Scalable Diffusion Models with Transformers (DiT). Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 4195-4205. https://doi.org/10.1109/ICCV51070.2023.00387"
  - "Brooks, T., Peebles, B., Holmes, C., DePue, W., Guo, Y., Jing, L., Schnurr, D., Taylor, J., Luhman, T., Luhman, E., Ng, C., Wang, R., & Ramesh, A. (2024) Video generation models as world simulators. OpenAI Technical Report. https://openai.com/research/video-generation-models-as-world-simulators"
  - "Liu, Y. et al. (2024) Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models. arXiv:2402.17177. https://arxiv.org/abs/2402.17177"
hook: "將不同時長與長寬比的影片壓縮並切成時空圖塊，以擴散轉換器生成影片；公開樣本呈現部分視角一致性，也顯示物理互動的限制。"
card_line: "把影片切成時空小塊，生成連貫的長影片"
---

# Sora 與世界模型時空物理模擬：基於擴散轉換器（DiT）與時空圖塊的視覺生成湧現

> 「影片先壓縮並切成時空圖塊，再由擴散轉換器生成；樣本的連貫性與物理互動仍有明確限制。」（本頁引言為 Wiki 撰寫，非原文）

**2024 發表 ｜ 視覺世界模型與擴散轉換器突破**

> **本頁範圍說明**：OpenAI 於 2024 年 2 月發布 Sora 及其技術簡報《Video generation models as world simulators》（Brooks, Peebles et al., 2024），未提供獨立長篇 PDF。本庫 `raw/2024-sora-world-simulator.pdf` 典藏之原始檔為 Lehigh University 與 Microsoft Research 團隊（Liu et al., 2024, arXiv:2402.17177）針對 Sora 架構逆向拆解與大型視覺模型技術演進所撰寫之系統性綜述，並以 Peebles & Xie (2023) 之擴散轉換器（Diffusion Transformer, DiT）與 OpenAI 官方技術報告為核心理論基礎。三篇文獻一併列於 `key_papers`。

---

## Card 1 ｜ 時代銘文 (The Hook)
OpenAI 報告指出，過去的圖像與影片生成做法通常把訓練影片縮放、裁切或截短成標準尺寸，例如 4 秒、$256 \times 256$ 解析度（§Variable durations, resolutions, aspect ratios）。2024 年 2 月，OpenAI 發布 **Sora** 與技術報告（Brooks, Peebles et al., 2024；Peebles 亦為擴散轉換器 DiT 之第一作者），展示可生成長達一分鐘、具動態攝影機運鏡的高畫質影片，且常能（但並非總是）在人物或物體被短暫遮擋後維持其存在（Object Permanence）。其核心做法是把大語言模型「Token 化 ＋ Transformer 擴展」的路線遷移到影片：先壓縮成時空潛在表示、切成時空圖塊，再交給擴散轉換器處理；報告同時列舉其作為世界模擬器的局限，例如無法準確模擬玻璃碎裂，吃東西時物體狀態不一定正確改變（§Discussion）。

---

## Card 2 ｜ 世紀瓶頸：U-Net 算力天花板與固定裁切導致的空間碎裂 (The Dilemma)
OpenAI 報告指出，過去部分圖像與影片生成做法會將資料縮放、裁切或截短為固定解析度與時長，例如 4 秒、$256 \times 256$。作者比較在原生尺寸與裁成正方形資料上訓練的模型，觀察到後者有時只生成畫面主體的一部分。另一個研究問題是：擴散轉換器在影片生成中的樣本品質，是否會隨訓練算力增加而改善（§Variable durations, resolutions, aspect ratios；§Scaling transformers for video generation）。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
OpenAI 技術報告公開的是高層流程，並明言不提供模型與實作細節；Liu 等（2024）圖 4 則是綜述作者的逆向推測，不能直接當成 Sora 已證實的內部架構。

### 1. 時空壓縮與圖塊序列

報告描述一個同時壓縮影片時間與空間維度的網路，另以解碼器將生成的潛在表示映回像素。壓縮後的表示被切成時空圖塊，作為 Transformer 的輸入；單張圖片可視為只有一個時間影格的影片。這種表示支援不同時長、解析度與長寬比（§Video compression network；§Spacetime latent patches）。

### 2. 從帶雜訊圖塊預測乾淨圖塊

OpenAI 描述 Sora 是擴散轉換器：訓練時給定帶雜訊的圖塊與文字等條件資訊，模型預測原始乾淨圖塊（§Scaling transformers for video generation）。報告未公開此處的具體損失函數、圖塊嵌入或位置編碼公式。Peebles 與 Xie（2023）的 DiT 研究了 adaLN-Zero；這是相關架構的已公開設計，不能據此斷定 Sora 使用相同機制。

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
* **以圖塊處理不同尺寸的視覺資料**：OpenAI 將影片與圖片壓縮後切成時空圖塊，再以 Transformer 處理，讓同一表示方式適用於不同尺寸與時長的輸入。
* **物理模擬仍有邊界**：報告展示部分視角變化與遮擋連貫的樣本，也指出玻璃破碎及進食後物體狀態可能不正確。這些輸出現象並未直接驗證模型隱藏層是否建構三維幾何或物理規則。
* **可能的後續用途**：生成影片可供研究合成資料與模擬，但是否適合互動控制或特定訓練任務，仍須針對物理一致性與失敗情況獨立驗證。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
**Wiki 延伸**：可變尺寸的時空圖塊提供一個設計思路：先選擇能容納不同資料形狀的表示，再檢驗模型能否從中生成有用的結果。影片看起來連貫，不等於模型已推導出世界幾何或物理定律；這仍須透過獨立實驗檢驗。

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
