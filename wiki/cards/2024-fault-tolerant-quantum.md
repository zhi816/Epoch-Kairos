# 卡片文字：2024-fault-tolerant-quantum

- **論文頁**：[2024-fault-tolerant-quantum](../papers/2024-fault-tolerant-quantum.md)
- **證據表**：[2024-fault-tolerant-quantum](../evidence/2024-fault-tolerant-quantum.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：用雷射搬動原子，／在受糾錯保護的／位元上運算
- 導語：搬動原子做邏輯閘，糾纏隨碼距增大而改善。

## Card 2｜世紀瓶頸
- 標題：加了糾錯，錯誤反而變多？
- 對照：糾錯電路｜要大量雙位元閘與量測，閘不夠準時反而引入更多錯
- 對照：平面近鄰｜只能與相鄰位元互動，兩個邏輯位元間的閘要繞道多步
- 對照：中途讀取｜讀取輔助位元時，須避免干擾仍在運算的位元
- 缺口：架構｜缺少能在邏輯位元層級直接編程運算的處理器
- 結語：得讓邏輯位元本身能被直接編程。

## Card 3｜突破原理
- 標題：搬原子成對打閘，再一起解碼
- 公式：\sum_{j=1}^{M} \log(p_j) E_j + \log(1 - p_j)(1 - E_j)
- 說明：以各錯誤機率 p_j 計分，在與偵測結果相符的錯誤組合中找最可能的一組。
- 圖類型：示意圖
- 圖說：示意：兩個邏輯區塊被搬到一起交錯排列，一道全域雷射同時對每對原子打閘，之後兩區塊一起解碼。

```svg
<svg viewBox="0 0 300 110" role="img" aria-label="示意：兩個邏輯區塊被搬到一起交錯排列，一道全域雷射同時對每對原子打閘，之後兩區塊一起解碼。">
  <rect class="k-soft" x="126" y="36" width="78" height="46" rx="4"/>
  <circle class="k-ink" cx="14" cy="22" r="3.5"/>
  <circle class="k-ink" cx="28" cy="22" r="3.5"/>
  <circle class="k-ink" cx="42" cy="22" r="3.5"/>
  <circle class="k-ink" cx="14" cy="36" r="3.5"/>
  <circle class="k-ink" cx="28" cy="36" r="3.5"/>
  <circle class="k-ink" cx="42" cy="36" r="3.5"/>
  <circle class="k-ink k-ring" cx="14" cy="78" r="3.5"/>
  <circle class="k-ink k-ring" cx="28" cy="78" r="3.5"/>
  <circle class="k-ink k-ring" cx="42" cy="78" r="3.5"/>
  <circle class="k-ink k-ring" cx="14" cy="92" r="3.5"/>
  <circle class="k-ink k-ring" cx="28" cy="92" r="3.5"/>
  <circle class="k-ink k-ring" cx="42" cy="92" r="3.5"/>
  <line class="k-ink" x1="92" y1="58" x2="116" y2="58"/>
  <polyline class="k-ink" points="111,53 116,58 111,63"/>
  <circle class="k-ink" cx="134" cy="48" r="3.5"/>
  <circle class="k-ink" cx="160" cy="48" r="3.5"/>
  <circle class="k-ink" cx="186" cy="48" r="3.5"/>
  <circle class="k-ink" cx="134" cy="70" r="3.5"/>
  <circle class="k-ink" cx="160" cy="70" r="3.5"/>
  <circle class="k-ink" cx="186" cy="70" r="3.5"/>
  <circle class="k-ink k-ring" cx="144" cy="48" r="3.5"/>
  <circle class="k-ink k-ring" cx="170" cy="48" r="3.5"/>
  <circle class="k-ink k-ring" cx="196" cy="48" r="3.5"/>
  <circle class="k-ink k-ring" cx="144" cy="70" r="3.5"/>
  <circle class="k-ink k-ring" cx="170" cy="70" r="3.5"/>
  <circle class="k-ink k-ring" cx="196" cy="70" r="3.5"/>
  <line class="k-line" x1="208" y1="59" x2="226" y2="59"/>
  <polyline class="k-line" points="221,54 226,59 221,64"/>
  <rect class="k-accent k-ring" x="230" y="45" width="62" height="28" rx="4"/>
  <text class="k-label" x="54" y="33">區塊 A</text>
  <text class="k-label" x="54" y="89">區塊 B</text>
  <text class="k-label" x="165" y="28" text-anchor="middle">全域雷射</text>
  <text class="k-label" x="165" y="98" text-anchor="middle">交錯排列</text>
  <text class="k-label-accent" x="261" y="63" text-anchor="middle">一起解碼</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：146｜d=7 時每個邏輯貝爾對使用的物理位元｜Fig. 2d
- 數字：72(2)%｜容錯製備四邏輯位元 GHZ 態的保真度｜Fig. 3c
- 數字：40｜280 個物理位元上製備的色碼邏輯位元｜Fig. 4b–c
- 數字：≈0.1｜48 邏輯位元電路經錯誤偵測後的 XEB｜Fig. 5f
- 範圍：Bluvstein 等 2024，最多 280 個原子；糾纏改善需相關解碼

## Card 5｜典範轉移
- 標題：原子陣列，朝更大規模推進
- 里程碑：2024｜Xu 等提出原子陣列上的高編碼率糾錯碼｜Xu et al. 2024, Nature Physics 20:1084-1090
- 里程碑：2024｜Google 團隊的表面碼錯誤率低於閾值｜Google Quantum AI 2024, Nature 638:920-926
- 里程碑：2025｜Zhou 等以相關解碼減少量測輪數｜Zhou et al. 2025, Nature 646:303-308
- 里程碑：2025｜Chiu 等讓逾三千原子陣列連續運作｜Chiu et al. 2025, Nature 646:1075-1080
- 註記：以上皆為後續研究，出處見長文

## Card 6｜Kairos
- 結語：把兩排原子搬到一起再打一道雷射，搬運本身就成了對整個區塊的運算。
- 轉變：搬資料是負擔→搬動即運算
