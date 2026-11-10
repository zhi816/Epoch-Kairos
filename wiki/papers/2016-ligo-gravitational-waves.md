---
title: "Observation of Gravitational Waves from a Binary Black Hole Merger"
title_zh: "LIGO 雙黑洞重力波直接探測：聆聽時空結構的漣漪"
paper_year: 2016
award_year: 2017
timeline_year: 2016
authors: "B. P. Abbott et al. (LIGO Scientific Collaboration and Virgo Collaboration)"
laureates: "Rainer Weiss, Barry C. Barish, Kip S. Thorne"
venue: "Physical Review Letters, 116(6), 061102"
venue_short: "PRL"
honor: "2017 諾貝爾物理學獎（表彰對 LIGO 探測器及重力波直接觀測之決定性貢獻）"
domain: "physics"
domain_tags: ["#天體物理", "#宇宙學"]
concepts: ["multi-messenger-astrophysics"]
status: "published"
verification: "verified"
my_focus: false
doi_url: "https://doi.org/10.1103/PhysRevLett.116.061102"
key_papers:
  - "Einstein, A. (1916) Näherungsweise Integration der Feldgleichungen der Gravitation. Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften, 688-696."
  - "Abbott, B. P. et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016) Observation of Gravitational Waves from a Binary Black Hole Merger. Physical Review Letters 116(6):061102. https://doi.org/10.1103/PhysRevLett.116.061102"
  - "Abbott, B. P. et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2017) GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral. Physical Review Letters 119(16):161101. https://doi.org/10.1103/PhysRevLett.119.161101"
hook: "兩座臂長 4 公里的雷射干涉儀同時記錄到重力波 GW150914，是首次直接偵測到重力波，也是首次觀測到雙黑洞併合；訊號與廣義相對論預測之旋近、併合與振鈴波形相符。"
card_line: "第一次直接測到黑洞相撞發出的重力波"
---

# LIGO 雙黑洞重力波直接探測：聆聽時空結構的漣漪

> 「2015 年 9 月 14 日，美國兩座干涉儀在 10 毫秒內先後記錄到同一段時空振動，那是約十三億光年外兩個黑洞合而為一時發出的訊號。」（本頁引言為 Wiki 撰寫，非原文）

**2016 發表 ｜ 2017 諾貝爾物理學獎**

> **本頁範圍說明**：2017 年諾貝爾物理學獎頒予 Rainer Weiss（1/2）、Barry C. Barish（1/4）與 Kip S. Thorne（1/4），表彰三人對雷射干涉儀重力波天文台（LIGO）及重力波直接觀測之決定性貢獻。本頁以 LIGO 與 Virgo 合作組於 2016 年 2 月發表於《Physical Review Letters》之首個重力波事件 GW150914 發現論文為主軸，並於 `key_papers` 列出 2017 年雙中子星併合多信使事件 GW170817 之代表文獻。

---

## Card 1 ｜ 時代銘文 (The Hook)
1916 年，愛因斯坦發現線性化的弱場方程有波動解：由波源質量四極矩隨時間變化所產生、以光速傳播的空間應變橫波，即重力波（Gravitational Waves）。他也了解重力波的振幅會非常微小；直到 1957 年 Chapel Hill 會議之前，學界對重力波是否真實存在仍有相當爭論（原文 p. 1）。一百年後，2015 年 9 月 14 日，LIGO 兩座探測器同時記錄到代號 **GW150914** 的瞬變訊號，峰值應變為 $1.0 \times 10^{-21}$。作者指出，這是首次直接偵測到重力波，也是首次觀測到雙黑洞併合；訊號與廣義相對論對雙黑洞旋近、併合，以及併合後單一黑洞振鈴所預測的波形相符（摘要）。

---

## Card 2 ｜ 世紀瓶頸：極微小的臂長差、各頻段雜訊與併合波形建模 (The Dilemma)
直接偵測雙黑洞併合的重力波，須同時克服三個難題：

