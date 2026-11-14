# 多領域 Print CSS、KaTeX 公式與原圖回嵌配方（Layout Recipes）

> **適用前提**：本檔為工程配方庫，不得當成單一萬用模板盲目套用（見 `SKILL.md` 〈版面保真〉與吸引子「版型」警語）。每次翻譯新論文前，須先執行 `scripts/measure_pdf.py` 量測原 PDF 的實際紙張尺寸、邊距、欄數與字級，再依原稿風格組合以下模組。

---

## 一、產檔總架構（HTML + Print CSS + 瀏覽器列印）

採用 **HTML5 + CSS `@page` + KaTeX + 本機 Chrome/Edge `--headless=new --print-to-pdf`** 作為跨領域通用產檔管線，最後統一由 `scripts/html_to_pdf.py` 自動偵測可用瀏覽器並編譯驗證。

```bash
# 1. 量測原論文規格並輸出對照圖
python .agents/skills/academic-paper-translator/scripts/measure_pdf.py raw/<檔名>.pdf --render-dir work/<slug>/orig_pages --dpi 180

# 2. 由同一份 HTML 產出雙版本 PDF（不寫死瀏覽器路徑）
python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/<slug>/translated.html <目標輸出路徑>_原版翻譯.pdf
python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/<slug>/translated.html <目標輸出路徑>_單欄翻譯.pdf --mode mobile

# 3. 轉出譯本逐頁 PNG 做兩階段視覺核對
python .agents/skills/academic-paper-translator/scripts/measure_pdf.py <目標輸出路徑>.pdf --render-dir work/<slug>/out_pages --dpi 180
```

---

## 二、`@page` 紙張規格、邊距與頁碼／頁眉配方

依 `measure_pdf.py` 回報之 `paper` 與 `estimated_margins_mm` 挑選對應 `@page`：

### 1. 常見紙張尺寸與邊距基準
* **ACL / EMNLP / WMT / 中文會議與學位論文（A4）**：
  ```css
  @page {
      size: A4 portrait;
      margin: 22mm 19mm 24mm 19mm; /* 依 measure_pdf.py 實測值微調 */
      @bottom-center {
          content: counter(page);
          font-family: "Times New Roman", "Noto Serif TC", serif;
          font-size: 9.5pt;
          color: #111;
      }
  }
  @page :first {
      @bottom-center { content: none; } /* 原稿首頁若無頁碼時隱藏 */
  }
  ```
* **NeurIPS / ICLR / ICML / IEEE（US Letter）**：
  ```css
  @page {
      size: letter portrait;
      margin: 25.4mm 25.4mm 25.4mm 25.4mm; /* NeurIPS 單欄常見 1 吋邊距 */
      /* 雙欄 IEEE 可改為 19mm 16mm 24mm 16mm */
  }
  ```

### 2. 頁眉左右資訊（期刊名／短標題／作者名）
若原稿每頁上方帶有欄標題或期刊卷期：
```css
@page {
    @top-left {
        content: "短標題或作者（沿用原稿風格）";
        font-family: "Times New Roman", "Noto Serif TC", serif;
        font-size: 8pt;
        color: #444;
    }
    @top-right {
        content: "Proceedings / Journal Vol(Issue), Year";
        font-family: "Times New Roman", "Noto Serif TC", serif;
        font-size: 8pt;
        color: #444;
    }
}
@page :first {
    @top-left { content: none; }
    @top-right { content: none; }
}
```

---

## 三、單欄、雙欄與跨欄混排控制

```css
/* 單欄（NeurIPS / ICLR / 中文碩論 / 物理與生醫單欄預印本） */
.one-col {
    max-width: 100%;
    text-align: justify;
}

/* 雙欄（ACL / IEEE / 雙欄期刊） */
.two-col {
    column-count: 2;
    column-gap: 6.5mm;
    column-fill: balance;
    text-align: justify;
}

/* 續接頁面時避免強行平衡留白（最末頁 References 除外） */
.two-col-auto {
    column-count: 2;
    column-gap: 6.5mm;
    column-fill: auto;
    text-align: justify;
}

/* 跨兩欄之寬表格、滿版圖與全寬標題區 */
.span-all {
    column-span: all;
    margin: 8pt 0;
    break-inside: avoid;
    page-break-inside: avoid;
}

/* 排版斷頁防護 */
h1, h2, h3, .sec, .subsec {
    break-after: avoid;
    page-break-after: avoid;
}
.table-wrap, figure, .footnote-box, .algo-box {
    break-inside: avoid;
    page-break-inside: avoid;
}
.page-break {
    break-before: page;
    page-break-before: always;
}
```

---

## 四、多元表格風格配方（依原稿選擇，嚴禁一律套三線表）

