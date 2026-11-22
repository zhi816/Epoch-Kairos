# 已結案問題：papers/2025-deepseek-r1.md

> 本檔收錄 [wiki/papers/2025-deepseek-r1.md](../../../papers/2025-deepseek-r1.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-037 | fixed | papers/2025-deepseek-r1.md | Card 4 | 原文不符
- **問題**：將 cons@64 標成 cons@16，並須註明所用論文版本。
- **來源**：[論文](https://arxiv.org/abs/2501.12948)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 arXiv:2501.12948 預印本 Table 1 與 Nature 2025 正式發表版本核實 Card 4：更正 AIME 2024 之 86.7% 數值為 64 次採樣多數決（cons@64），糾正誤植為「cons@16」之錯誤，並標明出自預印本 Table 1。證據表見 wiki/evidence/2025-deepseek-r1.md。

### EK-038 | fixed | papers/2025-deepseek-r1.md | Card 1 | 原文不符
- **問題**：把「完全不使用 SFT」同時套到 R1-Zero 與 R1；原文只有 R1-Zero 為純 RL，R1 使用冷啟動資料、RL、拒絕採樣與後續 SFT。
- **來源**：[封存原文](../../../../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照原文 §2.1 與 §2.3 核實修訂 Card 1：明確劃分僅 DeepSeek-R1-Zero 為完全不經 SFT 直接從 Base 模型以純 RL 訓練；正式版 DeepSeek-R1 為解決可讀性差與中英夾雜問題，採用包含冷啟動（數千筆長 CoT）、推理 RL、拒絕採樣及 80 萬筆混合 SFT、全場景二次 RL 的多階段管線，糾正將 Zero SFT 概括至 R1 之錯誤。證據表見 wiki/evidence/2025-deepseek-r1.md。

### EK-113 | fixed | papers/2025-deepseek-r1.md | Card 4 與證據表第 16 列 | 歸因／版本錯置
- **問題**：Card 4 第 85 行與證據表第 16 列稱 R1-Zero 之 AIME 2024 pass@1 由 15.6% 升至 71.0%，第 85 行並稱「與 OpenAI o1-0912 持平」；第 86 行稱「8,000 多個強化學習訓練步」。本頁引用之 Nature 版原文為 77.9%，訓練共 10,400 步（8.2k 步出現明顯躍升）。證據表同一列寫 10,400 步而論文頁寫 8,000，二者也不一致。71.0% 與 o1-0912 之比較疑為 arXiv 初版之數字，修正時須一併確認 cons@16 之 86.7% 是否為 Nature 版數字。
- **來源**：`raw/2025-deepseek-r1.pdf`，PDF 第 3 頁（10,400 steps；8.2k step）、第 4 頁（15.6% → 77.9%）。
- **發現於**：第一、二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。回原文核對：R1-Zero AIME 2024 pass@1 改為 15.6% → 77.9%（§2.3, p. 4），刪除與 o1-0912 之比較；訓練步數改為共 10,400 步、第 8.2k 步長度上限提高後躍升（§2.1, p. 3）；cons@16 之 86.7% 經確認為正式版數字（p. 5）。另刪除 Card 4「R1 之 cons@64 與 o1-1217 持平」（原文無此比較），Table 8 各數字逐一附上 o1-1217 對照值；章節 §2.2 改為 §2.3。證據表依正式版逐項重建，數字逐一寫出表列與欄位。

### EK-152 | fixed | papers/2025-deepseek-r1.md | hook、Card 1 至 Card 3 與 Card 6 | 過度表述
- **問題**：（1）`hook` 與 Card 1 稱 R1-Zero「首次公開證明」「首次向全球嚴格證明」，正式版原文未稱首次；Card 1 稱 R1「徹底解決」可讀性與中英夾雜、「追平 OpenAI o1 正式版」，原文 §6 仍列語言混雜為限制，Table 8 中 R1 與 o1-1217 互有高低；Card 1 與 Card 4 稱思考長度達「上萬 Token」，原文寫 hundreds to thousands。（2）Card 2 稱 PPO「使訓練顯存與通訊開銷翻倍」、Card 3 稱 GRPO「大幅省去一半顯存」，原文 Supplementary A.3 只說價值模型帶來顯著記憶體與運算負擔；Card 2 稱神經獎勵模型「導致訓練在中途崩潰」，原文只說易遭獎勵駭客利用。（3）Card 3 區塊公式：KL 估計量式末加了原文沒有之「≥ 0」並稱「恆為非負且低方差」；目標函數之期望寫法與原文式 (1) 不同；獎勵寫成 Wiki 自擬之 $r_i = R_{\text{acc}}(q, o_i) + R_{\text{fmt}}(o_i)$，原文為式 (4)。（4）Card 4 稱 Table 2 之頓悟時刻「重新檢驗積分符號」，原文例題為方程式求實根之和；Card 3 稱蒸餾「1.5B 至 70B」皆優於直接強化學習，原文只在 Qwen2.5-32B 上對照。（5）Card 6 稱強化學習「首次在六千億參數規模上穩定釋放威力」，無出處。（6）`title_zh` 冠以「推理運算擴展定律」，原文標題與內文均未提出此定律。
- **來源**：`raw/2025-deepseek-r1.pdf`（Nature 版全文與補充資料）：§2.1–2.3, pp. 3–5；§6, pp. 10–11；Supplementary A.3, pp. 14–16；Table 8, p. 41；Table 16, p. 61。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句；三條區塊公式改照原文式 (1)–(3) 並補式 (4)，刪去「≥ 0」；`title_zh` 與內文標題刪去「與推理運算擴展定律」。證據表逐式登記式號與頁碼。

### EK-153 | fixed | papers/2025-deepseek-r1.md | Card 4 後續與 Card 5 | 原文未支持
- **問題**：Card 4「後續領域關鍵證據」稱本篇刊於 Nature 後「成為首篇公開完整強化學習動態與訓練配方的主流推理大模型論文」、GRPO 加可驗證獎勵「迅速成為全球……標準範式」，無出處，且 Nature 刊登是本篇本身而非後續研究。Card 5 三點（「開闢測試時運算擴展定律新維度」「證實……解鎖全新的智慧增長曲線」「開源對閉源護城河的歷史性追平」）皆無出處。本篇發表於 2025 年，依 `wiki-content-audit` 須記載原文公開之資源、作者明列之限制與未來工作，頁面皆未記載。
- **來源**：頁面第 95、100–102 行；原文 §6, pp. 10–11（限制與未來方向）、Supplementary I, pp. 65–66（公開權重、蒸餾模型與程式）、Supplementary H.3, p. 65（原文自述啟發之後續探索）。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。刪去 Card 4 後續段與 Card 5 三點無出處之敘述；Card 5 改記原文公開之權重、蒸餾模型與程式，作者明列之能力限制、純強化學習之挑戰與未來方向，各附節與頁碼；註明原文自述之後續探索本頁未逐篇查核、不列為後續研究。證據表登記各列。
