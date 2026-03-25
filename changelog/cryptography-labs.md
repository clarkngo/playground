# Changelog — Cryptography Labs

Path: `/cryptography-labs/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

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
