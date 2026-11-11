# 證據表：1995-soai-asymmetric-autocatalysis

- **採用版本**：正式版，*Nature* 378(6559):767–768（1995-12-21 出版），https://doi.org/10.1038/378767a0；封存版本見 `raw/1995-soai-asymmetric-autocatalysis.pdf`（掃描版附文字層，數字與表格一律依 PDF 頁面影像逐項核對）。PDF 第 1 至 2 頁即印刷頁 767 至 768。
- **書目核對**：Crossref 之題名（Asymmetric autocatalysis and amplification of enantiomeric excess of a chiral molecule）、作者名單（Kenso Soai, Takanori Shibata, Hiroshi Morioka, Kaori Choji）、期刊、卷期頁與出版日期皆與原文首頁一致（2026-11-11 核對）。
- **獎項核對**：2026 年諾貝爾化學獎由 Henri B. Kagan 與 Kenso Soai 共享，表彰不對稱有機合成中非線性效應與自催化的發現（官方引文：「for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis」）。「分子同手性起源」為官方科普說明之概括，非表彰語原文。Kagan 並非本篇作者，故依規範於 Frontmatter 分立 `authors` 與 `laureates`。
- **查核者**：OpenCode by SST（MiniMax M3.1 Flash）完成 2026-11-11 源文逐列核對；DeepSeek Harness（DeepSeek-V4.1-Flash）撰寫區塊公式；2026-11-11 修正由 Claude Code by Anthropic（claude-haiku-5-5）統籌，依上述核對與 DSH 獨立審查結果更正頁碼、出處與判定。原表所載「由 Antigravity by Google DeepMind 審查核定」未有對應查核紀錄，已撤回。

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Card 1、hook | 作者實驗證明不對稱自催化可放大對映體過量（e.e.），產物對映體純度可顯著高於催化劑對映體純度（原文無「首次」用語，不作優先權主張） | 本篇研究結果 | 印刷頁 767 左欄摘要第 1 段；左欄末段 | 符合來源 |
| Card 1、Card 4、Card 6 | Series A 逐級放大：歷經 5 輪連續自催化反應（A1–A5），產物與催化劑混合物 e.e. 從 5% 放大至 39%、76%、85%、89%、89% (S)；Run A5 新生成物 e.e. 為 90% (S)，(S)-1 總量放大 1,674 倍 | 本篇研究結果 | 印刷頁 768 Table 1 Runs A1–A5（新生成物 90% 與 1,674 倍均見 Run A5 同一列）；p. 767 左欄第 3 段（Series A 起始 5% e.e. 之實驗描述與 20 mol% 條件）；942 與 1,674 倍之總結句見 p. 767 右欄首段（承左欄末段） | 符合來源；2026-11-11 回核 PDF 頁面影像，釐清 EK-216 |
| Card 1、Card 4 | Series B 極低起始：以 (S)-1 僅 2% e.e.（S : R = 51 : 49）啟動，歷經 5 輪連續自催化（B1–B5），產物混合物 e.e. 依序放大為 10%、57%、81%、88%、88% (S)，(S)-1 物質量放大 942 倍，新生成物純度達 88%–90% e.e. | 本篇研究結果 | 印刷頁 768 Table 1 Runs B1–B5（942 倍見 Run B5）；p. 767 左欄末段（2% e.e. 起始與「increased by the factor of 942 times」之文字塊） | 符合來源 |
| Card 2 | 先前不對稱自催化反應（refs 19–21）之產物 e.e. 始終低於催化劑 e.e.，手性訊息在複製中被稀釋而非放大 | 作者解釋 | 印刷頁 767 左欄第 2 段 | 符合來源 |
| Card 2 | Frank (1953) 提出「自催化 ＋ 相互抑制」理論方案（ref. 7），但長期缺乏化學反應實驗實例；當時唯一接近的實驗為 Kondepudi 等人（ref. 27）之自發結晶對稱破缺，屬物理而非化學過程 | 作者解釋 | 印刷頁 767 左欄第 1 段；p. 768 左欄末段 | 符合來源 |
| Card 3 區塊公式 1 | 對映體過量（e.e.）量化定義式：$\mathrm{e.e.} = \frac{|[S]-[R]|}{[S]+[R]} \times 100\%$ | Wiki 詮釋（標準定義，原文未印出） | 印刷頁 768 註解 § 計算例（原文未印出定義式，僅示範計算） | 符合（定義式為 Wiki 補充） |
| Card 3 區塊公式 2 | Frank (1953) 相互抑制手性自催化動力學方程：$\frac{\mathrm{d}[S]}{\mathrm{d}t} = k_{\mathrm{a}}[A][S] - k_{\mathrm{i}}[S][R]$，$\frac{\mathrm{d}[R]}{\mathrm{d}t} = k_{\mathrm{a}}[A][R] - k_{\mathrm{i}}[S][R]$（標準形式，作理論對照） | Wiki 詮釋 | 印刷頁 767 左欄第 1 段；p. 768 ref. 7 (Frank 1953) | 符合來源（原文僅文字描述，方程式為 Wiki 整理） |
| Card 3 區塊公式 3 | 原位生成之異丙基鋅烷氧基中間體 2 催化循環簡化反應式：$\mathrm{1} + \mathrm{i}\text{-}\mathrm{Pr}_2\mathrm{Zn} \rightarrow \mathrm{2} + \mathrm{i}\text{-}\mathrm{PrH}$；$\mathrm{3} + \mathrm{i}\text{-}\mathrm{Pr}_2\mathrm{Zn} \xrightarrow{\mathrm{2}} \mathrm{2}_{\mathrm{new}}$；$\mathrm{2}_{\mathrm{new}} + 2\,\mathrm{H^+} \rightarrow \mathrm{1}_{\mathrm{new}} + \mathrm{i}\text{-}\mathrm{PrH} + \mathrm{Zn^{2+}}$ | Wiki 詮釋（依 Fig. 2 改寫） | 印刷頁 767 Fig. 2 反應機理圖與正文 | 符合來源（改寫；步驟 3 已依質量與電荷守恒修正） |
| Card 3 區塊公式 4 | 二聚體平衡方程式：$\mathrm{(S)}\text{-}\mathrm{2} + \mathrm{(S)}\text{-}\mathrm{2} \rightleftharpoons \mathrm{(S)}\text{-}\mathrm{(S)}\text{-}\mathrm{2}_2$ ($K_{\mathrm{homo}}$)；$\mathrm{(S)}\text{-}\mathrm{2} + \mathrm{(R)}\text{-}\mathrm{2} \rightleftharpoons \mathrm{(S)}\text{-}\mathrm{(R)}\text{-}\mathrm{2}_2$ ($K_{\mathrm{hetero}}$) | 後續研究 | Blackmond et al. (2001), *JACS* 123:10103-10104 (doi:10.1021/ja0165133)（僅書目） | 書目符合（Crossref）；內容未核對 |
| Card 3 區塊公式 5 | 二聚體平衡常數定義式：$K_{\mathrm{homo}} = \frac{[\mathrm{(S)}\text{-}\mathrm{(S)}\text{-}\mathrm{2}_2]}{[\mathrm{(S)}\text{-}\mathrm{2}]^2}$；$K_{\mathrm{hetero}} = \frac{[\mathrm{(S)}\text{-}\mathrm{(R)}\text{-}\mathrm{2}_2]}{[\mathrm{(S)}\text{-}\mathrm{2}][\mathrm{(R)}\text{-}\mathrm{2}]}$ | 後續研究 | Blackmond et al. (2001), *JACS* 123:10103-10104 (doi:10.1021/ja0165133)（僅書目） | 書目符合（Crossref）；內容未核對 |
| Card 4 | Series A1 數據：起始 5% e.e. (S)-1，反應 74 h，產率 62%，混合物 e.e. 39% (S)；新生成物產率 42%、e.e. 55% (S)，(S)-1 放大 4.1 倍 | 本篇研究結果 | 印刷頁 768 Table 1 Run A1 | 符合來源 |
| Card 4 | Series B 詳細數據：B1（2% e.e. $\rightarrow$ 10% e.e., 2.5倍）、B2（10% e.e. $\rightarrow$ 57% e.e., 13倍）、B3（57% e.e. $\rightarrow$ 81% e.e., 61倍）、B4（81% e.e. $\rightarrow$ 88% e.e., 239倍）、B5（88% e.e. $\rightarrow$ 88% e.e., 942倍） | 本篇研究結果 | 印刷頁 768 Table 1 Runs B1–B5 | 符合來源 |
| Card 4 | Series C 鏡像對稱實驗：(R)-1 起始 10% e.e. 反應 70 h 得 53% e.e. (R)（新生成 67%）；(R)-1 起始 30% e.e. 反應 65 h 得 72% e.e. (R)（新生成 86%），證實催化劑組態決定產物組態 | 本篇研究結果 | 印刷頁 768 Table 1 Runs C1–C2；p. 767 右欄第 2 段 | 符合來源 |
| Card 4 | Run D 外消旋控制組：以外消旋 1（0% e.e.）催化反應 55 h，產率 68%，立體選擇性低於檢測極限（BDL） | 本篇研究結果 | 印刷頁 768 Table 1 Run D | 符合來源 |
| Card 4 後續 | Shibata et al. (1996), *JACS* 118:471-472 (doi:10.1021/ja953066g)：同嘧啶醇骨架高選擇性催化性自動增殖 | 後續研究 | JACS 118:471-472（僅書目） | 書目符合（Crossref）；內容未核對 |
| Card 4 後續 | Buono & Blackmond (2003), *JACS* 125:8978-8979 (doi:10.1021/ja034705n)：四聚體過渡態動力學證據 | 後續研究 | JACS 125:8978-8979（僅書目） | 書目符合（Crossref）；內容未核對 |
| Card 4 後續 | Kawasaki et al. (2009), *Science* 324:492-495 (doi:10.1126/science.1170322)：碳同位素 $^{13}\mathrm{C}/^{12}\mathrm{C}$ 觸發不對稱自催化手性放大（標題 “Triggered”） | 後續研究 | Science 324:492-495（僅書目） | 書目符合（Crossref）；內容未核對 |
| Card 4 後續 | Möhler et al. (2025), *Nature Communications* 16:7303 (doi:10.1038/s41467-025-62591-3)：吡啶基與嘧啶基受質動力學剖析更新 | 後續研究 | Nat. Commun. 16:7303（僅書目） | 書目符合（Crossref）；內容未核對 |
| Card 5、Card 6 | 本反應將「生命起源分子同手性之謎」轉化為實驗室可精確測量之化學動力學問題 | 作者解釋 | 印刷頁 767 左欄摘要第 1 段（“homochirality … remains a puzzle”） | 符合來源（出處已更正） |
| 限制 | 自催化詳細機構與動力學尚未完全闡明，是否存在抑制機制未知（原文 “remains to be clarified”）；全文未見 X-ray 單晶結構或完整速率常數（依 p.767–768 全文） | 作者解釋 | 印刷頁 768 右欄（“remains to be clarified”）；p. 767–768 全文（否定性陳述） | 符合來源（出處已更正） |
| Card 3、Card 4 | 不對稱自催化劑為含嘧啶基二級醇 2-methyl-1-(5-pyrimidyl)propan-1-ol（化合物 1），受質為嘧啶-5-甲醛（化合物 3） | 本篇研究結果 | 印刷頁 767 左欄第 2 段；Table 1 標題 | 符合來源 |
| Card 4「範圍」 | 催化劑 1 用量 20 mol%，摩爾比 3 : i-Pr₂Zn : 1 = 1 : 1.2 : 0.2；run B3 示範：1 31.7 mg（0.208 mmol，57% e.e.）於甲苯 49 ml，i-Pr₂Zn 1.2 mmol，0 °C 反應 96 h | 本篇研究結果 | 印刷頁 767 左欄（20 mol%）；印刷頁 768 註解 § 與 ＊（甲苯、0 °C、96 h） | 符合來源 |
| Card 3 中間體 2 表徵 | 中間體 2 為 1 與等莫耳二異丙基鋅原位反應生成之對掌性異丙基鋅烷氧化物，以 ¹H NMR（proton NMR）表徵 | 本篇研究結果 | 印刷頁 767 右欄第 3 段 | 符合來源 |
| Card 2、Card 3 | 作者僅稱本反應「可能」（It seems conceivable）為 Frank 方案之一例，並明示抑制機制是否存在仍待闡明 | 作者解釋 | 印刷頁 768 左欄末段至右欄 | 符合來源 |
| Card 3 §3 二聚體儲庫 | $K_{\mathrm{hetero}} > K_{\mathrm{homo}}$、$k_{\mathrm{cat}}^{\mathrm{homo}} > k_{\mathrm{cat}}^{\mathrm{hetero}}$、$\Delta G^{\circ} = -RT\ln K$ 與「儲庫」推論 | 後續研究 | Blackmond et al. (2001)，doi:10.1021/ja0165133（僅書目） | 書目符合（Crossref）；內容未核對；統計因子影響 $K$ 之直接比較，頁面已加註判讀界線（2026-11-11 修正 EK-212） |
