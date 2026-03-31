# Changelog — Cryptography Labs

Path: `/cryptography-labs/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-31

### [ux] Lab 10 — Removed all "Capstone" wording
- Navbar subtitle: `Module 10 Lab · Capstone` → `Module 10 Lab · Emerging Crypto`
- Scenario box: removed "capstone lab" phrasing
- Demo 4 Why This Matters box: "capstone assessment" → "assessment"; "capstone security framework" → "security framework"
- Reflection section title: `💭 Capstone Reflection Submission` → `💭 Reflection Submission`
- Reflection label: `📝 Your Capstone Reflection` → `📝 Your Reflection`
- Print summary h1: removed `(Capstone)` from title
- Print summary h2: `Capstone Reflection` → `Reflection`
- `labCompleted` field: `Module 10 Lab (Capstone)` → `Module 10 Lab`

### [feature] Lab 10 — Demo 3 ZK proof now requires all 8 rounds
- Previously `zkDone=true` triggered at round 5; button disabled at round 8
- Now `zkDone` only sets to `true` at round 8 (when button disables)
- Objective label updated: `Completed ≥5 ZK proof rounds` → `Completed all 8 ZK proof rounds`
- Print summary row updated to `All 8 rounds` from `≥5 rounds`
- Intermediate state at rounds 5–7 now shows "Proving knowledge…" / "Getting convinced…" text

## 2026-03-25

### [ux] Lab 08 — Demo 1 IPsec: replaced 2-button bar with 2×2 combo grid
- Removed separate Transport/Tunnel and ESP/AH buttons
- Added 4 clickable combination cards in a 2×2 grid: Transport+ESP, Transport+AH, Tunnel+ESP, Tunnel+AH
- Each card shows description, turns green border when visited (✅), blue border when currently selected
- Replaced `showMode()`/`showProto()` with single `showCombo(mode, proto)` function that tracks combo keys (`'transport-esp'` etc.) in `ipsecSeen`
- `ipsecDone` triggers when all 4 combo keys are in the Set
- State persists/restores: visited cards restore green, last-selected card restores blue with diagram redrawn

### [ux] Lab 08 — Demo 1 IPsec now starts with no mode pre-selected
- Removed `action-btn-blue` from Tunnel Mode button; all 4 buttons start unselected
- Changed `_currentMode` and `_currentProto` initial values from `'tunnel'`/`'esp'` to `null`
- Added null guard in `buildPacket()`: returns early if either argument is null
- Added placeholder text in `#pkt-diagram`: "← Select a mode and protocol above to see the packet structure."
- Removed `buildPacket('tunnel','esp')` call from `DOMContentLoaded`
- `saveState`/`loadState` now persist `currentMode`/`currentProto`; on restore, redraws the diagram and highlights the correct buttons if a selection was previously saved

### [bug] Lab 08 — All objectives reset to 0 on every page refresh
- **Symptom:** Every refresh wiped all progress even though state was being saved
- **Root cause:** `DOMContentLoaded` called `buildPacket('tunnel','esp')` BEFORE `loadState()`. `buildPacket()` calls `saveState()` internally — so it saved a blank initial state to localStorage, then `loadState()` read that blank state back
- **Fix:** Reordered to `loadState()` → `buildPacket()` → `updateObj()` so state is restored before anything writes to localStorage

### [bug] Lab 02 — Objectives overlay reset to 0 on every page refresh
- **Symptom:** All objectives showed unchecked after refresh even though progress was saved in localStorage
- **Root cause:** `DOMContentLoaded` called `loadState()` but never called `checkReflectionLock()` afterward — state was restored in memory but the overlay was never re-rendered from it
- **Fix:** Added `checkReflectionLock()` after `loadState()` in the `DOMContentLoaded` handler

