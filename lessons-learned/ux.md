# UX Improvements — Lessons Learned

Design decisions and user experience patterns from the cryptography labs.

---

## Objectives Overlay Placement

**Decision:** Fixed to `bottom:1rem; right:1rem` (matching Lab 05 reference).

**DOM order matters:** When using `position:fixed` with a `bottom` anchor, the element that appears "above" visually must come **first** in the DOM. The container grows upward from the bottom anchor.

```html
<!-- Badge is first = appears above panel visually -->
<div id="obj-badge">📋 0/6 objectives ▼</div>
<div id="obj-panel" style="display:none">...</div>
```

**Chevron logic:**
- Panel hidden → badge shows `▼` (click to open, panel drops down)
- Panel visible → badge shows `▲` (click to close)

**Anti-pattern:** `top:1rem` places the overlay at the top of the viewport, which conflicts with the navbar and feels disconnected from the export/submit area.

---

## Objectives Ordered to Match Content Flow

**Decision:** Objective items in the overlay should follow the top-to-bottom order of content on the page.

**Why:** When users are working through a lab sequentially, glancing at the overlay should tell them "what's next" without mental reordering. A quiz objective appearing first when the quiz is the last section on the page creates confusion.

**Pattern:** Review the page from top to bottom, then order `checks[]` array to match that sequence.

---

## Two Choices vs Auto-Execute

**Context:** Lab 04 Message Signing originally had a single "Tamper Message" button that auto-executed the tamper. There was no option to verify correctly.

**Lesson:** When an action has a meaningful "right path" and a "wrong path" for learning, give users both options. Let them choose to verify OR tamper. Both complete the objective — the learning value is in making the choice consciously.

**UI pattern:**
```
Would you like to verify the signature? Choose one:
[✅ Verify Correct Signature]  [❌ Tamper & Re-verify]
```

---

## Demo Start State: No Default Selection

**Context:** Lab 08 Demo 1 had a button pre-highlighted on load (Tunnel + ESP). This confused the blank packet diagram — it implied a selection had been made before the user did anything.

**Decision:** Start with `null` mode and `null` protocol. Show placeholder text in the output area. Let the user make the first selection.

**Implementation:**
```javascript
let _currentMode = null;
let _currentProto = null;

function buildPacket() {
  if (!_currentMode || !_currentProto) {
    // show placeholder, don't render
    return;
  }
  // ... render packet
}
```

---

## "Why This Matters" Boxes

**Decision:** Renamed all "Why and Purpose" labels to "Why This Matters" across all 10 labs (41 occurrences).

**Why:** "Why This Matters" is more direct and personal. "Why and Purpose" sounds academic and passive.

**Lesson:** Consistent, human language across all sections reduces cognitive friction. When a label is used 41 times across 10 files, a small improvement compounds.

---

## Collapsible Terminal Instructions

**Context:** Lab 01 has a key pair generation exercise that requires opening a terminal. Instructions for macOS, Windows, and Linux were all visible at once, causing visual overload.

**Decision:** Each OS tab gets its own collapsible "How to open Terminal" panel. Users on macOS don't need to see Windows/Linux instructions.

**Pattern:** Content only relevant to one platform → collapsible, inside a platform tab.

---

## Export Success Banner

**Problem:** Users would click "Export PDF" and not know if it worked, especially when browser print dialog appears.

**Solution:** Show a green "✅ Export Complete" banner with an "Exit Lab" button after export. Auto-hides after 8 seconds.

**Lesson:** After any async or off-screen action (print dialog, PDF save), give explicit on-page feedback that something happened.

---

## Tour Modal vs Inline Instructions

**Decision:** Use a step-by-step modal tour for first-time users (Lab 01 only), always accessible via Help icon on all labs.

**Why modal instead of inline:**
- Inline instructions add page length and become visual noise for returning users
- A modal can be dismissed and re-triggered without changing the page layout
- Auto-popup only on Lab 01 respects the user's time on subsequent labs

**Key UX rule:** First-visit auto-popup is acceptable only once (Lab 01). Labs 02–10 never auto-popup — users can opt in via Help icon.
