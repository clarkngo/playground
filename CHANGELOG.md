# Playground Changelog

All changes across the project, newest first.
Detailed entries are in `changelog/<collection>.md`.

Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-04-12

### [bug] `classroom-activities/data-governance/module-01.html` — fix org chart connector lines
- Replaced single centered `org-vline` between rows with proper branching connectors: `org-down-3` (CDO → 3 Owners), `org-vline-3` (3 parallel Owner → Steward lines), `org-up-3` (3 Stewards → Data Consumers)
- All nodes now have visible connecting lines; Customer and Marketing columns no longer appear disconnected

---

## 2026-04-09

### [feature] NCyTE AI for Educators Workshop 2025 — conference notes + STC strategy
- New notes: `conference-notes/ncyte-workshop-2025/index.html` — 7 sections (agenda, CO-STAR, grade weight flip, C2PA, QTI, NotebookLM, tools, synthesis, reflections); new applied doc: `stc-strategy/ncyte-workshop-2025/index.html` — 6 sections mapping workshop to CS445, CS628, BSAI, and NCyTE partnership opportunity; both index pages and root `index.html` updated (badges 1→2)

### [feature] `stc-strategy/` — new collection applying external insights to CityU STC
- New hub: `stc-strategy/index.html`; first document: `stc-strategy/higher-education-summit-2026/index.html` — 6 sections mapping summit insights to BSAI, MSAI, CS445, CS628, and the AI committee; includes validated practices, gaps, 8 opportunities, 7 open questions, and 9 prioritized next steps

### [feature] `conference-notes/` — new section with Higher Education Summit 2026 notes
- New hub: `conference-notes/index.html`; new notes: `conference-notes/higher-education-summit-2026/index.html` — 12 sections covering keynote, 2 panels, 3 breakout sessions, closing discussion, synthesis, and personal reflections; root `index.html` updated with nav link and card

### [feature] `index.html` — Class Notes and Class Activities sidebar + sections
- Added "Classroom" nav group in sidebar with links for Class Notes (badge 1) and Class Activities (badge 1)
- Added `data-section="class-notes"` section: card for `class-notes/data-governance/module-01.html`
- Added `data-section="classroom-activities"` section: card for `classroom-activities/data-governance/module-01.html`
- Both sections searchable via existing `/` search filter

### [feature] `class-notes/data-governance/module-01.html` — Data Governance Module 1 class notes
- 17-section notes page: DMBOK definitions, data quality, catalog/discovery, CIA triad in ETL, lineage, MDM (4 styles), 3 metadata types, EA roles, 3 pillars of trust, regulatory urgency; all raw-note placeholders filled with concrete examples

---

## 2026-04-08

### [feature] `classroom-activities/data-governance/module-01.html` — Module 01 answered case study
- Full answer key for "RetailCorp: The Data Chaos Challenge": org chart, glossary, catalog, domains, policies, Databricks notebook

---

## 2026-04-07

### [feature] `primer/industry/enterprise-architecture/` — Enterprise Architecture industry primer
- 12 tabs: TOGAF/ArchiMate/C4, extended node–edge process flows, governance, data architecture chains; hub card + nav link in `primer/index.html`

### [feature] `hos/dev-foundations-activities-hos/` — verbatim PDF text in curated HOS pages
- `_pdf_extracts/hos04b_full.txt` + `hos_verbatim_pdf_append.py`; collapsible full step-by-step extraction under each HOS02–10 handout section

### [feature] `hos/dev-foundations-activities-hos/` — HOS03A–HOS10A curated handouts
- `build_hos_curated_03_10.py` splices structured PDF sections + figure grids; `generate_hos_02_10.py` skips modules 02–10; eight workflow HTML files updated

### [feature] `hos/dev-foundations-activities-hos/` — HOS02A curated handout (HOS01 pattern)
- `02-git-repositories-refactoring-hos-workflow.html` — replaced generated `<pre class="hos-pdf-full-raw">` block with structured `<section class="hos-pdf-source">`: metadata, Before You Start, uploads, Key Concepts, Sections 1–4 with `<h3>` steps, commands in `<span class="hos-cmd">`, code in `<pre class="hos-pre-df">`, 31 figures placed by section; `.hos-pdf-note` for PDF callouts; scenario box un-escaped; `generate_hos_02_10.py` skips module 02; `build_hos02_curated_handout.py` reapplies splice after template edits

### [bug] `hos/dev-foundations-activities-hos/` — HOS02–10 layout + HOS04 PDF merge
- **Symptom:** Broken `pdf-header` / missing lab header on generated pages; HOS04 needed both database PDFs. **Root cause:** Handout splice indices were taken from the template *before* injecting `.hos-pdf-full-raw` CSS, so `start` pointed into the middle of `<div id="pdf-header" class="pdf-only">`. **Fix:** Compute `start`/`end` after the inject; merge `HOS04A - Databases - without Docker.pdf` text + `hos04b-pdf-figures/` via `build_handout` alt block; spine comment uses `m["hos"]`.
- `lessons-learned/bug-fixes.md` — documented stale `index()` / splice after earlier generator edit pattern.

### [feature] `hos/dev-foundations-activities-hos/` — HOS02A–HOS10A generated activities + hub
- Nine HTML pages from CS445 PDFs (Git, Flask, databases, pytest, UML, security, CI/CD, Azure Functions, AWS Lambda): full text extract + figures, shared drag/drop + dual simulator shell
- `generate_hos_02_10.py` — fixed prompt-block regex (three closing `</div>`) and `esc_html_body` so reference labels are not double-entity-encoded
- `index.html` — cards for modules 02–10

