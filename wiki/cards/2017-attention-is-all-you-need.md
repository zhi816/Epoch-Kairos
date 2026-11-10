# 卡片文字：2017-attention-is-all-you-need

- **論文頁**：[2017-attention-is-all-you-need](../papers/2017-attention-is-all-you-need.md)
- **證據表**：[2017-attention-is-all-you-need](../evidence/2017-attention-is-all-you-need.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：不再逐字讀句子，／讓每個字／同時看見整句
- 導語：只用注意力計算字與字的關係，不必逐字等待，訓練因此能大量並行。

## Card 2｜世紀瓶頸
- 標題：逐字計算，快不起也記不遠
- 對照：循環層｜每一步都要等上一步算完，並行硬體派不上用場
- 對照：卷積網路｜相距遠的兩個字，要經過好幾層才能交換資訊
- 缺口：架構｜沒有既能整句並行計算、又讓任兩字直接相連的結構
- 結語：需要一種不必排隊、一步就能看全句的計算。

## Card 3｜突破原理
- 標題：用內積算出誰該關注誰
- 公式：q \cdot k = \sum_{i=1}^{d_k} q_i k_i
- 說明：查詢與鍵的內積衡量相符程度；縮放後用來計算各位置的注意力權重。
- 圖類型：示意圖
- 圖說：示意：循環層逐字傳遞（左）；自注意力直接相連，一個字連到句中其他每個字（右）。

```svg
<svg viewBox="0 0 300 110" role="img" aria-label="示意：循環層逐字傳遞（左）；自注意力直接相連，一個字連到句中其他每個字（右）。">
  <line class="k-muted k-thin" x1="150" y1="8" x2="150" y2="102"/>
  <circle class="k-muted" cx="18" cy="66" r="4"/>
  <circle class="k-muted" cx="46" cy="66" r="4"/>
  <circle class="k-muted" cx="74" cy="66" r="4"/>
  <circle class="k-muted" cx="102" cy="66" r="4"/>
  <circle class="k-muted" cx="130" cy="66" r="4"/>
  <line class="k-muted" x1="24" y1="66" x2="40" y2="66"/>
  <polyline class="k-muted" points="36,62 40,66 36,70"/>
  <line class="k-muted" x1="52" y1="66" x2="68" y2="66"/>
  <polyline class="k-muted" points="64,62 68,66 64,70"/>
  <line class="k-muted" x1="80" y1="66" x2="96" y2="66"/>
  <polyline class="k-muted" points="92,62 96,66 92,70"/>
  <line class="k-muted" x1="108" y1="66" x2="124" y2="66"/>
  <polyline class="k-muted" points="120,62 124,66 120,70"/>
  <path class="k-line" d="M224 81 Q 197 36 170 82"/>
  <path class="k-line" d="M224 81 Q 210 58 197 82"/>
  <path class="k-line" d="M224 81 Q 238 58 251 82"/>
  <path class="k-line" d="M224 81 Q 251 36 278 82"/>
  <circle class="k-ink" cx="170" cy="86" r="4"/>
  <circle class="k-ink" cx="197" cy="86" r="4"/>
  <circle class="k-accent" cx="224" cy="86" r="5"/>
  <circle class="k-ink" cx="251" cy="86" r="4"/>
  <circle class="k-ink" cx="278" cy="86" r="4"/>
  <text class="k-label" x="74" y="50" text-anchor="middle">循環層逐字傳遞</text>
  <text class="k-label-accent" x="224" y="104" text-anchor="middle">自注意力直接相連</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：28.4｜WMT 2014 英譯德 BLEU（大型版本）｜Table 2
- 數字：41.0｜WMT 2014 英譯法 BLEU，NeurIPS 定稿｜Table 2
- 數字：3.5 天｜大型版本以 8 張 P100 GPU 訓練的時間｜§5.2
- 數字：91.3｜WSJ 英語句法剖析 F1，只用 WSJ 訓練｜Table 4
- 範圍：Vaswani 等 2017，2014 翻譯評測、華爾街日報句法剖析，8 張 P100

## Card 5｜典範轉移
- 標題：從翻譯模型，到各種模態的通用骨幹
- 里程碑：2019｜Devlin 等取編碼器提出 BERT｜Devlin et al. 2019, NAACL
- 里程碑：2020｜Brown 等取解碼器擴展到 1,750 億參數｜Brown et al. 2020, NeurIPS 33:1877-1901
- 里程碑：2020｜Kaplan 等觀察到損失隨規模呈冪律下降｜Kaplan et al. 2020, arXiv:2001.08361
- 里程碑：2021｜Jumper 等以注意力預測蛋白質結構｜Jumper et al. 2021, Nature
- 里程碑：2023｜Peebles 與 Xie 結合注意力與擴散模型｜Peebles & Xie 2023, ICCV
- 註記：以上皆為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：拿掉逐字遞推的結構，只留位置編碼等少數先驗，字與字的關聯交給資料學。
- 轉變：強結構偏置→資料驅動
