---
title: "The Colonial Origins of Comparative Development: An Empirical Investigation"
title_zh: "比較發展的殖民起源：制度形成與國家長期繁榮成因"
paper_year: 2001
award_year: 2024
timeline_year: 2024
authors: "Daron Acemoglu, Simon Johnson, James A. Robinson"
venue: "American Economic Review, 91(5), 1369-1401"
venue_short: "AER"
honor: "2024 諾貝爾經濟學獎（表彰對制度如何形成並影響國家繁榮之研究）"
domain: "econ"
domain_tags: ["#制度經濟學", "#宏觀經濟學"]
concepts: ["institutions-and-macro-dynamics"]
status: "wiki"
verification: "verified"
my_focus: false
doi_url: "https://doi.org/10.1257/aer.91.5.1369"
key_papers:
  - "Acemoglu, D., Johnson, S., & Robinson, J. A. (2001) The Colonial Origins of Comparative Development: An Empirical Investigation. American Economic Review 91(5):1369-1401. https://doi.org/10.1257/aer.91.5.1369"
  - "Acemoglu, D., Johnson, S., & Robinson, J. A. (2002) Reversal of Fortune: Geography and Institutions in the Making of the Modern World Income Distribution. Quarterly Journal of Economics 117(4):1231-1294. https://doi.org/10.1162/003355302320935025"
  - "Acemoglu, D., Johnson, S., & Robinson, J. A. (2005) Institutions as a Fundamental Cause of Long-Run Growth. Handbook of Economic Growth 1A:385-472. https://doi.org/10.1016/S1574-0684(05)01006-3"
hook: "以數百年前歐洲殖民者的疫病死亡率作為工具變數，嚴格識別出「產權保護制度」而非地理環境，才是決定國家貧富差距高達三十倍的根本原因。"
card_line: "從殖民者死亡率，找出制度決定國家貧富"
---

# 比較發展的殖民起源：制度形成與國家長期繁榮成因

> 「歷史並非宿命，但數百年前為掠奪資源或定居繁衍而設下的制度基因，卻透過強大的路徑依賴，決定了當代數十億人的富裕與貧窮。」

**2001 發表 ｜ 2024 諾貝爾經濟學獎**

> **本頁範圍說明**：2024 年諾貝爾經濟學獎頒予 Daron Acemoglu、Simon Johnson 與 James A. Robinson 三位學者，表彰其對「制度如何形成並影響國家長期繁榮」之開創性貢獻。本頁以三人於 2001 年發表於《American Economic Review》之代表作（AJR 2001）為主軸，並於 `key_papers` 列出 2002 年「命運逆轉（Reversal of Fortune）」與 2005 年政治制度動態理論之奠基文獻。

---

## Card 1 ｜ 時代銘文 (The Hook)
為何世界上最富裕國家與最貧窮國家的人均所得差距超過 30 倍？究竟是熱帶地理環境限制了生產力，還是制度決定了成敗？Acemoglu、Johnson 與 Robinson (2001) 巧妙利用 17 至 19 世紀歐洲派駐全球殖民地之士兵、主教與水手的歷史死亡率作為外生工具變數（Instrumental Variable），一舉破解了制度與經濟成長之間的雙向因果死結，奠定了現代發展經濟學與政治經濟學的實證基石。

---

## Card 2 ｜ 世紀瓶頸：制度與繁榮的「內生性死結」 (The Dilemma)
長久以來，經濟學家觀察到「產權保護越完善的國家越富裕」，但始終無法確立因果方向：

* **反向因果（Reverse Causality）**：究竟是因為擁有包容性好制度才帶來富裕，還是因為國家變得富裕之後，才負擔得起高品質的法院、廉潔官僚與產權保護？
* **遺漏變數偏誤（Omitted Variable Bias）与地理決定論**：Jeffrey Sachs 與 Jared Diamond 等學者指出，緯度、氣候、土壤與疾病負擔直接影響經濟產出。若不將制度從地理、文化等混雜因素中剝離，任何普通最小平方法（OLS）迴歸都只是一紙相關性，無法作為因果證據。

---

## Card 3 ｜ 突破架構與原理 (The Secret)
作者建構了一條跨越數百年的歷史因果鏈，並以兩階段最小平方法（2SLS）實現因果識別：

$$\ln M_i \implies S_i \implies C_i \implies R_i \implies \log y_i$$

其中 $\ln M_i$ 為歷史潛在殖民者死亡率，$S_i$ 為早期歐洲定居人數比例，$C_i$ 為早期殖民制度，$R_i$ 為當代制度品質，$\log y_i$ 為當代人均對數產出。

1. **雙軌殖民策略（Extractive vs. Inclusive Institutions）**：
   * 在瘧疾與黃熱病肆虐、歐洲人死亡率極高的地區（如剛果、黃金海岸），殖民強權無法大規模移民定居，遂建立以榨取金礦、象牙與奴隸為目的的「掠奪型制度（Extractive State）」，不設行政制衡與私人產權保護。
   * 在疾病環境溫和、死亡率極低的地區（如美國、加拿大、澳洲、紐西蘭），歐洲移民大量定居並要求享有與母國同等的法治與代議制，建立起保護財產與鼓勵投資的「新歐洲（Neo-Europes）」包容型制度。
