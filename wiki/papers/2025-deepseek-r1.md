---
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
title_zh: "DeepSeek-R1：以純強化學習激發大型語言模型之自我反思與長鏈推理湧現"
paper_year: 2025
award_year: 2025
timeline_year: 2025
authors: "Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi et al. (DeepSeek-AI)"
venue: "Nature, 645(8081), 633-638 (2025); and arXiv:2501.12948"
domain: "ai"
domain_tags: ["#人工智慧", "#強化學習", "#深度學習"]
concepts: ["generative-world-models"]
status: "published"
verification: "partial"
my_focus: false
doi_url: "https://doi.org/10.1038/s41586-025-09422-z"
key_papers:
  - "Shao, Z. et al. (2024) DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO). arXiv:2402.03300. https://arxiv.org/abs/2402.03300"
  - "DeepSeek-AI (Guo, D. et al.) (2025) DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. arXiv:2501.12948. https://arxiv.org/abs/2501.12948"
hook: "在基礎語言模型上僅憑基於規則的結果獎勵與群體相對策略優化（GRPO），以純強化學習（DeepSeek-R1-Zero）顯示長鏈推理、自我驗證與「頓悟時刻（Aha Moment）」無須人工示範即可在訓練中出現；再以冷啟動資料、多階段強化學習與監督微調訓練出 DeepSeek-R1，在多項推理基準上與 OpenAI o1-1217 互有高低，並把推理能力蒸餾給小模型。"
card_line: "以對錯獎勵訓練，讓語言模型學會逐步推理"
---

# DeepSeek-R1：以純強化學習激發大型語言模型之自我反思與長鏈推理湧現

> 「我們不需要手把手教導模型每一步該如何思考；只要給予明確的真偽判準與探索空間，強化學習便會讓模型在千萬次試錯中自發學會懷疑、回溯與頓悟。」

**2025 發表 ｜ 推理型大模型（Reasoning LLMs）與開源強化學習突破**

---

## Card 1 ｜ 時代銘文 (The Hook)
當預訓練階段的網際網路語料逐漸趨近枯竭，大型語言模型（LLMs）如何突破複雜數學證明、演算法競賽與科學推理的天花板？過去主流觀點認為，模型必須先依賴大量由人類專家撰寫的高品質「思維鏈（Chain-of-Thought, CoT）」示範數據進行監督式微調（SFT），或是搭配昂貴的過程獎勵模型（Process Reward Model, PRM）與蒙地卡羅樹搜索（MCTS）才能學會深度推理。2025 年 1 月，DeepSeek-AI 發表 **DeepSeek-R1-Zero** 與 **DeepSeek-R1**。其中 **DeepSeek-R1-Zero** 顯示：**在不使用任何監督微調（Zero SFT）作為前置步驟的情況下**，直接對基礎模型（DeepSeek-V3-Base）施加基於規則獎勵的大規模純強化學習（Pure RL），模型在訓練中逐漸產生數百至數千 Token 的長思維鏈、自我反思、驗證與「頓悟時刻（Aha Moment）」（§2.3, pp. 4–5）；而完整模型 **DeepSeek-R1** 則在此之上，導入數千筆冷啟動資料，結合多階段強化學習、拒絕採樣（Rejection Sampling）與約 80 萬筆監督資料之微調，改善純 RL 帶來的可讀性差與中英夾雜問題（作者仍將其他語言查詢之語言混雜列為限制，§6），在 AIME 2024、MATH-500、Codeforces 等基準上與 OpenAI o1-1217 互有高低（Table 8），並公開模型權重（Supplementary I）。

---

## Card 2 ｜ 世紀瓶頸：人類標註的天花板與 Critic 價值網路的記憶體高牆 (The Dilemma)
在邁向高階推理模型的道路上，學界曾面臨三大技術枷鎖：

