# Research Scout

Evidence-only research collection with persistent, git-backed topic memory.

## What it does

Research Scout finds traceable source material, records what a source says and
where it came from, and keeps it in a durable per-topic file under `memory/`.
It does not interpret, rank, or draw conclusions from what it collects — that
is a deliberately separate job, done later by a human or a different workflow.

## What it will refuse to do

- Analyse, synthesise, or explain what sources "mean"
- Recommend a choice, policy, product, or action
- Rank sources as best, most reliable, or most authoritative
- Invent a source, quote, date, author, URL, DOI, or identifier

If you ask for analysis, it will offer to collect evidence first and hand off
to a separate analysis step.

## Package map

| File / folder | Purpose |
|---|---|
| `SKILL.md` | The AI's operating instructions — read this first if you're the AI |
| `MANUAL.md` | Human-facing guide: install, use, troubleshoot (40 short pages) |
| `SKILL-MAINTENANCE.md` | Separate, explicitly-invoked mode for improving this skill itself |
| `TEMPLATE.md` | Blank topic notebook — copied to start a new topic, never filled in directly |
| `providers.md` | Provider-wrapper contract and included source families |
| `tools/` | One wrapper spec per provider (`tools/README.md` has the details) |
| `memory/` | One git-tracked file per topic — the actual evidence notebooks |
| `scripts/lint_evidence.py` | Checks a memory file for banned analysis language and missing fields |
| `.github/workflows/lint-evidence.yml` | Runs the linter on every PR that touches `memory/**.md` |
| `CHANGELOG.md` | Versioned history of changes to the skill itself |

## Quick start

1. Clone or fork this repo; give the AI read access to the whole repo and
   write access to `memory/` (see MANUAL Page 26 for exact scopes).
2. Ask it to read `README.md` then `SKILL.md`.
3. Give it a scoped collection request, e.g.: *"Use Research Scout to collect
   official and peer-reviewed sources about adolescent sleep duration since
   2018. Save to `adolescent-sleep-duration`. Do not analyse."*
4. Review the resulting branch/PR diff before merging — the diff is your
   check that nothing but evidence records landed in `memory/`.

See `MANUAL.md` for the full guide, including GitHub setup, permissions, and
what to do if something looks wrong.
