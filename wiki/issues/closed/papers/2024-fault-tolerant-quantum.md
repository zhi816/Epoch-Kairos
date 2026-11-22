# 已結案問題：papers/2024-fault-tolerant-quantum.md

> 本檔收錄 [wiki/papers/2024-fault-tolerant-quantum.md](../../../papers/2024-fault-tolerant-quantum.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-032 | fixed | papers/2024-fault-tolerant-quantum.md | Card 4 | 原文不符
- **問題**：把「40 個 color-code qubits」混寫成「40 個橫向邏輯 CNOT 閘」，混淆量子位元數與閘數；另須與以 3D [[8,3,2]] code blocks 執行之 48 邏輯量子位元取樣電路分開敘述。
- **來源**：[原文](https://arxiv.org/abs/2312.03982)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Abstract、Section 4 與 Fig. 4、Fig. 5 核實修訂 Card 4：明確區分兩大獨立實驗——(1) 40 個 $d=3$ 色碼邏輯量子位元在 280 個物理原子上的分區維持與操作（使用 20 個橫向 CNOT 實施標記容錯初始化，閒置退相干率約 1%），糾正混淆位元數與閘數之錯誤；(2) 48 個邏輯量子位元之三維 $[[8,3,2]]$ 碼取樣電路（動用 128 個物理原子，在 4D 超立方體連接拓撲下執行包含 228 個邏輯雙量子位元閘與 48 個邏輯 CCZ 閘之深層亂序電路，全錯誤偵測下 XEB 達約 0.1）。證據表見 wiki/evidence/2024-fault-tolerant-quantum.md。

### EK-033 | fixed | papers/2024-fault-tolerant-quantum.md | Card 1 | 原文不符
- **問題**：將中性 87Rb 原子寫成「帶電」搬運；原文為 neutral-atom 陣列。
- **來源**：[封存原文](../../../../raw/2024-fault-tolerant-quantum.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Fig. 1 與 Methods 查核修訂 Card 1：糾正將中性原子光學鑷子搬運誤植為「帶電」之嚴重錯誤，精確表述為「以光學鑷子（2D AOD）相干搬運中性原子（Neutral Atoms）」。證據表見 wiki/evidence/2024-fault-tolerant-quantum.md。

### EK-034 | fixed | papers/2024-fault-tolerant-quantum.md | Card 5 | 原文不符
- **問題**：把 qLDPC 說成已由本實驗實作；原文只把 qLDPC 列為未來降低開銷之方向。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文 Outlook（p. 8）查核修訂 Card 5：更正 qLDPC 相關表述，明確本實驗實作之編碼為表面碼、色碼與三維 $[[8,3,2]]$ 碼，qLDPC 碼僅為原文展望中進一步降低硬體開銷的關鍵未來方向，刪除將 qLDPC 寫成已由本實驗實作之陳述。證據表見 wiki/evidence/2024-fault-tolerant-quantum.md。

### EK-120 | fixed | papers/2024-fault-tolerant-quantum.md | Card 3 與 Card 4 | 原文不符
- **問題**：Card 3 第 53 行寫相干時間 $T_2 > 1.5\,\text{s}$，原文為 T2 > 1 s。Card 4 第 96 行稱 d = 7 時「總計動用約 200 個物理原子」，原文圖 2 標示每個邏輯貝爾對所用物理量子位元數，d = 3、5、7 依序為 26、74、146。
- **來源**：`raw/2024-fault-tolerant-quantum.pdf`（Bluvstein et al. 2024），PDF 第 2、12 頁（T2 > 1 s）、第 3 頁圖 2（146）。
- **發現於**：第一、二批卡片回填 B 組回報，協調者回原文核對（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。以正式版（PMC10830422）與 arXiv v1 核對後，$T_2$ 改為 $> 1$ s；Card 4 改寫為每個邏輯貝爾對使用 26、74、146 個物理位元（Fig. 2d），並補上相關解碼與傳統解碼之差異、初態製備非容錯等限制。證據表登記。

### EK-121 | fixed | papers/2024-fault-tolerant-quantum.md | Card 3 | 原文未支持
- **問題**：Card 3 四組區塊公式（第 64–67 行里德堡哈密頓量、第 75 行穩定子碼空間、第 79 行橫向 CNOT、第 87 行邏輯錯誤率標度）皆未登記於證據表（證據表 Card 3 只有三區架構一列）；B 組回報其中三組原文找不到。原文以文字描述橫向 CNOT 與穩定子，未見以這些形式寫出之公式。
- **來源**：同 EK-120 之 PDF；修正時逐式回原文正文與 Methods 確認，找不到者刪除或標明為教科書式背景。
- **發現於**：第二批卡片回填 B 組回報，協調者核對證據表（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5），第三批卡片回填 B 組。逐式回原文正文與 Methods 核對：里德堡哈密頓量、穩定子碼空間、橫向 CNOT 張量積三式原文沒有，刪除；邏輯錯誤率標度在 Methods 只是行文中之 $\propto (p/p_{\text{th}})^{(d+1)/2}$（引 ref. 24），改為行內並刪去原文沒有之 $\Lambda$ 等式。另補入 Methods「Correlated decoding」之混合整數規劃（未編號式），為本篇相關解碼之原文公式，證據表登記位置。同時改正閘時原子間距為 $\lesssim 2\,\mu$m（Extended Data Fig. 1 圖說）。

### EK-158 | fixed | papers/2024-fault-tolerant-quantum.md | Frontmatter、Card 1、Card 3 與 Card 4 | 過度表述
- **問題**：（1）`hook` 與 Card 1 稱「首次」在單一處理器上編碼 48 個邏輯位元、「打破超導固定晶格限制」、製造一個高碼距邏輯位元「需消耗上千個物理位元」、「正式揭開」早期容錯時代序幕；原文未稱首次、未作這些比較，摘要為「herald the advent of early error-corrected quantum computation」。`title_zh` 冠以「邁向容錯量子計算的歷史跨越」；開頭引言為 Wiki 撰寫卻未註明。（2）Card 3 稱閘時原子間距 $\lesssim 3\,\mu$m，原文為 $\lesssim 2\,\mu$m；稱直接實作「三維與四維拓撲碼」，原文為三維 $[[8,3,2]]$ 碼塊在 4D 超立方體上糾纏。（3）Card 4 稱 $d = 3 \to 7$ 之邏輯貝爾態「超越所有單一物理位元對之成對糾纏保真度」，原文無此說，且未交代改善只在相關解碼下成立、傳統解碼反而變差；稱物理電路「因相干誤差累積導致 XEB 歸零」、48 位元希爾伯特空間「遠超古典模擬極限」，原文沒有；GHZ 段把中途讀取前饋與 GHZ 保真度混寫，未列 72(2)% 之容錯結果。
- **來源**：Bluvstein et al. 2024 正式版全文（PMC10830422）：Abstract；Logical processor based on atom arrays、Improving entangling gates with code distance、Fault-tolerant logical algorithms、Complex logical circuits using 3D codes 各節；Extended Data Fig. 1 圖說；Fig. 2–5。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。依原文改寫上述各句；`title_zh` 與內文標題刪去副題；引言加註；Card 2 註明晶格手術成本等為 Wiki 補充背景；Card 6 第 2 點改為不誇飾之寫法。證據表逐項登記。

### EK-159 | fixed | papers/2024-fault-tolerant-quantum.md | Card 4 後續與 Card 5 | 原文未支持
- **問題**：Card 4 後續段稱 Google Willow 為 105 位元、「首次……無後選擇」，摘要為 101 位元之 $d = 7$ 碼、未提後選擇；稱 Bravyi et al. 2024 證明 $[[144,12,12]]$ 碼降低開銷近 10 倍，且「本篇……正是實作此類 qLDPC 碼的最理想物理平台」，後者無出處，Bravyi 一文亦未引用本篇。Card 5 三點（「正式跨入 EFTQC」、「打破平面拓撲死局」、「定制解碼將容錯門檻再放寬數倍」）皆無出處。本篇發表於 2024 年，頁面也未記載原文所述之未來方向。
- **來源**：doi:10.1038/s41586-024-08449-y、doi:10.1038/s41586-024-07107-7、doi:10.1038/s41567-024-02479-z（arXiv:2308.08648）、doi:10.1038/s41586-025-09543-5（arXiv:2406.17653）、doi:10.1038/s41586-025-09596-6，皆以 Crossref 與摘要核對，OpenAlex 顯示前四者中除 Bravyi 外皆引用本篇；本篇 Outlook。
- **發現於**：第三批卡片回填 B 組撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。後續段改列四篇引用本篇之後續研究（Xu 2024、Google Quantum AI 2024、Zhou 2025、Chiu 2025）並依摘要描述，Bravyi 2024 改標為未引用本篇之相關研究；Card 5 改為作者評價、後續發展與 Outlook 所列方向，各附出處。證據表登記各列。