### [feature] `hos/dev-foundations-activities-hos/` — HOS01A PDF screenshots as PNG assets
- `hos01a-pdf-figures/` (17 images) inlined in handout section

### [feature] `hos/dev-foundations-activities-hos/01-github-codespaces-hos-workflow.html` — full HOS01A PDF handout inline
- Complete cookbook copy + Dockerfile + print-friendly styles

### [refactor] `hos/full-stack-dev/` — CS628 track; Module 10 at `full-stack-dev/module-10/`
- Mini-hub `hos/full-stack-dev/index.html`; `hos/index.html` card + `.hos-hub-sublink`; prior `hos/module-10/` path retired
- Dev Foundations HOS unchanged at `hos/dev-foundations-activities-hos/`; `shared.css` includes `.hos-hub-cross`

### [feature] `hos/dev-foundations-activities-hos/` — HOS01A GitHub Codespaces workflow activity + hub
- PDF-infused drag/drop sequence from CS445 handout; dual simulator; playground index card points to `hos/…`

### [refactor] deep-dives — removed `docs/ads-platform/`; mind map + video list on `ebay-ads` hub
- Deleted legacy `docs/ads-platform/` (old tabbed guide, wiki `.docx` exports, markdown notes); canonical content remains `deep-dives/ebay-ads/`
- `ebay-ads/index.html` — Reference materials: `ads-platform-mind-map.png`, thirteen YouTube bookmarks (from former `ebay-internals.md`); `shared.css` — `.ref-lead`, `.mind-map-fig`, `.video-ref-list`

### [ux] `hos/module-10-conversation-to-design.html` — footer credit (Clark Ngo)

### [ux] `hos/module-10-conversation-to-design.html` — 5.6 App.js sample indented in `<pre class="hos-code-snippet">`

### [ux] `hos/module-10-conversation-to-design.html` — Section 2 Requirements Gathering styled (orange task headers, peach bodies, navy section title)

### [ux] `hos/module-10-conversation-to-design.html` — Section 4 architecture ASCII diagram fixed (`pre` + diagram table); component table header row semantic/styling

### [ux] `hos/module-10-conversation-to-design.html` — styles matched to CityU HOS10A PDF (callouts, Slack bubbles, navy banner)

### [ux] `hos/shared.css` — HOS10A Word Office theme colors (teal `#156082`, navy `#0E2841`, orange `#E97132`, blue `#0F9ED5`); light paper UI, title banner, section heading rails; recreated `hos/index.html`

### [refactor] deep-dives — `spark-ebay-supplement.html` (renamed); removed "classroom" wording from deep-dives hub, ebay-ads links, Spark supplement page, and CSS class names

### [ux] deep-dives/ebay-ads — interactive process node flow (placement path + measure/settle) on fundamentals section; `ads-pipeline-sim.js` `RETAIL` scenarios

### [ux] deep-dives/ebay-ads — removed disclaimer callouts; added "How ecommerce ads work" on hub; dropped reader tips and educational footers site-wide in that guide

### [feature] Industry primers — Data Governance tab (all 17 industries)
- New tab after Evolution: O'Reilly-style governance lenses (ownership, policy, metadata, quality, privacy, lifecycle), link to `data-gov-book/` supplement; nav/progress now 12 sections; `primer/tools/inject_datagov.py` + `datagov_data.py`; `primer/index.html` coverage labels updated to 12/12 for industry cards

### [ux] deep-dives/ebay-ads — interactive pipeline flow sims (`ads-pipeline-sim.js`, scenario buttons not dropdowns)

### [ux] deep-dives/ebay-ads — cooler high-contrast theme; CSS motion on Ch 3 tech cards & Ch 4 workflow pipelines (respects reduced-motion)

### [refactor] deep-dives/ebay-ads/ — hub + `ch/*.html` chapters; `ebay-ads-platform.html` redirects; `shared.css` (spark-book-style nav)
- Split former single-file guide into `deep-dives/ebay-ads/index.html` + five chapter pages; updated `deep-dives/index.html` card href; note in `docs/ads-platform/ebay-internals.md`

### [feature] eBay Ads Platform — Deep Dive system architecture guide (spark-book styled)
- New `deep-dives/ebay-ads-platform.html` — comprehensive 5-tab guide covering ad programs, tech stack (Kafka/Flink/Spark/Hadoop/ClickHouse/Prometheus/Sherlock/Control Center), A/B testing, and SRE operations playbook; integrated into deep-dives collection as entry #02

### [feature] Add Book Supplements section to playground home page
- `index.html` — new "Book Supplements" nav section + content section with cards for `spark-book/` (Learning Spark) and `data-gov-book/` (Data Governance: The Definitive Guide); both grouped as a collection with chapter counts and search tags

### [feature] Data Governance: The Definitive Guide — interactive book supplement (Phase 1)
- `data-gov-book/` — 3-page interactive companion: hub + Ch 1 (maturity model + 5-pillar trust simulator) + Ch 2 (role explorer + RACI decision matrix)

### [feature] Learning Spark interactive book supplement — Phase 1
- `spark-book/` — 4-page interactive companion to "Learning Spark 2nd Ed.": hub + Ch 1 (job flow animator + cluster topology), Ch 2 (lazy eval DAG builder), Ch 3 (partition layout visualizer with cost model)

## 2026-04-06

