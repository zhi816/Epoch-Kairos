# 卡片文字：2023-atayalic-multilingual-mt-liao

- **論文頁**：[2023-atayalic-multilingual-mt-liao](../papers/2023-atayalic-multilingual-mt-liao.md)
- **證據表**：[2023-atayalic-multilingual-mt-liao](../evidence/2023-atayalic-multilingual-mt-liao.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：合併泰雅、賽德克、／太魯閣語，／一起訓練翻譯
- 導語：三語共用子詞後，再借馬來語、印尼語模型微調。
- 封面標題：泛泰雅語群多語言機器翻譯

## Card 2｜世紀瓶頸
- 標題：資料少又不均，直接合併也不夠
- 對照：單語基準｜泰雅語與賽德克語辭典例句，都只有六千多句
- 對照：原文合併｜合併後，只有共用詞的資料增加了，中文譯族語方向全輸基準
- 缺口：子詞表示｜三語句法用詞相近卻不相同，缺少能共同表達三語的單位
- 結語：合併之前，三語得先有共同的單位。

## Card 3｜突破原理
- 標題：共用子詞與標籤，再借馬來語
- 公式：無
- 無公式理由：原文僅有評估指標公式：§1.4 式 1、2 為 BLEU 與平滑，式 3 Dice 係數只用於切分資料（p. 12）
- 說明：三語共用一套子詞，句首標明翻譯方向，再從馬來語、印尼語的模型微調。
- 圖類型：示意圖
- 圖說：示意：馬來語、印尼語與中文先訓練父模型，再以句首加上方向標籤的泛泰雅三語資料微調；兩邊共用一套子詞。

```svg
<svg viewBox="0 0 300 120" role="img" aria-label="示意：馬來語、印尼語與中文先訓練父模型，再以句首加上方向標籤的泛泰雅三語資料微調；兩邊共用一套子詞。">
  <rect class="k-ink k-ring" x="6" y="12" width="118" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="176" y="12" width="118" height="30" rx="4"/>
  <rect class="k-accent k-ring" x="6" y="78" width="118" height="30" rx="4"/>
  <rect class="k-accent k-ring" x="176" y="78" width="118" height="30" rx="4"/>
  <line class="k-ink" x1="124" y1="27" x2="174" y2="27"/>
  <polyline class="k-ink" points="169,22 174,27 169,32"/>
  <line class="k-ink" x1="124" y1="93" x2="174" y2="93"/>
  <polyline class="k-ink" points="169,88 174,93 169,98"/>
  <line class="k-ink" x1="235" y1="42" x2="235" y2="76"/>
  <polyline class="k-ink" points="230,71 235,76 240,71"/>
  <line class="k-muted k-dash" x1="65" y1="44" x2="65" y2="76"/>
  <text class="k-label" x="65" y="31" text-anchor="middle">馬來語、印尼語</text>
  <text class="k-label" x="235" y="31" text-anchor="middle">父模型</text>
  <text class="k-label-accent" x="65" y="97" text-anchor="middle">泛泰雅三語</text>
  <text class="k-label-accent" x="235" y="97" text-anchor="middle">翻譯系統</text>
  <text class="k-label" x="246" y="63" text-anchor="start">微調</text>
  <text class="k-label" x="76" y="63" text-anchor="start">子詞</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：19.38｜賽德克語譯成中文 BLEU，多語言遷移式學習｜表 21, p. 34
- 數字：15.50｜同方向，只用辭典例句的單語基準｜表 6, p. 23
- 數字：21.97｜中文譯成賽德克語 BLEU，多語言遷移式學習｜表 22, p. 35
- 數字：16.15｜同方向，只用辭典例句的單語基準｜表 7, p. 24
- 範圍：廖恒慶 2023，交叉驗證；外部測試偏高未採用

## Card 5｜典範轉移
- 標題：語料與做法，延伸到下一批論文
- 里程碑：2025｜金柏毅沿用本篇語料，再加入詞綴資訊｜金柏毅 2025, 國立臺灣海洋大學碩士論文
- 里程碑：2025｜吳維中把同套方法用到排灣語、布農語｜吳維中 2025, 國立臺灣海洋大學碩士論文
- 里程碑：2025｜楊鈞凱採用本篇整理的 E 樂園例句｜楊鈞凱 2025, 國立臺灣海洋大學碩士論文
- 註記：以上為同實驗室 2025 年之碩士論文，頁碼見長文

## Card 6｜Kairos
- 結語：族語資源常互相轉載例句，測試句可能已在訓練集中。
- 轉變：只看分數→先查重疊
