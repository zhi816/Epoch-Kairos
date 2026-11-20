# 待辦清單（Todo）

> 本檔登記尚未完成之工作：交接事項、做到一半的任務、須等使用者確認才能動工的工作。格式與規則見 [AGENTS.md](../AGENTS.md) 第七章第 5 節，接手順序見第六章第 4 節。標題四段依序為：編號、狀態（`open` / `waiting` / `doing`）、範圍（`wiki` / `web` / `raw` / `rule` / `skill`）、標題。完成或放棄之條目直接刪除，並於當次日誌條目寫明編號；新增前以 `stage_todo.py --next-id` 取號。
>
> 不收：Wiki 內容與原文不符之處（登記於 [issues.md](issues.md)）、美術方向之選擇題（登記於 [DESIGN.md](../DESIGN.md) 第八章）。

### TD-003 | waiting | raw | 取得光遺傳學頁奠基論文 Nagel et al. (2002) 原始 PDF
- **內容**：[2005-optogenetics](papers/2005-optogenetics.md) 之 `key_papers` 列有 Nagel et al. (2002) *Science* 296:2395-2398（https://doi.org/10.1126/science.1072068），`raw/` 尚無原始檔（Nagel et al. (2003) *PNAS* 已存為 `raw/2003-channelrhodopsin2.pdf`）。依第五章，AI 不得擅自寫入 `raw/`。
- **完成條件**：原始 PDF 置於 `raw/` 並推送至 Mine-RAW。
- **等待**：使用者自行放入 PDF，或明確指示下載。
- **來源**：wiki/log.md [2026-11-08 21:37] git「仍待補」與 index.md 原「待辦與已知問題」一節；2026-11-09 登記，Claude Code by Anthropic。

### TD-004 | waiting | wiki | 補填日誌條目之「模型版本」欄
- **內容**：下列日誌條目之「模型版本」欄為佔位文字「本次工作階段之平台政策禁止將模型型號寫入版控檔案，請使用者自行補填」，不符第九章須載明模型版本之規定：[2026-11-06 22:12] rule、[2026-11-07 22:47] 四筆（rule、fix、update、audit）、[2026-11-08 14:14] git。2026-11-10 TD-014 試跑之工作階段同樣受平台規範限制，[2026-11-10 12:23] ingest、[2026-11-10 12:25] fix 與 [2026-11-10 12:33] rule 三筆之「模型版本」欄、`wiki/evidence/1985-macroscopic-quantum-tunneling.md` 之「查核者」與 `wiki/cards/1985-macroscopic-quantum-tunneling.md` 之「撰寫者」「最後核對」皆以佔位文字代替型號（型號已於對話中告知使用者）。
- **完成條件**：依使用者決定補填或註記完畢；若決定維持原樣，經同意後刪除本條。
- **等待**：（2026-11-14 補記：[2026-11-14 22:07] ingest 一筆之總指揮「模型版本」欄同樣以佔位文字代替，型號已於對話中告知使用者。）使用者提供當時之模型型號，並決定直接補入原條目（屬修改舊條目，須使用者明示同意）、另追加更正條目，或維持原樣。
- **來源**：wiki/log.md [2026-11-07 22:47] audit「待使用者處理」第 1 項；2026-11-09 登記，Claude Code by Anthropic。

