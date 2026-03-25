# Changelog — Case Studies

Path: `/case-studies/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-24

### [bug] Hero title/subtitle unreadable — ECG canvas overlaps text
- **Symptom:** "System Design" and "Case Studies" title text was obscured by the animated green ECG heartbeat line and floating metric labels (99.99%, 200ms, 10K RPS)
- **Root cause:** Canvas drawn full-width at `H * 0.55` (center of hero), directly through the text area. Floating labels positioned at x=0.55, y=0.18 — overlapping the title.
- **Fix:**
  - Added radial dark vignette (`createRadialGradient`) over the center of the canvas, creating a readable backdrop behind the text
  - ECG line now fades to transparent (`globalAlpha`) in the center 40% of the canvas (x: 0.2–0.8)
  - Floating metric labels repositioned to far edges (x: 0.08, 0.88, 0.92) with reduced opacity
  - Hero `height` expanded from `200px` to `min-height:260px` to give badges breathing room
- **File:** `index.html`

---

## 2026-03-23

### [feature] Case Studies section created
- Hub page with animated heartbeat monitor canvas, red/orange accent theme
- 10 case studies across 4 sections: Scaling Stories, Data Architecture, Outages & Failures, Real-Time Systems
- Each case study includes: hero banner, narrative timeline, canvas architecture diagram (before/after toggle), "What Would You Do?" decision point, metrics panel, lessons, key takeaways

### Case studies included:
| # | Title | Key Concept |
|---|-------|-------------|
| 01 | Netflix: The Great Monolith Migration | Microservices decomposition, Chaos Engineering |
| 02 | Twitter: The Timeline Architecture Problem | Fan-out on write vs read, celebrity problem |
| 03 | Amazon Dynamo | Consistent hashing, vector clocks, sloppy quorums |
| 04 | Discord: Scaling to Trillions of Messages | MongoDB → Cassandra → ScyllaDB migration |
| 05 | GitHub's MySQL Outage | Split-brain, replication lag, Raft consensus |
| 06 | Uber Schemaless | Cell-based architecture, schemaless datastore |
| 07 | Slack: Scaling Real-Time Messaging | WebSocket fan-out, Flannel edge cache |
| 08 | Cloudflare: The Leap Second Bug | Monotonic clocks, NTP, negative durations |
| 09 | Instagram: 0 to 1M Users in 2 Months | Boring technology, vertical scaling first |
| 10 | Google Spanner: TrueTime | Atomic clocks, GPS, external consistency, CAP nuance |
