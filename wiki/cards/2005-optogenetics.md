# 卡片文字：2005-optogenetics

- **論文頁**：[2005-optogenetics](../papers/2005-optogenetics.md)
- **證據表**：[2005-optogenetics](../evidence/2005-optogenetics.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-10
- **最後核對**：Antigravity by Google DeepMind（Gemini 3.8 Flash），2026-11-10

## 封面
- 封面斷行：用一道藍光，／開關大腦裡／特定的神經元
- 導語：把綠藻的感光蛋白放進神經元，讓科學家能用一道藍光在千分之一秒內開關放電，把大腦研究推進到精準因果控制。

## Card 2｜世紀瓶頸
- 標題：快的不準，準的不快
- 對照：微電極刺激｜達到毫秒級速度，但電流擴散無差別激活周圍神經元
- 對照：化學藥物｜能依受體專一作用，但擴散代謝需數秒至數分鐘
- 缺口：工具｜沒有同時兼具細胞專一性與毫秒時間解析度的控制手段
- 結語：控制大腦需要兼具專一與即時的開關。

## Card 3｜突破原理
- 標題：一道藍光，一個分子開關
- 公式：無
- 無公式理由：原文無公式：全篇為實驗技術報告，以文字與圖表記述光電流，無編號數學公式
- 說明：藍光照射使通道構象改變，陽離子內流去極化，毫秒內誘發神經元放電。
- 圖類型：示意圖
- 圖說：示意：藍光照射質膜上的光敏通道，促使陽離子內流並誘發神經元放電。

```svg
<svg viewBox="0 0 300 126" role="img" aria-label="示意：藍光照射質膜上的光敏通道，促使陽離子內流並誘發神經元放電。">
  <rect class="k-soft" x="10" y="46" width="280" height="24" rx="2"/>
  <text class="k-label" x="282" y="62" text-anchor="end">質膜</text>
  <line class="k-line" x1="70" y1="18" x2="70" y2="42"/>
  <polyline class="k-line" points="66,36 70,42 74,36"/>
  <line class="k-line" x1="86" y1="18" x2="86" y2="42"/>
  <polyline class="k-line" points="82,36 86,42 90,36"/>
  <text class="k-label-accent" x="78" y="14" text-anchor="middle">藍光照射</text>
  <rect class="k-accent k-ring" x="110" y="40" width="80" height="36" rx="4"/>
  <text class="k-label-accent" x="150" y="62" text-anchor="middle">光敏通道</text>
  <line class="k-line" x1="150" y1="42" x2="150" y2="98"/>
  <polyline class="k-line" points="144,92 150,98 156,92"/>
  <circle class="k-ink" cx="136" cy="92" r="3"/>
  <circle class="k-ink" cx="164" cy="92" r="3"/>
  <text class="k-label" x="150" y="114" text-anchor="middle">陽離子內流</text>
  <path class="k-line" d="M 220 102 Q 235 102 242 82 Q 248 68 254 102"/>
  <text class="k-label" x="246" y="116" text-anchor="middle">動作電位</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：8.0 ms｜恆定光照誘發首發動作電位延遲時間｜p. 1263，Fig. 1d
- 數字：<5 ms｜高頻光脈衝序列放電之整體時間抖動｜p. 1264，Fig. 3d
- 數字：496 pA｜藍光照射誘發全細胞峰值內向光電流｜p. 1263，Fig. 1b
- 數字：5.1 s｜暗處光電流自發恢復之擬合時間常數｜p. 1263，Fig. 1c
- 範圍：Boyden 等 2005，離體培養大鼠海馬神經元，概念驗證

## Card 5｜典範轉移
- 標題：從觀察大腦相關性，到操控因果
- 里程碑：2007｜Aravanis 等以植入光纖在活體小鼠實現光控｜Aravanis et al. 2007, J Neural Eng 4:S143-S156
- 里程碑：2009｜Gradinaru 等釐清帕金森氏症深腦刺激靶點｜Gradinaru et al. 2009, Science 324:354-359
- 里程碑：2012｜Liu 等在小鼠海馬體實現恐懼記憶印痕召回｜Liu et al. 2012, Nature 484:381-385
- 里程碑：2026｜Deisseroth、Hegemann 與 Nagel 獲諾貝爾獎｜獎項
- 註記：前三項為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：困擾神經科學近百年的難題，解答不在神經科學內部，而在單細胞綠藻的冷門角落。
- 轉變：觀察相關→操控因果
