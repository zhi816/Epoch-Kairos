# 卡片文字：2024-formosan-mt-bilingual-lexicon-zheng

- **論文頁**：[2024-formosan-mt-bilingual-lexicon-zheng](../papers/2024-formosan-mt-bilingual-lexicon-zheng.md)
- **證據表**：[2024-formosan-mt-bilingual-lexicon-zheng](../evidence/2024-formosan-mt-bilingual-lexicon-zheng.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09

## 封面
- 封面斷行：把族語辭典的詞條／拿來訓練，／改善族語翻譯
- 導語：平行句太少時，辭典詞條也能當成平行句用。
- 封面標題：雙語詞彙資源改善臺灣南島語言翻譯

## Card 2｜世紀瓶頸
- 標題：平行句太少，辭典常被忽略
- 對照：平行語料｜每種語言只有約 4,400 至 10,400 句，神經翻譯通常要數百萬句
- 對照：雙語詞典｜容易取得、能補罕見詞，缺上下文
- 缺口：做法｜既有研究多拿詞典替換句中詞彙，詞條本身未直接拿來訓練
- 結語：需要更簡單的方式，把現成詞典交給模型。

## Card 3｜突破原理
- 標題：把詞條當成額外的平行句
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，BLEU 與 chrF 只引用、未列式（p. 11251）
- 說明：詞條直接當平行句；另以詞典替換族語端詞彙造偽平行句，兩者並用最佳。
- 圖類型：示意圖
- 圖說：示意：辭典的詞條當平行句，或拿來替換族語詞造出偽平行句，兩者與原有平行句一起送進翻譯模型。

```svg
<svg viewBox="0 0 300 120" role="img" aria-label="示意：辭典的詞條當平行句，或拿來替換族語詞造出偽平行句，兩者與原有平行句一起送進翻譯模型。">
  <rect class="k-ink k-ring" x="4" y="46" width="46" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="80" y="8" width="104" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="96" y="48" width="72" height="24" rx="4"/>
  <rect class="k-ink k-ring" x="80" y="86" width="104" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="226" y="46" width="70" height="28" rx="4"/>
  <polyline class="k-line" points="27,46 27,22 78,22"/>
  <polyline class="k-line" points="72,17 78,22 72,27"/>
  <polyline class="k-ink" points="27,74 27,100 78,100"/>
  <polyline class="k-ink" points="72,95 78,100 72,105"/>
  <line class="k-ink k-dash" x1="132" y1="72" x2="132" y2="84"/>
  <polyline class="k-ink" points="128,79 132,84 136,79"/>
  <polyline class="k-line" points="184,22 250,22 250,44"/>
  <polyline class="k-line" points="245,38 250,44 255,38"/>
  <line class="k-ink" x1="168" y1="60" x2="224" y2="60"/>
  <polyline class="k-ink" points="218,55 224,60 218,65"/>
  <polyline class="k-ink" points="184,100 250,100 250,76"/>
  <polyline class="k-ink" points="245,82 250,76 255,82"/>
  <text class="k-label" x="27" y="64" text-anchor="middle">辭典</text>
  <text class="k-label-accent" x="132" y="26" text-anchor="middle">詞條當平行句</text>
  <text class="k-label" x="132" y="64" text-anchor="middle">原有平行句</text>
  <text class="k-label" x="132" y="104" text-anchor="middle">替換族語詞</text>
  <text class="k-label" x="214" y="92" text-anchor="middle">偽平行句</text>
  <text class="k-label" x="261" y="64" text-anchor="middle">翻譯模型</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：+3.37｜只加詞條，16 種語言與華語雙向平均 BLEU 增幅｜表 2, p. 11252
- 數字：+0.51｜外部辭典加偽平行句，賽德克語→華語 BLEU 增幅｜表 10, §5.2, pp. 11254–11255
- 數字：+3.11｜卡那卡那富語→華語，加 4,000 條詞條 BLEU 增幅｜§5, p. 11253
- 數字：+6.22｜同一方向改加 4,000 句平行句的 BLEU 增幅｜§5, p. 11253
- 範圍：Zheng 等 2024，詞條幾乎都出現在平行句中，效果或偏高

## Card 5｜典範轉移
- 模式：新論文
- 標題：留下資料，也留下重疊難題
- 里程碑：2024｜作者整理 16 種臺灣南島語的平行句與詞典｜本篇 §3
- 里程碑：2024｜作者指出詞典與平行句的重疊難以界定｜本篇 §5.2
- 里程碑：2024｜作者指出可用的外部詞典很少｜本篇 §5.2
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：評估詞典增益時，宜另用與詞典來源不同的測試句，避免重疊抬高成績。
- 轉變：只用平行句→加入詞條