* **人工監督微調（SFT）限制了探索上限**：人類標註的思維鏈不僅極度昂貴，且強行將模型束縛在「人類習慣的線性思考格式」內，阻止了模型透過試錯探索更高效、非人類直覺的推理路徑（正如 AlphaGo Zero 拋棄人類棋譜後方能超越 AlphaGo）。
* **傳統 PPO 強化學習的雙倍記憶體與算力負擔**：標準近端策略優化（PPO）以廣義優勢估計（GAE）計算優勢，須另外訓練一個價值評估網路（Value/Critic Model）；價值模型通常與策略模型（Policy Model，如 6,710 億參數）規模相近，帶來顯著的記憶體與運算負擔，且在只有最終結果獎勵、長思維鏈又會中途反思修改時，價值模型很難從部分回答預測最終獎勵（Supplementary A.3, pp. 14–15）。
* **神經過程獎勵模型（PRM）的獎勵駭客（Reward Hacking）陷阱**：若用另一個神經網路給推理結果或中間步驟打分，作者觀察到神經獎勵模型在大規模強化學習中容易遭到獎勵駭客利用，重新訓練獎勵模型又需大量算力並使訓練流程更複雜（§2.2, p. 4）。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
DeepSeek-R1 以下列設計避開上述問題：

1. **群體相對策略優化（Group Relative Policy Optimization, GRPO）**：
   * 徹底**廢除龐大的 Critic 價值模型**。針對每一個輸入問題 $q$，直接從舊策略 $\pi_{\theta_{\text{old}}}$ 中平行採樣一組共 $G$ 個回答 $\{o_1, o_2, \dots, o_G\}$，以這組回答獲得之獎勵分數的**組內平均值與標準差**直接計算每個回答的相對優勢（Advantage）$A_i$，免去另外訓練一個與策略模型規模相近之價值模型的記憶體與運算負擔（Supplementary A.3）。
2. **純規則決定性獎勵系統（Rule-Based Verifiable Rewards）**：
   * 在 DeepSeek-R1-Zero 與推理強化階段，不使用容易被駭客攻擊的神經獎勵模型，而是僅採用兩項完全客觀的規則獎勵：
     * **準確度獎勵（Accuracy Reward）**：數學題以確定性規則比對最終方框 `\boxed{}` 內答案是否正確；程式題直接送入編譯器跑真實測試用例（Test Cases）檢驗是否通過。
     * **格式獎勵（Format Reward）**：要求模型將思考過程置於 `<think>` 與 `</think>` 標籤之間（訓練範本另要求答案置於 `<answer>` 與 `</answer>` 之間，Table 1）。兩項獎勵等權相加（式 4，p. 4）。
3. **四階段管線（DeepSeek-R1）與能力蒸餾（Distillation）**：
   * 為解決純 RL 模型（R1-Zero）偶發的中英夾雜與可讀性問題，DeepSeek-R1 引入極少量（數千筆）高可讀性冷啟動長思維鏈資料，隨後執行「推理導向強化學習 $\to$ 拒絕採樣生成通用與推理混合 SFT 資料 $\to$ 全場景二次強化學習」四階段管線；並以 R1 產生之約 80 萬筆資料微調 1.5B 至 70B 的小模型（蒸餾）。在 Qwen2.5-32B 上之對照顯示，蒸餾 R1 明顯優於讓同一基座直接做大規模強化學習（Supplementary F.1, Table 16）。

### 1. 群體相對策略優化（GRPO）目標泛函 (GRPO Objective Function)

對每個問題 $q$，自舊策略 $\pi_{\theta_{old}}$ 採樣一組 $G$ 個輸出 $\{o_1, o_2, \cdots, o_G\}$，再以最大化下列目標函數更新策略模型 $\pi_\theta$（式 1，p. 3；Supplementary A.3 式 11 同）：

$$\begin{aligned}
\mathcal{J}_{GRPO}(\theta) = \mathbb{E}[q \sim P(Q), \{o_i\}_{i=1}^G \sim \pi_{\theta_{old}}(O|q)] \frac{1}{G} \sum_{i=1}^{G} \Bigg( &\min\left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \operatorname{clip}\left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)}, 1-\varepsilon, 1+\varepsilon \right) A_i \right) \\
&- \beta \mathbb{D}_{KL}\left(\pi_\theta || \pi_{ref}\right) \Bigg)
\end{aligned}$$

其中 $\pi_{ref}$ 為參考策略，$\varepsilon$ 與 $\beta$ 為超參數。訓練 R1-Zero 時 KL 係數為 0.001，每題取樣 16 個輸出，每 400 步把參考模型換成最新的策略模型（p. 3）。

### 2. 無價值網路之組內標準化優勢與無偏 KL 估計 (Group-Normalized Advantage & KL Estimator)

