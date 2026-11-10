# 卡片文字：2023-atayal-truku-morphology-dai

- **論文頁**：[2023-atayal-truku-morphology-dai](../papers/2023-atayal-truku-morphology-dai.md)
- **證據表**：[2023-atayal-truku-morphology-dai](../evidence/2023-atayal-truku-morphology-dai.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：讓電腦拆解／泰雅語與太魯閣語的／詞根與詞綴
- 導語：沿用賽德克語的解析流程，為兩語另訂專屬規則。
- 封面標題：泰雅語與太魯閣語構詞結構自動解析

## Card 2｜世紀瓶頸
- 標題：書上的詞根，不是真正的詞根
- 對照：泰雅語教材｜標的是深層原形，還常省略弱元音，不是辭典詞根
- 對照：辭典參照｜「參照」欄不一定是詞根，須一路追到源頭
- 缺口：書寫規則｜兩語書寫時保留的元音數不一，歸納不出轉換規則
- 結語：賽德克語的流程，無法原封不動照搬。

## Card 3｜突破原理
- 標題：改用比對，再以機率挑前綴
- 公式：P(\mathit{pfx}) = \prod_{i=1}^{m+1} P(x_i \mid x_{i-1})
- 說明：書寫規則歸納不出，就改用三條規則比對；前綴斷法以機率挑選，二元模型頭尾另加邊界。
- 圖類型：示意圖
- 圖說：示意：由詞根列出深層原形候選，拼上中、後綴後與目標詞比對，剩下的前綴字串以機率挑出斷法，二元模型另加上邊界。

```svg
<svg viewBox="0 0 300 104" role="img" aria-label="示意：由詞根列出深層原形候選，拼上中、後綴後與目標詞比對，剩下的前綴字串以機率挑出斷法，二元模型另加上邊界。">
  <rect class="k-ink k-ring" x="4" y="22" width="52" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="64" y="22" width="52" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="124" y="22" width="52" height="30" rx="4"/>
  <rect class="k-accent k-ring" x="184" y="22" width="52" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="244" y="22" width="52" height="30" rx="4"/>
  <line class="k-ink" x1="56" y1="37" x2="62" y2="37"/>
  <polyline class="k-ink" points="58,33 62,37 58,41"/>
  <line class="k-ink" x1="116" y1="37" x2="122" y2="37"/>
  <polyline class="k-ink" points="118,33 122,37 118,41"/>
  <line class="k-ink" x1="176" y1="37" x2="182" y2="37"/>
  <polyline class="k-ink" points="178,33 182,37 178,41"/>
  <line class="k-ink" x1="236" y1="37" x2="242" y2="37"/>
  <polyline class="k-ink" points="238,33 242,37 238,41"/>
  <line class="k-accent k-dash" x1="210" y1="54" x2="210" y2="72"/>
  <text class="k-label" x="30" y="41" text-anchor="middle">原形</text>
  <text class="k-label" x="90" y="41" text-anchor="middle">拼接</text>
  <text class="k-label" x="150" y="41" text-anchor="middle">比對</text>
  <text class="k-label-accent" x="210" y="41" text-anchor="middle">前綴</text>
  <text class="k-label" x="270" y="41" text-anchor="middle">結構</text>
  <text class="k-label-accent" x="210" y="88" text-anchor="middle">加上邊界</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：96.72%｜泰雅語中後綴解析精確率｜表 14, p. 32
- 數字：96.43%｜泰雅語前綴，考慮邊界的二元模型測試正確率｜表 19, p. 35
- 數字：91.84%｜太魯閣語前綴，一元模型測試正確率｜表 21, p. 37
- 數字：85.71%｜太魯閣語前綴，考慮邊界二元模型正確率低於一元｜表 22, p. 37
- 範圍：戴晟哲 2023，前綴只評長度 2 以上的字串

## Card 5｜典範轉移
- 標題：解析器與規則，被後續論文沿用
- 里程碑：2025｜金柏毅用本篇解析器標出詞綴，再做翻譯｜金柏毅 2025, 國立臺灣海洋大學碩士論文
- 里程碑：2025｜吳維中沿用此架構，解析排灣語、布農語｜吳維中 2025, 國立臺灣海洋大學碩士論文
- 里程碑：2025｜楊鈞凱借本篇規則，列舉未知詞的原形｜楊鈞凱 2025, 國立臺灣海洋大學碩士論文
- 註記：三筆皆為同實驗室之後續碩士論文，頁碼見長文

## Card 6｜Kairos
- 結語：只有 56 個測試詞時，錯一個就差約 1.8 個百分點，數字要連詞數一起看。
- 轉變：只報正確率→同報詞數