### [bug] Lab 08 — "Compared VPN protocols" objective triggered on first scenario instead of all 4
- **Symptom:** Selecting any single VPN scenario immediately completed the objective
- **Root cause:** `showVPNScenario()` set `vpnDone=true` unconditionally; `selectVPN()` also set it directly
- **Fix:** Added `vpnScenariosSeen` Set; `showVPNScenario()` now calls `.add(v)` and sets `vpnDone = vpnScenariosSeen.size >= 4`. Removed `vpnDone=true` from `selectVPN()`. All 4 scenarios (DPI firewall, Quantum, IoT, Federal) must be selected to complete the objective. Label updated to "Explored all 4 VPN scenarios". State persisted/restored via `saveState`/`loadState`.

### [bug] Lab 09 — "Explored all 4 KDFs" objective never triggered
- **Symptom:** Clicking all 4 KDF tabs (PBKDF2, bcrypt, Argon2id, HKDF) did not complete the objective
- **Root cause:** PBKDF2 is the default active tab rendered in HTML — `showKDFTab()` is never called for it on load, so `kdfTabsSeen` started empty. Clicking the other 3 tabs only reached `size=3`, never `>=4`
- **Fix:** After `loadState()` in `DOMContentLoaded`, seed `kdfTabsSeen.add('pbkdf2')` when the Set is empty (fresh session). Saved sessions restore their full Set via `loadState()` and are unaffected

### [ux] Labs 01–04 — Objectives overlay moved from bottom-right to top-right
- Changed `position:fixed;bottom:1.25rem;right:1.25rem` → `top:1rem;right:1rem` on `#obj-overlay` in all 4 labs
- Removed `position:absolute;bottom:calc(100% + .4rem)` from `#obj-panel`; replaced with `margin-top:.3rem` so panel opens downward (matching Lab 05 reference)
- Badge style simplified to match Lab 05 (`border-radius:8px`, removed backdrop-filter/box-shadow from badge)
- Chevron initial value changed from `▼` → `▲`; `toggleObj()` logic flipped to `▲` when open, `▼` when closed

### [feature] Lab 03 — All 4 AES cipher modes now required (was 2)
- Updated objective label to "Explore all 4 AES cipher modes (ECB, CBC, CTR, GCM)"
- Changed threshold in `checkReflectionLock()` from `modesExplored.size >= 2` to `>= 4`

### [feature] Lab 02 — "Click both cipher types" added as first objective
- Added `cipherTypesSeen` Set; `selectCipherType()` now calls `.add(type)`, `saveState()`, `checkReflectionLock()`
- New objective: "Click both cipher types (Stream & Block)" — requires `cipherTypesSeen.size >= 2`
- Placed first in overlay (cipher cards are top of page); badge updated from `0/4` to `0/5`
- State persisted as array and restored via `new Set()`

### [feature] Lab 01 — CIA Triad pillars added as lab objective (all 3 must be clicked)
- Replaced `ciaInteracted` boolean with `ciaPillarsSeen` Set tracking individual pillar clicks
- `selectCIA()` now calls `ciaPillarsSeen.add(pillar)` instead of setting a flag
- New objective: "Explore all 3 CIA Triad pillars (C, I & A)" — requires `ciaPillarsSeen.size >= 3`
- Objective placed first in overlay (pillars appear first in the page, above the simulator)
- Badge updated from `0/5` to `0/6`
- Submission report updated: shows `✅ All 3 explored` or `⚠️ N/3 explored`
- State serialized as array (`[...ciaPillarsSeen]`) and restored via `new Set(state.ciaPillarsSeen || [])`

### [ux] Labs 02–04 — Objectives overlay reordered to match lab content sequence
- **Lab 02** (`02-stream-block-ciphers.html`): Quiz moved to last; new order: Stream Cipher → Block Cipher → Explore parameters → Quiz
- **Lab 03** (`03-symmetric-encryption-mac.html`): Quiz moved to last; new order: AES cipher modes → HMAC tamper attack → AES-GCM bit-flip test → Quiz
- **Lab 04** (`04-asymmetric-encryption.html`): Quiz moved to last; new order: Diffie-Hellman walkthrough → Tamper signed message → TLS handshake animation → Quiz
- Labs 05–10 already had correct HTML-matching order; no changes made

