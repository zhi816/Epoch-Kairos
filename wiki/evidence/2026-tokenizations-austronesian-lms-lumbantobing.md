# 證據表：2026-tokenizations-austronesian-lms-lumbantobing

> 本表將 `wiki/papers/2026-tokenizations-austronesian-lms-lumbantobing.md` 與對應卡片中的公式、數據與強主張，逐條對應至第一手論文之頁碼、章節、公式編號與圖表。

- **第一手來源**：Andhika Bernard Lumbantobing and Hokky Situngkir (2026), *Tokenizations for Austronesian Language Models: study on languages in Indonesia Archipelago*, `arXiv:2602.06998v1`（Version: 2026-01-27，arXiv 上架日 2026-01-28；原始檔 `raw/my-focus/報告論文題材/2026-tokenizations-austronesian-lms-lumbantobing.pdf`）。
- **查核範圍**：全篇 12 頁正文與 3 組圖表（音節切分演算步驟式 (1)–(6)、KBBI 詞表建立、NusaX 12 語 TPC 與 Smith-Waterman 序列相似度評測、研究邊界與未來構想）。
- **查核者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen）；2026-11-20 論文頁改為我的關注新六章，『位置』欄隨之改為新章節（DeepSeek Harness（DeepSeek V4.1 Flash））

