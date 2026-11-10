# 卡片文字：2026-hybrid-dictionary-rag-llm-paiwan-wang

- **論文頁**：[2026-hybrid-dictionary-rag-llm-paiwan-wang](../papers/2026-hybrid-dictionary-rag-llm-paiwan-wang.md)
- **證據表**：[2026-hybrid-dictionary-rag-llm-paiwan-wang](../evidence/2026-hybrid-dictionary-rag-llm-paiwan-wang.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：先查辭典／再交給大模型，／把排灣語譯成華語
- 導語：辭典沒收的詞，再從平行例句庫檢索補上。
- 封面標題：混合辭典與大語言模型之低資源機器翻譯

## Card 2｜世紀瓶頸
- 標題：只查辭典，句子卻不通順？
- 對照：詞典查找｜現有排灣語工具多只能查詞，逐字輸出語意不通
- 對照：向量檢索｜書面語料極少，可檢索的例句稀疏
- 對照：大模型｜缺少排灣語資料，未經增強時幾乎譯不出原意
- 缺口：工具｜沒有能把整句譯順、又保住排灣語詞義的工具
- 結語：要讓詞義準、句子順，兩者得兼顧。

## Card 3｜突破原理
- 標題：先查辭典，查不到再找例句
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，流程以文字與圖 1 至 3 說明（§3.2）
- 說明：辭典給出確定詞義，缺字時從例句庫檢索補充，再由大型語言模型重排成通順華語。
- 圖類型：示意圖
- 圖說：示意：排灣語句先查辭典，查到的詞直接給詞義，查不到的改從向量資料庫找例句，再交給大型語言模型重組成華語。

```svg
<svg viewBox="0 0 300 110" role="img" aria-label="示意：排灣語句先查辭典，查到的詞直接給詞義，查不到的改從向量資料庫找例句，再交給大型語言模型重組成華語。">
  <polygon class="k-ink k-ring" points="52,30 92,55 52,80 12,55"/>
  <rect class="k-ink k-ring" x="100" y="82" width="56" height="24" rx="4"/>
  <rect class="k-accent k-ring" x="176" y="42" width="64" height="26" rx="4"/>
  <polyline class="k-ink" points="52,30 52,16 208,16 208,40"/>
  <polyline class="k-ink" points="203,35 208,40 213,35"/>
  <polyline class="k-ink" points="52,80 52,94 98,94"/>
  <polyline class="k-ink" points="93,89 98,94 93,99"/>
  <polyline class="k-ink" points="156,94 208,94 208,70"/>
  <polyline class="k-ink" points="203,75 208,70 213,75"/>
  <line class="k-line" x1="240" y1="55" x2="262" y2="55"/>
  <polyline class="k-line" points="257,50 262,55 257,60"/>
  <text class="k-label" x="52" y="59" text-anchor="middle">查辭典</text>
  <text class="k-label" x="130" y="32" text-anchor="middle">查到</text>
  <text class="k-label" x="44" y="96" text-anchor="end">查不到</text>
  <text class="k-label" x="128" y="98" text-anchor="middle">找例句</text>
  <text class="k-label-accent" x="208" y="59" text-anchor="middle">語言模型</text>
  <text class="k-label" x="281" y="59" text-anchor="middle">華語</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：4.4｜排灣語→華語 BLEU，未加模組時之最高者｜§4, p. 6
- 數字：40.8｜同一測試，加上本系統後之最低者｜§4, p. 6
- 數字：0.236｜語意餘弦相似度，未加模組時之最高者｜§4, p. 6
- 數字：0.810｜同一指標，加上本系統後之最低者｜§4, p. 6
- 範圍：Wang 等 2026，教材 250 句，四個大模型；只用自動指標

## Card 5｜典範轉移
- 模式：新論文
- 標題：辭典覆蓋，決定譯得好不好
- 里程碑：2026｜作者指出辭典缺詞時譯文語意偏離｜本篇 §5, p. 7
- 里程碑：2026｜作者指出倒裝句與文化語句表現較弱｜本篇 §5, p. 7
- 里程碑：2026｜作者計畫擴充辭典並納入母語者評估｜本篇 §5, p. 7
- 里程碑：2026｜資料不公開，需向通訊作者申請｜本篇 Data Availability, p. 8
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：辭典只比對表面詞形，詞根加上詞綴就可能查不到，覆蓋率成了關鍵。
- 轉變：只靠大模型→先查辭典
