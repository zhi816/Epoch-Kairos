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
| Card 1 | 過去方法專精於特定交互作用類型；除一類外各類別均顯著優於專用方法（例外 CASP15 RNA：AF3 47.3、AIchemy_RNA2 54.5） | 正文 p. 493；Extended Data Table 1（PDF p. 21） | 核實符合（2026-11-10 補記：上方 Card 1 列記為已更正，但頁面當時未改，至 2026-11-10 才改寫，EK-101） |
| Card 3 區塊公式 1 | 座標中心化後以 $R$ 旋轉並以 $\vec{t}$ 平移；訓練時另加獨立雜訊 | Supplementary Information Algorithm 19 第 4 行（PDF p. 25）；§3.7.1（PDF p. 28） | 原頁與卡片使用原文未列出的自擬變換式，已改為原文演算法步驟（EK-202）。 |
| Card 3 區塊公式 2 | 擴散損失 $\mathcal{L}_{\text{diffusion}} = (\hat{t}^2 + \sigma_{\text{data}}^2)/(\hat{t} + \sigma_{\text{data}})^2 \cdot (\mathcal{L}_{\text{MSE}} + \alpha_{\text{bond}} \mathcal{L}_{\text{bond}}) + \mathcal{L}_{\text{smooth-LDDT}}$，$\sigma_{\text{data}} = 16$ | Supplementary Information 式 6，SI p. 28 | 核實更正（2026-11-10，EK-105）。原頁之權重只乘均方誤差項，與原式不符，已依原式改寫。 |
| Card 3 區塊公式 3 | 排序分數 $0.8 \cdot \text{ipTM} + 0.2 \cdot \text{pTM} + 0.5 \cdot \text{disorder} - 100 \cdot \text{has\_clash}$；has_clash 為 0 或 1 | Supplementary Information 式 19 與 §5.9.2，SI p. 37；正文 p. 498 | 核實更正（2026-11-10，EK-105）。原頁寫碰撞數 $N_{\text{clash}}$，並稱對無序區施加懲罰（原文為鼓勵溶劑可及面積較高之伸展構型）。 |
| Card 4 | PoseBusters V1 為 428 個 2021 年以後釋出之結構；DiffDock（給定結合態蛋白質結構）37.9%；V2 80.5% | 正文 p. 496；Extended Data Table 1（PDF p. 21） | 核實更正（2026-11-10，EK-102）。原頁寫「DiffDock-L（約 38%）」並歸為盲對接。 |
| Card 4 | 抗體—抗原 62.9%（AF-M 2.3 為 29.6%，N=65），1,000 個種子 | Extended Data Table 1；正文 p. 497 | 核實符合（2026-11-10，頁面由「超過 60%」改為原值） |
| Card 4 | CASP15 RNA 平均高於 RoseTTAFold2NA 與 AIchemy_RNA，不及 AIchemy_RNA2 | 正文 p. 497；Extended Data Table 1 | 核實更正（2026-11-10，EK-103）。原頁「超越所有自動預測伺服器」過度表述；蛋白質—核酸數值同時改為 iLDDT。 |
| Card 5 | 單一框架內對生物分子空間高準確度建模可行；多個隨機種子不能近似溶液構型系綜；E3 泛素連接酶預測為閉合構型 | 摘要 p. 493；模型限制 pp. 497–498 | 核實更正（2026-11-10，EK-107）。原頁稱擴散模型可採樣出完整構型系綜、自然捕捉變構效應，與作者所述限制相反。 |
| Card 4 後續 | Addendum（Nature 636:E4，2024-11-27）宣布釋出推論程式碼；Chai-1（Chai Discovery，bioRxiv 2024-10-11）公開權重與推論程式；Boltz-1（Wohlwend et al.，bioRxiv 2024-11-20）摘要稱達 AF3 等級準確度並以 MIT 授權開源 | Crossref 元資料與摘要；nature.com 附錄全文（2026-11-10 讀取） | 核實更正（2026-11-10，EK-106）。原頁「完整原始碼與訓練權重」與「全面驗證架構可重現性」無出處。 |
