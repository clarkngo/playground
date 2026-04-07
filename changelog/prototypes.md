# Changelog — Prototypes

Path: `/prototypes/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-04-07

### [feature] Data Governance: The Definitive Guide — interactive book supplement (Phase 1)
- `data-gov-book/index.html` — hub page; navy/blue dark theme; book icon + O'Reilly attribution; 2 live chapter cards + 4 coming-soon; "How to use" guidance section; Tailwind CDN only
- `data-gov-book/ch/01-what-is-data-governance.html` — Ch 1 interactive: (1) 5-level maturity model click-through (Ad-Hoc → Optimized) showing People/Process/Tools per level and trusted-data % bar; (2) 5-pillar trust simulator (Availability, Usability, Integrity, Security, Safety) — toggle pillars off and watch trust score + 3 downstream consumers (Analytics, ML, Compliance) degrade with context-aware messages; "break all / restore all / random failure" buttons
- `data-gov-book/ch/02-roles-responsibilities.html` — Ch 2 interactive: (1) Role Explorer — 5 tabs (CDO, Data Owner, Data Steward, Data Custodian, Governance Council); each shows Responsibilities / Decisions Owned / Key Partnerships / Typical Tools in 4-column layout; (2) RACI Decision Matrix — 4 selectable scenarios (Define a Data Standard, Handle a Data Breach, Approve Data Access, Launch a Data Product); R/A/C/I chips per role per task; click any cell for a plain-English explanation of what that role does
- All pages: sticky top bar with prev/next nav, hero + concept cards + key quote layout; JS syntax check passes

### [feature] Learning Spark — interactive book supplement (Phase 1)
- `spark-book/index.html` — warm-dark hub ("book on a shelf at night" aesthetic); amber/Georgia serif title; 7 chapter cards (3 live, 4 coming-soon); "How to use" guidance section; no external dependencies beyond Tailwind CDN
- `spark-book/ch/01-architecture.html` — Ch 1 interactive: ports `spark-flow-test.html` node-flow animator (all 3 scenarios: Batch WordCount, Kafka Streaming, Executor OOM); adds 4th outcome cell (Shuffle I/O); adds Cluster Topology view toggle with executor/cores/partitions sliders, task-slot metrics, and utilization indicators; sticky top bar with prev/next nav
- `spark-book/ch/02-lazy-eval.html` — Ch 2 interactive: step-by-step DAG builder; 8 addable transforms (narrow: map, filter, flatMap, union; wide: groupByKey, reduceByKey, join, repartition); stage lane visualization with color-coded boundaries and shuffle breaks; animated execution (nodes go pending → running → done-ok one by one on action trigger); live task counter that stays 0 until action fires; 3 action buttons (collect, count, saveAsTextFile); mini log panel; concept reinforces lazy evaluation
- `spark-book/ch/03-partitions.html` — Ch 3 interactive: 4 sliders (partitions 1–64, executors 1–12, cores/executor 1–8, partition size MB); live colored partition block grid distributed round-robin across executor rows with utilization bars; 5 metric chips (task slots, tasks/executor, scheduling waves, slot utilization, total data); dynamic insight box (under/over/well-partitioned with specific recommendations); rule-of-thumb callout updates per cluster config; before/after comparison cards (under/over/coalesce)
- All 3 chapter pages share: dark GitHub theme (`#0d1117`/`#ff7c43`), sticky top bar, hero + concept cards + interactive + use cases + gotchas layout; JS syntax check passes

---

## 2026-04-06

### [feature] node-flow-animator skill test prototypes
- `prototypes/node-flow-test.html` — system design request flow simulator; 3 scenarios: normal GET (cache miss), normal GET (cache hit), downstream timeout; nodes: Client → API Gateway → User Service → Postgres/Redis; outcome grid: Latency / Error Rate / Cache; blue accent theme
- `prototypes/spark-flow-test.html` — Apache Spark job flow simulator; 3 scenarios: Batch WordCount (HDFS), Structured Streaming (Kafka → Delta Lake), Executor OOM during shuffle; nodes: Driver → YARN RM → Executor Pool → Storage; outcome grid: Job Status / Stage Duration / Records; orange Spark accent theme; adds `node-error` red-glow class distinct from `node-hit` for failed-node state
- Both files test the `node-flow-animator` skill pattern (DOM + CSS transitions, double-RAF packet dots, timed step orchestrator) applied to non-security domains

