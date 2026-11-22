# 已結案問題：concepts/chiral-symmetry-breaking.md

> 本檔收錄 [wiki/concepts/chiral-symmetry-breaking.md](../../../concepts/chiral-symmetry-breaking.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-210 | fixed | concepts/chiral-symmetry-breaking.md | 第 34 行 | 歸因／版本錯置
- **問題**：內文稱「異手性二聚體充當『熱力學失活陷阱』，使主導手性單體在動力學活性池中佔據壓倒性催化優勢」，將活性催化中心誤寫為「單體」。在 Blackmond 2001 二聚體催化模型中，催化活性中心為同手性二聚體（homochiral dimer），並非單體；此處混淆了二聚體催化機制與單體催化模型（如 Noyori DAIB 機制），且與論文頁 Card 3 第 92、108 行矛盾。
- **來源**：Blackmond et al. (2001), *JACS* 123:10103–10104；論文頁 `papers/1995-soai-asymmetric-autocatalysis.md` Card 3 第 92、108 行。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。改為二聚體模型之正確描述：「異手性二聚體充當『熱力學失活陷阱』，使催化活性較高的同手性二聚體在活性池中佔據優勢」，刪除誤植之「單體」與「壓倒性」；並加註「依 Blackmond 2001 之模型描述，本頁尚未對照全文」，與論文頁 Card 3 表述一致。

### EK-218 | fixed | concepts/chiral-symmetry-breaking.md | 第 32、34 行 | 過度表述
- **問題**：第 32 行「物理場起源（如圓偏振光、地球自轉科氏力、宇稱不守恆之弱相互作用能差）與統計純漲落兩種假說」與「這些結果支持……假設」、第 34 行「在數學形式上與若干非線性模型（例如 Lotka–Volterra 競爭方程）有類比」及「異手性二聚體充當『熱力學失活陷阱』」，均非印刷頁 767–768 原文所有（原文僅言 homochirality「remains a puzzle」、Frank 之隨機漲落方案，並明言詳細機制「remains to be clarified」），卻把內容未核對之 Kawasaki 2009 與 Blackmond 2001 模型描述併為正面歸因與類比，超出原文可支持範圍。
- **來源**：印刷頁 767 左欄摘要第 1 段（pdf_page1_text.txt 第 10–25 行）；印刷頁 768 左欄末段至右欄「It seems conceivable…」與「remains to be clarified」（pdf_page2_text.txt 第 142–151、197–201 行）；證據表第 26、34 行。
- **發現於**：wiki/log.md [2026-11-11 12:28] audit（CodeBuddy Code by Tencent）
- **處理**：2026-11-11，Codex by OpenAI（GPT-6）。移除無來源的物理場清單、Lotka–Volterra 類比及熱力學陷阱歸因；以 Soai 1995 pp.767–768 與 Blackmond 2004 作者回顧分別描述種子放大及後續二聚體活性模型，建立限於本次查核的概念證據表。
