# 卡片文字：1985-macroscopic-quantum-tunneling

- **論文頁**：[1985-macroscopic-quantum-tunneling](../papers/1985-macroscopic-quantum-tunneling.md)
- **證據表**：[1985-macroscopic-quantum-tunneling](../evidence/1985-macroscopic-quantum-tunneling.md)
- **撰寫者**：Claude Code by Anthropic（模型版本依平台規範不寫入版控檔案），2026-11-10
- **最後核對**：Claude Code by Anthropic（模型版本依平台規範不寫入版控檔案），2026-11-10

## 封面
- 封面斷行：用微波，／量出超導電路／一階一階的能量
- 導語：微波對上能階間距時，超導接面更容易出現電壓，顯示巨觀變數也有量子化的能階。

## Card 2｜世紀瓶頸
- 標題：巨觀變數，也遵守量子力學嗎？
- 對照：逃逸率量測｜看低溫下穿隧逃出位能井的速率，但看不到井內的能階
- 對照：熱活化｜溫度偏高時，接面靠熱擾動逃出，表現是古典的
- 對照：共振活化｜古典粒子在電漿頻率也會被微波共振激發
- 缺口：量測方式｜還沒有不靠全部接面參數，就能分出量子能階與古典響應的做法
- 結語：要看的是共振落在哪裡，而不只是有沒有共振。

## Card 3｜突破原理
- 標題：讓微波對上能階的間距
- 公式：\Delta U = \frac{4}{3}\sqrt{2}\,U_0 (1 - I/I_0)^{3/2}
- 說明：偏壓電流越接近臨界電流 $I_0$，位能障 $\Delta U$ 越低，能階間距也越小。
- 圖類型：示意圖
- 圖說：示意：位能井裡的能階越往上越密，微波對上相鄰能階的間距時，粒子跳上高能階，更容易逃出位能井。

```svg
<svg viewBox="0 0 300 124" role="img" aria-label="示意：位能井裡的能階越往上越密，微波對上相鄰能階的間距時，粒子跳上高能階，更容易逃出位能井。">
  <path class="k-line" d="M12 8 C 40 8, 55 104, 95 104 C 135 104, 155 44, 185 44 C 215 44, 250 80, 292 116"/>
  <line class="k-ink k-thin" x1="79" y1="96" x2="116" y2="96"/>
  <line class="k-ink k-thin" x1="67" y1="82" x2="133" y2="82"/>
  <line class="k-ink k-thin" x1="60" y1="70" x2="144" y2="70"/>
  <polyline class="k-ink" points="18,92 23,87 28,97 33,87 38,97 43,87 48,97 53,92"/>
  <line class="k-accent" x1="97" y1="95" x2="97" y2="84"/>
  <polyline class="k-accent" points="93,88 97,83 101,88"/>
  <line class="k-ink k-dash" x1="148" y1="70" x2="235" y2="70"/>
  <polyline class="k-ink" points="230,65 235,70 230,75"/>
  <text class="k-label" x="185" y="34" text-anchor="middle">位能障</text>
  <text class="k-label" x="50" y="74" text-anchor="end">能階</text>
  <text class="k-label-accent" x="36" y="114" text-anchor="middle">微波</text>
  <text class="k-label" x="250" y="62">逃出</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：3 個｜2.0 GHz 微波、28 mK 下的逃逸率共振峰｜p. 1544、Fig. 2(a)
- 數字：4 個｜18 mK 下換用的微波頻率，共振移動皆合預測｜p. 1545、Fig. 3
- 數字：50 ± 10｜共振之 ω/Δω，與古典區所量 Q 大致相符｜p. 1545、Fig. 3(a)
- 數字：40 ns｜推得激發態與基態可維持同調的時間｜p. 1545
- 範圍：Martinis 等 1985，兩個超導接面之低溫量測，無擬合參數

## Card 5｜典範轉移
- 標題：接面的能階，後來成了量子位元
- 里程碑：1987｜同一團隊完整報告穿隧與能階實驗｜Martinis, Devoret & Clarke 1987, PRB 35:4682-4698
- 里程碑：2002｜Yu 等以微波觀察接面量子態同調振盪｜Yu et al. 2002, Science 296:889-892
- 里程碑：2002｜Martinis 等以接面最低兩能階作量子位元｜Martinis et al. 2002, PRL 89:117901
- 里程碑：2025｜Clarke、Devoret 與 Martinis 獲諾貝爾物理學獎｜獎項
- 註記：前三項為後續研究，出處見長文

## Card 6｜Kairos
- 結語：接面參數先在古典區量準，量子預測便無從事後調整。
- 轉變：古典事件→量子探針
