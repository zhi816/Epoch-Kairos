# 卡片文字：1995-treg-immune-tolerance

- **論文頁**：[1995-treg-immune-tolerance](../papers/1995-treg-immune-tolerance.md)
- **證據表**：[1995-treg-immune-tolerance](../evidence/1995-treg-immune-tolerance.md)
- **撰寫者**：Claude Agent SDK by Anthropic（Claude Haiku 5.5），2026-11-15
- **最後核對**：Claude Agent SDK by Anthropic（Claude Haiku 5.5），2026-11-16

## 封面
- 封面斷行：找到免疫調控細胞，／抑制免疫攻擊自身
- 導語：免疫系統不傷害自身，不只靠消滅危險細胞，周邊另有一群細胞會抑制自體反應；抽掉後其餘細胞轉輸裸鼠，便發生多器官自體免疫病。

## Card 2｜世紀瓶頸
- 標題：潛在致病的細胞，為何不發病？
- 對照：表面標記｜清除高或低表現的亞群可誘發疾病，但標記不夠專一
- 對照：定位｜scurfy 只定位到一段區間，致病基因仍未知
- 缺口：標記｜缺能只圈出有抑制作用的細胞、不混入其他細胞的表面標記
- 結語：要看清免疫如何自我節制，得先有夠專一的標記。

## Card 3｜突破原理
- 標題：用抗體清除一群細胞，看是否發病
- 公式：無
- 無公式理由：原文無公式：兩篇全文均無編號或展示型方程式，僅有文字、表與圖
- 說明：抗體加補體清掉介白素 2 受體 α 鏈陽性細胞，其餘細胞轉輸裸鼠會發病。
- 圖類型：示意圖
- 圖說：示意：全細胞轉輸裸鼠未發病；清除一群細胞後，其餘細胞轉輸裸鼠便發病。

```svg
<svg viewBox="0 0 300 176" role="img" aria-label="示意：全細胞轉輸裸鼠未發病；清除一群細胞後，其餘細胞轉輸裸鼠便發病。">
  <line class="k-muted k-thin" x1="150" y1="18" x2="150" y2="158"/>
  <text class="k-label" x="75" y="26" text-anchor="middle">全細胞</text>
  <circle class="k-muted k-ring" cx="52" cy="48" r="6.5"/>
  <circle class="k-muted k-ring" cx="75" cy="48" r="6.5"/>
  <circle class="k-muted k-ring" cx="98" cy="48" r="6.5"/>
  <line class="k-muted" x1="75" y1="58" x2="75" y2="80"/>
  <polyline class="k-muted" points="71,75 75,81 79,75"/>
  <rect class="k-muted k-ring" x="22" y="82" width="106" height="28" rx="4"/>
  <text class="k-label" x="75" y="101" text-anchor="middle">轉輸裸鼠</text>
  <line class="k-muted" x1="75" y1="112" x2="75" y2="130"/>
  <polyline class="k-muted" points="71,125 75,131 79,125"/>
  <rect class="k-muted k-ring" x="22" y="132" width="106" height="28" rx="4"/>
  <text class="k-label" x="75" y="151" text-anchor="middle">未發病</text>
  <text class="k-label-accent" x="225" y="26" text-anchor="middle">清除一群細胞</text>
  <circle class="k-muted k-ring k-dash" cx="188" cy="48" r="6.5"/>
  <line class="k-accent" x1="183" y1="43" x2="193" y2="53"/>
  <circle class="k-muted k-ring" cx="219" cy="48" r="6.5"/>
  <circle class="k-muted k-ring" cx="243" cy="48" r="6.5"/>
  <line class="k-accent" x1="225" y1="58" x2="225" y2="80"/>
  <polyline class="k-accent" points="221,75 225,81 229,75"/>
  <rect class="k-accent k-ring" x="172" y="82" width="106" height="28" rx="4"/>
  <text class="k-label-accent" x="225" y="101" text-anchor="middle">轉輸裸鼠</text>
  <line class="k-accent" x1="225" y1="112" x2="225" y2="130"/>
  <polyline class="k-accent" points="221,125 225,131 229,125"/>
  <rect class="k-accent k-ring" x="172" y="132" width="106" height="28" rx="4"/>
  <text class="k-label-accent" x="225" y="151" text-anchor="middle">發病</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：22/22｜清除介白素 2 受體 α 鏈陽性細胞，轉輸受鼠胃炎數｜p. 1155, Table I, Group D
- 數字：0/18｜補體處理全細胞後轉輸，對照組胃炎數｜p. 1155, Table I, Group A
- 數字：0/14｜2001 年，帶 Foxp3 轉殖基因的 scurfy 雄鼠發病數｜p. 70, Table 1
- 數字：6/6｜2001 年，未帶轉殖基因的 scurfy 雄鼠發病數｜p. 70, Table 1
- 範圍：Sakaguchi 1995 上排（轉輸裸鼠）；Brunkow 2001 下排（5 品系）

## Card 5｜典範轉移
- 標題：兩條線索，匯流到一個基因
- 里程碑：2001｜Wildin 等在人類患者找到 FOXP3 突變｜Wildin et al. 2001, Nature Genetics 27:18-20
- 里程碑：2003｜Hori 等顯示 Foxp3 專一見於天然調節性 T 細胞｜Hori, Nomura & Sakaguchi 2003, Science 299:1057-1061
- 里程碑：2003｜Fontenot 等指出調節性 T 細胞發育需要 Foxp3｜Fontenot, Gavin & Rudensky 2003, Nature Immunology 4:330-336
- 里程碑：2003｜Khattri 等指出 scurfin 缺陷鼠無調節性 T 細胞｜Khattri et al. 2003, Nature Immunology 4:337-342
- 里程碑：2025｜Brunkow 等三人獲諾貝爾生理學或醫學獎｜獎項
- 註記：前四項為後續研究；Brunkow、Ramsdell 非 1995 作者

## Card 6｜Kairos
- 結語：細胞實驗缺分子開關，基因定位缺細胞載體，兩條線要到 2003 年才接上。
- 轉變：基因→細胞亞群
