# 證據表：2026-formosanmt-parallel-corpus-scheppat
- **採用版本**：*Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)*, pp. 3445–3455（ELRA 出版，2026 年 5 月），DOI: 10.63317/3ut33xim33nt；封存於 `raw/my-focus/英文論文/FormosanMT A Multilingual Parallel Corpus_2026.lrec-1.273.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | DOI 正確為 `https://doi.org/10.63317/3ut33xim33nt`（ELRA 出版） | 書目校正 | 論文集首頁、Crossref 與 ELRA 官方註冊資訊 | 符合來源（糾正先前誤用之 ACL DOI，關閉 EK-060） |
| Frontmatter | 標題、作者 Hunter Scheppat、Joshua K. Hartshorne、Sema Koc、Éric Le Ferrand、Emily Prud'hommeaux；*LREC 2026*, pp. 3445–3455 | 本篇研究基本資訊 | 首頁標題與署名；Crossref | 符合來源 |
| Card 1 & Card 4 | 語料庫總規模 493,519 句對：族語－華語 397,710 句對、族語－英語 95,809 句對 | 本篇研究核心數據 | §3.4, p. 3448；Table 2, p. 3449 | 符合來源 |
| Card 2 | 來源碎片化與多來源雜訊；田野筆記包含語言學家註記；NLLB 繁中分詞缺陷 | 本篇研究背景與動機 | §1, §3.3, §4.2, pp. 3445, 3448, 3450 | 符合來源 |
| Card 3 | 刪除虛構之語言識別器與神經語義對齊評分公式；說明清洗係採正則規則與長度比門檻 | 系統方法更正 | §3.3, pp. 3448–3449 | 符合來源（確認原文無 AlignScore 與 LangID，關閉 EK-080 (1)） |
| Card 3 | 長度比門檻：雙邊 $\ge 2$ 詞時，目標/來源詞比 $r \le 0.2$ 或 $r > 8.0$ 剔除；任一邊 $< 2$ 詞時，字元比 $r \le 0.05$ 或 $r > 20.0$ 剔除 | 本篇過濾管線 | §3.3, p. 3448 | 符合來源（關閉 EK-080 (1)） |
| Card 3 | 15 個 ISO 639-3 語言代碼列表：ami, bun, ckv, dru, pwn, pyu, ssf, sxr, szy, tao, tay, trv, tsu, xnb, xsy（含噶瑪蘭 ckv 與撒奇萊雅 szy；賽德克與太魯閣合併為 trv） | 語言學分類校正 | Table 1, p. 3447 | 符合來源（更正先前錯誤代碼並補齊 ckv 與 szy，關閉 EK-080 (2)） |
| Card 3 | 說明係針對各語言對分別訓練獨立之雙向雙語基準模型（15 個族語－華語模型、4 個族語－英語模型），而非 15 語聯合多語言預訓練（列為未來工作） | 系統架構更正 | §4.1–§4.2, §6, pp. 3449–3451, 3453 | 符合來源（糾正聯合微調描述，關閉 EK-080 (3)） |
| Card 3 | OpenNMT 採用 2-layer LSTM（Embedding 256, RNN 512, Adam 1e-3, Batch 2048）；NLLB-200 重構 tokenizer 註冊代碼、種子嵌入初始化、繁中分詞調適、動態雙向採樣（$p=0.5$） | 本篇模型架構 | §4.1–§4.2, pp. 3449–3451 | 符合來源 |
| Card 4 | 基準測試數據：NLLB-200 在絕大多數語言對顯著優於 OpenNMT；族語 $\to$ 華語 BLEU（卡那卡那富 26.90、布農 25.08、邵語 25.09）；華語 $\to$ 族語 chrF++（卡那卡那富 51.79、噶瑪蘭 48.88、邵語 47.28）；族語 $\to$ 英語 BLEU（布農 43.08、泰雅 41.02） | 本篇評測數據 | Table 3 & Table 4, p. 3451 | 符合來源 |
| Card 5 | 建立全球首個涵蓋全臺 15 種南島語之標準化 MT 基準與開源工程管線 | 作者結論 | §1, §5, pp. 3445–3446, 3451–3453 | 符合來源 |
| Card 6 | 校正語料總量為「49.3 萬句對（含 39.7 萬族語－華語句對）」，消除與 Card 4 之數據矛盾；映射至碩士論文構詞解析器聯動 | Wiki 詮釋與數據校正 | 頁面已標明；§3.4, p. 3448 | 符合來源（糾正先前「30 萬」之不一致描述，關閉 EK-080 (4)） |