* **極微小的臂長差**：臂長 $L = 4\,\text{km}$（原文 p. 3）的干涉儀上，峰值應變 $h = 1.0 \times 10^{-21}$ 造成的臂長差約為 $\Delta L = hL \approx 4 \times 10^{-18}\,\text{m}$（依原文數據計算）。
* **三種頻段各有主要雜訊**：原文說明，高頻以光子散粒雜訊（Shot Noise）為主，低頻以地震雜訊為主，中頻以熱雜訊為主（p. 4）。因此每面測試質量鏡吊在四級擺系統的末端，下方再有主動隔震平台，對 10 Hz 以上的地面振動合計提供超過 10 個數量級的隔離；除雷射光源外，所有元件都裝在隔震平台上並置於超高真空中，容納臂腔光束、直徑 1.2 公尺的管道氣壓維持在 1 μPa 以下，以減少瑞利散射造成的光相位擾動（p. 4）。
* **併合波形需要數值相對論**：原文指出，1990 年代的高階後牛頓計算、其後的相對論二體動力學解析研究，加上近十年數值相對論（Numerical Relativity）的突破，才使雙黑洞併合得以建模並準確預測波形（p. 1）；在此之前，雙黑洞併合從未被觀測到（p. 1）。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
Advanced LIGO 以強化的邁克生干涉儀、隔震與低雜訊設計提高應變靈敏度，並以廣義相對論波形模板之匹配濾波（Matched Filtering）搜尋訊號：

1. **兩座相距遙遠的探測器（Hanford 與 Livingston）**：
   * 美國華盛頓州 Hanford（H1）與路易斯安那州 Livingston（L1）各有一座 Advanced LIGO 探測器。原文說明，重力波天文學利用多座相距遙遠的探測器，區分重力波與局域之儀器或環境雜訊、定位波源並量測偏振（p. 3）；GW150914 落在兩站 10 毫秒的光行時間之內（p. 2），先抵達 L1，約 6.9 毫秒後抵達 H1（圖 1 圖說）。
2. **臂內共振腔與功率循環**：
   * 每條臂由兩面測試質量鏡構成共振光學腔，把重力波對光相位的效應放大 300 倍；輸入端的功率循環鏡使雷射光在整台干涉儀中再共振增強：20 W 的雷射輸入在分光鏡上增為 700 W，每條臂腔內的循環功率再增為 100 kW（p. 3）。輸出端的訊號循環鏡加寬臂腔頻寬以利訊號擷取；光源為 1064 nm 之 Nd:YAG 雷射（p. 4）。
3. **旋近、併合與振鈴三階段**：
   * 訊號在約 0.2 秒、約 8 個週期內，頻率與振幅由 35 Hz 升至 150 Hz（振幅最大處）；較低頻的演化由啁啾質量（Chirp Mass）$\mathcal{M}$ 描述。峰值之後波形的衰減，與黑洞弛豫為最終穩態克爾（Kerr）組態之阻尼振盪一致（p. 3）。

### 1. 干涉儀量測的臂長差 (Differential Arm Length)

每條臂由兩面相距 $L_x = L_y = L = 4\,\text{km}$ 的測試質量鏡構成。通過的重力波等效改變兩臂長度，量到的長度差為（原文 p. 3）：

$$\Delta L(t) = \delta L_x - \delta L_y = h(t)\,L$$

其中 $h$ 為投影到探測器上的重力波應變振幅。這個長度差改變兩道返回分光鏡之光的相位差，使部分光訊號傳到輸出端的光偵測器（p. 3）。

### 2. 啁啾質量 (Chirp Mass)

訊號頻率與振幅隨時間上升，最合理的解釋是兩個互繞質量 $m_1$、$m_2$ 因輻射重力波而旋近。在較低頻段，這種演化由啁啾質量刻畫（原文 p. 3）：

$$\begin{aligned}
\mathcal{M} &= \frac{(m_1 m_2)^{3/5}}{(m_1 + m_2)^{1/5}} \\
&= \frac{c^3}{G} \left[ \frac{5}{96} \pi^{-8/3} f^{-11/3} \dot{f} \right]^{3/5}
\end{aligned}$$

