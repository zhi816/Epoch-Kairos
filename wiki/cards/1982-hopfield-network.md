# 卡片文字：1982-hopfield-network

- **論文頁**：[1982-hopfield-network](../papers/1982-hopfield-network.md)
- **證據表**：[1982-hopfield-network](../evidence/1982-hopfield-network.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-09

## 封面
- 封面斷行：讓神經網路／從殘缺線索／想起完整記憶
- 導語：借用磁性材料的能量模型，說明一群簡單的神經元連在一起，就能從殘缺的線索想起完整的記憶。

## Card 2｜世紀瓶頸
- 標題：帶回饋的網路，會不會停下來？
- 對照：邏輯電路｜單一元件時序錯亂或損壞，整個系統就崩潰
- 對照：大腦｜神經元隨機非同步激發、隨時可能受損，卻依然記得住
- 缺口：理論｜感知器的局限被指出後，沒有數學能分析帶回饋迴路的網路是否穩定
- 結語：缺的是一套能說明網路必然收斂的數學。

## Card 3｜突破原理
- 標題：把記憶變成能量的谷底
- 公式：E = -\frac{1}{2} \sum_{i \neq j} T_{ij} V_i V_j + \sum_{i} U_i V_i
- 說明：連接對稱時，每翻轉一個神經元，能量只降不升，網路必然停在某個谷底。
- 圖類型：示意圖
- 圖說：示意：殘缺線索像一顆球沿能量地形滾下，深谷是記憶，淺谷是偽穩定態。

```svg
<svg viewBox="0 0 300 124" role="img" aria-label="示意：殘缺線索像一顆球沿能量地形滾下，深谷是記憶，淺谷是偽穩定態。">
  <path class="k-line" d="M4 18 C 30 18, 40 96, 70 96 C 100 96, 106 40, 132 40 C 156 40, 160 70, 178 70 C 196 70, 204 30, 228 30 C 252 30, 258 104, 280 104 C 290 104, 294 60, 298 40"/>
  <circle class="k-accent" cx="70" cy="96" r="3.4"/>
  <circle class="k-accent" cx="280" cy="104" r="3.4"/>
  <circle class="k-muted k-ring" cx="178" cy="70" r="2.6"/>
  <circle class="k-ink" cx="22" cy="34" r="5"/>
  <line class="k-ink k-dash" x1="30" y1="42" x2="44" y2="66"/>
  <text class="k-label" x="34" y="20">殘缺線索</text>
  <text class="k-label-accent" x="70" y="116" text-anchor="middle">記憶 A</text>
  <text class="k-label" x="178" y="90" text-anchor="middle">偽穩定態</text>
  <text class="k-label-accent" x="280" y="120" text-anchor="end">記憶 B</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：0.15N｜嚴重出錯前，約可存的記憶數（N 為神經元數）｜p. 2556–2557、Fig. 2
- 數字：≈ 85%｜30 個神經元存 5 個記憶，隨機起點落回指定記憶｜p. 2557
- 數字：≈ 10%｜同一實驗中，停在無意義的偽穩定態｜p. 2557
- 數字：1/√2｜單向連接分析中，信噪比為原來的此倍｜p. 2557
- 範圍：Hopfield 1982，30 至 100 個神經元之數值模擬與解析

## Card 5｜典範轉移
- 標題：物理學家，走進神經網路
- 里程碑：1985｜Amit 等以自旋玻璃理論解出臨界容量約 0.138N｜Amit, Gutfreund & Sompolinsky 1985, PRL 55:1530-1533
- 里程碑：1985｜Ackley、Hinton 與 Sejnowski 提出波茲曼機｜Ackley, Hinton & Sejnowski 1985, Cognitive Science 9:147-169
- 里程碑：2021｜現代 Hopfield 網路等價於注意力機制｜Ramsauer et al. 2021, ICLR 2021
- 里程碑：2024｜Hopfield 與 Hinton 獲諾貝爾物理學獎｜獎項
- 註記：前三項為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：不要把物理定律當成計算要克服的雜訊，而要把物理定律本身，變成計算的引擎。
- 轉變：局部規則→湧現記憶
