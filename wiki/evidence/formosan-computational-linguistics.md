# 證據表：formosan-computational-linguistics
- **概念頁面**：[wiki/concepts/formosan-computational-linguistics.md](../concepts/formosan-computational-linguistics.md)
- **查核者**：Claude Code by Anthropic & Antigravity by Google DeepMind，2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | `papers` 移除閩南語論文 `2024-taiwanese-mt-resegmentation-tang` | 範圍校準 | 題名與語系分類（閩南語屬漢藏語系漢語族，非南島語） | 符合來源（關閉 EK-086 (1)） |
| 關鍵突破支柱 | 構詞解析流程以「已知詞根」為輸入，窮舉中後綴候選與機率模型判定 | 本篇研究方法綜述 | Lin et al. (2020); You (2021); Dai (2023); Wu (2025) 各篇碩論 | 符合來源（刪除逆向精確映射過度表述） |
| 關鍵突破支柱 | 楊鈞凱（2025）：由已知詞根集合以三種子字串匹配條件挑選候選詞根、檢查合法前後綴，再以 44 維成對特徵訓練隨機森林兩兩投票；書寫形式篩選曾測試但因過濾過多正解而未採用 | 本篇研究方法與結果 | 摘要 p. i；§3.2, pp. 29–32；§3.5, pp. 42–45 | 符合來源（修正候選詞正向窮舉描述，關閉 EK-086 (2)） |
| 關鍵突破支柱 | Gagnier（2026）採用詞級 TF-IDF 餘弦、頻率 $\ge 5$ Jaccard 相似度與前 500 高頻詞之正規化 Levenshtein 距離 | 本篇研究方法 | Gagnier (2026) §2.3, p. 125 | 符合來源（更正 MDS 與語義概念對齊，關閉 EK-086 (3)） |
| 關鍵突破支柱 | 謝富惠（2022）「說」動詞語法化；林鴻瑞（2024）時間詞實現/非實現對稱性 | 本篇研究成果 | Hsieh (2022); Lim (2024) 原文 | 符合來源 |
| 關鍵突破支柱 | FormosanMT（Scheppat et al. 2026）與 FormosanBench（Lin et al. 2025）語料基礎設施 | 本篇研究成果 | 各篇論文原文 | 符合來源 |