---

## 2026-04-02

### [feature] ByteByteGo-style course platform prototype
- `prototypes/course-platform.html` (349 lines) — self-contained lesson page prototype inspired by ByteByteGo's course UI
- Layout: sticky top bar with breadcrumb + prev/next nav; 264px sidebar with chapter list; max-width main content column
- Sidebar: sequential chapter numbering, FREE badge (orange pill) on first 3 chapters, lock icon on premium chapters, active chapter highlight with accent border-left, progress bar footer
- Main content: chapter tag + large lesson title; info and takeaway callout box variants; two Mermaid `flowchart LR` architecture diagrams with captions; multi-tab code block (Python / JavaScript / Java) with syntax-colored spans and clipboard copy; Q&A interview simulation with Interviewer/Candidate speaker labels; trade-off table (Approach / Benefit / Limitation); Key Takeaways callout; bottom prev/next chapter nav
- Design system: dark theme (`--bg: #0b1220`) matching playground CSS variable palette; Tailwind CDN for utilities; Mermaid CDN for diagrams; no external font dependencies

---

## 2026-03-20

### [refactor] Moved security labs under prototypes/security/
- Moved entire `security/cy615/` tree to `prototypes/security/cy615/`
- Moved misc security files: `GUIDE-software-security-apps.md`, `architect-gate` variants, `bof-3-dragon-gene-combinator.html`, `hidden-script-v0.html`, `integer-trap-v0.html`, `work-progress.html`
- Also moved `reddit-prototype.html` under `prototypes/security/`

---

## 2026-03-12

### [feature] Added slides-to-web prototypes for CS628 HOS01
- `prototypes/slides-to-web/CS628_HOS01.html` — base slide conversion (334 lines)
- `prototypes/slides-to-web/CS628_HOS01_Native.html` — native HTML version (777 lines)
- `prototypes/slides-to-web/CS628_HOS01_Redesigned.html` — redesigned version (938 lines)
- `prototypes/slides-to-web/CS628_HOS01_Redesigned.md` — redesign notes/prompts (405 lines)
- `prototypes/slides-to-web/CS628_HOS01_with_images.html` — image-inclusive version (453 lines)
- 5 iterations of converting course slides (CS628 HOS01) into web pages

---

## 2026-02-25

### [feature] Added containerization prototype series (6 versions)
- `prototypes/containerization/v1.html` — initial Docker containerization prototype (122 lines)
- `prototypes/containerization/v2.html` — v2 with expanded content (163 lines)
- `prototypes/containerization/v3.html` — v3 iteration (206 lines)
- `prototypes/containerization/v4.html` — v4 with further additions (271 lines)
- `prototypes/containerization/v5.html` — v5 iteration (227 lines)
- `prototypes/containerization/v6.html` — v6 final iteration (249 lines)

### [feature] Added system-design prototypes
- `prototypes/system-design/architect-sandbox.html` — Mermaid.js PASS/FAIL architecture validator (157 lines)
- `prototypes/system-design/autonomous-ai-agent-v-1.html` — AI agent system design prototype (149 lines)
- `prototypes/system-design/docker.html` — Docker architecture page (122 lines)
- `prototypes/system-design/scalability.html` — scalability interactive page (238 lines)
- `prototypes/system-design/veritystream.html` — VerityStream scenario (85 lines)
- `prototypes/visual-sandbox/v1.html` — visual sandbox prototype (134 lines)
- `reddit-prototype.html` — Reddit UI prototype (83 lines, later moved to prototypes/security/)
