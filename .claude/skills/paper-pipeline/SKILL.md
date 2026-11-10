---
name: paper-pipeline
description: >-
  End-to-end pipeline that turns a new raw/ source into a paper published on the Epoch-Kairos homepage: intake and bibliography check, reading the PDF, evidence table, wiki paper page, concept pages and index, two-stage verification, card file, paper-page prototype, homepage star map or my-constellation plus card wall, log and commit. Use it first whenever a new file appears in raw/, the user asks to ingest or "上架" a paper, or a paper must be brought to completion. For every step it names the skill to follow, the files to produce and the command that proves the step is done; pipeline_status.py shows where each paper stands.
---

# paper-pipeline（轉介檔）

本檔僅供 Claude Code 自動載入，不含任何規則。正本為 [`.agents/skills/paper-pipeline/SKILL.md`](../../../.agents/skills/paper-pipeline/SKILL.md)。

1. 先以 Read 完整讀取正本，再依正本執行；正本與本檔描述有出入時一律以正本為準。
2. 正本提到的 `references/` 與 `scripts/` 皆位於 `.agents/skills/paper-pipeline/` 之下，請以該路徑讀取與執行；`references/` 須依正本指示逐份讀完。
3. 修改規則時只改正本，不在本檔另寫內容（見 AGENTS.md 第六章開頭之 Skill 一覽）。
