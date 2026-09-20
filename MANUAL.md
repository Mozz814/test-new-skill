# AI Skills Beginner Guide
## Research Scout: deployment, use, and persistent evidence memory

**Audience:** people new to AI. **Format:** 41 short lesson pages. Each `\\newpage` marker starts a PDF page when exported. **Outcome:** a working evidence-only skill in a GitHub repository.

\\newpage
## Page 1 — The goal

Research Scout has one job: collect traceable source material. It records what a source says and where it came from. It does not decide what the material means. This guide shows you how to install, use, and maintain that simple division of work.

\\newpage
## Page 2 — What is a skill?

An AI skill is a reusable job card for an AI. It tells the AI its role, steps, files, and limits. A focused skill is easier to check than a general conversation. Research Scout is a collector; analysis belongs in a separate step.

\\newpage
## Page 3 — Collector versus analyst

Think of a librarian and an expert. A librarian locates and catalogues books. An expert interprets them. Research Scout is the librarian. “This report states…” belongs here. “Therefore we should…” does not. Keep those two sentences in different workflows.

\\newpage
## Page 4 — Memory is a notebook

Chat messages can be temporary. Persistent memory is a real notebook the AI can reopen. Research Scout stores one notebook per topic in `memory/`. Future sessions read it before collecting, so earlier records stay visible and duplicate work is reduced.

\\newpage
## Page 5 — Package map

The repository contains `README.md` (overview), `SKILL.md` (AI instructions), `SKILL-MAINTENANCE.md` (improving the skill itself), `TEMPLATE.md` (blank notebook), `providers.md` (source options), `MANUAL.md` (this guide), `CHANGELOG.md` (skill version history), `memory/` (saved topics, plus `_skill-log.md`), `tools/` (provider wrappers), `scripts/lint_evidence.py` (automated boundary check), and `.github/workflows/` (CI). Keep these parts together in one repo.

\\newpage
## Page 6 — Start with README

Read `README.md` before changing files. It explains the purpose, safe requests, boundaries, and quick start. Share it with collaborators. The most important promise is that a source inventory is not a decision or recommendation.

\\newpage
## Page 7 — SKILL.md

`SKILL.md` is the AI’s operating manual. It says which files to read, how to create a topic, which metadata to capture, and how to answer. Normally you use it rather than edit it: ask a file-connected AI to read it before working.

\\newpage
## Page 8 — The template

`TEMPLATE.md` is copied to make a new topic notebook. It supplies a topic card, evidence-record structure, collection log, and duplicate list. Never fill in the master template. Keep it blank and save each working copy in `memory/`.

\\newpage
## Page 9 — Topic IDs

A topic ID becomes a filename. Use short lowercase words with hyphens: `urban-trees`, `home-insulation-nz`, or `adolescent-sleep-duration`. Avoid “final”, dates, or punctuation. Start a new ID when the research question changes materially.

\\newpage
## Page 10 — A good request

State subject, boundaries, topic ID, and the non-analysis rule. Example: “Use Research Scout to collect official and peer-reviewed sources about adolescent sleep duration since 2018. Save to `adolescent-sleep-duration`. Do not analyse.” A good request asks for material, not proof.

\\newpage
## Page 11 — Scope

Scope is a filing rule: who or what, where, when, which source types, and what to exclude. “Flood preparedness” is broad. “Household flood-preparedness guidance in New Zealand since 2020” is clearer. Record scope in the topic card before collecting.

\\newpage
## Page 12 — Traceable evidence

Save only identifiable source material: journal articles, agency pages, datasets, proceedings, and company primary reports. A record needs a title, location (URL or DOI), organisation or author where available, source type, access date, and access level.

\\newpage
## Page 13 — Labels are not ratings

“Government page”, “dataset”, and “journal article” describe source types. They do not declare which source is best. Research Scout records who is speaking and what was accessed. A later analysis process may assess relevance using explicit criteria.

\\newpage
## Page 14 — Provider wrappers

A provider wrapper is an adaptor for a source family. It accepts a query and returns structured retrieval facts. The core skill does not depend on a single search engine. This makes it possible to change providers without rewriting evidence rules.

\\newpage
## Page 15 — Provider choices

Use `scholarly-search` for research papers, `government-web` for agency material, `dataset-catalogue` for data metadata, `conference-search` for proceedings, `company-primary` for first-party reports, and `web-search` for other traceable primary sources. Prefer the narrowest suitable provider.

