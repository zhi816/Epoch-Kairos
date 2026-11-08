# 內容問題清單（Issues）

> 本檔登記查核發現之待修正事項，格式與狀態規則見 [AGENTS.md](../AGENTS.md) 第七章第 4 節。標題五段依序為：編號、狀態（`open` / `fixed` / `wontfix`）、相對於 `wiki/` 之檔案、位置、判定。修正時就地改狀態並追加「處理」行，不得刪除條目。
>
> EK-001 至 EK-056 係於 2026-11-09 自 [wiki/log.md](log.md) 2026-11-08 21:40 至 23:36 之 audit 條目逐筆轉錄（原查核者均為 Codex by OpenAI，EK-031 例外），問題描述與來源沿用原條目，轉錄時未重新核對原文。修正前須依 `wiki-content-audit` 回原文確認，不得只照本檔描述改寫。EK-057 至 EK-060 為轉錄同日以 `crossref_check.py` 查得之 DOI 問題。

---

## 1982 Hopfield 網路

### EK-001 | open | papers/1982-hopfield-network.md | Card 3 | 過度表述
- **問題**：把所有局部能量極小值等同預先寫入的記憶吸引子。原文指出零閾值下全零狀態亦為穩定態，高能穩定態不必是儲存記憶；p. 5 隨機初態模擬（N=30、n=5）約 85% 落入已指定記憶、10% 落入無明顯意義之穩定態、5% 落在記憶附近。
- **來源**：[封存原文](../raw/1982-hopfield-network.pdf)，PNAS 79:2554–2558
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 23:36] audit

