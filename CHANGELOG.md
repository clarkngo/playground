# Playground Changelog

All changes across the project, newest first.
Detailed entries are in `changelog/<collection>.md`.

Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-26

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
