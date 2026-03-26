# Changelog — Root Playground & Global

Path: `/` (main `index.html`, `CLAUDE.md`, shared infrastructure)
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-25

### [feature] `index.html` — Lessons Learned section added
- New sidebar nav entry "🧠 Lessons Learned" under Meta group; collection card + 5 direct file-card shortcuts
- Links to viewer, prompting, bug-fixes, feature-dev, ux, and workflow topics

### [feature] `lessons-learned/workflow.md` — new topic: Claude Code Workflow
- Covers: branch/PR/merge cadence, plan mode, verify-one-then-batch, context window management, parallel vs sequential tool calls, git stash mid-session, CLAUDE.md purpose, commit message quality

### [feature] CLAUDE.md — workflow.md added to lessons-learned post-write checklist

### [feature] CLAUDE.md — post-write checklist now includes lessons-learned update step
- Added 5-line checklist item: after any change, check if it warrants updating `bug-fixes.md`, `feature-dev.md`, `ux.md`, `refactor.md`, or `prompting.md`

### [feature] lessons-learned/prompting.md — new entry: Ask Claude to maintain living documentation
- Documents the "should Claude do X the same way it does Y" prompting pattern
- Explains why analogy-based framing is more effective than issuing a direct rule

---

### [bug] `fetch()` failed for .md files on GitHub Pages
- **Symptom:** `Could not load root-playground.md: Failed to fetch` on GitHub Pages
- **Root cause:** GitHub Pages runs Jekyll by default; Jekyll intercepts `.md` files, transforming or blocking them so `fetch()` receives HTML or a 404 instead of raw markdown
- **Fix:** Added `.nojekyll` at repo root — disables Jekyll entirely, all files served as static assets

### [feature] Created `changelog/index.html` — visual changelog viewer
- Single-page markdown viewer (marked.js CDN) matching lessons-learned viewer style
- Sidebar grouped by category (Security, System Design, Content, Tools & Misc); home card grid with all 21 sections
- Tag badges `[feature]` `[bug]` `[ux]` `[refactor]` rendered as colored inline pills (green/red/blue/purple)
- URL param `?f=filename.md` for deep links; browser back/forward navigation supported

### [feature] Created `lessons-learned/` section — knowledge base for patterns and insights
- `lessons-learned/index.html` — single-page markdown viewer using marked.js (CDN); sidebar nav + home card grid; supports URL param `?f=filename.md` for deep links; works with `python3 -m http.server`
- `lessons-learned/feature-dev.md` — Set-based tracking, default-active seeding, 2×2 combo grid, localStorage versioning, badge count sync
- `lessons-learned/bug-fixes.md` — init order (saveState before loadState), missing re-render after loadState, default tab seeding, first-click objective completion, JS syntax errors causing blank pages
- `lessons-learned/ux.md` — overlay placement (bottom-right DOM order), objectives ordered to match page flow, choice vs auto-execute, demo null start state, export success feedback
- `lessons-learned/refactor.md` — global sed replace across N files, boolean→Set refactor, centralizing objective evaluation, removing hardcoded defaults
- `lessons-learned/prompting.md` — reference file beats description, symptom-first, batch after verify, "no + reference" redirect, compound requests as lists, planning mode

### [feature] CLAUDE.md — added Prompting Guidance section
- Claude now auto-suggests clearer prompt phrasing when it detects ambiguity (vague layout references, missing reference files, bundled tasks, presumed-fix mismatch)
- Inline suggestion format defined; only triggers when rewrite would have meaningfully changed interpretation

### [feature] CLAUDE.md — added JS State Pattern Checklist
- New section after Post-Write Checklist covering 6 state-pattern checks: saveState includes new var, loadState restores it, re-render called after load, init order guard, default-active seeding, badge count matches checks.length
- Added `lessons-learned/` → `changelog/root-playground.md` to the changelog routing table

---

## 2026-03-24

### [feature] Global attribution — metadata + copyright footer on all 353 HTML files
- **Metadata tags** (`author`, `copyright`) added to all 353 files for document attribution
- **Minimal footer** (© YYYY Clark Ngo, auto-updating) added to all 328 content files (non-index.html)
- **Lab homepages** (15 index.html files) retain full footer with LinkedIn link
- **Rationale:** Individual files may be deployed/shared on different platforms; metadata + minimal footer ensures proper attribution

### [feature] Copyright footer added to all lab homepages (10 subfolders)
- Auto-updating year via `new Date().getFullYear()` — no manual maintenance needed
- LinkedIn link (`linkedin.com/in/clarkngo`) with hover state
- Applied to: `coding-agents/`, `crypto-vuln-labs/`, `cryptography-labs/`, `encryption-labs/`, `prototypes/security/cy615/`, `security/`, `system-design-labs/`, `system-design-learn/`, `trainer-series/`, `case-studies/`
- Styling adapts: dark GitHub theme for dark-background labs; Tailwind colors for `system-design-learn` (light theme)

### [bug] Copyright year script executing before DOM element existed
- **Symptom:** Year span displayed empty (no year shown)
- **Root cause:** `document.getElementById('copyright-year')` was called inside the main `<script>` block, before the `<footer>` HTML was rendered
- **Fix:** Moved the copyright year script to a separate `<script>` tag placed **after** the footer HTML, ensuring the element is in DOM before the script runs
- **Files:** `crypto-vuln-labs/`, `cryptography-labs/`, `system-design-labs/`, week1-lab, week2-lab (all had script in wrong position)

---

## 2026-03-23

### [feature] CLAUDE.md created — agent diagnostic instructions
- **Why:** Lab 09 canvas was blank due to a JS syntax error (apostrophes in single-quoted strings). It took too long to diagnose because behavioral debugging was tried before syntax checking.
- **Contents:**
  - JS syntax check command: `sed -n '/<script>/,/<\/script>/p' <file> | grep -v '<.script' | node --check /dev/stdin`
  - Debugging order: (1) syntax check → (2) check globals exist → (3) console logs → (4) manual draw test → (5) runtime/timing issues
  - Post-write checklist: syntax check passes, no console errors, key elements visible
- **Common pitfall documented:** Single-quoted strings with apostrophes (`it's`, `don't`, `can't`) — use backtick template literals instead

### [feature] Case Studies & Trainer Series added to main index.html
- New sidebar nav section "Case Studies & Training" with two links and badge counts (10 each)
- Full content sections added: `data-section="case-studies"` and `data-section="trainer-series"`
- 11 cards each (hub card + 10 content cards) with section groups, thumbnails, and tags
- Inserted before the Simulators section in the content layout

### [feature] Coding Agents section updated
- Badge count updated to 9
- Lab 09 card added to main index.html coding-agents content section