2. **制度的歷史持續性（Institutional Persistence）**：
   * 建立包容型制度需要高昂的沉沒成本；反之，一旦掠奪型國家機器成型，獨立後的本土新統治菁英同樣有強烈誘因繼承這套便於尋租與徵收的體制，使早期制度延續至今。
3. **排他性限制（Exclusion Restriction）**：
   * 工具變數法之核心識別假設為 $\operatorname{Cov}(\ln M_i, \epsilon_i \mid X_i) = 0$，即數百年前殖民者死亡率僅能透過影響「早期制度形成」來決定當代產出，不存在直接影響當代生產力的殘差路徑。對此識別假設的最大疑慮是：高歷史死亡率的熱帶疾病環境可能直接延續至今，造成當代人口的健康劣勢。作者對此提出流行病學與歷史證據論證假設之合理性：導致 18、19 世紀歐洲軍人極高死亡率的瘧疾與黃熱病，對當地已具備自然免疫力與抗性之成年原住民勞動力的致命威脅遠低於歐洲人（例如 Philip Curtin 統計顯示在印度孟加拉與馬德拉斯服役之本地士兵年死亡率與英國本土部隊相當，而當地英國士兵死亡率則數倍於此）。因此，歷史殖民者死亡率反映的是歐洲殖民定居環境的阻力，而非當地原住民勞動力受不可抗拒地理宿命限制的證明。

### 1. 結構方程與歷史制度演化鏈 (Structural Causal Chain)

當代第 $i$ 個前殖民地國家的人均對數所得 $\log y_i$ 由當代制度品質 $R_i$（以「免於政府徵收風險指數」衡量）與其他協變數向量 $X_i'$ 決定：

$$\log y_i = \mu + \alpha R_i + X_i' \gamma + \epsilon_i$$

而當代制度 $R_i$ 則由早期制度 $C_i$、早期歐洲定居人口比例 $S_i$ 及歷史殖民者死亡率 $\ln M_i$ 依序傳遞：

$$\begin{aligned}
R_i &= \lambda_R + \beta_R C_i + X_i' \gamma_R + \nu_{Ri} \\
C_i &= \lambda_C + \beta_C S_i + X_i' \gamma_C + \nu_{Ci} \\
S_i &= \lambda_S + \beta_S \ln M_i + X_i' \gamma_S + \nu_{Si}
\end{aligned}$$

### 2. 兩階段最小平方法（2SLS）識別方程 (Two-Stage Least Squares Estimation)

由於結構誤差項 $\operatorname{Cov}(R_i, \epsilon_i) \neq 0$，直接估計 $\alpha$ 會產生偏誤。作者將上述歷史傳遞鏈收斂為以對數殖民者死亡率 $\ln M_i$ 為工具變數的第一階段（First-Stage）迴歸：

$$\begin{aligned}
\text{First Stage:} \quad R_i &= \zeta + \beta \ln M_i + X_i' \delta + v_i \\
\text{Second Stage:} \quad \log y_i &= \mu + \alpha \hat{R}_i + X_i' \gamma + \epsilon_i
\end{aligned}$$

其中兩階段最小平方法估計量 $\hat{\alpha}_{\text{2SLS}}$ 在排他性條件 $\operatorname{Cov}(\ln M_i, \epsilon_i \mid X_i) = 0$ 與強相關條件 $\beta \neq 0$ 下，具有統計一致性（Consistency）：

$$\begin{aligned}
\operatorname{plim} \hat{\alpha}_{\text{2SLS}} &= \frac{\operatorname{Cov}(\log y_i, \ln M_i \mid X_i)}{\operatorname{Cov}(R_i, \ln M_i \mid X_i)} \\
&= \alpha
\end{aligned}$$

---

## Card 4 ｜ 決定性數據 (The Evidence)

