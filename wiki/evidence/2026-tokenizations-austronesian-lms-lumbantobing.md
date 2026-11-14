# 證據表：2026-tokenizations-austronesian-lms-lumbantobing

> 本表將 `wiki/papers/2026-tokenizations-austronesian-lms-lumbantobing.md` 與對應卡片中的公式、數據與強主張，逐條對應至第一手論文之頁碼、章節、公式編號與圖表。

- **第一手來源**：Andhika Bernard Lumbantobing and Hokky Situngkir (2026), *Tokenizations for Austronesian Language Models: study on languages in Indonesia Archipelago*, `arXiv:2602.06998v1`（Version: 2026-01-27，arXiv 上架日 2026-01-28；原始檔 `raw/my-focus/報告論文題材/2026-tokenizations-austronesian-lms-lumbantobing.pdf`）。
- **查核範圍**：全篇 12 頁正文與 3 組圖表（音節切分演算步驟式 (1)–(6)、KBBI 詞表建立、NusaX 12 語 TPC 與 Smith-Waterman 序列相似度評測、研究邊界與未來構想）。
- **查核者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen）

| 編號 | 頁面主張摘要 | 第一手來源 | 位置 | 原文依據與核對備忘 | 類型 |
|---|---|---|---|---|---|
| 1 | 本篇為預印本 `arXiv:2602.06998v1`（版本標記 2026-01-27，arXiv API 發表時間 2026-01-28），作者為 Andhika Bernard Lumbantobing 與 Hokky Situngkir | Lumbantobing & Situngkir (2026) | p. 1 頁首與側邊 arXiv 浮水印 | PDF 第 1 頁與 `export.arxiv.org/api/query?id_list=2602.06998` 完全一致。 | 本篇研究結果 |
| 2 | 南島語系涵蓋逾 1,200 種語言，原始南島語（PAn）詞根以雙音節 `CV(C)CVC` 音韻型態為主，並結合前綴、後綴、中綴與環綴等黏著構詞 | Lumbantobing & Situngkir (2026) | §2, p. 2 | 引據 Blust [3] 與 Kroeger [21] 說明雙音節詞根與黏著詞綴特徵，作為以音節為分詞單位之語言學動機。 | 本篇研究結果 |
| 3 | 模擬傳統印尼音素音節文字（*aksara* / *abugida*）的無母音標記（*virama*）回溯歸併 $\phi_{\mathrm{vir}}$ 與借詞複輔音前向併入 $\phi_{\mathrm{clus}}$ 規則 | Lumbantobing & Situngkir (2026) | §3, p. 6 式 (3)、(4)（區塊公式 1） | 式 (3) $\nu(u_i)=\varnothing \Rightarrow \kappa(u_{i-1})\leftarrow \kappa(u_{i-1})+\omega(u_i)$；式 (4) $\nu(u_i)=\varnothing \Rightarrow \omega(u_{i+1})\leftarrow \omega(u_i)+\omega(u_{i+1})$。 | 本篇研究結果 |
| 4 | 音節切分程序 $P$ 由線性掃描（處理雙字母輔音 $D$ 與介音 $M$）、*virama* 回溯與複輔音前向三階段合成：$P = (\phi_{\mathrm{clus}} \circ \phi_{\mathrm{vir}} \circ \phi_{\mathrm{scan}})$ | Lumbantobing & Situngkir (2026) | §3, p. 6 式 (5)（區塊公式 2；另見式 (1)–(2)） | $\phi_{\mathrm{scan}}: \Sigma^* \to T^*$ 先標記 $(\omega,\nu,\kappa)$，再依序經 $\phi_{\mathrm{vir}}$ 與 $\phi_{\mathrm{clus}}$ 完成閉音節與借詞調整。 | 本篇研究結果 |
| 5 | 基於音節詞表 $\Sigma$ 與未登錄音節字元退回映射 $f_\Sigma$ 之分詞映射：$\tau_\Sigma = (f_\Sigma \circ P)$ | Lumbantobing & Situngkir (2026) | §4.1, p. 7 式 (6)（區塊公式 3） | 無法納入高頻音節詞表 $\Sigma$ 的音節片段，由 $f_\Sigma$ 拆回單一字元並對應回 $\Sigma$ 內之基礎符號。 | 本篇研究結果 |
| 6 | 依印尼大辭典（KBBI）詞條建立音節詞表，音節出現頻率分佈服從冪律 $p(x)\sim x^{-\alpha}$（$\alpha\approx 1.87$，Zipf 等級斜率 $\beta\approx 1.14$）；實驗選定詞表大小為 `\lvert \Sigma \rvert = 2,843` tokens（對照組 GPT-2 BPE 詞表為 `50,257` tokens） | Lumbantobing & Situngkir (2026) | §4.1, p. 7 及 Fig. 1 | KBBI 音節詞表僅為 GPT-2 詞表大小的約十七分之一（`2,843 / 50,257 ≈ 5.66%` 屬依原文數據計算）。 | 本篇研究結果 |
| 7 | 評測資料採用 NusaX-MT 平行語料之全部 `1,000` 筆樣本（500 訓練 + 100 驗證 + 400 測試），涵蓋亞齊語、峇里語、班查語、多巴巴塔克語、布吉語、爪哇語、馬都拉語、米南佳保語、恩加朱語、巽他語共 10 種印尼地方語，以及印尼語與英語（合計 12 語） | Lumbantobing & Situngkir (2026) | Abstract p. 1；§4.2, pp. 7–8 及 Table 4 | 僅測試表層分詞特性（TPC 與序列比對），並未進行任何下游神經語言模型訓練或機器翻譯生成實驗。 | 本篇研究結果 |
| 8 | 每字元詞元數指標 $\mathrm{TPC}(S) = \frac{\lvert \tau_\Sigma(S) \rvert}{\lvert S \rvert}$，衡量相對於字串長度之分詞碎片化程度 | Lumbantobing & Situngkir (2026) | §4.3.1, p. 8 式 (7)（區塊公式 4） | 若跨語言缺少對齊音節而頻繁觸發字元退回，$\lvert \tau_\Sigma(S) \rvert$ 會升高並使 TPC 偏離印尼語基準。 | 本篇研究結果 |
| 9 | 以 Smith-Waterman 局部序列比對計算正規化詞元序列相似度 $\mathrm{sim}(S_1, S_2) = \frac{\max(H)}{2\times\sqrt{\lvert \tau_\Sigma(S_1) \rvert \lvert \tau_\Sigma(S_2) \rvert}}$，精確匹配 $+2$、錯配 $-1$、空位懲罰 $w_k = w_l = -1$ | Lumbantobing & Situngkir (2026) | §4.3.2, p. 9 式 (8)–(11)（區塊公式 5） | 藉幾何平均正規化消除句長差異，捕捉平行翻譯句對在同源詞與構詞詞綴上的局部保守片段。 | 本篇研究結果 |
| 10 | 音節式分詞在印尼語及全部 10 種地方語皆維持穩定的 TPC（`~0.4`），而英語因頻繁觸發字元退回導致 TPC 顯著攀升（超過 `0.6`）；GPT-2 則呈相反偏斜，英語 TPC 最低而地方語 TPC 相對偏高 | Lumbantobing & Situngkir (2026) | Abstract p. 1；§4.4, p. 10 Fig. 2 | 兩組小提琴圖紅藍標線明確顯示：音節法於所有印尼南島地方語集中於約 `0.4`（英語高於 `0.6`），GPT-2 英語最低且地方語分佈較高（約 `0.4` 上下）。 | 本篇研究結果 |
| 11 | 在跨語言平行句 Smith-Waterman 序列相似度比較上，音節式分詞與 GPT-2 的語言對相對秩序維持高度相關（Pearson $r = 0.9956$、Spearman $\rho = 0.9895$），且音節式分詞於所有地方語言對均取得更高相似度，迴歸斜率 $m \approx 1.21$（平均高出約 `21%`） | Lumbantobing & Situngkir (2026) | Abstract p. 1；§4.4, p. 11 Fig. 3 | Fig. 3a 散佈圖中全部區域語言對點皆位於對角線 $y=x$ 之上，趨勢線斜率 `1.21`。 | 本篇研究結果 |
| 12 | 相似度增益最顯著的語言對集中在馬來語支近親（Fig. 3b 差值熱圖：班查—米南佳保 `+0.062`、印尼—米南佳保 `+0.060`、班查—印尼 `+0.059`），以及爪哇—峇里—巽他語群內部 | Lumbantobing & Situngkir (2026) | §4.4, p. 11 Fig. 3b | 作者解釋其源於詞表取自印尼語 KBBI，加上同語族深層音韻結構共享。 | 本篇研究結果 |
| 13 | 作者定位本研究為基於詞表統計與音節邏輯的跨語分詞初步探索（稱為 ToBA-LM 路線），未來構想擴及泛南島語系並結合古文獻手稿影像字體識別 | Lumbantobing & Situngkir (2026) | §5, pp. 11–12 | 論文未實作端對端大語言模型下游微調、翻譯或詞幹切分基準比對，屬於表層分詞幾何與序列保守度驗證。 | 作者解釋 |