R1-Zero 之規則獎勵為準確度獎勵與格式獎勵等權相加（式 4，p. 4）：

$$Reward_{\text{rule}} = Reward_{\text{acc}} + Reward_{\text{format}}$$

每個輸出之獎勵記為 $r_i$，組內第 $i$ 個輸出的優勢 $A_i$ 以同組 $G$ 個獎勵之平均與標準差計算（式 3，p. 3）：

$$A_i = \frac{r_i - \operatorname{mean}(\{r_1, r_2, \cdots, r_G\})}{\operatorname{std}(\{r_1, r_2, \cdots, r_G\})}$$

KL 散度項採用 Schulman (2020) 之無偏估計量，直接加入損失，而非像 PPO 那樣在每個 Token 加入 KL 懲罰（式 2，p. 3；Supplementary A.3, p. 15）：

$$\begin{aligned} \mathbb{D}_{KL}\left(\pi_\theta || \pi_{ref}\right) &= \frac{\pi_{ref}(o_i|q)}{\pi_\theta(o_i|q)} - \log \frac{\pi_{ref}(o_i|q)}{\pi_\theta(o_i|q)} - 1 \end{aligned}$$

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（DeepSeek-AI 2025）之核心證據
（本頁數字一律取自 `doi_url` 指向之 Nature 版及其補充資料，即 `raw/2025-deepseek-r1.pdf`；arXiv 初版 2501.12948v1 之 R1-Zero 數字不同，不混用。）

* **DeepSeek-R1-Zero 純 RL 之 AIME 訓練軌跡與多數決**：在不給任何人工思維鏈範例的純強化學習過程中（§2.3 與 Figure 1(a)，p. 4），DeepSeek-R1-Zero 在美國數學邀請賽（AIME 2024）上的平均 pass@1 從初始的 **$15.6\%$** 升至 **$77.9\%$**；以自我一致性解碼（16 次採樣多數決，`cons@16`）可再提高到 **$86.7\%$**，明顯高於人類參賽者的平均成績（p. 5）。
* **訓練步數、推理長度與「頓悟時刻（Aha Moment）」**：R1-Zero 共訓練 10,400 步（約 1.6 個 epoch）；第 8.2k 步起把最大長度由 32,768 提高到 65,536 Token，表現與回答長度在該步都明顯躍升（§2.1, p. 3）。在沒有設定「越長越好」獎勵的情況下，平均思考長度隨訓練穩定增加，模型以數百至數千 Token 探索與修正解法（Figure 1(b)，p. 5）。中間版本出現擬人化的重新思考：*"Wait, wait. Wait. That's an aha moment I can flag here. Let's reevaluate this step-by-step to identify if the correct sum can be"*，隨後回頭逐步重做一道方程式求根之和的推導（Table 2，p. 5）；作者並以反思用字「wait」之使用量突然增加描述此現象（Supplementary C.2, Figure 9(b)）。
* **DeepSeek-R1 與 OpenAI o1-1217 之比較（Table 8，p. 41）**：
  * **數學推理**：AIME 2024 pass@1 為 **$79.8\%$**（o1-1217 為 $79.2\%$）；MATH-500 pass@1 為 **$97.3\%$**（o1-1217 為 $96.4\%$）。AIME 2024 之 64 次採樣多數決（`cons@64`）為 **$86.7\%$**、pass@64 為 **$90.0\%$**（Supplementary E.4, p. 60）。
  * **程式競賽**：Codeforces 評分 **$2,029$**（o1-1217 為 $2,061$），百分位 **$96.3\%$**（o1-1217 為 $96.6\%$），即勝過 96.3% 的人類參賽者（p. 42）。
  * **科學與通用知識**：GPQA Diamond pass@1 為 $71.5\%$（o1-1217 為 $75.7\%$），MMLU 為 $90.8\%$（o1-1217 為 $91.8\%$）。
  * pass@1 以非零溫度（0.6）取樣 $k$ 個回答之平均正確率計算，AIME 與 GPQA 之 $k = 64$（Supplementary D.1, pp. 40–41）。
