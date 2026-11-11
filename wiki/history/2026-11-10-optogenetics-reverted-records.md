# 2026-11-10 光遺傳學收錄：回退前歷史紀錄

本檔保留提交 `0a17f2f` 自日誌與問題清單刪除的兩段原文，來源為其父提交之內容；下方是歷史快照，不代表現況，原收錄內容已被回退。初始收錄提交 `eb85be2` 曾使用 EK-203，合流提交 `b2dbc80` 將該紀錄改為 EK-204。EK-204 後來用於另一問題，原問題以 EK-219 恢復追蹤。保留原文不表示本次已重新核實原論文。

## 被刪除的日誌條目

```markdown
## [2026-11-10 22:40] ingest | 光遺傳學 2005-optogenetics 證據表、卡片檔與網頁上架 | #神經科學 #生物科技
- **執行代理**：Antigravity by Google DeepMind
- **模型版本**：Gemini 3.8 Flash
- **具體變更**：
  - [wiki/evidence/2005-optogenetics.md](evidence/2005-optogenetics.md)：依原文 Nature Neuroscience 8(9):1263–1268 建立完整證據表（24 列），涵蓋病毒表現、光電流動力學、動作電位延遲與突觸傳遞，並回原文逐一核對數據。
  - [wiki/issues.md](issues.md)：登記並關閉 EK-204，指出原論文頁 Card 3 列出之光電流方程、馬可夫動力學與 HH 微分方程未見於 2005 年實驗報告，改以作者實測之光電流動力學數據文字說明呈現。
  - [wiki/papers/2005-optogenetics.md](papers/2005-optogenetics.md)：依 EK-204 修訂 Card 3，將未見於原文之展示式改為實驗動力學條列說明，補註奠基論文 `raw/2003-channelrhodopsin2.pdf` 路徑，狀態改為 `published`，核實狀態改為 `verified`。
  - [wiki/cards/2005-optogenetics.md](cards/2005-optogenetics.md)：依 `paper-card-writer` 規範撰寫完整六張卡片；Card 3 採無公式模式並附 Type F 空間示意圖（藍光、質膜、光敏通道與離子內流），Card 4 提取 4 項核心實驗數值（$8.0\text{ ms}$、$<\!5\text{ ms}$、$496\text{ pA}$、$5.1\text{ s}$），Card 5 登記 4 項里程碑（Aravanis 2007、Gradinaru 2009、Liu 2012 與 2026 諾貝爾獎）。
  - [web/papers/2005-optogenetics/index.html](../web/papers/2005-optogenetics/index.html)：以 `tools/build_paper_prototype.py` 產生正式雙欄頁面，自我檢查 ERROR 0、WARN 0。
  - [web/index.html](../web/index.html)：以 `tools/build_home.py --card 2005-optogenetics` 重建首頁，完成卡片牆上架（No.01），自我檢查 ERROR 0、WARN 0。
  - [wiki/todo.md](todo.md)：完成並移除 TD-018（奠基論文原始檔路徑已補齊並列為已引用）。
  - 驗證：`check_cards.py` ERROR 0、`build_paper_prototype.py` ERROR 0、`build_home.py --check` 一致、`lint_wiki.py` ERROR 0。
```

## 被刪除的問題條目

```markdown
### EK-204 | fixed | papers/2005-optogenetics.md | Card 3 展示公式未見於原文 | 原文未支持
- **問題**：原論文頁 Card 3 列出光電流方程、三態連續馬可夫動力學與 Hodgkin-Huxley 整合微分方程等三組區塊展示公式，皆非 Boyden et al. (2005) 本文所載之公式；原文為實驗技術報告，全篇無編號數學展示式，上述公式實為後續生物物理學文獻之理論模型。
- **來源**：[Boyden 等原文](../raw/2005-optogenetics.pdf) Nature Neuroscience 8(9):1263–1268 全文；[論文頁](papers/2005-optogenetics.md) Card 3。
- **發現於**：2026-11-10，依 TD-017 / 2026-11-10 規則建立證據表與卡片檔，Antigravity by Google DeepMind。
- **處理**：2026-11-10，Antigravity by Google DeepMind（Gemini 3.8 Flash）。移除論文頁未見於原文之三組展示公式，改以作者對光電流動力學（峰值 $496\text{ pA}$、穩態 $193\text{ pA}$、上升率 $160\text{ pA/ms}$、恢復 $\tau = 5.1\text{ s}$）之實驗數據與測量說明呈現；建立證據表登記 24 列主張，卡片 Card 3 採無公式模式。頁面核實狀態改為 verified。
```
