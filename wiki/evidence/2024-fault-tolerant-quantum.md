# 證據表：2024-fault-tolerant-quantum

本表記錄 [wiki/papers/2024-fault-tolerant-quantum.md](../papers/2024-fault-tolerant-quantum.md) 各項主張在第一手文獻中的出處與核驗結果。

- **主要第一手來源**：Bluvstein, D., Evered, S. J., Geim, A. A., Li, S. H., Zhou, H., Manovitz, T., Ebadi, S., Cain, M., Kalinowski, M., Hangleiter, D. et al., Greiner, M., Vuletić, V., & Lukin, M. D. (2024). Logical quantum processor based on reconfigurable atom arrays. *Nature*, 626(7997), 58–65. DOI: [10.1038/s41586-023-06927-3](https://doi.org/10.1038/s41586-023-06927-3)
- **封存原文**：`raw/2024-fault-tolerant-quantum.pdf`

---

| 頁面章節 | 主張／陳述 | 第一手來源出處 | 核驗結果與說明 |
|---|---|---|---|
| Card 1 | 以光學鑷子相干搬運中性銣原子（$\mathrm{^{87}Rb}$）實現可重構陣列 | 摘要 (p. 1), §System overview (Methods, p. 12), Fig. 1 | 核實更正。使用 852-nm 光學鑷子與 2D AOD 相干搬運中性銣-87 原子（基態超精細鐘態，$T_2 > 1\,\text{s}$）。更正 Card 1 誤植之「帶電相干搬運」為中性原子光鑷搬運。 |
| Card 3 | 儲存區、糾纏區與讀取區之三區分立動態架構 | §Logical processor based on atom arrays (pp. 1–2), Fig. 1a, ED Fig. 1 | 核實符合。儲存區進行長壽命量子儲存，糾纏區施加里德堡雙光子雷射進行並行 CZ 閘，讀取區進行無損中途螢光成像與 FPGA 即時前饋。 |
| Card 4 | 表面碼碼距 $d=3 \to 5 \to 7$ 邏輯貝爾態錯誤抑制 | §Improving entangling gates with code distance (pp. 3–4), Fig. 2d | 核實符合。在相關解碼（Correlated Decoding）下，邏輯貝爾態錯誤率隨碼距增加單調下降（$d=7$ 動用 98 個資料位元與 48 個輔助位元，共 146 個物理原子）。 |
| Card 4 | 40 個色碼邏輯量子位元之分區編碼與操作 | §Fault-tolerant logical algorithms (p. 5), Fig. 4a–c | 核實更正。使用 280 個物理原子，透過分區架構分批編碼 40 個 $d=3$ 色碼邏輯量子位元，並以 20 個橫向 CNOT 實施標記容錯初始化，閒置退相干率約 1%。糾正原先將 40 個色碼位元誤寫為「40 個橫向 CNOT 閘」之錯誤。 |
| Card 4 | 48 個邏輯量子位元之三維 [[8,3,2]] 碼取樣電路 | §Complex logical circuits using 3D codes (pp. 5–7), Fig. 5c–f | 核實更正。在 128 個物理原子上編碼 16 個 3D $[[8,3,2]]$ 區塊（共 48 個邏輯位元），在 4D 超立方體連接拓撲下執行包含 **228 個邏輯雙位元閘（CZ/CNOT）與 48 個邏輯 CCZ 閘**（非 Clifford 閘）之深層亂序電路；全錯誤偵測下 XEB 達約 0.1，超越物理位元近一個數量級。明確區分此實驗與 40 色碼實驗。 |
| Card 5 | 突破平面拓撲限制，為未來 qLDPC 等高編碼率量子碼奠定硬體基礎 | §Outlook (p. 8) | 核實更正。本實驗實作了表面碼、色碼與三維 $[[8,3,2]]$ 碼；qLDPC 碼在原文 Outlook 中僅列為未來進一步降低物理開銷的重要發展方向，更正 Card 5 將 qLDPC 寫成已由本實驗實作之問題。 |
