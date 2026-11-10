# 卡片文字：2025-tulun-adaptable-lrl-mt-merx

- **論文頁**：[2025-tulun-adaptable-lrl-mt-merx](../papers/2025-tulun-adaptable-lrl-mt-merx.md)
- **證據表**：[2025-tulun-adaptable-lrl-mt-merx](../evidence/2025-tulun-adaptable-lrl-mt-merx.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：讓大模型參考／詞彙表與舊譯文，／修潤譯稿
- 導語：專用翻譯先出初稿，再由大型語言模型依詞彙表與舊譯文修正，不必重新訓練模型。

## Card 2｜世紀瓶頸
- 標題：有詞彙表，翻譯系統卻用不上？
- 對照：微調模型｜把術語加入翻譯模型多要微調，小型組織負擔不起
- 對照：專用翻譯｜會譯錯領域術語，遇到領域外內容常產生幻覺
- 對照：語言模型｜翻成低資源語言時，準確度可能不如專用翻譯模型
- 缺口：工具｜沒有讓非技術使用者直接用上詞彙表與舊譯文的工具
- 結語：要讓懂術語的人，不必寫程式也能改進翻譯。

## Card 3｜突破原理
- 標題：先機器翻譯，再查表後編輯
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，流程以文字與圖 1 說明（§3.1–§3.2）
- 說明：專用翻譯先出初稿，再把查到的詞彙表條目與相似舊譯文交給大型語言模型修正。
- 圖類型：示意圖
- 圖說：示意：來源句先經機器翻譯出初稿，同時查詢詞彙表與翻譯記憶，三者交給語言模型後編輯成最終譯文。

```svg
<svg viewBox="0 0 300 124" role="img" aria-label="示意：來源句先經機器翻譯出初稿，同時查詢詞彙表與翻譯記憶，三者交給語言模型後編輯成最終譯文。">
  <rect class="k-ink k-ring" x="4" y="49" width="48" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="76" y="6" width="64" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="76" y="49" width="64" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="76" y="92" width="64" height="26" rx="4"/>
  <rect class="k-accent k-ring" x="170" y="49" width="66" height="26" rx="4"/>
  <rect class="k-ink k-ring" x="256" y="49" width="40" height="26" rx="4"/>
  <polyline class="k-ink" points="52,62 62,62 62,19 74,19"/>
  <polyline class="k-ink" points="69,14 74,19 69,24"/>
  <line class="k-ink" x1="62" y1="62" x2="74" y2="62"/>
  <polyline class="k-ink" points="69,57 74,62 69,67"/>
  <polyline class="k-ink" points="62,62 62,105 74,105"/>
  <polyline class="k-ink" points="69,100 74,105 69,110"/>
  <polyline class="k-line" points="140,19 154,19 154,105 140,105"/>
  <line class="k-line" x1="140" y1="62" x2="168" y2="62"/>
  <polyline class="k-line" points="163,57 168,62 163,67"/>
  <line class="k-ink" x1="236" y1="62" x2="254" y2="62"/>
  <polyline class="k-ink" points="249,57 254,62 249,67"/>
  <text class="k-label" x="28" y="66" text-anchor="middle">來源句</text>
  <text class="k-label" x="108" y="23" text-anchor="middle">機器翻譯</text>
  <text class="k-label" x="108" y="66" text-anchor="middle">詞彙表</text>
  <text class="k-label" x="108" y="109" text-anchor="middle">翻譯記憶</text>
  <text class="k-label-accent" x="203" y="66" text-anchor="middle">語言模型</text>
  <text class="k-label" x="276" y="66" text-anchor="middle">譯文</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：35.78｜德頓語醫療翻譯 ChrF++，只用 MADLAD｜表 1, p. 133
- 數字：47.87｜同一測試集，MADLAD 初譯再經後編輯｜表 1, p. 133
- 數字：38.26｜FLORES 六種語言平均 ChrF++，只用 NLLB-54B｜表 2, p. 134
- 數字：41.09｜同一設定，NLLB-54B 初譯再經後編輯｜表 2, p. 134
- 範圍：Merx 等 2025，兩組織資料與六種語言評測

## Card 5｜典範轉移
- 模式：新論文
- 標題：下一步，調提示與離線部署
- 里程碑：2025｜以 MIT 授權公開程式碼與線上系統｜本篇 p. 130 註 2
- 里程碑：2025｜作者指出易用性評估僅兩位共同作者｜本篇 倫理聲明, p. 135
- 里程碑：2025｜作者指出基隆迪語因詞彙表誤改而退步｜本篇 §5, p. 134
- 里程碑：2025｜作者計畫最佳化提示並支援離線部署｜本篇 §6, pp. 134–135
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：詞彙表不是越多越好；未經校驗的條目會讓模型改錯字，基隆迪語就因此退步。
- 轉變：一次訓練→持續校正
