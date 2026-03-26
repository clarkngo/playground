# Feature Development — Lessons Learned

Patterns and decisions from building interactive lab features.

---

## Set-Based Objective Tracking

**Context:** Labs need to track whether a user has visited all N items (tabs, cards, buttons) before completing an objective.

**Lesson:** Use `new Set()` instead of a boolean or counter.

```javascript
// BAD — loses which specific items were seen
let modesExplored = 0;
modesExplored++;

// GOOD — tracks exactly what was interacted with
let modesExplored = new Set();
modesExplored.add('ecb');
// Objective: modesExplored.size >= 4
```

**Why it matters:** A counter can be incremented multiple times on the same item. A Set is idempotent and self-documenting.

**Serialization pattern for localStorage:**
```javascript
// Save
saveState() {
  localStorage.setItem('state', JSON.stringify({
    modesExplored: [...modesExplored],
    // ...
  }));
}

// Restore
loadState() {
  const s = JSON.parse(localStorage.getItem('state') || '{}');
  modesExplored = new Set(s.modesExplored || []);
}
```

---

## Default-Active Element Seeding

**Context:** When a tab or button is pre-highlighted in HTML (e.g., PBKDF2 is the default active KDF tab), the corresponding tracking function (`showKDFTab()`) is never called for it — so it's never added to the tracking Set.

**Lesson:** After `loadState()`, seed the default-active element into its Set if the Set is empty (first visit only).

```javascript
// After loadState():
if (kdfTabsSeen.size === 0) {
  kdfTabsSeen.add('pbkdf2'); // default active tab
}
```

**Why it matters:** Users who never click away from the default still need credit for "seeing" it. This prevents a permanent 3/4 stuck state.

---

## 2×2 Combo Grid vs Sequential Selectors

**Context:** Demo 1 in Lab 08 had separate "Mode" and "Protocol" buttons, requiring users to try 4 combos across 2 separate axes.

**Lesson:** When all combinations are equally important, show them as a flat grid of cards rather than two separate selectors.

**Before:** 2 mode buttons + 2 protocol buttons (4 clicks but conceptually unclear)
**After:** 4 combo cards (Transport+ESP, Transport+AH, Tunnel+ESP, Tunnel+AH) — each is one click, meaning is immediately visible, visited state shown with green border.

**Key implementation detail:** Track combos as composite keys:
```javascript
const ipsecSeen = new Set();
function showCombo(mode, proto) {
  ipsecSeen.add(`${mode}-${proto}`); // e.g. 'transport-esp'
  // Objective: ipsecSeen.size >= 4
}
```

---

## localStorage Key Versioning

**Context:** During testing, a localStorage key gets set to `true`. Later changes to the feature mean the old flag no longer matches the new behavior. Users (or yourself during development) get stuck in a stale state.

**Lesson:** Bump the version suffix when the meaning of a key changes.

```javascript
// Old — stale flag may be set
const TOUR_KEY = 'cryptography-tour-seen-v1';

// New — fresh start for all users
const TOUR_KEY = 'cryptography-tour-seen-v2';
```

**When to bump:** Any time the behavior controlled by that key changes in a way where the old value would cause wrong behavior.

---

## Objective Badge Count Must Match Array Length

**Context:** Added a new objective (CIA Triad pillars) without updating the badge from `0/5` to `0/6`.

**Lesson:** Always sync the badge text to `checks.length` when adding or removing objectives.

```javascript
// In updateObj():
badge.textContent = `${completed}/${checks.length} objectives`;
```

Or hardcode it in the HTML and double-check it matches every time the `checks` array changes.
