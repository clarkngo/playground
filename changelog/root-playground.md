# Changelog — Root Playground & Global

Path: `/` (main `index.html`, `CLAUDE.md`, shared infrastructure)
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-04-21

### [feature] Seattle AI Literacy workshop page — added Sample Workshop #1 tab
- Updated `workshop-planning/seattle-ai-literacy.html` to add a new tab button and section: `Sample Workshop #1`
- Added full "AI on the Front Lines" workshop blueprint for SPD, SFD, and Seattle EMTs, including 4-part agenda (landscape, implications, prompt lab, policy roadmap)
- Included detailed hands-on activity (`Incident Report Refiner`) and materials checklist (slide deck, prompting cheat sheet, data privacy guide, feedback form)
- Added SPD compliance visual to the workshop tab (`assets/spd-use-case-diagram-2025-2026.png`) with contextual caption for prohibited vs conditional vs permitted AI use
- Added Washington AI policy framework visual (`assets/wa-ai-policy-framework.png`) with caption tying statewide priorities to Seattle workshop governance context
- Added click-to-zoom lightbox behavior for workshop images (open on image click, close via backdrop, close button, or Escape key)
- Added local source document `assets/Washington_AI_Blueprint.pdf` and linked it in the Resources tab as "Washington AI Blueprint (PDF)"
- Added university-partner 2-hour workshop variant in `tab-sample-workshop-1`, including Ground Truth context, Traffic Light policy table, Redline exercise flow, strategy module, and university preparation checklist
- Added EMS/Fire "Hands-on Sandbox" expansion to the sample workshop tab: Radio-to-PCR activity, syndromic deployment scenario, multi-agent dispatcher exercise, Private-RAG lab setup, policy green-light table, and Seattle AI Incident Card checklist
- Added a high-level overview and in-tab subsection navigation for `Sample Workshop #1` using anchor jump links (visuals, modules, activities, Private-RAG, policy table, incident card)
- Increased color contrast for the Sample Workshop #1 overview/navigation area (stronger tinted panel, brighter link chips, higher-contrast hover state)
- Added a new Pillar 3 alignment section in `Sample Workshop #1`: workforce upskilling summary, module-to-objective mapping, implementation gap-mender framing, and participation takeaway
- Refreshed `Sample Workshop #1` visual design to reduce reading fatigue: themed tab background, higher-contrast section labels, alternating card accent rails, richer table striping, and an at-a-glance meta summary strip
- Added a dedicated 60-minute NCyTE-style hands-on lab block in `Sample Workshop #1` with 3 tracks (Police Redline, EMS/Fire Structured Triage, Leadership Bias/Equity audit) and defined checkout deliverables

---

## 2026-04-19

### [feature] PM Dashboard for Predictive Maintenance team project
- New file: `team-project/predictive-maintenance/pm.html` — 5-tab interactive project management dashboard
- **Tab 1 — Dashboard:** per-member progress cards with live progress bars (driven by localStorage task state); overall completion bar; next-actions priority list
- **Tab 2 — Task Board:** interactive Kanban with 36 tasks across M1–M4; click-to-cycle status (To Do → In Progress → Done → To Do); state persists in localStorage; Reset All button
- **Tab 3 — Timeline:** 6-week Gantt-style table with per-member tasks per week, milestone markers, and key dependency table
- **Tab 4 — Risks:** 8-row risk register with severity/probability ratings and mitigations (class imbalance, CrossValidator runtime, StringIndexer label order, etc.)
- **Tab 5 — Meetings:** 4 accordion meeting entries (Kickoff, Data Handoff, Mid-project, Final Review) each with agenda and action item checkboxes persisted in localStorage
- Added PM Dashboard button link to `team-project/predictive-maintenance/index.html` header
- Bug fix: task-list text overflow in Team Action Items tab — switched from flex anonymous text node to JS-wrapped `.task-text` span with `min-width:0; flex:1; overflow-wrap:break-word`

