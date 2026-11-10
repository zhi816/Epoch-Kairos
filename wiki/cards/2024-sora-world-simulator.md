# 卡片文字：2024-sora-world-simulator

- **論文頁**：[2024-sora-world-simulator](../papers/2024-sora-world-simulator.md)
- **證據表**：[2024-sora-world-simulator](../evidence/2024-sora-world-simulator.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：把影片切成／時空小塊，／生成連貫的長影片
- 導語：綜述 Sora：把影片壓縮切塊，再逐步去除雜訊。
- 封面標題：Sora 與世界模型

## Card 2｜世紀瓶頸
- 標題：裁成方形的短片，限制了模型
- 對照：固定解析度｜常裁成 4 秒、256×256 的方形短片
- 對照：U-Net｜擴散模型的骨幹多為卷積 U-Net
- 缺口：擴展｜影片能否像語言靠擴大規模變好
- 結語：影片得先切成像文字一樣的小單位。

## Card 3｜突破原理
- 標題：壓縮、切塊，再逐步去雜訊
- 公式：無
- 無公式理由：原文無公式：OpenAI 報告未公開機制公式；綜述圖 4 為逆向推測
- 說明：影片壓縮切塊後，模型依文字等條件，從帶雜訊小塊預測乾淨小塊。
- 圖類型：示意圖
- 圖說：示意：影片先壓縮再切成時空小塊，模型從加了雜訊的小塊逐步預測出乾淨的小塊。

```svg
<svg viewBox="0 0 300 96" role="img" aria-label="示意：影片先壓縮再切成時空小塊，模型從加了雜訊的小塊逐步預測出乾淨的小塊。">
  <rect class="k-ink k-ring" x="4" y="34" width="40" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="58" y="34" width="40" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="112" y="34" width="14" height="14"/>
  <rect class="k-ink k-ring" x="130" y="34" width="14" height="14"/>
  <rect class="k-ink k-ring" x="148" y="34" width="14" height="14"/>
  <rect class="k-ink k-ring" x="112" y="50" width="14" height="14"/>
  <rect class="k-ink k-ring" x="130" y="50" width="14" height="14"/>
  <rect class="k-ink k-ring" x="148" y="50" width="14" height="14"/>
  <rect class="k-accent k-ring" x="178" y="34" width="52" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="244" y="34" width="52" height="30" rx="4"/>
  <line class="k-ink" x1="44" y1="49" x2="56" y2="49"/>
  <polyline class="k-ink" points="51,44 56,49 51,54"/>
  <line class="k-ink" x1="98" y1="49" x2="110" y2="49"/>
  <polyline class="k-ink" points="105,44 110,49 105,54"/>
  <line class="k-ink" x1="164" y1="49" x2="176" y2="49"/>
  <polyline class="k-ink" points="171,44 176,49 171,54"/>
  <line class="k-ink" x1="230" y1="49" x2="242" y2="49"/>
  <polyline class="k-ink" points="237,44 242,49 237,54"/>
  <path class="k-muted k-dash" d="M192 32 C 192 12, 216 12, 216 32"/>
  <polyline class="k-muted" points="211,27 216,32 221,27"/>
  <text class="k-label" x="24" y="53" text-anchor="middle">影片</text>
  <text class="k-label" x="78" y="53" text-anchor="middle">壓縮</text>
  <text class="k-label" x="137" y="82" text-anchor="middle">時空小塊</text>
  <text class="k-label-accent" x="204" y="53" text-anchor="middle">去雜訊</text>
  <text class="k-label" x="270" y="53" text-anchor="middle">乾淨小塊</text>
</svg>
```

## Card 4｜決定性數據
- 模式：結論
- 結論：加大訓練算力，樣本品質明顯提升｜Brooks 等 2024 §Scaling
- 結論：以原尺寸訓練，取景比裁成方形更完整｜圖 6, p. 7
- 結論：咬了餅乾卻沒咬痕：物理因果仍常出錯｜§5.1, p. 23
- 範圍：Liu 等綜述與 OpenAI 報告，皆無量化指標

## Card 5｜典範轉移
- 模式：新論文
- 標題：下一步，檢驗物理定律
- 里程碑：2024｜作者指出物理因果與左右方位常出錯｜本篇 §5.1, p. 23
- 里程碑：2024｜作者指出影片最長一分鐘，多為數十秒｜本篇 §5.1, p. 23
- 里程碑：2024｜Kang 等測物理定律：模型只模仿相近案例｜Kang et al. 2024, arXiv:2411.02385
- 註記：前兩項出自本篇；末項為後續研究

## Card 6｜Kairos
- 結語：與其把每段影片裁成一樣，不如保留原樣，切成小塊。
- 轉變：裁成方形→原樣切塊
