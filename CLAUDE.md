# Playground — Agent Instructions

## Prompting Guidance — Auto-Suggest Better Phrasing

When a user prompt is ambiguous or likely to cause a misunderstanding, **proactively suggest a clearer rephrasing** before or after completing the task. Do not wait to be asked.

**Trigger conditions — suggest a rewrite when the prompt:**
- Describes a visual/layout change without naming a reference file (e.g., "move it to the top" — ask or note which file to follow)
- Uses relative terms without anchors ("the button", "that section") when multiple candidates exist
- Bundles multiple distinct tasks in one sentence without separators — suggest breaking into a numbered list
- Specifies a symptom but also a presumed fix that might be wrong — confirm the fix before applying
- Is a vague completion request ("make it work", "fix it") — clarify which behavior is expected

**Format for the suggestion** (keep it short, inline):
> **Clearer prompt would be:** "Follow Lab 05's overlay placement exactly — `bottom:1rem; right:1rem`, badge first in DOM."

Only suggest when it would have meaningfully changed the interpretation. Don't suggest rewrites for clear, specific prompts.

---

## After Writing or Editing HTML Files

Always run a JS syntax check on any HTML file you write or edit that contains `<script>` blocks:

```bash
sed -n '/<script>/,/<\/script>/p' <file> | grep -v '<.script' | node --check /dev/stdin
```

Or using line numbers if you know them:

```bash
sed -n '327,1006p' <file> > /tmp/check.js && node --check /tmp/check.js
```

Fix any syntax errors before declaring the task done.

**Common causes of JS syntax errors in HTML files:**
- Single-quoted strings containing apostrophes (`it's`, `don't`, `can't`) — use backticks instead
- Template literals with unescaped backticks
- Missing closing brackets or braces
- HTML entity characters (`&amp;`, `&lt;`) accidentally inside `<script>` blocks

---

## Debugging a Blank Canvas or Missing UI

Follow this order — do not skip ahead:

1. **Check if the script parsed** — extract the `<script>` block and run `node --check`. If the script has a syntax error, nothing inside it runs. This is the most common cause of "nothing works" bugs.
2. **Check if globals from the script exist** — run `typeof window.X` for any global the script should define. If `undefined`, the script didn't execute.
3. **Check browser console logs** — use `preview_console_logs` to look for runtime errors.
4. **Manually draw a test shape** — use `preview_eval` to call `ctx.fillRect(...)` directly. If it works, the canvas is fine; the issue is in initialization logic.
5. **Only then** investigate runtime/timing issues (layout not ready, `clientWidth` = 0, etc.)

---

## Post-Write Verification Checklist

After writing any `.html` file:

- [ ] JS syntax check passes (`node --check`)
- [ ] Page loads without console errors (`preview_console_logs`)
- [ ] Key interactive elements are visible (`preview_screenshot`)
- [ ] Changelog updated (see below)
- [ ] Lessons-learned updated? — if the change introduced or confirmed a pattern, update the relevant file:
  - New bug root cause → `lessons-learned/bug-fixes.md`
  - New feature/state pattern → `lessons-learned/feature-dev.md`
  - UX decision or layout rule → `lessons-learned/ux.md`
  - Code restructure insight → `lessons-learned/refactor.md`
  - Better prompting pattern discovered → `lessons-learned/prompting.md`
  - Better Claude Code process or workflow insight → `lessons-learned/workflow.md`

---

## JS State Pattern Checklist

After adding or modifying **any interactive state variable** in a lab (objectives, Sets, booleans):

- [ ] **saveState includes the new variable?** — every variable that needs to persist must be serialized (Sets: `[...mySet]`)
- [ ] **loadState restores it?** — deserialize Sets with `new Set(s.myVar || [])`, booleans with `s.myVar || false`
- [ ] **updateObj / checkReflectionLock called after loadState?** — restoring variables is not enough; the overlay must be re-rendered from them
- [ ] **Init order: nothing calls saveState before loadState?** — any function in `DOMContentLoaded` that internally calls `saveState()` must run AFTER `loadState()`
- [ ] **Default-active elements seeded in Set?** — if a tab/card/button is pre-highlighted in HTML, seed its value into the tracking Set after `loadState()` when the Set is empty (first visit only)
- [ ] **Badge count matches checks array length?** — `0/N objectives` in HTML must equal `checks.length` in `updateObj()`