### [feature] Team Projects section — Predictive Maintenance
- New top-level directory `team-project/` added under Classroom in sidebar nav and main `index.html`
- New file: `team-project/index.html` — collection index listing all team projects
- New file: `team-project/predictive-maintenance/index.html` — full 5-tab project workspace for the Big Data & ML course team project
- **Tab 1 — Domain Learning:** PdM maintenance types (reactive → predictive), AI4I 2020 dataset details sourced directly from Matzka IEEE AI4I 2020 paper, all 5 failure modes with exact trigger thresholds (TWF/HDF/PWF/OSF/RNF), feature importance findings, XAI concepts (explainable decision trees, LIME), class imbalance visualization (3.39% failure rate), asymmetric cost insight (false negative = 30× false positive)
- **Tab 2 — Team Action Items:** 4-member task boards (M1: Data Engineering Lead, M2: EDA & Analytics Lead, M3: ML Pipeline Engineer, M4: Paper & Presentation Lead) with numbered tasks and named deliverable notebooks; coordination checkpoint table
- **Tab 3 — Project Framework:** abstract, Spark ML pipeline diagram, 5-section framework table with owners, success criteria cards, known challenges with mitigations (class imbalance, RNF unpredictability, CrossValidator runtime)
- **Tab 4 — Course Alignment:** all 10 course chapters mapped to project tasks; quick-reference API table for every Spark/MLlib class used
- **Tab 5 — Paper Guide:** EDSIG/CONISAR structure (7 sections with page budgets), 3 required references with citation text

---

## 2026-04-18

### [feature] Workshop Planning section — AI Literacy for Seattle City Staff
- New section `workshop-planning/` added to `index.html` with sidebar nav link
- New file: `workshop-planning/seattle-ai-literacy.html` — planning document for a future AI literacy workshop targeting Seattle City staff
- Content: 6 tabs (Context, Audience, Key Themes, Workshop Formats, Open Questions, Resources)
- Extracts intelligence from City of Seattle 2025–2026 AI Plan (Pillar 3: Workforce Upskilling), AI Policy POL-211, and CTAB resources
- Audience segments: Officials, Managers, Front-line Employees, Technologists
- Theme priority matrix mapping 8 content themes to 4 audience tiers
- 4 workshop format options: Lightning Talk, Half-Day, Scenario-Based, Learning Series
- 9 open questions covering audience, format, and outcome decisions

---

## 2026-04-15

### [feature] Module 02 deliverables page with supporting evidence
- New file: `classroom-activities/data-governance/module-02-deliverables.html` — student submission page with 4 required screenshot deliverables (D1 Business Glossary, D2 Governance Policies, D3 Metadata Catalog, D4 Lineage Diagram) and D5 Reflection (medallion architecture visual, process steps, key learnings, roadblocks, final status checklist)
- Supporting evidence section with 5 supplementary screenshots: `00-databricks-raw-data.png`, `00-connection-test-success.png`, `00-custom-property-steward.png`, `00-governance-policies-overview.png`, `00-schema-column-level-tags.png`
- Created `module-02/submission/` directory for screenshot assets
- Wired deliverables link into `index.html` Module 02 card

### [feature] Data Governance classroom activities section homepage + Module 02 lab
- New file: `classroom-activities/data-governance/index.html` — section homepage listing Module 01 and Module 02 as navigatable cards with links to case study, deliverables, and lab guide
- New file: `classroom-activities/data-governance/module-02.html` — full lab guide for "GlobalTrust Bank: The Duplicate Records Crisis"; covers Part 1 (Databricks data quality: upload, profiling, 4 quality checks, 4 cleansing steps, optional Great Expectations validation) and Part 2 (OpenMetadata: metadata ingestion, business glossary, data classification tags, metadata cataloging, governance policies, lineage tracking, retention policies); includes sample dataset with highlighted DQ issues, code blocks with syntax highlighting, expected outputs table, 6 deliverables, and learning outcomes
- Updated `module-01.html` navbar and breadcrumb to link back to new section homepage
- Updated `module-01-deliverables.html` breadcrumb to link back to section homepage and Module 01
- JS syntax checks pass on all new files

