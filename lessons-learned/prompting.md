# Prompting — Lessons Learned

How to get better results from Claude by improving how you phrase requests.

---

## Be Specific About the Reference File

**What you said:**
> "make the lab objective overlay to be at the top instead of bottom"

**What happened:** Claude interpreted "top" as `position: top: 1rem` (top of viewport), which was wrong.

**What you meant:** The badge should be visually above the panel (but both stay at the bottom).

**Better prompt:**
> "Follow Lab 05's placement of the objectives overlay exactly — position and DOM order."

**Lesson:** When you have a file that already does what you want, name it explicitly as the reference. "Follow Lab 05" is clearer than describing the behavior in words.

---

## Describe the Symptom, Not the Presumed Fix

**What you said:**
> "state should be saved localStorage browser. when i refresh. the objectives resets."

**What Claude did:** Found the root cause (saveState called before loadState) and fixed it.

**Why this worked:** You described what you observed (objectives reset on refresh), not what you thought was wrong. Describing symptoms lets Claude find the actual root cause rather than applying a surface-level patch.

**Tip:** If you have a hypothesis about the cause, you can mention it — but lead with the symptom first.

---

## One Lab at a Time vs "Do It for All"

**Pattern you used:**
1. First, describe and verify the change on one lab
2. Then: "do it for lab 2 to 10"

**Why this works well:** The first lab is a test case. If it's wrong, you correct it before applying to all 10. This saves 9 incorrect edits.

**When to batch:** Only batch after you've confirmed the change is exactly right on the reference file.

---

## Reference Existing Working Code

**What you said:**
> "use Lab 03 as a reference to change the formatting of Lab 01 and Lab 02 mini quiz"

**Why this is effective:** Instead of describing the visual formatting in detail (font sizes, colors, spacing), you pointed to something that already exists and already looks correct. Claude reads the reference and matches it.

**General pattern:**
> "Match the [X] from [existing file/lab]"
is better than describing X from scratch.

---

## When Claude Misunderstands: Say "No" and Point to the Correct Reference

**What happened:** Claude misread the overlay positioning request twice.

**What worked:**
> "noo. follow lab 05 placement of the chevron with panel. fix lab 01 to 04"

**Lesson:** When Claude gets something wrong, a short "no" plus the correct reference file is enough to redirect. You don't need to fully re-explain the requirement.

---

## Compound Requests: List Them

**What you said:**
> "for all labs, change 'why and purpose' to 'Why This Matters' / use Lab 03 as a reference to change the formatting of Lab 01 and Lab 02 mini quiz and Learning Reflection Submission"

**What helped:** The `/` separator made it clear these were two separate tasks.

**Better practice:** Use a numbered list for compound requests:
> "1. Change 'Why and Purpose' to 'Why This Matters' in all labs
> 2. Use Lab 03 formatting for Lab 01 and 02 quiz and reflection sections"

This reduces ambiguity about whether it's one request or multiple.

---

## Specify Completion Criteria

**What you said:**
> "module 9 Explored all 4 KDFs... not triggering correctly when clicked all 4 KDFs"

**What you implicitly meant:** The objective should trigger when all 4 have been clicked at least once.

**Better prompt:**
> "Explored all 4 KDFs objective: should complete only after PBKDF2, bcrypt, Argon2id, and HKDF tabs have each been clicked at least once."

**Why:** Specifying exactly what "correct" means reduces the chance of a partial fix (e.g., just lowering the threshold to 3).

---

## Planning Mode vs Execution Mode

**Pattern:** You explicitly asked to "plan and think for now" before implementing a new section (lessons-learned folder).

**Why this is effective:** Planning mode lets you review the approach, catch scope issues, and confirm the design before any code is written. This is especially valuable for:
- New folder/section structures (hard to rename later)
- Changes that affect all N files
- Features where the UX isn't fully clear yet

**Lesson for yourself:** If you're unsure of the direction, say "let's plan first." You can always say "looks good, proceed" to start implementation.

---

## Short Confirmations Move Things Forward

**Effective patterns you used:**
- "do it for lab 2 to 10" — batch apply after first verification
- "noo. follow lab 05" — short redirect
- "gh auth login" — direct command to execute

**Lesson:** You don't need long explanations to redirect or confirm. Short, direct responses are fine and keep momentum.
