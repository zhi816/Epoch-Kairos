# 證據表：2024-fault-tolerant-quantum
- **採用版本**：正式版。Bluvstein, D. et al. (2024). Logical quantum processor based on reconfigurable atom arrays. *Nature*, 626(7997), 58–65. DOI: [10.1038/s41586-023-06927-3](https://doi.org/10.1038/s41586-023-06927-3)（開放取用，全文以 PMC10830422 核對；節名依正式版）。封存原文 `raw/2024-fault-tolerant-quantum.pdf` 為 arXiv:2312.03982v1（2023-12-07），本表所列數字兩版相同；Fig. 2d 之物理位元數取自 arXiv v1 圖中文字（正式版圖相同，HTML 無圖中文字）。
- **查核者**：先前版本由多位代理建立；2026-11-10 由 Claude Code by Anthropic（Claude Opus 5.5）依正式版逐項重建（EK-120、EK-121、EK-158、EK-159）。

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Card 1 | 最多 280 個物理位元；40 個色碼邏輯位元；48 個邏輯位元、228 個邏輯雙位元閘、48 個邏輯 CCZ 閘；預示早期糾錯量子計算的來臨 | 本篇研究結果 | Abstract | 符合來源 |
| Card 1 | Kitaev 之論文為 1997 年預印本，2003 年刊於 Annals of Physics 303:2–30 | 本篇研究結果 | doi:10.1016/S0003-4916(02)00018-0 | 符合來源 |
| Card 3 | 物理位元編碼於 $^{87}$Rb 基態超精細 $m_F = 0$ 鐘態，$T_2 > 1$ s（修正 EK-120：原寫 $> 1.5$ s） | 本篇研究結果 | Logical processor based on atom arrays 節；Methods, System overview | 符合來源 |
| Card 3 | 三個區：儲存區、糾纏區、讀取區之功能；雙位元閘保真度 99.5%（ref. 8）；以 2D AOD 搬運原子達成任意連接 | 本篇研究結果 | Logical processor based on atom arrays 節；Fig. 1a；Extended Data Fig. 1 | 符合來源 |
| Card 3 | 橫向閘：AOD 網格拾起兩個邏輯區塊交錯排列，打一道全域里德堡雷射；閘時同一閘位原子相距 $\lesssim 2\,\mu$m、不同閘位至少 $10\,\mu$m（原頁面寫 $\lesssim 3\,\mu$m，EK-121）；錯誤不會在同一邏輯區塊內擴散 | 本篇研究結果 | Fig. 2a；Extended Data Fig. 1 圖說；Methods, Fault tolerance and transversal gates | 符合來源 |
| Card 3 | 相關解碼：以邊與超邊連接兩區塊穩定子之聯合解碼超圖；傳統各自解碼時保真度隨碼距下降 | 本篇研究結果 | Improving entangling gates with code distance 節；Fig. 2b | 符合來源 |
| Card 3 區塊公式 1 | 相關解碼之混合整數規劃目標：maximize $\sum_j \log(p_j) E_j + \log(1-p_j)(1-E_j)$；以 Stim 估計 $p_j$，以 Gurobi 求解。頁面把原文同一展示式分為目標與限制兩式，符號與條件不變 | 本篇研究結果 | 正式發表版 PDF 第 11 頁，Methods, Correlated decoding，未編號式 | 符合來源 |
| Card 3 區塊公式 2 | 同一規劃的偵測器限制：$\sum_{E_j \in f(D_i)} E_j - 2K_i = D_i$；另有 $E_j \in \{0,1\}$、$K_i \in \mathbb{Z}_{\ge 0}$ 等條件，見該公式前之正文 | 本篇研究結果 | 正式發表版 PDF 第 11 頁，Methods, Correlated decoding，未編號式 | 符合來源 |
| Card 3 | 邏輯錯誤率 $\propto (p/p_{\text{th}})^{(d+1)/2}$ 為行文中之式子，引 ref. 24；原頁面之區塊式與 $\Lambda$ 定義、里德堡哈密頓量、穩定子碼空間、橫向 CNOT 張量積四條區塊公式原文皆沒有，已刪（修正 EK-121） | 作者解釋 | Methods, Code distance, decoding and thresholds | 符合來源 |
| Card 3 | $[[8,3,2]]$ 碼以 8 個物理位元編碼 3 個邏輯位元；邏輯三元組在 4D 超立方體上糾纏，物理連接相當於 7D 超立方體 | 本篇研究結果 | Fig. 5；Extended Data Fig. 6 | 符合來源 |
| Card 4 | Fig. 2d 橫軸：每個邏輯貝爾對之物理位元數，$d = 3$ 為 26、$d = 5$ 為 74、$d = 7$ 為 146（修正 EK-120：原寫「約 200 個」） | 本篇研究結果 | Fig. 2d（arXiv v1 PDF p. 3） | 符合來源 |
| Card 4 | $d = 7$ 相關解碼下 $X_L X_L$、$Z_L Z_L$ 布居約 0.95；邏輯貝爾對錯誤隨碼距下降；傳統解碼則上升；$d > 3$ 初態製備非容錯；超越的是含投影讀取之整體電路有效閾值（原頁面「超越所有單一物理位元對之成對糾纏保真度」原文沒有，已刪，EK-158） | 本篇研究結果 | Improving entangling gates with code distance 節；Fig. 2c–d | 符合來源 |
| Card 4 | GHZ：容錯製備 4 個邏輯位元，相關解碼保真度 72(2)%；後選擇全部穩定子正確時 $99.85^{+0.1}_{-1.0}\%$；捨棄 50% 資料時約 90% | 本篇研究結果 | Fault-tolerant logical algorithms 節；Fig. 3c–d | 符合來源 |
| Card 4 | 280 個物理位元上製備 40 個色碼；以 20 個橫向 CNOT 容錯製備其中 20 個；每多一個編碼步驟約 1% 邏輯退相干 | 本篇研究結果 | Fig. 4a–c 與圖說；同節正文 | 符合來源 |
| Card 4 | 48 個邏輯位元之 XEB 約 0.1，作者稱比先前同等複雜度之物理位元數位電路最多高約一個數量級（原頁面「因相干誤差累積導致 XEB 歸零」「遠超古典模擬極限」原文沒有，已刪，EK-158） | 本篇研究結果 | Complex logical circuits using 3D codes 節；Fig. 5e–f | 符合來源 |
| Card 5 | Xu et al. 2024：以重新排列原子實作 qLDPC 碼之症候群萃取；$10^{-3}$ 錯誤率下數百個物理位元即開始優於表面碼 | 後續研究 | doi:10.1038/s41567-024-02479-z，Nature Physics 20:1084–1090；摘要依 arXiv:2308.08648；OpenAlex 顯示引用本篇 | 符合來源 |
| Card 5 | Google Quantum AI 2024：Willow 上 101 位元 $d = 7$ 表面碼記憶，$\Lambda = 2.14 \pm 0.02$，超越最佳物理位元壽命 $2.4 \pm 0.3$ 倍 | 後續研究 | doi:10.1038/s41586-024-08449-y，Nature 638:920–926，摘要；OpenAlex 顯示引用本篇 | 符合來源 |
| Card 5 | Zhou et al. 2025：橫向操作與相關解碼，常數輪症候群萃取即可容錯 | 後續研究 | doi:10.1038/s41586-025-09543-5，Nature 646:303–308；摘要依 arXiv:2406.17653；OpenAlex 顯示引用本篇 | 符合來源 |
| Card 5 | Chiu et al. 2025：連續補充原子，維持超過 3,000 個原子之陣列超過兩小時 | 後續研究 | doi:10.1038/s41586-025-09596-6，Nature 646:1075–1080，摘要；OpenAlex 顯示引用本篇 | 符合來源 |
| Card 5 | Bravyi et al. 2024（未引用本篇，列為相關研究）：0.1% 錯誤率下 288 個物理位元保存 12 個邏輯位元近一百萬週期，表面碼需近 3,000 個（原頁面「本篇正是最理想平台」原文沒有，已刪，EK-159） | 後續研究 | doi:10.1038/s41586-024-07107-7，Nature 627:778–782，摘要 | 符合來源 |
| Card 5 | 作者所述未來方向：qLDPC 碼、擦除轉換、雜訊偏置、原子種類與光學控制；多輪症候群量測下之閾值 | 作者解釋 | Outlook；Improving entangling gates with code distance 節 | 符合來源 |
| Card 6 | 空間移動即運算、冗餘編碼對抗局部錯誤 | Wiki 詮釋 | 所據事實見本表 Card 3 各列 | 不適用 |