### TD-007 | waiting | wiki | 建立證據表「類型」欄白名單並清點違規列
- **內容**：`wiki/evidence/` 各表之「類型」欄目前混用組合值與白名單外描述，例如 [1992-creative-destruction-aghion.md](evidence/1992-creative-destruction-aghion.md) 之「本篇研究結果 / 官方事實」、[2001-colonial-origins-acemoglu.md](evidence/2001-colonial-origins-acemoglu.md) 之「本篇研究結果 / 作者解釋」與「後續研究 / 政策推論」，不符 AGENTS.md 第七章第 4 節所定五類（本篇研究結果、後續研究、作者解釋、依原文數據計算、Wiki 詮釋）。應先全庫清點所有不合規列並列出清單與建議類型，再決定處置方式；每一列須回原文判斷主張歸屬，不得機械拆解組合值或批次改寫。
- **完成條件**：清單列畢且經使用者確認處置方式（逐列修正，或於 AGENTS.md 明訂組合值之使用規則），必要時 `lint_wiki.py` 增列檢查；未經確認前不動任何證據表。另須處理 5 份缺「類型」欄之證據表（49 列）：補上欄位並逐列歸類，或經使用者同意另案處理；133 列之逐列清單與建議須以檔案存入專案，不得只留在對話中。
- **等待**：使用者確認處置方案（方案 A：全庫嚴格統一五類；方案 B：雙軌白名單，概念頁增設專用白名單；方案 C：有限複合值）。
- **進度**：2026-11-10 完成 50 份證據表清點（Antigravity by Google DeepMind）：45 份有「類型」欄，共 792 列，標準列 659 列、非標準列 133 列（論文頁 23 檔 93 列、概念頁 8 檔 40 列，共 71 種非標準標籤/變形）；四大成因：斜線複合值（31 列）、括號修飾（8 列）、論文細分標籤（54 列，如「本篇研究方法」20 列、「本篇研究基本資訊」6 列）與概念頁自立標籤（40 列，如「奠基論文成果」9 列）。已完成 133 列之逐列建議歸屬分析，惟報告尚未存入專案，目前只有本條摘要。2026-11-10 補核（DeepSeek Harness，deepseek-flash）：另發現 5 份證據表完全沒有「類型」欄，共 49 列，未計入上述 133 列：`2023-drugclip`（9 列）、`2024-alphafold3`（15 列）、`2024-sora-world-simulator`（14 列）、`2025-nerve-mito-cancer`（7 列）與概念頁 `generative-world-models`（4 列）。故全庫實際為 841 列（792 + 49）；「50 份」僅為檔案數，列數清點只覆蓋 45 份；5 份缺欄表中 4 份為論文頁、1 份為概念頁，概念證據表實際有 9 份。清點當時另有 3 個頁面完全沒有證據表：`2005-optogenetics`、概念頁 `low-resource-machine-translation`、`macroscopic-quantum-circuits`（不屬本條類型欄範圍，惟影響全庫完整性）。2026-11-11 處理 EK-219 與 EK-220 時，`2005-optogenetics` 已建立僅涵蓋 Card 3 指定項目的部分證據表；其餘主張仍待逐項核實。
- **來源**：使用者指示（2026-11-09 交接，承接 EK-090 之證據表類型觀察）；2026-11-09 登記，DeepSeek Harness（DeepSeek-V4.1-Flash）。2026-11-10 使用者要求核對本條清點是否有漏，補核與缺欄清單由 DeepSeek Harness（deepseek-flash）執行。

### TD-019 | waiting | wiki | 決定已公開論文頁正文中之 raw/ 原始檔路徑是否改寫
- **內容**：GitHub Pages 已上線（2026-11-10），下列 6 篇論文頁之正文或資訊欄以文字寫有私有倉庫之原始檔路徑（如 `raw/2025-deepseek-r1.pdf`），公開網頁上讀者看得到檔名但無法開啟：`2025-deepseek-r1`、`2007-woodford-globalization-monetary-control`、`2023-jwst-massive-galaxies`、`2024-fault-tolerant-quantum`（2 處）、`2024-alphafold3`、`2024-sora-world-simulator`。路徑多為說明「本頁採用哪一版本」（正式版、arXiv 版、補充資料），改寫時須保留版本資訊，改以 DOI 或 arXiv 版號表述。論文頁「知識網絡與文獻出處」之「原始檔典藏」一行為 `paper-pipeline` S1 所需，是否同樣出現在網頁上須一併確認。
- **完成條件**：使用者決定保留或改寫；改寫者依 `wiki-content-audit` 修改論文頁，重建論文頁並推送，網頁正文不再出現 `raw/`。
- **等待**：使用者決定是否改寫。
- **來源**：TD-005 部署前檢查發現（2026-11-10），TD-005 完成時轉登記；2026-11-10 登記，Claude Code by Anthropic。

