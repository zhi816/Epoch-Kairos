# 證據表：2025-fragment-shot-reasoning-mt-frontull
- **採用版本**：*arXiv:2505.22293v1* [cs.CL]，2025-05-28；封存於 `raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-09

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 作者 Samuel Frontull 與 Thomas Ströhle；arXiv 2505.22293 | 本篇研究基本資訊 | 首頁標題與署名；ACL/arXiv | 符合來源 |
| Frontmatter & Card 1 | 研究語言為拉定語（Ladin，雷托－羅曼語支），非拉丁語（Latin） | 本篇研究對象 | 摘要；§1, p. 1 | 符合來源（更正 Card 4 原文「拉丁語變體」之嚴重筆誤） |
| Card 1 | 傳統 NMT 微調需至少 13,000 句對 | 文獻引用 | §1, p. 1（引用 Gu et al., 2018） | 符合來源 |
| Card 2 | 整句檢索在低資源下難以命中；拉定語缺乏合適的語義嵌入模型 | 本篇研究背景分析 | §2, p. 3 | 符合來源 |
| Card 3 | 片段少樣本（FS）採 7 至 1 詞滑動視窗在來源端精確匹配，至多抽取 6 組雙語句對；片段選取旨在盡量避免重疊，理想上完整且不冗餘，並非零重疊保證 | 本篇研究方法 | §3, pp. 3–4；Figure 1 | 符合來源（修正先前「無重疊覆蓋」的絕對表述，關閉 EK-082） |
| Card 3 | 樞紐片段提示（PF）經由義大利語樞紐進行兩階段巢狀檢索 | 本篇研究方法 | §3, pp. 3–4；Figure 2 | 符合來源（補列原先漏述之核心機制，關閉 EK-082） |
| Card 4 | 5 款模型（GPT-3.5、GPT-4o、o1-mini、Llama-3.3、DeepSeek-R1） | 實驗設定 | §5, p. 5 | 符合來源 |
| Card 4 | 檢索語料（18,485 句與 14,953 句）；FLORES+ 175 句測試集（Micurá de Rü / OLDI） | 實驗設定 | §4, pp. 4–5 | 符合來源 |
| Card 4 | Table 1 之 BLEU 分數（含 ZS, RS, FS, PF 於各方向） | 本篇研究結果 | 表 1, p. 6 | 符合來源 |
| Card 4 | Table 2 之 Prompt 長度與推論耗時（PF 達 24,852 字元，DeepSeek-R1 耗時約 31 秒） | 本篇研究結果 | 表 2, p. 6 | 符合來源 |
| Card 4 | Table 3 之覆蓋率與 Pearson 相關性（IT $\to$ Ladin 與變體間呈顯著正相關 $r=0.24 \sim 0.53$；Ladin $\to$ IT 接近 0） | 本篇研究結果 | 表 3, p. 7 | 符合來源 |
| Card 4 | 生成譯文中無效詞多出 7%–9%；Figure 2 之 Prompt 敏感度案例 | 研究局限與分析 | §7, p. 7；Limitations, p. 9 | 符合來源 |
| Card 5 | 高資源目標語提示收益極低；推理模型能透過跨語言樞紐部分補償數據匱乏 | 作者結論 | §6–§7, pp. 6–9 | 符合來源 |
| Card 6 | 對個人碩士論文泛泰雅語群研究之映射與啟發 | Wiki 詮釋 | 頁面已標明 | 不適用 |
