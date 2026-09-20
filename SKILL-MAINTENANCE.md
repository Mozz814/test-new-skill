---
name: research-scout-maintenance
description: Improve Research Scout itself — its SKILL.md, wrappers, or lint rules. Use ONLY when explicitly asked to review, fix, or extend the skill's own instructions, never during an ordinary evidence-collection request.
---

# Research Scout — self-maintenance mode

## Why this is a separate file

Research Scout's whole design rests on one split: collecting evidence is not
the same job as deciding what it means. That split has to apply reflexively
to the skill itself — deciding "what should Research Scout do differently"
is a different job from "collect this evidence," and it must not happen
inside a collection run. If you're in the middle of collecting and you
notice something that should change about the skill, log it (see below) and
keep collecting. Don't switch modes mid-task.

Enter this mode only when the user explicitly asks to review, audit, tune,
or extend Research Scout itself.

## Inputs this mode reads

1. `memory/_skill-log.md` — the friction log. Each entry is one line, added
   by the collector during ordinary use whenever something recurring got in
   the way (a missing wrapper, an ambiguous scope pattern, a lint false
   positive, a dedup miss). This file is signal, not evidence — it does not
   follow the evidence-record format and is never treated as a source.
2. Recent PR history on `memory/**` (via `git log`) — look for repeated
   correction commits, which often mean an instruction is unclear rather
   than that the AI made an isolated mistake.
3. Any specific complaint the user gives directly this session.

## Workflow

1. **Read the log and recent history.** Group entries into patterns — three
   people hitting the same missing wrapper is a signal; one odd request
   isn't.
2. **Propose a specific, minimal change.** A new wrapper entry in
   `providers.md` + a stub in `tools/`, a clarified sentence in `SKILL.md`,
   a new banned phrase in `scripts/lint_evidence.py`. Avoid rewriting large
   sections speculatively — every change should trace back to a logged
   pattern or a stated complaint, the same way an evidence note traces back
   to a source.
3. **Branch: `maintain/<short-description>`.** Never edit `SKILL.md`,
   `providers.md`, or `scripts/lint_evidence.py` directly on `main`.
4. **Update `CHANGELOG.md`** with the change and bump `manifest.json`'s
   `version` (patch for wording clarifications, minor for new
   wrappers/capabilities, major for changes to the non-negotiable boundary
   itself — which should be very rare and flagged clearly to the user).
5. **Open a PR. Do not merge it yourself.** A human reviews changes to the
   skill's own instructions the same way they'd review a change to the
   evidence boundary itself — this is the one thing in the whole package
   that most needs a second pair of eyes, since it's the thing that governs
   everything else.
6. **Once merged, clear the log entries that were addressed** from
   `memory/_skill-log.md`, leaving unaddressed ones in place with a short
   note on why they weren't actioned yet.

## What this mode must never do

- Never weaken the non-negotiable boundary (`SKILL.md`'s "Do not" list) to
  make collection "easier" — if the log shows the boundary is being hit
  often, that's a signal to clarify the instruction or add a wrapper, not to
  loosen the rule.
- Never merge its own PRs.
- Never treat a single collection session's frustration as sufficient
  evidence for a change — that's what the log's pattern-grouping step is for.
- Never fold maintenance work into a collection commit. Keep the two commit
  histories (evidence in `memory/`, skill changes everywhere else) visibly
  separate, so a reviewer auditing evidence integrity never has to also
  reason about skill-logic changes in the same diff.