**Common pattern for default-active element:**
```javascript
loadState();
if (myTabsSeen.size === 0) {
  myTabsSeen.add('default-tab-id'); // pre-highlighted in HTML
}
checkReflectionLock();
```

---

## Building a New Industry Primer

When asked to add a new industry to `primer/`, follow this spec exactly.

### Canonical template

Copy the structure from **`primer/insurance/index.html`** — it is the reference implementation. Do not copy from ecommerce, edtech, or ai-infrastructure (they use an older `data-tab` JS system).

### File location

```
primer/<industry-slug>/index.html
```

Use lowercase kebab-case slugs: `video-game-retail`, `ai-infrastructure`, `real-estate`, etc.

### Tab structure — 8 tabs required

Every primer has exactly **9 tabs** in this order:

| # | Tab label | Section id |
|---|---|---|
| 1 | Overview | `tab-overview` |
| 2 | Key Terminology | `tab-terminology` |
| 3 | Major Players | `tab-players` |
| 4 | Core Metrics | `tab-metrics` |
| 5 | Technology Stack | `tab-stack` |
| 6 | Common Workflows | `tab-workflows` |
| 7 | Trends & Challenges | `tab-trends` |
| 8 | Market Dynamics & Monetization | `tab-dynamics` |
| 9 | Evolution & Foundations | `tab-evolution` |

Tab nav buttons use `onclick="showTab('name', idx)"` (0-indexed). Progress label reads `"Section N of 9"`. Progress bar has 9 dots (dot-0 through dot-8).

### Required content per tab

**1 — Overview**
- 6 sub-sector cards (`.card-grid` → `.card` with `.card-icon`, `<h3>`, `<p>`)
- Value chain diagram (`.value-chain` → `.chain-row` with `.chain-node` + `.chain-arrow`)
- 6 market context cards (featured companies, market size, key facts)

**2 — Key Terminology**
- 15–22 expandable glossary terms
- Search box (`#gloss-search`) filters by `data-terms` attribute + term text
- Each item: `.glossary-item[data-terms="..."]` > `.glossary-header[onclick="toggleGloss(this)"]` > `.glossary-term` + `.glossary-cat` + `.glossary-chevron` > `.glossary-body`

**3 — Major Players**
- 3–5 `.player-section` groups, each with a `.player-section-title` and `.player-grid`
- Each player: `.player-card` > `.player-name` + `.player-role` + `.player-tag`

**4 — Core Metrics**
- `.metrics-table` with columns: Metric | Formula/Definition | Benchmark/Notes
- Group rows under `.metrics-cat` labels (use `<span class="metrics-cat">` before rows)

**5 — Technology Stack**
- 7 `.stack-layer` rows, each with `.stack-layer-label` + `.chip-row`
- Chips: `.chip` (blue/default), `.chip.green`, `.chip.purple`, `.chip.muted`

**6 — Common Workflows**
- 3 workflows, each in `.workflow` > `<h3>` + `.workflow-desc` + `.workflow-steps`
- 5 steps per workflow: `.workflow-step` > `.step-num` + `.step-content` (`.step-title` + `.step-detail`)

**7 — Trends & Challenges**
- 6 `.trend-card` items in `.trend-grid`
- Each: `.trend-icon` + `.trend-title` + `.trend-desc`

**8 — Market Dynamics & Monetization**
- **Pain points** (5 cards in `.card-grid`): industry-specific operational/structural pain points operators face — regulatory friction, cost pressures, competitive dynamics, structural shifts
- **Monetization models** (`.metrics-table` with columns: Model | Description | Margin Profile): 5–7 rows covering how money is made in this industry, with margin benchmarks where known

**9 — Evolution & Foundations**
- **Historical timeline** (8 cards in `.card-grid`): chronological milestones spanning the industry's full history; each card has `.card-icon` (year or era), `<h3>` (milestone name), `<p>` (what happened and why it mattered); cover founding era → key inflection points → present
- **Foundational works** (`.metrics-table` with columns: Work | Author / Year | Why It Matters): 5–7 rows; include seminal books, landmark papers, key regulations/standards, and technical specifications that define the field's core principles; focus on works practitioners reference most

### JS rules

