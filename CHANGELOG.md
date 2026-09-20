# Changelog

All notable changes to Research Scout itself (not to any topic's evidence)
are recorded here. Evidence history lives in `git log` for `memory/**.md`.

## 1.1.0 — 2026-09-20

- Migrated storage model from Google Drive to git. `memory/` files are now
  updated via branch + PR instead of in-place editing, with a protected
  `main` requiring review before merge.
- Added `scripts/lint_evidence.py` and a matching GitHub Action
  (`.github/workflows/lint-evidence.yml`) that automatically checks every PR
  touching `memory/**.md` for banned analysis language, missing required
  fields, and duplicate URL/DOI identifiers. Previously this was enforced
  only by prose instructions in `SKILL.md`.
- Added `SKILL-MAINTENANCE.md`: a separate, explicitly-invoked mode for
  improving Research Scout's own instructions, fed by a friction log
  (`memory/_skill-log.md`) rather than by the collector deciding to change
  itself mid-task.
- Fixed `README.md`, which previously described only the `tools/` folder
  despite `manifest.json` calling it the package overview. That content
  moved to `tools/README.md`; `README.md` is now a real top-level overview.
- `SKILL.md`: added git workflow steps (branching, commit message format,
  PR-not-self-merge, recovery via `git log`/`git diff`/`git revert` instead
  of manual version-history inspection).

## 1.0.0

- Initial release: evidence-only collection, provider wrapper contract,
  Google-Drive-based persistent memory.
