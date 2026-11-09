# 卡片文字：2025-manchu-in-context-mt-pei

- **論文頁**：[2025-manchu-in-context-mt-pei](../papers/2025-manchu-in-context-mt-pei.md)
- **證據表**：[2025-manchu-in-context-mt-pei](../evidence/2025-manchu-in-context-mt-pei.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：找出哪些參考資料，／最能幫大模型／翻譯滿語
- 導語：詞典與相似例句最有用，語法書幾乎沒幫助。

## Card 2｜世紀瓶頸
- 標題：資源不少，卻不知哪個管用
- 對照：平行語料｜資料驅動的翻譯要靠它，這些語言卻很缺乏
- 對照：既有知識｜模型可能在預訓練時見過滿語，成績未必來自提示
- 缺口：相對重要性｜詞典、例句、語法書放進提示後，哪個最有用並不清楚
- 結語：得把每種資源拆開來，一項一項測。

## Card 3｜突破原理
- 標題：一次加一樣，再把滿語加密
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，僅以 π(·) 記號標示提示組合（§4）
- 說明：逐項加入詞典、例句等，留下最好的再加下一項；字母加密讓模型只能靠提示。
- 圖類型：示意圖
- 圖說：示意：構詞分析、詞典、例句、語法、思維鏈依序加入提示，前三項保留，後兩項不納入。

```svg
<svg viewBox="0 0 300 96" role="img" aria-label="示意：構詞分析、詞典、例句、語法、思維鏈依序加入提示，前三項保留，後兩項不納入。">
  <rect class="k-accent k-ring" x="2" y="24" width="62" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="79" y="24" width="42" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="136" y="24" width="42" height="28" rx="4"/>
  <rect class="k-muted k-ring" x="193" y="24" width="42" height="28" rx="4"/>
  <rect class="k-muted k-ring" x="250" y="24" width="46" height="28" rx="4"/>
  <line class="k-ink" x1="65" y1="38" x2="77" y2="38"/>
  <polyline class="k-ink" points="73,34 77,38 73,42"/>
  <line class="k-ink" x1="122" y1="38" x2="134" y2="38"/>
  <polyline class="k-ink" points="130,34 134,38 130,42"/>
  <line class="k-muted" x1="179" y1="38" x2="191" y2="38"/>
  <polyline class="k-muted" points="187,34 191,38 187,42"/>
  <line class="k-muted" x1="236" y1="38" x2="248" y2="38"/>
  <polyline class="k-muted" points="244,34 248,38 244,42"/>
  <line class="k-muted k-dash" x1="193" y1="64" x2="296" y2="64"/>
  <line class="k-muted" x1="193" y1="58" x2="193" y2="64"/>
  <line class="k-muted" x1="296" y1="58" x2="296" y2="64"/>
  <text class="k-label-accent" x="33" y="42" text-anchor="middle">構詞分析</text>
  <text class="k-label-accent" x="100" y="42" text-anchor="middle">詞典</text>
  <text class="k-label-accent" x="157" y="42" text-anchor="middle">例句</text>
  <text class="k-label" x="214" y="42" text-anchor="middle">語法</text>
  <text class="k-label" x="273" y="42" text-anchor="middle">思維鏈</text>
  <text class="k-label" x="244" y="78" text-anchor="middle">不納入</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：29.04｜直接提示：專家評分（滿語→英語，0 至 100）｜表 7, p. 8774
- 數字：64.47｜加入詞典與相似例句後的專家評分｜表 7, p. 8774
- 數字：56.12｜同設定改用加密滿語的專家評分｜表 7, p. 8774
- 數字：p = 0.27｜加密版與原版的評分差異不顯著｜§5.3, p. 8775
- 範圍：Pei 等 2025，GPT-4o 滿譯英，3 位專家評 33 句

## Card 5｜典範轉移
- 模式：新論文
- 標題：滿語之外，結論仍待驗證
- 里程碑：2025｜上下文翻譯可用來產生合成平行資料｜本篇 §7, p. 8775
- 里程碑：2025｜作者指出只以滿語一種語言為例｜本篇 Limitations, p. 8775
- 里程碑：2025｜滿語詞素界線清楚，結論能否外推未明｜本篇 Limitations, pp. 8775–8776
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：只把滿語切成詞素並不夠，配上詞典說明，構詞分析才派得上用場。
- 轉變：只切詞素→對上詞典