### [feature] Add Module 2 card to homepage
- Added Module 2 collection card to the Class Notes section in `index.html`; bumped section count label from "1 module" to "2 modules"



### [feature] Data Governance Module 2 class notes
- New file: `class-notes/data-governance/module-02.html`
- 19 sections covering the full arc of Module 2: When Data Quality Fails, Six Dimensions of Quality, Source System Landscape, Enterprise Data Dictionary, Top-Down vs Bottom-Up dictionary building, Semantic Matching & NLP (addresses student question on same-concept different-name fields), Data Cataloging & Metadata Management (dual-layer metadata, policy decoupling, sensitivity shift, data residency, visibility vs access), OLTP→OLAP→Reporting integration patterns (batch/NRT/streaming comparison table), Data Assessment & Profiling, Data Normalization, Data Lineage Tracking, Data Transmission & ETL (tools table: Kafka, Spark, Airflow, Informatica, SAP, Oracle EDQ, Databricks), Key Management & Encryption (KMS, TPM), Identity & Access Management (conditional policies, no/partial/full access, four governance decisions table), Data Retention & Deletion, External Data Acquisition, Governance Tools Landscape (Collibra, Alation, Purview, Informatica, OpenMetadata, Apache Atlas, Databricks Unity Catalog), Automation at Scale, and The Bigger Picture (discoverability, security, accountability)
- Matches module-01.html design system exactly; JS syntax verified

## 2026-04-14

### [feature] AI4I 2020 dataset guide — domain knowledge section added
- New section in `deep-dives/ai4i-2020-dataset-guide.html`: **Domain Knowledge — Why the Data Looks the Way It Does**
- 6 subsections: CNC Milling Fundamentals (sensor-to-physics table), 5 Failure Modes in Depth (physical mechanism, operator observation, trigger rationale, cost of missing), Feature Correlations (4 callout blocks on torque/wear/temp/power relationships), Product Type significance (L/M/H table + modeling implication), Synthetic vs. Real data (side-by-side cards + generalization caveat), ML Intuition (asymmetric cost structure, alarm fatigue, why tree models dominate)
- New CSS: `.dk-prose`, `.dk-table`, `.dk-fm`, `.dk-callout` (blue/orange/purple/green), `.dk-row`, `.cost-grid`, `.cost-card`, `.dk-subhead`

## 2026-04-13

### [feature] AI4I 2020 Predictive Maintenance Dataset Guide — new deep dive
- New file: `deep-dives/ai4i-2020-dataset-guide.html` — reference guide for the Kaggle AI4I 2020 milling dataset
- Feature dictionary: all 14 columns with type, range, description, and modeling notes (leakage warnings, encoding notes)
- 5 failure mode cards (TWF, HDF, PWF, OSF, RNF) — each with case count, trigger condition, key features, and ML insight; color-coded by mode
- Class imbalance visual: bar charts for Machine Failure (96.6% / 3.4%) and per-mode breakdown
- Derived features table + Python code snippet: Power [W], Temp Delta [K], OSF Factor, Tool Wear Rate — with formulas and failure mode mapping
- 8 ML modeling considerations: class imbalance, data leakage, feature engineering priority, model choice, SHAP/XAI, multi-label vs binary, RNF handling, threshold calibration
- Dataset quick stats grid + citation box with links to Kaggle, UCI ML Repository, and the companion PdM primer
- `deep-dives/index.html`: added entry card (03) in Live Entries grid
- `index.html`: Deep Dives nav badge 1 → 2; section count "1 entry" → "2 entries"; AI4I card added to Deep Dives section; Primer nav badge 4 → 5

## 2026-04-12

### [ux] `classroom-activities/data-governance/module-01-deliverables.html` — timeline collapsed by default with expand affordance
- Starts collapsed; animation fires only on first expand via `hasPlayed` flag
- Header now a bordered pill button (`border: 1px solid #30363d`, hover → blue border + tinted bg)
- Always-visible summary row: three pills (6 phases, 20 steps, 3 blockers resolved) + italic "click to expand" hint that fades on header hover

