# 證據表：2024-alphafold3

本表記錄 [wiki/papers/2024-alphafold3.md](../papers/2024-alphafold3.md) 各項主張在第一手文獻中的出處與核驗結果。

- **主要第一手來源**：Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L. et al., Jaderberg, M., Hassabis, D., & Jumper, J. M. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*, 630(8016), 493–500. DOI: [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w)
- **封存原文**：`raw/2024-alphafold3.pdf`

---

| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |
|---|---|---|---|
| Card 1 | 擴展至全生物分子複合物結構預測，優於許多既有領域專用工具 | 摘要 (p. 493), 正文 (p. 493) | 核實更正。原文載明「除一項外在所有類別均顯著超越專用工具」（CASP15 RNA 評估中含專家介入之 AIchemy_RNA2 為 54.5 LDDT，高於 AF3 之 47.3）。更正 Card 1「全面擊敗所有領域專用工具」之絕對化表述。 |
| Card 3 | Pairformer 主幹（48 層）與全原子擴散去噪模組架構 | §Network architecture (pp. 494–496), Fig. 1d, Fig. 2 | 核實符合。拋棄胺基酸剛體框架與內部 SE(3) 等變層，以全原子座標為去噪目標，搭配資料旋轉平移增強。 |
| Card 4 | 蛋白質—小分子配體（PoseBusters V1）盲測成功率達 $76.4\%$ | §Accuracy across complex types (p. 496), Fig. 1c, Extended Data Table 1 (p. 21) | 核實符合。PoseBusters V1（428 個靶點，$2019$ 年截止）之配體重原子 $\text{r.m.s.d.} < 2.0\,\text{\AA}$ 成功率為 $76.4\%$（Vina 為 $52.3\%$，RoseTTAFold All-Atom 為 $42.0\%$）。 |
| Card 4 | 蛋白質—核酸複合體介面精度：雙股 DNA iLDDT 達 64.8、RNA iLDDT 達 39.4 | Fig. 1c (p. 494), Extended Data Table 1 (p. 21) | 核實更正。原文在蛋白質—雙股 DNA（$N=38$）上報告之平均介面 LDDT（iLDDT）為 **$64.8$**（RoseTTAFold2NA 為 $28.3$）；蛋白質—RNA（$N=25$）iLDDT 為 **$39.4$**（RoseTTAFold2NA 為 $19.0$）。更正原頁面將 iLDDT 分數誤寫為百分比「成功率」之混淆。 |
| Card 4 | 抗體—抗原介面預測成功率（$\text{DockQ} > 0.23$）達 $62.9\%$ | Fig. 1c (p. 494), Fig. 5a (p. 499), Extended Data Table 1 (p. 21) | 核實符合。在 1,000 個 Seeds 採樣排序下，抗體—抗原成功率達到 $62.9\%$（AlphaFold-Multimer v2.3 為 $29.6\%$）。 |
| Card 4 | 共價修飾與糖基化預測精度數值歸屬 | §Covalent modifications (p. 497), Extended Data Table 1 (p. 21) | 核實更正。共價結合配體成功率為 **$78.5\%$**（$N=66$）；高質量單殘基糖基化為 **$72.1\%$**（$N=28$），多殘基多醣鏈（Multi-residue Glycans）在全部質量數據上成功率為 **$42.4\%$**（正文載為 $42.1\%$，$N=131$）；修飾殘基總體為 **$59.9\%$**（蛋白質修飾殘基為 $51.0\%$、DNA 修飾為 $68.6\%$、RNA 修飾為 $40.9\%$）。糾正將 $72.1\%$ 錯標為複雜多醣鏈之歸屬錯誤。 |
