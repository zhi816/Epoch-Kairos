# 證據表：2026-epark-formosan-dialectometry-gagnier
- **採用版本**：*DialRes 2026*, pp. 124–134 正式版，DOI: 10.63317/4scoopyavtvi（ELRA / ACL Anthology 2026.dialres-1.13）；封存於 `raw/my-focus/英文論文/Dialectometry and Evaluation of the ePark Corpus for_2026.dialres-1.13.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | DOI 更正為 `10.63317/4scoopyavtvi` | 書目校正 | 首頁頁碼 pp. 124–134；ELRA；Crossref | 符合來源（糾正未註冊之 `2026.dialres-1.13`，關閉 EK-059） |
| Frontmatter | 作者 Henry Gagnier（Pittsford Sutherland High School）；DialRes 2026 pp. 124–134 | 本篇研究基本資訊 | 首頁標題與署名；Crossref | 符合來源 |
| Card 1 | 分析 ePark 語料庫 16 族 42 種官方方言，總計 2,680,175 詞元、587 小時音檔 | 語料庫基本數據 | 摘要；§2.1, pp. 124–125 | 符合來源 |
| Card 2 | 歷史語言學分群爭議；ePark 高孤詞率（72%–79%）與六大板塊特徵 | 本篇研究背景 | §1, §3.1, pp. 124–126；表 1 | 符合來源 |
| Card 3 | 刪除虛構之概念對齊詞表與多維尺度分析（MDS） | 系統架構更正 | §2.3, p. 125 | 符合來源（關閉 EK-079） |
| Card 3 | 採用詞級 TF-IDF 餘弦（min_df=2, sublinear_tf=True）、頻率 $\ge 5$ 詞型 Jaccard 相似度，以及前 500 高頻詞之字元級正規化 Levenshtein 距離 | 本篇研究方法 | §2.3, p. 125 | 符合來源（補齊三項核心指標，關閉 EK-079） |
| Card 3 | Bootstrap 500 次放回抽樣（每次 10,000 詞元）計算 95% 信心區間 | 本篇研究方法 | §2.3, p. 125 | 符合來源 |
| Card 4 | 表 1 語料統計數值（各方言詞元、詞型、TTR、Hapax、核心共有詞、方言獨有詞） | 本篇研究數據 | 表 1, p. 127 | 符合來源 |
| Card 4 | 表 2 語群相似度（賽德克語餘弦 0.820 最密、排灣語 0.781 均質、泰雅語 0.605 與魯凱語 0.648 分化最深） | 本篇研究數據 | 表 2, p. 128 | 符合來源 |
| Card 4 | 重現布農語經典三分群（中群 0.774、北群 0.767、巒群南部分立） | 本篇研究發現 | §3.2, pp. 125–126 | 符合來源 |
| Card 4 | 表 3 板塊差異（詞彙篇 0.863 vs 文化篇 0.537 與閱讀書寫 0.537） | 本篇研究數據 | 表 3, p. 128 | 符合來源 |
| Card 5 | 首次客觀量化 ePark；指明核心詞比例決定跨方言模型遷移策略（Paiwan/Seediq 共享遷移 vs Atayal/Rukai 特化資源） | 作者結論 | §4, pp. 129–130 | 符合來源 |
| Card 1, Card 5 | 作者自述首次以語料計算方言相似度涵蓋全體臺灣南島語官方語言；多數語言結果與既有分群接近，排灣語無法判定、萬山魯凱語兩指標分歧 | 本篇研究結果 | 摘要，p. 124；排灣語，p. 128；§5，p. 130 | 符合來源（修正 EK-092，2026-11-09 Claude Code） |
| Card 6 | 對個人碩士論文泛泰雅語群遷移、權重矩陣與板塊偏差控制之映射與啟發 | Wiki 詮釋 | 頁面已標明 | 不適用 |
