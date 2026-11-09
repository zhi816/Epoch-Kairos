# 證據表：2023-drugclip

本表記錄 [wiki/papers/2023-drugclip.md](../papers/2023-drugclip.md) 各項主張在第一手文獻中的出處與核驗結果。

- **主要第一手來源**：Gao, B., Qiang, B., Tan, H., Jia, Y., Ren, M., Lu, M., Liu, J., Ma, W.-Y., & Lan, Y. (2023). DrugCLIP: Contrastive Protein-Molecule Representation Learning for Virtual Screening. *Advances in Neural Information Processing Systems (NeurIPS)*, 36, 44595–44614. [arXiv:2310.06367](https://arxiv.org/abs/2310.06367)
- **封存原文**：`raw/2023-drugclip.pdf`

---

| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |
|---|---|---|---|
| Card 1 | 將虛擬篩選重構為密集檢索，預先離線編碼，速度提升超過 $10^5$ 倍 | §1–§2 (p. 2), §3.4 (p. 5), §4.3 (p. 8) | 核實符合。傳統對接 100 億分子需約 3,000 CPU 年，DrugCLIP 離線預編碼後僅需向量內積。 |
| Card 3 | 雙塔 SE(3) 不變性幾何編碼器與 InfoNCE 損失 | §3.2 (pp. 3–4), §3.3 (pp. 4–5), Eq. (1)–(5) | 核實符合。以 Uni-Mol 為基礎架構，利用原子間歐氏距離偏置更新，對全域剛體旋轉平移不變。 |
| Card 3 | HomoAug 流程：Jackhmmer 搜尋 AlphaFold DB、TMalign 結構比對與篩選 | Appendix B.1 (pp. 14–15) | 核實更正。使用 Jackhmmer 於 AlphaFold DB（8,449,772 條序列聚類庫）搜尋，以 TMalign 比對（TM-score $\ge 0.4$、口袋對齊率 $\ge 40\%$），擷取配體 $6\,\text{Å}$ 範圍殘基，擴增出 758,107 個口袋—配體對；原文未使用 Pfam。 |
| Card 3 | 訓練期 RDKit 構型生成以克服訓練—測試不一致 | §3.4 (p. 6), Appendix A (p. 14) | 核實更正。RDKit 構型用於訓練期作為帶噪聲輸入 $c_m + \delta$，使模型學習非結合態向結合態之映射；推論期直接對分子單一嵌入做點積／餘弦檢索，原文無測試期取 K 構型最大值式。 |
| Card 3, Card 4 | 檢索速度：Enamine 60 億分子庫檢索耗時小於 10,000 秒 | §4.3 (p. 8) | 核實更正。預編碼後 60 億分子庫篩選耗時小於 10,000 秒（約 2.78 小時；原文括號誤註為約 30 小時）；非「毫秒內完成全庫 60 億分子檢索」。 |
| Card 4 | DUD-E 零樣本基準：$\text{EF}_{1\%} = 31.89$、$\text{AUROC} = 80.93\%$、$\text{BEDROC} = 50.52\%$ | Table 1 (p. 7) | 核實更正。原文 Table 1 載明 DrugCLIP_ZS 之 $\text{EF}_{0.5\%}=38.07$、$\text{EF}_{1\%}=31.89$、$\text{EF}_{5\%}=10.66$、AUROC 80.93%、BEDROC 50.52%。修正先前誤植之 28.54 / 84.74% / 47.41%。 |
| Card 4 | LIT-PCBA 基準：$\text{EF}_{1\%} = 5.51$、$\text{BEDROC} = 6.23\%$、$\text{AUROC} = 57.17\%$ | Table 3 (p. 8) | 核實更正。原文 Table 3 載明 DrugCLIP 之 $\text{EF}_{0.5\%}=8.56$、$\text{EF}_{1\%}=5.51$、$\text{EF}_{5\%}=2.27$、AUROC 57.17%、BEDROC 6.23%。更正先前將 10.66%（DUD-E EF@5%）錯標為 LIT-PCBA BEDROC 之問題。 |
| Card 4 | HomoAug 消融驗證：DUD-E 上 BEDROC 從 45.81% 提升至 50.52%，EF 1% 從 29.12 提升至 31.89 | Table 5 (p. 9) | 核實更正。Table 5 顯示加入 HomoAug 使 DUD-E BEDROC 由 45.81% 升至 50.52%，EF@1% 由 29.12 升至 31.89。刪除非原文表格之「LIT-PCBA 4.21 到 5.51」陳述。 |
| Card 4 | 專家雙盲評估：ChemDiv 庫 5 個靶點中 4 個傾向選擇 DrugCLIP | §4.5 (p. 9), Table 8 (p. 19) | 核實符合。五個靶點中專家偏好 DrugCLIP 比例在四個靶點高於 Glide（Table 8）。 |
