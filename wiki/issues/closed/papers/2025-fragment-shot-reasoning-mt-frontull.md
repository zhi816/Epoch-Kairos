# 已結案問題：papers/2025-fragment-shot-reasoning-mt-frontull.md

> 本檔收錄 [wiki/papers/2025-fragment-shot-reasoning-mt-frontull.md](../../../papers/2025-fragment-shot-reasoning-mt-frontull.md) 已結案（`fixed` / `wontfix`）之問題條目，由 `archive_issues.py` 自 [wiki/issues.md](../../../issues.md) 搬入；條目內容原封不動，僅相對連結已換算為本檔位置。本檔只追加，不修改已歸檔條目；同一處再出問題時於 wiki/issues.md 開新編號並加「關聯」行。規則見 AGENTS.md 第七章第 4 節。

### EK-082 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 3 與 Card 4 | 原文不符
- **問題**：（1）Card 3（第 44–53 行）稱依據「句法成分樹（Constituency Tree）」拆解來源句，並檢索包含片段及其「對應目標語譯文子串的最小對齊例句對」。原文 §3（p. 3，圖 1）完全未使用句法成分樹剖析器或子串級目標語對齊，而是以**由 7 個連續詞遞減至 1 個詞之滑動視窗（sliding window）**在檢索庫來源端進行精確子字串匹配，為每個片段隨機抽取至多 6 組完整雙語句對；原文只說片段選取會盡量避免重疊，理想上完整且不冗餘，並未保證零重疊；且 Card 3 漏述 Pivoted Fragment-Shot（§3，pp. 3–4，圖 2）經由義大利語樞紐進行兩階段巢狀片段檢索（排除整句完全重疊）之機制。（2）Card 4（第 83–84 行）兩度將研究對象 **Ladin（拉定語，北義多洛米蒂山區雷托－羅曼語支少數民族語言：Val Badia 與 Gherdëina）**誤寫為「**拉丁語**變體」。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`（§1 p. 1、§3–§4 pp. 3–4 圖 1–2）
- **發現於**：wiki/log.md [2026-11-09 00:55] audit（Antigravity by Google DeepMind）
- **處理**：2026-11-09，Antigravity by Google DeepMind（Gemini 3.8 Flash）。回原文全文核實後重寫：Card 3 刪除虛構之句法成分樹剖析與 argmax 公式，改述原文真實採用之 7 至 1 詞滑動視窗來源端匹配（抽取至多 6 組雙語例句、無重疊覆蓋）以及兩階段樞紐片段提示（PF）機制；Card 4 將研究對象正名為北義多洛米蒂山區雷托－羅曼語支「拉定語（Ladin）」兩大變體（Val Badia 與 Gherdëina），糾正「拉丁語變體」之筆誤；補列 Table 1–3 完整數據、推論耗時與語法有效性局限。建立證據表 wiki/evidence/2025-fragment-shot-reasoning-mt-frontull.md，頁面 verification 改為 verified。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。覆核發現先前處理記錄及證據表把原文「片段選擇會盡量避免重疊，理想上完整且不冗餘」寫成「無重疊覆蓋」，語氣過度絕對。方法本身修正符合原文；須將記錄與證據表改為「盡量避免重疊，力求完整且不冗餘覆蓋」後再關閉，本條重開。
- **處理**：2026-11-09，Codex by OpenAI（GPT-6）。回原文 §3（p. 3）核對，將引言、Card 3、Card 5 與證據表中的「不重疊／無重疊」絕對表述改為「盡量避免重疊，理想上完整且不冗餘」，並註明原文不保證零重疊；同步修正本問題對方法的描述，保留先前處理記錄以供追溯。狀態改為 fixed。

### EK-091 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 5 | 原文未支持
- **問題**：Card 5 第 1 點（第 135 行）寫 Fragment-Shot「顛覆整句 RAG 定式」，並稱「能遠比整句語意檢索更有效」。原文沒有整句語意檢索的對照實驗：表 1 的比較對象只有零樣本（ZS）與隨機例句（RS，隨機選 16 組句對，§3, p. 3），作者並說明因缺乏合適模型，無法以詞嵌入計算語意相似度（§2, p. 3）；與以句子相似度選例之前人作法僅作定性對照（§7, p. 6）。「顛覆」亦屬評價用詞。建議改為「在無法建立可靠語意檢索模型的情況下，以片段覆蓋選例比零樣本與隨機例句有效」。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`（§2 與 §3 Random-Shot 定義，PDF p. 3；表 1 與 §7，PDF p. 6）
- **發現於**：wiki/log.md [2026-11-09 23:33] audit（Claude Code by Anthropic；第一批卡片回填 C 組只讀論文頁時提出，本代理回原文核對）
- **處理**：2026-11-09，Claude Code by Anthropic（Claude Opus 5.5）。Card 5 第 1 點改為「以片段覆蓋取代整句相似度選例」：限定於缺乏可靠語意嵌入模型之情境，比較對象寫明為零樣本與隨機例句（表 1, p. 6），並註明作者未與整句語意檢索直接比較（§2, p. 3）、僅作定性對照（§7, p. 6）；刪除「顛覆」。證據表增列對應主張，頁面 verification 改回 verified。

