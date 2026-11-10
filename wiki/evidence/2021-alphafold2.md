# 證據表：2021-alphafold2
- **採用版本**：*Nature*, Vol. 596, No. 7873, pp. 583–589, August 2021；DOI: https://doi.org/10.1038/s41586-021-03819-2；封存版本見 `raw/2021-alphafold2.pdf`
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 作者 John Jumper, Demis Hassabis 等；2024 年諾貝爾化學獎共同得主（與 David Baker 共享） | 本篇研究結果 / 官方事實 | Nature 596 首頁；NobelPrize.org 官方通告 | 符合來源 |
| Card 1 | CASP14 主鏈誤差中位數 0.96 Å；結構預測取得進展 | 本篇研究結果 | 摘要與引言，pp. 583–584 | 評測結果不代表已解決所有蛋白質或其摺疊過程。 |
| Card 2 | Levinthal 構型爆炸與傳統共演化接觸圖缺乏 3D 幾何一致性之局限 | 作者解釋 / 背景 | pp. 583–584 | 符合來源 |
| Card 3 | Evoformer 雙軌注意力；三角形乘法與注意力受三角不等式啟發，非幾何硬性約束 | 本篇研究結果 | 主文 p. 586、Figure 3c | 對照主文對三角形更新之動機與適用範圍（EK-022）。 |
| Card 3 區塊公式 1 | 向外邊三角形乘法更新的 LayerNorm、投影、閘控與輸出 | 本篇研究結果 | [補充資料](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_MOESM1_ESM.pdf) Algorithm 11 第 1–4 行, p. 18 | 與 PDF 頁面逐項核對；原文的多個 Linear 為不同投影（EK-194）。 |
| Card 3 區塊公式 2 | 起始節點三角形注意力權重 | 本篇研究結果 | 補充資料 Algorithm 13 第 5 行, p. 19 | 與 PDF 頁面逐項核對；保留注意力頭索引與偏置（EK-194）。 |
| Card 3 區塊公式 3 | 起始節點三角形注意力的閘控輸出 | 本篇研究結果 | 補充資料 Algorithm 13 第 6 行, p. 19 | 與 PDF 頁面逐項核對；此式亦為卡片公式（EK-194）。 |
| Card 3 區塊公式 4 | IPA 各注意力頭權重及 $w_C$、$w_L$ | 本篇研究結果 | 補充資料 Algorithm 22 第 5–7 行, p. 28 | 與 PDF 頁面逐項核對；IPA 不變、座標更新等變（EK-022、EK-194）。 |
| Card 3 區塊公式 5 | FAPE 局部座標差、截斷平均與 $1/Z$ 長度正規化 | 本篇研究結果 | 補充資料 Algorithm 28 第 1–4 行, p. 34；§1.9.3 | 與 PDF 頁面逐項核對；原文設定 $Z=10\,\text{\AA}$、$d_{\text{clamp}}=10\,\text{\AA}$，FAPE 對反射不具不變性（EK-194）。 |
| Card 4 | CASP14 r.m.s.d.95 0.96 Å（亞軍 2.8 Å）；全原子 1.5 Å（亞軍 3.5 Å） | 本篇研究結果 | Figure 1, Figure 2，p. 584 | 符合來源 |
| Card 4 | pLDDT 與真實 lDDT-Cα 相關係數在近期 PDB 測試集為 r = 0.76（主論文 Figure 2c；伴篇 Tunyasuvunakool et al. 2021 報告為 r = 0.73） | 本篇研究結果 / 伴篇對照 | Figure 2c，p. 585（修正 EK-021） | 符合來源 |
| Card 4 | 消融實驗證實 IPA、三角形更新與 MSA 耦合缺一不可 | 本篇研究結果 | Extended Data Figure 5，p. 588 | 符合來源 |
| Card 4、卡片 Card 5 | AlphaFold DB 初版逾 36 萬預測；2022 年 7 月擴充至逾兩億 | 後續研究 | [Varadi et al. (2022)](https://doi.org/10.1093/nar/gkab1061) 摘要；[EMBL-EBI 2022 年 7 月公告](https://www.ebi.ac.uk/about/news/technology-and-innovation/alphafold-200-million/) | 初版論文與後續擴充分開歸屬；不把兩億當作初版論文已報告的數量（EK-195）。 |
| Card 4 | AlphaFold-Multimer、RFdiffusion（2023） | 後續研究 | 論文頁所列 Evans et al. (2021)、Watson et al. (2023) | 後續研究，非本篇成果。 |
| Card 5 | 核孔複合體的整合建模 | 後續研究 | [Fontana et al. (2022)](https://doi.org/10.1126/science.abm9326)；[Mosalaganti et al. (2022)](https://doi.org/10.1126/science.abm9506) 摘要 | Fontana 等研究非洲爪蟾細胞質環；Mosalaganti 等的模型覆蓋超過 90% 的人類核孔骨架。兩者均結合預測與實驗資訊，不能混為同一完整核孔模型（EK-023）。 |
| Card 6 | 自然選擇作為訓練集、對稱性先驗之跨界啟發 | Wiki 詮釋 | 哲學反思，無事實爭議 | 不適用 |
