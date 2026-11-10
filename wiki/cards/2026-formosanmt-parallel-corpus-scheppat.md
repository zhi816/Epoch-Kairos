# 卡片文字：2026-formosanmt-parallel-corpus-scheppat

- **論文頁**：[2026-formosanmt-parallel-corpus-scheppat](../papers/2026-formosanmt-parallel-corpus-scheppat.md)
- **證據表**：[2026-formosanmt-parallel-corpus-scheppat](../evidence/2026-formosanmt-parallel-corpus-scheppat.md)
- **撰寫者**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10
- **最後核對**：Claude Code by Anthropic（Claude Opus 5.5），2026-11-10

## 封面
- 封面斷行：彙整各族語／與中文的對照句，／建成翻譯語料庫
- 導語：收錄臺灣各原住民族語言與華語、英語的對照句，連同整理腳本與基準模型一起公開。

## Card 2｜世紀瓶頸
- 標題：族語平行語料少，又散在各處
- 對照：瀕危語言｜缺少書寫傳統與說話人口，平行語料難以累積
- 對照：前人｜只用辭典資料的一部分，自行篩選切分，結果無法與本篇比較
- 缺口：公開來源｜辭典、教材、田野紀錄與影片字幕分散各處，品質不一
- 結語：得把散落的資料整理成能直接訓練的語料。

## Card 3｜突破原理
- 標題：先清洗過濾，再分來源切分
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，過濾規則以文字敘述（§3.3, p. 3448）
- 說明：正規化文字，剔除非平行內容與長度比懸殊的句對，再按來源切成訓練、開發、測試集。
- 圖類型：示意圖
- 圖說：示意：多個公開來源的句對經清洗過濾後，按來源切分，再分別訓練兩種翻譯模型。

```svg
<svg viewBox="0 0 300 112" role="img" aria-label="示意：多個公開來源的句對經清洗過濾後，按來源切分，再分別訓練兩種翻譯模型。">
  <rect class="k-soft" x="6" y="10" width="58" height="12" rx="3"/>
  <rect class="k-soft" x="6" y="26" width="58" height="12" rx="3"/>
  <rect class="k-soft" x="6" y="42" width="58" height="12" rx="3"/>
  <rect class="k-ink k-ring" x="2" y="4" width="66" height="56" rx="4"/>
  <rect class="k-ink k-ring" x="84" y="18" width="62" height="28" rx="4"/>
  <rect class="k-ink k-ring" x="162" y="18" width="62" height="28" rx="4"/>
  <rect class="k-accent k-ring" x="240" y="18" width="58" height="28" rx="4"/>
  <line class="k-ink" x1="68" y1="32" x2="82" y2="32"/>
  <polyline class="k-ink" points="77,27 82,32 77,37"/>
  <line class="k-ink" x1="146" y1="32" x2="160" y2="32"/>
  <polyline class="k-ink" points="155,27 160,32 155,37"/>
  <line class="k-ink" x1="224" y1="32" x2="238" y2="32"/>
  <polyline class="k-ink" points="233,27 238,32 233,37"/>
  <line class="k-ink k-thin" x1="269" y1="46" x2="250" y2="78"/>
  <line class="k-ink k-thin" x1="269" y1="46" x2="288" y2="78"/>
  <circle class="k-ink k-ring" cx="250" cy="88" r="9"/>
  <circle class="k-ink k-ring" cx="288" cy="88" r="9"/>
  <text class="k-label" x="35" y="78" text-anchor="middle">公開來源</text>
  <text class="k-label" x="115" y="36" text-anchor="middle">清洗過濾</text>
  <text class="k-label" x="193" y="36" text-anchor="middle">切分</text>
  <text class="k-label-accent" x="269" y="36" text-anchor="middle">平行語料</text>
  <text class="k-label" x="269" y="110" text-anchor="middle">兩種模型</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：493,519｜族語與華語、英語之句對總數，已過濾切分｜§3.4, p. 3449
- 數字：26.90｜族語譯華語之最高 BLEU：卡那卡那富語｜表 3, p. 3451
- 範圍：Scheppat 等 2026，臺灣 15 種原住民族語言，微調多語翻譯模型

## Card 5｜典範轉移
- 模式：新論文
- 標題：語料與模型公開，方言仍待細分
- 里程碑：2026｜公開語料、腳本、分詞器與模型｜本篇 §1, p. 3446
- 里程碑：2026｜只試兩種架構，也未使用方言資訊｜本篇 §7, p. 3453
- 里程碑：2026｜擬以全部語料繼續預訓練，借助親屬語｜本篇 §6, p. 3453
- 註記：以上皆出自本篇，尚無後續研究

## Card 6｜Kairos
- 結語：語料連同整理規則與腳本一起公開，來源增加時，語料也能跟著重建。
- 轉變：一次釋出→可再重建