### [feature] node-flow-animator skill + test prototypes
- New `node-flow-animator` Claude skill — generic DOM-based process-flow animation build tool (node row, packet dots, phase strip, log panel, outcome grid); covers network security, system design, CI/CD, business process, data pipeline domains
- `prototypes/node-flow-test.html` — system design request flow (3 scenarios: cache miss/hit, timeout)
- `prototypes/spark-flow-test.html` — Apache Spark job flow (3 scenarios: batch WordCount, Kafka streaming, executor OOM)

## 2026-04-03

### [feature] Primer — reorganized into industry/ + technology/ subfolders; added Real-Time Systems technology primer (9 tabs)
- 17 existing industry primers moved to `primer/industry/`; all paths updated
- New `primer/technology/` category with `shared.css` stub and Technology Primer section on index page
- `primer/technology/real-time-systems/index.html` — 9 tabs: RTOS kernels, scheduling theory, embedded hardware, safety standards, major players (VxWorks, QNX, FreeRTOS, Zephyr), workflows, trends (RISC-V, TSN, mixed-criticality), monetization, and evolution timeline

### [feature] Deep Dives series — Wild Rift entry 01
- New series `deep-dives/` for cross-domain technology internals deep dives
- `deep-dives/index.html` — hub with animated network-graph canvas, coming-soon cards for ServiceNow, OpenSearch, SAP
- `deep-dives/01-wild-rift.html` — 6-tab deep dive: game engine internals, matchmaking (Glicko-2, MMR vs rank, interactive queue slider), tech stack, F2P business model, key numbers
- Root `index.html` updated: nav link + section block added

---

## 2026-04-02

### [feature] Conversation to Design — 10-activity requirements engineering series
- New `conversation-to-design/` collection: 10 self-contained HTML activities teaching actors/FRs/NFRs/open questions/design-doc/architecture from realistic team conversations (Slack, email, Jira, Discord)
- Root `index.html` updated with sidebar nav link and section block

### [feature] ByteByteGo-style course platform prototype
- `prototypes/course-platform.html` — full course lesson page prototype with sidebar nav, FREE/locked chapter badges, progress bar, Mermaid architecture diagrams, multi-tab code block with copy, Q&A interview simulation, trade-off table, callout boxes, and bottom chapter nav

### Dev Foundations Activities
- `[ux]` All 10 activities — simulator dropdown replaced with two always-visible side-by-side panels, each with its own Simulate button
- `[ux]` All 10 activities — Validate Architecture and Export PDF buttons normalized to identical placement (toolbox column) and label text across all activities

---

## 2026-04-01

### Dev Foundations Activities
- `[feature]` Activities 02–10 live — full collection of 10 system design sequencing activities complete (Git, REST APIs, Databases, Testing, Architecture, Security, CI/CD, Microservices, Resiliency)
- `[feature]` `dev-foundations-activities/index.html` — homepage with 10-card grid, "How It Works" section, and answer key banner
- `[feature]` `answer-key.html` — all 10 modules updated to Live with correct sequences and distractor chips
- `[feature]` Created `dev-foundations-activities/` collection — Activity 01 (Container Runtime Architecture) live with GitHub dark theme, 7 correct layers + 4 VM distractors, count-mismatch validation
- `[feature]` `index.html` — Added "Dev Foundations" sidebar nav entry and 10-activity section

---

## 2026-03-31

### Cryptography Labs
- `[ux]` Lab 10 — Demo 4 renamed to "📝 Assessment — Protocol Security True/False"
- `[feature]` Lab 10 — Assessment now requires all 20 questions answered (was ≥15 correct)

### Cryptography Labs
- `[ux]` Lab 10 — Removed all "Capstone" wording from navbar, scenario, Demo 4, reflection, and print summary
- `[feature]` Lab 10 — Demo 3 ZK proof now requires all 8 rounds to complete objective (was 5)

## 2026-03-30

### Primer
- `[feature]` Added Data Architecture & Flows + Failure Modes & Incidents tabs to all 9 remaining primers (maritime, oil, telecom, esports, sports, restaurant, video-game-retail, video-platform, fishing) via direct Python injection — no subagents
- `[feature]` Created `changelog/token-usage.md` — session-by-session token consumption tracking with cost estimates and usage guidance

## 2026-03-27

### [ux] deep-dives/ebay-ads — drop "CIA-style" labels on pipeline sims (neutral copy)

### [feature] deep-dives — eBay Spark primary-source supplement + home hub refresh
- New `deep-dives/ebay-ads/spark-ebay-supplement.html` — digest of two eBay Innovation Spark articles (2014 adoption vs 2021 SQL engine), comparison table, discussion prompts; linked from `ebay-ads/index.html`, Ch 3 tech stack, and `deep-dives/index.html` supplements grid
- `deep-dives/index.html` — hero copy + Primary-source supplements section; `shared.css` — `.supplement-prompt-list` styles

### [ux] deep-dives/ebay-ads — `glossary.html` reader guide + jargon tables; hub onboarding box; chapter tips linking to glossary

### [bug] deep-dives/ebay-ads Ch 3 — fixed architecture SVG; now matches eBay Spark SQL / Thrift gateway article (was misleading telemetry fan-in)

### [ux] deep-dives/ebay-ads — more node-flow animations + SVG architecture diagrams (Ch 1–3, 5); `ads-pipeline-sim.js` scenario packs for overview, RTB, observability, incident paths

### [feature] deep-dives/ebay-ads Ch 3 — anomaly detection implementation + control center requirements + stack map
- `ch/03-tech-stack.html` — expanded Sherlock section (pipeline, streaming vs batch, requirements, ads quirks); Control Center requirements (product/UX, integration, safety); six-row stack table; `hub/index.html` Ch 3 blurb; `ch/05-operations.html` cross-link to `#control-center-stack`