### [ux] Lab 01 — Objectives overlay reordered to match lab content sequence
- Previous order had quiz first; reordered to match top-to-bottom position in the page:
  1. Run the CIA Triad Threat Simulator
  2. Click "Demonstrate Key Exchange"
  3. Upload your key pair terminal screenshot
  4. Complete the Password Task (Weak, Medium & Strong)
  5. Answer the mini quiz correctly

### [feature] Lab 01 — CIA Triad Threat Simulator added as lab objective
- Added `simulatorUsed` boolean state variable (saved/restored via `localStorage`)
- `simulateThreat()` now sets `simulatorUsed = true` and calls `saveState()` + `checkReflectionLock()` when the simulation completes (after CIA indicators update)
- New objective entry: "Run the CIA Triad Threat Simulator" added to `checks` array in `checkReflectionLock()`
- Objectives badge updated from `0/4` to `0/5`
- Reflection area remains locked until all 5 objectives are complete

### [bug] Labs 01–02 — "Enter your full name" input unstyled
- **Symptom:** Name input rendered without dark background, border, or text color — looked like a plain browser-default text box
- **Root cause:** Both labs used `class="lab-input"` on the input but had no `.lab-input` CSS rule defined (only `.reflection-input` was present)
- **Fix:** Added `.lab-input` and `.lab-input:focus` rules matching Lab 03 exactly (`background:#21262d`, `border:1px solid #30363d`, `padding:.45rem .6rem`, `color:#e6edf3`, `width:100%`, `font-size:.88rem`; focus `border-color:#58a6ff`)

### [bug] Lab 01 — Tour auto-popup not showing on first visit
- **Symptom:** Guided tour overlay never appeared on first page load despite code being present
- **Root cause:** `localStorage` key `cryptography-tour-seen-v1` was already set from prior development/testing sessions
- **Fix:** Bumped key to `cryptography-tour-seen-v2` in both `initTourSystem()` and `closeTour()` — clears stale flag, tour shows again for all users on next visit

### [ux] All labs — Renamed "Why and Purpose" → "Why This Matters"
- Applied to all 10 lab files (41 total occurrences) via global search-replace

### [ux] Lab 01 — Terminal open instructions added to key pair generator section
- Added collapsible `<details>/<summary>` block at the top of each OS tab (macOS, Windows, Linux) in the "Generate Your Own Key Pair" section
- macOS: Spotlight shortcut (⌘ Space), Finder path, Dock, iTerm2 note
- Windows: Win+X menu, Win+R run dialog, Start menu search, Git Bash option; admin warning for OpenSSH step
- Linux: Ctrl+Alt+T shortcut, desktop right-click, app menu search, Alt+F2 run dialog
- Added CSS for `▶`/`▼` arrow rotation on `details[open]` and marker reset across browsers

### [ux] Labs 01–02 — Quiz and reflection formatting aligned with Lab 03 reference
- Both labs: Replaced hardcoded quiz buttons (`check('A',this)`) with `QUIZ_OPTIONS` array + dynamic rendering + `checkQ()` function matching Lab 03
- Both labs: Each wrong answer now has distinct feedback text explaining why it's incorrect
- Both labs: Required reflection textarea wrapped in blue border box (`background:#0d1a2e;border:2px solid #1f6feb`) with `📝 Your Learning Reflection ★ Required` label
- Both labs: Lab Observations section reformatted with `(Optional)` tag, description text, and `border-top` separator
- Both labs: Student name input uses `class="lab-input"` consistent with Lab 03
- Both labs: `loadState()` quiz restoration updated to use `_correctBtn` + `QUIZ_OPTIONS` feedback instead of hardcoded strings
- Lab 01: Reflection title changed from `💭 Reflection & Learning Submission` to `💭 Learning Reflection Submission`
- Lab 01: Added guided questions `<ul>` block (5 questions + key question) before reflection-lock, matching Lab 03 structure
- Lab 01: `reflection-lock` inner content changed to `<p>` tag matching Lab 03 padding/weight