### [ux] `classroom-activities/data-governance/module-01-deliverables.html` — collapsible timeline
- "How I Built This" header is now a click-to-toggle; chevron rotates ▼↔▶; body fades and slides via `max-height` + `opacity` transition
- Root cause of initial clipping bug: `position: static` on `.tl-body` let absolutely-positioned spine/dot children escape `overflow: hidden`; fixed with `position: relative`

### [refactor] `classroom-activities/data-governance/module-01/` — rename long case study folder
- Renamed `Module 01 Case Study Enterprise Data Governance Foundation/` → `module-01/` for kebab-case consistency
- Updated all 9 screenshot `src` and iframe `src` in `module-01-deliverables.html` (`module-01/submission/...`)

### [refactor] `classroom-activities/data-governance/module-01-deliverables.html` — move and rename deliverables page
- Moved from deep `submission/deliverables.html` to `data-governance/module-01-deliverables.html` alongside `module-01.html`
- Fixed all relative paths: navbar back-link (`module-01.html`), breadcrumb (`../../index.html`), 9 screenshot `src` and iframe `src` now prefixed with `Module 01 Case Study Enterprise Data Governance Foundation/submission/`

### [feature] `classroom-activities/data-governance/.../submission/deliverables.html` — process flow animation
- Added animated vertical timeline (6 phases · 20 steps) showing the full end-to-end activity workflow
- Phase 1: Env Setup (Docker, port conflict, resolution) · Phase 2: MySQL/Workbench Config (grants, default schema) · Phase 3: Airflow Ingestion (pipeline run, task logs, 0 records, filter fix) · Phase 4: Metadata Tagging (customers + orders, PII labels) · Phase 5: Ownership & Roles (steward + owner assignment) · Phase 6: Reflection (lessons-learned, deliverables html)
- CSS: `--pc`/`--pcr` custom properties for per-phase color; `tl-spine-fill` animates `height` via JS-set transition duration; alternating `node-r`/`node-l` grid; `::before` connectors; `.tag-badge` variants (err/fix/milestone)
- JS: IIFE with `PHASES` data array; DOM builder; staggered `setTimeout` at 260ms/step; Replay button resets + re-runs; stat label shows final count on completion

---

## 2026-04-09

### [feature] `index.html` — Classroom nav group and content sections
- Added "Classroom" sidebar nav section with two links: Class Notes and Class Activities (each badged with count)
- Added `data-section="class-notes"` main section: collection card linking to `class-notes/data-governance/module-01.html` with full search metadata tags
- Added `data-section="classroom-activities"` main section: collection card linking to `classroom-activities/data-governance/module-01.html`
- Both sections participate in existing sidebar filter and `/` keyword search

### [feature] `class-notes/data-governance/module-01.html` — Data Governance Module 1 class notes
- New top-level section `class-notes/` with subsection `data-governance/`
- 17-section scrollable class notes page covering: Data Mgmt vs Governance (DMBOK), data quality dimensions, data catalog & discovery, CIA triad in ETL, data lineage & auditability, MDM (4 implementation styles), 3 metadata types, enterprise architecture roles, 3 pillars of trust, and regulatory urgency
- All `<insert example>` placeholders from raw notes filled in: corrugated box manufacturing lifecycle, cross-department cascade (Widget X sales drop), Costco manual entry quality, attribution data integration (Facebook/Google/e-commerce), SOX-compliant audit trail, data splitting integrity risk, CityU EA diagram walkthrough, Thomson Reuters PDF ingestion
- Dark GitHub-style theme; sticky left-sidebar TOC with active-section highlighting via IntersectionObserver; print-safe styles; responsive collapse on mobile

---

## 2026-04-08

### [feature] `classroom-activities/data-governance/module-01.html` — Module 01 answered case study
- New section `classroom-activities/` with subsection `data-governance/`
- `module-01.html`: full answer key for "RetailCorp: The Data Chaos Challenge"
- Covers all 6 tasks: governance org chart, business glossary (4 terms), metadata catalog (Customers + Orders with PII tags), domain classification (3 domains + cross-domain joins), 3 governance policies, Databricks notebook walkthrough
- Embeds dataset preview from `Customers.xlsx` and `Orders.xlsx`
- Accordion expand/collapse per task; dark GitHub-style theme matching existing activities

