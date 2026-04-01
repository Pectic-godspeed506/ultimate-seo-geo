# SEO Content Subagent

Evaluates content quality, E-E-A-T signals, readability, and duplicate content.

## Scope

- E-E-A-T signal detection (author credentials, experience, expertise, trust)
- Readability analysis (Flesch-Kincaid grade, sentence length, complexity)
- Article structure (H2/H3 hierarchy, keyword density, word count)
- Thin content detection
- Near-duplicate content across pages
- Meta tag optimization (title, description, H1 lengths)
- Content pruning / refresh recommendations

## Scripts

| Script | Purpose |
|--------|---------|
| `article_seo.py` | Article structure + keyword extraction |
| `readability.py` | Flesch-Kincaid readability scoring |
| `duplicate_content.py` | Near-duplicate page detection |
| `meta_lengths_checker.py` | Title / meta description / H1 length checks |
| `programmatic_seo_auditor.py` | Quality gates for template pages at scale |

## Output

Returns content quality scores, readability metrics, duplicate page pairs,
and concrete rewrite recommendations (before/after sentence improvements).

## Reference Files

- `references/eeat-framework.md`
- `references/core-eeat-framework.md`
- `references/content-eeat.md`
