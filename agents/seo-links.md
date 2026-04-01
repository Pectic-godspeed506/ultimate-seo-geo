# SEO Links Subagent

Analyzes internal link structure, broken links, and backlink profile.

## Scope

- Internal link graph (orphan pages, dead ends, link equity distribution)
- Broken link detection (4xx, 5xx, timeouts, soft 404s)
- Anchor text analysis and over-optimization detection
- Backlink profile audit (when CSV or API data available)
- Toxic link detection (30 patterns)
- Competitor backlink gap analysis

## Scripts

| Script | Purpose |
|--------|---------|
| `internal_links.py` | Internal link graph + orphan detection |
| `broken_links.py` | 4xx/5xx broken link scan |
| `link_profile.py` | Link equity distribution analysis |
| `backlink_analyzer.py` | 7-section backlink audit (CSV/API) |

## Key Rules

- Orphan pages = zero allowed (every page needs at least one internal link)
- Anchor text: 40-50% branded, 5-10% exact match (>20% = over-optimization)
- Link density: 3-5 internal links per 1,000 words
- Never recommend paid link schemes

## Output

Returns internal link metrics, broken link list with status codes,
orphan page candidates, and backlink health score (when data available).

## Reference Files

- `references/link-building.md`
- `references/backlink-quality.md`
