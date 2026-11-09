# 卡片文字：2021-seediq-chinese-mt-you

- **論文頁**：[2021-seediq-chinese-mt-you](../papers/2021-seediq-chinese-mt-you.md)
- **證據表**：[2021-seediq-chinese-mt-you](../evidence/2021-seediq-chinese-mt-you.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09

## 封面
- 封面斷行：讓電腦在賽德克語／與中文之間翻譯
- 導語：以字典例句為資料，先自動拆出賽德克語詞的前、中、後綴，再把詞綴資訊加進神經翻譯模型，譯成中文。

## Card 2｜世紀瓶頸
- 標題：語料稀少，詞形又千變萬化
- 對照：語料｜相關研究相當稀少，可用的只有語法書草稿與辭典例句
- 對照：字典｜只收詞字串與參考原形，沒有標出前、中、後綴
- 缺口：工具｜沒有能自動拆出賽德克語詞綴的工具，遇到新詞就無從處理
- 結語：要先把千變萬化的詞形，拆回詞根與詞綴。

## Card 3｜突破原理
- 標題：先拆詞綴，再交給神經翻譯
- 公式：P_{\text{uni}}(\text{pfx}) = \prod_{i=1}^{m} P(x_i)
- 說明：前綴有多種斷法時，用各單元機率的乘積來評估哪種斷法較可能。
- 圖類型：示意圖
- 圖說：示意：賽德克詞先拆出前綴、中綴、後綴，詞綴資訊與詞一起送進翻譯模型，譯成中文。

```svg
<svg viewBox="0 0 300 110" role="img" aria-label="示意：賽德克詞先拆出前綴、中綴、後綴，詞綴資訊與詞一起送進翻譯模型，譯成中文。">
  <rect class="k-ink k-ring" x="6" y="30" width="58" height="30" rx="4"/>
  <rect class="k-accent k-ring" x="82" y="30" width="58" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="158" y="30" width="58" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="236" y="30" width="58" height="30" rx="4"/>
  <line class="k-ink" x1="66" y1="45" x2="80" y2="45"/>
  <polyline class="k-ink" points="75,40 80,45 75,50"/>
  <line class="k-ink" x1="142" y1="45" x2="156" y2="45"/>
  <polyline class="k-ink" points="151,40 156,45 151,50"/>
  <line class="k-ink" x1="218" y1="45" x2="234" y2="45"/>
  <polyline class="k-ink" points="229,40 234,45 229,50"/>
  <line class="k-accent k-dash" x1="111" y1="62" x2="111" y2="78"/>
  <text class="k-label" x="35" y="49" text-anchor="middle">賽德克詞</text>
  <text class="k-label-accent" x="111" y="49" text-anchor="middle">拆詞綴</text>
  <text class="k-label" x="187" y="49" text-anchor="middle">翻譯模型</text>
  <text class="k-label" x="265" y="49" text-anchor="middle">中文</text>
  <text class="k-label-accent" x="111" y="94" text-anchor="middle">前綴、中綴、後綴</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：25.10｜賽德克語→中文 BLEU，自訓練詞嵌入加詞綴特徵｜表 11，p. 38
- 數字：21.03｜同樣設定，但不加詞綴特徵｜表 11，p. 38
- 數字：12.09｜改用預訓練詞嵌入，加詞綴特徵反而下降｜表 11，p. 38
- 數字：93.38%｜構詞結構完整解析之精準度（測試資料）｜§5.2，p. 36
- 範圍：游景勝 2021，約六千句字典例句訓練之小規模實驗

## Card 5｜典範轉移
- 標題：同實驗室的後續論文接棒
- 里程碑：2023｜戴晟哲的泰雅語、太魯閣語構詞解析引用本文｜戴晟哲 2023, 國立臺灣海洋大學碩士論文
- 里程碑：2025｜楊鈞凱依戴晟哲與本文的技術分析未知詞｜楊鈞凱 2025, 國立臺灣海洋大學碩士論文
- 里程碑：2025｜金柏毅沿用本文的書寫轉換規則與詞綴特徵｜金柏毅 2025, 國立臺灣海洋大學碩士論文
- 註記：以上皆為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：同樣的詞綴資訊，換一種表徵方式，結果可以從加分變成大幅扣分。
- 轉變：整詞處理→拆解詞綴
