# 卡片文字：2025-paiwan-bunun-morphology-mt-wu

- **論文頁**：[2025-paiwan-bunun-morphology-mt-wu](../papers/2025-paiwan-bunun-morphology-mt-wu.md)
- **證據表**：[2025-paiwan-bunun-morphology-mt-wu](../evidence/2025-paiwan-bunun-morphology-mt-wu.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：拆解排灣語、／布農語的詞，／並與中文互譯
- 導語：把泛泰雅語的拆詞與翻譯，搬到排灣語、布農語。

## Card 2｜世紀瓶頸
- 標題：換一個族語，規則就不同
- 對照：排灣語重疊｜常重複詞根最後兩音節，並放在前面
- 對照：布農語｜ti 有時拼作 ci，喉塞音常被省略
- 對照：方言｜南排灣語法書、北排灣辭典拼法不同
- 缺口：比對｜遇到重疊與拼寫變化，詞根比對不到
- 結語：舊方法要搬家，得先補上各語的規則。

## Card 3｜突破原理
- 標題：拆詞補規則，翻譯疊技術
- 公式：無
- 無公式理由：原文僅有評估指標公式：§1.3 為 BLEU 平滑式，§4.1.2 Dice 係數只用於切分資料
- 說明：從已知詞根比對詞綴，排灣語另試重疊詞根末兩音節；翻譯另做，未用拆詞結果。
- 圖類型：示意圖
- 圖說：示意：上排為構詞解析，依詞根比對出詞綴；下排為翻譯，兩者是獨立實驗。

```svg
<svg viewBox="0 0 300 112" role="img" aria-label="示意：上排為構詞解析，依詞根比對出詞綴；下排為翻譯，兩者是獨立實驗。">
  <rect class="k-ink k-ring" x="4" y="8" width="84" height="30" rx="4"/>
  <rect class="k-accent k-ring" x="108" y="8" width="84" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="212" y="8" width="84" height="30" rx="4"/>
  <line class="k-ink" x1="88" y1="23" x2="106" y2="23"/>
  <polyline class="k-ink" points="101,18 106,23 101,28"/>
  <line class="k-ink" x1="192" y1="23" x2="210" y2="23"/>
  <polyline class="k-ink" points="205,18 210,23 205,28"/>
  <line class="k-muted k-dash" x1="4" y1="56" x2="296" y2="56"/>
  <rect class="k-ink k-ring" x="4" y="74" width="84" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="108" y="74" width="84" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="212" y="74" width="84" height="30" rx="4"/>
  <line class="k-ink" x1="88" y1="89" x2="106" y2="89"/>
  <polyline class="k-ink" points="101,84 106,89 101,94"/>
  <line class="k-ink" x1="192" y1="89" x2="210" y2="89"/>
  <polyline class="k-ink" points="205,84 210,89 205,94"/>
  <text class="k-label" x="46" y="27" text-anchor="middle">詞＋詞根</text>
  <text class="k-label-accent" x="150" y="27" text-anchor="middle">詞根比對</text>
  <text class="k-label" x="254" y="27" text-anchor="middle">詞綴</text>
  <text class="k-label" x="46" y="93" text-anchor="middle">族語句</text>
  <text class="k-label" x="150" y="93" text-anchor="middle">多語言翻譯</text>
  <text class="k-label" x="254" y="93" text-anchor="middle">中文</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：98.09%｜排灣語拆詞精確率｜表 8, p. 17
- 數字：99.79%｜布農語拆詞精確率｜表 9, p. 17
- 數字：25.02｜排灣語譯中文 BLEU｜表 23, p. 32
- 數字：17.81｜布農語譯中文 BLEU｜表 23, p. 32
- 範圍：吳維中 2025 碩論，翻譯分數取自交叉驗證

## Card 5｜典範轉移
- 模式：新論文
- 標題：留給下一步，把詞綴接上翻譯
- 里程碑：2025｜作者指出移植須先處理各語特殊構詞｜本篇 第六章, p. 33
- 里程碑：2025｜作者把導入詞綴資訊列為未來工作｜本篇 第六章, p. 33
- 里程碑：2025｜同實驗室同期論文在泛泰雅語導入詞綴｜金柏毅 2025, 碩士論文
- 註記：前兩項出自本篇；末項為同期平行研究

## Card 6｜Kairos
- 結語：拆詞骨架可以跨族語共用，各語只需補上自己的規則。
- 轉變：一語一套→共用骨架
