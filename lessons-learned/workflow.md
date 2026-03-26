# Claude Code Workflow — Lessons Learned

How to work with Claude Code effectively across sessions — process, cadence, and context management.

---

## Branch → Commit → PR → Merge as a Unit

**Pattern:** Treat every logical chunk of work as a full git cycle, not a running stream of changes.

**Why:** A PR gives you a clean review point, a rollback target, and a named artifact in history. Committing directly to main loses that.

**Cadence that works well:**
1. Do all related changes in one session
2. Verify everything works
3. Branch → commit → PR → merge in one shot at the end

**Naming convention:** `feature/short-description`, `fix/what-was-broken`

---

## Plan Mode Before Implementation

**When to use it:** Any time the scope is unclear, the change touches many files, or you haven't done this type of change before.

> "let's plan and think for now"

**What it prevents:**
- Implementing the wrong thing across 10 files
- Structural decisions (folder names, HTML layout) that are hard to undo
- Missing edge cases that are obvious when written out but easy to skip when coding immediately

**When to skip it:** Small, well-understood changes (add a CSS rule, fix a typo, bump a threshold). Just do it.

---

## Verify on One File Before Batching

**Pattern:** Make a change on the reference file first, confirm it's correct, then say "do it for the rest."

```
1. Apply to Lab 01 → verify
2. "do it for labs 02–10"
```

**Why:** Batching before verification means 10 wrong files instead of 1. The verification step costs almost nothing.

---

## Context Window Management

**Problem:** Long sessions accumulate context. Claude's responses may become less precise as the window fills.

**Signals that context is getting long:**
- Claude starts re-explaining things it already did
- Responses reference earlier work incorrectly
- Summaries appear in the conversation

**Strategies:**
- Finish a logical chunk and commit/PR/merge before starting the next topic
- Use plan mode to capture the approach in a file — the plan persists even if context compresses
- Short, targeted sessions beat one long sprawling session

---

## Parallel vs Sequential Tool Calls

**Claude Code runs tool calls in parallel when they're independent.** Use this deliberately.

**Parallel is fine:**
- Reading multiple files at the same time
- Writing unrelated files simultaneously
- Running syntax checks while writing a changelog

**Must be sequential:**
- Read a file → then edit it
- Create a branch → then commit → then push → then PR

**Tip:** When you give Claude multiple independent tasks in one message, it can run them concurrently. One well-structured message often beats three back-and-forth exchanges.

---

## Stash When Switching Context Mid-Session

**Problem:** You're mid-change on one thing when a new request comes in on a different branch.

**Pattern Claude follows:**
```bash
git stash          # save in-progress work
git checkout main  # switch base
git checkout -b feature/new-thing
git stash pop      # restore if needed on new branch
```

**Lesson for you:** If Claude is mid-implementation and you pivot to a different task, say "stash this and start fresh" — Claude will preserve the work cleanly.

---

## CLAUDE.md as the Agent's Long-Term Memory

**What it is:** Project-level instructions that Claude reads at the start of every session. Equivalent to onboarding a new contractor — they read the README, then start work.

**What belongs in CLAUDE.md:**
- Post-write checklists (JS syntax check, changelog update, lessons-learned update)
- Debugging order (don't skip straight to runtime — check syntax first)
- Routing table (which changelog file maps to which folder)
- Behavioral rules (auto-suggest prompts, update living docs)

**What does NOT belong:**
- In-progress task state (use TodoWrite or a plan file for that)
- One-off notes from a single session
- Anything derivable from the code itself

**Lesson:** When you find yourself giving Claude the same instruction twice across sessions, that's a signal to add it to CLAUDE.md.

---

## Commit Messages as Session Summaries

**Pattern:** Write the commit message as if explaining the PR to a future reader who has no context.

**Good:**
```
Fix objectives resetting on refresh in Labs 02 and 08

- Lab 08: buildPacket() called saveState() before loadState() ran,
  overwriting stored state on every page load
- Lab 02: checkReflectionLock() was never called after loadState(),
  so overlay never re-rendered from restored state
```

**Bad:**
```
fix bug
```

**Why it matters:** `git log` is your session history. Good messages mean you can reconstruct what happened without re-reading all the code.

---

## Always Use a Local HTTP Server for Dev — Not `file://`

**Problem:** Opening `changelog/index.html` or `lessons-learned/index.html` directly from the filesystem (`file://`) causes `fetch()` to fail with a CORS or network error. The `.md` files can't be loaded.

**Fix:**
```bash
python3 -m http.server 8080
# then open http://localhost:8080/changelog/
```

**Why `file://` breaks `fetch()`:** Browsers block `fetch()` requests to other `file://` URLs as a security measure. Even same-folder fetches fail.

**Rule:** Any page that uses `fetch()` — including markdown viewers, data loaders, or API calls — must be served over HTTP, even locally.

---

## Archive Before Replacing — Don't Delete Immediately

**Context:** Database Labs had v1–v3 versions (customers/employees schema). Before creating the new HOS04/PE04 labs, old versions were moved to `archives/database/` rather than deleted.

**Why:** Old versions often contain working code snippets, UI patterns, or content that's useful for reference or recovery. Deletion is permanent; archiving costs almost nothing.

**Pattern:**
```
archives/
  database/
    v1-customers.html
    v2-employees.html
```

**Rule:** Before replacing a working file with a new version, move the old one to `archives/<section>/`. Only delete if you are certain it has zero reuse value.

---

## Commit Message Discipline Starts From Day One

**Context:** Early commits in this project used messages like `update`, `updates`, `fix`, `type`, `touch`. These are permanent and unsearchable.

**What was lost:** It's impossible to know from `git log` what changed in those early commits without reading the full diff.

**What good looks like** (from later in the project):
```
Cryptography labs: objectives overhaul, UX fixes, and bug fixes
Fix objectives resetting on refresh in Labs 02 and 08
```

**Rule:** Write commit messages as if the reader has no context. If you can't summarize what changed in one line, the commit is probably too large. Start this habit from commit #1 — retrofitting is not possible.