### [ux] All labs — Renamed "Why and Purpose" label to "Why This Matters"
- Replaced all instances of `🎯 Why and Purpose` with `🎯 Why This Matters` across all 10 lab files

### [ux] Labs 01–02 — Formatting consistency with Lab 03, tour system, navigation cleanup
- Added 6-step guided tour modal (CSS + HTML + JS) to both labs, matching Lab 03 structure
- Lab 01: `initTourSystem()` auto-shows tour on first visit via `cryptography-tour-seen-v1` localStorage key; `closeTour(completed)` shows `#help-reminder` toast when closed early to remind users of ❓ Help button
- Lab 02: `initTourSystem()` is empty (no auto-popup); tour accessible via ❓ Help button only
- Both labs: Removed forward navigation link (no `Lab 02 →` or `Lab 03 →`) — students get per-week links
- Lab 01 footer: changed to `Module 1` only (no links)
- Lab 02 footer: changed to `← Lab 01` + `Module 2` only (no forward link)
- Lab 02: Removed all stray `<!-- Change X: ... -->` comments from navbar, reflection-lock div, obj overlay, and JS
- Both labs: Added `<meta name="author">` and `<meta name="copyright">` tags
- Added `<div id="help-reminder">` toast element to Lab 01

### [ux] Labs 03–06 — Added "Why and Purpose" boxes to all demo sections
- Added blue-left-border Why/Purpose info box after each `<h4>` in all 4 demos of `03-symmetric-encryption-mac.html` (AES Mode, HMAC, AES-GCM, Padding Oracle)
- Added Why/Purpose boxes after each `<h4>` in all 6 demos of `04-asymmetric-encryption.html` (DH, RSA, Signatures, Hybrid, TLS, Entropy)
- Added Why/Purpose boxes after each `<h4>` in all 4 demos of `05-hash-algorithms.html` (Avalanche, Comparison, bcrypt, Birthday)
- Added Why/Purpose boxes after each `<h4>` in all 4 demos of `06-cryptography-standards.html` (NIST Levels, Algorithm Dashboard, FIPS, Agility)

### [ux] Lab 09 — Why/Purpose boxes, KDF/Mistakes/Lifecycle thresholds raised, hardware notes updated, language badges
- Added Why/Purpose boxes to all 4 demos (already present from prior pass; confirmed correct)
- Updated `KDF_HW_PRESETS` notes to match spec (e.g. `Single-core, ~1,200 PBKDF2 attempts/sec`)
- Updated initial `kdf-hw-note` text to match laptop preset note
- Changed `lifecyclesSeen.size>=3` to `>=5` (requires all 5 stages)
- Updated `updateObj()` labels: `'Fixed all 8 crypto implementation mistakes'` and `'Explored all 5 key lifecycle stages'`
- Added `lang` property to all 8 MISTAKES objects (JavaScript/Python/Java)
- Added language badge `<span>` to `buildMistakesGrid()` card headers using `m.lang`

### [ux] Lab 10 — Why/Purpose boxes, PQC requires 4 algorithms, ZK blue→green, checklist replaced with True/False quiz
- Added Why/Purpose box to Demo 4 (`✅ Demo 4 — Protocol Design Security Checklist`)
- Changed `pqcSeen.size>=3` to `>=4` (requires all 4 NIST PQC algorithms)
- Updated `updateObj()` label from `'Explored ≥3 NIST PQC algorithms'` to `'Explored all 4 NIST PQC algorithms'`
- Replaced all `🟦` with `🟩` in ZK demo (HTML and JS); updated prover state text from "blue" to "green"
- Replaced entire `CHECKLIST_SECTIONS` + `buildChecklist` + `updateChecklistScore` with `TF_QUESTIONS` array (20 true/false questions across 5 sections), `_tfAnswered` Set, `buildChecklist()`, `answerTF()`, and updated `updateChecklistScore()`
- Added `tfAnswered:Array.from(_tfAnswered)` to `saveState()`
- Added `_tfAnswered=new Set(s.tfAnswered||[])` to `loadState()`

