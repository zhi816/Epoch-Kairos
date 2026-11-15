# 卡片文字：2023-drugclip

- **論文頁**：[2023-drugclip](../papers/2023-drugclip.md)
- **證據表**：[2023-drugclip](../evidence/2023-drugclip.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-15
- **最後核對**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-15

## 封面
- 封面斷行：不再逐一模擬，／從海量分子中／快速挑出候選藥
- 導語：把蛋白質口袋與小分子映進同一三維向量空間，靠預先編碼的向量比對高速篩藥，不必逐一對接。

## Card 2｜世紀瓶頸
- 標題：物理對接太慢，回歸模型難泛化
- 對照：分子對接｜須逐一採樣三維結合姿態，篩選十億級化合物庫動輒耗時數千年
- 對照：親和力回歸｜實驗結合力資料稀少且缺負樣本，模型易死記骨架而難跨靶點
- 缺口：方法｜缺乏既不依賴姿態採樣、又能跨靶點排序候選分子的表徵方法
- 結語：虛擬篩選需要直接對齊口袋與分子的檢索架構。

## Card 3｜突破原理
- 標題：把篩藥變成口袋與分子的向量配對
- 公式：\mathcal{L} = \frac{1}{2} \sum_{k=1}^N \left( \mathcal{L}_k^p + \mathcal{L}_k^m \right)
- 說明：平均雙向對比損失讓互補口袋與分子在嵌入空間靠近，推論期僅需計算向量內積。
- 圖類型：示意圖
- 圖說：示意：分子編碼器與口袋編碼器將結構映為向量後計算內積，在嵌入空間拉近正樣本對、推開負樣本。

```svg
<svg viewBox="0 0 300 128" role="img" aria-label="示意：分子編碼器與口袋編碼器將結構映為向量後計算內積，在嵌入空間拉近正樣本對、推開負樣本。">
  <rect class="k-ink k-ring" x="10" y="18" width="84" height="32" rx="4"/>
  <text class="k-label" x="52" y="38" text-anchor="middle">分子編碼器</text>
  <rect class="k-ink k-ring" x="10" y="78" width="84" height="32" rx="4"/>
  <text class="k-label" x="52" y="98" text-anchor="middle">口袋編碼器</text>
  <line class="k-ink" x1="94" y1="34" x2="132" y2="52"/>
  <polyline class="k-ink" points="125,54 132,52 129,45"/>
  <line class="k-ink" x1="94" y1="94" x2="132" y2="76"/>
  <polyline class="k-ink" points="129,83 132,76 125,74"/>
  <rect class="k-soft" x="138" y="16" width="152" height="96" rx="4"/>
  <rect class="k-line k-ring" x="138" y="16" width="152" height="96" rx="4"/>
  <text class="k-label-accent" x="214" y="34" text-anchor="middle">向量內積</text>
  <circle class="k-accent" cx="164" cy="58" r="4.5"/>
  <circle class="k-accent" cx="192" cy="58" r="4.5"/>
  <line class="k-line" x1="169" y1="58" x2="187" y2="58"/>
  <text class="k-label-accent" x="244" y="62" text-anchor="middle">正樣本對</text>
  <circle class="k-muted k-ring" cx="156" cy="88" r="4"/>
  <circle class="k-muted k-ring" cx="200" cy="88" r="4"/>
  <line class="k-muted k-dash" x1="162" y1="88" x2="194" y2="88"/>
  <text class="k-label" x="244" y="92" text-anchor="middle">負樣本</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：31.89｜DUD-E 零樣本 EF 1%，對照 Glide-SP 為 16.18｜Table 1，p. 7
- 數字：50.52%｜DUD-E 零樣本 BEDROC，對照 Glide-SP 為 40.70%｜Table 1，p. 7
- 數字：5.51｜LIT-PCBA 零樣本 EF 1%，對照 Gnina 為 4.63｜Table 3，p. 8
- 數字：4/5｜ChemDiv 盲篩中專家評審偏好 DrugCLIP 之靶點比例｜§4.5、Table 8
- 範圍：Gao 等 2023，兩項零樣本虛擬篩選基準與 60 億庫測時

## Card 5｜典範轉移
- 標題：對比檢索走向全基因組與濕實驗
- 里程碑：2025｜Feng 等提出 LigUnity，串接篩選與親和力排序｜Feng et al. 2025, Patterns 6:101371
- 里程碑：2026｜Jia 等擴展至全人類基因組並取得濕實驗命中率｜Jia et al. 2026, Science 391:eads9530
- 里程碑：2026｜He 等結合蛋白質序列預訓練與三維口袋對比學習｜He et al. 2026, AAAI 40:354-362
- 里程碑：2026｜Zhang 評述 DrugCLIP 與全基因組藥物探索挑戰｜Zhang 2026, Drug Dev. Res. 87:e70351
- 註記：以上皆為後續延伸與獨立研究，出處見長文

## Card 6｜Kairos
- 結語：把口袋與小分子看作兩種語言，用對比排序取代逐一算結合能，才能在百億空間裡篩藥。
- 轉變：逐一模擬結合→向量空間排序
