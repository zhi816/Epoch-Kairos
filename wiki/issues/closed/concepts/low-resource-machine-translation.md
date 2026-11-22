# 已結案問題：concepts/low-resource-machine-translation.md

> 本檔收錄 [wiki/concepts/low-resource-machine-translation.md](../../../concepts/low-resource-machine-translation.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-087 | fixed | concepts/low-resource-machine-translation.md | 關鍵技術路徑 | 原文不符
- **問題**：第 49–52 行將構詞特徵增強寫為詞根嵌入與詞綴嵌入拼接投影 $e(w) = W_{\text{proj}}[e_{\text{root}}(w) \,\|\, e_{\text{affix}}(w)]$ 並歸給游景勝（2021）與金柏毅（2025）；惟游景勝（2021）實驗證實詞根嵌入使 BLEU 暴跌、最佳模型係使用表面詞形搭配 52 維詞綴特徵（見 EK-062），而金柏毅（2025）最佳模型 `FC_ftr_jnt` 係使用雙獨立並聯 Transformer Encoder 分別編碼「詞綴字串形式子詞」與「詞綴組合特徵向量」後於編碼器輸出端串接（見 EK-066）。
- **來源**：同 EK-062、EK-066
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。依 EK-062、EK-066 回原文確認之結果改寫「構詞特徵增強」段：刪除無來源之 $W_{\text{proj}}$ 拼接式，改述游景勝（2021）之布林特徵拼接（含預訓練嵌入下 BLEU 下降之反例）與金柏毅（2025）之 FC_ftr_jnt 雙 encoder；同節「跨語言遷移」段一併依廖恒慶（2023）原文改寫，刪除原文未測量之「降低 OOV 率」「零樣本遷移」。
