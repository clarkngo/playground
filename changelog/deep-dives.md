# Changelog — Deep Dives

Path: `/deep-dives/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

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