### [ux] Lab 08 — Why/Purpose boxes for all 4 demos, Demo 1 requires all 4 combinations, vpnDone added to objectives
- Added "Why and Purpose" blue-left-border info boxes after each `<h4>` in all 4 demo boxes in `08-ipsec-tls.html`
- Demo 1: Updated description to add "Click all 4 buttons (Transport, Tunnel, ESP, AH) to complete this objective"
- Demo 1: Added `ipsecSeen` Set to track which mode/protocol buttons have been clicked; `ipsecDone` only set to `true` after all 4 values (transport, tunnel, esp, ah) are seen
- Demo 1: Updated `showMode()` and `showProto()` to call `ipsecSeen.add(m/p)` before `buildPacket()`
- Demo 1: Changed `buildPacket()` to set `if(ipsecSeen.size>=4)ipsecDone=true` instead of unconditionally
- Demo 1: Updated `updateObj()` label from `'Compared IPsec Tunnel vs Transport mode'` to `'Explored all 4 IPsec mode/protocol combinations'`
- Added `{done:vpnDone,label:'Compared VPN protocols'}` to `updateObj()` checks (was missing)
- Updated objective badge initial text from `0/5` to `0/6` to reflect the added vpnDone objective
- Updated `saveState()` to persist `ipsecSeen:Array.from(ipsecSeen)`
- Updated `loadState()` to restore `ipsecSeen=new Set(s.ipsecSeen||[])`

### [feature] Labs 01–02 — Help + Exit Lab buttons, Why/Purpose boxes, and footer nav links
- Added ❓ Help (`showTourModal(1)`) and ✕ Exit Lab (`closeTab()`) buttons to navbar in `01-cia-triad-authentication.html` and `02-stream-block-ciphers.html`
- Added `closeTab()` function to both files (tries `window.close()`, falls back to `history.back()`)
- Added "Why and Purpose" blue-left-border info boxes after each demo box `<h4>` in both files (3 boxes in Lab 01, 4 boxes in Lab 02)
- Added Lab 02 → footer nav link to `01-cia-triad-authentication.html`
- Added ← Lab 01 and Lab 03 → footer nav links to `02-stream-block-ciphers.html`

### [ux] Lab 07 — Why/Purpose boxes, objective label fixes, Demo 4 attack-card tracking
- Added "Why and Purpose" info box after each `<h4>` in all 4 demo boxes in `07-public-key-infrastructure.html`
- Demo 1: Updated description to add "Click all 11 fields to complete this objective" hint text
- Demo 1: Updated `updateObj()` label from `'Explored ≥5 certificate fields'` to `'Clicked all 11 certificate fields'`
- Demo 4: Added description paragraph "Click all 4 attack cards to complete this objective"
- Demo 4: Replaced `toggleAttack` function — now uses `attackCardsSeen` Set to track all 4 cards; sets `ctDone=true` only after all 4 are seen
- Demo 4: Updated `reportCT()` to only set `ctDone=true` if `attackCardsSeen.size>=4`
- Demo 4: Updated `updateObj()` CT label to `'Explored all 4 CT attack scenarios + reported'`
- Updated `saveState()` to persist `attackCardsSeen` array
- Updated `loadState()` to restore `attackCardsSeen` as a Set

## 2026-03-24

### [feature] Mini quiz system upgrade — per-option feedback for all 10 labs
- Added `feedback` property to every option in QUIZ_OPTIONS for labs 01–10
- Added `_correctBtn` tracking to DOMContentLoaded quiz builder in all 10 labs
- Replaced `check`/`checkQ` functions in all 10 labs with new shared logic:
  - Shows per-option feedback text on every click (not a generic hint)
  - Removes lock after correct answer — allows exploration of wrong answers post-solve
  - Keeps correct button green while exploring wrong answers after getting it right
- Updated `loadState` restore sections to remove hardcoded feedback text strings (no longer needed)

### [bug] Lab 06 Demo 2 — objective label was still showing "≥6" despite requiring all 12
- **Symptom:** Objective tracker showed "Identified ≥6 deprecated/current/PQC algorithms" even though the threshold was already `algosSeen.size===12`
- **Fix:** Updated objective label to "Explored all 12 algorithms in the dashboard"; updated print summary to "All 12 reviewed"
- **File:** `06-cryptography-standards.html`