### [refactor] lessons-learned/prompting.md — added multi-workstream git prompting pattern (stash paths, PR scope, avoid primer vs fix inversion)

### [refactor] `.gitignore` — ignore `.DS_Store`; removed 4 tracked macOS metadata files from the index (root, cryptography-labs, passport-shop, retro-game)

### [bug] simulators/wireshark-simulator — fixed broken page: embedded sample HTML contained `</script>`, which terminated the main script; escaped tag and used template literal for multi-line body

### [refactor] lessons-learned/bug-fixes — documented inline-HTML `</script>` string pitfall (related Wireshark simulator root cause)

### [feature] primer/healthcare — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); progress bar expanded to 11 dots

### [feature] primer/insurance — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); progress bar expanded to 11 dots

### [feature] primer/logistics — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); progress bar expanded to 11 dots

### [feature] primer/manufacturing — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); progress bar expanded to 11 dots

### [feature] primer/ai-infrastructure — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); shared.js updated to compute "of N" dynamically from progress-dot count

### [feature] primer/edtech — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); progress bar and showTab override updated to 11 tabs

### [feature] primer/ecommerce — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); progress bar and showTab override updated to 11 tabs

### [feature] primer/fintech — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents); progress bar and showTab updated to 11 tabs

## 2026-03-26

### [ux] primer/video-platform, ecommerce, edtech, ai-infrastructure, fintech — rewrote tab-evolution: Foundational Works moved to top, card-grid timelines replaced with new alternating tl-item timeline structure

### [ux] primer/sports, restaurant, fishing, telecom — rewrote tab-evolution: Foundational Works moved to top, card-grid timelines replaced with new alternating tl-item timeline structure

### [ux] primer/oil, healthcare, esports, video-game-retail — rewrote tab-evolution: Foundational Works moved to top, card-grid timelines replaced with new alternating tl-item timeline structure

### [ux] primer/insurance, manufacturing, maritime, logistics — rewrote tab-evolution: Foundational Works moved to top, card-grid timelines replaced with alternating tl-item timeline structure; manufacturing card-grid foundations converted to metrics-table

### [refactor] primer/fintech — migrated from data-tab + activateTab system to canonical showTab system; replaced ~450-line inline style block with shared.css; replaced inline script with shared.js; all 9 tab sections, glossary, player cards, metrics, workflows, and trends converted to canonical classes

### [refactor] primer/ai-infrastructure — migrated from data-tab system to canonical showTab system; shared CSS/JS; all 9 tab sections converted to tab-section divs with canonical IDs

### [refactor] primer/edtech — migrated from old data-tab system to canonical showTab system; shared CSS/JS; all components converted to canonical classes

### [refactor] primer/ecommerce — migrated from old data-tab system to canonical showTab system; shared CSS/JS; 9 canonical tabs

### [ux] primer/index.html — remove all Live/New status badges from hub cards and sidebar
### [refactor] primer — extract shared.css and shared.js; eliminate ~1,400 lines of duplication across 13 primers

### [bug] primer/fintech — Market Dynamics and Evolution tabs both broken; three fixes applied

### [feature] primer/telecom — Evolution & Foundations tab (Tab 9) added; 8-era timeline + 6 foundational works; JS PASS

### [feature] primer/index.html — manufacturing card + nav link added; all 17 primers updated to 9 / 9 sections

### [feature] CLAUDE.md — primer-building instructions updated to 9-tab structure with Evolution & Foundations spec

### [feature] primer — Evolution & Foundations tab added to logistics, video-platform, oil, fishing
- Added Tab 9 (`id="tab-evolution"`) with 8 timeline cards + foundational works table to all four files; all JS syntax checks pass

### [feature] primer — Evolution & Foundations tab added to healthcare, esports, video-game-retail, insurance
- Added Tab 9 (`id="tab-evolution"`) with 8 timeline cards + foundational works table to all four files; all JS syntax checks pass

### [feature] Manufacturing — Corrugated Packaging industry primer
- Created `primer/manufacturing/index.html` — 9-tab primer covering containerboard mills, box plants, e-commerce packaging, OCC recycling; IP, Smurfit WestRock, PCA; 20 glossary terms, 3 workflows, 9 timeline milestones, 8 foundational standards

### [feature] primer — Evolution & Foundations tab added to restaurant, sports, maritime
- 8-card historical timeline + foundational works table in each; all JS syntax checks pass

### [feature] primer — Evolution & Foundations tab added to fintech, ecommerce, edtech, ai-infrastructure
- 8-card historical timeline + foundational works table in each; all JS syntax checks pass

### [feature] CLAUDE.md — Industry Primer build instructions added
- Added "Building a New Industry Primer" section covering: canonical template (insurance), 8-tab structure, required content per tab, JS rules (no apostrophes, showTab/toggleGloss patterns), header block HTML, post-creation checklist, and changelog routing
- Added `primer/` → `changelog/primer.md` to the changelog routing table

### [feature] primer/index.html — 6 new industry cards + nav links (maritime, telecom, logistics, video-platform, oil, fishing)
- Added 6 industry cards with `data-search` attributes and sidebar nav links; updated all card section counts to 8 / 8

### [feature] Telecommunications industry primer
- Created `primer/telecom/index.html` — 8-tab primer featuring T-Mobile, AT&T, Verizon; 20 glossary terms (ARPU, churn, 5G NR, spectrum, MVNO, FWA, eSIM, Open RAN), 3 workflows (subscriber onboarding, 5G site build, enterprise private 5G sale)

