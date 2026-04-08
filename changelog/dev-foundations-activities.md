# Changelog — Dev Foundations Activities

## 2026-04-07

### [feature] HOS handouts — full PDF step-by-step text preserved (verbatim extract)
- `hos_verbatim_pdf_append.py` — appends collapsible `<details>` + `<pre class="hos-pdf-full-raw">` with `html.escape` text from `_pdf_extracts/hos{NN}_full.txt` after each curated `<section class="hos-pdf-source">`; `inject_verbatim_styles()` adds print-friendly rules; HOS04 includes optional `hos04b_full.txt` (without-Docker PDF) — file added from course PDF
- `build_hos_curated_03_10.py` / `build_hos02_curated_handout.py` — call `full_pdf_text_append` before `</section>`; lab intro explains curated top + full extraction at bottom

### [feature] HOS03A–HOS10A — curated handouts + builder (HOS01/HOS02 pattern)
- `build_hos_curated_03_10.py` — replaces generated `<pre class="hos-pdf-full-raw">` with `<section class="hos-pdf-source">` for `03-flask-rest-api-hos-workflow.html` through `10-advanced-microservices-aws-lambda-hos-workflow.html`: standardized lab intro + scenario un-escape, strips `.hos-pdf-verbatim-details` / `.hos-pdf-full-raw` CSS block; H03/H04 sectioned narrative + figure grids (`hos03-pdf-figures/`, `hos04-pdf-figures/` + `hos04b-pdf-figures/` for without-Docker); H05–H10 short narrative + full figure index per `hos{NN}-pdf-figures/`
- `generate_hos_02_10.py` — skips modules **02–10** so curated HTML is not overwritten by verbatim PDF dumps (re-run `build_hos02_curated_handout.py` or `build_hos_curated_03_10.py` after template changes)

### [feature] HOS02A — curated cookbook HTML (aligned with HOS01A build)
- Same recipe as HOS01: no verbatim `<pre>` dump; semantic headings, `hos-cmd` / `hos-pre-df`, `hos-pdf-fig-grid` + captions; optional note line style `.hos-pdf-note`; `build_hos02_curated_handout.py` splices the handout and fixes lab intro + scenario HTML; bulk generator skips `02` so it is not overwritten

### [bug] HOS02–10 generator — handout splice vs CSS inject; HOS04 dual PDF
- **Symptom:** `class="pd  <!-- Complete HOS…` (truncated `pdf-only`), missing `.lab-header`, broken DOM. **Root cause:** `start`/`end` for replacing the HOS01A handout were computed on the template before optional `mid_style_inject`, so body offsets were short by the inject length. **Fix:** `start = t.index(...)` / `end = t.index(...)` after inject on `t`.
- **HOS04A merge:** `pdf_file_alt` → extract text with `pdf_text_all_pages`, images to `hos04b-pdf-figures/`; second `<details>` + figure grid for the without-Docker handout; hub card copy updated.

### [feature] HOS cookbook HOS02A–HOS10A — generated pages + generator fixes
- `hos/dev-foundations-activities-hos/02-git-repositories-refactoring-hos-workflow.html` through `10-advanced-microservices-aws-lambda-hos-workflow.html` — same UX as HOS01A: verbatim PDF text in `<pre class="hos-pdf-full-raw">`, per-module `hos{NN}-pdf-figures/`, Why cards, dual-panel simulator, scenario, collapsible step reference, seven toolbox steps + four distractors, `localStorage` keys `dfa-hos02a-canvas` … `dfa-hos10a-canvas`
- `generate_hos_02_10.py` — **Symptom:** extra `</div>` after AI prompts / `&amp;amp;` in reference names. **Root cause:** regex matched only through `prompt-grid` close, leaving `prompt-guide` close in the template; **Fix:** require three closing `</div>` for the prompt block; use `esc_html_body` (`html.unescape` then `html.escape`) for ref labels
- `hos/dev-foundations-activities-hos/index.html` — landing cards for all ten HOS modules

### [feature] HOS01A activity — PDF figures embedded (`hos01a-pdf-figures/`)
- Seventeen PNGs extracted from the HOS01A PDF (pages 1, 5–13) and referenced beside matching sections: course header, Python/Jupyter marketplace, notebook/kernel UI, Hello World output, Docker extension, Dockerfile tree + editor, `docker build`, `docker image ls`, `docker run` shell, `docker container ls` + terminals; `.hos-pdf-fig` / `.hos-pdf-fig-grid` styles + print-friendly rules