---

## 2026-04-07

### [docs] `lessons-learned/bug-fixes.md` — splice indices after earlier HTML edit
- New pattern: stale `index()` anchors when a generator prepends CSS or other content before recomputing slice positions (HOS `generate_hos_02_10.py` handout bug)

### [refactor] `hos/full-stack-dev/` — CS628 track (Module 10 nested)
- `hos/full-stack-dev/index.html` — mini-hub; Module 10 at `hos/full-stack-dev/module-10/` with `../../shared.css` and `../../index.html` back link
- Dev Foundations HOS remains `hos/dev-foundations-activities-hos/`; main hub `hos/index.html` card points at `full-stack-dev/module-10/module-10-conversation-to-design.html`

### [ux] `hos/full-stack-dev/module-10/module-10-conversation-to-design.html`
- Footer credit: "Developed by Clark Ngo." (`hos-pdf-doc-credit`)

### [ux] HOS10A module page — PDF handout styling
- `hos/full-stack-dev/module-10/module-10-pdf-theme.css` + classes on `module-10-conversation-to-design.html`: solid navy course banner, centered hero block with blue rule, green **Tools Required** and blue **Deliverables** callouts, Slack thread (`#product-dev-chat` bar + Maria/Alex/Sam bubble tints), STC footer; `body.hos-pdf10-page` + paper column on gray backdrop
- **Section 4 Architecture Overview:** ASCII diagram moved from one `<p>` per line (broken layout) to `<pre class="hos-arch-diagram">` inside `table.hos-arch-diagram-table`; component table uses `<thead>`/`<th>`; generic PDF table CSS excludes `hos-arch-diagram-table`
- **Section 2 Requirements Gathering:** wrapped in `<section class="hos-req-gathering">`, task tables `hos-req-task`; colors aligned to handout — section title `#1f3864`, task header bar `#c55a11` / white text, body `#fde9d9` / `#111` text
- **5.6 App.js / React Router:** sample code moved from one `<p>` per line to `<pre class="hos-code-snippet">` with proper JSX indentation; `table.hos-code-block-table` + CSS exclusion from generic table striping

### [ux] `hos/shared.css` + `hos/index.html`
- Hub: `.hos-hub-cross` callout for CS445 Dev Foundations; hero covers CS628 + CS445
- Styles aligned to embedded Word **Office** theme from `HOS10A_AIFirst_ConversationToDesignDoc.docx`: accent1 `#156082`, dk2 `#0E2841`, accent2 `#E97132`, accent4 `#0F9ED5`, lt2 `#E8E8E8`; Segoe UI / Inter stack; light page background; first table as gradient title banner; `p.heading` with orange left rail; callout tables with alternating tint; hub hero card with orange accent edge

## 2026-03-27

### [feature] lessons-learned/prompting.md — git / multi-workstream prompting (stash vs PR order, primer vs Wireshark mix-up)
- New section: name paths for stash vs ship, explicit numbered steps, stash push vs pop, confirm `git stash list`

### [refactor] `.gitignore` — ignore `.DS_Store`; `git rm --cached` for four tracked `.DS_Store` files so they stay local only

### [bug] lessons-learned/bug-fixes.md — document `</script>` inside inline HTML scripts
- New section: HTML parser terminates `<script>` at first `</script>` even inside JS strings; use `<\/script>` in source

## 2026-03-25

### [feature] lessons-learned — 10 new entries from history review
- **bug-fixes.md**: hardcoded count string, script-before-DOM, canvas z-index overlap, threshold/label mismatch
- **feature-dev.md**: canonical template pattern for series (build one right, then copy)
- **refactor.md**: consolidate standalone files into folder, kebab-case naming convention
- **workflow.md**: `file://` vs HTTP server, archive before replacing, commit message discipline from day one

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
