# 證據表：2025-deepseek-r1

本表記錄 [wiki/papers/2025-deepseek-r1.md](../papers/2025-deepseek-r1.md) 各項主張在第一手文獻中的出處與核驗結果。

- **主要第一手來源**：DeepSeek-AI (Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X. et al.). (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *Nature*, 645(8081), 633–638. DOI: [10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z)（原預印本：*arXiv:2501.12948*）。
- **演算法奠基來源**：Shao, Z. et al. (2024). DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv:2402.03300*. [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300)（提出群體相對策略優化 GRPO）。
- **封存原文**：`raw/2025-deepseek-r1.pdf`（Nature 定稿投審手稿，86 頁）。

---

| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |
|---|---|---|---|
| Frontmatter / Card 1 | R1-Zero 純 RL 與 R1 多階段訓練之嚴格區分 | 原文 §1 Introduction (pp. 1–2), §2 DeepSeek-R1-Zero (pp. 2–5), §3 DeepSeek-R1 (pp. 5–7) | 核實更正（EK-038）。原文明確區分：(1) **DeepSeek-R1-Zero** 係直接在 DeepSeek-V3-Base 上進行大規模純強化學習，完全跳過任何監督式微調（Zero SFT），自發湧現自我反思與長鏈推理；(2) **DeepSeek-R1** 為解決 R1-Zero 語言混雜與可讀性缺陷，採用四階段管線：千筆冷啟動長思維鏈資料 $\to$ 推理導向 RL $\to$ 拒絕採樣與 80 萬筆通用/推理混合資料之 SFT $\to$ 全場景二次偏好 RL。更正將「Zero SFT」同時套用至 R1 之錯誤。 |
| Card 3 | 群體相對策略優化（GRPO）目標函數與無價值網路優勢計算 | 原文 §2.1 (p. 3, 式 1–3); Shao et al. (2024) | 核實符合。GRPO 廢除 Critic 價值網路，自舊策略採樣 $G$ 個輸出，以組內獎勵均值與標準差計算相對優勢 $A_i$（式 3），目標函數包含裁剪項與無偏非負 KL 散度估計量（式 1 與式 2）。 |
| Card 3 | 決定性規則獎勵系統（Rule-Based Verifiable Rewards） | 原文 §2.1 (pp. 3–4, 式 4) | 核實符合。獎勵由準確度獎勵（$R_{\text{acc}}$，數學題目以方框答案正誤比對，程式題以編譯器跑測試用例）與格式獎勵（$R_{\text{format}}$，強制 `<think>` 與 `</think>` 標籤）等權相加。 |
| Card 4 | R1-Zero 於 AIME 2024 之訓練增長軌跡與 cons@16 | 原文 §2.2 (pp. 4–5), Figure 1(a) | 核實符合。在純 RL 訓練 10,400 步中，AIME 2024 Pass@1 由初始 15.6% 增長至 71.0%；16 次採樣多數決（`cons@16`）達到 86.7%，超越人類選手平均成績。 |
| Card 4 | 基準評測與多數決指標：cons@64 與 cons@16 之版本釐清 | 原文 §D.1 (pp. 40–41), §D.2 (Table 8, p. 41), Table 16 (p. 61) | 核實更正（EK-037）。原文在大模型正式基準評測（Table 8）中，多數決共識評估一律採用 64 個樣本採樣（`cons@64`）。DeepSeek-R1 在 AIME 2024 達成之 86.7% 為 `cons@64`（與 OpenAI o1-1217 持平，Pass@1 為 79.8%、Pass@64 達 90.0%）。明確區分訓練軌跡圖（Fig. 1(a) 之 `r1-zero-cons@16`）與正式基準表（Table 8 之 `cons@64`），並標明 Nature 645:633–638 / arXiv:2501.12948 定稿版本。 |
| Card 4 | 推理長度擴展與「頓悟時刻（Aha Moment）」文字記錄 | 原文 §2.2 (pp. 4–5), Figure 1(b), Table 2 | 核實符合。訓練過程中模型平均長度自發由數百 Token 擴展至上萬 Token。Table 2 完整記錄中間檢查點出現之擬人化自我懷疑語句：「*Wait, wait. Wait. That's an aha moment I can flag here... Let's re-evaluate this step-by-step*」。 |
| Card 4 | 蒸餾（Distillation）對比小模型直接純 RL 之決定性實驗 | 原文 §4 (pp. 7–8), Appendix F (Table 16, p. 61) | 核實符合。將 R1 軌跡蒸餾至 Qwen-32B（DeepSeek-R1-Distill-Qwen-32B），AIME 2024 Pass@1 達 72.6%（cons@64 達 83.3%）、MATH-500 達 94.3%；而對 Qwen2.5-32B-Base 耗費龐大算力直接跑大規模純強化學習（Qwen2.5-32B-Zero），AIME 2024 Pass@1 僅達 47.0%（cons@64 達 60.0%）。 |
| Card 5, 6 | 測試時運算擴展定律（Test-Time Compute Scaling）與可驗證獎勵界限 | 原文 §1, §5 (Discussion) | 核實更正（EK-046）。可驗證獎勵（RLVR）在本文嚴格驗證於具備確定性解答之數學定理比對與程式測試用例；將其推廣至任意領域通用驗證器與自主科學探索代理，屬於後續研究展望，非本文直接實驗結果。 |