### TD-020 | open | wiki | 補齊多得獎者代表性奠基論文（首篇：Robert E. Hall 2005 勞動工資微觀基礎）
- **內容**：使用者指示（2026-11-10）：凡重大榮譽（如諾貝爾獎）由多位學者共享、且各做出獨立奠基突破者，知識庫應分別獨立收錄每位得獎者之代表性論文，不應僅收錄單方論文而將另一位標註為非本篇作者。優先推進項目為 2026 諾貝爾經濟學獎共同得主 Robert E. Hall：收錄其勞動市場均衡與工資僵固性奠基論文 *Employment Fluctuations with Equilibrium Wage Stickiness*（AER 95(1): 50–65, 2005, DOI: 10.1257/0002828053828482，規劃 slug `2005-hall-wage-stickiness`），與現有之 Woodford 2007 共同掛鉤於概念頁 `institutions-and-macro-dynamics`。原始 PDF 已於 2026-11-10 取得（Stanford 官方典藏 AER 正式版，429KB，存為 `raw/2005-hall-wage-stickiness.pdf` 並推入 Mine-RAW）。其餘待補多得主項目列入後續儲備：Geoffrey Hinton（1986 Nature 反向傳播 / 1985 玻爾茲曼機，2024 物理獎）、David Baker（2003 Science Top7，2024 化學獎）、Nagel & Hegemann（2003 PNAS 光敏感通道蛋白，2026 生理醫學獎，原始檔已在 `raw/2003-channelrhodopsin2.pdf`）、Henri B. Kagan（不對稱氫化，2026 化學獎）。
- **完成條件**：依 `paper-pipeline` 完成 S0 至 S10 收錄上架（Crossref 核驗、證據表、論文頁、概念頁更新、卡片、論文頁網頁與首頁星圖/卡片牆）；`wiki/index.md` 與概念頁完成雙星關聯。
- **來源**：使用者指示（2026-11-10，因 Woodford 2007 標註「Hall 並非本篇作者」引發討論，確立多得主各自收錄代表作原則）；2026-11-10 登記，Antigravity by Google DeepMind。

### TD-021 | open | web | 補驗受影響論文頁與首頁卡片牆
- **內容**：2026-11-10 複核問題清單後，`1982-hopfield-network`、`2017-attention-is-all-you-need`、`2021-alphafold2`、`2021-seediq-chinese-mt-you`、`2025-indigenous-tek-ai-revitalization-wang` 因核實狀態改為 `issues` 而重建，原先均只移除核實完成標記。後續 `1982-hopfield-network` 釐清突觸失效分析，`2017-attention-is-all-you-need` 更正英譯法數字及版本，`2021-alphafold2` 修正公式與後續研究歸屬，`2021-seediq-chinese-mt-you` 修正論文頁及卡片公式，`2025-fragment-shot-reasoning-mt-frontull` 補充模型參數來源差異，均再次重建；`2019-generalized-data-augmentation-xia` 修正證據表公式後重建，網頁產出未變；`2007-woodford-globalization-monetary-control` 修正封面限定語後重建論文頁與首頁；`2024-sora-world-simulator` 移除未公開的公式並重建論文頁。各篇建置自我檢查均為 ERROR 0、WARN 0。瀏覽器服務不可用，尚未完成論文頁與首頁卡片牆驗證。
- **進度**：2026-11-10 處理 TD-011，另重建 `1992-creative-destruction-aghion`（EK-203，核實狀態改為 issues）、`2001-colonial-origins-acemoglu`、`2013-icecube-neutrino`、`2024-alphafold3`、`2024-formosan-mt-bilingual-lexicon-zheng`、`2025-formosanbench-llm-benchmark-lin`、`2025-manchu-in-context-mt-pei`；`1982-hopfield-network` 與 `2017-attention-is-all-you-need` 修正公式與卡片後再次重建。建置自我檢查皆為 ERROR 0、WARN 0。冰立方、Hopfield、Transformer 與 AlphaFold 3 卡片牆已重建且檢查一致；瀏覽器連線服務仍不可用，桌面、手機與卡片牆目視驗證均待補。
- **進度**：2026-11-11 複查日誌發現 `1995-soai-asymmetric-autocatalysis` 於 10:28 驗證後曾再修改並重建；同日後續修正 Card 2、3、5、6 與長文後再次建置。瀏覽器服務無法連線，該篇現行論文頁與首頁卡片牆均待桌面及手機版複驗。Woodford 舊網址轉介亦待以瀏覽器確認。2026-11-13 處理 EK-203 後重建 `1992-creative-destruction-aghion`（Card 3 公式與 `verification: "verified"`），本機 Chrome DevTools 未啟用（`DevToolsActivePort` 不存在），該篇論文頁與卡片牆瀏覽器驗證仍留待本條補驗。
- **進度**：2026-11-14，Codex by OpenAI（GPT-6）完成 `1992-creative-destruction-aghion` 最新版檢查：Chrome `verify_page.js` 結果 PASS（1440 x 900、375 x 812，WARN 0），`verify_wall.js` 結果 PASS（六組尺寸／模式，指定卡片僅一張），全牆 WARN 27（其他卡片的論文名、年份或標籤截斷）；目視檢查論文頁 Card 1–6 與返回群星連結，確認 Aghion 卡出現在群星檔案。自動驗證涵蓋手機尺寸，手機捲動後卡片選取狀態仍須人工補驗；本條其餘待驗論文尚未完成。
- **完成條件**：在可使用的瀏覽器環境中，依 `paper-card-writer` 流程檢查上述論文頁之桌面與手機版，以及各篇首頁卡片牆；確認先前的核實完成標記及版面正確，記錄驗證結果並處理所見問題。`2025-indigenous-tek-ai-revitalization-wang` 另於 EK-192 修正後重建，亦須複驗。
- **來源**：2026-11-10 問題清單分組複核整合，Codex by OpenAI。

