---
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
title_zh: "DeepSeek-R1 與推理運算擴展定律：以純強化學習激發大型語言模型之自我反思與長鏈推理湧現"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi et al. (DeepSeek-AI)"
venue: "Nature, 645(8081), 633-638 (2025); and arXiv:2501.12948"
domain: "ai"
domain_tags: ["#人工智慧", "#強化學習", "#深度學習"]
concepts: ["generative-world-models"]
status: "wiki"
verification: "verified"
my_focus: false
doi_url: "https://doi.org/10.1038/s41586-025-09422-z"
key_papers:
  - "Shao, Z. et al. (2024) DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO). arXiv:2402.03300. https://arxiv.org/abs/2402.03300"
  - "DeepSeek-AI (Guo, D. et al.) (2025) DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. arXiv:2501.12948. https://arxiv.org/abs/2501.12948"
hook: "在基礎語言模型上僅憑基於規則的結果獎勵與群體相對策略優化（GRPO），以純強化學習（DeepSeek-R1-Zero）首次公開證明長鏈推理、自我驗證與「頓悟時刻（Aha Moment）」無須人工示範即可自發湧現；並透過多階段冷啟動與蒸餾管線（DeepSeek-R1）全面比肩頂尖閉源推理模型。"
card_line: "以對錯獎勵訓練，讓語言模型學會逐步推理"
---

# DeepSeek-R1 與推理運算擴展定律：以純強化學習激發大型語言模型之自我反思與長鏈推理湧現

> 「我們不需要手把手教導模型每一步該如何思考；只要給予明確的真偽判準與探索空間，強化學習便會讓模型在千萬次試錯中自發學會懷疑、回溯與頓悟。」

**2025 發表 ｜ 推理型大模型（Reasoning LLMs）與開源強化學習突破**

---

## Card 1 ｜ 時代銘文 (The Hook)
當預訓練階段的網際網路語料逐漸趨近枯竭，大型語言模型（LLMs）如何突破複雜數學證明、演算法競賽與科學推理的天花板？過去主流觀點認為，模型必須先依賴大量由人類專家撰寫的高品質「思維鏈（Chain-of-Thought, CoT）」示範數據進行監督式微調（SFT），或是搭配昂貴的過程獎勵模型（Process Reward Model, PRM）與蒙地卡羅樹搜索（MCTS）才能學會深度推理。2025 年 1 月，DeepSeek-AI 發表 **DeepSeek-R1-Zero** 與 **DeepSeek-R1**。其中 **DeepSeek-R1-Zero** 首次向全球嚴格證明：**在完全不使用任何監督微調（Zero SFT）作為前置步驟的情況下**，直接對基礎模型（DeepSeek-V3-Base）施加基於確定性規則獎勵的大規模純強化學習（Pure RL），模型就能自發演化出數千至上萬 Token 的長思維鏈、自我糾錯（Self-Correction）、回溯驗證與驚人的「頓悟時刻（Aha Moment）」；而完整的旗艦模型 **DeepSeek-R1** 則在此突破之上，導入少量高質量冷啟動數據（數千筆），結合多階段大規模強化學習、拒絕採樣（Rejection Sampling）與多領域通用 SFT（約 80 萬筆），徹底解決了純 RL 帶來的可讀性差與中英夾雜缺陷，在 AIME 2024 與 Codeforces 等基準上追平 OpenAI o1 正式版，並將完整權重與訓練配方開源。

---

## Card 2 ｜ 世紀瓶頸：人類標註的天花板與 Critic 價值網路的記憶體高牆 (The Dilemma)
在邁向高階推理模型的道路上，學界曾面臨三大技術枷鎖：

* **人工監督微調（SFT）限制了探索上限**：人類標註的思維鏈不僅極度昂貴，且強行將模型束縛在「人類習慣的線性思考格式」內，阻止了模型透過試錯探索更高效、非人類直覺的推理路徑（正如 AlphaGo Zero 拋棄人類棋譜後方能超越 AlphaGo）。
* **傳統 PPO 強化學習的雙倍記憶體與算力負擔**：標準近端策略優化（PPO）必須額外維護一個與策略模型（Policy Model，如 6,710 億參數）同等規模的價值評估網路（Value/Critic Model）來估計每個 Token 的基線價值，使訓練顯存與通訊開銷翻倍。
* **神經過程獎勵模型（PRM）的獎勵駭客（Reward Hacking）陷阱**：若用另一個神經網路去給推理的每一個中間步驟打分，策略模型在大規模強化學習中極易找到欺騙打分網路的漏洞（輸出看似合理但邏輯錯誤的冗長廢話），導致訓練在中途崩潰。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
DeepSeek-R1 以極簡而堅實的強化學習工程設計，徹底避開了上述陷阱：

