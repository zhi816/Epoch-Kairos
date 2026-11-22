# 已結案問題：concepts/brain-machine-interface.md

> 本檔收錄 [wiki/concepts/brain-machine-interface.md](../../../concepts/brain-machine-interface.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-043 | fixed | concepts/brain-machine-interface.md | 核心支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 能量吸引子寫成當代 BCI 神經流形解碼之數學基礎；神經流形屬獨立研究脈絡，現有來源不足以建立直接傳承。
- **來源**：[Hopfield 封存原文](../../../../raw/1982-hopfield-network.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 21:57] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂腦機介面與神經編碼概念頁：釐清 Hopfield (1982) 為群體狀態空間吸引子提供物理啟發，而現代 BCI 之神經流形解碼源自運動皮質實證降維建模脈絡（如 Churchland et al. 2012），兩者在群體狀態空間幾何上深層呼應而非直接數學繼承。建立證據表 wiki/evidence/brain-machine-interface.md。

### EK-044 | fixed | concepts/brain-machine-interface.md | 跨學科延伸 | 過度表述
- **問題**：將雙光子讀取與全息光遺傳寫入概括為「萬級神經元的無損閉環互動」；原始研究為光刺激選定個別細胞、同時記錄數千神經元，未驗證萬級同時控制、無損或臨床可用。
- **來源**：[原始研究](https://www.nature.com/articles/s41593-026-02350-9)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。修訂腦機介面概念頁全光學 BCI 段落：將實驗規模客觀限定為在動物模型中記錄數千神經元並全息光刺激數十至數百個特定細胞之單細胞級閉環調控，刪除「萬級神經元無損閉環互動」之過度表述，交代光散射深度與光熱耐受等客觀物理瓶頸。建立證據表 wiki/evidence/brain-machine-interface.md。
- **複核**：2026-11-10，Codex by OpenAI（GPT-6）。萬級與無損臨床的舊表述已收斂；但目前以單句將數千細胞記錄、數十至數百細胞刺激和單細胞級閉環調控合併，證據表所列研究尚未逐項支持同一實驗的全部條件。閉環研究存在，仍須為這項具體規模和回饋主張補直接來源或拆開。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。改以 Zhang 等（2018）小鼠皮質全光學閉環研究為直接例證，區分單細胞訊號觸發與目標細胞群，不再把不同實驗規模合成同一結果；同步改正概念頁及證據表。
