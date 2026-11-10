# 卡片文字：2023-low-resource-nmt-survey-ranathunga

- **論文頁**：[2023-low-resource-nmt-survey-ranathunga](../papers/2023-low-resource-nmt-survey-ranathunga.md)
- **證據表**：[2023-low-resource-nmt-survey-ranathunga](../evidence/2023-low-resource-nmt-survey-ranathunga.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：盤點資料稀少時，／機器翻譯的各種做法
- 導語：依平行語料有多少、有無單語語料，替低資源翻譯整理出挑選技術的流程。
- 封面標題：低資源神經機器翻譯綜述
- 研究類型：綜述

## Card 2｜世紀瓶頸
- 標題：語料不足，也沒有一致的定義
- 對照：神經翻譯｜需要大量平行語料，世上多數語言都做不到
- 對照：低資源｜沒有統一定義，作者以少於 50 萬句為參考
- 缺口：新研究者｜缺少系統整理，難以依資料條件挑選合適的方法
- 結語：需要一張依資料條件挑技術的地圖。

## Card 3｜突破原理
- 標題：依語料多寡，選擇翻譯技術
- 公式：無
- 無公式理由：原文僅有評估指標公式：唯一編號式為 §12.1 式 (1)，以四分位距篩選離群語言（p. 229:22）
- 說明：先看有無平行語料與規模，再看單語語料與共同語言，決定用哪一類技術。
- 圖類型：示意圖
- 圖說：示意：有平行語料時依規模選監督式或半監督等方法；沒有時看單語語料，選無監督或人工建立語料。

```svg
<svg viewBox="0 0 300 130" role="img" aria-label="示意：有平行語料時依規模選監督式或半監督等方法；沒有時看單語語料，選無監督或人工建立語料。">
  <rect class="k-accent k-ring" x="4" y="18" width="70" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="4" y="84" width="70" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="196" y="2" width="100" height="24" rx="4"/>
  <rect class="k-ink k-ring" x="196" y="36" width="100" height="24" rx="4"/>
  <rect class="k-ink k-ring" x="196" y="70" width="100" height="24" rx="4"/>
  <rect class="k-ink k-ring" x="196" y="104" width="100" height="24" rx="4"/>
  <line class="k-ink" x1="74" y1="32" x2="194" y2="14"/>
  <line class="k-ink" x1="74" y1="32" x2="194" y2="48"/>
  <line class="k-ink k-dash" x1="39" y1="46" x2="39" y2="82"/>
  <line class="k-ink" x1="74" y1="98" x2="194" y2="82"/>
  <line class="k-ink k-dash" x1="74" y1="98" x2="194" y2="116"/>
  <text class="k-label-accent" x="39" y="36" text-anchor="middle">平行語料</text>
  <text class="k-label" x="39" y="102" text-anchor="middle">單語語料</text>
  <text class="k-label" x="246" y="18" text-anchor="middle">監督式</text>
  <text class="k-label" x="246" y="52" text-anchor="middle">半監督等</text>
  <text class="k-label" x="246" y="86" text-anchor="middle">無監督</text>
  <text class="k-label" x="246" y="120" text-anchor="middle">人工建立</text>
</svg>
```

## Card 4｜決定性數據
- 模式：結論
- 結論：多語言翻譯論文到 2019 年最多，其後無監督略為超越｜§10，圖 6a, p. 229:19
- 結論：各語言的神經翻譯論文數，與其可用資料量密切相關｜§10，圖 6b, p. 229:20
- 結論：作者建議建立資源、公開模型與算力，並納入區域社群｜§14, p. 229:27
- 範圍：Ranathunga 等 2023，文獻綜述；檢索至 2021 年 1 月

## Card 5｜典範轉移
- 標題：後續細究補資料的方法
- 里程碑：2023｜McNamee 等在 60 種語言上實測回譯｜McNamee & Duh 2023, Findings of ACL 2023:8166-8183
- 里程碑：2024｜Pang 等比較單語資料的各種用法｜Pang et al. 2024, Computational Linguistics 50(1):25-47
- 里程碑：2026｜Ranathunga 等評估以他領域語料調整多語模型｜Ranathunga et al. 2026, ACM TALLIP 25(4):1-34
- 註記：以上皆為引用本篇之後續研究，出處見長文

## Card 6｜Kairos
- 結語：先數清手上的平行與單語語料，再依流程圖挑技術；人工建語料也是一步。
- 轉變：無從挑選→依料選法
