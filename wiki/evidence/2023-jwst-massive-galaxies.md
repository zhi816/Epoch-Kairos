# 證據表：2023-jwst-massive-galaxies

本表記錄 [wiki/papers/2023-jwst-massive-galaxies.md](../papers/2023-jwst-massive-galaxies.md) 各項主張在第一手文獻中的出處與核驗結果。

- **主要第一手來源**：Boylan-Kolchin, M. (2023). Stress testing ΛCDM with high-redshift galaxy candidates. *Nature Astronomy*, 7(6), 731–735. DOI: [10.1038/s41550-023-01937-7](https://doi.org/10.1038/s41550-023-01937-7)
- **觀測來源**：Labbé, I. et al. (2023). A population of red candidate massive galaxies ~600 Myr after the Big Bang. *Nature*, 616(7956), 266–269. DOI: [10.1038/s41586-023-05786-2](https://doi.org/10.1038/s41586-023-05786-2)
- **封存原文**：`raw/2023-jwst-massive-galaxies.pdf`

---

| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |
|---|---|---|---|
| Card 1, Card 3 | 宇宙學參數與重子質量約束：$f_b = 0.156$、$M_\star \le \epsilon f_b M_{\text{halo}}$ | §2 (p. 1) | 核實符合。採 Planck 2020 基準參數（$H_0 = 67.32\,\text{km}\,\text{s}^{-1}\,\text{Mpc}^{-1}$、$\Omega_m = 0.3158$、$f_b = 0.156$）。 |
| Card 3 | 暗物質暈質量函數計算：採用 Sheth & Tormen (1999) HMF 數值積分 | §2 (p. 1), Eq. (1)–(2) | 核實更正。主文計算採用 Sheth & Tormen (1999) 橢球坍縮暗物質暈質量函數；補充解析式為 Press-Schechter (1974) 球對稱坍縮近似（用於解釋高斯指數尾部衰減），非主計算數值來源。 |
| Card 3, Card 4 | 極端峰高：Labbé et al. 樣本在 $\epsilon=1$ 下對應峰高 $\nu \ge 4.5$ | §3 (p. 2), Figure 1 | 核實符合。在 $V \approx 10^5\,\text{Mpc}^3$ 巡天體積中，$z \approx 7.5$（$M_\star \approx 10^{11}\,M_\odot$）與 $z \approx 9.1$（$M_\star \approx 10^{10.5}\,M_\odot$）星系之暗物質暈對應 $\nu \ge 4.5$，僅佔全宇宙重子的 $6.2 \times 10^{-5}$。 |
| Card 4 | 累積恆星質量密度與轉化效率：中心估計 $\epsilon(z \approx 9) = 0.99$、$\epsilon(z \approx 7.5) = 0.84$ | §3 (p. 2), Figure 2 | 核實更正。中心測量值緊貼理論極限曲線 $\rho_\star = f_b \rho_m$，中心估計分別為 $\epsilon(z \approx 9) = 0.99$ 與 $\epsilon(z \approx 7.5) = 0.84$。 |
| Card 4 | 觀測誤差邊界：納入 $1\sigma$ 不確定度後邊際一致要求 $\epsilon(z \approx 9) \ge 0.57$ | §3 (p. 2), Figure 2 說明 | 核實更正。在納入星系質量估計、泊松漲落與樣本方差之 $1\sigma$ 誤差後，數據在 $\epsilon(z \approx 9) \ge 0.57$ 時與基準 $\Lambda\text{CDM}$ 邊際一致。修正原先將 $\epsilon \approx 0.57$ 錯配至 $z \approx 7.5$ 之錯誤，並刪除超出原文結論之「觀測密度為理論上限 2–5 倍」陳述。 |
| Card 4 | 後續 NIRSpec 光譜確認部分極端候選者為含塵埃 AGN（Little Red Dots） | Card 4 後續進展 (Arrabal Haro 2023, Kocevski 2023) | 核實符合。後續光譜證實部分超亮紅外訊號來自活躍星系核吸積盤，使恆星質量下修約一個數量級，緩解了極端張力。 |
