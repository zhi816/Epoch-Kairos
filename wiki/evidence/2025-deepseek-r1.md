# 證據表：2025-deepseek-r1
- **採用版本**：正式版。DeepSeek-AI (Guo, D., Yang, D., Zhang, H., Song, J. et al.) (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *Nature*, 645(8081), 633–638. DOI: [10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z)。封存原文 `raw/2025-deepseek-r1.pdf` 為對應 Nature 版之全文與補充資料（86 頁，PDF 頁碼即印刷頁碼）。arXiv 初版 2501.12948v1 之 R1-Zero 數字（AIME 71.0%、與 o1-0912 比較）與正式版不同，本表與頁面不採用。演算法奠基來源：Shao, Z. et al. (2024). DeepSeekMath, arXiv:2402.03300（提出 GRPO）。
- **查核者**：先前版本由多位代理建立（EK-037、EK-038、EK-046）；2026-11-10 由 Claude Code by Anthropic（Claude Opus 5.5）依原文逐項重建本表（EK-113、EK-152、EK-153）。

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Card 1 | R1-Zero 直接在 DeepSeek-V3-Base 上做大規模純強化學習，不經監督微調；R1 另用數千筆冷啟動資料、多階段強化學習、拒絕採樣與監督微調 | 本篇研究結果 | §1, pp. 1–2；§2.3, p. 4；§3, p. 6（「thousands of cold-start data」） | 符合來源 |
| Card 1 | 約 80 萬筆監督資料（approximately 800,000 supervised samples），蒸餾以同一批 800k 資料微調 2–3 個 epoch | 本篇研究結果 | Supplementary B.3.3, pp. 26–27；B.4.3, p. 35（「using the 800k data」） | 符合來源 |
| Card 2 | 價值模型通常與策略模型規模相近，帶來顯著記憶體與運算負擔；只有最終結果獎勵時價值模型難以由部分回答預測最終獎勵 | 作者解釋 | Supplementary A.3, pp. 14–15 | 符合來源 |
| Card 2 | 神經獎勵模型在大規模強化學習中易遭獎勵駭客利用，重新訓練需大量算力 | 作者解釋 | §2.2, p. 4 | 符合來源 |
| Card 3 | 區塊公式：GRPO 目標函數 $\mathcal{J}_{GRPO}(\theta)$ | 本篇研究結果 | §2.1, p. 3，式 (1)；Supplementary A.3, p. 15，式 (11) | 符合來源 |
| Card 3 | 區塊公式：KL 無偏估計量 $\mathbb{D}_{KL}(\pi_\theta \Vert \pi_{ref}) = \pi_{ref}/\pi_\theta - \log(\pi_{ref}/\pi_\theta) - 1$（原頁面加註之「≥ 0」原文沒有，已刪，EK-152）；採 Schulman (2020) 之無偏估計並直接加入損失 | 本篇研究結果 | §2.1, p. 3，式 (2)；Supplementary A.3, p. 15，式 (12) 與正文 | 符合來源 |
| Card 3 | 區塊公式：優勢 $A_i = (r_i - \mathrm{mean}(\{r_1, \cdots, r_G\})) / \mathrm{std}(\{r_1, \cdots, r_G\})$ | 本篇研究結果 | §2.1, p. 3，式 (3) | 符合來源 |
| Card 3 | 區塊公式：規則獎勵 $Reward_{\text{rule}} = Reward_{\text{acc}} + Reward_{\text{format}}$，兩項等權；不對推理任務使用神經獎勵模型 | 本篇研究結果 | §2.2, p. 4，式 (4) | 符合來源 |
| Card 3 | 訓練設定：學習率 3e-6、KL 係數 0.001、每題取樣 16 個輸出、每 400 步更新參考模型 | 本篇研究結果 | §2.1, p. 3 | 符合來源 |
| Card 3 | 格式獎勵要求思考過程置於 think 標籤；範本另要求答案置於 answer 標籤 | 本篇研究結果 | §2.2, p. 4；Table 1, p. 3 | 符合來源 |
| Card 3 | Qwen2.5-32B 上，蒸餾 R1 優於同一基座直接做大規模強化學習 | 本篇研究結果 | Supplementary F.1, Table 16, p. 61；p. 62 正文 | 符合來源 |
| Card 4 | R1-Zero AIME 2024 平均 pass@1 由初始 15.6% 升至 77.9%（修正 EK-113：原寫 71.0% 為 arXiv 初版數字） | 本篇研究結果 | §2.3, p. 4，正文與 Figure 1(a) | 符合來源 |
| Card 4 | R1-Zero 以自我一致性解碼（cons@16）提高到 86.7%，明顯高於人類參賽者平均 | 本篇研究結果 | p. 5 正文；Figure 1(a) 圖例 r1-zero-cons@16（p. 4） | 符合來源 |
| Card 4 | R1-Zero 共訓練 10,400 步（1.6 epoch）；第 8.2k 步最大長度由 32,768 提高到 65,536 Token，表現與長度明顯躍升（修正 EK-113：原寫 8,000 多步） | 本篇研究結果 | §2.1, p. 3 | 符合來源 |
| Card 4 | 平均思考長度隨訓練穩定增加，以數百至數千 Token 探索解法；Table 2 頓悟時刻原句（方程式求實根之和）；「wait」用字突然增加 | 本篇研究結果 | Figure 1(b), p. 4；p. 5 正文；Table 2, p. 5；Supplementary C.2, Figure 9(b) | 符合來源 |
| Card 4 | Table 8：DeepSeek-R1 列 AIME 2024 pass@1 79.8（o1-1217 列 79.2）；MATH-500 pass@1 97.3（o1-1217 96.4）；Codeforces Rating 2029（o1-1217 2061）；Codeforces Percentile 96.3（o1-1217 96.6）；GPQA Diamond pass@1 71.5（o1-1217 75.7）；MMLU EM 90.8（o1-1217 91.8） | 本篇研究結果 | Supplementary D.2, Table 8, p. 41 | 符合來源 |
| Card 4 | R1 AIME 2024 pass@64 為 90.0%，多數決由 79.8% 提高到 86.7%（cons@64）；原頁面稱 cons@64 與 o1-1217 持平，原文沒有此比較，已刪（EK-113） | 本篇研究結果 | Supplementary E.4, p. 60；cons@64 定義見 D.1, p. 41 | 符合來源 |
| Card 4 | pass@1 之計算：溫度 0.6、top-p 0.95，AIME 與 GPQA 取 k = 64 | 本篇研究結果 | Supplementary D.1, pp. 40–41 | 符合來源 |
| Card 4 | Table 16：DeepSeek-R1-Distill-Qwen-32B 列 AIME 2024 pass@1 72.6、cons@64 83.3、MATH pass@1 94.3；Qwen2.5-32B-Zero 列 AIME 2024 pass@1 47.0、cons@64 60.0、MATH pass@1 91.6；QwQ-32B-Preview 列 50.0、60.0、90.6 | 本篇研究結果 | Supplementary F.1, Table 16, p. 61 | 符合來源 |
| Card 4 | Qwen2.5-32B-Zero 以數學、程式與 STEM 資料訓練超過 10K 步；作者結論：蒸餾效果極佳，小模型靠大規模強化學習需龐大算力且未必達到蒸餾表現 | 作者解釋 | Supplementary F.1, p. 62 | 符合來源 |
| Card 5 | 公開資源：R1 與 R1-Zero 權重（HuggingFace）；六個蒸餾模型（Qwen 1.5B、7B、14B、32B，Llama 8B、70B）；推論程式與使用說明（GitHub）；SFT 與 RL 資料之網址原文為「xxx」，審查期間以附件提供 | 本篇研究結果 | Supplementary I, pp. 65–66；§1, p. 2 | 符合來源 |
| Card 5 | 作者明列之限制：結構化輸出與工具使用、Token 效率（過度思考）、語言混雜、對提示敏感（少樣本降低表現）、軟體工程任務進步有限 | 作者解釋 | §6, pp. 10–11 | 符合來源 |
| Card 5 | 純強化學習之挑戰：難建構可靠獎勵之任務（如寫作）擴大純強化學習仍是開放問題 | 作者解釋 | §6, p. 11 | 符合來源 |
| Card 5 | 作者所述未來方向：下一版處理結構化輸出與工具使用；軟體工程以拒絕採樣或非同步評估改進；穩健獎勵模型；推理中使用工具 | 作者解釋 | §6, pp. 10–11 | 符合來源 |
| Card 5 | 原文自述啟發後續探索（Face 2025、Liu et al. 2025、Pan et al. 2025）；本頁未逐篇查核，不列為後續研究 | 作者解釋 | Supplementary H.3, p. 65 | 符合來源 |
| Card 6 | 頓悟時刻、反思行為與組內比較之啟發 | Wiki 詮釋 | 所據事實見本表 Card 3、Card 4 各列 | 不適用 |
