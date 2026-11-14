# 卡片文字：2026-cross-lingual-alignment-moe-routers-bandarkar

- **論文頁**：[2026-cross-lingual-alignment-moe-routers-bandarkar](../papers/2026-cross-lingual-alignment-moe-routers-bandarkar.md)
- **證據表**：[2026-cross-lingual-alignment-moe-routers-bandarkar](../evidence/2026-cross-lingual-alignment-moe-routers-bandarkar.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14
- **最後核對**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14

## 封面

- 封面斷行：訓練多語模型時，／讓翻譯句對／分派相似專家
- 導語：對齊混合專家模型的分派比例分佈，不用逐字對應翻譯句，就能拉近語言間的表徵並促進遷移。
- 封面標題：混合專家路由器跨語言對齊

## Card 2｜世紀瓶頸

- 標題：缺句子向量，解碼器怎做跨語對齊？
- 對照：編碼器｜有整句向量可做對比學習，但主流架構已轉向純解碼器
- 對照：隱狀態｜直接做序列平均與餘弦對齊時，詞元特徵方向易互相抵銷
- 對照：全層對齊｜盲目強制全部層數表徵一致，容易損傷語言專屬結構
- 缺口：對齊目標｜純解碼器缺少能代表整句語意、又不必逐詞對應的穩定對齊介面
- 結語：需要繞過逐詞對應的輕量序列統計介面。

## Card 3｜突破原理

- 標題：讓平行句在中間層選相似專家
- 公式：\mathcal{L} = \mathcal{L}_{LM} + \alpha \cdot \mathcal{L}_{XLR}
- 說明：目標語預測損失加上中間層路由散度對齊項，僅對目標語端更新，讓選路分佈向英語靠攏。
- 圖類型：示意圖
- 圖說：示意：英與目標語經詞元路由取平均路由分佈，在中間層散度對齊後僅對目標語端更新。

```svg
<svg viewBox="0 0 300 136" role="img" aria-label="示意：英與目標語經詞元路由取平均路由分佈，在中間層散度對齊後僅對目標語端更新。">
  <rect class="k-muted k-ring" x="10" y="12" width="70" height="26" rx="4"/>
  <text class="k-label" x="45" y="29" text-anchor="middle">英語序列</text>
  <line class="k-muted" x1="80" y1="25" x2="102" y2="25"/>
  <polyline class="k-muted" points="97,21 102,25 97,29"/>
  <rect class="k-muted k-ring" x="102" y="12" width="86" height="26" rx="4"/>
  <text class="k-label" x="145" y="29" text-anchor="middle">平均路由分佈</text>
  <polyline class="k-muted" points="188,25 251,25 251,40"/>
  <polyline class="k-muted" points="247,35 251,40 255,35"/>
  <rect class="k-soft" x="214" y="40" width="76" height="32" rx="4"/>
  <rect class="k-line k-ring" x="214" y="40" width="76" height="32" rx="4"/>
  <text class="k-label-accent" x="252" y="60" text-anchor="middle">中間層散度</text>
  <rect class="k-ink k-ring" x="10" y="72" width="70" height="26" rx="4"/>
  <text class="k-label" x="45" y="89" text-anchor="middle">目標語序列</text>
  <line class="k-ink" x1="80" y1="85" x2="102" y2="85"/>
  <polyline class="k-ink" points="97,81 102,85 97,89"/>
  <rect class="k-accent k-ring" x="102" y="72" width="86" height="26" rx="4"/>
  <text class="k-label-accent" x="145" y="89" text-anchor="middle">平均路由分佈</text>
  <polyline class="k-ink" points="188,85 236,85 236,72"/>
  <polyline class="k-ink" points="232,77 236,72 240,77"/>
  <polyline class="k-accent k-dash" points="256,72 256,112 45,112 45,98"/>
  <polyline class="k-accent" points="41,103 45,98 49,103"/>
  <text class="k-label-accent" x="150" y="128" text-anchor="middle">僅對目標語端更新</text>
</svg>
```

## Card 4｜決定性數據

- 模式：數字
- 數字：13/14｜實驗組合多任務平均勝過純語言模型基線（1 平手）｜§5.2 p. 7、Table 1
- 數字：+0.9｜14 組跨多任務平均分較純語言模型基線提升｜§5.2 p. 7
- 數字：+2.1｜Qwen3-30B-A3B 吉爾吉斯語均分較基線高｜§5.2 p. 7、Table 1
- 數字：38.1｜Marco-Nano 匈牙利語均分（隱狀態降為 36.9）｜§5.2 p. 7、Table 2
- 範圍：Bandarkar 等 2026，4 款已後訓練模型、7 語各 20 萬平行句

## Card 5｜典範轉移

- 模式：新論文
- 標題：留給預訓練規模的路由器對齊測試題
- 里程碑：2026｜於 GitHub 公開路由對齊訓練與評估程式碼｜本篇 Code Availability, p. 10
- 里程碑：2026｜設計無填補打包與早期退出以壓低額外運算量｜本篇 §3.3, p. 4
- 里程碑：2026｜作者明列僅測已後訓練模型與 20 萬句級語料｜本篇 §6, pp. 8–9
- 里程碑：2026｜作者擬於預訓練驗證並降低對平行句依賴｜本篇 §6–§7, pp. 8–9
- 註記：以上皆出自本篇預印本，尚無後續他人研究。

## Card 6｜Kairos

- 結語：把跨語言對齊從高維向量轉到專家選擇分佈，為低資源翻譯避開逐字對應難題。
- 轉變：對齊詞元向量→對齊專家分派