\\newpage
## Page 16 — Wrapper contract

Each wrapper returns provider ID, retrieval date, original query, and results. Each result should include title, author or organisation, date if known, URL, source type, access level, identifier, and returned text. Unknown fields stay unknown; never guess.

\\newpage
## Page 17 — Create a topic

Ask: “Use Research Scout to create `urban-trees` for sources about urban canopy and heat exposure. Limit it to official agencies, datasets, and peer-reviewed articles. Do not collect yet.” Then open `memory/urban-trees.md` and check its question and scope.

\\newpage
## Page 18 — Evidence records

Every source gets a stable ID such as `SRC-001`. Its table records the metadata. Its note describes only what the source says. It may include a short attributed excerpt. It also states whether the AI saw full text, an abstract, or only a summary.

\\newpage
## Page 19 — Faithful paraphrase

Good: “The agency page lists emergency water storage among household-preparedness items.” Bad: “Water storage is the most important action.” The bad sentence adds a ranking. Use “The report states…” or “The metadata describes…” to keep notes tied to the original.

\\newpage
## Page 20 — Short quotations

Quote only short passages when exact wording matters. Attribute the source and add a page or section if available. Prefer a short paraphrase and link for normal records. Do not copy a full article into memory, and do not pretend an abstract is a full text.

\\newpage
## Page 21 — Collection log

Every session adds a log row with date, action, provider, result, and memory change. Examples include “saved SRC-004–006” or “one duplicate skipped.” The log is your audit trail: it explains what happened even when no source was retrieved.

\\newpage
## Page 22 — Duplicate checking

Before saving, compare title, URL, DOI, report number, and identifier with existing records. Skip obvious duplicates and log the skip. If two records might be the same work, label the later one as a possible duplicate and name the related ID.

\\newpage
## Page 23 — Add to a topic

Ask: “Add up to five official agency pages about urban tree canopy to `urban-trees`. Check duplicates first; record limits; do not analyse.” The AI reads the existing file, assigns next IDs, appends records, and adds a log row. Earlier material must remain.

\\newpage
## Page 24 — Retrieve without searching

Ask: “List titles, dates, URLs, and IDs in `urban-trees`. Do not search or analyse.” This is a retrieval request. The AI should read the saved notebook only. Use it to prepare meetings, share a bibliography, or choose what you want to read.

\\newpage
## Page 25 — Analysis comes later

“What do these sources collectively mean?” is an analysis question. First collect and inspect the evidence. Then give a separate analyst clear criteria and the source inventory. Separating these steps lets a reader trace every later claim back to a saved source.

\\newpage
## Page 26 — Prepare the GitHub repository

Create a repository (or use an existing one) and put the whole package in it as one folder tree — do not split `SKILL.md` from `memory/` or `tools/` across repos. Protect the `main` branch: require a pull-request review before merging, and disable force-push on `main`. This one setting does most of the work of keeping evidence trustworthy — it means no change to a topic file reaches the record everyone reads without a human seeing the diff first. Do not commit personal passwords, credentials, or confidential data into any notebook.

\\newpage
## Page 27 — Getting the package in

Push the repository, or fork/clone it if it already exists elsewhere. Confirm `README.md`, `SKILL.md`, `SKILL-MAINTENANCE.md`, `TEMPLATE.md`, `providers.md`, `CHANGELOG.md`, `manifest.json`, `memory/`, `tools/`, `scripts/`, and `.github/workflows/` are all present at the top level — a partial checkout (e.g. `SKILL.md` alone, or missing `scripts/`) will run but silently skip the automated checks in Pages 33–34.

\\newpage
## Page 28 — Connect the AI

Give your AI environment read access to the repository and write access via pull requests (not direct pushes to `main`). Test access: ask the AI to read `README.md` and identify the memory directory. Then have it create a test topic on a branch and open a PR — confirm the PR shows up and the CI lint check runs on it before you do any real research.

\\newpage
## Page 29 — Team permissions

Give write access (the ability to push branches and open PRs) fairly freely — nothing reaches `main` without review anyway. Reserve **merge** access on `main` for people who should be approving research changes. Agree on topic IDs with collaborators to avoid parallel notebooks for the same question — a quick `git log --oneline -- memory/` shows every topic file anyone has touched recently.

