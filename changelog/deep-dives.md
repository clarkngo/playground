# Changelog — Deep Dives

Path: `/deep-dives/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-04-07

### [refactor] `deep-dives/ebay-ads/` — Spark page rename; no &ldquo;classroom&rdquo; wording in deep dives
- Renamed `spark-ebay-classroom.html` → `spark-ebay-supplement.html`; `shared.css` — `.supplement-prompt-list`, `body.spark-supplement-page` (replaces `.classroom-prompt-list` / `body.classroom-supplement`)
- `deep-dives/index.html` — hero subcopy and **Primary-source supplements** section (replaces &ldquo;Classroom supplements&rdquo;); card links + tags updated
- `ebay-ads/index.html`, `glossary.html`, `ch/03-tech-stack.html` — hrefs and labels; Spark supplement page copy (no &ldquo;in class&rdquo; / &ldquo;Ask students&rdquo;)

### [feature] `deep-dives/ebay-ads/index.html` — process node flow on ecommerce ads fundamentals
- `ads-pipeline-sim.js`: new `RETAIL` scenario pack — **Placement path** (shopper → placements → rank/auction → sponsored + IDs) and **Measure + settle** (click/view → events → attribution → ledger); `wireIfPresent("eps-retail-root", …)` in `init()`
- Hub: `#eps-retail-root` + subheading &ldquo;Process node flow&rdquo;; `shared.css` — `.fundamentals-subtitle`, `.fundamentals-flow-lead`, `.fundamentals-eps`

### [ux] `deep-dives/ebay-ads/` — hub disclaimers removed; ecommerce ads fundamentals section
- Removed `about-box` (&ldquo;What this is&rdquo; / educational-use) and `reader-guide-box` (&ldquo;Too much jargon?&rdquo;); removed per-chapter `reader-tip` callouts and footer lines with &ldquo;Educational notes&rdquo; / &ldquo;Not affiliated&rdquo;; glossary lead shortened (no reassurance paragraph); `shared.css` — new `.fundamentals-section` / `.hub-footer`, removed `.about-box`, `.reader-guide-box`, `.reader-tip`
- Hub `index.html`: new **How ecommerce ads work** block (retail media, sponsored placement loop, CPC/CPM/CPS, measurement, why marketplace ads differ from generic display)

## 2026-03-27

### [ux] `deep-dives/ebay-ads/` — removed &ldquo;CIA-style&rdquo; wording from pipeline sim badges and docs (neutral &ldquo;Flow&rdquo; badge + `shared.css` / changelog copy)

### [ux] `deep-dives/ebay-ads/glossary.html` — reader guide &amp; jargon decoder (business / data / ops tables)
- Hub: `reader-guide-box` + &ldquo;Reader help &amp; supplements&rdquo; card; `shared.css` — `.reader-tip`, `.reader-guide-box`, glossary table styling
- Ch 1, 2, 3, 5 + `spark-ebay-supplement.html` — short tips linking to glossary anchors (`#business`, `#data`, `#ops`)