### TD-023 | waiting | raw | 改名 raw 檔以對應 2007 Woodford 論文之新 slug
- **內容**：2007 Woodford 論文之 slug 已於提交 a83a66e 改為 `2007-woodford-globalization-monetary-control`，對應英文原題 *Globalization and Monetary Control*。raw 檔仍為 `raw/2007-woodford-inflation-dynamics.pdf`，`paper-pipeline` S1 依 slug 對應 raw 檔名。依 AGENTS.md 第五章，raw 檔名由使用者親自更名，AI 不得改動。更名後需同步更新論文頁「原始檔典藏」行、`wiki/index.md` 原始文獻行，以及 `wiki/issues.md` 內指向舊 raw 檔名之連結。
- **完成條件**：`raw/` 內存在新檔名之 PDF（或使用者決定之檔名）；`pipeline_status.py 2007-woodford-globalization-monetary-control` 之 S1 指向新檔名且 OK；`lint_wiki.py` 無 ERROR。
- **等待**：使用者親自更名 `raw/2007-woodford-inflation-dynamics.pdf`。
- **來源**：wiki/log.md [2026-11-11 12:27] fix（slug 改名）；2026-11-11 登記，Claude Code by Anthropic。

### TD-033 | open | wiki | 其餘 27 篇我的關注論文改寫為新六章
- **內容**：2026-11-20 起我的關注論文改用新六章（`paper-card-writer` 之 `references/focus/`），F.07 `2026-hybrid-dictionary-rag-llm-paiwan-wang` 已完成並作為範例。其餘各篇之論文頁（六段標題、刪開頭引言、舊 Card 6 個人研究映射移至「延伸想法」）、證據表「位置」欄與卡片檔須逐篇改寫，再建置論文頁並驗證。依 `paper-card-writer` 第七節一篇一個提交、一筆日誌。待改：`2019-generalized-data-augmentation-xia`、`2021-seediq-chinese-mt-you`、`2022-formosan-say-verbs-hsieh`、`2023-atayal-truku-morphology-dai`、`2023-atayalic-multilingual-mt-liao`、`2023-low-resource-nmt-survey-ranathunga`、`2024-finnish-northern-sami-mt-saleva`、`2024-formosan-mt-bilingual-lexicon-zheng`、`2024-formosan-temporal-words-lim`、`2024-taiwanese-mt-resegmentation-tang`、`2025-atayalic-affix-mt-jin`、`2025-atayalic-oov-enumeration-yang`、`2025-formosanbench-llm-benchmark-lin`、`2025-fragment-shot-reasoning-mt-frontull`、`2025-indigenous-tek-ai-revitalization-wang`、`2025-manchu-in-context-mt-pei`、`2025-paiwan-bunun-morphology-mt-wu`、`2025-tulun-adaptable-lrl-mt-merx`、`2026-context-volume-rag-domain-shift-setiawan`、`2026-cross-lingual-alignment-moe-routers-bandarkar`、`2026-data-centric-continual-pretraining-ji`、`2026-data-centric-russian-kyrgyz-mt-novokshanov`、`2026-epark-formosan-dialectometry-gagnier`、`2026-formosanmt-parallel-corpus-scheppat`、`2026-malm-backtranslation-indic-mt-rao`、`2026-tao-filipino-nmt-macayan`、`2026-tokenizations-austronesian-lms-lumbantobing`。
- **完成條件**：`check_cards.py` 不再出現「我的關注論文尚未改用新六章」WARN；各篇 `verify_page.js` PASS。
- **來源**：使用者指示（2026-11-20）；登記：Claude Code by Anthropic。
