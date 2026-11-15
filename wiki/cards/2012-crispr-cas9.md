# 卡片文字：2012-crispr-cas9

- **論文頁**：[2012-crispr-cas9](../papers/2012-crispr-cas9.md)
- **證據表**：[2012-crispr-cas9](../evidence/2012-crispr-cas9.md)
- **撰寫者**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-15
- **最後核對**：Antigravity by Google DeepMind（Gemini 4 Hydrogen），2026-11-15

## 封面
- 封面斷行：把細菌免疫蛋白，／變成能指定位置的／基因剪刀
- 導語：將雙 RNA 融合成單鏈嵌合體，只需更換導向序列，即可精準剪斷鄰近特定辨識基序的雙股 DNA。

## Card 2｜世紀瓶頸
- 標題：每換一個基因位點，就得重造蛋白
- 對照：鋅指核酸酶｜靠蛋白質結構域辨識鹼基，每次換靶點都得重製蛋白
- 對照：細菌基因組｜雖知免疫系統靠雙 RNA 運作，最小充要組件與分工未明
- 缺口：目標序列｜缺乏只改短核酸片段、不重造酵素即可鎖定的通用剪刀
- 結語：基因編輯亟盼與目標序列解耦的通用剪刀。

## Card 3｜突破原理
- 標題：把雙股剪刀的導航濃縮成一條 RNA
- 公式：無
- 無公式理由：原文無公式：全文無編號公式，生化切割機制與突變定位以膠電泳與定序圖呈現（Figs. 1–5）
- 說明：單鏈嵌合引導核酸帶領酵素辨識鄰近基序並解開雙股，分別切斷兩股。
- 圖類型：示意圖
- 圖說：示意：核酸酶與單鏈嵌合導引核酸結合，於鄰近基序上游解開雙股，分別切斷非互補股與互補股造成平末端斷裂。

```svg
<svg viewBox="0 0 300 180" role="img" aria-label="示意：核酸酶與單鏈嵌合導引核酸結合，於鄰近基序上游解開雙股，分別切斷非互補股與互補股造成平末端斷裂。">
  <rect class="k-soft" x="14" y="10" width="272" height="160" rx="10"/>
  <rect class="k-line k-ring" x="14" y="10" width="272" height="160" rx="10"/>
  <text class="k-label" x="30" y="28">核酸酶</text>
  <line class="k-muted k-dash" x1="162" y1="36" x2="162" y2="140"/>
  <path class="k-ink" d="M 24 68 L 72 68 Q 86 52 104 52 L 194 52 Q 210 52 220 68 L 276 68"/>
  <text class="k-label" x="50" y="58" text-anchor="middle">非互補股</text>
  <rect class="k-ink k-ring" x="86" y="74" width="110" height="22" rx="4"/>
  <text class="k-label-accent" x="141" y="89" text-anchor="middle">導向序列</text>
  <line class="k-accent" x1="196" y1="85" x2="218" y2="85"/>
  <rect class="k-soft" x="218" y="74" width="54" height="22" rx="11"/>
  <rect class="k-line k-ring" x="218" y="74" width="54" height="22" rx="11"/>
  <path class="k-ink" d="M 24 122 L 72 122 Q 86 136 104 136 L 194 136 Q 210 136 220 122 L 276 122"/>
  <text class="k-label" x="50" y="142" text-anchor="middle">互補股</text>
  <rect class="k-soft" x="218" y="102" width="54" height="20" rx="4"/>
  <rect class="k-line k-ring" x="218" y="102" width="54" height="20" rx="4"/>
  <text class="k-label-accent" x="245" y="116" text-anchor="middle">鄰近基序</text>
  <text class="k-label-accent" x="150" y="156" text-anchor="middle">平末端斷裂</text>
</svg>
```

## Card 4｜決定性數據
- 模式：數字
- 數字：3 bp｜質體 DNA 於鄰近基序上游產生平末端斷裂之距離｜p. 3、Fig. 1C–E
- 數字：13 bp｜近鄰近基序種子區高效切割所需連續互補長度下限｜p. 4、Fig. 3E
- 數字：6 處｜遠離鄰近基序前端最多可容忍之連續錯配數｜pp. 4–5、Fig. 3E
- 數字：5/5｜針對綠色螢光蛋白五條嵌合核酸測試全數切割｜p. 6、Fig. 5D
- 範圍：Jinek 等 2012，純化蛋白體外切割與細菌質體維持試驗

## Card 5｜典範轉移
- 標題：從細菌免疫走進人類細胞與醫療
- 里程碑：2013｜Cong 與 Mali 在人類與小鼠細胞實現編輯｜Cong et al. 2013; Mali et al. 2013, Science
- 里程碑：2016｜Komor 以單股切口酶融合脫氨酶開創單鹼基編輯｜Komor et al. 2016, Nature 533:420-424
- 里程碑：2019｜Anzalone 等發展先導編輯實現精準序列寫入｜Anzalone et al. 2019, Nature 576:149-157
- 里程碑：2020｜Charpentier 與 Doudna 獲諾貝爾化學獎｜獎項
- 註記：前三項為後續他人成果，出處見長文

## Card 6｜Kairos
- 結語：當核酸酶成為通用硬體、短引導序列化為軟體，改寫基因不再需要針對每個位點重製蛋白。
- 轉變：重造辨識蛋白→更換導向序列
