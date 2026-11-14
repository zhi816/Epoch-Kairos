# 卡片文字：2026-tokenizations-austronesian-lms-lumbantobing

- **論文頁**：[2026-tokenizations-austronesian-lms-lumbantobing](../papers/2026-tokenizations-austronesian-lms-lumbantobing.md)
- **證據表**：[2026-tokenizations-austronesian-lms-lumbantobing](../evidence/2026-tokenizations-austronesian-lms-lumbantobing.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14
- **最後核對**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14

## 封面

- 封面斷行：借傳統書寫邏輯，／依音節單位切分／南島語詞元
- 導語：效法印尼傳統音節文字的消元音規則，讓語言模型不再把南島語詞根切成碎塊。
- 封面標題：南島語系音節分詞法

## Card 2｜世紀瓶頸

- 標題：統計分詞為何切碎南島語詞根
- 對照：統計子詞法｜如英文導向壓縮方法，把少見南島語拆成碎字元
- 對照：純音素切分｜雖不缺符號卻丟失音節韻律，難呈雙音節詞根骨架
- 對照：整詞詞表｜南島語詞綴變化極繁，整詞收錄易爆發未登錄詞問題
- 缺口：音節邊界｜缺能保留南島語音節邊界、又不必逐語手寫規則之切分層
- 結語：需要兼顧跨語同源音節與零爆炸詞表的切分法。

## Card 3｜突破原理

- 標題：音節切分搭配字元退回映射
- 公式：\tau_\Sigma = (f_\Sigma \circ P)
- 說明：先以切分算子 $P$ 依三階段拆出音節，遇詞表 $\Sigma$ 外音節再經 $f_\Sigma$ 退回字元。
- 圖類型：示意圖
- 圖說：示意：輸入字母序列依序經過線性掃描、消元音回溯與複輔音前向三階段後，查音節詞表並把生詞退回字元。

```svg
<svg viewBox="0 0 300 132" role="img" aria-label="示意：輸入字母序列依序經過線性掃描、消元音回溯與複輔音前向三階段後，查音節詞表並把生詞退回字元。">
  <rect class="k-muted k-ring" x="6" y="14" width="60" height="26" rx="4"/>
  <text class="k-label" x="36" y="31" text-anchor="middle">字母序列</text>
  <line class="k-ink" x1="66" y1="27" x2="80" y2="27"/>
  <polyline class="k-ink" points="76,23 80,27 76,31"/>
  <rect class="k-ink k-ring" x="80" y="14" width="60" height="26" rx="4"/>
  <text class="k-label" x="110" y="31" text-anchor="middle">線性掃描</text>
  <line class="k-ink" x1="140" y1="27" x2="152" y2="27"/>
  <polyline class="k-ink" points="148,23 152,27 148,31"/>
  <rect class="k-ink k-ring" x="152" y="14" width="68" height="26" rx="4"/>
  <text class="k-label" x="186" y="31" text-anchor="middle">消元音回溯</text>
  <line class="k-ink" x1="220" y1="27" x2="230" y2="27"/>
  <polyline class="k-ink" points="226,23 230,27 226,31"/>
  <rect class="k-ink k-ring" x="230" y="14" width="64" height="26" rx="4"/>
  <text class="k-label" x="262" y="31" text-anchor="middle">複輔音前向</text>
  <polyline class="k-accent" points="262,40 262,62 174,62 174,78"/>
  <polyline class="k-accent" points="170,73 174,78 178,73"/>
  <rect class="k-soft" x="128" y="78" width="92" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="128" y="78" width="92" height="28" rx="4"/>
  <text class="k-label-accent" x="174" y="96" text-anchor="middle">音節詞表</text>
  <polyline class="k-muted k-dash" points="128,92 102,92"/>
  <polyline class="k-muted" points="107,88 102,92 107,96"/>
  <rect class="k-muted k-ring" x="24" y="78" width="78" height="28" rx="4"/>
  <text class="k-label" x="63" y="96" text-anchor="middle">退回字元</text>
</svg>
```

## Card 4｜決定性數據

- 模式：數字
- 數字：2,843｜印尼大辭典建出之音節詞表規模（對照組五萬餘）｜§4.1 p. 7
- 數字：約 0.4｜十種印尼南島地方語每字元詞元比維持一致｜摘要 p. 1、§4.4 p. 10
- 數字：+21%｜十種地方語平行句局部詞元序列相似度平均增幅｜摘要 p. 1、§4.4 p. 11
- 數字：0.9956｜跨語言距離秩序與對照分詞法之線性相關係數｜§4.4 p. 11
- 範圍：Lumbantobing 與 Situngkir 2026，千句十二語（未測下游生成）

## Card 5｜典範轉移

- 模式：新論文
- 標題：從印尼語辭典詞表走向泛南島驗證
- 里程碑：2026｜僅以印尼語詞表即跨十種地方語對齊相似詞元段｜本篇 §4.4, pp. 10–11
- 里程碑：2026｜本預印本僅量測分詞幾何，尚未接模型測下游翻譯｜本篇 §4–§5, pp. 7–12
- 里程碑：2026｜英語音節觸發退回機制使每字元詞元數升至逾六成｜本篇 §4.4, p. 10
- 里程碑：2026｜作者構想擴至泛南島諸語並結合手稿影像辨識｜本篇 §5, p. 12
- 註記：以上皆出自本篇預印本，尚無後續他人研究。

## Card 6｜Kairos

- 結語：傳統音節文字的正字法規則，也能為現代低資源南島語模型鋪出低碎片分詞底座。
- 轉變：統計壓縮切分→音節邏輯切分