* **風格 A：LaTeX 三線表（ACL / NeurIPS / ICML / 物化主流）**
  ```css
  table.booktabs {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.5pt;
      line-height: 1.3;
      border-top: 1.2pt solid #000;
      border-bottom: 1.2pt solid #000;
  }
  table.booktabs th {
      font-weight: 700;
      padding: 4pt;
      border-bottom: 0.75pt solid #000;
      vertical-align: bottom;
  }
  table.booktabs td { padding: 3pt 4pt; vertical-align: top; }
  table.booktabs tr.midrule td { border-top: 0.6pt solid #000; }
  ```
* **風格 B：全網格框線表（IEEE 部分會議 / 工程標準 / 台灣碩博士論文）**
  ```css
  table.grid {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.5pt;
      line-height: 1.3;
  }
  table.grid th, table.grid td {
      border: 0.5pt solid #222;
      padding: 3.5pt 4.5pt;
      vertical-align: middle;
  }
  table.grid thead th {
      background: #f2f2f2;
      font-weight: 700;
  }
  ```
* **風格 C：淡灰底＋行分隔表（Nature / 生醫 / BioNLP 期刊常見）**
  ```css
  table.minimal-band {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.4pt;
      border-top: 1pt solid #333;
      border-bottom: 1pt solid #333;
  }
  table.minimal-band thead th {
      background: #f3f4f6;
      border-bottom: 0.75pt solid #666;
      padding: 4pt;
  }
  table.minimal-band tbody tr:nth-child(even) { background: #fafafa; }
  table.minimal-band td {
      padding: 3.5pt 4pt;
      border-bottom: 0.4pt solid #e5e7eb;
  }
  ```
* **數值對齊共用類**：`.al-l { text-align: left; }`, `.al-r { text-align: right; font-variant-numeric: tabular-nums; }`, `.al-c { text-align: center; }`。

---

## 五、多語混排與字體堆疊配方（解決缺字、偏移與網址破版）

1. **拉丁重音符號優先規則**：
   將英文標準襯線字體放在中文襯線字體**之前**，避免 `Popović`、`Costa-Jussà`、`Sälevä`、`Łódź`、`Müller` 等組合變音符號被中文字型的 fallback 渲染成偏移或分離重音：
   ```css
   body {
       font-family: "Times New Roman", "Noto Serif", "Noto Serif TC", "PMingLiU",
                    "Nirmala Text", "Nirmala UI", serif;
       font-size: 9.5pt;
       line-height: 1.48;
   }
   ```
   > 單純無襯線風格論文（如 Nature／ICLR 部分版型）改用 `"Helvetica Neue", "Liberation Sans", "Noto Sans", "Noto Sans TC", "Microsoft JhengHei", sans-serif`。

2. **特殊語言書寫系統 Fallback**：
   ```css
   .deva { font-family: "Nirmala Text", "Nirmala UI", "Noto Sans Devanagari", sans-serif; }
   .ipa  { font-family: "Gentium Plus", "Segoe UI", "DejaVu Sans", sans-serif; }
   .arab { font-family: "Segoe UI", "Noto Naskh Arabic", serif; direction: rtl; unicode-bidi: isolate; }
   .cjk-jp { font-family: "Noto Serif JP", "MS Mincho", "Noto Serif TC", serif; }
   ```

3. **網址、DOI 與腳註防切字**：
   嚴禁在腳註中使用 `word-break: break-all`（會把網址從單字正中間截斷）；改用：
   ```css
   .footnote-box p, .url-wrap {
       overflow-wrap: anywhere;
       word-break: normal;
   }
   ```

---

## 六、KaTeX 向量數學公式整合標準

凡原文含數學公式、矩陣、物理定律或化學方程式，**嚴禁裁切或截圖代替排版**（公式內無法翻譯的字形除外，統一用 KaTeX 向量排版維持與內文相同的字級清晰度）。

1. **在 `<head>` 加入 KaTeX 與 Auto-Render**（對齊專案版本 `0.16.11`；若目標環境離線可先備份 `katex/` 至工作目錄並改指相對路徑）：
   ```html
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
   <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
   <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
   ```
2. **頁面底部啟動渲染並搭配 `html_to_pdf.py`**：
   ```html
   <script>
     document.addEventListener("DOMContentLoaded", function () {
       if (typeof renderMathInElement === "function") {
         renderMathInElement(document.body, {
           delimiters: [
             { left: "$$", right: "$$", display: true },
             { left: "$", right: "$", display: false }
           ],
           throwOnError: false
         });
       }
     });
   </script>
   ```
   `html_to_pdf.py` 預設啟動 `--virtual-time-budget=8000`，確保字型下載與 `renderMathInElement` 全數完成後才執行 `--print-to-pdf`。
