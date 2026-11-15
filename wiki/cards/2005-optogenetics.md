# 卡片文字：2005-optogenetics

- **論文頁**：[2005-optogenetics](../papers/2005-optogenetics.md)
- **證據表**：[2005-optogenetics](../evidence/2005-optogenetics.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-15
- **最後核對**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-15

## 封面
- 封面斷行：用一道藍光，／開關大腦裡／特定的神經元
- 導語：將綠藻光敏離子通道基因導入哺乳動物神經元，以短促藍光脈衝直接控制神經元放電與突觸傳遞。

## Card 2｜世紀瓶頸
- 標題：毫秒精度與細胞專一性難以兼得
- 對照：電刺激｜反應雖達毫秒級，電流擴散卻會無差別激活周圍各類神經元
- 對照：化學藥物｜透過受體精確作用特定細胞，但擴散代謝需數秒至數十分鐘
- 缺口：光控開關｜缺乏同時具備細胞專一性與毫秒級動態調控的遺傳工具
- 結語：系統神經研究亟盼以光精密操控迴路的工具。

## Card 3｜突破原理
- 標題：一道藍光驅動單一微生物離子通道
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，光電流動力學與脈衝放電以電生理波形及統計圖呈現
- 說明：將單一光敏感通道蛋白導入神經元，藍光照射開啟陽離子內流並於毫秒內誘發放電。
- 圖類型：示意圖
- 圖說：示意：藍光照射導入神經元的單一光敏感通道蛋白後，陽離子迅速內流促使去極化，短脈衝即可精準誘發動作電位。

```svg
<svg viewBox="0 0 300 180" role="img" aria-label="示意：藍光照射導入神經元的單一光敏感通道蛋白後，陽離子迅速內流促使去極化，短脈衝即可精準誘發動作電位。">
  <rect class="k-ink k-ring" x="24" y="20" width="64" height="30" rx="4"/>
  <text class="k-label-accent" x="56" y="39" text-anchor="middle">藍光</text>
  <line class="k-accent" x1="88" y1="35" x2="124" y2="56"/>
  <polyline class="k-accent" points="116,58 124,56 121,49"/>
  <line class="k-muted k-dash" x1="20" y1="74" x2="120" y2="74"/>
  <line class="k-muted k-dash" x1="180" y1="74" x2="280" y2="74"/>
  <rect class="k-soft" x="120" y="54" width="60" height="40" rx="6"/>
  <rect class="k-line k-ring" x="120" y="54" width="60" height="40" rx="6"/>
  <text class="k-label" x="150" y="78" text-anchor="middle">離子通道</text>
  <line class="k-accent" x1="150" y1="94" x2="150" y2="122"/>
  <polyline class="k-accent" points="146,116 150,122 154,116"/>
  <text class="k-label-accent" x="88" y="114" text-anchor="middle">陽離子</text>
  <rect class="k-ink k-ring" x="108" y="128" width="84" height="32" rx="4"/>
  <text class="k-label" x="150" y="148" text-anchor="middle">去極化</text>
  <line class="k-ink" x1="192" y1="144" x2="220" y2="144"/>
  <polyline class="k-ink" points="214,140 220,144 214,148"/>
  <rect class="k-soft" x="224" y="128" width="62" height="32" rx="4"/>
  <rect class="k-line k-ring" x="224" y="128" width="62" height="32" rx="4"/>
  <text class="k-label-accent" x="255" y="148" text-anchor="middle">動作電位</text>
  <text class="k-label" x="234" y="39" text-anchor="middle">神經元</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：496 pA｜藍光誘發全細胞向內峰值電流均值（穩態 193 pA）｜p. 1264、Fig. 1b
- 數字：0.5 ms｜穩定光照首個動作電位之跨試驗平均時間抖動｜pp. 1264–1265、Fig. 1d
- 數字：>95%｜相同帕松脈衝序列重複刺激之跨試驗一致率｜p. 1265、Fig. 2b
- 數字：30 Hz｜穩定驅動神經元跟隨光脈衝放電之測試上限頻率｜p. 1265、Fig. 3
- 範圍：Boyden 等 2005，大鼠海馬體離體培養神經元實驗

## Card 5｜典範轉移
- 標題：大腦研究從觀察推進至因果操控
- 里程碑：2007｜Aravanis 等以植入光纖在清醒小鼠實現活體光控｜Aravanis et al. 2007, J Neural Eng 4:S143-S156
- 里程碑：2009｜Gradinaru 等以光控釐清帕金森深腦刺激作用標的｜Gradinaru et al. 2009, Science 324:354-359
- 里程碑：2012｜Liu 等藉光控海馬體細胞實現特定恐懼記憶召回｜Liu et al. 2012, Nature 484:381-385
- 里程碑：2026｜Deisseroth、Hegemann 與 Nagel 獲諾貝爾獎｜獎項
- 註記：前三項為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：單細胞綠藻演化出的光敏開關，意外成為解鎖大腦毫秒尺度因果關係的分子鑰匙。
- 轉變：觀察相關性→光控因果關係
