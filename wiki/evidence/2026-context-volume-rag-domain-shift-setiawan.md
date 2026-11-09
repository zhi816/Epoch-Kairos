# 證據表：2026-context-volume-rag-domain-shift-setiawan
- **採用版本**：*LoResMT 2026*, pp. 87–101 正式版，DOI: 10.18653/v1/2026.loresmt-1.7（ACL Anthology 2026.loresmt-1.7）；封存於 `raw/my-focus/英文論文/llm 輔助/Context Volume Drives Performance Tackling Domain Shift in Extremely.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 作者 David Samuel Setiawan、Raphaël Merx、Jey Han Lau；墨爾本大學；*LoResMT 2026* pp. 87–101 | 本篇研究基本資訊 | 首頁標題與署名；ACL Anthology | 符合來源 |
| Card 1 & Card 2 | 達豪語（Dhao）僅存新約數位資料；舊約 OOV 率達 25.9%（新約為 8.1%）；NMT 發生嚴重崩跌 | 本篇研究背景 | 摘要；§1, p. 87；Figure 5, p. 98 | 符合來源 |
| Card 2 | 微調加入語法書（NMT + Grammar）效能劣化（27.11 跌至 26.62 chrF++） | 本篇研究結果 | 表 1, p. 89；§5.1, p. 89 | 符合來源 |
| Card 3 | NMT 初譯草稿搭配 Gemini 2.5 Flash RAG 後編輯架構 | 本篇研究方法 | §4.1, pp. 88–89；Figure 1 | 符合來源 |
| Card 3 | 刪除虛構之對數線性擴展公式；澄清最優策略為基於 RapidFuzz 之詞級模糊匹配而非稠密向量 | 系統架構更正 | §4.3, p. 90；§5.2–5.3, pp. 90–93 | 符合來源（糾正公式與檢索器表述，關閉 EK-084） |
| Card 3 | 句級檢索（BM25、BGE、ChrF-RAG）在 $K \approx 60 \sim 80$ 飽和；詞級檢索在 $N=10$（eff. $K \approx 137$）達峰值 35.28 chrF++，後因語境雜訊回落至 35.16 與 34.22 | 本篇研究結果 | §5.2.1, p. 91；表 4–5, p. 100 | 符合來源（更正單調無限擴展之錯誤斷言，關閉 EK-084） |
| Card 3 | 詞典檢索隨容量單調線性增長，全量詞典（2,377 條）取得 31.32 chrF++ | 本篇研究結果 | §5.2.2, p. 91；表 6, p. 100 | 符合來源 |
| Card 4 | 表 1 基線數據（NMT NT 36.17 / OT 27.11；LLM 0-shot 18.84 等） | 本篇研究結果 | 表 1, p. 89 | 符合來源 |
| Card 4 | 表 2 核心成果：NMT Only 27.11 $\to$ 最終結合系統 35.21 chrF++（恢復 8.10 分） | 本篇研究結果 | 表 2, p. 91 | 符合來源 |
| Card 4 | 表 7 定性分析：修復重複迴圈、神之稱謂實體幻覺與親族成語 `matana` 重構 | 本篇研究分析 | §5.4, pp. 93–94；表 7, p. 101 | 符合來源 |
| Card 5 | 語境容量優先於演算法選擇；語法書留作 ICL 外部知識庫；LLM 作為安全網 | 作者結論與建議 | §5.5, p. 94 | 符合來源 |
| Card 6 | 對個人碩士論文南島語領域偏移、語法書定位與語境雜訊控制之映射與啟發 | Wiki 詮釋 | 頁面已標明 | 不適用 |
