# 已結案問題：papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md

> 本檔收錄 [wiki/papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md](../../../papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-058 | fixed | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.loresmt-1.25` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：本檔建立時以 crossref_check.py 查得（Claude Code by Anthropic）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回 ACL Anthology 核對：該篇位於 LoResMT 2026 論文集第 225–230 頁，正確 DOI 為 `10.18653/v1/2026.loresmt-1.22`（原誤記為 `.25`），經 Crossref 與 doi.org 解析確認無誤並更新頁面。

### EK-085 | fixed | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | Card 3 | 原文不符
- **問題**：（1）第 46–48 行將 SONAR 評分寫為餘弦相似度；原文 §2.1.1（p. 226）明言使用 `blaser_2.0` 跨語言語義相似度預測模型（輸出 1–5 分段，故門檻為 3.0 與 3.7，餘弦相似度不可能大於 1）。（2）第 61–72 行與架構圖將四階段課程學習順序與資料集完全寫反：頁面寫作「階段 1：FineWeb-2 合成回譯 50 萬句 -> 階段 2：SONAR 標準品質 -> 階段 3：SONAR 高品質 -> 階段 4：官方驗證集收斂」。原文 §2.3.3（pp. 227–228）與表 1（p. 226）之真實順序為：**階段 1：OPUS 標準品質多語資料**（$3.0 \le \text{SONAR} < 3.7$，含俄、吉、烏茲別克、塔吉克四語全方向共 8,207,314 句）-> **階段 2：OPUS 高品質多語資料**（$\text{SONAR} \ge 3.7$，7,069,840 句）-> **階段 3：FineWeb-2 開源合成回譯資料**（由 50 萬篇吉爾吉斯語文件切出 1,849,234 段，經 Gemma-3-27B 與 Qwen3-235B 回譯及 MADLAD-400-7B-MT 交叉熵 $(0.1, 4.5)$ 過濾後保留 1,566,927 句對、雙向 3,133,854 句）-> **階段 4：SiberianPersonaChat 高品質合成對話資料**（由 GPT-4o 翻譯之 56,529 段俄吉對話、雙向 113,058 句，絕非在官方驗證集上訓練）。另漏述烏茲別克語／塔吉克語輔助遷移（§2.3.1）與 `mt0-large` 詞表剪枝（1.23B 至 800M，§2.3.2）。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Data-Centric Approach at the LoResMT 2026 Turkic Translation.pdf`（§2.1.1 p. 226 表 1、§2.3.1–2.3.3 pp. 227–228）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核對後重寫：Card 3 更正 SONAR 評分為 `blaser_2.0` 跨語言語義相似度預測模型（1–5 分制，非餘弦相似度）；糾正四階段課程學習倒置錯誤，改述真實順序（階段 1：OPUS 標準 8.2M $\to$ 階段 2：OPUS 高品質 7.1M $\to$ 階段 3：FineWeb-2 回譯 3.1M $\to$ 階段 4：合成對話 113K）；補列烏茲別克與塔吉克雙語輔助遷移、以及 mt0-large 詞表剪枝由 1.23B 壓縮至 800M 架構；Card 4 補齊 Table 1–3 與官方競賽測試集（49.1 chrF++ / 69.7 xCOMET 奪冠）詳細數據。建立證據表 wiki/evidence/2026-data-centric-russian-kyrgyz-mt-novokshanov.md，頁面 verification 改為 verified。

### EK-231 | fixed | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | 原 Card 2、Card 5 | 原文不符
- **問題**：原文 §3.3 寫明公開最終模型、過濾後的合成平行資料與 Hugging Face Spaces 線上展示，原頁未記載公開資源。另原 Card 2 寫網路與回譯資料「毒化」模型、「注意力發散」，以及無差別混洗造成「梯度混亂」，原文沒有這些說法；原文只說大型語言模型回譯資料需過濾模型產生的註記、後設說明與重複輸入，並採由較雜到較乾淨資料的分階段訓練。原 Card 5「決定性勝利」「證明」等為 Wiki 加強之表述。
- **來源**：[原文 PDF](../../../../raw/my-focus/大模型輔助/Data-Centric%20Approach%20at%20the%20LoResMT%202026%20Turkic%20Translation.pdf)，§2.1.1, p. 226；§2.3.3, p. 227；§3.3 與 §4, p. 228。
- **發現於**：2026-11-20 改寫為我的關注新六章時回原文抽查，Claude Code by Anthropic（Claude Opus 5.5）。
- **處理**：2026-11-20，Claude Code by Anthropic（Claude Opus 5.5）。改寫論文頁：02 改依原文 §2.1.1、§2.3.3；06 補公開資源；05 改為作者 §4 結論；證據表新增四列。
