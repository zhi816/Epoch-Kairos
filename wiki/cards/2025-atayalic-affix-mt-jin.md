# 卡片文字：2025-atayalic-affix-mt-jin

- **論文頁**：[2025-atayalic-affix-mt-jin](../papers/2025-atayalic-affix-mt-jin.md)
- **證據表**：[2025-atayalic-affix-mt-jin](../evidence/2025-atayalic-affix-mt-jin.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：測試加入詞綴資訊，／能否改善／泰雅語群翻譯
- 導語：把詞綴拆給模型看，族語與中文互譯都進步。

## Card 2｜世紀瓶頸
- 標題：要用詞綴，卻缺詞綴標記
- 對照：叢書｜有學者標記的詞綴，但量太小，無法訓練神經網路
- 對照：線上辭典｜資料較多，泰雅語、太魯閣語詞綴靠解析器猜測
- 對照：E 樂園｜沿用辭典預測，查不到的詞視為詞根
- 缺口：資料｜沒有大量且人工標記詞綴的訓練語料
- 結語：詞綴資訊多半靠程式預測，未必全對。

## Card 3｜突破原理
- 標題：拆出詞綴，再用兩個編碼器
- 公式：無
- 無公式理由：原文僅有評估指標公式：§1.3.3 公式 1 至 4 為 BLEU 與 chrF（pp. 6–7）
- 說明：詞綴與詞根斷開成字串，另把詞綴特徵送進第二個編碼器，兩路輸出串接後再翻譯。
- 圖類型：示意圖
- 圖說：示意：族語句改寫成詞綴字串，詞綴特徵另走一個編碼器，兩路輸出串接後送入解碼器譯成中文。

```svg
<svg viewBox="0 0 300 106" role="img" aria-label="示意：族語句改寫成詞綴字串，詞綴特徵另走一個編碼器，兩路輸出串接後送入解碼器譯成中文。">
  <rect class="k-ink k-ring" x="4" y="12" width="62" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="4" y="66" width="62" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="88" y="12" width="56" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="88" y="66" width="56" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="188" y="39" width="56" height="28" rx="4"/>
  <line class="k-ink" x1="68" y1="26" x2="86" y2="26"/>
  <polyline class="k-ink" points="81,21 86,26 81,31"/>
  <line class="k-accent" x1="68" y1="80" x2="86" y2="80"/>
  <polyline class="k-accent" points="81,75 86,80 81,85"/>
  <polyline class="k-line" points="146,26 164,26 164,80 146,80"/>
  <line class="k-line" x1="164" y1="53" x2="186" y2="53"/>
  <polyline class="k-line" points="181,48 186,53 181,58"/>
  <line class="k-ink" x1="246" y1="53" x2="262" y2="53"/>
  <polyline class="k-ink" points="257,48 262,53 257,58"/>
  <text class="k-label" x="35" y="30" text-anchor="middle">詞綴字串</text>
  <text class="k-label" x="35" y="84" text-anchor="middle">詞綴特徵</text>
  <text class="k-label" x="116" y="30" text-anchor="middle">編碼器</text>
  <text class="k-label-accent" x="116" y="84" text-anchor="middle">編碼器</text>
  <text class="k-label" x="216" y="57" text-anchor="middle">解碼器</text>
  <text class="k-label" x="281" y="57" text-anchor="middle">中文</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：19.75｜泰雅語→中文 BLEU，單一族語原文基線｜§4.2.3, p. 50
- 數字：23.84｜同方向，泛泰雅＋詞綴字串＋雙編碼器｜§4.2.3, p. 50
- 數字：28.06｜中文→泰雅語 BLEU，只換 BERT 編碼器｜表 19, pp. 55–56
- 數字：29.49｜同方向，BERT 加詞綴字串形式｜表 19, pp. 55–56
- 範圍：金柏毅 2025，交叉驗證；中文→泰雅語基線為 21.49

## Card 5｜典範轉移
- 模式：新論文
- 標題：其他族語，還待驗證
- 里程碑：2025｜作者計畫在其他臺灣南島語驗證效果｜本篇 p. 71
- 里程碑：2025｜作者想找與 BERT 一樣好的中文解碼器｜本篇 p. 71
- 里程碑：2025｜外部測試中，族語翻中文以原文形式最佳｜本篇 §4.2.4, p. 50
- 註記：皆引自本篇第四、五章

## Card 6｜Kairos
- 結語：換上更強的預訓練編碼器，進步可能大過構詞特徵，實驗要能分開比較。
- 轉變：只看總分→拆開來源
