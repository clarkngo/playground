# Changelog — Root Playground & Global

Path: `/` (main `index.html`, `CLAUDE.md`, shared infrastructure)
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

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
