# 卡片文字：2025-formosanbench-llm-benchmark-lin

- **論文頁**：[2025-formosanbench-llm-benchmark-lin](../papers/2025-formosanbench-llm-benchmark-lin.md)
- **證據表**：[2025-formosanbench-llm-benchmark-lin](../evidence/2025-formosanbench-llm-benchmark-lin.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：出一套族語考題，／測大型語言模型／懂多少
- 導語：用阿美語、泰雅語、排灣語的翻譯、語音辨識與摘要，檢驗大型語言模型，結果三項都不理想。

## Card 2｜世紀瓶頸
- 標題：大型語言模型，懂臺灣南島語嗎？
- 對照：語態系統｜動詞居首，同一句可依主事或受事語態有多種說法
- 對照：先前研究｜集中在機器翻譯與傳統序列模型
- 缺口：評測｜沒有研究系統性評估大型語言模型在多項任務的能力
- 結語：需要一套跨任務、跨語言的共同考題。

## Card 3｜突破原理
- 標題：三語三任務，分頭取材出題
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，BLEU、WER、ROUGE 僅引用未列式（§5.3）
- 說明：翻譯取自線上辭典、語音取自 E 樂園錄音、摘要取自族語維基，三者來源各自獨立。
- 圖類型：示意圖
- 圖說：示意：線上辭典、E 樂園錄音、族語維基三個獨立來源，分別出成翻譯、語音辨識與摘要三項考題。

```svg
<svg viewBox="0 0 300 120" role="img" aria-label="示意：線上辭典、E 樂園錄音、族語維基三個獨立來源，分別出成翻譯、語音辨識與摘要三項考題。">
  <rect class="k-ink k-ring" x="10" y="8" width="100" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="10" y="47" width="100" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="10" y="86" width="100" height="26" rx="4"/>
  <rect class="k-accent k-ring" x="186" y="8" width="100" height="26" rx="4"/>
  <rect class="k-accent k-ring" x="186" y="47" width="100" height="26" rx="4"/>
  <rect class="k-accent k-ring" x="186" y="86" width="100" height="26" rx="4"/>
  <line class="k-line" x1="114" y1="21" x2="182" y2="21"/>
  <polyline class="k-line" points="176,16 182,21 176,26"/>
  <line class="k-line" x1="114" y1="60" x2="182" y2="60"/>
  <polyline class="k-line" points="176,55 182,60 176,65"/>
  <line class="k-line" x1="114" y1="99" x2="182" y2="99"/>
  <polyline class="k-line" points="176,94 182,99 176,104"/>
  <text class="k-label" x="60" y="25" text-anchor="middle">線上辭典</text>
  <text class="k-label" x="60" y="64" text-anchor="middle">E 樂園錄音</text>
  <text class="k-label" x="60" y="103" text-anchor="middle">族語維基</text>
  <text class="k-label-accent" x="236" y="25" text-anchor="middle">翻譯</text>
  <text class="k-label-accent" x="236" y="64" text-anchor="middle">語音辨識</text>
  <text class="k-label-accent" x="236" y="103" text-anchor="middle">摘要</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：<40%｜排灣語譯文中，母語者估計有意義者的比例｜§6.1, p. 16533
- 數字：<10%｜泰雅語譯文中，整句全對的比例｜§6.1, p. 16533
- 範圍：Lin 等 2025，翻譯輸出經母語者人工檢視之估計

## Card 5｜典範轉移
- 模式：新論文
- 標題：一份公開的族語考卷
- 里程碑：2025｜作者公開三語三任務的資料集與程式碼｜本篇 p. 16527
- 里程碑：2025｜作者指出訓練資料量是主要瓶頸｜本篇 §6.1
- 里程碑：2025｜作者指出擴充語言與任務需大量人工標注｜本篇 Limitations, p. 16535
- 註記：此卡各項皆出自本篇

## Card 6｜Kairos
- 結語：這份翻譯考題取自辭典例句，若訓練也用辭典，須先查兩者是否重疊。
- 轉變：只測翻譯→多項任務