### [feature] HOS01A activity — full PDF handout embedded in page
- `hos/dev-foundations-activities-hos/01-github-codespaces-hos-workflow.html` — `<section class="hos-pdf-source">` includes complete HOS01A text: metadata (authors, dates), Before You Start, Readings, Learning Outcomes, five screenshot upload filenames, Key Concepts (Codespaces, Python, Jupyter, Dockerfile, Image, Container), Sections 1–4 with numbered steps; Dockerfile body from handout (`FROM ubuntu:20.04`, `RUN apt… sbcl`, `WORKDIR /usr/src`); commands `docker build -t lisp .`, `docker image ls`, `docker run --interactive --tty`, `docker container ls`; print CSS for light handout; `.why-section` hidden when printing

### [refactor] HOS cookbook activities live under `hos/dev-foundations-activities-hos/`
- Moved from repo root `dev-foundations-activities-hos/` to `hos/dev-foundations-activities-hos/`; playground card and nav links updated (`../../` to Playground, `../index.html` HOS hub)
- `hos/index.html` — hero copy covers CS628 + CS445; new `.hos-hub-cross` callout links the Dev Foundations (HOS) hub; Module 10 card targets `full-stack-dev/module-10/module-10-conversation-to-design.html`
- `hos/full-stack-dev/module-10/` — holds `module-10-conversation-to-design.html` and `module-10-pdf-theme.css`; stylesheet path `../../shared.css`, back link `../../index.html`; optional `full-stack-dev/index.html` mini-hub

### [feature] `dev-foundations-activities-hos/` — parallel CS445 HOS track (HOS01A)
- New collection folder for PDF-infused activities; landing `hos/dev-foundations-activities-hos/index.html` links the generic `dev-foundations-activities/` collection for comparison
- `01-github-codespaces-hos-workflow.html` — HOS01A (GitHub Codespaces): seven-step workflow (Codespace → Python/Jupyter + `helloworld.ipynb` → Docker extension + Dockerfile → `docker build -t lisp .` → `docker image ls` → `docker run -it … /bin/bash` → `git push`); four distractors (`docker container ls`, local hypervisor, `docker push` to Hub, pip before repo); dual simulator (Codespaces happy path vs `docker build` without Dockerfile / wrong cwd); expandable reference for all 11 toolbox items; `localStorage` key `dfa-hos01a-canvas`
- Playground root `index.html` — file card under Dev Foundations pointing to the HOS hub

---

## 2026-04-02

### [ux] All 10 activities — dual-panel simulator replaces dropdown
- Replaced single `<select>` + one Simulate button with two side-by-side `.sim-panel` blocks, each labeled and with its own `▶ Simulate` button — no scenario selection step required
- Added `.sim-dual`, `.sim-panel`, `.sim-panel-header`, `.sim-panel-label` CSS classes; removed `.sim-controls` and `.sim-select`
- All simulator JS updated: `runSimulator(key, sfx)` signature, `_simTimers = { a: [], b: [] }` per-panel timers, all element IDs suffixed with `-a` or `-b`
- Added `@media (max-width: 620px) { .sim-dual { flex-direction: column; } }` to all activity files

### [ux] All 10 activities — Validate Architecture + Export PDF button placement normalized
- **Activities 07 and 08**: buttons were in the canvas column (below the drop zone); moved to toolbox column (below `#toolbox`) to match all other activities
- **Activity 07**: removed `&#10003;` prefix from "Validate Architecture"; added `no-pdf` class to Export PDF button
- **Activity 08**: changed button label from "Validate Pipeline" → "Validate Architecture"; removed `&#8681;` icon from "Export PDF"; added `no-pdf` class
- All 10 files now have identical button markup in `#toolbox-col`

---

## 2026-04-01

