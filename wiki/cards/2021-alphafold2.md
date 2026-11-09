# 卡片文字：2021-alphafold2

- **論文頁**：[2021-alphafold2](../papers/2021-alphafold2.md)
- **證據表**：[2021-alphafold2](../evidence/2021-alphafold2.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09

## 封面
- 封面斷行：從胺基酸序列，／準確預測蛋白質的／立體結構
- 導語：讓深度學習同時讀懂演化留下的序列線索與立體幾何，把預測誤差縮小到接近實驗測量。
- 封面標題：AlphaFold2

## Card 2｜世紀瓶頸
- 標題：算不完的構型，拼不起的距離
- 對照：分子動力學｜逐一模擬原子受力，算力只夠模擬少數小蛋白的摺疊
- 對照：接觸圖｜由共同突變推測相鄰位置，拼成立體時常扭曲、碰撞
- 缺口：方法｜缺少能把演化線索直接變成一致立體結構的方法
- 結語：需要一種從序列直接算到原子座標的辦法。

## Card 3｜突破原理
- 標題：演化與幾何，互相校正
- 公式：\alpha_{ijk} = \operatorname{softmax}_{k}\left( \frac{1}{\sqrt{c}} q_{ij}^\top k_{ik} + b_{jk} \right)
- 說明：更新胺基酸 i 與胺基酸 j 的關係時，一併參考第三個胺基酸 k，引導三者距離趨於一致。
- 圖類型：示意圖
- 圖說：示意：更新胺基酸 i 與 j 的關係時，同時參考每個第三個胺基酸 k 與兩者的關係。

```svg
<svg viewBox="0 0 300 120" role="img" aria-label="示意：更新胺基酸 i 與 j 的關係時，同時參考每個第三個胺基酸 k 與兩者的關係。">
  <line class="k-muted k-thin" x1="64" y1="86" x2="110" y2="36"/>
  <line class="k-muted k-thin" x1="64" y1="86" x2="190" y2="36"/>
  <line class="k-muted k-thin" x1="236" y1="86" x2="110" y2="36"/>
  <line class="k-muted k-thin" x1="236" y1="86" x2="190" y2="36"/>
  <line class="k-accent" x1="64" y1="86" x2="150" y2="30"/>
  <line class="k-accent" x1="236" y1="86" x2="150" y2="30"/>
  <line class="k-line" x1="66" y1="90" x2="234" y2="90"/>
  <circle class="k-ink" cx="110" cy="36" r="4"/>
  <circle class="k-ink" cx="150" cy="30" r="4.4"/>
  <circle class="k-ink" cx="190" cy="36" r="4"/>
  <circle class="k-accent" cx="60" cy="90" r="5.5"/>
  <circle class="k-accent" cx="240" cy="90" r="5.5"/>
  <text class="k-label" x="150" y="18" text-anchor="middle">第三個胺基酸 k</text>
  <text class="k-label-accent" x="60" y="112" text-anchor="middle">胺基酸 i</text>
  <text class="k-label-accent" x="240" y="112" text-anchor="middle">胺基酸 j</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：0.96 Å｜CASP14 盲測主鏈誤差之中位數｜Figure 1，p. 584
- 數字：2.8 Å｜同一評測中，第二名方法的主鏈誤差｜Figure 1，p. 584
- 數字：1.5 Å｜含側鏈全原子誤差之中位數（第二名 3.5 Å）｜Figure 1，p. 584
- 數字：0.76｜模型自評信心與實測精度之相關係數｜Figure 2c，p. 585
- 範圍：Jumper 等 2021，蛋白質結構預測盲測賽與近期實驗結構之評估

## Card 5｜典範轉移
- 標題：結構生物學，改為計算先行
- 里程碑：2021｜Tunyasuvunakool 等預測人類蛋白質組｜Tunyasuvunakool et al. 2021, Nature 596:590-596
- 里程碑：2022｜Varadi 等的資料庫收錄逾兩億個預測結構｜Varadi et al. 2022, Nucleic Acids Research 50:D439-D444
- 里程碑：2023｜Watson 等以 RFdiffusion 從頭設計蛋白質｜Watson et al. 2023, Nature 620:1089-1100
- 里程碑：2024｜Baker、Hassabis、Jumper 獲諾貝爾獎｜獎項
- 註記：前三項為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：三十億年演化留下的序列就是現成的訓練資料；把對稱性寫進架構，模型就不必再學旋轉。
- 轉變：拼湊管線→端到端