### [bug] `deep-dives/ebay-ads/ch/03-tech-stack.html` — replaced incorrect &ldquo;telemetry fan-in&rdquo; SVG
- Old diagram mixed Kafka/Flink with Prometheus in a misleading way; replaced with **SQL-on-Hadoop path** aligned to eBay&rsquo;s [Optimized Spark SQL Engine](https://innovation.ebayinc.com/stories/explore-ebays-new-optimized-spark-sql-engine-for-interactive-analysis/) post (gateway → Spark Thrift on YARN → Hive metastore + HDFS)

### [ux] `deep-dives/ebay-ads/` — expanded node-flow sims + SVG architecture diagrams
- **`ads-pipeline-sim.js`:** new scenario packs — `OVERVIEW` (streaming / batch / edge), `RTB` (auction + DSP⇄SSP), `OBSERVABILITY` (Sherlock path + PromQL alerts), `INCIDENT` (rollback vs Kafka lag); `wireIfPresent()` wires any `#eps-*-root` on the page
- **Ch 1:** layered topology SVG + `#eps-overview-root`
- **Ch 2:** programmatic chain SVG + `#eps-rtb-root`
- **Ch 3:** `#eps-obs-root` + reference architecture SVG (before Touchstone)
- **Ch 5:** `#eps-incident-root` + script include
- **`shared.css`:** `.arch-wrap`, `.arch-svg`, `.arch-hchain`, box/arrow styles for diagrams
- Hubs: `ebay-ads/index.html`, `deep-dives/index.html` — chapter/deep-dive blurbs updated

### [feature] `deep-dives/ebay-ads/ch/03-tech-stack.html` — anomaly detection implementation, ads control center requirements, stack map
- **Sherlock / anomaly:** data path (ingest → windows → baseline → score → notify), streaming vs batch roles, detection-layer requirements (latency, precision/recall, explainability, ownership), ads-specific twists (seasonality, auctions, attribution lag)
- **Control Center:** product/UX, technical integration, reliability & safety requirements for an ads-oriented control plane
- **Stack map table:** telemetry → Flink/PromQL → Sherlock/ES ML/alerts → PagerDuty/Slack → ServiceNow/Touchstone → Control Center UI
- `ch/05-operations.html` — link to Ch 3 anchor `#control-center-stack`; hub `index.html` — Ch 3 card blurb updated

### [feature] `deep-dives/ebay-ads/spark-ebay-supplement.html` — eBay Innovation Spark articles (primary-source digest)
- Summarizes and relates [Using Spark to Ignite Data Analytics](https://innovation.ebayinc.com/stories/using-spark-to-ignite-data-analytics/) (2014: RDDs, YARN, HDFS, scale snapshot, MLlib, Shark vs Hive) and [Optimized Spark SQL Engine](https://innovation.ebayinc.com/stories/explore-ebays-new-optimized-spark-sql-engine-for-interactive-analysis/) (2021: post-migration SQL service, Thrift server, governance, Delta updates, cache/indexes/AQE, operational metrics)
- Discussion prompts + tie-in to Ch 3; linked from `deep-dives/index.html` (Classroom supplements), `ebay-ads/index.html`, and `ch/03-tech-stack.html`
- `shared.css` — `.supplement-prompt-list`, `body.spark-supplement-page` heading spacing

## 2026-04-07

### [ux] `deep-dives/ebay-ads/` — pipeline flow widgets (`ads-pipeline-sim.js`)
- Phase strip + animated packet dots on connectors + monospace log; **scenario pick = buttons only** (no dropdown)
- Ch 3: tech scenarios — Real-time path, Batch ETL, Log / search
- Ch 4: workflow scenarios — Experiment ramp, Deploy pipeline; removed static CSS-only flow strips in favor of the live sim

### [ux] `deep-dives/ebay-ads/` — readable cool-slate theme; animations on tech stack & workflows
- **`shared.css`:** higher-contrast palette (slate/cyan/violet), larger base type, improved tables; `prefers-reduced-motion` respected
- **Ch 3 (`chapter-stack`):** staggered fade-in on `.tech-card`, animated section `h3` accents, subtle pulse on `.highlight-box`
- **Ch 4 (`chapter-workflows`):** experiment + deployment flows rebuilt as horizontal `.flow-pipeline` with `.flow-step` chips, animated connectors (`flowShine`, `arrowNudge`), staggered step entrance

### [refactor] eBay Ads — `deep-dives/ebay-ads/` hub + chapter split (spark-book pattern)
- New folder `deep-dives/ebay-ads/`: `index.html` hub, `shared.css`, `ch/01-overview.html` … `ch/05-operations.html` (breadcrumb + prev/next nav like `spark-book/ch/*`)
- Content migrated from monolithic `deep-dives/ebay-ads-platform.html` (unchanged body per chapter)
- `deep-dives/ebay-ads-platform.html` → redirect stub to `ebay-ads/index.html`
- `deep-dives/index.html` entry card href updated to `ebay-ads/index.html`
- Hub `about-box` disclaimer: educational, not affiliated with eBay
- `docs/ads-platform/ebay-internals.md` — pointer to canonical `deep-dives/ebay-ads/`

### [feature] eBay Ads Platform — System Deep Dive (Entry 02)
- New `deep-dives/ebay-ads-platform.html` — comprehensive 5-tab deep dive moved from `/docs/ads-platform/`
- Converted from gradient-purple theme to spark-book dark theme for consistency
- Expanded tech stack section with detailed deep dives on: Kafka (event streaming, partitioning, consumer lag), Flink (windowing, state management, backpressure), Spark (DAG execution, ML pipelines), Hadoop/HDFS (data organization, retention), Elasticsearch (indexing, anomaly detection), ClickHouse (columnar architecture, ingestion), Prometheus/Grafana (metrics, PromQL queries), Sherlock.IO (statistical anomaly detection), Control Center (observability hub), Touchstone (A/B testing framework), ServiceNow (change tracking)
- Removed: video embeds and external links; documentation wiki section; video resources section; common incident topics section
- Enhanced: operational tools expanded to full toolkit (5 cards: Prometheus+Grafana, Control Center, Sherlock.IO, Kubernetes, Pronto); incident diagnosis table with 7 common incident types; detailed investigation workflow (phases 1-4); SLA targets for revenue, engagement, system health, data quality
- Tab structure: Overview, Concepts, Tech Stack (expanded), Workflows, Operations (expanded)
- Root `deep-dives/index.html` updated: added eBay entry as #02 in live cards; renumbered coming-soon entries (ServiceNow #03, OpenSearch #04, SAP #05)

## 2026-04-03

### [feature] Deep Dives series created
- New series: cross-domain technology internals deep dives — how real products actually work under the hood
- `deep-dives/index.html` — hub page with animated network-graph canvas hero, live entry card, and 3 "coming soon" cards (ServiceNow, OpenSearch, SAP)
- `deep-dives/01-wild-rift.html` — first entry: Wild Rift, 6 tabs

### Entry 01: Wild Rift — How It Really Works
6-tab deep dive covering:

| Tab | Content |
|-----|---------|
| Overview | What Wild Rift is, quick-facts metrics row, animated 5v5 minimap canvas, core game loop value chain, 4 feature cards |
| Game Engine | Authoritative server model, client-server tick loop canvas animation, client prediction, fog of war partial-state broadcast, UDP + custom reliability layer |
| Matchmaking | Visible LP rank vs hidden MMR, Glicko-2 inspired rating (RD uncertainty), interactive queue-time slider with expanding MMR search radius canvas, role preference weighting |
| Tech Stack | 7 stack layers (game servers, matchmaking, backend platform, data storage, real-time comms, CDN/assets, mobile client) with chip-row tech labels |
| Business Model | F2P cosmetic-only model, animated revenue breakdown bars (skins 72%, battle pass 12%, events 9%, bundles 5%), monetization table with margin profiles, pricing psychology section |
| Key Numbers | Metrics cards across scale (80M+ downloads, 5M+ DAU), infrastructure (30Hz tick, <20ms latency, ~300KB/match), matchmaking (<90s queue, ±50 MMR window), economics ($150M+ revenue, ~85% gross margin) |

### Root index.html
- Added `🔬 Deep Dives` nav link under "Case Studies & Training" nav group, badge `1`
- Added `deep-dives` section block with collection card + Wild Rift entry card
