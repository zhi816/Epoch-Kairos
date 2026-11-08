---
title: "AI for Structural Biology & Molecular Design"
title_zh: "AI 驅動之結構生物學與分子設計"
domain: "ai"
domain_tags: ["#計算生物", "#人工智慧", "#結構生物學", "#生物科技"]
papers: ["2012-crispr-cas9", "2017-attention-is-all-you-need", "2021-alphafold2", "2023-drugclip", "2024-alphafold3"]
related_concepts: ["generative-world-models", "programmable-cellular-engineering"]
verification: "issues"
---

# 概念：AI 驅動之結構生物學與分子設計 (AI for Structural Biology & Molecular Design)

> 領域：`#計算生物` `#人工智慧` `#結構生物學` `#生物科技`

---

## 核心定義
**AI 驅動之結構生物學與分子設計** 結合深度幾何注意力網路、三維等變表徵、生成式擴散模型與對比學習，旨在直接從一維生物序列（胺基酸、DNA、RNA）與化學分子拓撲預測原子級三維複合體結構，並逆向在百億級化學空間與全新蛋白質序列空間中檢索或從頭設計具特定催化、結合與調控功能的生物分子。

---

## 關鍵突破支柱
* **可編程基因編輯酶之結構與功能基礎（2012）**：CRISPR-Cas9 雙結構域（HNH 與 RuvC）受單鏈引導 RNA（sgRNA）構型重組控制之分子機制，成為當代 AI 輔助新型緊湊基因編輯酶（如 OpenCRISPR）挖掘與工程設計的核心標的。
  * 詳見核心論文：[CRISPR-Cas9 基因剪刀誕生（2012 發表 ｜ 2020 諾貝爾化學獎）](../papers/2012-crispr-cas9.md)
* **自注意力機制與序列共演化建模（2017）**：Transformer 的多頭自注意力直接啟發了對多重序列比對（MSA）中長程胺基酸共突變關係的精準捕捉。
  * 詳見核心論文：[Attention Is All You Need（2017 發表）](../papers/2017-attention-is-all-you-need.md)
* **AlphaFold2 破解單鏈與多聚體蛋白質摺疊（2021）**：以 Evoformer 三角形幾何更新與 $\mathrm{SE}(3)$ 等變不變點注意力（IPA）達到 $0.96\,\text{\AA}$ 原子級精度，釋出逾兩億個預測蛋白質結構。
  * 詳見核心論文：[AlphaFold2 與蛋白質結構預測（2021 發表 ｜ 2024 諾貝爾化學獎）](../papers/2021-alphafold2.md)
* **DrugCLIP 三維對比學習超高速虛擬篩選（2023）**：將蛋白質口袋與小分子映射至共享三維幾何嵌入空間，並利用 AlphaFold 結構庫進行同源演化資料增強（HomoAug），使十億級化合物庫篩選速度較物理對接提升逾十萬倍。
  * 詳見核心論文：[DrugCLIP 對比學習虛擬藥物篩選（2023 發表）](../papers/2023-drugclip.md)
* **AlphaFold 3 全生物分子擴散統一模型（2024）**：以 Pairformer 與全原子擴散生成模組統一預測蛋白質、DNA、RNA、小分子配體、共價修飾與離子之交互作用，在盲對接基準達 $76.4\%$ 成功率。
  * 詳見核心論文：[AlphaFold 3（2024 發表）](../papers/2024-alphafold3.md)

---

## 跨學科交會與延伸
1. **「結構預測 $\to$ 超高速檢索 $\to$ 從頭生成」的數位生物學閉環**：
   * AlphaFold2/3 提供全蛋白質組與核酸複合物的高精度靶點口袋；DrugCLIP 在數秒內完成百億級小分子初篩；AlphaFold 3 與自由能微擾（FEP）再對命中分子進行全原子誘導契合精排，徹底改寫新藥研發管線。
2. **從「讀懂自然界蛋白質」到「創造自然界未曾演化的蛋白質」**：
   * 結合結構擴散與逆向摺疊（如 David Baker 團隊之 RFdiffusion 與 ProteinMPNN），人類已能定制高親和力迷你結合蛋白、人工酶與全新基因編輯器。

---

## 關聯概念網絡
* [生成式世界模型與擴展定律](generative-world-models.md)
* [可編程細胞與基因工程](programmable-cellular-engineering.md)
