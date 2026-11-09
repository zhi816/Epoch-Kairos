# 證據表：2026-data-centric-russian-kyrgyz-mt-novokshanov
- **採用版本**：*LoResMT 2026*, pp. 225–230 正式版，DOI: 10.18653/v1/2026.loresmt-1.22（ACL Anthology 2026.loresmt-1.22）；封存於 `raw/my-focus/英文論文/llm 輔助/Data-Centric Approach at the LoResMT 2026 Turkic Translation.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | DOI 更正為 `10.18653/v1/2026.loresmt-1.22` | 書目校正 | 首頁頁碼 pp. 225–230；ACL Anthology；Crossref | 符合來源（糾正原本之 `.25` 錯誤，關閉 EK-058） |
| Frontmatter | 作者 Dmitry Novokshanov（HSE University）；LoResMT 2026 pp. 225–230 | 本篇研究基本資訊 | 首頁標題與署名；Crossref | 符合來源 |
| Card 1 | LoResMT 2026 突厥語挑戰賽俄吉賽道第一名；官方測試集 49.1 chrF++ / 69.7 xCOMET-XXL | 競賽結果 | 摘要；§3.2, p. 228 | 符合來源 |
| Card 2 | 突厥語黏著構詞與資料雜訊；合成數據回譯毒化效應 | 本篇研究背景 | §1, §2.1, pp. 225–226 | 符合來源 |
| Card 3 | SONAR 評分為 `blaser_2.0` 跨語言語義相似度預測模型（1–5 分），門檻 3.0 與 3.7 | 系統方法校正 | §2.1.1, p. 226 | 符合來源（糾正餘弦相似度之錯誤表述，關閉 EK-085 (1)） |
| Card 3 | 四階段課程學習排程：標準 OPUS (8.2M) $\to$ 高品質 OPUS (7.1M) $\to$ FineWeb-2 回譯 (3.1M) $\to$ 合成對話 (113K) | 系統方法校正 | §2.3.3, pp. 227–228；表 1, p. 226 | 符合來源（糾正順序與資料集倒置錯誤，關閉 EK-085 (2)） |
| Card 3 | 烏茲別克語與塔吉克語輔助語言遷移；mt0-large 詞表剪枝至 800M | 系統方法補全 | §2.3.1–2.3.2, pp. 226–227；表 2 | 符合來源（補列原先漏述之核心架構，關閉 EK-085） |
| Card 4 | 表 1 各資料集統計數值 | 本篇研究數據 | 表 1, p. 226 | 符合來源 |
| Card 4 | 表 2 輔助語言消融結果（ru-ky 21.5 $\to$ +uz+tg 23.2 chrF++） | 本篇研究結果 | 表 2, p. 227 | 符合來源 |
| Card 4 | 表 3 基準模型對比（800M 模型以 44.9 chrF++ / 80.5 xCOMET 超越 54B NLLB 與 235B Qwen3） | 本篇研究結果 | 表 3, p. 228 | 符合來源 |
| Card 5 | 資料中心 AI 勝利；詞表剪枝與多語言預訓練結合 | 作者結論 | §4, p. 228 | 符合來源 |
| Card 6 | 對個人碩士論文南島語多語遷移、詞表剪枝與課程學習排程之映射與啟發 | Wiki 詮釋 | 頁面已標明 | 不適用 |
