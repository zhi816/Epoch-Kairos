# 證據表：2025-tulun-adaptable-lrl-mt-merx
- **採用版本**：*ACL 2025 System Demonstrations*, pp. 129–139 正式版，DOI: 10.18653/v1/2025.acl-demo.13（ACL Anthology 2025.acl-demo.13）；封存於 `raw/my-focus/英文論文/llm 輔助/TULUN Transparent and Adaptable Low-resource Machine Translation.pdf`（PDF 第 1 頁即 p. 129）。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09；2026-11-10 由 Claude Code by Anthropic（Claude Opus 5.5）回原文逐項重建（EK-116、EK-117、EK-156）

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | DOI `10.18653/v1/2025.acl-demo.13`；作者 Raphaël Merx、Hanna Suominen、Lois Hong、Nick Thieberger、Trevor Cohn、Ekaterina Vylomova；pp. 129–139 | 本篇研究結果 | 首頁署名；Crossref（關閉 EK-057） | 符合來源 |
| Card 1 | 既有術語約束方法多需專用模型或微調，對非技術使用者與小型組織不實際；商用服務少支援低資源語言與術語自訂 | 作者解釋 | 摘要；§1, pp. 129–130 | 符合來源 |
| Card 1 | Tulun 在德頓語意為「assistance」，取其輔助而非取代人類專業之意 | 作者解釋 | p. 129 註 1 | 符合來源 |
| Card 1 | 作者稱就其所知，TULUN 是唯一支援德頓語、比斯拉馬語等低資源語言的開源術語感知翻譯工具（原頁面「首創」改為此句，EK-156） | 作者解釋 | §2 Our contribution, p. 131 | 符合來源 |
| Card 2 | 術語約束之既有做法（替換來源詞、前置詞典條目）需專用模型或微調，耗資源且可能災難性遺忘 | 作者解釋 | §2, p. 130 | 符合來源 |
| Card 2 | 介面示例：MT 把「potable」譯錯，LLM 從翻譯記憶找到正確譯法「stret blong dring」（原頁面「錯譯為非飲用水」原文沒有，EK-156） | 本篇研究結果 | §3.1, p. 131；Figure 2 | 符合來源 |
| Card 2 | LLM 翻譯成低資源語言或特定領域時，準確度可能不如專用 MT | 作者解釋 | §1, p. 130；§2, p. 130 | 符合來源 |
| Card 3 | 原文全文無編號公式，流程以文字與 Figure 1 說明；原頁面兩條流程區塊公式為 Wiki 自擬，已刪（EK-116） | 本篇研究結果 | 全文；§3.1–§3.2, pp. 131–132；Figure 1 | 符合來源 |
| Card 3 | 詞彙表以 spaCy `en_core_web_sm` 斷詞後之 {1,2}-gram 重疊檢索；翻譯記憶以 Tantivy 實作 Top-N BM25，N 可設定（原頁面「預設為 5 句」原文沒有，EK-156） | 本篇研究結果 | §3.2, p. 132 | 符合來源 |
| Card 3 | 後端為 Django；Google Translate 或 Hugging Face translation pipeline；LiteLLM；評估之系統提示含少樣本示例與思維鏈；Docker 部署 | 本篇研究結果 | §3.2, p. 132 | 符合來源 |
| Card 3 | 介面以紅色與綠色標出後編輯改動，並列出所用詞彙表條目與相似句 | 本篇研究結果 | §3.1, p. 131；Figure 2 | 符合來源 |
| Card 4 | 資料：德頓語醫療詞彙表 2,698 條、翻譯記憶 1,018 句、評估保留 451 句；比斯拉馬語詞典 5,769 條、翻譯記憶 3,353 段、評估保留 841 段；資料屬合作組織，可依協議申請 | 本篇研究結果 | §4.1.1, p. 132 | 符合來源 |
| Card 4 | 表 1，MADLAD-400-10B 列：TDT 35.78、BIS 15.22、AVG 24.37；opus-mt 列：TDT 16.01、BIS 32.60、AVG 24.31 | 本篇研究結果 | 表 1, p. 133 | 符合來源 |
| Card 4 | 表 1，Gemini 0-shot 列：TDT 44.05、BIS 37.78、AVG 39.63；Gemini 10-shot 列：TDT 44.59、BIS 45.37、AVG 44.98 | 本篇研究結果 | 表 1, p. 133 | 符合來源 |
| Card 4 | 表 1，MADLAD + Gemini 列：TDT 47.87、BIS 47.94、AVG 47.91；∆vs MADLAD 列：+12.09、+32.72、+22.41 | 本篇研究結果 | 表 1, p. 133 | 符合來源 |
| Card 4 | 表 1，opus-mt + Gemini 列：TDT 34.27、BIS 48.14、AVG 41.21；∆vs opus-mt 列：+18.26、+15.54、+16.90 | 本篇研究結果 | 表 1, p. 133 | 符合來源 |
| Card 4 | 表 1 僅列 ChrF++，不含 BLEU | 本篇研究結果 | 表 1, p. 133 | 符合來源 |
| Card 4 | SUS 平均 81.25，只收兩份回應（臨床主任、比斯拉馬語語言學家），屬 excellent（原頁面「Grade A」原文沒有，EK-156）；兩位參與者為共同作者 | 本篇研究結果 | §4.1.2, p. 133；倫理聲明, p. 135 | 符合來源 |
| Card 4 | TAM 各題平均 4 至 5 分；整體有用性 5/5；提升翻譯品質 4.5/5；協助翻譯專業內容 4.5/5 | 本篇研究結果 | §4.1.2, p. 133；附錄 B | 符合來源 |
| Card 4 | FLORES-200 devtest 1,012 句；GATITOS 詞彙表；allenai/nllb 平行句；NLLB-54B 為 MT 基線；Gemini 2.0 Flash | 本篇研究結果 | §4.2, p. 133 | 符合來源 |
| Card 4 | 表 2，NLLB 54B 列：TPI 41.61、DZO 34.67、QUY 26.87、RUN 42.51、LIN 47.99、ASM 35.91、AVERAGE 38.26 | 本篇研究結果 | 表 2, p. 134 | 符合來源 |
| Card 4 | 表 2，Gemini 10-shot 列：TPI 44.07、DZO 30.74、QUY 31.28、RUN 39.83、LIN 49.42、ASM 38.29、AVERAGE 38.94 | 本篇研究結果 | 表 2, p. 134 | 符合來源 |
| Card 4 | 表 2，NLLB + Gemini APE 列：TPI 46.80、DZO 35.76、QUY 32.40、RUN 41.17、LIN 50.58、ASM 39.80、AVERAGE 41.09 | 本篇研究結果 | 表 2, p. 134 | 符合來源 |
| Card 4 | 表 2，∆vs NLLB 54B 列：+5.19、+1.09、+5.53、-1.34、+2.59、+3.89、AVERAGE +2.83；正文另稱比 Gemini 平均高 2.15；摘要寫作 2.8 | 本篇研究結果 | 表 2, p. 134；§4.2, p. 134；摘要 | 符合來源 |
| Card 4 | 基隆迪語下降 1.34 分；不注入詞彙表時比 NLLB 高 0.25 分，判定為 LLM 依詞彙表錯誤改字（原頁面「回升至 42.76」為 Wiki 依此計算之值，已改寫為原文說法，EK-156） | 本篇研究結果 | §5, p. 134；附錄 C | 符合來源 |
| Card 5 | FLORES 實驗以 NLLB-54B 本身為初譯模型再以 LLM 後編輯，平均比 NLLB-54B 高 2.83；原文未以小型 NMT 與 54B 模型比較（修正 EK-117） | 本篇研究結果 | §4.2 與表 2, pp. 133–134；摘要 | 符合來源 |
| Card 5 | 公開資源：程式碼 GitHub `raphaelmerx/tulun`，MIT 授權；線上系統 bislama-trans.rapha.dev；展示影片 | 本篇研究結果 | p. 130 註 2；摘要；§1, p. 130 | 符合來源 |
| Card 5 | 作者明列之限制：準確度影響因語言而異（基隆迪語下降）；可設定性需使用者了解 MT 與 LLM；極低資源、構詞複雜或罕見文字之語言可能幻覺更多；易用性研究僅兩位參與者且為共同作者 | 作者解釋 | §5, p. 134；倫理聲明, p. 135 | 符合來源 |
| Card 5 | 作者所述未來方向：系統化提示最佳化（DSPy MIPRO）；本機小型後編輯模型以支援離線部署；擴大易用性研究；評估 DeepSeek-R1 等其他 LLM；智慧預設與提示調整模組 | 作者解釋 | §5, p. 134；§6, pp. 134–135 | 符合來源 |
| Card 5 | 作者主張 TULUN 讓使用者能以專業持續改進翻譯過程，是 MT 理念之轉變 | 作者解釋 | §1, p. 130；§6, p. 134 | 符合來源 |
| Card 6 | 對個人研究方向之映射與啟發 | Wiki 詮釋 | 頁面已標明 | 不適用 |
