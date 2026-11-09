# 卡片文字：2026-data-centric-russian-kyrgyz-mt-novokshanov

- **論文頁**：[2026-data-centric-russian-kyrgyz-mt-novokshanov](../papers/2026-data-centric-russian-kyrgyz-mt-novokshanov.md)
- **證據表**：[2026-data-centric-russian-kyrgyz-mt-novokshanov](../evidence/2026-data-centric-russian-kyrgyz-mt-novokshanov.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：精挑語料、／分段訓練，／俄譯吉爾吉斯語奪冠
- 導語：先用語意評分把語料分級，再由粗到精分階段訓練，讓小模型在俄譯吉爾吉斯語競賽奪冠。
- 封面標題：俄羅斯語至吉爾吉斯語翻譯

## Card 2｜世紀瓶頸
- 標題：語料越灌越多，模型越學越亂
- 對照：回譯｜網路與回譯資料夾雜錯位、錯字與重複，未清洗會毒化模型
- 對照：無差別混洗｜雜訊合成句與少量好句子隨機混合，模型早期被噪聲帶偏
- 缺口：排程｜不清楚雜訊資料與乾淨資料該以什麼順序給模型學
- 結語：要的不是更多資料，而是分好等級的資料。

## Card 3｜突破原理
- 標題：先分好壞，再由粗到精分段教
- 公式：無
- 無公式理由：原文無公式：全文 6 頁無編號公式，方法以文字與表格敘述（§2）
- 說明：語料先依語意評分分級，再依序以粗資料、精資料、回譯、對話分四段訓練。
- 圖類型：示意圖
- 圖說：示意：語料先依語意評分分級，再依標準品質、高品質、回譯、對話的順序由粗到精訓練。

```svg
<svg viewBox="0 0 300 112" role="img" aria-label="示意：語料先依語意評分分級，再依標準品質、高品質、回譯、對話的順序由粗到精訓練。">
  <rect class="k-accent k-ring" x="4" y="8" width="140" height="26" rx="4"/>
  <line class="k-ink" x1="36" y1="34" x2="36" y2="52"/>
  <polyline class="k-ink" points="32,47 36,52 40,47"/>
  <line class="k-ink" x1="112" y1="34" x2="112" y2="52"/>
  <polyline class="k-ink" points="108,47 112,52 116,47"/>
  <rect class="k-ink k-ring" x="4" y="54" width="64" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="80" y="54" width="64" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="156" y="54" width="64" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="232" y="54" width="64" height="30" rx="4"/>
  <line class="k-ink" x1="146" y1="69" x2="154" y2="69"/>
  <polyline class="k-ink" points="150,65 154,69 150,73"/>
  <line class="k-ink" x1="222" y1="69" x2="230" y2="69"/>
  <polyline class="k-ink" points="226,65 230,69 226,73"/>
  <line class="k-line k-dash" x1="10" y1="94" x2="286" y2="94"/>
  <polyline class="k-line" points="280,90 286,94 280,98"/>
  <text class="k-label-accent" x="74" y="25" text-anchor="middle">語意評分</text>
  <text class="k-label" x="36" y="73" text-anchor="middle">標準品質</text>
  <text class="k-label" x="112" y="73" text-anchor="middle">高品質</text>
  <text class="k-label" x="188" y="73" text-anchor="middle">回譯</text>
  <text class="k-label" x="264" y="73" text-anchor="middle">對話</text>
  <text class="k-label" x="150" y="108" text-anchor="middle">由粗到精</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：49.1｜官方測試集俄→吉 chrF++，賽道第一｜§3.2, p. 228
- 數字：44.9｜公開測試集 chrF++，勝過 54B 與 235B 模型｜表 3, p. 228
- 數字：800M｜詞表剪枝後的模型參數量｜§2.3.2, pp. 226–227
- 數字：23.2｜小模型加烏、塔語資料後 chrF++（原 21.5）｜表 2, p. 227
- 範圍：Novokshanov 2026，單一語言對之共享任務系統報告

## Card 5｜典範轉移
- 模式：新論文
- 標題：留給吉爾吉斯語的資源
- 里程碑：2026｜公開最終模型權重｜本篇 §3.3, p. 228
- 里程碑：2026｜公開過濾後的合成平行語料｜本篇 §3.3, p. 228
- 里程碑：2026｜提供免安裝的線上翻譯展示｜本篇 §3.3, p. 228
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：語料稀少時，順序也是一種資源：先用大量粗資料打底，再以精資料收尾。
- 轉變：擴大模型→整理資料
