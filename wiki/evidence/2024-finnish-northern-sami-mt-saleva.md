# 證據表：2024-finnish-northern-sami-mt-saleva
- **採用版本**：*Findings of ACL 2024*, pp. 12949–12956 正式版，DOI 10.18653/v1/2024.findings-acl.768（Crossref 核對書目相符）；封存於 `raw/my-focus/報告論文題材/2024.findings-acl.768.pdf`。
- **查核者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09；2026-11-10 增補（Claude Code by Anthropic，Claude Opus 5.5）：表 1、3、4、5 數值逐一列出，公式改照原文單豎線並登記位置，補列 Card 5 公開資源與未來方向（EK-170）

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 題名作 *Northern Sámi*；作者 Sälevä、Lignos | 本篇研究結果 | 首頁，p. 12949；Crossref | 符合來源 |
| Card 1 | 北薩米語約 25,000 名使用者 | 本篇研究結果 | §1, p. 12949 | 符合來源 |
| Card 1 | 四項貢獻；MADLAD-400 翻成北薩米語 1.92 BLEU | 本篇研究結果 | §1, p. 12949；表 1, p. 12950，「Finnish →Sámi」列「UiT Test」BLEU 欄 1.92（chrF 16.92；YLE Test BLEU 3.66） | 符合來源 |
| Card 2 | 平行語料 25,106 句；擴充至約 190 萬句；`<BT>` 防排擠 | 本篇研究結果 | 表 2, p. 12951；§3.1, p. 12950 | 符合來源 |
| Card 2 | UiT 域內（網頁、政治文本）、YLE 域外（新聞，151 句） | 本篇研究結果 | §4.1, p. 12951；§4.3, p. 12953 | 符合來源 |
| Card 2 | QLoRA 微調 MADLAD 仍低於 10 BLEU | 本篇研究結果 | 註 2, p. 12950 | 符合來源 |
| Card 3 | 反向模型加 RBMT 合成資料、兩組回譯；正譯 95 萬句芬蘭語 mC4 | 本篇研究結果 | §3.1, p. 12950 | 符合來源 |
| Card 3 | 區塊公式 $J(\theta) = -\log P_{\text{NMT}}(y \mid x) + \lambda D_{\text{KL}}(p_{\text{LM}}(y) \mid p_{\text{NMT}}(y \mid x))$（論文頁拆成兩行 aligned）；語言模型凍結 | 本篇研究結果 | §3.2, p. 12950，正文內嵌式、無式號；原文分隔符為單豎線 | 符合來源（2026-11-10 由雙豎線改照原文，EK-170） |
| Card 3 | Transformer-base 設定；SentencePiece 8,000／5,000 | 本篇研究結果 | §4.1, p. 12951 | 符合來源 |
| Card 4 | 芬蘭語→北薩米語 UiT 測試 BLEU／chrF：Baseline 26.86／58.60（Aulamo 欄 18.9）；Transformer-BT (RBMT) 37.22／67.89；Transformer-BT (combined) 41.75／70.12；Aulamo 欄最佳為 RNN-clean + RBMT 列 40.1 | 本篇研究結果 | 表 3, p. 12952，Finnish–Northern Sámi「UiT Test」BLEU、CHRF 欄 | 符合來源 |
| Card 4 | 芬蘭語→北薩米語 YLE 測試 BLEU／chrF：Baseline 8.43／35.67；Transformer-BT (RBMT) 16.34／47.46；Transformer-BT (combined) 14.96／45.93 | 本篇研究結果 | 表 4, p. 12952，Finnish–N. Sámi BLEU、CHRF 欄 | 符合來源 |
| Card 4 | 表 5（UiT Test 與 YLE Test 之 BLEU／CHRF）：Baseline + forward translation 25.93／59.52、9.01／36.99；Baseline + language model 31.26／62.99、8.60／37.41；Transformer-BT (combined) + tagging 41.71／70.33、19.20／48.60；+ forward translation 38.96／69.16、17.91／48.60；+ forward translation + tagging 38.84／69.10、17.36／48.19；+ language model 33.30／65.69、14.51／45.52 | 本篇研究結果 | 表 5, p. 12953 | 符合來源 |
| Card 4 | 比 Aulamo 最佳 40.1 高 1.65 | 本篇研究結果 | §4.2, p. 12951 | 符合來源 |
| Card 4 | 標記「有些情況有益、有些沒有」 | 作者解釋 | §4.3, p. 12952 | 符合來源 |
| Card 4 | 內文 33.80 與表 5 之 33.30 不一致 | 本篇研究結果 | §4.3, p. 12953；表 5 | 符合來源（原文內部不一致，頁面已註明） |
| Card 5 | 結論；回譯可能已提供足夠正則化 | 作者解釋 | §5；§4.3, p. 12953 | 符合來源 |
| Card 5 | 正譯域內有害、域外有益之解釋 | 作者解釋 | §4.3, p. 12953 | 符合來源 |
| Card 5 | 單一語言對、單次執行之限制 | 作者解釋 | Limitations, pp. 12953–12954 | 符合來源 |
| Card 5 | 全部程式與資料（含正譯與回譯輸出）公開於 GitHub `j0ma/sami-translation` | 本篇研究結果 | §1, p. 12949 | 符合來源（2026-11-10 補列，EK-170） |
| Card 5 | 方法能否推廣到其他語言為關鍵問題，因運算資源所限未能回答 | 作者解釋 | §5, p. 12953 | 符合來源（2026-11-10 補列，EK-170） |
| Card 5 | 推測調整超參數後語言模型先驗與正譯或可並用，初步實驗只見下降 | 作者解釋 | §4.3, p. 12953 | 符合來源（2026-11-10 補列，EK-170） |
| Card 6 | 臺灣南島語之延伸 | Wiki 詮釋 | 頁面已標明 | 不適用 |
