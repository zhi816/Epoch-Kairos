# 卡片文字：2019-generalized-data-augmentation-xia

- **論文頁**：[2019-generalized-data-augmentation-xia](../papers/2019-generalized-data-augmentation-xia.md)
- **證據表**：[2019-generalized-data-augmentation-xia](../evidence/2019-generalized-data-augmentation-xia.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：借相近語言的語料，／擴充小語種翻譯資料
- 導語：把親屬高資源語言的平行語料逐詞換成低資源語言，在四組語言上勝過標準回譯。
- 封面標題：低資源翻譯之泛化資料增強

## Card 2｜世紀瓶頸
- 標題：回譯缺好模型，親屬語又不全通
- 對照：標準回譯｜反向模型太弱，合成資料品質差，白俄羅斯語反而變差
- 對照：親屬語言｜即使高度相關，仍有許多詞彙與句法不共享
- 缺口：模型設計｜以架構促進共享，卻增加計算與實作上的複雜度
- 結語：改從資料下手，把親屬語的語料轉過來。

## Card 3｜突破原理
- 標題：逐詞替換，再用無監督翻譯修飾
- 公式：\min_{W} \| W X - Y \|_F^2 \quad \text{s.t.} \quad W^\top W = I
- 說明：求正交矩陣 W 對齊兩語詞向量，得詞典後逐詞替換，再以無監督翻譯修飾。
- 圖類型：示意圖
- 圖說：示意：高資源句經詞典逐詞替換，再經無監督修飾，成為低資源句。

```svg
<svg viewBox="0 0 300 110" role="img" aria-label="示意：高資源句經詞典逐詞替換，再經無監督修飾，成為低資源句。">
  <rect class="k-ink k-ring" x="2" y="30" width="62" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="82" y="30" width="62" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="162" y="30" width="62" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="240" y="30" width="58" height="28" rx="4"/>
  <rect class="k-soft" x="87" y="78" width="52" height="22" rx="3"/>
  <line class="k-ink" x1="64" y1="44" x2="80" y2="44"/>
  <polyline class="k-ink" points="75,39 80,44 75,49"/>
  <line class="k-ink" x1="144" y1="44" x2="160" y2="44"/>
  <polyline class="k-ink" points="155,39 160,44 155,49"/>
  <line class="k-ink" x1="224" y1="44" x2="238" y2="44"/>
  <polyline class="k-ink" points="233,39 238,44 233,49"/>
  <line class="k-ink k-dash" x1="113" y1="78" x2="113" y2="60"/>
  <text class="k-label" x="33" y="48" text-anchor="middle">高資源句</text>
  <text class="k-label" x="113" y="48" text-anchor="middle">逐詞替換</text>
  <text class="k-label" x="193" y="48" text-anchor="middle">無監督修飾</text>
  <text class="k-label-accent" x="269" y="48" text-anchor="middle">低資源句</text>
  <text class="k-label" x="113" y="93" text-anchor="middle">詞典</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：16.34｜白俄羅斯語→英語，監督基線 BLEU｜表 2, p. 5791
- 數字：15.72｜同方向加標準回譯後，BLEU 反而下降｜表 2, p. 5791
- 數字：24.51｜同方向再加兩種來源的逐詞替換資料｜表 2, p. 5791
- 數字：1.5–8｜四組語言上，比標準回譯提升之 BLEU｜§1, p. 5787
- 範圍：Xia 等 2019，演講語料四組語言→英語；白俄羅斯語樞紐為俄語

## Card 5｜典範轉移
- 標題：沿親屬語與詞典延伸
- 里程碑：2021｜Ko 等以相近高資源語言調適低資源翻譯｜Ko et al. 2021, ACL-IJCNLP 2021:802-812
- 里程碑：2023｜Ranathunga 等指出成效看親緣與詞典｜Ranathunga et al. 2023, ACM Computing Surveys 55(11):229
- 里程碑：2023｜Jones 等以雙語詞典增強資料，公開 168 語詞典｜Jones et al. 2023, EMNLP 2023:371-405
- 註記：以上皆為引用本篇之後續研究，出處見長文

## Card 6｜Kairos
- 結語：借親屬語言的語料，前提是兩語詞彙相近；先確認能否建出可靠的詞典。
- 轉變：等資料出現→借親屬語料
