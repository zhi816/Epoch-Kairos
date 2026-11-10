# 卡片文字：2023-jwst-massive-galaxies

- **論文頁**：[2023-jwst-massive-galaxies](../papers/2023-jwst-massive-galaxies.md)
- **證據表**：[2023-jwst-massive-galaxies](../evidence/2023-jwst-massive-galaxies.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：算出宇宙早期／最多能長出／多大的星系
- 導語：早期候選星系已逼近標準宇宙學的恆星上限。
- 封面標題：以高紅移星系候選對宇宙學進行壓力測試

## Card 2｜世紀瓶頸
- 標題：宇宙早期，真能長出這麼重的星系？
- 對照：哈伯｜觀測波長不夠長，看不清早期星系已累積多少恆星
- 對照：重子分數｜暗物質暈裡重子只佔物質的 0.156，成星原料有限
- 對照：轉化效率｜低紅移宇宙中，星系把重子變成恆星的效率都在兩成以下
- 缺口：檢驗｜沒有簡單方法判斷這些候選是否超出標準宇宙學允許的範圍
- 結語：先得知道那時宇宙最多能提供多少原料。

## Card 3｜突破原理
- 標題：恆星不能多於可用的重子
- 公式：\rho_\star(> M_\star) \le f_b \rho_m(> M_\star / f_b)
- 說明：大於某質量的星系，恆星總密度不能超過夠重暗物質暈裡的重子總量。
- 圖類型：示意圖
- 圖說：示意：暗物質暈裡只有一部分是重子，恆星最多用完這些重子；觀測候選幾乎貼著上限。

```svg
<svg viewBox="0 0 300 120" role="img" aria-label="示意：暗物質暈裡只有一部分是重子，恆星最多用完這些重子；觀測候選幾乎貼著上限。">
  <rect class="k-ink k-ring" x="8" y="8" width="164" height="104" rx="4"/>
  <rect class="k-soft" x="28" y="36" width="124" height="66" rx="4"/>
  <rect class="k-accent k-ring" x="56" y="62" width="68" height="30" rx="4"/>
  <rect class="k-soft" x="230" y="28" width="12" height="80"/>
  <line class="k-line" x1="226" y1="28" x2="250" y2="28"/>
  <circle class="k-accent" cx="236" cy="36" r="4"/>
  <text class="k-label" x="90" y="26" text-anchor="middle">暗物質暈</text>
  <text class="k-label" x="90" y="54" text-anchor="middle">重子</text>
  <text class="k-label-accent" x="90" y="82" text-anchor="middle">恆星</text>
  <text class="k-label" x="258" y="32">上限</text>
  <text class="k-label-accent" x="222" y="44" text-anchor="end">觀測候選</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：0.99｜z≈9 恆星質量密度所需的重子轉化效率｜Results, Fig. 2
- 數字：0.84｜z≈7.5 的同一指標｜Results, Fig. 2
- 數字：≥0.57｜計入 1σ 誤差後，z≈9 仍需的最低效率｜Results, Fig. 2
- 數字：≲0.2｜低紅移宇宙所有星系的轉化效率｜§Discussion
- 範圍：Boylan-Kolchin 2023，單一巡天的測光候選，未經光譜確認

## Card 5｜典範轉移
- 標題：張力之下，光譜與理論回應
- 里程碑：2023｜Dekel 等提出免反饋星暴，說明高效成星｜Dekel et al. 2023, MNRAS 523:3201-3218
- 里程碑：2023｜Arrabal Haro 等光譜否定 z≈16 候選｜Arrabal Haro et al. 2023, Nature 622:707-711
- 里程碑：2024｜Glazebrook 等：恆星在 z≈11 已形成｜Glazebrook et al. 2024, Nature 628:277-281
- 里程碑：2024｜Desprez 等另選樣本，未見特別重的星系｜Desprez et al. 2024, MNRAS 530:2935-2952
- 里程碑：2024｜Chworowsky 等認為過量與宇宙學無衝突｜Chworowsky et al. 2024, AJ 168:113
- 註記：以上皆為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：不追究星系怎麼形成，只清點那時有多少重子，就畫出不可越過的線。
- 轉變：模擬細節→守恆上限
