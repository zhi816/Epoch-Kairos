# 已結案問題：concepts/generative-world-models.md

> 本檔收錄 [wiki/concepts/generative-world-models.md](../../../concepts/generative-world-models.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-045 | fixed | concepts/generative-world-models.md | 支柱與時間線 | 歸因／版本錯置
- **問題**：將 Hopfield/Hinton 能量模型合標為 1982（Boltzmann machine 學習論文為 Ackley、Hinton、Sejnowski 1985），並把 Hopfield、Boltzmann、score matching、擴散模型與 Transformer 寫成直接奠基鏈；須分開作者年代並改標為概念類比或補中間研究。
- **來源**：[Hopfield 封存原文](../../../../raw/1982-hopfield-network.pdf)、[Ackley et al. 1985](https://doi.org/10.1207/s15516709cog0901_7)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂生成式世界模型概念頁：分開標註 Hopfield (1982) 李亞普諾夫能量函數與 Ackley、Hinton、Sejnowski (1985) 波茲曼機學習演算法之年代；將擴散模型、分數匹配與 Transformer 注意力之聯繫明確界定為統計物理能量景觀與連續狀態空間之深層理論類比與現代聯想記憶等價性，刪除直接線性奠基之過度概括。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。Hopfield 與 Boltzmann 年代已拆開；目前支柱仍稱該概念視角啟發分數匹配等方法，現有兩篇來源不足以建立所述歷史因果鏈，應補直接承接證據或明確改為有限的概念類比。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。將 Hopfield（1982）與波茲曼機（1985）分開描述，刪去對分數匹配等方法的未證實歷史因果鏈，限定為概念類比；同步更新證據表。

### EK-046 | fixed | concepts/generative-world-models.md | DeepSeek-R1 段 | 歸因／版本錯置
- **問題**：將「無須人工示範」歸給 DeepSeek-R1（實為 R1-Zero），並把可驗證獎勵從原文之數學與程式任務推廣到任意驗證器與科學探索代理，應標為展望。
- **來源**：[DeepSeek-R1 封存原文](../../../../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂生成式世界模型概念頁 DeepSeek 段落：明確將「無須人工示範」限定於 R1-Zero 純 RL 模型，說明完整版 R1 結合冷啟動、多階段 SFT 與二次 RL，並將可驗證獎勵（RLVR）向任意領域驗證器與自主科學探索代理之推廣標明為重大未來展望。證據表見 wiki/evidence/2025-deepseek-r1.md。

### EK-056 | fixed | concepts/generative-world-models.md | Sora 段 | 過度表述
- **問題**：重述 Sora 能力界線問題（見 EK-036），把有限能力觀察寫成已證明之通用物理模擬。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂生成式世界模型概念頁 Sora 支柱：將其界定為「時空圖塊與視覺物理世界模擬初步探索」，明確指出純視覺擴散模型基於高維統計關聯擬合，在因果狀態改變與嚴格物理規律（如碰撞、破碎）時頻繁出現穿模與失真，指明其距通用物理世界模型之長期挑戰。

### EK-139 | fixed | concepts/generative-world-models.md | 關鍵突破支柱（DeepSeek-R1） | 過度表述
- **問題**：概念頁仍沿用論文頁已修正之說法：條目名「推理運算擴展定律」，並稱 R1-Zero「證明無須人工示範即可激發」長鏈推理與測試時算力擴展。論文頁已依 Nature 版改寫（EK-113、EK-152），`title_zh` 已刪「與推理運算擴展定律」，原文未稱證明。
- **來源**：`wiki/papers/2025-deepseek-r1.md` Card 1、Card 5（依 `raw/2025-deepseek-r1.pdf` 修正後）。
- **發現於**：第三批卡片回填 B 組回報，協調者核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依修正後論文頁改寫條目與連結文字，補作者所列限制；概念頁 `verification` 改為 partial。