3. **數學與化學排版硬規則**：
   * **化學元素正體**：離子或分子式須寫 `$\mathrm{Na}^+$`、`$\mathrm{Ca}^{2+}$`，不可寫 `$Na^+$`。
   * **金額轉義**：貨幣金額一律寫為 `\$100` 或「100 美元」，嚴禁裸 `$` 造成行內公式誤判。
   * **編號公式對齊**：多欄長公式使用 `\begin{aligned}...\end{aligned}` 斷行；有右對齊式號時可用雙欄格線或 `\tag{1}`。
   * **列印公式防截斷**：
     ```css
     .katex-display {
         margin: 6pt 0;
         overflow-x: visible; /* Print 時配合縮小字級或 \begin{aligned} 斷行，避免出現水平捲軸 */
         font-size: 0.94em;
     }
     ```

---

## 七、原圖裁切與高解析回嵌工作流

遇到原文包含架構圖、消融折線圖、實驗照片、分子／電路圖時，優先保留原圖而不重繪：

1. **自動偵測與高解析裁切（300 DPI）**：
   ```bash
   # 方法 A：先自動偵測所有非文字繪圖與圖片區塊（輸出 pN_figK.png 與各塊 pt 座標）
   python .agents/skills/academic-paper-translator/scripts/measure_pdf.py raw/<檔名>.pdf --auto-figures work/<slug>/figs --dpi 300

   # 方法 B：從原頁影像與 captions 座標精確手動微調裁切框（page:x0,y0,x1,y1）
   python .agents/skills/academic-paper-translator/scripts/measure_pdf.py raw/<檔名>.pdf --crop 4:52,70,543,295 --out work/<slug>/figs/fig2.png --dpi 300
   ```
   * 用 `--auto-figures` 或 `--crop` 從原 PDF 擷取 `clip` 渲染的好處是：**純向量流程圖／座標軸折線圖會直接以 300 DPI 光柵化輸出，曲線、文字與標註皆極度銳利，不會像舊式抽圖只抓到底層殘圖或遺失文字層標籤**。
2. **嵌回譯文 HTML 與雙語圖說處理**：
   ```html
   <figure class="fig-wrap span-all"> <!-- 單欄圖移除 span-all 即可 -->
       <img src="figs/fig2.png" alt="Figure 2" style="width:100%; max-width:100%; height:auto; display:block; margin:0 auto;">
       <figcaption class="fig-caption">
           <strong>圖 2：</strong>模型整體架構與雙階段微調流程。（圖內原文標註保留，核心詞彙說明詳見正文）
       </figcaption>
   </figure>
   ```
   * **圖內文字原則（遵守 `SKILL.md` 第 20 條）**：預設維持原圖影像不任意塗改重繪，把重點術語對照寫進下方繁體中文 `<figcaption>` 或正文即可；若使用者明確要求改寫圖內英文標籤，只可在逐項核對座標與數值無誤後疊加覆蓋層，並於交付說明中明確列出改動之圖號與項目。

---

## 八、雙版本輸出：手機單欄大字 CSS 配方（`_單欄翻譯`）

為兼顧「紙本列印／原稿左右對照（`_原版翻譯.pdf`）」與「手機直螢幕無縮放閱讀（`_單欄翻譯.pdf`）」，同一份已核對完畢的 `translated.html` 可直接以 `--mode mobile` 編譯第二份單欄 PDF，免除重翻與雙份內容分歧：

```bash
python .agents/skills/academic-paper-translator/scripts/html_to_pdf.py work/<slug>/translated.html <目標輸出路徑>_單欄翻譯.pdf --mode mobile
```

### 核心覆寫原則（已內建於 `html_to_pdf.py` 之 `MOBILE_OVERRIDE_CSS`）
1. **強制單欄與連續流式排版**：將 `.two-col`、`.two-col-auto` 設為 `column-count: 1 !important`，移除 `.span-all` / `.col-span-all` 跨欄設定，並將原稿對齊分頁用的 `.page-break` 設為 `display: none !important`，避免單欄出現半頁留白。
2. **手機可讀性字級與邊距**：改為 `@page { size: A4 portrait; margin: 12mm 14mm 15mm 14mm; }`，內文放大至 `13.5pt`、`line-height: 1.65`（手機直向每行約 32–36 中文字，無需兩指縮放），標題與參考文獻等比放大。
3. **寬表格與原圖保護**：`table.acl` 等表格採 `width: 100%` 與 `10pt` 字級配合 `break-inside: avoid` 與 `thead { display: table-header-group }`，讓原雙欄寬表在 A4 單欄幅寬中維持清晰不擠壓且不輕易拆斷；`figure.fig-wrap img` 放大至單欄滿寬展示。
4. **首頁出處欄轉分隔帶**：原位於第 1 頁底部的 `.venue-footer` 改為上下細線分隔之置中資訊帶，在連續單欄閱讀時自然區隔首頁註腳與後續章節；若特定論文仍需微調單欄字級或表格行距，可另傳入 `--css custom_mobile.css` 疊加覆寫。