\\newpage
## Page 30 — Full request example

“Collect up to eight traceable sources about New Zealand residential insulation programmes from 2020 onward. Prefer official agencies, programme documents, and datasets. Save to `home-insulation-nz`. Record title, organisation, date, URL, access level, and source-bound note. Do not analyse.”

\\newpage
## Page 31 — The collection receipt

The reply names the topic, counts collected and duplicate records, shows the memory path, lists source titles, and states access limits. It is a delivery receipt, not a conclusion. Open the memory file and check the fields before depending on it.

\\newpage
## Page 32 — No results

No results can be correct. Check whether scope is too narrow, wording differs locally, dates are restrictive, or the provider is unsuitable. Ask for alternate factual terms or an additional provider. Preserve the unsuccessful query in the collection log; do not invent citations.

\\newpage
## Page 33 — Missing metadata

Ask a targeted follow-up, for example: “Check whether the publisher page lists a date for SRC-004; do not change other fields.” If it remains unavailable, leave `Not available` and log the limitation. Never substitute an access date or estimated year.

\\newpage
## Page 34 — Unwanted analysis

If the AI writes “these sources show…” or recommends action, ask it to return a source inventory instead. Inspect the notebook for conclusions and remove or flag them. Do not lose useful analysis—move it into a separate, clearly labelled analysis document.

\\newpage
## Page 35 — Overwritten memory

If old records vanish, stop collection and run `git log --follow -- memory/<topic-id>.md`, then `git diff <old-commit> <new-commit> -- memory/<topic-id>.md` to see exactly what changed and in which commit. If the change shouldn't have happened, ask the AI to `git revert` that commit rather than editing the file back by hand — the revert itself becomes a visible, dated entry in history, same as a collection-log row. This is stronger than Drive's version history: every change to a topic file has an author, a message, and a diff, and — because `main` is protected — every one of them passed through a PR someone approved.

\\newpage
## Page 36 — Routine maintenance

Mark topics Active, Paused, or Complete in the topic card. Retain completed notebooks as evidence trails. Log link checks and metadata repairs. Start a new topic when the scope changes greatly rather than mixing unlike questions in one file.

\\newpage
## Page 37 — Adding a wrapper

Add a wrapper file in `tools/`, such as `regional-data-catalogue.md`. State its query inputs, allowed sources, returned contract fields, access limits, and no-result behaviour. Follow `providers.md`. Test it with one small query before using it broadly.

\\newpage
## Page 38 — Quality checklist

- Is the topic question and scope clear?
- Does each record have title, location, access date, and provider?
- Are limits labelled honestly?
- Are notes source-bound?
- Were duplicates checked?
- Does every session have a log entry?
- Are conclusions absent?
- Does `python scripts/lint_evidence.py memory/<topic-id>.md` pass locally, and does the CI check pass on the PR?

\\newpage
## Page 39 — When something keeps going wrong

A single odd result isn't a reason to change the skill. A pattern is: the same provider keeps missing coverage, the same kind of request keeps being ambiguous, or the linter keeps false-flagging the same wording. When you notice a pattern, don't ask the AI to fix `SKILL.md` mid-collection — ask it to add one line to `memory/_skill-log.md` and continue. Later, in a separate conversation, ask it to enter maintenance mode (`SKILL-MAINTENANCE.md`) and turn the log into a reviewed pull request. This keeps "collect evidence" and "improve the collector" from ever mixing in the same diff — the same separation the skill enforces for your own research.

\\newpage
## Page 40 — First-week plan

Day 1: set up the repo, branch protection, and CI; test access. Day 2: collect three sources for one narrow question, on a branch, and merge the PR yourself. Day 3: inspect every record and the CI run. Day 4: run a second collection and watch duplicate handling. Day 5: request an inventory, then use a separate analyst if needed.

\\newpage
## Page 41 — Glossary and next action

**Persistent memory:** a git-tracked file retained between sessions. **Provider wrapper:** a source-family adaptor. **Topic ID:** stable notebook filename. **Source-bound:** wording limited to what a source explicitly gives. **Evidence lint:** the automated check for banned analysis language and missing fields. **Maintenance mode:** the separate, explicitly-invoked process for changing the skill's own instructions. Your next action: set up the repository with branch protection, and create one small, carefully scoped topic.