### [feature] Logistics & Supply Chain industry primer
- Created `primer/logistics/index.html` — 8-tab primer featuring Maersk integrated logistics, DHL, UPS, FedEx, Amazon; 20 glossary terms (3PL, TMS, WMS, drayage, OTIF, cross-docking, control tower), 3 workflows (inbound warehouse receipt, e-commerce fulfillment, freight broker load execution)

### [feature] Video Platforms & Streaming industry primer
- Created `primer/video-platform/index.html` — 8-tab primer featuring YouTube, Netflix, TikTok; 20 glossary terms (CPM, RPM, watch time, CTR, algorithm, SVOD/AVOD/FAST, Content ID, CTV, Super Chat), 3 workflows (YouTube upload lifecycle, streaming content licensing, YouTube ad campaign setup)

### [feature] Oil & Gas industry primer
- Created `primer/oil/index.html` — 8-tab primer featuring ExxonMobil, Chevron, Saudi Aramco, SLB; 20 glossary terms (Brent/WTI, upstream/midstream/downstream, proved reserves, lifting cost, fracking, OPEC+, crack spread, CII), 3 workflows (shale well drilling, crude oil trading, refinery crude procurement)

### [feature] Commercial Fishing & Aquaculture industry primer
- Created `primer/fishing/index.html` — 8-tab primer featuring Mowi, Trident Seafoods, Alaska pollock; 18 glossary terms (IUU, MSC/ASC, TAC, ITQ, bycatch, FIFO ratio, FCR, sea lice, traceability), 3 workflows (Alaska pollock season, salmon farm grow-out, seafood restaurant supply chain)

### [feature] Market Dynamics tab added to ecommerce, edtech, and ai-infrastructure primers
- Added 8th tab button + Market Dynamics section to `primer/ecommerce/index.html`, `primer/edtech/index.html`, and `primer/ai-infrastructure/index.html`; 5 pain-point cards + 6 monetization models each; JS syntax checks pass

### [feature] Market Dynamics tab content added to esports, video-game-retail, and maritime primers
- Added `tab-dynamics` section HTML to `primer/esports/index.html`, `primer/video-game-retail/index.html`, and `primer/maritime/index.html` — 5 pain-point cards + monetization table each; JS syntax checks pass

### [feature] Market Dynamics tab content added to insurance, restaurant, sports primers
- Added `#tab-dynamics` section to `primer/insurance/index.html`, `primer/restaurant/index.html`, and `primer/sports/index.html` — 5 industry-specific pain-point cards + Monetization Models table in each; JS syntax checks passed

### [feature] Market Dynamics section added to healthcare and fintech primers
- Added Market Dynamics tab content to `primer/healthcare/index.html` and `primer/fintech/index.html` — 5 industry-specific cards + Monetization Models table in each

### [feature] Maritime & Shipping industry primer
- Created `primer/maritime/index.html` — 7-tab primer featuring Maersk, MSC, CMA CGM; 20 glossary terms (TEU, B/L, SCFI, demurrage, CII, Incoterms), 3 workflows (container booking to vessel load, port call ops, freight rate negotiation cycle)

## 2026-03-25 (primer batch 2)

### [feature] Insurance industry primer
- Created `primer/insurance/index.html` — 7-tab primer featuring Allstate, State Farm, Geico, Progressive; 18 glossary terms, 3 workflows (auto quote-to-bind, claims FNOL-to-settlement, actuarial rate filing)

### [feature] Restaurant & Food Service industry primer
- Created `primer/restaurant/index.html` — 7-tab primer featuring ramen shop + poke shop; 16 glossary terms (FOH/BOH, prime cost, RevPASH, menu engineering, ghost kitchen), 3 workflows

### [feature] Sports & Athletics industry primer
- Created `primer/sports/index.html` — 7-tab primer featuring NBA; 15 glossary terms (salary cap, Bird Rights, EPM/RAPTOR, Second Spectrum), 3 workflows (draft scouting, in-game coaching, cap construction)

### [feature] primer/index.html — 3 new industry cards + nav links (insurance, restaurant, sports)
- Added insurance, restaurant, sports cards with searchable `data-search` attributes and sidebar nav links with "New" badges

## 2026-03-25 (primer batch)

### [feature] Healthcare & MedTech industry primer
- Created `primer/healthcare/index.html` — 7-tab primer featuring Stryker/Mako, FDA pathways, GPO/VAC procurement, MedTech value chain, 25 glossary terms, 3 workflows

### [feature] eSports & Competitive Gaming industry primer
- Created `primer/esports/index.html` — 7-tab primer featuring Wild Rift / WCS SEA, tournament production, org sponsorship lifecycle, 18 glossary terms, 3 workflows

### [feature] Video Game Retail industry primer
- Created `primer/video-game-retail/index.html` — 7-tab primer featuring GameStop, trade-in economics, digital storefront pipeline, 18 glossary terms, 3 workflows

### [feature] primer/index.html — 3 new industry cards + nav links
- Added Healthcare, eSports, and Video Game Retail cards to hub grid; added sidebar nav links with New badges

## 2026-03-25

### Lessons Learned
- `[feature]` 10 new entries from project history review — hardcoded counts, script-before-DOM, canvas z-index, threshold/label mismatch, series template pattern, folder consolidation, kebab-case naming, file:// vs HTTP server, archive before replace, commit message discipline