1. **群體相對策略優化（Group Relative Policy Optimization, GRPO）**：
   * 徹底**廢除龐大的 Critic 價值模型**。針對每一個輸入問題 $q$，直接從舊策略 $\pi_{\theta_{\text{old}}}$ 中平行採樣一組共 $G$ 個回答 $\{o_1, o_2, \dots, o_G\}$，以這組回答獲得之獎勵分數的**組內平均值與標準差**直接計算每個回答的相對優勢（Advantage）$A_i$，大幅省去一半顯存與計算開銷。
2. **純規則決定性獎勵系統（Rule-Based Verifiable Rewards）**：
   * 在 DeepSeek-R1-Zero 與推理強化階段，不使用容易被駭客攻擊的神經獎勵模型，而是僅採用兩項完全客觀的規則獎勵：
     * **準確度獎勵（Accuracy Reward）**：數學題以確定性規則比對最終方框 `\boxed{}` 內答案是否正確；程式題直接送入編譯器跑真實測試用例（Test Cases）檢驗是否通過。
     * **格式獎勵（Format Reward）**：要求模型將思考過程置於 `<think>` 與 `</think>` 標籤之間、最終答案置於 `<answer>` 與 `</answer>` 之間。
3. **四階段管線（DeepSeek-R1）與能力蒸餾（Distillation）**：
   * 為解決純 RL 模型（R1-Zero）偶發的中英夾雜與可讀性問題，DeepSeek-R1 引入極少量（數千筆）高可讀性冷啟動長思維鏈資料，隨後執行「推理導向強化學習 $\to$ 拒絕採樣生成通用與推理混合 SFT 數據 $\to$ 全場景二次強化學習」四階段管線，並證實將 R1 的推理軌跡直接蒸餾給 1.5B 至 70B 的小模型，效果遠優於讓小模型從頭跑強化學習。

### 1. 群體相對策略優化（GRPO）目標泛函 (GRPO Objective Function)

對每個問題 $q \sim P(Q)$，自舊策略 $\pi_{\theta_{\text{old}}}$ 採樣 $G$ 個輸出序列 $\{o_i\}_{i=1}^G$，策略模型 $\pi_\theta$ 透過最大化以下帶裁剪與直接 KL 散度正規化之目標函數進行更新：

$$\begin{aligned}
\mathcal{J}_{\text{GRPO}}(\theta) = \mathbb{E}_{q \sim P(Q),\, \{o_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(O|q)} \Bigg[ \frac{1}{G} \sum_{i=1}^{G} \Bigg( &\min\left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)} A_i,\; \operatorname{clip}\left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)}, 1-\varepsilon, 1+\varepsilon \right) A_i \right) \\
&- \beta\,\mathbb{D}_{\text{KL}}\left(\pi_\theta \,\|\, \pi_{\text{ref}}\right) \Bigg) \Bigg]
\end{aligned}$$

其中 $\varepsilon$ 為裁剪超參數，$\beta$ 為懲罰偏離參考策略 $\pi_{\text{ref}}$ 之係數。

### 2. 無價值網路之組內標準化優勢與無偏 KL 估計 (Group-Normalized Advantage & KL Estimator)

設第 $i$ 個回答經規則驗證器獲得之純量總獎勵為 $r_i = R_{\text{acc}}(q, o_i) + R_{\text{fmt}}(o_i)$。組內第 $i$ 個回答的相對優勢 $A_i$ 直接由該組 $G$ 個樣本之Z-score 標準化給出：

$$A_i = \frac{r_i - \operatorname{mean}\left(\{r_1, r_2, \dots, r_G\}\right)}{\operatorname{std}\left(\{r_1, r_2, \dots, r_G\}\right)}$$

同時，為確保 KL 散度項恆為非負且低方差，採用 Schulman 無偏非負估計量：

$$\begin{aligned}
\mathbb{D}_{\text{KL}}\left(\pi_\theta \,\|\, \pi_{\text{ref}}\right) &= \frac{\pi_{\text{ref}}(o_i|q)}{\pi_\theta(o_i|q)} - \log \frac{\pi_{\text{ref}}(o_i|q)}{\pi_\theta(o_i|q)} - 1 \ge 0
\end{aligned}$$

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（DeepSeek-AI 2025）之核心證據
* **DeepSeek-R1-Zero 純 RL 之 AIME 訓練軌跡與多數決躍升**：在完全不給任何人工思維鏈範例的純強化學習過程中（對照 Nature 645:633–638 / arXiv:2501.12948 原文 §2.2 與 Figure 1(a)），DeepSeek-R1-Zero 在美國數學邀請賽（AIME 2024）上的單次採樣通過率（Pass@1）從初始的 **$15.6\%$** 穩步飆升至 **$71.0\%$**（與 OpenAI o1-0912 持平）；若結合 16 次採樣多數決（`cons@16`，見訓練動態曲線 Figure 1(a)），準確率更達 **$86.7\%$**，超越人類競賽選手平均水準。
* **推理長度（Test-Time Compute）隨訓練自發擴展與「頓悟時刻（Aha Moment）」**：在從未設定「回答越長分數越高」的前提下，模型為了提升困難題目的解題正確率，在 8,000 多個強化學習訓練步中自發將平均思考長度從數百 Token 推升至數千乃至上萬 Token（Figure 1(b)）；並在中間步驟觀測到模型突然中斷既有推導，寫出 *"Wait, wait. Wait. That's an aha moment I can flag here... Let's re-evaluate this step-by-step"*（Table 2），重新檢驗積分符號並改正錯誤。
* **DeepSeek-R1 全基準比肩 OpenAI o1-1217（64 次採樣共識評測）**：
  * 在正式基準評測中（原文 §D.1 與 Table 8），多數決共識評估一律採用 64 個樣本採樣（`cons@64`）。
  * **數學推理**：AIME 2024 達 **$79.8\%$**（Pass@1），64 次採樣多數決（`cons@64`）達 **$86.7\%$**（與 OpenAI o1-1217 持平），Pass@64 達 **$90.0\%$**；MATH-500（Pass@1）達 **$97.3\%$**（勝過 o1-1217 之 $96.4\%$）。
  * **程式競賽**：Codeforces 評分達 **$2,029$ Elo**，超越人類 **$96.3\%$** 的競賽程式設計師。
  * **科學與通用知識**：GPQA Diamond（Pass@1）達 $71.5\%$（o1-1217 為 $75.7\%$），MMLU 達 $90.8\%$。
