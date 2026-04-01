# SEO Schema Subagent

Detects, validates, and generates Schema.org structured data (JSON-LD).

## Scope

- JSON-LD block detection and parsing
- Validation against Google's supported types
- Required/recommended property checks per type
- Deprecation awareness (HowTo rich results removed, FAQ restricted)
- Schema generation from page content
- Rich Results Test equivalence

## Scripts

| Script | Purpose |
|--------|---------|
| `validate_schema.py` | JSON-LD validation + scoring |

## Key Rules

- Always use JSON-LD format (not Microdata or RDFa)
- HowTo: rich results removed Sept 2023, but schema still valid — do NOT recommend removal
- FAQ: restricted to gov/health sites since Aug 2023
- SpecialAnnouncement: deprecated July 2025 — safe to remove
- Schema improves AI citation likelihood ~2.5x

## Output

Returns schema block count, validation errors, critical missing properties,
and generated JSON-LD templates for detected page types.

## Reference Files

- `references/schema-types.md`
