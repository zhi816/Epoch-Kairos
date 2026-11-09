# 證據表：2025-deepseek-r1

本表記錄 [wiki/papers/2025-deepseek-r1.md](../papers/2025-deepseek-r1.md) 各項主張在第一手文獻中的出處與核驗結果。

- **主要第一手來源**：DeepSeek-AI (Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X. et al., & Liang, W.) (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *Nature*, 645(8081), 633–638 (2025). DOI: [10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z); 原預印本: *arXiv:2501.12948*.
- **封存原文**：`raw/2025-deepseek-r1.pdf`

---

| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |
|---|---|---|---|
| Card 1 | 嚴格區分 DeepSeek-R1-Zero（純 RL 無 SFT）與 DeepSeek-R1（冷啟動 ＋ RL ＋ 拒絕採樣 SFT ＋ 二次 RL） | §2.1 (p. 2), §2.3 (pp. 5–6) | 核實更正。原文明確區分：僅 R1-Zero 為完全不經 SFT 直接從 Base 模型以純 RL 訓練；正式版 DeepSeek-R1 為解決可讀性與混雜語言問題，包含冷啟動（數千筆長 CoT）、推理 RL、拒絕採樣及 80 萬筆混合 SFT、全場景二次 RL 四階段。更正原 Card 1 將 Zero SFT 通用於 R1 之不符表述。 |
| Card 3 | 群體相對策略優化（GRPO）無價值網路與規則獎勵機制 | §2.1.1 (pp. 2–3), Eq. (1)–(3) | 核實符合。以組內 $G$ 個採樣答案獎勵之均值與標準差標準化直接計算優勢 $A_i$，廢除獨立 Critic 網路；採準確度規則獎勵（編譯測試與方框比對）與格式標籤規則獎勵。 |
| Card 4 | DeepSeek-R1-Zero 之 AIME 2024 Pass@1 達 71.0%，多數決達 86.7% | §2.2 (p. 4), Table 1 | 核實更正。原文 Table 1 報告 DeepSeek-R1-Zero 在 AIME 2024 之 Pass@1 為 **$71.0\%$**，多數決 **$86.7\%$** 係基於 **64 次採樣共識（cons@64）**，更正原頁面誤植之「cons@16」。註明出處為 arXiv:2501.12948 Table 1。 |
| Card 4 | DeepSeek-R1 正式版基準：AIME 79.8%（Pass@1）、MATH-500 97.3%、Codeforces 2029 Elo | §2.4 (pp. 7–9), Table 2 | 核實符合。AIME 2024 Pass@1 為 79.8%（cons@64 為 92.5%），MATH-500 為 97.3%，Codeforces Rating 為 2,029（96.3% 百分位），GPQA Diamond 達 71.5%。 |
| Card 4 | 蒸餾 vs. 小模型直接 RL 對照實驗（Qwen-32B） | §3 (pp. 9–10), Table 4, Table 5 | 核實符合。以 R1 生成的 80 萬筆數據微調之 DeepSeek-R1-Distill-Qwen-32B 在 AIME 達 72.6%，顯著超越直接對 Qwen-32B-Base 大規模 RL 所得之 47.0%。 |
| Card 5, 6 | 頓悟時刻（Aha Moment）與測試時運算擴展定律 | §2.2.3 (pp. 4–5), Fig. 3 | 核實符合。模型在未引入長度獎勵下，平均長度自發隨訓練步數增長；觀測到中途自我反思、回溯驗證與重新計算之思維行為。 |
