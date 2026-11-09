# 卡片文字：2024-taiwanese-mt-resegmentation-tang

- **論文頁**：[2024-taiwanese-mt-resegmentation-tang](../papers/2024-taiwanese-mt-resegmentation-tang.md)
- **證據表**：[2024-taiwanese-mt-resegmentation-tang](../evidence/2024-taiwanese-mt-resegmentation-tang.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：對齊台語／與華語的斷詞，／改善台華翻譯
- 導語：部分台語語料未照斷詞標準，作者依華語句重切。

## Card 2｜世紀瓶頸
- 標題：台語斷詞不一，台華又不同調
- 對照：iCorpus｜斷詞像子句：「都佇來到」連成一詞
- 對照：TGB 通訊｜同句中「統治者」連寫、「抗爭 者」卻斷開
- 缺口：斷詞標準｜台語端斷詞不一，與華語端的斷詞標準也沒有對齊
- 結語：作者推論：兩邊切法一致，翻譯可能更好。

## Card 3｜突破原理
- 標題：照華語句，重切台語的詞
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，對齊計分以文字與算例敘述（§3.3）
- 說明：先找出總分最高的台華詞對應，再把台語沒對上的詞，照華語斷法重新切開。
- 圖類型：示意圖
- 圖說：示意：台語原本連寫成一詞（虛線），依華語「更 擔心」的斷法重切為「閣 煩惱」並一一對應。

```svg
<svg viewBox="0 0 300 112" role="img" aria-label="示意：台語原本連寫成一詞（虛線），依華語「更 擔心」的斷法重切為「閣 煩惱」並一一對應。">
  <rect class="k-ink k-ring" x="84" y="10" width="44" height="24" rx="4"/>
  <rect class="k-ink k-ring" x="164" y="10" width="60" height="24" rx="4"/>
  <rect class="k-accent k-ring" x="84" y="74" width="44" height="24" rx="4"/>
  <rect class="k-accent k-ring" x="164" y="74" width="60" height="24" rx="4"/>
  <line class="k-line" x1="106" y1="36" x2="106" y2="72"/>
  <line class="k-line" x1="194" y1="36" x2="194" y2="72"/>
  <line class="k-muted k-dash" x1="84" y1="106" x2="224" y2="106"/>
  <line class="k-muted" x1="84" y1="101" x2="84" y2="106"/>
  <line class="k-muted" x1="224" y1="101" x2="224" y2="106"/>
  <text class="k-label" x="36" y="26" text-anchor="middle">華語</text>
  <text class="k-label" x="36" y="90" text-anchor="middle">台語</text>
  <text class="k-label" x="106" y="26" text-anchor="middle">更</text>
  <text class="k-label" x="194" y="26" text-anchor="middle">擔心</text>
  <text class="k-label-accent" x="106" y="90" text-anchor="middle">閣</text>
  <text class="k-label-accent" x="194" y="90" text-anchor="middle">煩惱</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：90.69%｜BERT 台語斷詞 F1（不保留連音號）｜§4.1, p. 37
- 數字：43.47｜TGB 台語→華語詞級 BLEU，基準 37.81｜表 15, p. 50
- 數字：79.02｜iCorpus 台語→華語詞級 BLEU，基準 72.01｜表 15, p. 50
- 數字：16.29%｜TGB 原始語料重斷詞後，未能對應的詞｜第五章, p. 51
- 範圍：湯景閔 2024，BERT 斷詞再重斷詞對比只用 BERT；字級提升較小

## Card 5｜典範轉移
- 模式：新論文
- 標題：評估與詞典，都還待補強
- 里程碑：2024｜正解斷詞不同，分數不太能直接相比｜本篇 §4.3.3, p. 48
- 里程碑：2024｜作者計畫擴充台語詞典、增設對應規則｜本篇 第五章, pp. 51–52
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：改了斷詞，詞級 BLEU 就跟著變；比較方法時，字級分數也要一起看。
- 轉變：各自斷詞→對齊斷詞