### EK-002 | open | papers/1982-hopfield-network.md | Card 4 | 原文不符
- **問題**：寫作「隨機正交型態」並稱 N=100 可穩定檢索 15 個完整記憶。原文稱隨機型態具 pseudoorthogonality，容量約 0.15N 是誤差變嚴重前之近似容量，不保證完整無誤檢索。另「隨機切除相當比例突觸或損毀神經元仍可正確重建」在原文無定量結果，須降格或另引直接實驗。
- **來源**：[封存原文](../raw/1982-hopfield-network.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit、[2026-11-08 23:36] audit

## 1992 Aghion–Howitt 創造性破壞

### EK-003 | open | papers/1992-creative-destruction-aghion.md | Card 4 | 過度表述
- **問題**：成長率與變異數公式以線性研發技術 φ(n)=n 為條件，卡片未明示；原文只說某些條件下存在週期均衡，頁面稱可解釋實際商業週期，強於原文。
- **來源**：[Aghion & Howitt 原文（Econometrica 60(2), 1992）](https://web.econ.ku.dk/dalgaard/growth/growth07/AghionHowitt.pdf)
- **發現於**：wiki/log.md [2026-11-08 23:36] audit

### EK-004 | open | papers/1992-creative-destruction-aghion.md | Card 5 | 原文未支持
- **問題**：把 1992 模型直接連到現代反壟斷標準與 Killer Acquisitions；屬後續政策延伸，須另引研究並標明非本文結果。Card 6 若有同類政策結論亦同。
- **來源**：同 EK-003
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit

## 2001 Acemoglu–Johnson–Robinson 殖民起源

### EK-005 | open | papers/2001-colonial-origins-acemoglu.md | Card 4 | 原文不符
- **問題**：Table 3 第一階段係數原文為 −0.61（SE 0.13），頁面寫 −0.60；制度指標原文為 0–10 分，頁面寫 1–10；奈及利亞與智利差距原文表述為「至多約 7 倍」並提醒測量誤差，頁面之 8.2 倍須標為依四捨五入值計算；穩健性估計不宜概括為單一 0.7–1.0 範圍。
- **來源**：[原文（AER 91(5), 2001）](https://economics.mit.edu/sites/default/files/publications/colonial-origins-of-comparative-development.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit

### EK-006 | open | papers/2001-colonial-origins-acemoglu.md | Card 3 | 過度表述
- **問題**：把疾病免疫機制寫成支撐排他性限制之既定事實。原文 pp. 1371–1372 將排他性列為識別假設，並把當代疾病直接影響列為主要疑慮；免疫差異是作者論證假設合理性的依據。
- **來源**：同 EK-005
- **發現於**：wiki/log.md [2026-11-08 23:36] audit

### EK-007 | open | papers/2001-colonial-origins-acemoglu.md | Card 5 | 原文未支持
- **問題**：外援與基建必然遭攫取之結論不屬 AJR 2001 實證檢驗，應補直接研究或標為政策推論。
- **來源**：同 EK-005
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit

## 2007 Woodford 通膨動態

### EK-008 | open | papers/2007-woodford-inflation-dynamics.md | Card 1 | 過度表述
- **問題**：「嚴格證明決定權毫不動搖」強於原文摘要「全球化不太可能削弱央行控制通膨的能力」。
- **來源**：[原文（NBER WP 13329）](https://www.nber.org/system/files/working_papers/w13329/w13329.pdf)
- **發現於**：wiki/log.md [2026-11-08 23:36] audit

### EK-009 | open | papers/2007-woodford-inflation-dynamics.md | Card 3 | 原文未支持
- **問題**：稱短期利率由準備金付息與供給條件決定，並列出未標號之 IS、NKPC 與廣義確定性公式。原文 p. 36 明說以 Taylor rule 表示政策、未建模央行如何實施操作利率；另行推導之標準式不得標為本文原式。
- **來源**：[封存原文](../raw/2007-woodford-inflation-dynamics.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-010 | open | papers/2007-woodford-inflation-dynamics.md | Card 4 | 原文不符
- **問題**：「本國利率傳導因開放而增強」與原文結論不符，原文指出國內通膨之政策效果不依賴進口份額參數；所列 β=0.99、σ=1、γ=0.2、κ=0.024 校準在原文找不到對應表或頁碼；把任何外國衝擊說成可完全隔絕亦過度概括。
- **來源**：同 EK-008
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 23:36] audit

### EK-011 | open | papers/2007-woodford-inflation-dynamics.md | Card 5 | 歸因／版本錯置
- **問題**：點陣圖效果、終結貨幣主義及全球合作最優結論屬後續應用或綜合詮釋，被寫成本篇直接研究結果。
- **來源**：同 EK-008
- **發現於**：wiki/log.md [2026-11-08 22:35] audit、[2026-11-08 23:36] audit

## 2012 CRISPR-Cas9

### EK-012 | open | papers/2012-crispr-cas9.md | Card 1 | 過度表述
- **問題**：寫更換 20 nt 即可「靶向任意基因」，省略 S. pyogenes Cas9 所需之 NGG PAM。
- **來源**：[封存原文](../raw/2012-crispr-cas9.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

### EK-013 | open | papers/2012-crispr-cas9.md | Card 4 | 原文不符
- **問題**：把 PAM 近端錯配效應寫成單一錯配即可完全廢除切割，與原文對連續配對需求及遠端錯配容忍度之結果不符。
- **來源**：[原文](https://doi.org/10.1126/science.1225829)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-014 | open | papers/2012-crispr-cas9.md | Card 3 | 原文未支持
- **問題**：R-loop 自由能、切割速率常數與 K_d 等符號模型未見於原文，卻呈現為本文模型；可保留為教學推導，但須標明推導者、假設與來源。
- **來源**：[封存原文](../raw/2012-crispr-cas9.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-015 | open | papers/2012-crispr-cas9.md | Card 5 | 歸因／版本錯置
- **問題**：把 dCas9、nCas9 及鹼基／先導編輯工具家族寫成本篇建立；2012 原文報告的是雙 RNA 引導與嵌合單 RNA 切割，dCas9 調控平台見 2013 年後續研究。
- **來源**：[封存原文](../raw/2012-crispr-cas9.pdf)、[Qi et al. 2013](https://doi.org/10.1016/j.cell.2013.02.022)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2013 IceCube 高能微中子

### EK-016 | open | papers/2013-icecube-neutrino.md | Card 4 | 原文未支持
- **問題**：「高能端分析 4.3σ、p≈1.5×10⁻⁵」在原文找不到。原文報告為 26 個新事件 3.3σ、預先指定分析合併 28 個事件 4.1σ、事後計算全 28 事件 4.8σ，較高 charm 背景下分別降為 3.6σ 與 4.5σ。
- **來源**：[原文](https://arxiv.org/abs/1311.5238)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit

### EK-017 | open | papers/2013-icecube-neutrino.md | Card 3 | 原文不符
- **問題**：99.999% 在原文是 6000 p.e. 門檻以上大氣緲子背景之拒斥率，頁面擴寫為同時濾除大氣微中子；原文仍估計約 6.1 個大氣微中子事件與 6.0 ± 3.4 個穿透緲子事件。
- **來源**：[封存原文](../raw/2013-icecube-neutrino.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

## 2017 Transformer

### EK-018 | open | papers/2017-attention-is-all-you-need.md | Card 4 | 歸因／版本錯置
- **問題**：41.8 BLEU 符合 arXiv 版，NeurIPS 定稿 PDF 報 41.0（官方摘要頁 41.1）；頁面同時標 NeurIPS venue 與 arXiv 連結，須註明採用版本。
- **來源**：[NeurIPS 定稿 PDF](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit

### EK-019 | open | papers/2017-attention-is-all-you-need.md | Card 5 | 原文不符
- **問題**：稱原始 Transformer 訓練「完美契合 Tensor Cores」；原文使用 8 張 P100（Pascal），首代 Tensor Cores 出現於 Volta。
- **來源**：[NeurIPS 原文](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need.pdf)、[NVIDIA Volta 白皮書](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-product-literature/volta-architecture-whitepaper.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

### EK-020 | open | papers/2017-attention-is-all-you-need.md | Card 6 | 過度表述
- **問題**：「拿掉歸納偏置」過於絕對；原模型仍使用位置編碼與遮罩等結構先驗。
- **來源**：同 EK-019
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2021 AlphaFold2

### EK-021 | open | papers/2021-alphafold2.md | Card 4 | 歸因／版本錯置
- **問題**：r=0.73 出自 Tunyasuvunakool et al. 人類蛋白質組伴篇；Jumper et al. 主論文 Figure 2c 在另一組測試鏈報 r=0.76。須標明出處。
- **來源**：[主論文](https://www.nature.com/articles/s41586-021-03819-2)、[伴篇](https://www.nature.com/articles/s41586-021-03828-1)
- **發現於**：wiki/log.md [2026-11-08 21:46] audit

### EK-022 | open | papers/2021-alphafold2.md | Card 3 | 過度表述
- **問題**：原文說三角更新受三角不等式「啟發」，頁面寫成「強制滿足」歐氏三角幾何；並把 IPA 注意力值之不變性與其後座標更新之等變性混稱。
- **來源**：[封存原文](../raw/2021-alphafold2.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-023 | open | papers/2021-alphafold2.md | Card 5 | 歸因／版本錯置
- **問題**：把核孔複合體結構寫成直接套用 AF2 預測；後續研究是以 AlphaFold 模型結合 cryo-EM 等實驗資料做整合建模。
- **來源**：[封存主論文](../raw/2021-alphafold2.pdf)、[NPC 整合建模研究](https://pubmed.ncbi.nlm.nih.gov/35679401/)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2023 DrugCLIP

### EK-024 | open | papers/2023-drugclip.md | Card 4 | 原文不符
- **問題**：DUD-E 與 LIT-PCBA 之 EF、AUROC、BEDROC 數值與指標歸屬與原文表格不一致；10.66 被錯標為 LIT-PCBA BEDROC，原文該值屬 DUD-E EF@5%；HomoAug 之 LIT-PCBA 4.21 → 5.51 消融敘述未見於原文表格。
- **來源**：[原文](https://www.proceedings.com/content/075/075280-1932open.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-025 | open | papers/2023-drugclip.md | Card 3 | 原文不符
- **問題**：寫「十億個分子全庫檢索在毫秒內完成」；原文 Section 4.3 報告 6 billion Enamine 分子檢索耗時少於 10,000 秒（約 2.78 小時；原文括號之「30 小時」與其秒數不符，見 22:44 勘誤）。
- **來源**：[封存原文](../raw/2023-drugclip.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:00] audit、[2026-11-08 22:44] audit

### EK-026 | open | papers/2023-drugclip.md | Card 3 | 原文未支持
- **問題**：test-time 取 K 個構型最大相似度未見於原文方法（RDKit 構型主要用於訓練期噪聲輸入與消融）；HomoAug 實際流程為同源序列搜尋、AlphaFold DB、TM-align 與相似度篩選，頁面所寫 Pfam 未獲支持。
- **來源**：同 EK-025
- **發現於**：wiki/log.md [2026-11-08 22:00] audit

## 2023 JWST 大質量星系

### EK-027 | open | papers/2023-jwst-massive-galaxies.md | Card 4 | 原文不符
- **問題**：將 ε≈0.57 指派至 z≈7.5；原文此值對應 z≈9.1 之 1σ 邊際一致性，z≈7.5 中心估計約 0.84。「觀測密度為理論上限 2–5 倍」亦超出原文結論。
- **來源**：[原文](https://www.nature.com/articles/s41550-023-01937-7.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-028 | open | papers/2023-jwst-massive-galaxies.md | Card 3 | 歸因／版本錯置
- **問題**：主計算採 Sheth–Tormen 暈質量函數，後文卻附 Press–Schechter erfc 解析式；須明示 PS 為補充近似，非 Boylan-Kolchin 論文所用之 HMF。
- **來源**：[封存原文](../raw/2023-jwst-massive-galaxies.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:00] audit

## 2024 AlphaFold 3

### EK-029 | open | papers/2024-alphafold3.md | Card 4 | 歸因／版本錯置
- **問題**：將介面 LDDT 標成成功率；複雜多醣鏈 72.1% 之歸屬未獲主文支持。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-030 | open | papers/2024-alphafold3.md | Card 1 | 過度表述
- **問題**：「全面擊敗所有領域專用工具」強於原文「優於許多既有專用工具」；原文按任務與基準分別比較。
- **來源**：[封存原文](../raw/2024-alphafold3.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2024 可容錯量子處理器

### EK-032 | open | papers/2024-fault-tolerant-quantum.md | Card 4 | 原文不符
- **問題**：把「40 個 color-code qubits」混寫成「40 個橫向邏輯 CNOT 閘」，混淆量子位元數與閘數；另須與以 3D [[8,3,2]] code blocks 執行之 48 邏輯量子位元取樣電路分開敘述。
- **來源**：[原文](https://arxiv.org/abs/2312.03982)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit

### EK-033 | open | papers/2024-fault-tolerant-quantum.md | Card 1 | 原文不符
- **問題**：將中性 87Rb 原子寫成「帶電」搬運；原文為 neutral-atom 陣列。
- **來源**：[封存原文](../raw/2024-fault-tolerant-quantum.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

### EK-034 | open | papers/2024-fault-tolerant-quantum.md | Card 5 | 原文不符
- **問題**：把 qLDPC 說成已由本實驗實作；原文只把 qLDPC 列為未來降低開銷之方向。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2024 Sora

### EK-035 | open | papers/2024-sora-world-simulator.md | Card 3 | 原文未支持
- **問題**：把 VAE 具體架構、3D RoPE、adaLN-Zero 與 epsilon-prediction 當作 Sora 已知實作。OpenAI 報告未提供實作細節，並說模型訓練預測原始乾淨 patch，與 epsilon-MSE 公式不符；二手反向推測須明標推測。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-036 | open | papers/2024-sora-world-simulator.md | Card 1 | 過度表述
- **問題**：將遮擋後維持物體存在寫成一般穩定能力，報告措辭為「常能但並非總是」並明列物理模擬限制；即時互動與狀態記憶之說法亦超出原文示例。Card 5、6 之世界模型與隱式幾何重建描述應保留為有限能力觀察或詮釋。
- **來源**：同 EK-035
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:35] audit

## 2025 DeepSeek-R1

### EK-037 | open | papers/2025-deepseek-r1.md | Card 4 | 原文不符
- **問題**：將 cons@64 標成 cons@16，並須註明所用論文版本。
- **來源**：[論文](https://arxiv.org/abs/2501.12948)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-038 | open | papers/2025-deepseek-r1.md | Card 1 | 原文不符
- **問題**：把「完全不使用 SFT」同時套到 R1-Zero 與 R1；原文只有 R1-Zero 為純 RL，R1 使用冷啟動資料、RL、拒絕採樣與後續 SFT。
- **來源**：[封存原文](../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2025 神經元粒線體與癌症

### EK-039 | open | papers/2025-nerve-mito-cancer.md | Card 4 | 原文不符
- **問題**：測序方法、實驗模型與轉移比例被混併；原文為分選癌細胞後之 Nanopore 分析，不是單細胞長讀長測序。
- **來源**：[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328229/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit

### EK-040 | open | papers/2025-nerve-mito-cancer.md | Card 3 | 原文未支持
- **問題**：粒線體轉移—OCR 線性增益、轉移灶富集等符號模型未見於原文，卻呈現為本文模型；須標為教學推導並註明假設。
- **來源**：[封存原文](../raw/2025-nerve-mito-cancer.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-041 | open | papers/2025-nerve-mito-cancer.md | Card 6 | 原文未支持
- **問題**：推論癌細胞偽裝成受損組織、誘使神經元依修復程序供應粒線體；原文支持轉移與富集，未證明此機制，應標作假說或比喻；治療建議亦非本文已驗證療效。
- **來源**：同 EK-040
- **發現於**：wiki/log.md [2026-11-08 22:35] audit

## 2025 滿語上下文機器翻譯

### EK-031 | open | papers/2025-manchu-in-context-mt-pei.md | Card 1 | 原文不符
- **問題**：第 27 行語族寫作「阿爾泰阿爾泰通古斯語族」，字詞重複，且「阿爾泰語系」歸類有爭議，宜依原文寫作通古斯語族（Tungusic）。
- **來源**：待回原文核對語族表述
- **發現於**：wiki/log.md [2026-11-08 22:06] audit（Claude Code by Anthropic）

## 概念頁

### EK-042 | open | concepts/neural-circuits.md | 2017 支柱 | 歸因／版本錯置
- **問題**：把 Transformer 注意力與 Hopfield 網路等價列在 2017 支柱；等價結果來自連續／現代 Hopfield 之後續工作（Ramsauer et al. 2021），不應歸給 1982 原始網路或 2017 Transformer 原文。
- **來源**：[Ramsauer et al.](https://arxiv.org/abs/2008.02217)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-043 | open | concepts/brain-machine-interface.md | 核心支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 能量吸引子寫成當代 BCI 神經流形解碼之數學基礎；神經流形屬獨立研究脈絡，現有來源不足以建立直接傳承。
- **來源**：[Hopfield 封存原文](../raw/1982-hopfield-network.pdf)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 21:57] audit

### EK-044 | open | concepts/brain-machine-interface.md | 跨學科延伸 | 過度表述
- **問題**：將雙光子讀取與全息光遺傳寫入概括為「萬級神經元的無損閉環互動」；原始研究為光刺激選定個別細胞、同時記錄數千神經元，未驗證萬級同時控制、無損或臨床可用。
- **來源**：[原始研究](https://www.nature.com/articles/s41593-026-02350-9)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit

### EK-045 | open | concepts/generative-world-models.md | 支柱與時間線 | 歸因／版本錯置
- **問題**：將 Hopfield/Hinton 能量模型合標為 1982（Boltzmann machine 學習論文為 Ackley、Hinton、Sejnowski 1985），並把 Hopfield、Boltzmann、score matching、擴散模型與 Transformer 寫成直接奠基鏈；須分開作者年代並改標為概念類比或補中間研究。
- **來源**：[Hopfield 封存原文](../raw/1982-hopfield-network.pdf)、[Ackley et al. 1985](https://doi.org/10.1207/s15516709cog0901_7)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:44] audit

### EK-046 | open | concepts/generative-world-models.md | DeepSeek-R1 段 | 歸因／版本錯置
- **問題**：將「無須人工示範」歸給 DeepSeek-R1（實為 R1-Zero），並把可驗證獎勵從原文之數學與程式任務推廣到任意驗證器與科學探索代理，應標為展望。
- **來源**：[DeepSeek-R1 封存原文](../raw/2025-deepseek-r1.pdf)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-047 | open | concepts/quantum-error-correction.md | 支柱 | 歸因／版本錯置
- **問題**：把 Hopfield 1982 列為表面碼／色碼隨機鍵 Ising 映射之直接來源；映射可追溯至 Dennis et al. 2002，其原文未引用 Hopfield，須分開數學類比與歷史來源。
- **來源**：[Dennis et al. 2002](https://arxiv.org/abs/quant-ph/0110143)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit

### EK-048 | open | concepts/quantum-error-correction.md | 定義段 | 原文不符
- **問題**：稱以橫向閘即可阻止錯誤擴散並實現「任意深度」演算法；依 Eastin–Knill 定理，可偵測錯誤之非平凡量子碼不存在通用橫向邏輯閘集合，須說明其他非橫向或測量型資源。
- **來源**：[Eastin–Knill](https://arxiv.org/abs/0811.4262)
- **發現於**：wiki/log.md [2026-11-08 21:57] audit、[2026-11-08 22:00] audit

### EK-049 | open | concepts/quantum-error-correction.md | 跨學科延伸 | 過度表述
- **問題**：稱可重構中性原子陣列已能直接實作 3D／4D 拓撲碼與常數編碼率 qLDPC；所引 2024 實驗將 qLDPC 列為後續方向，未報告已實作。
- **來源**：[Nature 原文](https://www.nature.com/articles/s41586-023-06927-3)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-050 | open | concepts/multi-messenger-astrophysics.md | 核心定義 | 原文不符
- **問題**：把深空紅外線列為與重力波、微中子、宇宙射線並列之獨立信使；紅外線屬電磁波譜。定義與後文「三大信使」亦不一致，須統一分類（光、粒子、重力波）。
- **來源**：[NASA 多信使說明](https://svs.gsfc.nasa.gov/gallery/multimessengerastronomy/)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-051 | open | concepts/institutions-and-macro-dynamics.md | AJR 支柱 | 過度表述
- **問題**：稱 AJR 以殖民者死亡率「嚴格識別」制度而非地理為收入差距的唯一根因；原文是在排他性假設與控制條件下估計制度效果，不能概括為已排除所有地理作用或證明唯一根因。
- **來源**：[AER 原文摘要](https://www.aeaweb.org/articles?id=10.1257/aer.91.5.1369)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit

### EK-052 | open | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文不符
- **問題**：稱 DrugCLIP 可「數秒」篩選百億級分子；原文為 6 billion 分子檢索少於 10,000 秒，GenomeScreenDB 規模約 10,000 個人類蛋白質、5 億化合物，全基因組篩選約 24 小時（8 張 A100）。
- **來源**：[DrugCLIP 封存原文](../raw/2023-drugclip.pdf)、[論文紀錄](https://pubmed.ncbi.nlm.nih.gov/41505557/)、[計算配置](https://www.biorxiv.org/content/10.1101/2024.09.02.610777v3.full)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit、[2026-11-08 23:21] audit

### EK-053 | open | concepts/ai-for-structural-biology.md | 跨學科延伸 | 原文未支持
- **問題**：把 AlphaFold 3＋FEP 描述成已實證之全原子誘導契合精排管線；AF3 原文報告的是複合體結構預測基準，應標為待驗證提案並另引直接驗證研究。
- **來源**：[AlphaFold 3 原文](https://www.nature.com/articles/s41586-024-07487-w)
- **發現於**：wiki/log.md [2026-11-08 23:21] audit

### EK-054 | open | concepts/programmable-cellular-engineering.md | 跨學科延伸 | 過度表述
- **問題**：「已能直接在患者肝臟、視網膜與造血幹細胞中修正致病突變」合併不同遞送方式與證據階段：Casgevy 為體外編輯後回輸；EDIT-101 為小型 1–2 期試驗；肝臟 LNP 鹼基編輯為單一新生兒 N-of-1 個案。另須同步校正自 CRISPR 論文頁重述之 PAM 與衍生技術歸因（見 EK-012、EK-015）。
- **來源**：[FDA 審查文件](https://www.fda.gov/media/175179/download?attachment=)、[視網膜試驗](https://www.nejm.org/doi/10.1056/NEJMoa2309915)、[肝臟 N-of-1](https://www.nejm.org/doi/10.1056/NEJMoa2504747)
- **發現於**：wiki/log.md [2026-11-08 22:44] audit、[2026-11-08 23:21] audit

### EK-055 | open | concepts/neural-circuits.md | Hopfield 支柱 | 歸因／版本錯置
- **問題**：與 EK-043、EK-045 同源，將 Hopfield 1982 吸引子延伸為後續多個領域之直接歷史基礎；22:44 審查指出此錯誤於多個概念頁重述，修正時須同步。
- **來源**：同 EK-042
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit

### EK-056 | open | concepts/generative-world-models.md | Sora 段 | 過度表述
- **問題**：重述 Sora 能力界線問題（見 EK-036），把有限能力觀察寫成已證明之通用物理模擬。
- **來源**：[OpenAI 技術報告](https://openai.com/index/video-generation-models-as-world-simulators/)
- **發現於**：wiki/log.md [2026-11-08 21:40] audit、[2026-11-08 22:44] audit

## DOI 無法解析（2026-11-09 crossref_check.py）

### EK-057 | open | papers/2025-tulun-adaptable-lrl-mt-merx.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2025.acl-demos.13` 在 Crossref 與 doi.org 均查無此號，DOI 可能有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：本檔建立時以 crossref_check.py 查得（Claude Code by Anthropic）

### EK-058 | open | papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.loresmt-1.25` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：同 EK-057

### EK-059 | open | papers/2026-epark-formosan-dialectometry-gagnier.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.dialres-1.13` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 ACL Anthology 原文首頁核對
- **發現於**：同 EK-057

### EK-060 | open | papers/2026-formosanmt-parallel-corpus-scheppat.md | Frontmatter doi_url | 未能核實
- **問題**：`10.18653/v1/2026.lrec-1.273` 在 Crossref 與 doi.org 均查無此號；可能尚未註冊或 DOI 有誤。
- **來源**：須回 LREC 2026 論文集原文首頁核對
- **發現於**：同 EK-057