### Root / Global
- `[feature]` `index.html` — Lessons Learned section added with sidebar nav, collection card, and 5 topic shortcuts
- `[feature]` `lessons-learned/workflow.md` — new topic: Claude Code Workflow (branch/PR cadence, plan mode, context management, CLAUDE.md)
- `[feature]` CLAUDE.md — workflow.md added to lessons-learned post-write checklist
- `[feature]` CLAUDE.md — post-write checklist now prompts lessons-learned update alongside changelog
- `[feature]` lessons-learned/prompting.md — new entry on analogy-based prompting pattern ("do X the same way you do Y")
- `[bug]` Added `.nojekyll` at repo root — fixes `fetch()` failing for `.md` files on GitHub Pages (Jekyll was intercepting them)
- `[feature]` Created `changelog/index.html` — visual markdown viewer for all 21 changelog files; tag badges colored inline (feature/bug/ux/refactor); sidebar grouped by category

### Lessons Learned (new section)
- `[feature]` Created `lessons-learned/` — markdown knowledge base with single-page viewer (marked.js CDN); 5 category files: feature-dev, bug-fixes, ux, refactor, prompting

### Root / Global
- `[feature]` CLAUDE.md — added Prompting Guidance: Claude now auto-suggests clearer phrasing when a prompt is ambiguous
- `[feature]` CLAUDE.md — added JS State Pattern Checklist (6 checks for saveState/loadState correctness, init order, default-active seeding, badge count)

### Cryptography Labs
- `[ux]` Lab 08 — Demo 1 IPsec: 2-button bar replaced with 2×2 combo grid (Transport+ESP, Transport+AH, Tunnel+ESP, Tunnel+AH); cards mark themselves visited with green on click
- `[bug]` Lab 08 — All objectives reset on refresh; `buildPacket()` was calling `saveState()` before `loadState()` ran, overwriting saved state
- `[bug]` Lab 02 — Objectives overlay no longer resets on refresh; `checkReflectionLock()` was missing after `loadState()` in `DOMContentLoaded`
- `[bug]` Lab 08 — VPN scenarios objective now requires all 4 scenarios (DPI, Quantum, IoT, Federal); was completing on first selection
- `[bug]` Lab 09 — "Explored all 4 KDFs" objective now triggers correctly; PBKDF2 default tab was never registered in `kdfTabsSeen` on load
- `[ux]` Labs 01–04 — Objectives overlay moved to bottom-right matching Lab 05; chevron above panel, opens downward
- `[feature]` Lab 02 — "Click both cipher types (Stream & Block)" added as first objective; badge updated to 0/5
- `[feature]` Lab 03 — All 4 AES cipher modes now required as objective (was 2); label updated to list ECB, CBC, CTR, GCM
- `[ux]` Labs 02–04 — Objectives overlay reordered to match top-to-bottom HTML content sequence in each lab (quiz moved to last in all three)
- `[feature]` Lab 01 — CIA Triad pillars added as objective #1; all 3 (C, I, A) must be clicked; badge now shows 0/6
- `[feature]` Lab 01 — CIA Triad Threat Simulator added as lab objective; reflection unlocks only after simulator is run
- `[ux]` Lab 01 — Objectives overlay reordered to match top-to-bottom content sequence (simulator → key exchange → screenshot → password task → quiz)
- `[bug]` Labs 01–02 — "Enter your full name" input now styled correctly (was missing `.lab-input` CSS, rendering as unstyled browser default)
- `[bug]` Lab 01 — Tour auto-popup fixed: bumped localStorage key to `v2` to clear stale flag from prior sessions
- `[ux]` All labs — "Why and Purpose" renamed to "Why This Matters" across all 10 files (41 occurrences)
- `[ux]` Lab 01 — Collapsible "How to open Terminal" panels added to macOS/Windows/Linux tabs in key pair section
- `[ux]` Labs 01–02 — Quiz and reflection formatting aligned with Lab 03: QUIZ_OPTIONS with per-option feedback, blue required-reflection box, optional observations separator, guided questions added to Lab 01
- `[ux]` All labs — Renamed "Why and Purpose" label to "Why This Matters" across all 10 files
- `[ux]` Labs 03–06 — Added "Why and Purpose" info boxes to all demo sections (16 boxes total across 4 files)
- `[ux]` Lab 09 — KDF/Mistakes/Lifecycle thresholds raised to require 100% completion; language badges on 8 mistake cards; hardware preset notes updated
- `[ux]` Lab 10 — PQC requires all 4 algorithms; ZK demo blue→green; checklist replaced with 20-question True/False quiz with instant feedback
- `[ux]` Lab 08 IPsec/TLS — Added "Why and Purpose" boxes to all 4 demos, Demo 1 now requires all 4 mode/protocol combos, vpnDone objective added to tracker
- `[ux]` Labs 01–02 — Formatting aligned with Lab 03 reference: tour modal system, forward nav removed, stray comments cleaned, meta tags added; Lab 01 auto-popup tour on first visit with help-reminder toast
- `[ux]` Lab 07 PKI — Added "Why and Purpose" boxes to all 4 demos, fixed cert field objective label, Demo 4 now requires all 4 attack cards to complete objective

### Primer
- `[feature]` primer/edtech/ — Higher Education & EdTech industry primer with 7-tab navigation
- `[feature]` Created `primer/ai-infrastructure/index.html` — AI Infrastructure & Research Ops industry primer with 7-tab SPA (~35-term searchable glossary, 8 player categories, 6 metric categories, 7-layer tech stack, 3 workflows, 6 trend cards)
- `[feature]` Created `primer/fintech/index.html` — Financial Services & FinTech industry primer with 7-tab SPA (Overview, Terminology, Players, Metrics, Tech Stack, Workflows, Trends)
- `[feature]` Created `primer/ecommerce/index.html` — E-Commerce & Digital Marketplaces industry primer with 7-tab SPA, searchable glossary (~30 terms), 27 player cards, conversion funnel visualization, 3 workflow flows, and 6 trend cards

