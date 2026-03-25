# Changelog — System Design Learn

Path: `/system-design-learn/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-07

### [feature] Added Module 11 — Rate Limiting and updated index
- `system-design-learn/11-rate-limiting.html` — interactive rate limiting module with algorithm selector (token bucket, leaky bucket, fixed window, sliding window), rate sliders, and burst traffic visualizer (472 lines)
- Updated `system-design-learn/index.html` to include Module 11 card
- Updated main `index.html` with revised navigation and section links

### [ux] Minor fix to Module 10 (Latency)
- Small content update to `system-design-learn/10-latency.html`

---

## 2026-03-06

### [feature] Created System Design Learn — 10-module interactive metrics series
- `system-design-learn/index.html` — hub page with card grid ("SysDesign Learn — Interactive Metrics")
- Module 01 `01-rps-traffic.html` — RPS and traffic scaling (DAU to peak RPS calculator)
- Module 02 `02-storage.html` — storage estimation (GB to PB growth visualizer)
- Module 03 `03-bandwidth.html` — bandwidth estimation with slider controls
- Module 04 `04-availability.html` — availability nines calculator (uptime/downtime breakdown)
- Module 05 `05-caching.html` — caching hit rate and cache sizing explorer
- Module 06 `06-read-replicas.html` — read replica sizing and load distribution
- Module 07 `07-queues.html` — message queue worker count and throughput
- Module 08 `08-cdn.html` — CDN offload cost and performance calculator
- Module 09 `09-sharding.html` — database sharding plan estimator
- Module 10 `10-latency.html` — latency budget breakdown across components
- Format: "Adjust sliders. See systems react. Build intuition."
- Each module built with Tailwind CSS
