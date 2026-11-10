# 證據表：ai-for-structural-biology
- **概念頁面**：[wiki/concepts/ai-for-structural-biology.md](../concepts/ai-for-structural-biology.md)
- **查核者**：Antigravity by Google DeepMind，2026-11-09

| 位置 | 主張／陳述 | 類型 | 第一手來源與精確位置 | 核驗結果與說明 |
|---|---|---|---|---|
| 關鍵突破支柱 | CRISPR-Cas9（2012）結構與雙結構域構型機制 | 奠基論文成果 | Jinek et al. (2012) *Science* 337:816–821 | 符合來源。為 AI 輔助緊湊編輯酶工程提供結構標的。 |
| 關鍵突破支柱 | 自注意力機制應用於蛋白質共演化建模（2017） | 演算法與架構啟發 | Vaswani et al. (2017) *NeurIPS 30*; Marks et al. (2012) *Nat Biotechnol* 30:1072–1080 | 符合來源。多頭注意力架構為長程殘基共突變關聯提供先驗。 |
| 關鍵突破支柱 | AlphaFold2（2021）蛋白質結構預測原子級精度 | 奠基論文成果 | Jumper et al. (2021) *Nature* 596:583–589 | 符合來源。Evoformer 與 IPA 達成 $0.96\,\text{\AA}$ 原子級精度。 |
| 關鍵突破支柱 | DrugCLIP（2023）三維對比學習超高速虛擬藥物篩選 | 奠基論文方法與效能 | Gao et al. (2023) *NeurIPS 36*, §4.3 (p. 8) | 符合來源。共享嵌入空間與 HomoAug 使篩選速度提升數個數量級。 |
| 關鍵突破支柱 | AlphaFold 3（2024）全生物分子複合體擴散統一模型 | 奠基論文成果 | Abramson et al. (2024) *Nature* 630:493–500 | 符合來源。Pairformer 與擴散模組預測各類生物分子相互作用。 |
| 跨學科交會 | DrugCLIP 單靶點檢索時間與前置條件 | 本篇研究結果 | [Gao et al. (2023)](https://proceedings.neurips.cc/paper_files/paper/2023/file/8bd31288ad8e9a31d519fdeede7ee47d-Paper-Conference.pdf) §4.3, p. 8 | 對預先編碼並存於記憶體的 60 億分子，原文同句寫少於 10,000 秒與約 30 小時；前者換算小於約 2.78 小時，兩者矛盾，不能擇一當作確定實測時間（EK-052）。 |
| 跨學科交會 | DrugCLIP 全基因組尺度後續篩選 | 後續研究 | [Jia et al. (2026)](https://doi.org/10.1126/science.ads9530), §Genome-wide virtual screening with DrugCLIP, 6 of 14 | 約一萬個人類蛋白質、五億個化合物，超過十兆次蛋白質—配體評分約 24 小時，以單一節點八張 A100 執行；後續另做聚類與分子對接（EK-052）。 |
| 跨學科交會 | AlphaFold 3 與自由能微擾（FEP）的可能串接 | Wiki 詮釋 | Abramson et al. (2024), *Nature* 630:493–500；Wang et al. (2015), *JACS* 137:2695–2703 | 將結構預測與 FEP 串接是 Wiki 提案；所列來源分別支持各自方法，不證明本組合已有成熟或高精度精排管線（EK-053）。 |