* **蒸餾與小模型直接 RL 之對照（Supplementary F.1, Table 16, p. 61）**：以 R1 產生之約 80 萬筆資料微調 Qwen2.5-32B，所得 **DeepSeek-R1-Distill-Qwen-32B** 之 AIME 2024 pass@1 為 **$72.6\%$**（`cons@64` 為 $83.3\%$，MATH pass@1 為 $94.3\%$）；直接對 Qwen2.5-32B-Base 以數學、程式與 STEM 資料做超過 10K 步之大規模強化學習所得 Qwen2.5-32B-Zero，AIME 2024 pass@1 為 $47.0\%$（`cons@64` 為 $60.0\%$，MATH 為 $91.6\%$），與 QwQ-32B-Preview 相當。作者據此認為：把較強的模型蒸餾到小模型效果極佳，小模型若依賴大規模強化學習需要龐大算力，且未必達到蒸餾的表現；而要超越人類智慧的邊界，可能仍需更強的基座模型與更大規模的強化學習（p. 62）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
本篇發表於 2025 年，本頁尚未收錄逐篇查核之後續研究。原文自述其方法啟發了後續探索（Supplementary H.3, p. 65，引 Face 2025、Liu et al. 2025、Pan et al. 2025），本頁未逐篇查核，不列為後續研究。以下為原文記載之公開資源、限制與未來方向：

* **公開資源**：DeepSeek-R1 與 DeepSeek-R1-Zero 之模型權重公開於 HuggingFace，另公開六個蒸餾模型（DeepSeek-R1-Distill-Qwen-1.5B、7B、14B、32B 與 DeepSeek-R1-Distill-Llama-8B、70B），以及推論程式與使用說明（GitHub `deepseek-ai/DeepSeek-V3`、`deepseek-ai/DeepSeek-R1`）（Supplementary I, p. 65；§1, p. 2）。原文稱 SFT 與 RL 資料亦會公開，但所附網址為「xxx」，審查期間以附件提供（p. 66）。
* **作者明列之能力限制**（§6, pp. 10–11）：結構化輸出不如既有模型，且不能使用搜尋引擎、計算機等工具；簡單問題仍會過度思考，Token 效率有改進空間；主要針對中文與英文最佳化，處理其他語言查詢時可能語言混雜；對提示敏感，少樣本提示會降低表現；因評估耗時，大規模強化學習未廣泛用於軟體工程任務，相關基準進步有限。
* **純強化學習方法本身之挑戰**（§6, p. 11）：純強化學習依賴可靠的獎勵訊號；寫作等任務難以建構可靠的規則獎勵，若改由模型給獎勵，策略模型可能找到捷徑鑽漏洞，因此對無法以可靠獎勵模型評估之複雜任務，擴大純強化學習仍是開放問題。
* **作者所述之未來方向**（§6, p. 11）：下一版將處理結構化輸出與工具使用；軟體工程任務將以拒絕採樣或非同步評估提高效率；希望得到穩健的獎勵模型以處理難驗證的任務，並認為在推理過程中使用編譯器、搜尋引擎等工具很有前景。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
DeepSeek-R1-Zero 的「頓悟時刻（Aha Moment）」是人工智慧發展史上極具哲學意味的瞬間：

1. **「反思（Reflection）」並非人類專屬的高階模組，而是目標導向搜索的自然副產品**：當系統的唯一目標是「最終答案必須正確」，而計算資源允許它在給出最終答案前進行自由的內部獨白時，「自我懷疑、回溯檢查與換個角度重算」就會作為最大化期望回報的最優策略自發湧現。
2. **簡潔勝過繁複（Simplicity of GRPO + Rule Rewards）**：捨棄複雜的蒙地卡羅樹搜索、捨棄容易失真的神經過程獎勵模型、捨棄沉重的 Critic 價值網路，回歸組內相對比較與規則判準，反而讓強化學習在 6,710 億參數的模型上順利運作。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [生成式世界模型與擴展定律](../concepts/generative-world-models.md)
* **原始權威文獻**：
  * 官方期刊發表：DeepSeek-AI (Guo, D., Yang, D., Zhang, H., Song, J. et al., & Liang, W.) (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. Nature, 645(8081), 633-638. DOI: [10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z)
  * 原預印本：arXiv: [2501.12948](https://arxiv.org/abs/2501.12948)
  * 原始檔典藏：`raw/2025-deepseek-r1.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 證據表：[evidence/2025-deepseek-r1.md](../evidence/2025-deepseek-r1.md)
