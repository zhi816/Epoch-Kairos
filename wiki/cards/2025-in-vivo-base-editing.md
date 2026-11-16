# 卡片文字：2025-in-vivo-base-editing

- **論文頁**：[2025-in-vivo-base-editing](../papers/2025-in-vivo-base-editing.md)
- **證據表**：[2025-in-vivo-base-editing](../evidence/2025-in-vivo-base-editing.md)
- **撰寫者**：Claude Agent by Anthropic（Claude Haiku 5.5），2026-11-15
- **最後核對**：Claude Agent by Anthropic（Claude Haiku 5.5），2026-11-16

## 封面
- 封面斷行：為一名病嬰，／訂做專屬的／基因編輯療法
- 導語：病童因先天代謝缺陷無法處理體內的氨，作者先以替代細胞篩選編輯器，再以包裹藥物的微粒送入肝臟，屬單一患者的未核准用藥。

## Card 2｜世紀瓶頸
- 標題：資源集中於常見變異，獨有的呢？
- 對照：藥物開發｜所需資源龐大，多集中於少數較常見遺傳疾病的復發性變異
- 對照：肝臟移植｜能改善預後，但嬰兒常在可移植前即有高血氨危象與不可逆神經損傷
- 對照：人類肝細胞｜取不到帶此變異的細胞，難以可靠評估編輯效果
- 缺口：方法｜超罕見或獨有的變異，缺少快速開發客製療法的流程
- 結語：超罕見變異的病人，需要快速客製化的療法。

## Card 3｜突破原理
- 標題：替代細胞先篩選，動物支撐起始劑量
- 公式：無
- 無公式理由：原文無公式：PDF 與 PMC 全文均無編號或區塊公式，機制以文字敘述
- 說明：把變異片段放入人類細胞株，篩選編輯器與引導 RNA，再由動物試驗支撐起始劑量。
- 圖類型：示意圖
- 圖說：示意：先在替代細胞篩選編輯器與引導 RNA，再以動物試驗支撐劑量，最後為病童給藥。

```svg
<svg viewBox="0 0 300 140" role="img" aria-label="示意：先在替代細胞篩選編輯器與引導 RNA，再以動物試驗支撐劑量，最後為病童給藥。">
  <rect class="k-accent k-ring" x="4" y="28" width="90" height="84" rx="4"/>
  <rect class="k-ink k-ring" x="106" y="28" width="88" height="84" rx="4"/>
  <rect class="k-ink k-ring" x="206" y="28" width="90" height="84" rx="4"/>
  <line class="k-ink" x1="94" y1="70" x2="104" y2="70"/>
  <polyline class="k-ink" points="98,65 104,70 98,75"/>
  <line class="k-ink" x1="194" y1="70" x2="204" y2="70"/>
  <polyline class="k-ink" points="198,65 204,70 198,75"/>
  <text class="k-label-accent" x="49" y="74" text-anchor="middle">替代細胞篩選</text>
  <text class="k-label" x="150" y="74" text-anchor="middle">動物試驗</text>
  <text class="k-label" x="251" y="74" text-anchor="middle">病童給藥</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：42%｜小鼠全肝矯正編輯最高值，單次給藥｜p. 4、Fig. 2B
- 數字：≤1%｜小鼠目標位點的插入或缺失突變率，各劑量組｜PMC 全文 Fig. 2 圖說 Panel B
- 數字：23→13｜血氨中位數 µmol/L，兩劑間 9，作者稱治療相關差異｜p. 5、Fig. 3E
- 數字：減半｜氮清除劑每日量降至 5 mL/m²，次劑後 2 週｜p. 5
- 範圍：Musunuru 2025，單一病童追蹤 7 週、小鼠試驗；未做肝臟切片

## Card 5｜典範轉移
- 模式：新論文
- 標題：流程走完，療效仍待答
- 里程碑：2025｜計畫書與補充附錄隨全文提供，未提及公開程式碼｜本篇 p. 2、p. 3、PMC 全文 Supplementary Material 清單
- 里程碑：2025｜作者列追蹤時間短、生殖細胞編輯未評估｜本篇 §Discussion 第 1 段
- 里程碑：2025｜作者稱未來必要時病人可再接受更多次或更高劑量｜本篇 §Discussion 第 2 段
- 里程碑：2026｜Li 等回顧區分已有證據與仍屬推測之事項｜Li et al. 2026, Cureus 18(8):e114354
- 註記：前三項出自本篇，Li 等為他人回顧

## Card 6｜Kairos
- 結語：作者預期脂質配方可共用、小鼠與獼猴試驗或可省，但本篇未證實。
- 轉變：從頭開發→共用底盤構想
