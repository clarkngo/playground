# Refactoring — Lessons Learned

Patterns for restructuring code without changing behavior.

---

## Global Find-and-Replace Across Many Files

**Context:** Needed to rename "Why and Purpose" → "Why This Matters" across 10 HTML files (41 occurrences).

**Tool:** `sed -i` with a loop, or targeted per-file replacements.

```bash
# Replace in all 10 files at once
for f in cryptography-labs/*.html; do
  sed -i '' 's/Why and Purpose/Why This Matters/g' "$f"
done
```

**Lesson:** For purely textual renames across many files, a shell loop with `sed` is more reliable than editing files one by one. Less chance of missing an occurrence.

**Verify after:** Grep to confirm zero remaining old strings:
```bash
grep -r "Why and Purpose" cryptography-labs/
```

---

## Boolean → Set Refactor

**When to do it:** A boolean objective flag that should actually require multiple distinct interactions.

```javascript
// Before: just needs any interaction
let vpnDone = false;
function selectVPN(v) {
  vpnDone = true; // completes on first click
}

// After: needs all 4 specific scenarios
let vpnScenariosSeen = new Set();
function showVPNScenario(v) {
  vpnScenariosSeen.add(v);
  vpnDone = vpnScenariosSeen.size >= 4;
}
```

**When NOT to refactor:** If the objective genuinely is "do this once," keep the boolean. Don't over-engineer.

---

## Centralizing Objective Evaluation

**Pattern:** All objective checks live in one `updateObj()` function (or `checkReflectionLock()`). Individual interaction handlers just update state variables and call `saveState()` + `checkReflectionLock()`.

```javascript
// Interaction handler: only update state
function clickCIAPillar(pillar) {
  ciaPillarsSeen.add(pillar);
  saveState();
  checkReflectionLock();
}

// checkReflectionLock: evaluate all objectives from current state
function checkReflectionLock() {
  const checks = [
    { label: 'CIA Triad pillars', done: ciaPillarsSeen.size >= 3 },
    { label: 'Run simulator', done: simulatorUsed },
    // ...
  ];
  updateObj(checks);
  // unlock/lock submission based on all complete
}
```

**Why:** Keeps objective logic in one place. Adding a new objective = add one entry to `checks`, not scatter logic across multiple handlers.

---

## Removing Hardcoded Defaults Before State Restoration

**Context:** Lab 08 Demo 1 had `buildPacket('tunnel', 'esp')` called on init, which set a visual default AND saved that default to localStorage — overwriting any previously stored state.

**Refactor:**
1. Remove the hardcoded call with arguments
2. Set initial variables to `null`
3. Add a null guard in the rendering function
4. Call `buildPacket()` (no args) after `loadState()` to render from restored state

```javascript
// Before
document.addEventListener('DOMContentLoaded', () => {
  buildPacket('tunnel', 'esp'); // hard default, saves to localStorage
  loadState();
});

// After
document.addEventListener('DOMContentLoaded', () => {
  loadState();
  buildPacket(); // reads _currentMode/_currentProto from state, may be null
});
```

---

## Consolidating Repeated HTML Patterns

**Lesson:** When the same structural block (e.g., "Why This Matters" info box, objective overlay, footer nav) appears across 10 files, define a canonical template and copy it exactly.

**Anti-pattern:** Slight variations creep in between files over time — one file uses `class="info-box"`, another uses `class="tip-box"` for the same visual element. These diverge further with each edit.

**Maintenance rule:** When you find a variation from the canonical pattern, fix it back to the standard. Don't let drift compound.

---

## Consolidate Standalone Files Into a Folder When a Section Grows

**Context:** 18 standalone security HTML files were scattered at the root level. As the section grew, navigation and maintenance became unwieldy.

**Fix:** `[refactor]` Moved all 18 files into `security/` folder, updated all links.

**Signal that consolidation is needed:**
- More than ~5 files sharing a topic at the root level
- File names need a common prefix to be understood (`security-xss.html`, `security-sqli.html`, etc.)
- The homepage nav entry becomes a list instead of a single card

**Rule:** A folder is the right abstraction when a section has its own index page, shared assets, or more than one level of content.

---

## Consistent File Naming Convention: kebab-case

**Context:** `baron_smite.html` was renamed to `baron-smite.html`.

**Convention across this project:** All HTML files use kebab-case (hyphens, no underscores, all lowercase).

**Why it matters:**
- URLs on GitHub Pages are case-sensitive — `Baron-Smite.html` and `baron-smite.html` are different files
- Underscores can be invisible in some underlined link styles
- Consistency makes glob patterns and scripts predictable (`*.html`, `cryptography-labs/0*.html`)

**Rule:** When creating any new file, use kebab-case. When renaming, update every link that references it.