### [feature] Lab 07 Demo 1 — require all 11 certificate fields clicked for objective
- **Previous behavior:** Clicking any 5 of the 11 cert fields marked the objective complete
- **New behavior:** All 11 fields must be clicked before `certFieldDone` is set to `true`
- **Fields:** version, serial, subject, issuer, validity, validto, pubkey, keyuse, san, sigalg, sig
- **File:** `07-public-key-infrastructure.html` (threshold changed from `>=5` to `>=11`)

### [feature] Lab 06 Module improvements — objectives refinement & reset functionality
- **Demo 1 (NIST Levels):** Changed objective to require all 5 security levels (1–5) to be clicked, not just one. Added tracking via `levelsSeen` Set
- **Demo 2 (Algorithm Dashboard):** Changed objective from "explore ≥6 algorithms" to "explore all 12 algorithms" for complete coverage
- **Demo 4 (Cryptographic Agility):** Added reset button to restart the era timeline. Clicking reset returns system to 2005 state, clears insights, re-enables upgrade button
- **Updated save/load:** Persists `levelsSeen` Set to localStorage for state restoration
- **File:** `06-cryptography-standards.html`

### [feature] Lab 07 Module 1 & 3 improvements — text clarity & enhanced learning content
- **Demo 1 (X.509 Certificate Anatomy):** Changed instruction from "Click any field" to "Click each field" to clarify that all fields should be explored
- **Demo 3 (Certificate Revocation: OCSP vs CRL):**
  - **Added comprehensive educational content:** Each method panel now includes what it is, pros/cons, implementation details, real-world trade-offs (privacy, latency, cache size)
  - **OCSP Stapling explanation:** Added context on how servers cache OCSP responses to eliminate privacy concerns
  - **Changed objective:** Both CRL and OCSP must be checked to complete the objective (tracked via `revocationMethodsChecked` Set)
  - **UI feedback:** Status label shows "Status: REVOKED" or "Status: Valid" with color coding; completion message updates when both methods are checked
  - **Enhanced comparison:** Side-by-side "Pros/Cons" boxes showing concrete trade-offs (file size, privacy leak, real-time nature)
- **Updated save/load:** Persists `revocationMethodsChecked` Set to localStorage
- **File:** `07-public-key-infrastructure.html`

### [feature] Lab 05 Demo 3 — Attacker hardware selector + dynamic crack-time comparison
- **Enhancement:** Demo 3 (Raw Hash vs bcrypt) now shows what CPU/GPU power was assumed for the calculation, and lets users switch between 4 hardware presets to see how crack times change
- **Hardware presets:**
  - 💻 Laptop CPU — Intel Core i7 (MD5: 500M/sec · bcrypt: 100/sec)
  - 🖥️ Gaming GPU — NVIDIA RTX 4090 (MD5: 68B/sec · bcrypt: 5K/sec) — **default**
  - 🔥 GPU Cluster — 8× NVIDIA H100 (MD5: 800B/sec · bcrypt: 50K/sec)
  - 🌐 Nation-State — 1,000-GPU botnet (MD5: 100T/sec · bcrypt: 5M/sec)
- **Dynamic crack-time panel:** Shows estimated time to crack the entered password under MD5 vs bcrypt for the selected hardware. Updates live as user types or switches hardware
- **Accurate keyspace detection:** Estimates character set from actual password content (lowercase, uppercase, digits, special chars) rather than a fixed `2^(len*6)` approximation
- **Inline hardware label:** bcrypt result description now shows "Selected hardware: ~X/sec" rather than hardcoded "~1,000 bcrypt/sec"
- **formatCrackTime():** Human-readable output from seconds → "T years", scaling through seconds/minutes/hours/days/months/years/K/M/B/T
- **UX lesson:** Students can see that bcrypt protects well even against GPU clusters, while MD5 crumbles at every level
- **File:** `05-hash-algorithms.html`

