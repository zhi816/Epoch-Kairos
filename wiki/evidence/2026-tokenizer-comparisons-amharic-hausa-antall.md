# 證據表：2026-tokenizer-comparisons-amharic-hausa-antall

> 本表將 `wiki/papers/2026-tokenizer-comparisons-amharic-hausa-antall.md` 與對應卡片中的公式、數據與強主張，逐條對應至第一手論文之頁碼、章節、公式編號與圖表。

- **採用版本**：Antall 與 Saha (2026), *What Do Tokenizer Comparisons Measure? Disentangling Granularity, Root Assignment, and Word-Level Readout across Amharic and Hausa*, arXiv:2611.14818v1（2026-11-10 投稿；官方頁 https://arxiv.org/abs/2611.14818 ；PDF 共 19 頁、6 圖、7 表；原始檔 `raw/my-focus/每日推介/2026-tokenizer-comparisons-amharic-hausa.pdf`）。PDF 首頁側邊標「arXiv:2611.14818v1 [cs.CL] 10 Nov 2026」；全文無期刊卷期與期刊 DOI，arXiv 頁列 arXiv-issued DOI（DataCite pending registration），故書目以 arXiv 官方頁與 PDF 首頁為準。
- **查核範圍**：全文 19 頁，含摘要、§1 至 §5、Limitations、附錄 A 至 F 與 Table 1 至 7；數字與公式另以 PyMuPDF 將 PDF 原頁轉為影像逐頁核對（核對頁：1、3、4、5、6、7、8、9、16、17、18、19）。
- **查核者**：Hy4 Flash（Command Code），2026-11-21。

