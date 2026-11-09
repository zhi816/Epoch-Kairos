# 證據表：2025-tulun-adaptable-lrl-mt-merx
- **採用版本**：*ACL 2025 System Demonstrations*, pp. 129–139 正式版，DOI: 10.18653/v1/2025.acl-demo.13（ACL Anthology 2025.acl-demo.13）；封存於 `raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | DOI 更正為 `10.18653/v1/2025.acl-demo.13`（原誤記為 `acl-demos`） | 書目校正 | ACL Anthology 2025.acl-demo.13；Crossref | 符合來源（關閉 EK-057） |
| Frontmatter | 作者 Raphaël Merx、Hanna Suominen、Lois Hong、Nick Thieberger、Trevor Cohn、Ekaterina Vylomova；ACL 2025 pp. 129–139 | 本篇研究基本資訊 | 首頁標題與署名；Crossref | 符合來源 |
| Card 1 | 東帝汶德頓語與萬那杜比斯拉馬語醫療/救災專業領域翻譯 | 本篇研究背景 | 摘要；§1, pp. 129–130 | 符合來源 |
| Card 2 | 微調門檻高阻斷小型社群參與；純 NMT 術語失誤與通用 LLM 低資源語法弱 | 本篇研究動機 | §1–§2, pp. 129–130 | 符合來源 |
| Card 3 | 詞彙表動態檢索以 spaCy `en_core_web_sm` 斷詞後比對 `{1,2}`-gram 重疊 | 系統架構補全 | §3.2, p. 132 | 符合來源（補列具體實作，關閉 EK-083） |
| Card 3 | 翻譯記憶庫（TM）使用 `Tantivy` 函式庫執行 Top-$N$ BM25 檢索 | 系統架構補全 | §3.2, p. 132 | 符合來源（補列具體實作，關閉 EK-083） |
| Card 3 | 初譯支援 Google Translate API / Hugging Face Pipeline；後編輯採 LiteLLM 支援數百模型（實測 Gemini 2.0 Flash）並採 CoT Few-Shot 提示 | 系統架構補全 | §3.2, p. 132 | 符合來源（補列具體實作，關閉 EK-083） |
| Card 3 | 標明解碼公式為流程示意式（原文為系統工程展示論文，無理論優化公式） | 系統形式更正 | §3.1–§3.2 | 符合來源（關閉 EK-083） |
| Card 4 | Tetun（TDT）：MADLAD-400-10B 35.78→47.87（+12.09），OPUS-MT 16.01→34.27（+18.26）ChrF++ | 本篇研究數據 | §4.1.1, pp. 132–133；表 1 | 符合來源 |
| Card 4 | Bislama（BIS）：MADLAD-400-10B 15.22→47.94（+32.72），OPUS-MT 32.60→48.14（+15.54）ChrF++ | 本篇研究數據 | §4.1.1, pp. 132–133；表 1 | 符合來源 |
| Card 4 | Tetun 與 Bislama 的詞彙表／翻譯記憶規模及評估保留數：2,698／1,018／451 與 5,769／3,353／841 | 實驗資料 | §4.1.1, p. 132 | 符合來源 |
| Card 4 | 表 1 跨 TDT、BIS 的平均增益：+22.41 ChrF++（對 MADLAD）、+16.90 ChrF++（對 OPUS-MT）；表 1 僅列 ChrF++，不含 BLEU | 本篇研究數據與指標 | §4.1.1, p. 133；表 1 | 符合來源 |
| Card 4 | 系統可用性量表（SUS）得分 81.25；TAM 有用性滿分 5/5 | 使用者研究結果 | §4.1.2, p. 134；附錄 B | 符合來源 |
| Card 4 | FLORES-200 六語平均 41.09 chrF++（比 NLLB-54B 提高 +2.83）；Rundi 詞彙雜訊負影響與剔除詞彙後回升說明 | 本篇研究數據與分析 | §4.2, p. 134；表 2；§5, p. 135 | 符合來源 |
| Card 5 | 透明協同即時自適應；小模型保語法大模型做修訂 | 作者結論 | §6, p. 135 | 符合來源 |
| Card 6 | 對個人碩士論文南島語醫療長照模組、UI 協同審校與詞彙雜訊控制之映射與啟發 | Wiki 詮釋 | 頁面已標明 | 不適用 |
