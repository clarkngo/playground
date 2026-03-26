# Bug Fixes — Lessons Learned

Root causes and patterns for bugs found across the cryptography labs.

---

## Init Order: saveState Called Before loadState

**Symptom:** All objectives reset on page refresh. localStorage exists but is overwritten on load.

**Root cause:** A function called during `DOMContentLoaded` internally called `saveState()` — before `loadState()` had run. This overwrote the stored state with a blank default.

```javascript
// BAD — buildPacket() calls saveState() internally
document.addEventListener('DOMContentLoaded', () => {
  buildPacket('tunnel', 'esp'); // ← saves blank state!
  loadState();
  updateObj();
});

// GOOD — always load first
document.addEventListener('DOMContentLoaded', () => {
  loadState();
  buildPacket('tunnel', 'esp');
  updateObj();
});
```

**Rule:** Any function that may call `saveState()` must run AFTER `loadState()`.

**Labs affected:** Lab 08 (buildPacket), Lab 02 (checkReflectionLock missing after loadState)

---

## checkReflectionLock Not Called After loadState

**Symptom:** Objectives overlay appears empty/wrong on refresh even though state is correctly stored.

**Root cause:** `loadState()` restores variables, but `checkReflectionLock()` / `updateObj()` must be called to re-render the overlay from those variables.

```javascript
// After loadState(), always re-render:
loadState();
checkReflectionLock(); // re-evaluates all objectives, re-draws overlay
```

---

## Default Active Tab Never Triggers Tracking Function

**Symptom:** "Explored all 4 KDFs" objective gets stuck at 3/4 no matter what.

**Root cause:** PBKDF2 tab is pre-rendered active in HTML. `showKDFTab('pbkdf2')` is never called, so `kdfTabsSeen` starts empty every session. Clicking the other 3 tabs gets you to size=3, never 4.

**Fix:** Seed the default after `loadState()`, only on fresh sessions:
```javascript
loadState();
if (kdfTabsSeen.size === 0) {
  kdfTabsSeen.add('pbkdf2');
}
```

---

## Objective Completes on First Interaction Instead of All

**Symptom:** VPN scenarios objective marks complete on the first scenario click.

**Root cause:** `vpnDone = true` was set unconditionally on any click, not after all scenarios were visited.

**Fix:** Replace the boolean with a Set and check `.size >= N`:
```javascript
vpnScenariosSeen.add(scenarioId);
vpnDone = vpnScenariosSeen.size >= 4;
```

---

## Quiz Always Shows Option B as Correct

**Symptom:** No matter which option the user picks, option B is always the correct answer.

**Root cause:** Correct answer index was hardcoded to `1` (index of B) instead of being tied to `QUIZ_OPTIONS` shuffle randomization.

**Fix:** Randomize options on page load, track which shuffled index holds the correct answer.

---

## Tour Auto-Popup Not Showing

**Symptom:** Tour modal never opens on Lab 01 first visit.

**Root cause:** `cryptography-tour-seen-v1` was already set in localStorage from earlier testing. The init check `if (!localStorage.getItem(TOUR_KEY))` evaluated false.

**Fix:** Bump the version key so all users get a fresh state:
```javascript
const TOUR_KEY = 'cryptography-tour-seen-v2';
```

**Lesson:** During feature development, manually clear localStorage or use versioned keys so your own testing doesn't mask first-visit behavior.

---

## JS Syntax Error Causes Blank Page / No Interactivity

**Symptom:** Page loads but nothing works — buttons do nothing, canvas is blank.

**Root cause:** A JS syntax error (e.g., apostrophe inside single-quoted string: `'don't'`) causes the entire `<script>` block to fail silently. No functions are defined.

**Diagnosis checklist (in order):**
1. `node --check` the script block — if it fails, nothing in the script runs
2. Check browser console for `SyntaxError`
3. Only then investigate runtime/logic issues

**Prevention:** Run `node --check` after every HTML file edit. See CLAUDE.md for the exact command.

---

## Broken Previous Lab Navigation Links

**Symptom:** "← Previous Lab" buttons 404.

**Root cause:** Links were generated as `../week*/lab.html` (old path structure) instead of the actual filenames.

**Fix:** Use correct relative filenames: `../cryptography-labs/02-stream-block-ciphers.html`.

**Lesson:** When copy-pasting nav templates, always verify the actual file paths.

---

## Hardcoded Count String Doesn't Match Actual Data

**Symptom:** Tour Step 2 said "you have 4 objectives" but labs have between 4 and 10 objectives depending on complexity.

**Root cause:** Count was hardcoded as a string literal instead of being derived from the actual `checks.length`.

**Fix:** Remove the hardcoded number. Either derive it dynamically or use a range ("a few objectives").

**General rule:** Any string that says "you have N of X" is a maintenance liability. Either pull the value from data or keep it vague enough to stay accurate.

---

## Script Executes Before Its Target DOM Element Exists

**Symptom:** Copyright year span displayed empty — no year shown in footer.

**Root cause:** `document.getElementById('copyright-year')` ran inside the main `<script>` block, before the `<footer>` HTML was rendered.

**Fix:** Move the script tag to after the HTML element it targets, or wrap in `DOMContentLoaded`.

**Pattern:** This is the same class of bug as saveState-before-loadState — execution order matters. Scripts at the top of `<body>` can't query elements defined later.

---

## Canvas Animation Overlapping Page Content

**Symptom:** Case Studies hero title and subtitle were unreadable — text was there but invisible because the ECG canvas animation was painted on top.

**Root cause:** Canvas element had a stacking context that placed it above the text, or `position` / `z-index` wasn't set to keep it behind.

**Fix:** Ensure canvas sits behind text content with `position: absolute; z-index: 0` and the text container has a higher `z-index`.

**General rule:** Decorative canvas animations should always be `position: absolute` within a `position: relative` container, with text at a higher z-index.

---

## Threshold Raised in Code But Label Not Updated

**Symptom:** Lab 06 Demo 2 objective label said "≥6 algorithms" but the code already required all 12. Users who completed the real requirement saw a misleading label.

**Root cause:** The threshold in `updateObj()` was raised from 6 to 12, but the human-readable label string was not updated.

**Fix:** Treat the label and the threshold as a pair — changing one always means updating the other.

**Related:** Same family as "Badge count must match checks array length" — any time a number appears in both code and UI text, they must stay in sync.