| 編號 | 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|---|
| 1 | 本頁範圍、Card 1 速覽 | 作者為 Abdul Rehman Antall（FAST-NUCES, Lahore）與 Baidya Nath Saha（Concordia University of Edmonton）；2026 年 arXiv 預印本，19 頁、6 圖、7 表 | 本篇研究結果 | PDF p. 1 標題頁與作者、機構；arXiv 官方 abs 頁 Submitted on 10 Nov 2026、Comments「19 pages, 6 figures, 7 tables」 | 符合來源 |
| 2 | Card 1、Card 2 | 論文把形態感知分詞器相對 BPE 的增益拆成三因子：切分粒度、詞根指派、詞級讀出 | 本篇研究結果 | Abstract p. 1；§1 p. 2；§3 p. 3 | 符合來源 |
| 3 | Card 2 | 吉茲字母（Ge'ez abugida）把輔音與元音熔在同一字形，同詞根的不同詞形不共享可見字串，任何字元子串分詞器都無法直接取出詞根 | 本篇研究結果 | §1 p. 1（√s-b-r 的詞形舉例）；Appendix B, Theorem 1, p. 13 | 符合來源 |
| 4 | Card 3 區塊公式 1 | 總效果分解式：S(T) − S(B) = S(T°) − S(B) + S(T) − S(T°)，前項為粒度、後項為詞根指派 | 本篇研究結果 | §3.1, p. 3, 式 (1) | 符合來源 |
| 5 | Card 2 | 只訓練 BPE 與形態分詞器兩個條件時，觀察到兩個分數，任何粒度／詞根拆分都與之相容，故兩條件比較不能歸因 | 本篇研究結果 | §3.1, p. 3；Appendix A, Proposition 1, p. 12 | 符合來源 |
| 6 | Card 3 | 打亂與置換對照只替換詞根記號，保留前綴、模板、後綴、詞表、每詞詞元數、 fertility、參數量與詞元位置 | 本篇研究結果 | §3.2, pp. 3–4；Appendix A, Proposition 2, p. 12 | 符合來源 |
| 7 | Card 3、Card 4 | 粒度掃描以五種 BPE 詞表大小取約 1.0、1.3、1.6、2.0、2.3–2.4 倍基準 fertility；實際掃描範圍阿姆哈拉語 1.00–2.42、豪薩語 1.00–2.27 | 本篇研究結果 | §3.3, p. 4；§4.1, p. 5 | 符合來源 |
| 8 | Card 3 區塊公式 2 | 讀出污染式：Δread = Γ(T) − Γ(B)，其中 Γ(X) = S_pool(X) − S_first(X) | 本篇研究結果 | §3.4, p. 4, 式 (2) | 符合來源 |
| 9 | Card 2 | 作者以片段偏移與雜訊模型推導首詞元與平均池化讀出的均方誤差差，預測：片段無偏時池化較佳、首詞元已代表整詞時池化較差、強上下文化時讀出差異很小 | 作者解釋 | §3.4, p. 4, 式 (3) 與其後三段；Appendix A, Proposition 3, p. 13 | 符合來源 |
| 10 | Card 3 | ROOTPAT 把可分析詞切成至多四個記號（前綴、詞根、模板、後綴），無分析者走子詞加位元組退回；因式分解在同音正規化下無損 | 本篇研究結果 | §3.5, p. 4；Appendix B, Theorem 2, p. 13 | 符合來源 |
| 11 | Card 4 | NER 用 MasakhaNER 1.0 新聞資料，九種 BIO 標籤；阿姆哈拉語 1,750/250/500 句、豪薩語 1,912/276/552 句（訓練／開發／測試） | 本篇研究結果 | §4.1, p. 5,「Data」段 | 符合來源 |
| 12 | Card 4 | 翻譯用過濾後 OPUS-100，English→阿姆哈拉語與 English→豪薩語各 20,000/1,000/1,000 對；語域中宗教文本佔 44% 與 43% | 本篇研究結果 | §4.1, p. 5,「Data」段 | 符合來源 |
| 13 | Card 4 | 詞形表單來自 UniMorph 的 2,461 個阿姆哈拉語詞條（lemmas），分析器 HornMorpho 僅用於 Study I；豪薩語沒有詞根資源，故無詞根對照組 | 本篇研究結果 | §4.1, p. 5,「Data」段；Table 4, p. 18 | 符合來源 |
| 14 | Card 4 | Study I 阿姆哈拉語 BPE 與 unigram 的 fertility 為 1.62 與 1.89；三個 ROOTPAT 組 fertility 2.82–2.90、詞表 5,387 對 5,388；誘導詞根 1,608、詞典詞根 1,703、分析器覆蓋 80.4%；同 fertility BPE 對照之詞表為 600 | 本篇研究結果 | §4.1, p. 5,「Tokenizer arms」段 | 符合來源 |
| 15 | Card 4 | Study II 只用詞形典誘導 1,238 個詞根，覆蓋 67.2% NER 詞型；ROOTPAT fertility 降至 2.17、BPE 為 1.53；NER 模型 1.95M 參數；兩個預訓練編碼器為 XLM-R base 與 AfroXLM-R base，其分詞器 fertility 2.20，各三 seeds | 本篇研究結果 | §4.1, p. 5,「Study II」段 | 符合來源 |
| 16 | Card 4 | 顯著性採 2,000 次句子層配對 bootstrap、Holm 校正；等價 margin 預先訂為 F1 的 1 與 2 點、chrF++ 的 0.5 點 | 本篇研究結果 | §3.6, p. 5 | 符合來源 |
| 17 | Card 5 | Study I 分析器組池化讀出比 BPE 高 +9.11 F1；打亂對照重現 +4.25（47%），真詞根再添 +4.86 [3.14, 6.69]（pHolm < 10^−4） | 本篇研究結果 | §4.2, p. 5；Fig. 2a, p. 6；Table 5, p. 19 | 符合來源 |
| 18 | Card 5 | Study I 分析及詞典對照對 fertility 匹配 BPE 的詞根貢獻 +3.50；無分析器之誘導組取得分析器組增益的 77.6%，F1 為 23.81 對 25.85，基準 16.74 | 本篇研究結果 | §4.2, pp. 5–6；Fig. 2a, p. 6；Table 5, p. 19 | 符合來源 |
| 19 | Card 5 | Study II 真詞根減打亂詞根 +4.65 [3.01, 6.33]，五個 seeds 全為正（pseed = 0.011）；真詞根減 BPE 的總差 +1.25 為 inconclusive（pHolm = 0.15） | 本篇研究結果 | §4.2, p. 6；Fig. 2b, p. 6；Table 6, p. 19 | 符合來源 |
| 20 | Card 5 | Study II 對置換對照的 +2.92 與 +5.21 在句子層顯著（pHolm = 0.006），但各有一個 seed 為負（pseed = 0.16 與 0.055）；剔除高分的 29.4 seed 後，真詞根對打亂仍為 +3.68（pseed = 0.003），對置換降為 +1.73 與 +3.59 | 本篇研究結果 | §4.2, p. 6；Fig. 2b, p. 6；附錄 F.2 per-seed 分數 p. 18 | 符合來源 |
| 21 | Card 5 | 詞頻結構可解釋的部分：分層置換減打亂 −0.56 [−2.09, 0.99] 在 2 點 margin 下等價於零；普通置換減打亂 +1.73 [0.19, 3.32] 為 inconclusive（pHolm = 0.070） | 本篇研究結果 | §4.2, p. 6；Table 6, p. 19 | 符合來源 |
| 22 | Card 5 | Study I 中首詞元讀出下所有 ROOTPAT 組看似比 BPE 差（−0.47 至 −2.50，校正後皆不顯著）；池化讀出下全部顯著較佳（+7.07 至 +9.11，pHolm ≤ 0.006） | 本篇研究結果 | §4.3, p. 6；Fig. 3a, p. 7；Table 5, p. 19 | 符合來源 |
| 23 | Card 5 | Study I 阿姆哈拉語 BPE 首詞元 F1 14.73 ± 1.18、池化 16.74 ± 1.49，Γ = +2.01 [1.02, 3.03]；unigram 首詞元 15.43 ± 0.94、池化 19.36 ± 1.39，Γ = +3.93 [2.24, 5.63] | 本篇研究結果 | Table 5, p. 19，bpe 與 unigram 列 | 符合來源 |
| 24 | Card 5 | Study I 阿姆哈拉語分析器組首詞元 F1 12.47 ± 0.58、池化 25.85 ± 1.94，Γ = +13.38 [10.74, 16.08]；誘導組 12.24 ± 1.42 與 23.81 ± 0.49，Γ = +11.57；詞典組 14.26 ± 1.79 與 25.49 ± 1.12，Γ = +11.23 | 本篇研究結果 | Table 5, p. 19，analyser、induced、lexicon 列 | 符合來源 |
| 25 | Card 5 | 分析器組與 BPE 比較中，讀出造成的污染 Γ(T) − Γ(B) 為 +11.4 F1，大於比較本身 | 依原文數據計算 | §4.3, p. 6（由 Table 5, p. 19 之 +13.38 與 +2.01 相減，原文亦寫 +11.4） | 符合來源 |
| 26 | Card 5 | 豪薩語 BPE fertility 1.19 時兩種讀出幾乎無差（−0.10，不顯著）；較細的 fertility 匹配 BPE 與 unigram 在池化下反而變差（−2.98，pHolm = 0.009；−4.11）；F1 首詞元／池化為 BPE 48.01/47.90、unigram 48.04/43.93、fertility 匹配 BPE 42.11/39.13 | 本篇研究結果 | §4.3, p. 6；Appendix F.1, p. 17 | 符合來源 |
| 27 | Card 5 | Study II 所有從頭模型讀出增益皆正（+2.7 至 +4.7 F1），但未重現隨 fertility 增長：在 0.64 詞元的 fertility 對比下，交互作用 +0.40、−1.56、−0.05、−1.19（pHolm ≥ 0.61）；Study I 五組的 r = 0.99 不被當作 scaling law，Table 1 判定為 not reproduced | 本篇研究結果 | §4.3, p. 6；Table 1, p. 8 | 符合來源 |
| 28 | Card 5 | 兩個預訓練編碼器在 fertility 2.20 的讀出增益為 AfroXLM-R +0.54 [−1.21, 2.10]（2 點 margin 等價於零）與 XLM-R +0.72 [−1.53, 2.95]（inconclusive），Table 1 記為 pretrained < 1，皆小於同 fertility 的從頭模型 | 本篇研究結果 | §4.3, p. 6；Table 1, p. 8；Table 7, p. 19 | 符合來源 |
| 29 | Card 5、Card 6 留意 | 一個 XLM-R 微調 run 發散且開發與測試 F1 皆為零，被開發分數閘門剔除；若納入，句子 bootstrap 會誤報 −13.5 F1 的讀出效果（pHolm = 0.001） | 本篇研究結果 | §4.3, p. 6；Appendix F.2, p. 17；Table 7 註 ‡, p. 19 | 符合來源 |
| 30 | Card 5 | 同容量 BPE 掃描中，阿姆哈拉語在 1.97 倍 fertility 時最好（+7.7 F1），2.42 倍時回到基準（+0.2，pHolm = 0.85）；豪薩語每一檔都下降，最低 −10.7 F1 | 本篇研究結果 | §4.4, p. 7；Fig. 4, p. 7 | 符合來源 |
| 31 | Card 5 | ROOTPAT 的粒度步驟在兩次實作變號：Study I 打亂減 BPE +4.25 F1，Study II −3.39 F1 | 本篇研究結果 | Fig. 2a、2b, p. 6；Table 6, p. 19 | 符合來源 |
| 32 | Card 5 | Study I 翻譯 BPE 為 16.9（阿姆哈拉語）與 31.1 chrF++（豪薩語）；較細目標切分皆有代價：阿姆哈拉語 ROOTPAT 掉 0.95–1.47、打亂掉 0.90、豪薩語 fertility 匹配 BPE 掉 1.52（pHolm < 10^−3）；真詞根與打亂無差（−0.05，pHolm = 0.30），分析器只覆蓋 59.7% MT 詞型，作者不對翻譯中的詞根效果下結論 | 本篇研究結果 | §4.5, p. 7；Appendix F.1, p. 17 | 符合來源 |
| 33 | Card 6 留意 | 重現帳本：Study I 六項結論中兩項重現、三項未重現、翻譯 null 未獲確認；編碼器特徵通道 Study I +1.83 F1、Study II −0.42 且等價於零；同詞根注意力偏置絕對值不超過 0.12 F1，但目標詞對注意力提高 1.65 至 2.44 倍 | 本篇研究結果 | Table 1, p. 8；Appendix C, pp. 15–16 | 符合來源 |
| 34 | Card 6 報告 | 作者稱約 78% 的分析器支援增益可由詞形表單獨取得；詞根效果被解讀為詞彙身份的彙整，而非詞形學任務本身；此解釋未經實驗驗證 | 作者解釋 | §4.7, p. 8 | 符合來源 |
| 35 | Card 6 限制 | 詞根結果只基於一種語言、兩套分析器；因無 NER 語料未能做提格利尼亞語擴充；粒度現象只據兩種語言，不能推廣到非洲或亞非語系整體 | 作者解釋 | Limitations, pp. 8–9；Ethical considerations, p. 9 | 符合來源 |
| 36 | Card 6 限制、留意 | 效果只在 1M 至 2M 參數、1,750 句從頭訓練的小模型上量到；五個 seeds 下單一 run 可主導對照；未做同時重抽 seeds 與句子的兩層 bootstrap | 作者解釋 | Limitations, p. 9 | 符合來源 |
| 37 | Card 6 留意 | 翻譯語料約 44% 宗教文本、貪心解碼，Study II 系統分數接近底部且原因未診斷；粒度在兩研究中變號的原因未找出；分解後的音流上訓練 BPE 這個中介基線未測試 | 作者解釋 | Limitations, p. 9 | 符合來源 |
| 38 | Card 1 速覽「公開」、Card 6 公開 | 原文未聲明程式、資料或模型公開發布；倫理段稱研究用小模型不作工具釋出，語料以記錄之 SHA-256 哈希取得 | 本篇研究結果 | Ethical considerations, p. 9；Appendix E「Data and compute」, p. 17；全文 19 頁無 Data Availability 或程式碼連結 | 符合來源 |
| 39 | Card 6 報告 | 分詞比較應交叉讀出、匹配詞表與非嵌入參數與詞級序列預算；主張語言結構而言須有打亂詞根對照與容量匹配粒度掃描 | 作者解釋 | §4.7, p. 8；§5, p. 8 | 符合來源 |
| 40 | Card 6 延伸想法 | 把同類對照搬到別的分詞研究時，先訓練只改粒度的參考系統，再問語言結構是否有額外貢獻 | Wiki 詮釋 | 本頁根據式 (1)（§3.1, p. 3）與 §5 建議（p. 8）提出；原文未在第三種語言或其他任務驗證 | 符合來源 |
| 41 | Card 1 速覽「模型與測試」 | Study I 的 NER 編碼器約 0.97M 參數（965k 至 967k），Study II 為 1.95M 參數 | 本篇研究結果 | §4.1, p. 5；Appendix E, p. 17；Appendix E「Capacity matching in Study II」, p. 17 | 符合來源 |
| 42 | Card 5 對照表 | Study I 阿姆哈拉語分析器組對 BPE 的差額：首詞元讀出 −2.26 F1，平均池化讀出 +9.11 F1 | 本篇研究結果 | Table 5, p. 19，analyser 列「vs. bpe, first」與「vs. bpe, pool」欄 | 符合來源 |
| 43 | Card 5 翻譯段、重現帳本 | Study II 英譯阿姆哈拉語句子層真詞根減打亂為 +0.19 chrF++ [0.07, 0.31]（p = 0.002），種子層 +0.31 但不顯著（pseed = 0.11）；對兩種置換的句子層差為 +0.29 與 +0.62，種子層 pseed = 0.064 與 0.001；五套系統都只有 7.2 至 8.2 chrF++；Table 1 對「翻譯無詞根效果」之判定為 null not confirmed | 本篇研究結果 | Appendix D, p. 16；Table 1, p. 8；Table 3, p. 18 | 符合來源 |
| 44 | Card 5 重現帳本 | Table 1 逐項判定：真詞根勝打亂 Study I +4.86 F1、Study II +4.65 F1 且 5/5 seeds 為正，判定 reproduced；讀出增益全為正（Study I +2.0 至 +13.4 F1、Study II +2.7 至 +4.7 F1、預訓練模型小於 1 點），判定 reproduced in sign；讀出增益隨 fertility 增長 not reproduced；ROOTPAT 粒度步驟有幫助 not reproduced；編碼器通道在 BPE 後有幫助 not reproduced；翻譯無詞根效果 null not confirmed。六項中兩項重現、三項未重現、一項 null 未確認 | 本篇研究結果 | Table 1, p. 8；§4.6, p. 8 | 符合來源 |
| 45 | Card 6 留意 | §4.6 另指出重現帳本之外有四項 Study I 預測失敗（豪薩語粒度增益轉移、每種分詞器皆有讀出效果、ROOTPAT 壓縮優勢、同詞根注意力偏置）；九個 null 在預先設定的 margin 下屬等價，其餘 null 僅為 inconclusive | 本篇研究結果 | §4.6, pp. 7–8；Appendix F.2, p. 18 | 符合來源 |
| 46 | Card 4 評分、卡片 04 評分 | Study I 每設定五個 seeds 並在最後 epoch 評估；Study II 從頭模型亦用五個 seeds（seeds 0 至 4），XLM-R base 與 AfroXLM-R base 各用三個 seeds | 本篇研究結果 | §4.1, p. 5,「Models」與「Study II」段；Table 4, p. 18,「Pretrained」列；Table 7, p. 19,「Per-seed F1」欄；Appendix F.2, p. 18,「Per-seed scores」段 | 符合來源 |
| 47 | Card 4 阿姆哈拉語、Card 5 翻譯段 | Study II 翻譯只做 en→am，訓練 60,000 對、4.06M 參數模型，並以共享詞典解碼器還原詞形；該解碼器對真實與對照組完全對齊，但使 ROOTPAT 各組相對 BPE 受罰，故 ROOTPAT 與 BPE 的 MT 絕對分數不可直接比較，只有對覆蓋率的依賴可解讀；不同於 Study I 的 20k 對、8.8M 參數、精確反轉，亦沒有豪薩語 Study II 翻譯系統；Table 3 標明 Study II MT 為 en→am、五個 seeds | 本篇研究結果 | Appendix D, p. 16,「Study II set-up」與「Results」段；Table 3, p. 18 標題與註 †；Table 4, p. 18,「MT」列 | 符合來源 |
| 48 | 卡片 04 評分、卡片 05 指標說明 | NER 以詞級 entity-level micro-F1 over words 計分並乘 100 報告，故滿分 100；翻譯以 chrF++（字元 n-gram 重疊）計分並以 sacreBLEU 檢查；原文只報告這些自動指標，未描述人工評分 | 本篇研究結果 | §4.1, p. 5,「Models」段；§4.3–§4.5, pp. 6–7；全文 19 頁未見人工評分流程 | 符合來源 |
