# 證據表：2026-cross-lingual-alignment-moe-routers-bandarkar
- **採用版本**：*arXiv:2610.01921*（2026-10-01，25 頁全文）；封存於 `raw/my-focus/報告論文題材/2026-cross-lingual-alignment-moe-routers-bandarkar.pdf`。
- **查核者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Frontmatter | 題名 *Cross-Lingual Alignment for Decoder-Only Models using MoE Routers*；作者 Lucas Bandarkar, Clark Peng, Ahmed Haj Ahmed, Aditi Khandelwal, Nanyun Peng（UCLA、Haverford College、MILA & McGill）；arXiv:2610.01921（2026-10-01） | 本篇研究基本資訊 | p. 1 標題與署名；arXiv metadata (`https://arxiv.org/abs/2610.01921`) | 符合來源 |
| Card 1 | 解碼器大語言模型缺乏序列級表徵且多語分詞粒度差異大，難以直接套用詞元對應或隱狀態對比學習；但在中間層已隱含跨語言共用表徵 | 本篇研究動機 | 摘要 p. 1；§1 p. 2 | 符合來源 |
| Card 1 | 提出在持續預訓練（CPT）期間對中間層 MoE 路由器經序列平均池化之權重施加 KL 散度輔助損失；在 4 個開源 MoE 模型與 7 種語言共 14 組設定上試驗 | 本篇核心主張 | 摘要 p. 1；§1 p. 2；§4.1 p. 4 | 符合來源 |
| Card 2 | 傳統編碼器（如序列對序列模型）具自然序列級嵌入可作對比學習，而解碼器模型僅有末詞元或平均隱狀態；平均高維隱狀態向量容易相互抵銷或衰減詞元特徵，且 Liu & Niehues (2025) 須對隱狀態作餘弦相似度對齊 | 既有方法限制 | §1 p. 2；§2.1–§2.3 pp. 2–3 | 符合來源 |
| Card 2 | 基線表 2（Marco-Nano）顯示隱狀態餘弦對齊 $\mathcal{L}_{XLH}$ 在匈牙利語從基線 37.4 降至 36.9，在僧伽羅語僅升至 26.3（低於路由對齊 26.8） | 本篇實驗對照 | §5.2 p. 7；Table 2 p. 8 | 符合來源 |
| Card 3 | 式 (1)：$\mathcal{L}_{XLR} = \frac{1}{\|\mathcal{M}\|} \sum_{l \in \mathcal{M}} D_{\mathrm{KL}}(\bar{\boldsymbol{p}}_{\mathrm{eng}, l} \parallel \bar{\boldsymbol{p}}_{\mathrm{tgt}, l})$，其中 $\bar{\boldsymbol{p}} = \frac{1}{T}\sum_{t=1}^{T}\boldsymbol{p}^t$ 且 $\boldsymbol{p}_{\mathrm{lang}, l}^t = \mathrm{G}(\boldsymbol{z}_{\mathrm{lang}, l}^t)$ | 區塊公式 1 | §3.2 p. 4 式 (1) | 符合來源 |
| Card 3 | 總目標函數 $\mathcal{L} = \mathcal{L}_{LM} + \alpha \cdot \mathcal{L}_{XLR}$，梯度僅經由目標語序列反向傳播，英語序列僅作對齊參考不接收梯度更新 | 區塊公式 2 與設計 | §3.2 p. 4 | 符合來源 |
| Card 3 | 依 Bandarkar et al. (2026c) 路由發散曲線預先選定各模型之中間層集合 $\mathcal{M}$（Qwen3-30B-A3B 7–34 層、GPT-OSS-20B 4–17 層、Marco-Nano 7–19 層、Granite-4.0-H-Tiny 10–35 層）；採不填補共享打包前向傳播，來源序列於 $\mathcal{M}$ 末層提前結束 | 演算法細節與最佳化 | §3.1 p. 3；§3.3 p. 4；Appendix C–D pp. 23–24 Table 7 | 符合來源 |
| Card 4 | 四個模型為 Qwen3-30B-A3B（31B 總參 / A3B 啟動、48 層、8/128 專家）、GPT-OSS-20B（22B / A4B、24 層、4/32）、Marco-Nano（8B / A0.6B、28 層、8/238）、Granite-4.0-H-Tiny（7B / 1B、40 層、6/64） | 本篇實驗架構 | §4.1 p. 4；Table 7 p. 24 | 符合來源 |
| Card 4 | 7 種目標語言與平行訓練規模：每種語言 200,000 筆訓練樣本與 1,000 筆驗證樣本（1 個 epoch、有效批次大小 32）；較大模型測泰盧固語（8 項任務）、吉爾吉斯語（4）、康納達語（4）、泰語（7），較小模型測越南語（9）、僧伽羅語（5）、匈牙利語（6） | 本篇實驗規模 | §4.1 pp. 4–5；Appendix E–F pp. 24–25 | 符合來源 |
| Card 4 | 下游評測整體結果：在 14 組模型—語言對中，加入路由對齊損失在 13 組優於純 LM 持續預訓練基線、1 組平手（Marco-Nano 越南語 45.6 vs. 45.6），平均分數最高提升 2.1 分（Qwen3-30B-A3B 吉爾吉斯語 43.5 $\to$ 45.6），14 組平均提升 0.9 分 | 本篇主要數據 | §5.2 p. 7；Table 1 p. 8；Tables 3–6 pp. 20–23 | 符合來源 |
| Card 4 | Table 1 與 Table 2 逐項分數：Qwen3-30B-A3B 泰盧固語 45.4$\to$46.3、吉爾吉斯語 43.5$\to$45.6、康納達語 49.6$\to$51.4、泰語 44.9$\to$45.4；GPT-OSS-20B 泰盧固語 46.5$\to$47.0、吉爾吉斯語 42.0$\to$43.8、康納達語 55.5$\to$56.4、泰語 39.9$\to$40.8；Granite 越南語 36.5$\to$36.8、僧伽羅語 32.8$\to$32.9、匈牙利語 38.1$\to$38.8；Marco-Nano 越南語 45.6$\to$45.6、僧伽羅語 26.1$\to$26.8（隱狀態 26.3）、匈牙利語 37.4$\to$38.1（隱狀態 36.9） | 本篇表格精確數據 | Table 1 p. 8；Table 2 p. 8 | 符合來源 |
| Card 4 | 僅訓練路由器（更新小於 0.1% 參數）表現不穩定且整體遜於全參數搭配路由損失；內部表徵檢驗顯示路由損失同時降低中間層路由發散並提高 Qwen3-30B-A3B 的 SoftCKA 隱狀態跨語言相似度 | 本篇機制驗證 | §5.1–§5.2 pp. 6–7；Fig. 1 p. 1；Fig. 3–4 pp. 6–7 | 符合來源 |
| Card 5 | 公開程式碼與研究限制：程式碼公開於 `https://github.com/lucasbandarkar/xl_moe_alignment`；作者明列實驗受限於已後訓練檢查點上的 200k 短程 CPT、仰賴句級平行語料且未驗證預訓練階段與無負樣本對負載平衡之交互影響；在推論／數學任務上亦未明確確立優於翻譯與閱讀理解之幅度差異 | 本篇限制、公開資源與未來工作 | §6 pp. 8–9；Code Availability p. 10 | 符合來源 |
| Card 6 | 對低資源機器翻譯與多語大語言模型研究方向之跨領域啟發（不涉及未公開碩論設計） | Wiki 詮釋 | 頁面已標明 | 不適用 |
