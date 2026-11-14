# 卡片文字：2026-malm-backtranslation-indic-mt-rao

- **論文頁**：[2026-malm-backtranslation-indic-mt-rao](../papers/2026-malm-backtranslation-indic-mt-rao.md)
- **證據表**：[2026-malm-backtranslation-indic-mt-rao](../evidence/2026-malm-backtranslation-indic-mt-rao.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14
- **最後核對**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-14

## 封面

- 封面斷行：用詞幹比對／過濾回譯句對／提升印度低資源翻譯
- 導語：只用官方平行語料歸納雙語詞表，再藉借詞擴充與詞幹子字串比對篩掉雜訊回譯，讓那加梅斯語與博多語奪下比賽第一。
- 封面標題：構詞詞彙過濾低資源回譯

## Card 2｜世紀瓶頸

- 標題：沒品質評估工具時回譯怎麼篩
- 對照：品質評估｜現有 LaBSE 與 CometKiwi 模型在四種目標語中僅覆蓋阿薩姆語
- 對照：語言識別｜只驗語言與長度比例能抓格式異常，卻看不出譯文語意是否漂移
- 對照：字面比對｜那加梅斯語詞表缺借詞，博多語黏著詞綴變形更常被誤判成零分
- 缺口：構詞感知｜缺不靠外部評估器、僅憑平行語料就能辨識詞根與借詞的過濾法
- 結語：需要兼顧詞幹變化與借詞的輕量濾網。

## Card 3｜突破原理

- 標題：以詞幹與借詞擴充過濾回譯合成句
- 公式：無
- 無公式理由：原文無公式：全篇僅以文字敘述構詞過濾流程、信心門檻 k 與訓練設定，無編號數學公式。
- 說明：由平行語料執行詞彙歸納並擴充借詞，再以詞幹比對過濾單語回譯後進行兩階段訓練。
- 圖類型：示意圖
- 圖說：示意：由官方平行語料歸納詞表，對單語回譯進行詞幹比對後進入兩階段訓練與官方盲測。

```svg
<svg viewBox="0 0 300 132" role="img" aria-label="示意：由官方平行語料歸納詞表，對單語回譯進行詞幹比對後進入兩階段訓練與官方盲測。">
  <rect class="k-ink k-ring" x="8" y="10" width="66" height="24" rx="4"/>
  <text class="k-label" x="41" y="26" text-anchor="middle">平行語料</text>
  <line class="k-ink" x1="74" y1="22" x2="90" y2="22"/>
  <polyline class="k-ink" points="85,18 90,22 85,26"/>
  <rect class="k-ink k-ring" x="90" y="10" width="66" height="24" rx="4"/>
  <text class="k-label" x="123" y="26" text-anchor="middle">詞彙歸納</text>
  <rect class="k-muted k-ring" x="8" y="68" width="96" height="24" rx="4"/>
  <text class="k-label" x="56" y="84" text-anchor="middle">單語回譯</text>
  <polyline class="k-accent" points="156,22 184,22 184,41"/>
  <polyline class="k-muted" points="104,80 184,80 184,65"/>
  <rect class="k-soft" x="150" y="41" width="68" height="24" rx="4"/>
  <rect class="k-line k-ring" x="150" y="41" width="68" height="24" rx="4"/>
  <text class="k-label-accent" x="184" y="57" text-anchor="middle">詞幹比對</text>
  <line class="k-ink" x1="218" y1="53" x2="230" y2="53"/>
  <polyline class="k-ink" points="225,49 230,53 225,57"/>
  <rect class="k-ink k-ring" x="230" y="41" width="62" height="24" rx="4"/>
  <text class="k-label" x="261" y="57" text-anchor="middle">兩階段訓練</text>
  <polyline class="k-muted k-dash" points="261,65 261,114 162,114"/>
  <rect class="k-muted k-ring" x="74" y="102" width="88" height="24" rx="4"/>
  <text class="k-label" x="118" y="118" text-anchor="middle">官方盲測</text>
</svg>
```

## Card 4｜決定性數據

- 模式：數字
- 數字：54.4%｜六十三萬回譯句對過濾保留比例（344,768 句）｜表 4, p. 2210
- 數字：+8.33｜兩千句對那加梅斯語主系統 BLEU 增益（奪第一）｜§5 p. 2211、表 5
- 數字：16.30｜博多語主系統盲測 BLEU（第 1 名，對比系統 15.64）｜§5 p. 2211、表 5
- 數字：14.09｜五萬四句對阿薩姆語主系統 BLEU（低於對比 15.00）｜表 5, p. 2211
- 範圍：Rao 等 2026 四語盲測；極低資源見效，五萬句以上反微損

## Card 5｜典範轉移

- 模式：新論文
- 標題：從零評估器過濾到資源轉折界線
- 里程碑：2026｜僅列外部單語語料網址，未釋出程式碼與模型權重｜本篇 §3.2 與全文檢查
- 里程碑：2026｜過濾回譯在兩千與一萬五千句對極低資源最有效｜本篇 §5–§6, p. 2211
- 里程碑：2026｜博多語黏著構詞易成偽陰性，待後綴比對與擴詞表｜本篇 §4.2, §6, pp. 2210–2211
- 里程碑：2026｜未與未過濾回譯及 IndicTrans2 回譯直接對照｜本篇 §6, p. 2211
- 註記：以上皆出自本篇論文，尚無後續他人研究。

## Card 6｜Kairos

- 結語：當多語評估器仍缺席時，從平行語料提煉構詞濾網就是極低資源翻譯的破口。
- 轉變：外掛評估模型→自舉詞幹濾網
