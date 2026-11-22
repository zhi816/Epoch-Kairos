# 已結案問題：cards/1995-soai-asymmetric-autocatalysis.md

> 本檔收錄 [wiki/cards/1995-soai-asymmetric-autocatalysis.md](../../../cards/1995-soai-asymmetric-autocatalysis.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-208 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 5 第 65 行 | 歸因／版本錯置
- **問題**：Card 5 里程碑將 2026 諾貝爾化學獎表彰語寫為「Kagan與Soai獲諾貝爾化學獎表彰不對稱自催化」，遺漏官方表彰核心「非線性效應（non-linear effects）」，且將非自催化發現者的 Kagan 錯誤歸為表彰不對稱自催化（Kagan 獲獎工作為非線性效應，Soai 為自催化）。
- **來源**：[Nobel Prize in Chemistry 2026](https://www.nobelprize.org/prizes/chemistry/2026/)；論文頁 Frontmatter 第 10 行與正文第 28 行；證據表第 5 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。里程碑改為「Kagan與Soai獲諾貝爾化學獎，表彰非線性效應」，補回官方引文核心「非線性效應」並不再把自催化單獨歸給 Kagan；另於註記標明獎項亦表彰自催化（官方引文：「for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis」）。

### EK-209 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 6 第 70 行與 Card 2 第 16–17 行 | 過度表述
- **問題**：Card 6 轉變寫「稀釋雜訊→自發放大」，Card 2 缺口寫「缺乏能自發濃縮微小手性偏差之化學反應網路」，但 1995 原文為 2% 及 5% e.e. 種子放大，Run D 外消旋對照（0% e.e.）產物手性選擇性低於檢測極限（BDL），未顯示能「自發」放大或濃縮；且 EK-205 已決議刪除「自發」，卡片檔未同步清除殘留之「自發放大」與「自發濃縮」。
- **來源**：印刷頁 768 Table 1 Run D；p. 767 左欄摘要第 1 段（文字層 `pdf_page1_text.txt` 第 18–25 行）；`wiki/issues.md` EK-205。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。Card 6 轉變改為「稀釋雜訊→種子逐輪放大」、Card 2 缺口改為「缺乏能把微小手性偏差逐輪放大的化學反應網路」，刪除「自發放大」與「自發濃縮」殘留；Card 2 結語改以 Run D 外消旋對照之實測結果表述（「無手性種子時，產物選擇性低於檢測極限。」），與種子實驗一致。

### EK-214 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 5 第 64 行 | 過度表述
- **問題**：Card 5 里程碑將 Kawasaki 2009 表述為「證明碳同位素微弱差異亦能觸發手性自催化」，使用絕對化強斷言「證明」；該文在證據表第 26 行標註為「僅書目，內容未核對」，且自然科學實驗為「顯示/示範」（Triggered/demonstrated），不宜在未核對全文下逕寫「證明」。
- **來源**：Kawasaki et al. (2009), *Science* 324:492–495；證據表 `evidence/1995-soai-asymmetric-autocatalysis.md` 第 26 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。「證明」降格為「顯示」，並於出處欄保留「（書目未對照全文）」標示，與證據表第 26 行「僅書目」之狀態一致。

### EK-215 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 2 結語 | 歸因／版本錯置
- **問題**：「無手性種子時，產物選擇性低於檢測極限。」為本篇 Table 1 Run D 之外消旋對照實驗結果，卻置於描述 1995 年前困境的「世紀瓶頸」卡結語，把本篇實驗誤置為先前瓶頸；且「無手性種子」把外消旋 1（0% e.e.）錯述為無手性種子，原文為「the enantioselectivity of a racemic 1 as autocatalyst was below the detection level (run D; Table 1)」。
- **來源**：印刷頁 768 Table 1 Run D（pdf_page2_text.txt 第 117–123 行）；印刷頁 767 右欄「On the other hand」段（pdf_page1_text.txt 第 127–135 行）。
- **發現於**：wiki/log.md [2026-11-11 12:28] audit（CodeBuddy Code by Tencent）
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。依原文 p.767 與 p.768 將卡片結語改為 Frank 方案仍待化學反應實例檢驗，移除誤置的 Run D 結果；論文頁 Run D 明示使用外消旋催化劑。

### EK-223 | fixed | cards/1995-soai-asymmetric-autocatalysis.md | Card 6 結語 | 過度表述
- **問題**：卡片以「隨機漲落」直接連接本篇實驗與生命手性起源；本篇以已有偏差的催化劑起始，未確定生命手性的最初來源。
- **來源**：Soai 等（1995）印刷頁 767 摘要、左欄及 p.768 Table 1。
- **發現於**：2026-11-11 複核卡片與 EK-218 時，Codex by OpenAI（GPT-6）。
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。改寫為起始手性偏差可被自催化放大，並保留生命手性最初起點尚待釐清的界線；論文頁 Card 6 同步改寫。
