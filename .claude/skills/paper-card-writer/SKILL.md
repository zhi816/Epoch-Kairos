---
name: paper-card-writer
description: >-
  Write the text and diagram for every Epoch-Kairos paper card: the homepage cover card (card wall and paper-page Card 1) and the paper-page Cards 2-6, stored as wiki/cards/<slug>.md, then build and browser-verify both the paper-page prototype and the homepage card wall. Use whenever a paper is ingested, when backfilling or revising card files, or when card_line, hook-derived lead text or Card 3 diagrams change. Every field has hard length limits, source rules and mandatory check scripts; do not skip steps.
---

# paper-card-writer（轉介檔）

本檔僅供 Claude Code 自動載入，不含任何規則。正本為 [`.agents/skills/paper-card-writer/SKILL.md`](../../../.agents/skills/paper-card-writer/SKILL.md)。

1. 先以 Read 完整讀取正本，再依正本執行；正本與本檔描述有出入時一律以正本為準。
2. 正本提到的 `references/` 與 `scripts/` 皆位於 `.agents/skills/paper-card-writer/` 之下，請以該路徑讀取與執行；`references/` 須依正本指示逐份讀完。
3. 修改規則時只改正本，不在本檔另寫內容（見 AGENTS.md 第六章開頭之 Skill 一覽）。
