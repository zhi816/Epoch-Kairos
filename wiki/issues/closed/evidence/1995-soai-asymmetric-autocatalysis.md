# 已結案問題：evidence/1995-soai-asymmetric-autocatalysis.md

> 本檔收錄 [wiki/evidence/1995-soai-asymmetric-autocatalysis.md](../../../evidence/1995-soai-asymmetric-autocatalysis.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-213 | fixed | evidence/1995-soai-asymmetric-autocatalysis.md | 第 11 行 | 原文不符
- **問題**：表格將 Series A 出處標記為「印刷頁 768 Table 1 Runs A1–A5；p. 767 右欄首段」，但 p. 767 右欄首段實為 Series B 之延續與 A、B 兩系列總結（lines 122–126），Series A 之具體實驗描述與反應條件位於 p. 767 左欄第 3 段至末段（lines 37–53）。
- **來源**：印刷頁 767（PDF 第 1 頁）文字層 `pdf_page1_text.txt` 第 37–53 行（左欄 Series A）與第 122–126 行（右欄 Series B 結尾）。
- **發現於**：2026-11-11 10:47，Antigravity by Google DeepMind（Gemini 3.8 Flash）。
- **處理**：2026-11-11 11:14，OpenCode by SST（MiniMax M3.1 Flash）。Series A 出處改為「印刷頁 768 Table 1 Runs A1–A5（1,674 倍見 Run A5）；p. 767 左欄第 3 段（Series A 起始 5% e.e. 之實驗描述與 20 mol% 條件）」，並註明 942 與 1,674 倍之合併總結句位於 p. 767 右欄首段（承左欄末段）。Series B 出處同步改為「印刷頁 768 Table 1 Runs B1–B5（942 倍見 Run B5）；p. 767 左欄末段（2% e.e. 起始與「increased by the factor of 942 times」之文字塊）」，均以 pymupdf 文字塊座標逐一核對。
