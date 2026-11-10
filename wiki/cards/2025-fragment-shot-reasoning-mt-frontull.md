# 卡片文字：2025-fragment-shot-reasoning-mt-frontull

- **論文頁**：[2025-fragment-shot-reasoning-mt-frontull](../papers/2025-fragment-shot-reasoning-mt-frontull.md)
- **證據表**：[2025-fragment-shot-reasoning-mt-frontull](../evidence/2025-fragment-shot-reasoning-mt-frontull.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：檢索相似片段／當例句，／讓大模型翻譯拉定語
- 導語：翻向拉定語時效果明顯，翻回義大利語則幾乎無益。

## Card 2｜世紀瓶頸
- 標題：資料不夠微調，語意也無從檢索
- 對照：大模型｜對小語言與其變體認識有限，難分變體、譯文不連貫
- 對照：微調｜少於 13,000 句對，就訓練不到可接受的翻譯品質
- 缺口：語意檢索｜拉定語沒有合適的嵌入模型，無法依語意相似度挑例句
- 結語：得換一種不靠語意的選例方法。

## Card 3｜突破原理
- 標題：把句子拆成片段，各找例句
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，片段選取以文字與圖 1 敘述（§3）
- 說明：從 7 個詞的視窗逐步縮到 1 個詞，凡能精確比對的片段就取至多 6 組例句。
- 圖類型：示意圖
- 圖說：示意：待譯句切成片段 A 與片段 B，各自在語料中找到例句，一起送進大模型翻譯。

```svg
<svg viewBox="0 0 300 124" role="img" aria-label="示意：待譯句切成片段 A 與片段 B，各自在語料中找到例句，一起送進大模型翻譯。">
  <rect class="k-accent k-ring" x="40" y="10" width="108" height="24" rx="4"/>
  <rect class="k-accent k-ring" x="152" y="10" width="108" height="24" rx="4"/>
  <rect class="k-soft" x="46" y="50" width="44" height="16" rx="3"/>
  <rect class="k-soft" x="98" y="50" width="44" height="16" rx="3"/>
  <rect class="k-soft" x="158" y="50" width="44" height="16" rx="3"/>
  <rect class="k-soft" x="210" y="50" width="44" height="16" rx="3"/>
  <rect class="k-ink k-ring" x="100" y="94" width="100" height="24" rx="4"/>
  <line class="k-ink k-thin" x1="94" y1="34" x2="68" y2="50"/>
  <line class="k-ink k-thin" x1="94" y1="34" x2="120" y2="50"/>
  <line class="k-ink k-thin" x1="206" y1="34" x2="180" y2="50"/>
  <line class="k-ink k-thin" x1="206" y1="34" x2="232" y2="50"/>
  <line class="k-ink" x1="68" y1="66" x2="146" y2="92"/>
  <line class="k-ink" x1="120" y1="66" x2="148" y2="92"/>
  <line class="k-ink" x1="180" y1="66" x2="152" y2="92"/>
  <line class="k-ink" x1="232" y1="66" x2="154" y2="92"/>
  <text class="k-label" x="4" y="27">待譯句</text>
  <text class="k-label-accent" x="94" y="27" text-anchor="middle">片段 A</text>
  <text class="k-label-accent" x="206" y="27" text-anchor="middle">片段 B</text>
  <text class="k-label" x="68" y="62" text-anchor="middle">例句</text>
  <text class="k-label" x="150" y="111" text-anchor="middle">大模型</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：28.60｜片段提示，Val Badia→Gherdëina BLEU｜Table 1, p. 6
- 數字：13.11｜同方向零樣本提示之 BLEU｜Table 1, p. 6
- 數字：20.94｜同方向改走義大利語樞紐之 BLEU｜Table 1, p. 6
- 數字：14.22｜片段提示，義大利語→Val Badia BLEU｜Table 1, p. 6
- 範圍：Frontull 與 Ströhle 2025，DeepSeek-R1，測試 175 句

## Card 5｜典範轉移
- 模式：新論文
- 標題：推理為何有效，仍待釐清
- 里程碑：2025｜公開程式碼與檢索語料｜本篇 摘要, p. 1
- 里程碑：2025｜只做拉定語與義大利語，測試僅 175 句｜本篇 Limitations, p. 9
- 里程碑：2025｜作者擬探究推理機制與多輪查詢引導｜本篇 Future Work, p. 8
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：親屬變體之間沒有平行句時，可以借一個共同的樞紐語言，讓大模型兩跳推理。
- 轉變：直接對譯→經樞紐兩跳
