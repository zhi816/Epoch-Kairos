# 已結案問題：papers/1995-soai-asymmetric-autocatalysis.md

> 本檔收錄 [wiki/papers/1995-soai-asymmetric-autocatalysis.md](../../../papers/1995-soai-asymmetric-autocatalysis.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-204 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 1–5、證據表 | 原文不符
- **問題**：Table 1 與其註解（含 Run 數據、註 § 與 ＊）位於印刷頁 768（PDF 第 2 頁），論文頁、卡片檔與證據表多處標為 p.767；Series C 之出處標為「右欄末段」、Run D 之出處標為「右欄第 4 段」，但 p.767 右欄實為 3 段，兩者皆不對應。證據表原列之試劑與反應條件（20 mol%、0.208 mmol、甲苯、0 °C、96 h）亦未列。
- **來源**：[1995 原文](../../../../raw/1995-soai-asymmetric-autocatalysis.pdf) PDF 第 2 頁（印刷頁 768）含 Table 1 與註 §（toluene 49 ml、0.208 mmol、0 °C、96 h）；PDF 第 1 頁（印刷頁 767）右欄 “On the other hand…”、“We propose…” 段。
- **發現於**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）統籌，調派 OpenCode MiniMax M3.1 Flash 逐列核對。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。Table 1 相關出處統一改為 p.768，段落序號依正文改為「右欄首段」「右欄第 2 段」；證據表補列試劑與條件列（以 PDF 文字層核對）。

### EK-205 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | hook、Card 1、Card 5、card_line；concepts/chiral-symmetry-breaking.md | 過度表述
- **問題**：頁面以「首次」「自發」描述 1995 年成果，原文兩頁文字層均未見 “first”，「自發」與本篇的種子實驗（2% e.e. 起始）與 Run D 對照矛盾。卡片導語「首個化學實證」、card_line「揭示同手性起源」超出原文能支持的範圍。概念頁另有「首次在有機合成反應中實現」「千倍自增殖」，並把 Kawasaki 2009 的同位素結果歸於 Soai 反應，又以「證明」「精確相通」描述後續模型與其他領域模型之關係。
- **來源**：[1995 原文](../../../../raw/1995-soai-asymmetric-autocatalysis.pdf) PDF 第 1 頁摘要第 1 段（“Here we show experimentally that autocatalysis in a chemical reaction can indeed enhance…”）；PDF 第 2 頁（印刷頁 768）“It seems conceivable…”、“remains to be clarified”。
- **發現於**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）統籌；DeepSeek Harness 獨立審查提出，總指揮對照原文複核。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。刪除「首次」「自發」「首個」；card_line 改為「不對稱自催化，微弱手性偏差被逐輪放大」，封面斷行同步改寫；導語改為「為生命起源同手性提供化學實驗模型。」；概念頁第 24、26、32、34 行改寫；後續研究之二聚體內容於論文頁註明「以 Blackmond 2001 為準，本頁尚未對照該文全文」。已重建論文頁與首頁，論文頁與首頁相關驗證通過。

### EK-206 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 3 鋅烷氧化物循環式 | 原文未支持
- **問題**：步驟 3 寫作 `2_new + H+ → 1_new + Zn(II)`，質量與電荷皆不平衡（缺 i-PrH，且 H+ 數不足）。頁面與證據表原稱「鋅副產物未配平」，但缺漏的 i-PrH 為有機副產物，不屬於鋅物種。
- **來源**：依 Fig. 2 改寫（原文未配平）；以原子與電荷守恒推導為 `2_new + 2H+ → 1_new + i-PrH + Zn2+`（DeepSeek Harness 獨立審查提出，總指揮複核）。
- **發現於**：2026-11-11 10:28，DeepSeek Harness 獨立審查（只讀）。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。改為平衡式並註明「依 Fig. 2 改寫，未列鋅物種之完整計量」；證據表第 17 行同步。

### EK-207 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | frontmatter honor、正文表彰語、證據表獎項核對 | 原文不符
- **問題**：honor 與正文寫「表彰分子同手性起源與不對稱自催化合成」，但諾貝爾官網 2026 化學獎引文為 “for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis”；「分子同手性起源」為官方科普說明之概括，不是表彰語原文。
- **來源**：[Nobel Prize in Chemistry 2026](https://www.nobelprize.org/prizes/chemistry/2026/)
- **發現於**：2026-11-11 10:28，總指揮查證；DeepSeek Harness 獨立審查同樣指出。
- **處理**：2026-11-11 10:28，Claude Code by Anthropic（claude-haiku-5-5）。改為「表彰不對稱有機合成中非線性效應與自催化的發現」；證據表註明官方引文與科普概括之區別。

### EK-211 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 6 第 144–145 行 | 過度表述
- **問題**：內文斷言「放大的本質不是『製造』手性，而是『選擇』手性」，並將異手性二聚體熱力學穩定化類比為「免疫系統的容忍機制」。原文實驗顯示自催化反應由非手性受質原位化學合成了新嘧啶醇分子（新生成物 e.e. 達 90%、物質量放大至 1,674 倍），為化學合成與不對稱誘導過程，並非被動篩選；且與免疫系統容忍機制之結構類比缺乏文獻支持，屬過度詮釋。
- **來源**：印刷頁 767–768 全文（文字層 `pdf_page1_text.txt`、`pdf_page2_text.txt` 均未見此類哲學主張與免疫學類比）；Table 1 新生成物數據（p. 768）。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。Card 6 第 1 點改為「放大的機制同時包含『合成』與『選擇』（Wiki 詮釋）」，並補述本篇確實原位化學合成新嘧啶醇分子（新生成物 e.e. 達 90%、(S)-1 總量放大 1,674 倍，Table 1，p.768），不再斷言僅為「選擇」；第 2 點明確標為 Wiki 詮釋，刪去「有結構上的類比」之過度延伸，改為「僅作為概念類比，不是本篇或文獻之結論」。

### EK-212 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 3 第 108 行 | 未能核實
- **問題**：內文斷言「異手性二聚體 S-R 的生成平衡常數大於同手性二聚體，即 $K_{\mathrm{hetero}} > K_{\mathrm{homo}}$；在相同標準態下以 $\Delta G^{\circ} = -RT \ln K$ 表示，異手性二聚體的 $\Delta G^{\circ}$ 較負，熱力學上較穩定」，忽視了純統計二聚即存在 $K_{\mathrm{hetero}} = 2 K_{\mathrm{homo}}$ 之對稱度因子，且 Blackmond 2001 核心在於催化活性差異（$k_{\mathrm{homo}} \gg k_{\mathrm{hetero}} \approx 0$）；內文坦承「本頁尚未對照該文全文」，證據表第 34 行亦標記為「內容未核對」，卻於正文作出肯定性熱力學數值判定。
- **來源**：Blackmond et al. (2001), *JACS* 123:10103–10104；證據表 `evidence/1995-soai-asymmetric-autocatalysis.md` 第 34 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。$K_{\mathrm{hetero}} > K_{\mathrm{homo}}$、$\Delta G^{\circ}$ 與「儲庫」推論全部改寫為「依 Blackmond 2001 之模型描述」之敘述（催化活性差異亦同），不再以本頁斷言該文數值；並加註判讀界線「同手性與異手性二聚體的統計因子會影響 $K$ 之直接比較，本頁未對照該文全文，數值判斷以原文為準」，證據表第 34 行同步標記。
- **重開**：2026-11-11，Codex by OpenAI（GPT-6）。論文頁仍將上述比較與熱力學推論歸於 Blackmond 2001，但證據表仍記「內容未核對」；加註限制無法證明此歸因，需核對原始文獻或移除未受支持的主張後重新結案。
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。移除未核實的 2001 年平衡常數排序、熱力學穩定性與配平推論；改引 Blackmond（2004）作者回顧的二聚體統計形成與催化活性差異，並明示這是後續模型。同步修正論文頁 Card 3、Card 6 與證據表。

### EK-216 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 6 第 1 點 | 歸因／版本錯置
- **問題**：「（新生成物 e.e. 達 90%，(S)-1 總量放大至 1,674 倍，Table 1，p.768）」把 Series A Run A5 的 1,674 倍與頁面他處（Card 4、證據表第 12 行）歸於 Series B 的新生成物 90% e.e. 併列為同一筆結果且未標系列／run，而原文總結句僅為「amplified to 88-89%, and the amount of (S)-1 was increased by a factor of 942 and 1,674」，並未把 90% 新生成物 e.e. 與 1,674 倍並列。
- **來源**：印刷頁 768 Table 1 Runs A5、B4（pdf_page2_text.txt 第 53–60、86–101 行）；印刷頁 767 右欄首段總結句（pdf_page1_text.txt 第 122–126 行）。
- **發現於**：wiki/log.md [2026-11-11 12:28] audit（CodeBuddy Code by Tencent）
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。直接複核原 PDF 印刷頁 768 Table 1：Run A5 同一列的新生成物 e.e. 為 90% (S)，(S)-1 增加 1,674 倍，因此兩數並非分屬不同系列；Run B4 亦有 90% (S)。原問題判斷有誤，正文與證據表已明確標出 Run A5，保留本條及原判斷供追溯。

### EK-217 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 4 後續第 129 行 | 過度表述
- **問題**：「證明碳同位素 $^{13}\mathrm{C}/^{12}\mathrm{C}$ 比例造成的微弱手性差異，也能在反覆自催化中被放大」對 Kawasaki 2009 使用絕對化強斷言「證明」，但證據表第 26 行標為「書目符合（Crossref）；內容未核對」，卡片 Card 5 第 64 行已依 EK-214 降為「顯示」並加註「書目未對照全文」，論文頁既未同步亦未註明書目未核對。
- **來源**：印刷頁 767–768 全文（pdf_page1_text.txt、pdf_page2_text.txt 均無此後續研究）；證據表 evidence/1995-soai-asymmetric-autocatalysis.md 第 26 行；wiki/issues.md EK-214。
- **發現於**：wiki/log.md [2026-11-11 12:28] audit（CodeBuddy Code by Tencent）
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。依 Kawasaki 等（2009）作者摘要及原文 p.495，改為同位素取代引入手性的分子引發自催化，移除「證明」與易誤解的比例表述；明示未取得其餘全文，並同步卡片及證據表。

### EK-221 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 3 展示公式與卡片公式 | 原文未支持
- **問題**：論文頁列出五組區塊公式，分別為 e.e. 定義、Frank 方程、改寫的反應循環與兩組後續二聚體平衡；1995 年原文未印出這些公式，卡片又將補充定義當成本篇機制公式。
- **來源**：Soai 等（1995）原 PDF 印刷頁 767–768，Fig. 2 與 Table 1 註 §；原證據表將前三組標為 Wiki 整理、後兩組標為 2001 文獻尚未核對。
- **發現於**：2026-11-11 處理 EK-212 與卡片來源時，Codex by OpenAI（GPT-6）。
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。移除五組區塊公式；保留明示為 Wiki 補充的行內 e.e. 定義，以文字描述 Frank 方案與 Fig. 2；卡片改無公式模式並寫明兩頁原文的確認範圍。

### EK-222 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 4 後續文獻作者 | 原文不符
- **問題**：Blackmond 等（2001）作者 Andrea Schorm 的姓氏誤寫為 Schormann。
- **來源**：[期刊書目](https://pubs.acs.org/doi/10.1021/ja0165133)與 [PubMed 紀錄](https://pubmed.ncbi.nlm.nih.gov/11592892/)。
- **發現於**：2026-11-11 處理 EK-212 時，Codex by OpenAI（GPT-6）。
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。更正為 Schorm，並註明 2001 年全文尚未取得。

### EK-224 | fixed | papers/1995-soai-asymmetric-autocatalysis.md | Card 4 Series B、證據表第 12 行 | 過度表述
- **問題**：論文頁寫「B5 的 (S)-1 總量放大 942 倍，新生成物 e.e. 達 88%–90%」，緊接在 B5 之後，讀來像是 Run B5 的數值；證據表同列寫「新生成物純度達 88%–90% e.e.」。原文 Table 1 Series B 新生成物 e.e. 依序為 B1 16、B2 74、B3 89、B4 90、B5 88 (S)，「88%–90%」只對 B3 至 B5 成立，B5 本身為 88%。
- **來源**：Soai 等（1995）印刷頁 768 Table 1 Runs B1–B5「Newly formed product 1」之 e.e. 欄（依 `raw/1995-soai-asymmetric-autocatalysis.pdf` 第 2 頁頁面影像核對）。
- **發現於**：2026-11-11 子代理迴圈試跑（測試分支 test/subagent-loop），由 OpenCode（DeepSeek V4.1 Flash 免費版）審查時提出，Claude Code by Anthropic 回原文確認。
- **處理**：2026-11-11，Claude Code by Anthropic（claude-fable-5-2）。論文頁改為「B5 的 (S)-1 總量放大 942 倍、其新生成物 e.e. 為 88% (S)；B3–B5 新生成物 e.e. 依序為 89%、90%、88% (S)」，證據表第 12 行同步並補上欄位名稱；重建論文頁網頁。卡片 Card 4 原已寫 Run B5 之 88% e.e.，無須修改。