### [feature] Interactive "How Labs Work" tour guide — all 10 labs
- **Purpose:** Help new users understand lab structure, objectives, and workflow
- **Tour Content (6 Steps):**
  1. Welcome introduction to cryptography labs
  2. Objective system & 📋 tracker badge (bottom-right corner) explaining the objective unlock mechanism (varies by lab: 4-10 objectives)
  3. Interactive playgrounds & parameter exploration (choosing options, adjusting sliders, seeing results)
  4. Quiz mechanics & randomized answers (tests understanding, unlocks submission)
  5. Reflection submission (required) & Lab Observations field (optional)
  6. PDF export & exit process (see success banner with prominent exit button)
- **Entry Points:**
  - **Auto-popup on Lab 01 first visit:** Tour automatically shows on first load of Lab 01 (new users only)
  - **Help icon in navbar:** Available on all 10 labs (❓ button next to Reset and Exit buttons)
- **User Experience:**
  - Step-by-step modal with dark theme backdrop
  - Previous/Next buttons for navigation, Skip button to dismiss
  - Shows progress: "Step X of 6"
  - Dismissible with X button (top-right)
  - localStorage remembers: `cryptography-tour-seen-v1` (prevents annoying repeat auto-popups)
- **UX Benefits:**
  - New users get clear, guided onboarding without hunting through documentation
  - Highlights key concepts (objectives unlock submission, answers randomized, reflections required)
  - Can be replayed anytime via Help icon (great for users who need a refresher)
- **Technical:** Fixed-position modal with z-index 10001, smooth backdrop blur, single-page navigation, localStorage persistence

### [feature] Lab 04 Diffie-Hellman Step 4 — Disconnect After Key Exchange
- **Enhancement:** Added a 4th step to the Diffie-Hellman Key Exchange walkthrough
- **Scenario:** Shows what happens when Bob disconnects **after** the shared secret K is already established
- **Previous behavior:** Only 3 steps (agree on params → exchange public keys → compute shared secret), with a red "Disconnect" button available during steps 1-2 showing the vulnerability window
- **New behavior:** Step 4 demonstrates that once K is established and both parties have it, a disconnect has **no effect** — the key exchange is already complete and secure
- **UI:** Step 4 button shows "▶ Step 4 of 4: Simulate Disconnect" with output message confirming the shared secret is safe; button auto-disables after completion
- **Objective:** dhCompleted flag set when Step 4 finishes, allowing reflection submission to unlock
- **File:** `04-asymmetric-encryption.html` (lines 661-714 DH_STEPS array)

### [feature] Lab 04 Message Signing Yes/No Selection
- **Enhancement:** Changed single-button interface to two-button choice for message signing verification
- **Previous behavior:** Single "✏️ Tamper Message & Re-verify" button that always tampered the message
- **New behavior:** User can now choose:
  - **✅ Verify Correct Signature** — Shows the original message with valid signature, displays green "Signature Valid" message
  - **❌ Tamper & Re-verify** — Appends "[MODIFIED]" to message, shows verification failure with red error message
- **New function:** `runSignatureVerify()` shows successful verification flow (lines 832-850)
- **Updated function:** `runTamperSig()` moved after new function, behavior unchanged (lines 852-870)
- **Objective:** Either button choice sets `sigTamperTested = true`, unlocking reflection submission
- **UX benefit:** Users explore both success and failure paths at their own pace, understanding what correct vs. tampered signatures look like
- **File:** `04-asymmetric-encryption.html` (lines 305-316 UI, lines 832-870 functions)

### [ux] Export success banner with prominent exit button — all 10 labs
- **Problem:** After exporting a PDF, users see the print dialog close but have no visual cue to exit. They may forget that the "✕ Exit Lab" button is at the top of the page in the navbar.
- **Solution:**
  - After PDF export completes, a green success banner slides up from the bottom of the page
  - Banner displays: "✅ PDF exported successfully! Your lab work has been saved as a PDF. You can now exit the lab or continue exploring."
  - Includes a prominent "✕ Exit Lab" button matching the navbar button style
  - Banner auto-hides after 8 seconds, but user can click the Exit button anytime
