# 卡片文字：2024-finnish-northern-sami-mt-saleva

- **論文頁**：[2024-finnish-northern-sami-mt-saleva](../papers/2024-finnish-northern-sami-mt-saleva.md)
- **證據表**：[2024-finnish-northern-sami-mt-saleva](../evidence/2024-finnish-northern-sami-mt-saleva.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：比較補資料方法，／改善北薩米語翻譯
- 導語：以芬蘭語譯北薩米語為例，比較幾種補資料做法，發現效果隨測試領域而不同。
- 封面標題：語言模型先驗與資料增強

## Card 2｜世紀瓶頸
- 標題：語料極少，合成資料又怕喧賓奪主
- 對照：平行語料｜只有 25,106 句；只用它訓練，域外新聞僅 8.43 BLEU
- 對照：合成資料｜可擴充到約 190 萬句，卻可能排擠真實平行資料
- 對照：多語模型｜初步微調實驗仍低於 10 BLEU，品質無法使用
- 缺口：基線｜前人的純平行語料基線訓練不足，比較的起點本身就偏低
- 結語：先把基線練足，再看哪種補法真的有用。

## Card 3｜突破原理
- 標題：讓單語資料也能幫上翻譯
- 公式：+ \lambda\, D_{\text{KL}}\big(p_{\text{LM}}(y) \mid p_{\text{NMT}}(y \mid x)\big)
- 說明：在翻譯損失外再加這一項，把譯文的用字分布拉向凍結的北薩米語語言模型。
- 圖類型：示意圖
- 圖說：示意：北薩米語單語資料一路回譯成句對，與平行語料一起訓練翻譯模型；另一路訓練語言模型當先驗。

```svg
<svg viewBox="0 0 300 118" role="img" aria-label="示意：北薩米語單語資料一路回譯成句對，與平行語料一起訓練翻譯模型；另一路訓練語言模型當先驗。">
  <rect class="k-ink k-ring" x="4" y="61" width="80" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="118" y="4" width="70" height="26" rx="4"/>
  <rect class="k-accent k-ring" x="118" y="42" width="70" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="118" y="82" width="70" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="226" y="22" width="70" height="44" rx="4"/>
  <line class="k-ink" x1="84" y1="75" x2="100" y2="75"/>
  <line class="k-ink" x1="100" y1="55" x2="100" y2="95"/>
  <line class="k-ink" x1="100" y1="55" x2="116" y2="55"/>
  <polyline class="k-ink" points="110,50 116,55 110,60"/>
  <line class="k-ink" x1="100" y1="95" x2="116" y2="95"/>
  <polyline class="k-ink" points="110,90 116,95 110,100"/>
  <line class="k-ink" x1="188" y1="17" x2="206" y2="17"/>
  <line class="k-ink" x1="188" y1="55" x2="206" y2="55"/>
  <line class="k-ink" x1="206" y1="17" x2="206" y2="55"/>
  <line class="k-ink" x1="206" y1="36" x2="224" y2="36"/>
  <polyline class="k-ink" points="218,31 224,36 218,41"/>
  <line class="k-accent k-dash" x1="188" y1="95" x2="261" y2="95"/>
  <line class="k-accent k-dash" x1="261" y1="95" x2="261" y2="68"/>
  <polyline class="k-accent" points="256,74 261,68 266,74"/>
  <text class="k-label" x="44" y="79" text-anchor="middle">北薩米語單語</text>
  <text class="k-label" x="153" y="21" text-anchor="middle">平行語料</text>
  <text class="k-label-accent" x="153" y="59" text-anchor="middle">回譯句對</text>
  <text class="k-label" x="153" y="99" text-anchor="middle">語言模型</text>
  <text class="k-label" x="261" y="48" text-anchor="middle">翻譯模型</text>
  <text class="k-label-accent" x="226" y="108" text-anchor="middle">先驗</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：26.86｜充分訓練之基線，UiT BLEU（前人報 18.9）｜表 3, p. 12952
- 數字：41.75｜兩組回譯合訓之最佳模型，UiT BLEU｜表 3, p. 12952
- 數字：19.20｜最佳模型加標記，域外 YLE BLEU｜表 5, p. 12953
- 數字：1.92｜大型多語模型 MADLAD-400，UiT BLEU｜表 1, p. 12950
- 範圍：Sälevä 與 Lignos 2024，芬蘭語→北薩米語，單次執行

## Card 5｜典範轉移
- 模式：新論文
- 標題：公開程式，留下推廣的問題
- 里程碑：2024｜公開程式碼與正譯、回譯資料｜本篇 §1, p. 12949
- 里程碑：2024｜只研究單一語言對、每實驗只跑一次｜本篇 Limitations, p. 12953
- 里程碑：2024｜作者指出能否推廣到其他語言仍待回答｜本篇 §5, p. 12953
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：同一個標記，域內幾乎沒差、域外卻明顯加分；評估時兩種測試集都要看。
- 轉變：只看域內→域內域外並看
