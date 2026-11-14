# 卡片文字：2026-data-centric-continual-pretraining-ji

- **論文頁**：[2026-data-centric-continual-pretraining-ji](../papers/2026-data-centric-continual-pretraining-ji.md)
- **證據表**：[2026-data-centric-continual-pretraining-ji](../evidence/2026-data-centric-continual-pretraining-ji.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14
- **最後核對**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14

## 封面

- 封面斷行：併入雙語平行句，／替語言模型／補足低資源語言
- 導語：彙整大規模雙語對照語料並併入後續訓練，讓既有語言模型學會翻譯與理解更多低資源語言。
- 封面標題：五百餘語言雙語持續預訓練
- 研究類型：多語預訓練

## Card 2｜世紀瓶頸

- 標題：五百餘語模型為何難跨出高資源
- 對照：單語混合｜只用單語網頁文本持續預訓練，缺乏跨語言對齊訊號
- 對照：平行資料｜多數僅有句對而無長文，若拆成單語串又會損及翻譯遷移
- 對照：過度預訓練｜高資源訓練極度飽和的基座，擴充語種時易起波動或退化
- 缺口：雙語混合｜缺橫跨五百語的雙語混合語料與降學習率全參數續訓方案
- 結語：需要兼具平行句與高穩定續訓的新方案。

## Card 3｜突破原理

- 標題：將句對串成偽文件併入全參數預訓
- 公式：無
- 無公式理由：原文無公式：全篇聚焦雙語語料編纂、混合配方與全參數持續預訓練之實證評測。
- 說明：每十句串成偽文件並併入雙語混合，再把學習率降至萬分之一，展開全參數續訓。
- 圖類型：示意圖
- 圖說：示意：雙語句對串成偽文件後與單語文本混編為雙語混合，經全參數續訓進行評測對照。

```svg
<svg viewBox="0 0 300 132" role="img" aria-label="示意：雙語句對串成偽文件後與單語文本混編為雙語混合，經全參數續訓進行評測對照。">
  <rect class="k-accent k-ring" x="8" y="14" width="60" height="28" rx="4"/>
  <text class="k-label-accent" x="38" y="32" text-anchor="middle">雙語句對</text>
  <line class="k-accent" x1="68" y1="28" x2="86" y2="28"/>
  <polyline class="k-accent" points="81,24 86,28 81,32"/>
  <rect class="k-ink k-ring" x="86" y="14" width="52" height="28" rx="4"/>
  <text class="k-label" x="112" y="32" text-anchor="middle">偽文件</text>
  <rect class="k-muted k-ring" x="8" y="70" width="96" height="28" rx="4"/>
  <text class="k-label" x="56" y="88" text-anchor="middle">單語文本</text>
  <polyline class="k-accent" points="138,28 176,28 176,48"/>
  <polyline class="k-muted" points="104,84 176,84 176,72"/>
  <rect class="k-soft" x="142" y="48" width="68" height="24" rx="4"/>
  <rect class="k-line k-ring" x="142" y="48" width="68" height="24" rx="4"/>
  <text class="k-label-accent" x="176" y="64" text-anchor="middle">雙語混合</text>
  <line class="k-ink" x1="210" y1="60" x2="224" y2="60"/>
  <polyline class="k-ink" points="219,56 224,60 219,64"/>
  <rect class="k-ink k-ring" x="224" y="46" width="68" height="28" rx="4"/>
  <text class="k-label" x="258" y="64" text-anchor="middle">全參數續訓</text>
  <polyline class="k-muted k-dash" points="258,74 258,112 150,112"/>
  <rect class="k-muted k-ring" x="62" y="100" width="88" height="24" rx="4"/>
  <text class="k-label" x="106" y="116" text-anchor="middle">評測對照</text>
</svg>
```

## Card 4｜決定性數據

- 模式：數字
- 數字：2,507｜MaLA 雙語翻譯語料庫涵蓋之跨語言對總數｜§2.1 p. 18778、Table 1
- 數字：24.02｜FLORES-200 英譯他語均分（基座 9.93 BLEU）｜Table 11, p. 18798
- 數字：25.99｜低資源子集英譯他語均分（單語續訓 22.03）｜Table 3, p. 18782
- 數字：88.18%｜FLORES-200 排名進入全組前三之語言比例｜Table 4, p. 18783
- 範圍：Ji 等 2026，7 任務 12 基準（分類與高資源閱讀理解見退化）

## Card 5｜典範轉移

- 模式：新論文
- 標題：從開源雙語語料到過度訓練基座瓶頸
- 里程碑：2026｜釋出 MaLA 雙語語料庫與四款八億模型｜本篇 Abstract, p. 18776
- 里程碑：2026｜雙語版現九項基準退化，高資源遺忘仍顯著｜本篇 §3.3, pp. 18782–18783
- 里程碑：2026｜受算力限制未窮舉比例，雙單語步數未等長｜本篇 Limitations, p. 18785
- 里程碑：2026｜尚未經偏好對齊與安全紅隊測試，不可直接部署｜本篇 Limitations, pp. 18784–18785
- 註記：以上皆出自本篇論文，尚無後續他人研究。

## Card 6｜Kairos

- 結語：大規模雙語平行資料能為飽和大模型打開低資源之門，也映出多語容量的代際權衡。
- 轉變：單語網頁預訓→雙語平行續訓
