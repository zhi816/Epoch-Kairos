# 收件：找出原始檔、命名、核對書目、讀原文（S0 至 S2）

本檔規範 SKILL.md 第五節 S0 至 S2：一份原始檔放進 `raw/` 之後，到開始寫證據表之前要做的事。

## 一、找出要收錄的原始檔

```bash
python .agents/skills/paper-pipeline/scripts/pipeline_status.py --new
```

輸出把 `raw/` 中尚未有論文頁的 PDF（不含檔名有「繁體中文翻譯」之譯本）分成三類：

| 類別 | 意思 | 怎麼做 |
|---|---|---|
| `新檔案` | 沒有論文頁、沒有待辦條目、沒有任何論文頁提到它 | 依本檔第二節起收錄 |
| `已列待辦` | `wiki/todo.md` 某條目提到這份檔案 | 看該條目狀態：`waiting` 不得動工（等使用者）；`open` 可接手，動工前把狀態改為 `doing` 並填「負責」；`doing` 且不是你，不得接手 |
| `已引用` | 某篇論文頁提到這份檔案（多半是奠基論文） | 依本檔第三節判斷要不要另立新頁；不需要就不立 |

`wiki/index.md` 中標 `[planned]` 的條目也是待收錄的論文：原始檔到齊後依本檔收錄，收錄完成時把該條目改寫為連結並改標 `[wiki]`（`concepts-and-index.md` 第三節）。

輸出最後若列出「raw/（Mine-RAW）有未提交之變動」，依本檔第五節處理。

## 二、驗證原始檔

1. **是真的 PDF**：檔頭前 5 個位元組是 `%PDF-`。下載失敗的 HTML 錯誤頁曾被誤存為 `.pdf`（`raw/AGENTS.md` 第二節第 5 條）。不是 PDF 時停止，告知使用者，不得自行刪除或覆寫。
   ```bash
   python -c "import sys; d=open(sys.argv[1],'rb').read(); print(d[:5], d.rstrip()[-5:])" "raw/<檔名>.pdf"
   ```
   應見 `b'%PDF-'` 與 `b'%%EOF'`。
2. **抽得出文字**：依 `paper-pdf-parser` 用 PyMuPDF 抽取（本檔第六節）。抽出來是空白或亂碼時，依 `paper-pdf-parser` 改用 MinerU 或頁面影像，並在交付說明寫明。
3. **是正式版還是預印本**：看首頁與頁首頁尾（期刊名、卷期、DOI、"arXiv:"、"Preprint"、勘誤）。同一篇有預印本與正式版時，以正式版為準；`raw/` 只有預印本時，頁面註明採用版本，數字只取該版本（`wiki-content-audit` 寫作模式第 1 步）。

## 三、這份檔案要不要另立一頁

| 情況 | 處理 |
|---|---|
| 一篇獨立的研究或綜述 | 另立一頁，依本檔第四節起收錄 |
| 某獎項表彰一系列工作，這份是其中一篇，而該獎已有論文頁以另一篇為主軸（例如 `raw/2003-channelrhodopsin2.pdf` 是 `2005-optogenetics` 之奠基論文） | 不另立頁。依 `AGENTS.md` 第七章第 1 節「單篇頁容納多篇工作之原則」，在既有論文頁 `key_papers` 列出它，必要時在證據表增列，並在論文頁「知識網絡與文獻出處」寫明此原始檔路徑；屬於修訂既有頁面，從 S3 做起 |
| 同一篇的不同版本（預印本與正式版、中文譯本） | 不另立頁。以正式版為主；譯本不得當證據 |
| 一份檔案收了好幾篇論文（論文集、合輯） | 停下，問使用者要收哪一篇 |

判斷不了時問使用者，不要自行決定。

## 四、書目、slug 與分類

### 1. 書目

依序找出並寫進收件紀錄：英文原題（照原文大小寫）、作者（依署名順序，不得混入得獎者）、發表年份、期刊或會議全名與卷期頁、DOI。

* **有 DOI**：以 Crossref 核對（`https://api.crossref.org/works/<DOI>`）。論文頁寫好後再以 `python .agents/skills/wiki-content-audit/scripts/crossref_check.py <slug>` 確認一致（S6）。年份以正式出版為準；Crossref 之 `published-print` 與 `published-online` 不同年時，取期刊卷期所屬年份，並在交付說明寫明。
* **沒有 DOI**（學位論文、部分會議、預印本）：以原文封面、書名頁、版權頁或會議論文集首頁為準。學位論文之年份取口試或出版年（照封面），`venue` 寫成「Master's Thesis, Department of ……, National ……University」，並在論文頁正文寫明原文連結或典藏處；`lint_wiki.py` 會對缺 `doi_url` 報 WARN，交付說明寫明「學位論文無 DOI」。
* **arXiv**：`venue` 寫 `arXiv preprint, arXiv:XXXX.XXXXX`，`doi_url` 寫 arXiv 網址；之後有正式版時改用正式版。

