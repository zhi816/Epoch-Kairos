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
| 跨學科交會 | DrugCLIP 檢索速度與全基因組篩選規模 | 實證數據核校 | Gao et al. (2023) §4.3 (p. 8); GenomeScreenDB (bioRxiv 2024) | 核實更正。更正 DrugCLIP 單靶點 60 億 Enamine 分子檢索耗時為小於 10,000 秒（約 2.78 小時），刪除「數秒內完成百億級初篩」之誇大陳述，並客觀交代 GPU 叢集一日內完成全基因組尺度篩選之實況（關閉 EK-052）。 |
| 跨學科交會 | AlphaFold 3 與自由能微擾（FEP）誘導契合精排管線狀態 | 前沿技術整合展望 | Abramson et al. (2024); Wang et al. (2015) *JACS* 137:2695–2703 | 核實更正。明確指出 AF3 本文為靜態複合體結構預測基準，其與熱力學 FEP 物理計算結合為計算生物學界正在探索的前沿整合策略，刪除寫成已實證成熟管線之陳述（關閉 EK-053）。 |
