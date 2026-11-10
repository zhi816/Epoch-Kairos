# 證據表：2026-hybrid-dictionary-rag-llm-paiwan-wang
- **採用版本**：*Engineering Proceedings*, 120(1), 52, pp. 1–9（線上發表：2026-02-05；發表於 ICKII 2025 國際研討會），DOI: 10.3390/engproc2025120052；封存於 `raw/my-focus/英文論文/Hybrid Dictionary–Retrieval-Augmented Generation–Large Language Model for Low-Resource Translation _ engproc-120-00052.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 標題、作者 Reen-Cheng Wang、Cheng-Kai Yang、Tun-Chieh Yang、Yi-Xuan Tseng；國立臺東大學；*Eng. Proc.* 120(1), 52 | 本篇研究基本資訊 | 首頁標題與署名；Crossref | 符合來源 |
| Card 1 | 作者團隊與通訊作者 Reen-Cheng Wang（不列未見於首頁的教授職稱） | 書目校正 | 首頁署名與通訊作者註記 | 符合來源（修正 EK-081） |
| Card 1 & Card 2 | 極低資源排灣語（小於 10 萬句）通用 LLM 直接翻譯 BLEU 僅 1.7–4.4，幻覺頻繁 | 本篇研究背景與動機 | §1–§2, pp. 1–3；Figure 5 | 符合來源 |
| Card 3 | 刪除虛構之 BM25 結合語意餘弦相似度線性加權公式；說明原文無數學公式與 BM25 | 系統方法更正 | §3.1–§3.2, pp. 4–5；Figure 1–3 | 符合來源（確認原文無數學公式，關閉 EK-081 (2)） |
| Card 3 | 串聯條件分支（If-Else Fallback）：逐詞先查記憶體 JSON 雜湊表字典，命中則 Word Merge；未命中才查詢 Qdrant 向量庫 | 本篇核心管線 | §3.1–§3.2, pp. 4–5；Figure 3 (Data flow) | 符合來源（關閉 EK-081 (2)） |
| Card 3 | 說明詞典模組僅做表面詞字面匹配，未進行詞根與語素焦點解析 | 系統方法更正 | §3.1, p. 4；Figure 2 | 符合來源（關閉 EK-081 (2)） |
| Card 3 | 模組三 LLM（以 GPT-4o mini 為基準，另比較 Llama 3.1-70B、Gemma 3-27B、DeepSeek-R1-Distill-Llama-70B）接收初步翻譯與例句，進行語序重構與後編輯 | 本篇核心管線 | §3.2 與 §3.4, p. 5（模型名與節次修正 EK-110） | 符合來源 |
| Card 4 | 250 句測試集量化評估：Cosine 相似度由 0.210–0.236 升至 0.810–0.846（約 +0.60）；BLEU 由 1.7–4.4 暴升至 40.8–51.9（約 +40 至 +50）；ROUGE-L 由 0.135–0.177 升至 0.548–0.632（約 +0.45） | 本篇實驗結果 | §4, pp. 6–7；Figure 4, 5, 6 | 符合來源 |
| Card 4 | 系統局限性：高度依賴詞典覆蓋率；倒裝句與文化從屬子句難度較高 | 作者分析與局限 | §4–§5, pp. 7–8 | 符合來源 |
| Card 5 | 確立「符號詞典定錨 ＋ 向量檢索補缺 ＋ LLM 後編輯」輕量架構 | 作者結論 | §5, p. 8 | 符合來源 |
| Card 6 | 對個人碩士論文海大構詞解析器前置增強與條件分支 RAG 之映射與啟發 | Wiki 詮釋 | 頁面已標明 | 不適用 |
