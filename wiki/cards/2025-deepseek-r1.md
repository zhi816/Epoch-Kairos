# 卡片文字：2025-deepseek-r1

- **論文頁**：[2025-deepseek-r1](../papers/2025-deepseek-r1.md)
- **證據表**：[2025-deepseek-r1](../evidence/2025-deepseek-r1.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：以對錯獎勵訓練，／讓語言模型／學會逐步推理
- 導語：不先用人寫的示範微調，只以規則判定答案對錯，模型便在訓練中學會反思與驗證。

## Card 2｜世紀瓶頸
- 標題：沒有人類示範，模型學得會推理嗎？
- 對照：監督微調｜要大量人寫的思維鏈，昂貴又把模型綁在人類的寫法
- 對照：價值模型｜規模與策略模型相近，記憶體與運算負擔都大
- 對照：神經獎勵｜另用網路打分，大規模訓練時容易被鑽漏洞
- 缺口：方法｜沒有不靠人類示範、又能擴大規模的推理訓練法
- 結語：要讓模型自己摸索，先得有可靠的對錯訊號。

## Card 3｜突破原理
- 標題：同一題的回答，彼此比較
- 公式：A_i = \frac{r_i - \operatorname{mean}(\{r_1, r_2, \cdots, r_G\})}{\operatorname{std}(\{r_1, r_2, \cdots, r_G\})}
- 說明：獎勵減去組內平均、除以標準差即為優勢，因此不必另訓價值模型。
- 圖類型：示意圖
- 圖說：示意：每題取樣一組回答，由規則檢查對錯打分，組內比較後更新模型，再取樣下一輪。

```svg
<svg viewBox="0 0 300 100" role="img" aria-label="示意：每題取樣一組回答，由規則檢查對錯打分，組內比較後更新模型，再取樣下一輪。">
  <polyline class="k-muted" points="12,26 68,26 68,54"/>
  <polyline class="k-muted" points="8,30 64,30 64,58"/>
  <rect class="k-ink k-ring" x="4" y="34" width="56" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="84" y="34" width="56" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="156" y="34" width="56" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="228" y="34" width="56" height="28" rx="4"/>
  <line class="k-ink" x1="70" y1="48" x2="82" y2="48"/>
  <polyline class="k-ink" points="77,43 82,48 77,53"/>
  <line class="k-line" x1="142" y1="48" x2="154" y2="48"/>
  <polyline class="k-line" points="149,43 154,48 149,53"/>
  <line class="k-ink" x1="214" y1="48" x2="226" y2="48"/>
  <polyline class="k-ink" points="221,43 226,48 221,53"/>
  <polyline class="k-muted k-dash" points="256,64 256,86 32,86 32,66"/>
  <polyline class="k-muted" points="27,71 32,66 37,71"/>
  <text class="k-label" x="32" y="52" text-anchor="middle">一組回答</text>
  <text class="k-label-accent" x="112" y="52" text-anchor="middle">規則檢查</text>
  <text class="k-label" x="184" y="52" text-anchor="middle">組內比較</text>
  <text class="k-label" x="256" y="52" text-anchor="middle">更新模型</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：15.6%｜R1-Zero 訓練前，AIME 2024 平均 pass@1｜§2.3, p. 4
- 數字：77.9%｜同一模型純強化學習 10,400 步後｜§2.3, p. 4
- 數字：72.6%｜蒸餾 R1 的 32B 小模型，同一指標｜Table 16, p. 61
- 數字：47.0%｜同一 32B 基座直接做大規模強化學習｜Table 16, p. 61
- 範圍：DeepSeek-AI 2025，美國數學邀請賽題；pass@1 為取樣平均

## Card 5｜典範轉移
- 模式：新論文
- 標題：公開權重，也列出待解弱點
- 里程碑：2025｜公開 R1、R1-Zero 與六個蒸餾模型權重｜本篇 Supplementary I, p. 65
- 里程碑：2025｜作者列出不能用工具、過度思考等限制｜本篇 §6, pp. 10–11
- 里程碑：2025｜作者指出難驗證任務仍難靠強化學習｜本篇 §6, p. 11
- 里程碑：2025｜作者期待可靠獎勵模型與工具輔助推理｜本篇 §6, p. 11
- 註記：以上皆出自本篇，未列後續研究

## Card 6｜Kairos
- 結語：只要求最終答案正確、又允許先在內部推演，反思與回頭重算便自行出現。
- 轉變：專屬模組→搜索副產品