其中 $f$ 與 $\dot{f}$ 為觀測到的頻率及其時間導數，$G$ 與 $c$ 為重力常數與光速。由圖 1 的資料估計 $f$ 與 $\dot{f}$，得到啁啾質量 $\mathcal{M} \simeq 30\,M_\odot$，表示偵測器座標系中的總質量 $M = m_1 + m_2 \gtrsim 70\,M_\odot$，兩者史瓦西半徑之和 $2GM/c^2 \gtrsim 210\,\text{km}$。要達到 75 Hz 的軌道頻率（重力波頻率的一半），兩個天體必須非常接近且非常緻密：以等質量牛頓點質量計，相距僅約 350 km。一對中子星質量不足；具有此啁啾質量的黑洞—中子星雙星總質量會很大，因而在低得多的頻率就併合。作者據此指出，黑洞是唯一已知足夠緻密、能在 75 Hz 軌道頻率而不相觸的天體（p. 3）。

### 3. 輻射能量與峰值光度 (Radiated Energy & Peak Luminosity)

作者以雙黑洞併合數值模擬之擬合式，估算最終黑洞的質量與自旋、以重力波輻射的總能量，以及重力波峰值光度（原文 p. 7）。以重力波輻射的總能量估計為 $3.0^{+0.5}_{-0.5}\,M_\odot c^2$，與初始兩黑洞質量之和減去最終黑洞質量的差值相當（36 + 29 − 62 = 3，依原文表 I 數據計算；見 Card 4）。

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Abbott et al. 2016, GW150914）之核心證據
* **訊雜比 24、顯著性超過 $5.1\sigma$**：2015 年 9 月 14 日 09:50:45 UTC，訊號先抵達 Livingston（L1），$6.9^{+0.5}_{-0.4}\,\text{ms}$ 後抵達 Hanford（H1）（圖 1 圖說）。約 0.2 秒、約 8 個週期內，頻率與振幅由 35 Hz 升至 150 Hz（p. 3）；整段訊號的頻率由 35 Hz 掃到 250 Hz（摘要）。匹配濾波訊雜比（SNR）為 24，誤報率估計低於每 203,000 年 1 次，相當於顯著性超過 $5.1\sigma$（摘要；p. 7）。
* **峰值應變與雙黑洞參數**：峰值重力波應變為 $1.0 \times 10^{-21}$（摘要）。光度距離 $410^{+160}_{-180}\,\text{Mpc}$（約 13 億光年，依原文數據換算），紅移 $z = 0.09^{+0.03}_{-0.04}$；源座標系下初始兩黑洞質量為 $36^{+5}_{-4}\,M_\odot$ 與 $29^{+4}_{-4}\,M_\odot$，最終黑洞質量 $62^{+4}_{-4}\,M_\odot$，最終自旋 $0.67^{+0.05}_{-0.07}$（表 I，p. 7）。所有不確定度均為 90% 可信區間（摘要）。
* **輻射能量與峰值光度**：以重力波輻射的總能量估計為 $3.0^{+0.5}_{-0.5}\,M_\odot c^2$；峰值重力波光度為 $3.6^{+0.5}_{-0.4} \times 10^{56}\,\text{erg/s}$，相當於每秒 $200^{+30}_{-20}\,M_\odot c^2$（p. 7）。
* **重力子質量上限**：假設重力波有修正的色散關係，觀測結果把重力子的康普頓波長限制在 $\lambda_g > 10^{13}\,\text{km}$，可解讀為重力子質量 $m_g < 1.2 \times 10^{-22}\,\text{eV}/c^2$；此界限比太陽系與雙脈衝星的界限分別改善數倍與約千倍，但未優於依賴模型的星系團動力學與弱重力透鏡界限（p. 8）。作者總結，所做的三項檢驗都與廣義相對論在強場區的預測一致（p. 8）。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **雙中子星併合 GW170817**：Abbott et al. (2017), *Physical Review Letters* 119:161101（doi:10.1103/PhysRevLett.119.161101）。Advanced LIGO 與 Advanced Virgo 首次觀測到雙中子星旋近，訊雜比 32.4，光度距離約 $40\,\text{Mpc}$；Fermi-GBM 在併合後 1.7 秒偵測到伽瑪射線暴 GRB 170817A，作者稱這是雙中子星併合與短伽瑪射線暴相關聯的第一個直接證據（摘要）。
* **多信使觀測**：Abbott et al. (2017), *Astrophysical Journal Letters* 848:L12（doi:10.3847/2041-8213/aa91c9）。併合後不到 11 小時，在星系 NGC 4993 發現明亮的光學瞬變源 AT 2017gfo，之後在紫外、光學、紅外、X 射線與無線電波段陸續觀測（摘要）。
* **重力與光速之差**：Abbott et al. (2017), *Astrophysical Journal Letters* 848:L13（doi:10.3847/2041-8213/aa920c）。以 GRB 170817A 與 GW170817 之間 $(+1.74 \pm 0.05)\,\text{s}$ 的時間差，把重力傳播速度與光速之差限制在光速的 $-3 \times 10^{-15}$ 至 $+7 \times 10^{-16}$ 之間（摘要）。
* **標準汽笛測量哈伯常數**：Abbott et al. (2017), *Nature* 551:85–88（doi:10.1038/nature24471）。以重力波訊號直接推得的距離，搭配電磁觀測得到的退行速度，不需宇宙距離階梯，測得哈伯常數 $70.0^{+12.0}_{-8.0}\,\text{km}\,\text{s}^{-1}\,\text{Mpc}^{-1}$（摘要）。
* **第三版重力波瞬變星表 GWTC-3**：Abbott et al. (2023), *Physical Review X* 13:041039（doi:10.1103/PhysRevX.13.041039）。前三次觀測運行中以 $p_{\text{astro}} > 0.5$ 認定的緻密雙星併合候選事件共 90 起，其中包含首批可信的黑洞—中子星雙星觀測（摘要）。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **雙黑洞的存在與形成**：過去已有許多以電磁觀測辨識出的黑洞候選者，但黑洞併合從未被觀測到（原文 p. 1）。作者指出，GW150914 證明存在質量大於約 $25\,M_\odot$ 的恆星級黑洞，並確立雙黑洞能在自然界形成、並在哈伯時間內併合；由恆星演化形成這麼重的黑洞需要較弱的大質量恆星風，這在金屬豐度低於太陽約一半的環境中才可能（p. 8）。
* **強場區的廣義相對論檢驗**：此前，Hulse 與 Taylor 發現的雙脈衝星 PSR B1913+16 及其後的能量損失觀測，已間接證明重力波存在（原文 p. 1）。GW150914 讓研究者得以在強場、高速區檢驗時空性質，作者的三項檢驗都與廣義相對論在強場區的預測一致（p. 2、p. 8）。
* **重力波成為觀測工具**：此後的雙中子星併合 GW170817 結合了重力波與電磁波觀測，並被用作「標準汽笛」，不經宇宙距離階梯測量哈伯常數（Abbott et al. 2017, Nature 551:85–88）；到第三次觀測運行結束，GWTC-3 收錄的緻密雙星併合候選事件已有 90 起（Abbott et al. 2023, PRX 13:041039）。出處與數值見 Card 4 後續。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
以下為 Wiki 詮釋：

