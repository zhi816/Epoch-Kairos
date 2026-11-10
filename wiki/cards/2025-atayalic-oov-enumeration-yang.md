# 卡片文字：2025-atayalic-oov-enumeration-yang

- **論文頁**：[2025-atayalic-oov-enumeration-yang](../papers/2025-atayalic-oov-enumeration-yang.md)
- **證據表**：[2025-atayalic-oov-enumeration-yang](../evidence/2025-atayalic-oov-enumeration-yang.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：窮舉構詞變化，／替沒見過的／泰雅語群詞找詞根
- 導語：猜出未知詞的詞根，才能再查語意、拆構詞。
- 封面標題：以構詞規則窮舉解決泛泰雅語未知詞

## Card 2｜世紀瓶頸
- 標題：沒見過的詞，詞根該怎麼猜？
- 對照：未知詞｜翻譯時佔不小比例，又無詞根資訊
- 對照：候選詞根｜賽德克語 mkdesun 的正解是 adis，但 idas、daus 也對得上
- 對照：詞根集合｜最大集合僅涵蓋 E 樂園 659 詞中 524 詞的正解
- 缺口：猜測｜未知詞與已知詞根之間可能的對應太多，難以直接判定
- 結語：詞根猜得出來，構詞與語意才能接著分析。

## Card 3｜突破原理
- 標題：先窮舉變化，再兩兩比較
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，成對組合數與差值、比例僅於行文帶過（p. 44）
- 說明：列出每個詞根的各種變化形去比對未知詞，再讓隨機森林兩兩比較候選，得票最多者勝。
- 圖類型：示意圖
- 圖說：示意：未知詞先與各詞根的變化形比對得出候選，候選兩兩送入隨機森林比較，票數最高者為詞根。

```svg
<svg viewBox="0 0 300 110" role="img" aria-label="示意：未知詞先與各詞根的變化形比對得出候選，候選兩兩送入隨機森林比較，票數最高者為詞根。">
  <rect class="k-ink k-ring" x="4" y="46" width="46" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="62" y="46" width="66" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="184" y="46" width="56" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="256" y="46" width="40" height="28" rx="4"/>
  <line class="k-ink" x1="51" y1="60" x2="60" y2="60"/>
  <polyline class="k-ink" points="55,55 60,60 55,65"/>
  <line class="k-ink" x1="129" y1="60" x2="141" y2="60"/>
  <polyline class="k-ink" points="136,55 141,60 136,65"/>
  <line class="k-muted k-thin" x1="148" y1="44" x2="164" y2="60"/>
  <line class="k-muted k-thin" x1="164" y1="60" x2="148" y2="76"/>
  <line class="k-muted k-thin" x1="148" y1="44" x2="148" y2="76"/>
  <circle class="k-ink" cx="148" cy="44" r="4"/>
  <circle class="k-ink" cx="164" cy="60" r="4"/>
  <circle class="k-ink" cx="148" cy="76" r="4"/>
  <line class="k-ink" x1="170" y1="60" x2="182" y2="60"/>
  <polyline class="k-ink" points="177,55 182,60 177,65"/>
  <line class="k-line" x1="241" y1="60" x2="254" y2="60"/>
  <polyline class="k-line" points="249,55 254,60 249,65"/>
  <text class="k-label" x="27" y="64" text-anchor="middle">未知詞</text>
  <text class="k-label-accent" x="95" y="64" text-anchor="middle">變化形比對</text>
  <text class="k-label" x="156" y="30" text-anchor="middle">候選詞根</text>
  <text class="k-label" x="212" y="64" text-anchor="middle">兩兩比較</text>
  <text class="k-label" x="212" y="94" text-anchor="middle">隨機森林</text>
  <text class="k-label-accent" x="276" y="64" text-anchor="middle">詞根</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：90.50%｜賽德克語已知詞交叉驗證，隨機森林猜中詞根｜§4.5, p. 64
- 數字：63.88%｜同法於族語 E 樂園 659 個未知詞的猜中率｜表 38, p. 72
- 數字：72.12%｜臺大臺灣南島語語料庫 208 個未知詞的猜中率｜表 38, p. 72
- 數字：79.5%｜詞根集合涵蓋之上限，族語 E 樂園未知詞｜依原文表 15 計算, p. 46
- 範圍：楊鈞凱 2025，賽德克語；驗證為已知詞、測試為真實未知詞

## Card 5｜典範轉移
- 模式：新論文
- 標題：未知詞的詞根，常常也是未知
- 里程碑：2025｜作者指出不少未知詞的詞根也是未知詞｜本篇 p. 74
- 里程碑：2025｜作者捨棄書寫形式篩選，因濾掉過多正解｜本篇 p. 73
- 里程碑：2025｜作者以表 15 統計詞根集合涵蓋多少正解｜本篇 表 15
- 註記：三項均見於本篇，尚無後續研究

## Card 6｜Kairos
- 結語：先估算詞根集合裡有沒有正解，才分得清是排名錯了，還是資源不足。
- 轉變：只看正確率→先估上限