## 2026-03-24

### Primer
- `[feature]` Created `primer/` section — industry-by-industry foundational knowledge base with landing page, search, and card grid
- `[feature]` Added Primer nav entry and section card to root `index.html`
- `[feature]` Scheduled weekly Monday 9am task to prompt for next industry to build

### Cryptography Labs
- `[feature]` All 10 labs — mini quiz system upgraded with per-option feedback, exploration mode after correct answer, and persistent correct button highlight
- `[bug]` Lab 06 Demo 2 — objective label still said "≥6" despite threshold already being all 12; label and print summary updated to match
- `[feature]` Lab 07 Demo 1 — all 11 certificate fields must be clicked to complete the objective (was any 5 of 11)

### Root / Global
- `[feature]` Added author/copyright metadata to all 353 HTML files for proper attribution if shared/deployed separately
- `[feature]` Added minimal auto-updating copyright footer to all 328 content files (non-homepages)
- `[feature]` Copyright footer added to all lab homepages (auto-updating year, LinkedIn link)
- `[bug]` Fixed copyright year script placement — script was executing before DOM element existed

### Cryptography Labs
- `[feature]` Lab 06 Demo 1 — NIST levels objective now requires all 5 levels (1–5) clicked; Demo 2 requires all 12 algorithms clicked (was 6); Demo 4 has reset button for agility timeline
- `[feature]` Lab 07 Demo 1 — Changed text from "Click any" to "Click each" field; Demo 3 — enhanced with comprehensive CRL vs OCSP comparison, both methods must be checked to complete objective
- `[feature]` Lab 05 Demo 3 — attacker hardware selector (Laptop/RTX 4090/H100 Cluster/Nation-State) with dynamic crack-time comparison; crack times update live as user types password or switches hardware
- `[feature]` Added interactive "How Labs Work" tour guide — 6-step modal with auto-popup on Lab 01 first visit, Help icon in navbar (all labs)
- `[bug]` Fixed tour Step 2 text — removed hardcoded "4 objectives" (labs have 4-10 objectives depending on complexity)
- `[ux]` Added prominent "Export Complete" banner after PDF export — shows green success message with "✕ Exit Lab" button (auto-hides after 8 sec)
- `[bug]` Fixed broken "Previous Lab" navigation links — were pointing to non-existent `../week*/` paths, now use correct relative filenames
- `[feature]` Added navigation footer to all 10 labs with link to previous lab (Lab 01 has no previous link)

### Cryptography Labs
- `[ux]` Exit Lab button added to all 10 labs (confirms → closes tab, fallback to Lab Home)
- `[ux]` Separated Learning Reflection (★ Required, blue border) from Lab Observations (Optional, below divider)
- `[bug]` Quiz correct answer was always option B — now randomized on every page load
- `[feature]` Modules 07 & 10 upgraded to match Module 06 format: reflection-lock, guided questions, Lab Observations field
- `[ux]` Removed all forward "Next →" navigation links — users can only navigate to prior labs
- `[feature]` Lab 04 Diffie-Hellman Key Exchange Step 4 — Shows disconnect after shared secret is established (no effect); distinct from steps 1-2 vulnerability window
- `[feature]` Lab 04 Message Signing yes/no selection — User can choose to verify correctly OR tamper; both unlock submission (was single auto-tamper button)

### Case Studies
- `[bug]` Hero title/subtitle unreadable — ECG canvas animation overlapped text
- `[feature]` Created full section: hub + 10 case studies (Netflix, Twitter, Amazon, Discord, GitHub, Uber, Slack, Cloudflare, Instagram, Google Spanner)

### Coding Agents
- `[feature]` Added thorough explanations to labs 01–08 (Concept Overview, How It Works, Real World Examples, Common Pitfalls, Key Takeaways)
- `[feature]` Created Lab 09 — "Do I Still Need to Code?" (skill shift chart, scenario quiz, spot-the-bug challenge)
- `[bug]` Lab 09 canvas blank — JS syntax error from apostrophes in single-quoted strings; fixed with backtick template literals

### Trainer Series
- `[feature]` Created full section: hub + 10 interview prep trainers (URL Shortener, Chat System, News Feed, Rate Limiter, Notification System, Key-Value Store, Search Autocomplete, Video Streaming, Distributed Cache, Ride-Sharing)

---

## 2026-03-23

### Root / Global
- `[feature]` Added Case Studies & Trainer Series sections to main index.html sidebar nav and content grid
- `[feature]` Created CLAUDE.md — agent instructions for JS syntax checking, debugging order, post-write checklist

---

## 2026-03-20

### Simulators
- `[feature]` Created Wireshark Network Analysis Simulator — 1750-line faithful Wireshark UI with 3-pane layout, step-by-step guided analysis, protocol color coding, display filter bar

### Cryptography Labs (new section)
- `[feature]` Created 10-lab Cryptography Labs series: CIA Triad & Authentication, Stream/Block Ciphers, Symmetric Encryption & MAC, Asymmetric Encryption, Hash Algorithms, Cryptography Standards, PKI, IPsec/TLS, Secure Implementation, Emerging Crypto
- `[refactor]` Moved `security/cy615/` and misc security prototypes under `prototypes/security/`
- `[ux]` Revised `security/index.html` and updated `security/cryptography.html`, `security/secure-header.html`