* **蒸餾 vs. 小模型直接 RL 之決定性對比實驗**：將 DeepSeek-R1 生成的 80 萬筆推理軌跡直接監督微調給 Qwen-32B，所得 **DeepSeek-R1-Distill-Qwen-32B** 在 AIME 2024 達到 **$72.6\%$**（`cons@64` 達 $83.3\%$，MATH-500 達 $94.3\%$）；相比之下，若直接對 Qwen2.5-32B-Base 耗費龐大算力跑大規模純強化學習（Qwen2.5-32B-Zero），AIME 2024 僅能達到 $47.0\%$（`cons@64` 僅 $60.0\%$，見 Table 16）。這嚴格證明：**強大基座模型透過強化學習探索出的新推理模式，可透過蒸餾高效遷移，但小模型自身容量不足以獨立在 RL 中搜索出同等深度的推理策略。**

### 後續領域關鍵證據（非本篇成果，標註出處）
* **經同行評審刊登於《Nature》並引爆全球開源推理生態**：DeepSeek-R1 隨後於 2025 年正式通過同行評審發表於《Nature》，成為首篇公開完整強化學習動態與訓練配方的主流推理大模型論文；其提出的「GRPO ＋ 可驗證規則獎勵（RLVR, Reinforcement Learning with Verifiable Rewards）」迅速成為全球開源社群與各大實驗室訓練數學、程式碼與科學推理智能體（Reasoning Agents）的標準範式。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **開闢「測試時運算擴展定律（Test-Time / Post-Training Scaling Law）」新維度**：當預訓練參數規模與網際網路語料面臨邊際效益遞減時，DeepSeek-R1 證實將算力投入「後訓練強化學習（Post-Training RL）」與「推論時長思維鏈思考（Test-Time Compute）」，可解鎖全新的智慧增長曲線。
* **從「模仿人類過程」到「以真理驗證驅動演化」**：只要一個領域存在可靠的驗證器（Verifier）——如數學證明檢驗器 Lean、程式碼編譯器、物理模擬器或形式邏輯檢查器——AI 就能透過 GRPO 自我對弈與探索，突破人類既有解題套路的限制。
* **開源對閉源護城河的歷史性追平**：證明推理大模型並非少數科技巨頭憑藉神祕演算法壟斷的黑箱，透明簡潔的強化學習原則足以在開源生態中重現頂尖推理智慧。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
DeepSeek-R1-Zero 的「頓悟時刻（Aha Moment）」是人工智慧發展史上極具哲學意味的瞬間：

1. **「反思（Reflection）」並非人類專屬的高階模組，而是目標導向搜索的自然副產品**：當系統的唯一目標是「最終答案必須正確」，而計算資源允許它在給出最終答案前進行自由的內部獨白時，「自我懷疑、回溯檢查與換個角度重算」就會作為最大化期望回報的最優策略自發湧現。
2. **簡潔勝過繁複（Simplicity of GRPO + Rule Rewards）**：捨棄複雜的蒙地卡羅樹搜索、捨棄容易失真的神經過程獎勵模型、捨棄沉重的 Critic 價值網路，回歸最純粹的組內相對比較與真偽判準，反而讓強化學習首次在六千億參數規模上穩定釋放威力。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [生成式世界模型與擴展定律](../concepts/generative-world-models.md)
* **原始權威文獻**：
  * 官方期刊發表：DeepSeek-AI (Guo, D., Yang, D., Zhang, H., Song, J. et al., & Liang, W.) (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. Nature, 645(8081), 633-638. DOI: [10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z)
  * 原預印本：arXiv: [2501.12948](https://arxiv.org/abs/2501.12948)
  * 原始檔典藏：`raw/2025-deepseek-r1.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2025-deepseek-r1.md](../evidence/2025-deepseek-r1.md)