- **UX benefit:** Users immediately see the success confirmation and have an easy way to exit without hunting for the navbar button
- **CSS:** Fixed positioning with slide-up animation; green accent color (#3fb950) matches lab theme

### [bug] Fixed broken previous lab navigation links — all 10 labs
- **Symptom:** Navigation footer displayed but "← Lab NN" links pointed to non-existent paths like `../week4-lab/04-asymmetric-encryption.html`
- **Root cause:** Files were reorganized from week-based folder structure (`week1-lab/`, `week2-lab/`, etc.) into a single `cryptography-labs/` folder, but navigation links weren't updated
- **Fix:** Updated all lab navigation links to use correct relative filenames in the same directory:
  - Lab 02 links to `01-cia-triad-authentication.html`
  - Lab 03 links to `02-stream-block-ciphers.html`
  - ... and so on through Lab 10
- **Lab 01:** No previous lab link (it's the first lab)
- **Deployment:** All links are now relative paths, so they work correctly when files are deployed together on any platform

### [ux] Exit Lab button — all 10 labs
- **Problem:** No way to close the tab after completing a lab; users had to manually close the browser tab.
- **Fix:** Added "✕ Exit Lab" button (red, top-right of navbar) to all 10 lab files.
- **Behavior:** Confirms with the user → `window.close()` → fallback redirects to `../index.html` if the tab can't be closed programmatically.
- **Files:** `01` through `10`

---

### [ux] Separated Learning Reflection from Lab Observations — all 10 labs
- **Problem:** Lab Observations textarea appeared immediately after the Learning Reflection textarea with no visual distinction. Users thought Lab Observations was the only required input and skipped the Learning Reflection.
- **Fix:**
  - Learning Reflection wrapped in a blue-bordered box (`border: 2px solid #1f6feb`) with a "★ Required" red label.
  - Lab Observations placed below a horizontal divider, labeled "(Optional)".
- **Files:** `01` through `10`

---

### [bug] Quiz correct answer always appeared in position B — all 10 labs
- **Problem:** Quiz options were hardcoded in HTML as static A/B/C/D buttons. The correct answer was always option B (or in a fixed position), making it easy to guess without reasoning.
- **Root cause:** `checkQ(this, 'B')` hardcoded — the letter, not the content, determined correctness.
- **Fix:**
  - Quiz options defined as a JS array with `{text, correct}` objects.
  - Array shuffled with Fisher-Yates on every page load.
  - Options rendered dynamically into `#quiz-options-grid`.
  - `checkQ(btn, isCorrect)` now receives a boolean flag, not a letter.
  - State restore no longer references hardcoded button index.
- **Files:** `01` through `10`

---

### [feature] Modules 07 & 10 upgraded to Module 06 format
- **Problem:** Modules 07 (PKI) and 10 (Emerging Crypto) used a simplified reflection box — no lock mechanism, no guided questions, no Lab Observations field. Inconsistent with modules 01–06 and 08–09.
- **Fix:**
  - Added `reflection-lock` div (red warning banner until objectives complete).
  - Added `submission-area` with `sub-area-locked` class, unlocked by `checkReflectionLock()`.
  - Added guided questions list (5 questions, module-specific).
  - Added `#lab-feedback` Lab Observations textarea.
  - `saveReflection()` and `loadState()` updated to persist lab-feedback.
  - PDF print-summary updated to include Lab Observations section.
- **Files:** `07-public-key-infrastructure.html`, `10-emerging-crypto.html`

---

### [ux] Removed forward navigation — all labs except Module 01 and 10
- **Problem:** Footer had both `← Previous` and `Next →` links, allowing students to skip ahead to labs they haven't completed yet.
- **Fix:** Removed all forward-facing `Week N →` anchor links from lab footers. Only backward navigation (`← Week N`) remains.
- **Module 01:** No backward or forward link existed; added `← Lab Home` link pointing to `../index.html`.
- **Files:** `02` through `09`
