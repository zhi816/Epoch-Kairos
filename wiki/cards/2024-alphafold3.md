# 卡片文字：2024-alphafold3

- **論文頁**：[2024-alphafold3](../papers/2024-alphafold3.md)
- **證據表**：[2024-alphafold3](../evidence/2024-alphafold3.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：預測蛋白質與核酸、／藥物結合後的／立體結構
- 導語：把蛋白質、核酸、小分子與離子都放進同一個模型，直接在原子座標上去雜訊，預測結合後的形狀。

## Card 2｜世紀瓶頸
- 標題：一類分子，一套工具
- 對照：剛體框架｜AlphaFold2 只為胺基酸設計
- 對照：專用方法｜各管一種交互，無法處理一般複合體
- 缺口：複合體｜沒有模型能同時處理各類生物分子
- 結語：細胞裡的分子，從不單獨行動。

## Card 3｜突破原理
- 標題：隨機轉向，再從雜訊還原原子
- 公式：\tilde{X}_0 = \mathcal{T}(X_0)
- 說明：整個複合體先隨機旋轉平移再加雜訊，模型學著還原，網路不必內建旋轉對稱。
- 圖類型：示意圖
- 圖說：示意：原子座標先經隨機旋轉平移，再加上雜訊，模型逐步去除雜訊，還原出結構。

```svg
<svg viewBox="0 0 300 96" role="img" aria-label="示意：原子座標先經隨機旋轉平移，再加上雜訊，模型逐步去除雜訊，還原出結構。">
  <rect class="k-ink k-ring" x="4" y="34" width="52" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="64" y="34" width="52" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="124" y="34" width="52" height="30" rx="4"/>
  <rect class="k-accent k-ring" x="184" y="34" width="52" height="30" rx="4"/>
  <rect class="k-ink k-ring" x="244" y="34" width="52" height="30" rx="4"/>
  <line class="k-ink" x1="56" y1="49" x2="62" y2="49"/>
  <polyline class="k-ink" points="58,45 62,49 58,53"/>
  <line class="k-ink" x1="116" y1="49" x2="122" y2="49"/>
  <polyline class="k-ink" points="118,45 122,49 118,53"/>
  <line class="k-ink" x1="176" y1="49" x2="182" y2="49"/>
  <polyline class="k-ink" points="178,45 182,49 178,53"/>
  <line class="k-ink" x1="236" y1="49" x2="242" y2="49"/>
  <polyline class="k-ink" points="238,45 242,49 238,53"/>
  <path class="k-muted k-dash" d="M198 32 C 198 12, 222 12, 222 32"/>
  <polyline class="k-muted" points="217,27 222,32 227,27"/>
  <text class="k-label" x="30" y="53" text-anchor="middle">座標</text>
  <text class="k-label" x="90" y="53" text-anchor="middle">轉向</text>
  <text class="k-label" x="150" y="53" text-anchor="middle">加雜訊</text>
  <text class="k-label-accent" x="210" y="53" text-anchor="middle">去噪</text>
  <text class="k-label" x="270" y="53" text-anchor="middle">結構</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：76.4%｜不給結合口袋，藥物分子位置預測成功率｜Extended Data 表 1, p. 21
- 數字：62.9%｜抗體與抗原介面成功率｜Extended Data 表 1, p. 21
- 數字：64.8｜蛋白質－DNA 介面分數｜Extended Data 表 1, p. 21
- 數字：78.5%｜共價結合配體預測成功率｜Extended Data 表 1, p. 21
- 範圍：Abramson 等 2024，近期結構；DNA 為雙股

## Card 5｜典範轉移
- 標題：程式公開，開源模型跟上
- 里程碑：2024｜Chai-1 公開模型權重與推論程式｜Chai Discovery 2024, bioRxiv
- 里程碑：2024｜Boltz-1 以 MIT 授權開源同等級模型｜Wohlwend et al. 2024, bioRxiv
- 里程碑：2024｜DeepMind 釋出 AlphaFold 3 推論程式｜Abramson et al. 2024, Nature 636:E4
- 註記：三項皆為後續發布，出處見長文

## Card 6｜Kairos
- 結語：拆掉只適合蛋白質的框架，模型反而能處理更多分子。
- 轉變：專用框架→通用生成
