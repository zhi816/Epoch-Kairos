# 證據表：2023-jwst-massive-galaxies
- **採用版本**：正式版。Boylan-Kolchin, M. (2023). Stress testing ΛCDM with high-redshift galaxy candidates. *Nature Astronomy*, 7(6), 731–735. DOI: [10.1038/s41550-023-01937-7](https://doi.org/10.1038/s41550-023-01937-7)（開放取用，全文以 PMC10281863 核對；節名為 Main、Assumptions、Results、Discussion，式 1 至 5）。封存原文 `raw/2023-jwst-massive-galaxies.pdf` 為 arXiv:2208.01611v2（2023-02-20 審稿後預印本），與正式版之差異：早期暗能量比較為 3.3 倍與 $\epsilon = 0.72$（正式版 3.1 倍與 0.74）；$1\sigma$ 誤差之組成多列「恆星質量估計」；可能解釋未列黑洞吸積。本表一律採正式版。觀測來源：Labbé, I. et al. (2023), *Nature* 616:266–269, doi:10.1038/s41586-023-05786-2（摘要依 arXiv:2207.12446）。
- **查核者**：先前版本由多位代理建立；2026-11-10 由 Claude Code by Anthropic（Claude Opus 5.5）依正式版逐項重建（EK-114、EK-115、EK-154、EK-155）。

| 位置 | 主張 | 類型 | 第一手來源與精確位置 | 判定 |
|---|---|---|---|---|
| Card 1 | 本篇所用之觀測來源（非本篇成果、非後續研究）：Labbé 等找到 6 個恆星質量大於 $10^{10}\,M_\odot$、$7.4 < z < 9.1$ 之候選，其中一個可能約 $10^{11}\,M_\odot$ | 作者解釋 | Labbé et al. 2023 摘要（arXiv:2207.12446）；本篇 Results 第 1 段 | 符合來源 |
| Card 1 | 最重候選落在上限邊緣，指出觀測推得之星系性質、早期星系形成或標準宇宙學本身有尚未解決的重要問題 | 本篇研究結果 | Abstract | 符合來源 |
| Card 2 | 低紅移宇宙中所有星系 $\epsilon \lesssim 0.2$（修正 EK-115：原頁面寫 0.1–0.3） | 作者解釋 | Discussion 倒數第 2 段 | 符合來源 |
| Card 3 | 參數：$H_0 = 67.32$、$\Omega_m = 0.3158$、$n_s = 0.96605$、$\sigma_8 = 0.8120$、$f_b = 0.156$（Planck 2020 基準 $\Lambda$CDM） | 本篇研究結果 | Assumptions 第 1 段 | 符合來源 |
| Card 3 區塊公式 1 | $M_\star = \epsilon f_b M_{\text{halo}}$，$\epsilon \le 1$（原頁面之 $M_{\text{halo}} \ge M_\star/f_b \approx 6.4 M_\star$ 與 $f_b = 0.1564$ 原文沒有，已刪，EK-154） | 本篇研究結果 | 正式版 Assumptions，p. 732，正文內嵌式，無式號 | 符合來源（核對正式版 PDF 頁面） |
| Card 3 區塊公式 2 | $n(> M_{\text{halo}}, z) = \int_{M_{\text{halo}}}^\infty dM\, dn/dM$ | 本篇研究結果 | 正式版 Assumptions，p. 731，式 (1) | 符合來源（核對正式版 PDF 頁面） |
| Card 3 區塊公式 3 | $\rho_m(> M_{\text{halo}}, z) = \int_{M_{\text{halo}}}^\infty dM\, M\, dn/dM$ | 本篇研究結果 | 正式版 Assumptions，p. 732，式 (2) | 符合來源（核對正式版 PDF 頁面） |
| Card 3 區塊公式 4 | $n_{\text{gal}}(> M_\star) \le n_{\text{halo}}(> M_\star / f_b)$ | 本篇研究結果 | 正式版 Assumptions，p. 732，式 (3) | 符合來源（核對正式版 PDF 頁面） |
| Card 3 區塊公式 5 | $\rho_\star(> M_\star) \le f_b \rho_m(> M_\star / f_b)$ | 本篇研究結果 | 正式版 Assumptions，p. 732，式 (5) | 符合來源（核對正式版 PDF 頁面） |
| Card 3 | 以 Sheth & Tormen (1999) 暗物質暈質量函數計算；其在 $z \approx 7$–$10$ 相對模擬高估大質量暗物質暈豐度 20–50%，限制偏保守 | 本篇研究結果 | Assumptions；Discussion | 符合來源 |
| Card 3 | 峰高 $\nu = \delta_c / \sigma$，$\delta_c \approx 1.7$；典型 $\nu = 1$ 對應宇宙 24% 的質量位於至少同等質量之暗物質暈 | 作者解釋 | Results 第 2 段 | 符合來源 |
| Card 3 | $\epsilon < 1$ 時上限曲線相對資料點下移 $\epsilon$ 倍 | 作者解釋 | Fig. 1 圖說 | 符合來源 |
| Card 3 | 原頁面之「極值統計鎖定最重暗物質暈」與 Press–Schechter erfc 解析式，原文沒有，已刪（EK-115、EK-154） | 不適用 | 全文搜尋「extreme value」「erfc」無結果 | 原文未支持 |
| Card 4 | 兩個最重候選：$z \approx 7.5$（$M_\star \approx 10^{11}\,M_\odot$）與 $z \approx 9.1$（$M_\star \approx 10^{10.5}\,M_\odot$） | 本篇研究結果 | Results 第 1 段；Fig. 1 | 符合來源 |
| Card 4 | 累積共動數密度：$\epsilon = 1$ 時不高於約 $10^{-5.2}\,\text{Mpc}^{-3}$；$\epsilon = 0.32$ 時約 $10^{-7}$；$\epsilon = 0.10$ 時約 $10^{-9.3}\,\text{Mpc}^{-3}$ | 本篇研究結果 | Results 第 1 段；Fig. 1 左 | 符合來源 |
| Card 4 | 巡天 38 arcmin²，在 $7 < z < 8.5$ 與 $8.5 < z < 10$ 兩個紅移區間各約 $V \approx 10^5\,\text{Mpc}^3$ | 本篇研究結果 | Results 第 1 段 | 符合來源 |
| Card 4 | 峰高至少 $\nu = 4.5$（$\epsilon = 1$），宇宙中至多 $6.2 \times 10^{-5}$ 的重子位於足以容納之暗物質暈；$\epsilon = 0.32$ 或 0.10 時 $\nu \approx 5.4$ 或 6.4 | 本篇研究結果 | Results 第 2 段；Fig. 1 右 | 符合來源 |
| Card 4 | Fig. 2：測量值落在理論極限上，$\epsilon(z \approx 9) = 0.99$、$\epsilon(z \approx 7.5) = 0.84$，作者稱物理上不太可能（修正 EK-114：原頁面稱超過 100%、低於觀測值） | 本篇研究結果 | Results 第 3 段；Fig. 2 | 符合來源 |
| Card 4 | 納入泊松漲落與樣本方差之 $1\sigma$ 誤差後，$\epsilon(z \approx 9) \ge 0.57$ 才勉強相容；取 $\epsilon = 0.1$ 或 0.32 則兩紅移都明顯不符 | 本篇研究結果 | Results 第 3 段；Fig. 2 圖說 | 符合來源 |
| Card 4 | 可能解釋：初始質量函數、黑洞吸積貢獻、巡天體積不典型；NIRCam 流量校正；早期暗能量使重子密度為 3.1 倍、$\epsilon = 0.74$ 但與 $S_8$ 及古老星系年齡有張力；光譜確認後將構成嚴重挑戰 | 作者解釋 | Discussion | 符合來源 |
| Card 4 | 原頁面之最重暗物質暈 $4 \times 10^{11}$、重子極限 $6.5 \times 10^{10}$ 與 $1.2 \times 10^{10}\,M_\odot$、Labbé 候選 ID 38094 與 $10^{10.9}$，原文沒有，已刪（EK-115） | 不適用 | 正式版全文搜尋無結果 | 原文未支持 |
| Card 5 | Dekel et al. 2023：免反饋星暴，$z \sim 10$ 高密度低金屬量使最重暗物質暈成星效率高 | 後續研究 | doi:10.1093/mnras/stad1557，MNRAS 523:3201–3218，摘要 | 符合來源 |
| Card 5 | Arrabal Haro et al. 2023：光譜確認兩個 $z > 11$ 明亮星系，一個 $z \approx 16$ 候選實為 $z = 4.9$ | 後續研究 | doi:10.1038/s41586-023-06521-7，Nature 622:707–711，摘要（arXiv:2303.15431） | 符合來源 |
| Card 5 | Glazebrook et al. 2024：$z = 3.205$ 之大質量靜止星系 ZF-UDS-7329，恆星約於 $z \sim 11$ 形成 | 後續研究 | doi:10.1038/s41586-024-07191-9，Nature 628:277–281，摘要（arXiv:2308.05606） | 符合來源 |
| Card 5 | Desprez et al. 2024：CANUCS 五個視野約 60 arcmin²、19 個候選，恆星質量不特別高；五個光譜之紅色來自強發射線；視野間最大恆星質量差約 1.5 dex | 後續研究 | doi:10.1093/mnras/stae1084，MNRAS 530:2935–2952，摘要（arXiv:2310.03063） | 符合來源 |
| Card 5 | Chworowsky et al. 2024：CEERS $z \sim 4$–$8$ 大質量星系數密度超出固定效率模型，可由成星物理或效率之適度改變解釋，與現代宇宙學無衝突 | 後續研究 | doi:10.3847/1538-3881/ad57c1，AJ 168:113，摘要（arXiv:2311.14804） | 符合來源 |
| Card 6 | 上限檢驗不判定何者出錯、後續分頭回應 | Wiki 詮釋 | 所據事實見本表 Card 1、Card 5 各列 | 不適用 |
