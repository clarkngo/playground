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