### 本篇論文（Acemoglu, Johnson & Robinson 2001）之核心證據
* **64 個前殖民地國家基礎樣本與強第一階段關聯**：在 64 個前歐洲殖民地基礎樣本中，歷史殖民者對數死亡率 $\ln M_i$ 與 1985–1995 年平均「免於徵收風險指數」（Protection Against Expropriation Risk，PRS 計分範圍 0–10，分數越高代表產權保護越完善）呈現負相關。第一階段係數為 $\hat{\beta}=-0.61$（標準誤 $0.13$，$R^2=0.27$）；對數死亡率增加 1 個單位，指數平均下降約 0.61 分。
* **制度效果的 2SLS 估計（$\hat{\alpha}_{\text{2SLS}}=0.94$）**：基準 2SLS 估計出制度指數對 1995 年 PPP 人均對數 GDP 的係數為 $0.94$（標準誤 $0.16$），高於同一表 OLS 估計值 $0.52$。作者指出，測量誤差造成的衰減偏誤可能比反向因果與遺漏變數偏誤更重要。
* **奈及利亞與智利的制度差距解釋力**：作者以兩國作為 IV 迴歸中的典型比較，報告制度風險指數相差 $2.24$ 分，按基準 2SLS 估計對應約 206 對數點、約 7 倍的人均所得差距；作者提醒測量誤差可能解釋部分指數差，因此將 7 倍視為上限。論文另指出，1995 年智利人均所得實際上超過奈及利亞 11 倍。若僅以文中四捨五入的 $0.94$ 與 $2.24$ 重算，$\exp(0.94\times2.24)\approx8.2$；這是依四捨五入值推算，並非作者報告的 206 對數點結果。
* **穩健性與替代規格**：
  * **樣本與洲別規格（Table 4）**：排除新歐洲國家後，係數為 $1.21$–$1.28$；排除非洲樣本後為 $0.58$；加入洲別虛擬變數後為 $0.98$–$1.10$（基準為 $0.94$）。
  * **殖民來源、法律來源與宗教控制（Table 5）**：2SLS 係數範圍為 $0.92$–$1.20$。
  * **地理、環境與族群控制（Table 6）**：納入溫濕度、歐洲裔人口比例、土壤與自然資源、內陸與族群破碎度等變數，係數範圍為 $0.71$–$1.30$。
  * **當代疾病、健康與替代工具變數（Table 7）**：納入瘧疾、壽命、嬰兒死亡率等控制，並另以黃熱病作工具變數，係數範圍為 $0.55$–$0.91$。
  不同規格下估計值與顯著性並不完全相同；作者特別提醒健康變數可能內生，直接控制可能低估制度效果。這些結果仍顯示其制度估計對多種控制組合保持正向。

### 後續領域關鍵證據（非本篇成果，標註出處）
* **命運逆轉（Reversal of Fortune）**：Acemoglu, Johnson & Robinson (2002), *Quarterly Journal of Economics* 117(4):1231-1294，證明在 1500 年最富裕、城市化與人口密度最高的文明區（如蒙兀兒印度、阿茲特克、印加），因最有利於建立強迫勞動與掠奪型稅收制度，反而在工業化時代淪為相對貧困區，徹底否定「某些地理環境天生不利發展」的靜態地理決定論。
* **殖民強迫勞動制度（Mita）的微觀斷點迴歸**：Dell (2010), *Econometrica* 78(6):1863-1903，以秘魯與玻利維亞安地斯山脈 1573 年西班牙殖民政府劃定的礦業強迫勞役（Mita）地理邊界進行空間斷點迴歸（Spatial RDD），證明邊界兩側海拔與地理完全相同，但曾受掠奪制度統治的一側至今家庭消費仍低約 25%、兒童發育遲緩率高出 6 個百分點。

---

## Card 5 ｜ 時代典範轉移 (The Revolution)
* **引爆經濟學「可信度革命（Credibility Revolution）」的宏觀典範**：將原本侷限於勞動經濟學的自然實驗（Natural Experiments）與工具變數法推向宏觀歷史與制度研究，開啟「歷史持續性研究（Persistence Studies）」的全新領域。
* **重塑國際發展援助與世界銀行政策思維**：促使國際發展政策從單純的「資本注入與硬體基建」轉向「治理、法治與制度改革」。後續制度經濟學文獻進一步推論指出：若在掠奪型體制下單純輸送外援，援助資金容易遭尋租菁英截留攫取，難以轉化為普惠的長期繁榮（此屬文獻與政策延伸觀點，非 AJR 2001 本文直接檢驗之經驗結果）。
* **政治權力與技術走向的合流**：Acemoglu 與 Johnson 後續將此框架延伸至技術史（《Power and Progress》，2023），指出人工智慧與自動化究竟是「賦能勞工、創造新職位」還是「純粹監控並取代勞工」，同樣取決於社會制度的權力分配結構。

---

## Card 6 ｜ 跨界思維與啟發 (The Kairos)
AJR (2001) 帶給科學方法論與人類文明史的雙重啟示：

1. **歷史是天然的因果實驗室**：當我們無法在宏觀國家層級進行隨機對照實驗（RCT）時，歷史長河中的偶然分岔（如微生物免疫差異），提供了拆解社會複雜系統因果迴路的天然探針。
2. **繁榮的本質是「對普遍創造力的制度承諾」**：唯有當一個社會的規則能確保一般人的勞動、知識與創新成果不會被強權任意剝奪時，技術進步與資本積累的飛輪才會真正啟動。

---

## 知識網絡與文獻出處
* **核心實體與跨領域概念**：
  * [制度演化與宏觀經濟動態](../concepts/institutions-and-macro-dynamics.md)
* **原始權威文獻**：
  * 官方學術出處：Acemoglu, D., Johnson, S., & Robinson, J. A. (2001). American Economic Review, 91(5), 1369-1401. DOI: [10.1257/aer.91.5.1369](https://doi.org/10.1257/aer.91.5.1369)
  * 原始檔典藏：`raw/2001-colonial-origins-acemoglu.pdf`（不納入本倉庫，由私有倉庫 Mine-RAW 版控）
  * 獎項通告：[The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2024](https://www.nobelprize.org/prizes/economic-sciences/2024/)
