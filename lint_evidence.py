#!/usr/bin/env python3
"""Lint a Research Scout memory file for boundary violations.

Usage: python scripts/lint_evidence.py memory/<topic-id>.md [more files...]

Checks (all heuristic, not a substitute for human PR review):
  1. Banned analysis/recommendation phrases anywhere in the file.
  2. Each evidence-record block has the required fields present (not blank).
  3. No two records share the same URL/DOI (exact-match duplicate check).

Exits non-zero if any check fails, so it can gate a CI job.
"""
import re
import sys

BANNED_PHRASES = [
    r"\btherefore\b",
    r"\bwe recommend\b",
    r"\bwe suggest\b",
    r"\bthis shows that\b",
    r"\bthis proves\b",
    r"\bthis demonstrates\b",
    r"\bbest option\b",
    r"\bmost reliable\b",
    r"\bmost authoritative\b",
    r"\bshould be (adopted|used|chosen|preferred)\b",
    r"\bin conclusion\b",
    r"\boverall,? (the|these) (sources|evidence)\b",
    r"\bcollectively,? (the|these|it) (shows|show|suggests|suggest)\b",
]

REQUIRED_FIELDS = [
    "Source type",
    "Full citation or title",
    "URL or DOI",
    "Accessed",
    "Provider wrapper",
]


def check_banned_phrases(text: str) -> list[str]:
    hits = []
    for pat in BANNED_PHRASES:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            line_no = text[: m.start()].count("\n") + 1
            hits.append(f"line {line_no}: banned phrase matched /{pat}/ -> "
                        f"\"{m.group(0)}\"")
    return hits


def split_records(text: str) -> list[str]:
    # Records start with "### SRC-" headings; split on those.
    parts = re.split(r"(?=^### SRC-)", text, flags=re.MULTILINE)
    return [p for p in parts if p.startswith("### SRC-")]


def check_required_fields(record: str) -> list[str]:
    problems = []
    header = record.splitlines()[0].strip()
    for field in REQUIRED_FIELDS:
        pat = re.compile(rf"\|\s*{re.escape(field)}\s*\|\s*(.+?)\s*\|")
        m = pat.search(record)
        if not m or not m.group(1).strip() or m.group(1).strip().lower() in {
            "", "{{...}}",
        }:
            problems.append(f"{header}: missing or blank field '{field}'")
    return problems


def check_duplicate_identifiers(records: list[str]) -> list[str]:
    seen: dict[str, str] = {}
    problems = []
    for record in records:
        header = record.splitlines()[0].strip()
        m = re.search(r"\|\s*URL or DOI\s*\|\s*(.+?)\s*\|", record)
        if not m:
            continue
        ident = m.group(1).strip()
        if not ident or ident.lower() == "not available":
            continue
        if ident in seen:
            problems.append(
                f"{header}: URL/DOI also used by {seen[ident]} -> {ident}"
            )
        else:
            seen[ident] = header
    return problems


def lint_file(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        text = f.read()

    problems = []
    problems += [f"[phrase] {p}" for p in check_banned_phrases(text)]

    records = split_records(text)
    for record in records:
        problems += [f"[field] {p}" for p in check_required_fields(record)]
    problems += [f"[dup] {p}" for p in check_duplicate_identifiers(records)]

    return problems


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2

    all_problems: dict[str, list[str]] = {}
    for path in argv:
        problems = lint_file(path)
        if problems:
            all_problems[path] = problems

    if not all_problems:
        print(f"OK: {len(argv)} file(s) passed evidence lint.")
        return 0

    for path, problems in all_problems.items():
        print(f"\n{path}:")
        for p in problems:
            print(f"  - {p}")
    print(f"\nFAILED: {sum(len(p) for p in all_problems.values())} issue(s) "
          f"across {len(all_problems)} file(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