1. **理論預言與工程能力的接力**：原文回顧，干涉式探測器的構想最早見於 1960 年代初與 1970 年代，其後歷經雜訊與性能研究、長基線寬頻雷射干涉儀的提案（p. 1）；1916 年的預言，要等到雷射干涉、隔震、真空與數值相對論都成熟後，才在 2015 年被直接偵測到。
2. **把雜訊拆成頻段逐一處理**：原文把雜訊依頻段分開說明，高頻的光子散粒雜訊、低頻的地震雜訊、中頻的熱雜訊各有對策（p. 4）。面對約 $4 \times 10^{-18}\,\text{m}$ 的臂長差，關鍵不在單一突破，而在把每一種雜訊的來源找出來並分別壓低。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [多信使天體物理與極端宇宙學](../concepts/multi-messenger-astrophysics.md)
* **原始權威文獻**：
  * 官方學術出處：Abbott, B. P. et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). Physical Review Letters, 116(6), 061102. DOI: [10.1103/PhysRevLett.116.061102](https://doi.org/10.1103/PhysRevLett.116.061102)
  * 原始檔典藏：`raw/2016-ligo-gravitational-waves.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 獎項通告：[The Nobel Prize in Physics 2017](https://www.nobelprize.org/prizes/physics/2017/)