### 2. slug 與檔名

* slug 格式：`YYYY-<小寫英文與數字，以連字號分隔>`。`YYYY` 是**實際發表年份**（`paper_year`），不是獲獎年份，也不是 `raw/` 檔名上的年份（兩者不同時，以核對過的發表年份為準，並告知使用者 `raw/` 檔名有誤；不得自行改名）。
* 群星論文：`YYYY-<主題關鍵詞>`，如 `2016-ligo-gravitational-waves`、`2021-alphafold2`。
* 我的關注論文：`YYYY-<主題關鍵詞>-<第一作者姓氏拼音>`，如 `2025-paiwan-bunun-morphology-mt-wu`、`2024-finnish-northern-sami-mt-saleva`。
* 收錄前以 `ls wiki/papers/ | grep <關鍵詞>` 確認沒有同名或同一篇的既有頁面。
* `raw/` 根目錄之原始檔名應為 `YYYY-<slug 主體>.pdf`；`raw/my-focus/` 之下保留使用者取的檔名。檔名不合規則時只告知使用者，不得改名。

### 3. 群星或我的關注

| 原始檔位置 | 類別 | `my_focus` | `focus_role` |
|---|---|---|---|
| `raw/` 根目錄 | 群星 | `false` | 不填 |
| `raw/my-focus/學長姐論文/` | 我的關注 | `true` | `senior-thesis` |
| `raw/my-focus/報告論文題材/` | 我的關注 | `true` | `report` |
| `raw/my-focus/台灣相關論文/` | 我的關注 | `true` | `taiwan-linguistics` |
| `raw/my-focus/英文論文/`（不含 `llm 輔助/`） | 我的關注 | `true` | `international` |
| `raw/my-focus/英文論文/llm 輔助/` | 我的關注 | `true` | `llm-assisted` |

群星論文出現在首頁星圖；我的關注論文出現在我的星系（`#my-constellation`），兩者的封面卡都上卡片牆（分屬群星檔案與我的星系檔案）。`focus_languages` 之寫法見 `paper-page-template.md` 第二節。

### 4. 獎項

有獎項者（諾貝爾獎、引文桂冠獎等）查官方紀錄（如 NobelPrize.org），記下得獎者、頒獎年份與事由原文。得獎者若不是本篇作者，記於 `laureates`，不得混入 `authors`。沒有獎項者，`award_year` 與 `paper_year` 相同，不填 `honor` 與 `laureates`。

## 五、`raw/` 倉庫的提交（Mine-RAW）

`raw/` 是獨立的私有倉庫，主倉庫的提交不會帶到它（`AGENTS.md` 第五章第 1 節）。

1. `pipeline_status.py --new` 最後列出「raw/（Mine-RAW）有未提交之變動」時，逐項確認：是使用者新放入的原始檔（未追蹤之 PDF），還是其他變動。
2. 使用者新放入的原始檔：收錄完成後（S10）在 `raw/` 另行提交，只列這些檔案：
   ```bash
   python .agents/skills/git-sync-guardian/scripts/safe_commit_push.py "chore(raw): add <檔名>" raw --agent "<代理名稱>" -- <相對於 raw/ 之路徑>
   ```
3. 其他變動（既有檔案被改、被刪、被改名）：不是你做的，不得提交或還原，告知使用者。
4. 單檔接近 50 MB 時先問使用者；超過 100 MB 不得提交（GitHub 會拒絕），改以 DOI 連結留存並告知使用者。

## 六、讀原文時要記下的事（S2）

依 `paper-pdf-parser` 抽取全文，輸出放在 scratchpad，**不放進倉庫**。抽取文字只用來搜尋，所有數字、公式與頁碼寫入證據表前，都要回原 PDF（必要時看頁面影像）確認。

讀完要能寫出（S3、S4、S7 都會用到）：

1. **四句**：做了什麼、怎麼做、證據是什麼、限制是什麼，各附頁碼。
2. **主要結果**：表號、圖號，以及每個準備引用的數字所在之列與欄（語言方向、資料集、指標、基線、條件）。
3. **公式**：原文的編號公式與所在頁；哪一條是本篇機制的核心公式；只有評估指標公式或完全沒有公式時，記下怎麼確認的（全文搜尋「(1)」、「Eq」、「=」）。
4. **公開資源**：程式、資料、模型之網址（常在摘要末、§1 貢獻清單、註腳、Data Availability）。
5. **作者明列之限制與未來工作**（常在 Limitations、Conclusion、Future Work、Ethics）。
6. **作者所述之歷史背景**：前人做法與其問題（論文頁 Card 2 的素材），附頁碼。
7. **後續研究線索**：較早的論文（發表超過兩年）要找引用本篇的後續研究，至少 3 筆附 DOI（`wiki-content-audit` 寫作模式第 3 步）；可用 Crossref、OpenAlex、Semantic Scholar 查引用，或查同實驗室後續學位論文。搜尋引擎出現機器人驗證時不得繞過，改用其他來源。