- **No apostrophes in JS strings** — use `"don" + "t"` or rephrase; double quotes or template literals only
- The `showTab` function signature: `function showTab(name, idx)` — updates `.tab-section` active class, `.tab-btn` active class, `.progress-dot` active class, and `#progress-label` text
- The `toggleGloss` function: `function toggleGloss(header) { header.parentElement.classList.toggle("open"); }`
- Glossary search: `input` event on `#gloss-search` filters `.glossary-item` by checking `data-terms` + term text against lowercase query; toggles `hidden` class or `display:none`
- `/` keyboard shortcut focuses `#gloss-search`

### Header block

```html
<div class="breadcrumb"><a href="../index.html">Industry Primer</a><span>/</span>INDUSTRY NAME</div>
<div class="page-header">
  <h1>EMOJI Industry Name</h1>
  <div class="subtitle">One-sentence description of scope and featured companies.</div>
  <div class="tag-row">
    <span class="tag">tag1</span>
    <span class="tag green">tag2</span>
    <span class="tag purple">tag3</span>
    <span class="tag">tag4</span>
  </div>
</div>
```

### Post-creation checklist

- [ ] JS syntax check passes: `sed -n '/<script>/,/<\/script>/p' primer/<slug>/index.html | grep -v '<[/]*script>' | node --check /dev/stdin`
- [ ] Add industry card to `primer/index.html` grid (`data-industry`, `data-search`, status badge `live`, progress `8 / 8 sections`)
- [ ] Add nav link to `primer/index.html` sidebar with "New" badge
- [ ] Update `changelog/primer.md` with detailed entry (all 8 tabs, terminology count, workflow titles)
- [ ] Update root `CHANGELOG.md` with one-line summary

### Changelog routing

| What changed | Update this file |
|---|---|
| Any `primer/` file | `changelog/primer.md` |

---

## Changelog Update — Required After Every Change

After **any** file is created or edited in this project, update the changelog before declaring the task done.

### Which files to update

| What changed | Update this file |
|---|---|
| `coding-agents/` | `changelog/coding-agents.md` |
| `case-studies/` | `changelog/case-studies.md` |
| `trainer-series/` | `changelog/trainer-series.md` |
| `cryptography-labs/` | `changelog/cryptography-labs.md` |
| `encryption-labs/` | `changelog/encryption-labs.md` |
| `crypto-vuln-labs/` | `changelog/crypto-vuln-labs.md` |
| `security/` | `changelog/security.md` |
| `system-design-learn/` | `changelog/system-design-learn.md` |
| `system-design-labs/` | `changelog/system-design-labs.md` |
| `system-design-metrics/` | `changelog/system-design-metrics.md` |
| `system-design-activities/` | `changelog/system-design-activities.md` |
| `system-design-games/` | `changelog/system-design-games.md` |
| `digital-twin/` | `changelog/digital-twin.md` |
| `wild-rift/` | `changelog/wild-rift.md` |
| `history-timelines/` | `changelog/history-timelines.md` |
| `simulators/` | `changelog/simulators.md` |
| `prototypes/` | `changelog/prototypes.md` |
| `database-labs/` | `changelog/database-labs.md` |
| `cityu-tools/` | `changelog/cityu-tools.md` |
| `primer/` | `changelog/primer.md` |
| `projects/` | `changelog/projects.md` |
| `lessons-learned/` | `changelog/root-playground.md` |
| `index.html`, `CLAUDE.md`, shared infra | `changelog/root-playground.md` |

Always **also** add a one-line summary entry to `CHANGELOG.md` (root) under today's date.

### Tag reference

| Tag | Use when |
|---|---|
| `[feature]` | New file, section, or capability added |
| `[bug]` | Something was broken and is now fixed |
| `[ux]` | Layout, flow, or usability improvement |
| `[refactor]` | Code restructured without changing behavior |

### Entry format

```markdown
## YYYY-MM-DD

### [tag] Short title
- Bullet with specific detail
- Another bullet if needed
```

### Rules

1. Use today's date from `currentDate` context (or run `date +%Y-%m-%d`)
2. Add new entries at the **top** of the file (newest first)
3. Be specific — name the files, functions, or UI elements affected
4. If fixing a bug, include: **Symptom**, **Root cause**, **Fix**
5. If multiple sections were changed in one task, update each collection file
