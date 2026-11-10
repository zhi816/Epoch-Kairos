# 卡片文字：2026-tao-filipino-nmt-macayan

- **論文頁**：[2026-tao-filipino-nmt-macayan](../papers/2026-tao-filipino-nmt-macayan.md)
- **證據表**：[2026-tao-filipino-nmt-macayan](../evidence/2026-tao-filipino-nmt-macayan.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：借親屬語伊巴丹語，／把達悟語／譯成菲律賓語
- 導語：親屬語預訓練與辭典合成資料，各有所長。
- 封面標題：達悟語－菲律賓語翻譯

## Card 2｜世紀瓶頸
- 標題：只有聖經，學不會日常對話
- 對照：聖經語料｜主要平行資料是新約經文，模型偏向古老句構與用詞
- 對照：NLLB-200｜多語翻譯模型，預訓練有他加祿語，卻沒有巴丹語群語言
- 缺口：會話資料｜只靠經文，模型難以處理日常會話
- 結語：得替日常會話另找翻譯資料。

## Card 3｜突破原理
- 標題：借親屬語暖身，用辭典補會話
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，僅有合成資料量之乘算（p. 32）
- 說明：先用同屬巴丹語群的伊巴丹語預訓練，再以聖經與辭典轉譯的會話句微調。
- 圖類型：示意圖
- 圖說：示意：先以伊巴丹語預訓練模型，再用聖經與辭典例句轉成的會話資料微調達悟語。

```svg
<svg viewBox="0 0 300 126" role="img" aria-label="示意：先以伊巴丹語預訓練模型，再用聖經與辭典例句轉成的會話資料微調達悟語。">
  <rect class="k-ink k-ring" x="4" y="40" width="72" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="106" y="40" width="84" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="214" y="40" width="82" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="200" y="98" width="42" height="24" rx="4"/>
  <rect class="k-ink k-ring" x="248" y="98" width="48" height="24" rx="4"/>
  <line class="k-ink" x1="76" y1="54" x2="104" y2="54"/>
  <polyline class="k-ink" points="98,49 104,54 98,59"/>
  <line class="k-ink" x1="190" y1="54" x2="212" y2="54"/>
  <polyline class="k-ink" points="206,49 212,54 206,59"/>
  <line class="k-ink" x1="221" y1="96" x2="221" y2="72"/>
  <polyline class="k-ink" points="216,78 221,72 226,78"/>
  <line class="k-ink" x1="272" y1="96" x2="272" y2="72"/>
  <polyline class="k-ink" points="267,78 272,72 277,78"/>
  <text class="k-label" x="40" y="58" text-anchor="middle">伊巴丹語</text>
  <text class="k-label" x="148" y="58" text-anchor="middle">預訓練模型</text>
  <text class="k-label-accent" x="255" y="58" text-anchor="middle">微調達悟語</text>
  <text class="k-label" x="221" y="114" text-anchor="middle">聖經</text>
  <text class="k-label" x="272" y="114" text-anchor="middle">辭典例句</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：34.85｜伊巴丹語預訓練後，聖經測試 BLEU｜表 3, p. 33
- 數字：32.00｜只用聖經語料的基線，聖經測試 BLEU｜表 3, p. 33
- 數字：6.67｜加辭典合成資料，域外會話 BLEU（內文 6.61）｜表 3, p. 33
- 數字：3.12｜同一基線之域外會話 BLEU｜表 3, p. 33
- 範圍：Macayan 等 2026，達悟語→他加祿語；聖經 200 句、會話 20 句

## Card 5｜典範轉移
- 模式：新論文
- 標題：斷詞與人工評估，留待下一步
- 里程碑：2026｜只研究達悟語→他加祿語一個語言對｜本篇 Limitations, p. 34
- 里程碑：2026｜沒有人工評估，指標測不到比喻與偏誤｜本篇 Limitations, p. 34
- 里程碑：2026｜建議改用子詞斷詞，處理罕見詞與構詞｜本篇 §7, p. 34
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：與達悟語越近的親屬語，越能幫上忙：先學伊巴丹語，經文翻得更好。
- 轉變：只靠本語→借力親屬語
