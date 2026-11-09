# 卡片文字：2026-context-volume-rag-domain-shift-setiawan

- **論文頁**：[2026-context-volume-rag-domain-shift-setiawan](../papers/2026-context-volume-rag-domain-shift-setiawan.md)
- **證據表**：[2026-context-volume-rag-domain-shift-setiawan](../evidence/2026-context-volume-rag-domain-shift-setiawan.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：讓大模型參考例句，／修補跨領域的／達豪語翻譯
- 導語：小翻譯模型先出初稿，再讓大模型參考檢索來的例句修稿，把換領域後的翻譯拉回接近原水準。

## Card 2｜世紀瓶頸
- 標題：只有新約，卻要翻舊約
- 對照：小模型｜只用新約微調，遇到舊約就重複迴圈、虛構名稱
- 對照：語法書｜直接加進微調反而變差，生硬例句干擾譯文流暢
- 對照：大模型｜從未見過達豪語，直接翻譯品質很低
- 缺口：方法｜缺少不必重新訓練就能修補跨領域錯誤的做法
- 結語：需要一張能接住跨領域錯誤的安全網。

## Card 3｜突破原理
- 標題：小模型打底稿，大模型來修
- 公式：無
- 無公式理由：原文無公式：全文 15 頁無編號公式，等號僅見於參數設定（§5）
- 說明：小翻譯模型先出初稿，大模型對照檢索來的例句與詞典，只修重複、幻覺與錯詞。
- 圖類型：示意圖
- 圖說：示意：英文來源句先由小模型譯成初稿，大模型再參考檢索到的例句與詞典後編輯成譯文。

```svg
<svg viewBox="0 0 300 116" role="img" aria-label="示意：英文來源句先由小模型譯成初稿，大模型再參考檢索到的例句與詞典後編輯成譯文。">
  <rect class="k-ink k-ring" x="4" y="14" width="66" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="86" y="14" width="56" height="30" rx="4"/>
  <rect class="k-accent k-ring" x="158" y="14" width="66" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="240" y="14" width="56" height="30" rx="4"/>
  <rect class="k-ink k-ring k-dash" x="150" y="76" width="82" height="30" rx="4"/>
  <line class="k-ink" x1="70" y1="29" x2="84" y2="29"/>
  <polyline class="k-ink" points="79,24 84,29 79,34"/>
  <line class="k-ink" x1="142" y1="29" x2="156" y2="29"/>
  <polyline class="k-ink" points="151,24 156,29 151,34"/>
  <line class="k-ink" x1="224" y1="29" x2="238" y2="29"/>
  <polyline class="k-ink" points="233,24 238,29 233,34"/>
  <polyline class="k-muted k-dash" points="37,44 37,91 148,91"/>
  <line class="k-accent" x1="191" y1="76" x2="191" y2="47"/>
  <polyline class="k-accent" points="186,52 191,47 196,52"/>
  <text class="k-label" x="37" y="33" text-anchor="middle">英文來源句</text>
  <text class="k-label" x="114" y="33" text-anchor="middle">初稿</text>
  <text class="k-label-accent" x="191" y="33" text-anchor="middle">後編輯</text>
  <text class="k-label" x="268" y="33" text-anchor="middle">譯文</text>
  <text class="k-label" x="191" y="95" text-anchor="middle">例句與詞典</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：36.17｜新約（訓練同領域）測試之 chrF++｜表 1, p. 89
- 數字：27.11｜換到舊約，小模型單獨翻譯之 chrF++｜表 1, p. 89
- 數字：35.21｜加入檢索與後編輯之最終系統 chrF++｜表 2, p. 91
- 數字：≈137｜詞級檢索效果最好時的有效例句數｜表 5, p. 100
- 範圍：Setiawan 等 2026，英譯達豪語，新約訓練、舊約測試

## Card 5｜典範轉移
- 模式：新論文
- 標題：下一步：換語言，也換領域
- 里程碑：2026｜作者指出只測一個語言對與一種領域轉換｜本篇 §7, p. 95
- 里程碑：2026｜作者建議驗證新聞、衛生等非宗教文本｜本篇 §7, p. 95
- 里程碑：2026｜作者建議改用部分詞典以減少雜訊｜本篇 §7, p. 95
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：換了領域不必重訓大模型：小模型先打底稿，再讓大模型帶著例句修稿。
- 轉變：重新訓練→檢索修稿
