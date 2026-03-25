# Changelog — Coding Agents Labs

Path: `/coding-agents/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-24

### [feature] Lab 09 — "Do I Still Need to Code?"
- New lab exploring the developer's role in the AI age
- Hero canvas: Developer node ↔ Shared Workspace ↔ AI Agent node with task token routing
- Skill shift chart comparing pre-AI vs AI-era developer skills
- Scenario quiz: classify tasks as Human-led / AI-led / Collaborative
- Spot-the-bug challenge with nuanced "yes, you still need to code" answer

### [bug] Lab 09 canvas blank — JS syntax error
- **Symptom:** Canvas area visible but completely empty; no animation
- **Root cause:** Single-quoted strings containing apostrophes (`it's`, `don't`) caused a silent SyntaxError that killed the entire `<script>` block
- **Fix:** Converted all affected strings to backtick template literals
- **Lesson:** Run `node --check` first when canvas is blank — script parse errors kill everything silently
- **Led to:** Creation of `CLAUDE.md` with diagnostic checklist

### [feature] Thorough explanations added to Labs 01–08
- Each lab received a rich static HTML section below the interactive simulation
- Sections added: Concept Overview, How It Works (numbered steps), Callouts (info/warn/tip), Real World Examples, Common Pitfalls, Key Takeaways
- CSS classes introduced: `.explain-section`, `.explain-h2`, `.explain-p`, `.explain-grid`, `.explain-card`, `.steps-list`, `.callout`, `.takeaways`, `.rw-badge`, `.pitfall`, `.compare-table`, `.divider`

---

## 2026-03-23

### [feature] Lab 09 added to coding-agents homepage
- Card added in new "The Big Question" section group
- New `.tag-b{background:#0d2a14;color:#3fb950}` CSS tag class added
