# 已結案問題：papers/2024-sora-world-simulator.md

> 本檔收錄 [wiki/papers/2024-sora-world-simulator.md](../../../papers/2024-sora-world-simulator.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-035 | fixed | papers/2024-sora-world-simulator.md | Card 3 | 原文未支持
- **問題**：把 VAE 具體架構、3D RoPE、adaLN-Zero 與 epsilon-prediction 當作 Sora 已知實作。OpenAI 報告未提供實作細節，並說模型訓練預測原始乾淨 patch，與 epsilon-MSE 公式不符；二手反向推測須明標推測。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 OpenAI 技術報告與 DiT、綜述原文核實修訂 Card 3：明確劃分 OpenAI 官方公開機制（時空壓縮網路、時空圖塊 Token 化、預測原始乾淨圖塊）與學界推測（adaLN-Zero 源自 Peebles & Xie 2023，3D-RoPE 與 3D-VAE 細節源自 Liu et al. 2024）；公式依官方報告明示更新為預測乾淨圖塊目標（$\hat{U}_0$），並對比經典 DiT 之 $\epsilon$ 預測目標。證據表見 wiki/evidence/2024-sora-world-simulator.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。OpenAI 報告未公開模型實作細節；Card 3 仍把 adaLN-Zero 與影片重標註並列為引導生成的機制，論文頁仍列圖塊映射、乾淨圖塊損失與 adaLN 區塊公式，卡片 Card 3 另列圖塊數量式，報告未提供這些公式。EK-099 原先所指的舊冪律式與運算量式已刪；其複核提出的現存公式缺口在此一併追蹤，修正時須同時核對論文頁與卡片。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。依 OpenAI 技術報告及 Liu 綜述圖 4 分開公開流程與逆向推測，移除未公開的圖塊數量、嵌入、損失與 adaLN 區塊公式；論文頁改以文字說明，卡片採無公式模式，證據表同步更正。DiT 的 adaLN-Zero 僅歸給 Peebles 與 Xie 的研究。

### EK-036 | fixed | papers/2024-sora-world-simulator.md | Card 1 | 過度表述
- **問題**：將遮擋後維持物體存在寫成一般穩定能力，報告措辭為「常能但並非總是」並明列物理模擬限制；即時互動與狀態記憶之說法亦超出原文示例。Card 5、6 之世界模型與隱式幾何重建描述應保留為有限能力觀察或詮釋。
- **來源**：同 EK-035
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。對照 OpenAI 官方報告修訂 Card 1、Card 4 與 Card 5：Card 1 將遮擋存在性精確限定為「常能（但並非總是）維持短暫被遮擋物體時空存在感」，並補列報告明示之物理交互局限；Card 4 刪除 Minecraft 具備即時互動與完備狀態記憶之表述，改為提示詞零樣本渲染動態畫面，並客觀補列玻璃碎裂與吃食物咬痕等物理失敗模式；Card 5 將世界模型描述限定為初步探索與有限能力湧現，強調高維視覺統計擬合與顯式因果物理引擎之本質差異。證據表見 wiki/evidence/2024-sora-world-simulator.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。Card 1 的限定語已補，但 Card 5 仍將隱藏層的三維幾何關聯寫成既定事實，Card 6 稱模型被迫反推世界幾何與物理規則；報告展示的是有限生成能力與失敗案例，未直接驗證這些內部機制。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。Card 5、6 改述報告展示的樣本及失敗案例，移除對隱藏層幾何與物理推理的未證實斷言；封面導言、hook 與證據表同步收斂。僅修正登記問題，論文頁 verification 改為 partial。

### EK-094 | fixed | papers/2024-sora-world-simulator.md | Card 4 | 原文不符
- **問題**：Card 4 第一點寫 DiT「在橫跨三個數量級的訓練算力區間內呈現單調緊密的負相關冪律（相關係數逾 $-0.95$）」。原文圖 8 為 12 種設定之「模型 Gflops」（單次前向運算量，0.3 至 118.6 Gflops）與 FID-50K 之相關，係數為 $-0.93$，並非訓練算力，亦未稱冪律。同點「ADM-U 的 3.94」在原文表 3 為 ADM-G、ADM-U 合用之 512 結果。
- **來源**：Peebles & Xie (2023), arXiv:2212.09748v2，圖 8（p. 8）、§4（p. 5）、§5（p. 8）、表 3（p. 9）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為模型 Gflops 與 FID-50K 相關係數 $-0.93$（圖 8，p. 8），256 由 LDM 之 3.60 降至 2.27、512 為 3.04（ADM-G、ADM-U 為 3.94），證據表增列。

### EK-095 | fixed | papers/2024-sora-world-simulator.md | Card 4 | 原文不符
- **問題**：Card 4 第二點寫「1×、4×、16×、32× 訓練算力對照」，並逐級描述「畫面模糊且物體結構瞬間崩解」「初具物體形狀但運動違反物理」「自發湧現逼真的流體力學波浪、光影反射……」。OpenAI 報告之影片標籤只有 Base compute、4x compute、32x compute 三組，文字僅寫「Sample quality improves markedly as training compute increases」；16× 與各級描述皆無出處。證據表原列「$1\times$ 至 $32\times$」亦判為符合。
- **來源**：Brooks et al. (2024), OpenAI 技術報告 §Scaling transformers for video generation（https://openai.com/index/video-generation-models-as-world-simulators/ ，2026-11-10 讀取頁面文字與影片標籤）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為基礎、4 倍、32 倍三組樣本與報告原句，註明只有影片樣本、無定量指標；證據表該列改判核實更正。

### EK-096 | fixed | papers/2024-sora-world-simulator.md | Card 4 | 過度表述
- **問題**：Card 4 第三點寫「對比實驗證明……頻繁出現人物無頭、主體出框」「主體完整居中率與電影級構圖品質顯著躍升」。原文為樣本之質性比較：方形裁切版本「sometimes generates videos where the subject is only partially in view」，Sora「have improved framing」；無「居中率」等量化指標。
- **來源**：OpenAI 報告 §Improved framing and composition；Liu et al. (2024), arXiv:2402.17177，圖 6 與正文，p. 7。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫為「後者有時生成主體只部分入鏡的畫面，Sora 的取景較佳」，註明為質性比較。

### EK-097 | fixed | papers/2024-sora-world-simulator.md | Card 4 後續 | 歸因／版本錯置
- **問題**：後續研究寫「Kang et al. (2024, *ICML*, ...)」，並稱其發現模型在「牛頓力學碰撞動量守恆、流體質量守恆與複雜剛體因果交互」上發生「穿模或憑空生成」。該文為 arXiv:2411.02385（2024 年 11 月），發表於 ICML 2025；摘要所述為二維物體運動與碰撞模擬之分布內、分布外與組合泛化測試，未提流體質量守恆或穿模。
- **來源**：arXiv:2411.02385 摘要與 comment 欄（「ICML 2025」），2026-11-10 以 arXiv API 讀取。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改寫出處為 arXiv 2024 年 11 月、ICML 2025，內容依摘要：分布內完美泛化、組合泛化隨規模改善、分布外失敗，模型模仿最相近案例，作者認為單靠擴大規模不足以發現物理定律。

### EK-098 | fixed | papers/2024-sora-world-simulator.md | Card 1 | 原文未支持
- **問題**：Card 1 寫「早期的影片生成模型（如初代 Runway Gen-2、Pika）大多只能生成 2 至 4 秒、固定正方形裁剪……」並稱 Sora 由 Peebles 與 Brooks「領軍開發」。OpenAI 報告原文為過去做法「typically resize, crop or trim videos to a standard size—e.g., 4 second videos at 256x256 resolution」，未點名任何產品；報告僅列作者，無「領軍」之述。
- **來源**：OpenAI 報告 §Variable durations, resolutions, aspect ratios；作者列（Tim Brooks, Bill Peebles, ...）。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。改依報告原文敘述過去做法與一分鐘影片，作者改寫為「Brooks, Peebles et al., 2024；Peebles 亦為 DiT 之第一作者」。

### EK-099 | fixed | papers/2024-sora-world-simulator.md | Card 3 | 原文未支持
- **問題**：Card 3 第 3 節稱「Peebles & Xie (2023) 與 OpenAI 實驗共同證實」生成品質「嚴格受……總訓練算力 $C$ 的冪律支配」，並列區塊公式 $\mathcal{L}_{\text{val}}(C) \propto C^{-\alpha}$ 與 $G \propto N \cdot d^2 + N^2 \cdot d$。DiT 原文只報告模型 Gflops 與 FID 之強負相關（圖 8），OpenAI 報告只有三組算力之樣本；兩者皆無此冪律或公式。
- **來源**：Peebles & Xie (2023) 圖 8，p. 8；OpenAI 報告 §Scaling transformers for video generation。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。第 3 節改題「算力與生成品質」，改寫為兩來源實際所述，刪除冪律公式與運算量估算式。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6；思考程度：max，依使用者指示）。回查 OpenAI 官方報告與目前頁面：報告明言未提供模型及實作細節；目前 Card 3 仍列 patch 數量式，論文頁仍列 patch embedding 及 clean-patch diffusion 目標式，報告未見這些公式。舊冪律與運算量式已刪，現存公式仍須移除或明確標為 Wiki 推導並補一手依據，因此重開為 open。
- **總核**：2026-11-10，Codex by OpenAI（GPT-6）。原問題的冪律與運算量式已移除，故本條維持 fixed；複核指出的其他公式確實仍須處理，已明確併入同頁的 EK-035，避免重複計數。依現行公式規範，非原文公式不可僅加註 Wiki 推導後仍保留為區塊公式；必要的推導須改以行內公式或文字呈現，並標明假設與依據。

### EK-100 | fixed | papers/2024-sora-world-simulator.md | Card 4 後續 | 未能核實
- **問題**：後續研究第一點列出快手 Kling、智譜 CogVideoX、騰訊 HunyuanVideo、阿里 Wan2.1 與 Meta Movie Gen，稱其遵循「3D-VAE ＋ 時空圖塊 ＋ DiT ＋ 3D-RoPE ＋ 流匹配」範式並「全面驗證時空 DiT 架構作為視覺基座模型的普適性」，未附任何出處。
- **來源**：Yang et al. (2024) arXiv:2408.06072；Polyak et al. (2024) arXiv:2410.13720；Kong et al. (2024) arXiv:2412.03603；Wan Team (2025) arXiv:2503.20314（arXiv 摘要）。快手 Kling 無公開技術報告。
- **發現於**：撰寫卡片文字檔時發現（Claude Code by Anthropic，第二批卡片回填 A 組，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。以 arXiv API 取得 CogVideoX、Movie Gen、HunyuanVideo、Wan 四份技術報告之摘要，改寫為各報告自述之設計並附 arXiv 編號；刪除無技術報告之 Kling，以及「遵循同一範式」「全面驗證」等原頁說法，註明不據此推論與 Sora 之承接關係。