---

## 2026-03-16

### Security / CY615
- `[feature]` Created CY615 course lab suite: hub index, shared CSS/JS, Week 1 lab, Week 2 lab

### CityU Tools
- `[bug]` Fixed pop-up blocker in multi-tab launcher

---

## 2026-03-12

### Prototypes
- `[feature]` Added 5-version slides-to-web prototype series for CS628 HOS01

---

## 2026-03-11

### Crypto Vulnerability Labs (new section)
- `[feature]` Created 10-lab Python Crypto Vulnerability Labs: Hardcoded Secrets, Weak PRNG, Broken Password Hashing, ECB Mode, Unauthenticated Encryption, Weak Key Derivation, Timing Attack, Insecure TLS, Predictable IV, Broken Cipher

---

## 2026-03-10

### Encryption Labs (new section)
- `[feature]` Created 10-lab Encryption Labs series: What is Encryption, Secret Keys, Symmetric vs Asymmetric, Block Ciphers/ECB, IV/Nonce Reuse, Hashing & Integrity, Password Storage, Authenticated Encryption (GCM), TLS/Certificates, Spot the Mistake

---

## 2026-03-07

### System Design Learn
- `[feature]` Added Module 11 — Rate Limiting (token bucket, leaky bucket, fixed/sliding window algorithms)
- `[ux]` Updated index and main homepage navigation

---

## 2026-03-06

### System Design Learn (new section)
- `[feature]` Created 10-module interactive metrics series: RPS & Traffic, Storage Estimation, Bandwidth, Availability Nines, Caching, Read Replicas, Queues, CDN, Sharding, Latency Budget

### System Design Metrics (new section)
- `[feature]` Created 10 printable assessment worksheets covering same metrics as Learn modules

### System Design Activities (new section)
- `[feature]` Created 10 scenario-based design activities: URL Shortener, Distributed Cache, File Storage, OAuth2, Payment Processing, Push Notifications, Rate Limiting/API Gateway, Search Autocomplete, News Feed, Video Streaming

---

## 2026-03-05

### Digital Twin
- `[feature]` Completed 10-module Digital Twin lab series with modules 08–10: Scenarios, Quiz, Design
- `[feature]` Created modules 01–07: Intro, Factory, Building, Maintenance, Smart City, Health, Sync

---

## 2026-03-04

### Database Labs
- `[ux]` Expanded and refined SQL Injection lab (HOS07) — restructured with improved scenarios and examples
- `[feature]` Created initial SQL Injection lab `database-lab-cs445-hos07-sql-injection.html`

---

## 2026-03-02

### CityU Tools (new section)
- `[feature]` Created multi-tab launcher and link generator utilities

---

## 2026-02-25

### Prototypes
- `[feature]` Added containerization prototype series (v1–v6)
- `[feature]` Added system-design prototypes: architect-sandbox, AI agent, Docker, scalability, VerityStream

### System Design Labs
- `[refactor]` Moved system-design game/course to prototypes/; added 10 new case study scenarios

---

## 2026-02-19

### Wild Rift
- `[feature]` Added pings tool with 6 audio files (attack, danger, group, missing, omw, retreat)
- `[ux]` Bug fixes to baron smite timing logic

---

## 2026-02-13

### Digital Twin
- `[feature]` Added React-based Digital Twins explainer pages (3 versions, up to 1648 lines)

### System Design Labs
- `[feature]` Added `system-design-course.html` — large React-based interactive course (2162 lines)

---

## 2026-02-10

### Database Labs
- `[feature]` Archived previous lab versions (v1–v3 customers/employees) under `archives/database/`
- `[ux]` Added descriptions to HOS04 and PE04 labs; refactored both files
- `[refactor]` Renamed answer key file (removed " copy" from filename)
- `[feature]` Created initial HOS04 and PE04 database labs with answer keys

---

## 2026-02-04

### Wild Rift
- `[feature]` Created Baron Smite timing trainer — dark LoL-styled UI, smite sound effect, score tracking
- `[refactor]` Renamed `baron_smite.html` to `baron-smite.html`
- `[ux]` Multiple layout and interaction improvements to Baron Smite trainer

---

## 2026-01-12

### History Timelines (new section)
- `[feature]` Created 4 retro game concept pages: FF7 Dialogue Box, History Check, RE Ink Ribbon, Rotating Save Crystal

---

## 2026-01-06

### System Design Games
- `[feature]` Created System Design Architect drag-and-drop game (toolbox + canvas + architecture validation)
- Added to main `index.html` homepage

---

## 2025-12-18

### Security
- `[refactor]` Consolidated 18 standalone security HTML files into `security/` folder

---

## 2025-12-16

### Security
- `[feature]` Added 5 SDLC secure coding exercises: Cryptography, Data Integrity, Invisible Request, Poisoned Script, Secure Headers

---

## 2025-12-14

### Security
- `[feature]` Created "The Shattered Database" — PyScript interactive SQL injection exercise

---

## 2025-12-13

### Security
- `[feature]` Added 4 SDLC security activities: Brute Force Balance, BoF3 Dragon Gene Combinator, Architect Gate (3 versions), Missing Gate, Hidden Script, Salted Vault, Malicious Link

---

## 2025-11-25

### Security
- `[ux]` Minor edits to cost-of-insecurity.html content

---

## 2025-11-20

### Root / Global
- `[feature]` Initial playground: created `index.html` homepage and `cost-of-insecurity.html` interactive security awareness lab (CIA triad sorter, cost calculators, dark/light mode)