### EK-172 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 1、Card 2、Card 5 與證據表第 15 列 | 原文未支持
- **問題**：（1）Card 2 第 1、2 點稱整句檢索在小語料中「命中率低、強制檢索出的整句往往只有少數不相關的高頻停用詞重疊」，並稱辭典提示「無法提供屈折變化、黏著語綴、詞序排列與焦點選擇的上下文示範」，原文 §1–§2 沒有這些說法；原文所述困難為大模型對小語言及其變體認識有限、少於 13,000 句對不足以訓練（Gu et al. 2018），以及拉定語沒有合適之語意嵌入模型。（2）Card 1 稱本篇「證明」大模型能以推理補償數據之不足，Card 5 第 2 點以圖 2 單一例子稱推理模型能「自發跨越兩跳完成語素映射，證明推理能部分補償數據匱乏」，且未交代 PF（20.94）仍低於有直接例句時之 FS（28.60）；原文摘要與結論之措辭為「更善用檢索知識」「讓模型超越例句而泛化」。（3）Card 5 漏記原文公開之程式碼、檢索語料與 PyPI 套件、Limitations 所列限制與 Future Work。（4）證據表第 15 列只寫「Table 1 之 BLEU 分數」，未逐一列出數值。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`，摘要與 §1（p. 1）、§2（pp. 2–3）、註 1（p. 3）、表 1（p. 6）、Conclusion 與 Future Work（p. 8）、Limitations（p. 9）。
- **發現於**：第三批卡片回填撰寫前抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。回原文核對後：Card 2 依 §1–§2 改寫為大模型對小語言掌握有限、微調資料不足、拉定語無嵌入模型而無從語意檢索；Card 1「證明」改為摘要之發現；Card 5 第 2 點改述 PF 與 ZS、FS 之數值關係並引結論原句；Card 5 補列公開資源、限制與未來工作；證據表逐一列出表 1 四個方向（另含 Gherdëina→Italian GPT-4o 兩格）之數值與信賴區間，補登上述各項。頁面 `verification` 改為 `partial`。

### EK-173 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 4 與 Card 5 第 3 點 | 原文不符
- **問題**：（1）Card 4 實驗設定稱檢索語料為「Gherdëina–Italian（18,485 句）」，原文無此數，原文為 Val Badia–Italian 18,140 句、Gherdëina–Italian 19,971 句，另對齊出 Val Badia–Gherdëina 14,953 句；證據表同列亦誤。（2）稱 BLEU 以「平均值 ± 標準差」報告，原文表 1 標題為平均值與信賴區間。（3）表 3 相關係數加註「p < 0.05」，原文僅以星號標示、未註明顯著水準。（4）「原文指出的局限性」7%–9% 一項寫作「無效拼寫或非標準詞」並標 Limitations p. 9，原文為 §7 p. 7「syntactically not valid in the target language」；Figure 2 一項寫成提示偏移「即」使 GPT-4o 找不到例句，原文為「may have caused」。（5）Card 5 第 3 點稱譯入高資源語言時「複雜提示無效甚至引入干擾」，原文為只有些微改善、FS 僅對 o1-mini 與 Llama-3.3 顯著，部分情形零樣本最好，未提干擾。
- **來源**：`raw/my-focus/英文論文/llm 輔助/Compensating for Data with Reasoning Low-Resource Machine Translation with LLMs.pdf`，§4（pp. 4–5）、§6（p. 5）、表 1 標題與表 2（p. 6）、表 3（p. 7）、§7（p. 7）、Conclusion（p. 8）。
- **發現於**：第三批卡片回填交付稿撰寫時再抽查（Claude Code by Anthropic，2026-11-10）
- **處理**：2026-11-10，Claude Code by Anthropic（Claude Opus 5.5）。以原 PDF 頁面影像核對後，依原文改寫上述五處，表 2 補列 ZS、FS、PF 三種字元數與 DeepSeek-R1 推論秒數；證據表同步更正並逐一列出數值。卡片檔不受影響（Card 4 四個數字均取自表 1）。`verification` 維持 `partial`。

### EK-193 | fixed | papers/2025-fragment-shot-reasoning-mt-frontull.md | Card 4 模型參數與證據表 | 未能核實
- **問題**：論文頁列 GPT-3.5 175B、GPT-4o 200B、o1-mini 50B、Llama 3.3 70B、DeepSeek-R1 658B，與本篇原文 §5 所列數字一致，但證據表僅記模型名稱。DeepSeek 官方資料為原始 R1 列出 671B 總參數與 37B 啟用參數，與本篇的 658B 不一致；所查 OpenAI 資料的 175B 是 GPT-3 的數字，不能據此確定 GPT-3.5 的參數量，所查 GPT-4o 與 o1 系統卡亦未核實頁面列出的 200B 與 50B。Meta 的 Llama 3.3 70B 模型卡支持 70B 規模。原研究使用 API，未明確記載服務實例的具體快照；修訂時須保留論文與官方來源的差異，不把未證實直接視為證偽，也不能僅憑官方權重推定當時 API 版本。
- **來源**：[Frontull 與 Ströhle 原文](https://arxiv.org/html/2505.22293v1) §5 p. 5；[DeepSeek 官方模型資料](https://github.com/deepseek-ai/DeepSeek-R1)；[OpenAI GPT-3 資料](https://openai.com/index/language-models-are-few-shot-learners/)；[GPT-4o 系統卡](https://cdn.openai.com/gpt-4o-system-card.pdf)；[o1 系統卡](https://openai.com/index/openai-o1-system-card/)；[Meta Llama 3.3 70B 模型卡](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)。
- **發現於**：2026-11-10，第五批審查回報，Codex by OpenAI 再核對原文與官方資料。
- **處理**：2026-11-10，Codex by OpenAI（GPT-6）。論文頁將參數量明確歸給原研究，並列官方 R1 的 671B／37B、GPT-3 175B 的版本歸屬及所查系統卡無法核實的數字，保留 API 快照未明的限制；證據表逐一登記原文及官方資料。無法核實的實際 API 規模不作猜測，此頁核實狀態改為 partial。
