---
title: "Brain-Machine Interfaces & Neural Coding"
title_zh: "腦機介面與神經編碼"
domain: "bio"
domain_tags: ["#神經科學", "#生物科技", "#人工智慧"]
papers: ["1982-hopfield-network", "2005-optogenetics"]
related_concepts: ["neural-circuits", "programmable-cellular-engineering"]
verification: "verified"
---

# 概念：腦機介面與神經編碼 (Brain-Machine Interfaces & Neural Coding)

> 領域：`#神經科學` `#生物科技` `#人工智慧`

---

## 核心定義
**腦機介面（Brain-Machine Interface, BMI / BCI）** 與 **神經編碼（Neural Coding）** 旨在破譯大腦神經元群體動作電位序列（Spike Trains）與內在認知意圖、感官表徵之間的雙向映射法則，並藉由物理（電、光、磁、聲）或分子工程介面，實現生物神經系統與外部計算裝置之間的高頻寬、高時空解析度雙向讀寫（Bidirectional Read-Write）。

---

## 關鍵突破支柱
* **群體吸引子編碼與分佈式狀態空間（1982）**：Hopfield 證明神經資訊可分散編碼於神經元群體狀態空間的能量極小點與吸引子（Attractors）中，推動了計算神經科學從單一細胞記錄走向群體幾何動態學。當代腦機介面廣泛採用的神經流形（Neural Manifolds）解碼技術源於運動皮質經驗生理學與降維統計建模（如 Churchland et al. 2012, Cunningham & Yu 2014），兩者在群體狀態空間觀念上相互啟發，但非直接數學推導。
  * 詳見核心論文：[Hopfield 神經網絡（1982 發表 ｜ 2024 諾貝爾物理學獎）](../papers/1982-hopfield-network.md)
* **光遺傳學精準神經寫入介面（2005）**：克服傳統金屬微電極刺激「空間擴散、無細胞型別專一性」之物理極限，以光敏離子通道（ChR2）實現毫秒級、細胞類型特異性的光學神經訊號寫入。
  * 詳見核心論文：[光遺傳學（2005 發表 ｜ 2026 諾貝爾生理學或醫學獎）](../papers/2005-optogenetics.md)

---

## 跨學科交會與延伸
1. **從微電極陣列到全息光學腦機介面（All-Optical BCI）**：
   * 傳統侵入式 BCI 依賴金屬微電極陣列（如猶他陣列）或柔性神經探針記錄細胞外電位並以電流脈衝刺激；次世代全光學腦機介面結合基因編碼指示劑（如 GCaMP，雙光子螢光讀取）與雙光子全息光遺傳學（Holographic Optogenetics，以空間光調製器 SLM 引導多焦點雷射寫入），在動物模型中實現記錄數千神經元並對數十至數百個特定細胞進行單細胞級閉環調控。但受限於大腦組織散射深度、光熱沉積耐受極限與外源基因遞送，目前距萬級神經元規模或無損人體臨床實用仍存在客觀物理瓶頸。
2. **臨床神經義肢與感官重建**：
   * 在視網膜色素變性失明患者之光遺傳學臨床試驗（如 AAV 介導之 ChrimsonR 配合光刺激眼鏡）以及高位脊髓損傷、肌萎縮性脊髓側索硬化症（ALS）患者之微電極皮質植入（如 BrainGate 結合低維流形投影與循環網路解碼手寫/語音）中，群體神經解碼與細胞級調控正持續邁向臨床驗證。

---

## 關聯概念網絡
* [神經迴路因果解耦](neural-circuits.md)
* [可編程細胞與基因工程](programmable-cellular-engineering.md)
