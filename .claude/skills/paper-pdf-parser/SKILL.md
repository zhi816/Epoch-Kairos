---
name: paper-pdf-parser
description: >-
  Extract academic paper PDFs into searchable Markdown with PDF page markers so wiki-content-audit and academic-paper-translator can locate claims, numbers and pages. Default to PyMuPDF; use local MinerU only for image-only PDFs, garbled text layers, or drafting long formulas. All output is a draft, never evidence: verify every number, formula and page against the original PDF before writing it anywhere. Runs locally only on macOS and Windows.
---

# paper-pdf-parser（轉介檔）

本檔僅供 Claude Code 自動載入，不含任何規則。正本為 [`.agents/skills/paper-pdf-parser/SKILL.md`](../../../.agents/skills/paper-pdf-parser/SKILL.md)。

1. 先以 Read 完整讀取正本，再依正本執行；正本與本檔描述有出入時一律以正本為準。
2. 正本提到的 `scripts/` 皆位於 `.agents/skills/paper-pdf-parser/scripts/`，請以該路徑執行。
3. 修改規則時只改正本，不在本檔另寫內容（見 AGENTS.md 第六章開頭之 Skill 一覽）。
