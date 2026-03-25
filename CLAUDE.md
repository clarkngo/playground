# Playground — Agent Instructions

## After Writing or Editing HTML Files

Always run a JS syntax check on any HTML file you write or edit that contains `<script>` blocks:

```bash
sed -n '/<script>/,/<\/script>/p' <file> | grep -v '<.script' | node --check /dev/stdin
```

Or using line numbers if you know them:

```bash
sed -n '327,1006p' <file> > /tmp/check.js && node --check /tmp/check.js
```

Fix any syntax errors before declaring the task done.

**Common causes of JS syntax errors in HTML files:**
- Single-quoted strings containing apostrophes (`it's`, `don't`, `can't`) — use backticks instead
- Template literals with unescaped backticks
- Missing closing brackets or braces
- HTML entity characters (`&amp;`, `&lt;`) accidentally inside `<script>` blocks

---

## Debugging a Blank Canvas or Missing UI

Follow this order — do not skip ahead:

1. **Check if the script parsed** — extract the `<script>` block and run `node --check`. If the script has a syntax error, nothing inside it runs. This is the most common cause of "nothing works" bugs.
2. **Check if globals from the script exist** — run `typeof window.X` for any global the script should define. If `undefined`, the script didn't execute.
3. **Check browser console logs** — use `preview_console_logs` to look for runtime errors.
4. **Manually draw a test shape** — use `preview_eval` to call `ctx.fillRect(...)` directly. If it works, the canvas is fine; the issue is in initialization logic.
5. **Only then** investigate runtime/timing issues (layout not ready, `clientWidth` = 0, etc.)

---

## Post-Write Verification Checklist

After writing any `.html` file:

- [ ] JS syntax check passes (`node --check`)
- [ ] Page loads without console errors (`preview_console_logs`)
- [ ] Key interactive elements are visible (`preview_screenshot`)
- [ ] Changelog updated (see below)

---

## Changelog Update — Required After Every Change

After **any** file is created or edited in this project, update the changelog before declaring the task done.

### Which files to update

| What changed | Update this file |
|---|---|
| `coding-agents/` | `changelog/coding-agents.md` |
| `case-studies/` | `changelog/case-studies.md` |
| `trainer-series/` | `changelog/trainer-series.md` |
| `cryptography-labs/` | `changelog/cryptography-labs.md` |
| `encryption-labs/` | `changelog/encryption-labs.md` |
| `crypto-vuln-labs/` | `changelog/crypto-vuln-labs.md` |
| `security/` | `changelog/security.md` |
| `system-design-learn/` | `changelog/system-design-learn.md` |
| `system-design-labs/` | `changelog/system-design-labs.md` |
| `system-design-metrics/` | `changelog/system-design-metrics.md` |
| `system-design-activities/` | `changelog/system-design-activities.md` |
| `system-design-games/` | `changelog/system-design-games.md` |
| `digital-twin/` | `changelog/digital-twin.md` |
| `wild-rift/` | `changelog/wild-rift.md` |
| `history-timelines/` | `changelog/history-timelines.md` |
| `simulators/` | `changelog/simulators.md` |
| `prototypes/` | `changelog/prototypes.md` |
| `database-labs/` | `changelog/database-labs.md` |
| `cityu-tools/` | `changelog/cityu-tools.md` |
| `index.html`, `CLAUDE.md`, shared infra | `changelog/root-playground.md` |

Always **also** add a one-line summary entry to `CHANGELOG.md` (root) under today's date.

### Tag reference

| Tag | Use when |
|---|---|
| `[feature]` | New file, section, or capability added |
| `[bug]` | Something was broken and is now fixed |
| `[ux]` | Layout, flow, or usability improvement |
| `[refactor]` | Code restructured without changing behavior |

### Entry format

```markdown
## YYYY-MM-DD

### [tag] Short title
- Bullet with specific detail
- Another bullet if needed
```

### Rules

1. Use today's date from `currentDate` context (or run `date +%Y-%m-%d`)
2. Add new entries at the **top** of the file (newest first)
3. Be specific — name the files, functions, or UI elements affected
4. If fixing a bug, include: **Symptom**, **Root cause**, **Fix**
5. If multiple sections were changed in one task, update each collection file