### [feature] Activities 02–10 live — full collection complete
- `02-distributed-version-control.html` — Distributed Version Control System: sequence WorkingTree → StagingIndex → LocalRepo → RemoteRepo → BranchRef → MergeEngine → CITrigger; distractors: Central Lock Server, Single Shared Branch, FTP File Upload; simulator: Distributed Git Workflow vs Centralized Lock-Based Workflow
- `03-rest-api-gateway.html` — REST API Gateway Architecture: sequence Client → DNS → LoadBalancer → APIGateway → AuthService → AppServer → Database; distractors: CDN Proxy, Message Queue, Direct DB Write; simulator: Secure API Gateway Path vs Direct Client-to-Database (Insecure)
- `04-relational-database-internals.html` — Relational Database Internals: sequence SQLParser → QueryOptimizer → ExecEngine → BufferPool → StorageEngine → WAL → DiskStorage; distractors: Full Table Scan Optimizer, Memory-Only Storage, Skip Transaction Log; simulator: Optimized Query Path vs Full Table Scan
- `05-automated-testing-pipeline.html` — Automated Testing Pipeline: sequence UnitRunner → Coverage → Integration → ReportAgg → QualityGate → ArtifactStore → DeployGate; distractors: Deploy Before Tests, Skip Coverage Check, Manual QA Only; simulator: Gate-First Pipeline vs Deploy-Before-Test Anti-Pattern
- `06-software-architecture-layers.html` — Layered Software Architecture (SOLID): sequence Presentation → Application → Domain → RepoInterface → DataAccess → Database → ExternalSvc; distractors: Business Logic in UI, Direct DB from Presentation, Circular Dependency; simulator: Clean Architecture vs Spaghetti Architecture
- `07-application-security-architecture.html` — Application Security Architecture: sequence WAF → APIGateway → AuthService → InputValidation → BusinessLogic → EncryptedStore → AuditLog; distractors: Plaintext Credentials, Skip WAF, Auth After Business Logic; simulator: Hardened Request vs Unguarded Request
- `08-cicd-pipeline-architecture.html` — CI/CD Pipeline Architecture: sequence SourceRepo → CIBuild → ArtifactReg → Staging → AutoTests → ApprovalGate → Production; distractors: Deploy to Prod Before Testing, Skip Artifact Registry, Skip Staging; simulator: Full CI/CD Pipeline Deploy vs Direct-to-Production
- `09-microservices-system-design.html` — Microservices System Design: sequence APIGateway → ServiceReg → Microservices → MsgBroker → PerSvcDB → DistCache → Observability; distractors: Shared Monolithic DB, Direct Calls Without Registry, Skip Message Broker; simulator: Microservices Architecture vs Monolithic Architecture
- `10-resilient-distributed-system.html` — Resilient Distributed System Design: sequence LoadBalancer → CircuitBreaker → RetryBackoff → Bulkhead → ReplicaSet → DistTracing → ChaosTesting; distractors: Single Point of Failure, No Circuit Breaker, Skip Replica Set; simulator: Resilient Failure vs Cascading Failure
- All 9 new activities share identical CSS/JS shell from Activity 01; only LAB_CONFIG, toolData, distractors, and simulator scenarios differ per file
- All 10 activities pass `node --check` JS syntax validation

### [feature] Homepage `index.html` created for dev-foundations collection
- `dev-foundations-activities/index.html` — dark theme landing page with 10-card activity grid, "How It Works" 4-step section, and answer key banner
- Links back to `../index.html` (root playground); card links match `01-container-runtime-architecture.html` through `10-resilient-distributed-system.html`

### [feature] `answer-key.html` — all 10 modules marked Live with correct sequences
- All status pills updated from "Planned" to "Live"; mod-badge updated to `.built` (green) for all 10 modules

---

Path: `/dev-foundations-activities/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-04-01

### [feature] Created Dev Foundations Activities collection — Activity 01 live, 02–10 planned
- `dev-foundations-activities/01-container-runtime-architecture.html` — Container Runtime Architecture: sequence 7 stack layers (Application Code → Dockerfile → Container Image → Container Runtime → OS Namespaces/cgroups → Host Kernel → Physical Hardware) with 4 VM-themed distractors (Full VM Hypervisor, Guest OS, Registry Cache, Reverse Proxy)
- GitHub dark theme (raw CSS, no Tailwind): `#0d1117` background, `#58a6ff` accents, `#3fb950` pass, `#f85149` fail
- Toolbox Fisher-Yates shuffles all 11 items (7 correct + 4 distractors) on each load
- Validation: count-mismatch hint fires before per-layer contextual clues (catches placed distractors cleanly)
- `removePlaced()` re-numbers canvas steps after item removal
- `dragleave` uses `!canvas.contains(e.relatedTarget)` to prevent drag-over flicker
- Student name required; PDF export blocked until Validate Architecture is clicked
- `index.html` — Added "Dev Foundations" sidebar nav entry (data-filter="dev-foundations") after Database Labs; added 10-card section div (data-section="dev-foundations") with placeholder cards 02–10 pointing to future files