| 編號 | 頁面主張摘要 | 第一手來源 | 位置 | 原文依據與核對備忘 | 類型 |
|---|---|---|---|---|---|
| 1 | 本篇為預印本 `arXiv:2602.06998v1`（版本標記 2026-01-27，arXiv API 發表時間 2026-01-28），作者為 Andhika Bernard Lumbantobing 與 Hokky Situngkir | Lumbantobing & Situngkir (2026) | 本頁範圍、Card 1 | PDF 第 1 頁與 `export.arxiv.org/api/query?id_list=2602.06998` 完全一致。 | 本篇研究結果 |
| 2 | 南島語系涵蓋逾 1,200 種語言，原始南島語（PAn）詞根以雙音節 `CV(C)CVC` 音韻型態為主，並結合前綴、後綴、中綴與環綴等黏著構詞 | Lumbantobing & Situngkir (2026) | Card 2、Card 6 延伸想法 | §2, p. 2，引據 Blust [3] 與 Kroeger [21] 說明雙音節詞根與黏著詞綴特徵，並稱 PAn 推定數千年前使用於臺灣地區。 | 本篇研究結果 |
| 3 | 模擬傳統印尼音素音節文字（*aksara* / *abugida*）的無母音標記（*virama*）回溯歸併 $\phi_{\mathrm{vir}}$ 與借詞複輔音前向併入 $\phi_{\mathrm{clus}}$ 規則 | Lumbantobing & Situngkir (2026) | Card 3 | §3, p. 6 式 (3)、(4)（區塊公式 1） | 本篇研究結果 |
| 4 | 音節切分程序 $P$ 由線性掃描（處理雙字母輔音 $D$ 與介音 $M$）、*virama* 回溯與複輔音前向三階段合成：$P = (\phi_{\mathrm{clus}} \circ \phi_{\mathrm{vir}} \circ \phi_{\mathrm{scan}})$ | Lumbantobing & Situngkir (2026) | Card 3 | §3, p. 6 式 (5)（區塊公式 2；另見式 (1)–(2)） | 本篇研究結果 |
| 5 | 基於音節詞表 $\Sigma$ 與未登錄音節字元退回映射 $f_\Sigma$ 之分詞映射：$\tau_\Sigma = (f_\Sigma \circ P)$ | Lumbantobing & Situngkir (2026) | Card 3 | §4.1, p. 7 式 (6)（區塊公式 3） | 本篇研究結果 |
| 6 | 依印尼大辭典（KBBI）詞條建立音節詞表，音節出現頻率分佈服從冪律 $p(x)\sim x^{-\alpha}$（$\alpha\approx 1.87$，Zipf 等級斜率 $\beta\approx 1.14$）；實驗選定詞表大小為 `\lvert \Sigma \rvert = 2,843` tokens（對照組 GPT-2 BPE 詞表為 `50,257` tokens） | Lumbantobing & Situngkir (2026) | Card 1、Card 3、Card 4 | §4.1, p. 7 及 Fig. 1 | 本篇研究結果 |
| 7 | 評測資料採用 NusaX-MT 平行語料之全部 `1,000` 筆樣本（500 訓練 + 100 驗證 + 400 測試），涵蓋亞齊語、峇里語、班查語、多巴巴塔克語、布吉語、爪哇語、馬都拉語、米南佳保語、恩加朱語、巽他語共 10 種印尼地方語，以及印尼語與英語（合計 12 語） | Lumbantobing & Situngkir (2026) | Card 1、Card 4 | Abstract p. 1；§4.2, pp. 7–8 及 Table 4。僅測試表層分詞特性（TPC 與序列比對），並未進行任何下游神經語言模型訓練或機器翻譯生成實驗。 | 本篇研究結果 |
| 8 | 每字元詞元數指標 $\mathrm{TPC}(S) = \frac{\lvert \tau_\Sigma(S) \rvert}{\lvert S \rvert}$，衡量相對於字串長度之分詞碎片化程度 | Lumbantobing & Situngkir (2026) | Card 4 | §4.3.1, p. 8 式 (7)（區塊公式 4） | 本篇研究結果 |
| 9 | 以 Smith-Waterman 局部序列比對計算正規化詞元序列相似度 $\mathrm{sim}(S_1, S_2) = \frac{\max(H)}{2\times\sqrt{\lvert \tau_\Sigma(S_1) \rvert \lvert \tau_\Sigma(S_2) \rvert}}$，精確匹配 $+2$、錯配 $-1$、空位懲罰 $w_k = w_l = -1$ | Lumbantobing & Situngkir (2026) | Card 4 | §4.3.2, p. 9 式 (8)–(11)（區塊公式 5） | 本篇研究結果 |
| 10 | 音節式分詞在印尼語及全部 10 種地方語皆維持穩定的 TPC（`~0.4`），而英語因頻繁觸發字元退回導致 TPC 顯著偏高（正文未給數值）；GPT-2 則呈相反偏斜，英語 TPC 最低而地方語 TPC 相對偏高 | Lumbantobing & Situngkir (2026) | Card 5、Card 6 | Abstract p. 1；§4.4, p. 10 Fig. 2 | 本篇研究結果 |
| 11 | TPC 約 `0.4` 反映南島語以 CV(C) 音節為主、每單位平均 2 至 3 個音素 | Lumbantobing & Situngkir (2026) | Card 4、Card 5 | §4.4, p. 10（"stable TPC values hovering around 0.4 … CV(C) syllabic patterns with an average length of 2 to 3 phonemes per unit"） | 本篇研究結果 |
| 12 | 在跨語言平行句 Smith-Waterman 序列相似度比較上，音節式分詞與 GPT-2 的語言對相對秩序維持高度相關（Pearson $r = 0.9956$、Spearman $\rho = 0.9895$），且音節式分詞於所有地方語言對均取得更高相似度，迴歸斜率 $m \approx 1.21$（平均高出約 `21%`） | Lumbantobing & Situngkir (2026) | Card 5 | Abstract p. 1；§4.4, p. 11 Fig. 3a | 本篇研究結果 |
| 13 | 相似度增益最顯著的語言對集中在馬來語支近親（Fig. 3b 差值熱圖：班查—米南佳保 `+0.062`、印尼—米南佳保 `+0.060`、印尼—班查 `+0.059`），以及爪哇—峇里—巽他語群內部 | Lumbantobing & Situngkir (2026) | Card 5 | §4.4, p. 11 Fig. 3b | 本篇研究結果 |
| 14 | 作者定位本研究為基於詞表統計與音節邏輯的跨語分詞初步探索（稱為 ToBA-LM 路線），未來構想擴及泛南島語系並結合古文獻手稿影像字體識別 | Lumbantobing & Situngkir (2026) | Card 6 | §5, pp. 11–12 | 論文未實作端對端大語言模型下游微調、翻譯或詞幹切分基準比對，屬於表層分詞幾何與序列保守度驗證。 | 作者解釋 |
| 15 | 作者自述此分詞法「對英語效果低」（low effectiveness for English），並把本研究定位為這條路線的初步一步 | Lumbantobing & Situngkir (2026) | Card 6 | §5, p. 12（"demonstrates low effectiveness for English"；"serves as an initial step"） | 作者解釋 |
| 16 | 原文未提及程式、詞表或資料是否公開，全文沒有資料可得性（Data Availability）一節，也沒有程式碼或資料集連結 | Lumbantobing & Situngkir (2026) | Card 1（速覽「公開」）、Card 6 | 全文 12 頁正文與致謝、參考文獻逐頁核對（p. 1–14 皆無公開聲明或連結） | 本篇研究結果 |
| 17 | 音節詞表規模約為 GPT-2 詞表的 5.66%（`2,843 / 50,257`） | Lumbantobing & Situngkir (2026) | Card 4 | §4.1, p. 7（兩詞表大小），比例為依原文數據計算 | 依原文數據計算 |
| 18 | 臺灣南島語與印尼南島語同屬南島語系，但書寫系統與語料條件不同，規則能否直接套用需逐語檢查 | 本頁 | Card 6 延伸想法 | Wiki 詮釋；原文僅述 PAn 推定源於臺灣地區（§2, p. 2），未討論臺灣族語 | Wiki 詮釋 |
| 19 | 由 Fig. 2 的軸刻度與均值標線判讀：音節分詞的英語 TPC 約 `0.63`，GPT-2 的英語 TPC 約 `0.2–0.25` | Lumbantobing & Situngkir (2026) | Card 5、Card 6 | §4.4, p. 10 Fig. 2；左圖英語列紅色均值線落在 0.6–0.7 之間、接近 0.63，右圖英語列均值線落在 0.2–0.3 之間偏左（約 0.23，論文頁寫「約 0.2–0.25」）。原文正文僅寫「顯著偏高」與「最低」，未給出小數，故本列為依圖判讀；卡片不放這兩個值，論文頁標明「依 Fig. 2 判讀」 | 依原文數據計算 |
