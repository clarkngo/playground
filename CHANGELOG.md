# Playground Changelog

All changes across the project, newest first.
Detailed entries are in `changelog/<collection>.md`.

Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-24

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
