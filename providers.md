# Provider wrappers

Provider wrappers are small, replaceable instructions or tools that obtain records from one source family. The core skill never assumes a particular search engine or website; it asks a wrapper for structured results, validates them, and writes them to topic memory.

## Standard wrapper contract

Every wrapper must return only verifiable retrieval data:

```json
{
  "provider_id": "example-provider",
  "retrieved_at": "2026-09-19",
  "query": "original query text",
  "results": [
    {
      "title": "Exact source title",
      "authors_or_organisation": "Name",
      "published_date": "2025-03-12",
      "url": "https://example.org/source",
      "source_type": "journal_article",
      "access_level": "abstract",
      "snippet_or_excerpt": "Text returned by the provider",
      "identifier": "doi, report number, or provider ID"
    }
  ],
  "limitations": ["Any material limitation"]
}
```

Wrappers must not analyse, rank, recommend, alter quotations, conceal limits, or manufacture missing fields.

## Included wrapper specifications

| Provider ID | Intended sources | Typical use | Required caution |
|---|---|---|---|
| `scholarly-search` | Peer-reviewed articles and preprints | Research questions | Clearly label abstracts versus full text |
| `government-web` | Government departments and public agencies | Public guidance, statistics, policy records | Record jurisdiction and page update date |
| `dataset-catalogue` | Official or reputable data catalogues | Dataset discovery and metadata | Do not infer trends from the data |
| `conference-search` | Conference proceedings and programmes | Emerging work | Record publication status if stated |
| `company-primary` | Company reports, filings, technical pages | First-party claims | Identify organisation as the source |
| `web-search` | Other traceable primary sources | Gap-filling discovery | Prefer original material over commentary |
| `social-public` | Public LinkedIn posts and other public social posts | Discovery of current stakeholder statements | Treat posts as attributed statements, not verified facts |
| `forum-public` | Public forums, community discussions, and comments | Discovery of experiences, concerns, and leads | Treat every post as an unverified, attributed viewpoint; never generalise it to an industry fact |

## Adding a wrapper

Create a file in `tools/` named after the provider, for example `tools/government-web.md`. State its inputs, allowed sources, returned fields, access limitations, and how it handles an unavailable result. The main workflow in `SKILL.md` remains unchanged.

## Social and forum collection rules

Use `social-public` and `forum-public` only for material that is publicly viewable. Record the platform, account or community name, post date, URL, and exact access limitation. A social post or forum comment is evidence that the named person or community made a statement; it is **not** evidence that the statement is true. Do not use private, login-only, deleted, or scraped personal content. Do not capture private personal information.
