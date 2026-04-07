> **Progressive disclosure:** Load this file only when the current task maps to this section (see `SKILL.md` §0). Do not load all procedure files for narrow tasks.

## 8. Competitor Analysis

### Step by Step

1. **Identify 3–5 direct competitors** — Search the site's primary keyword and note positions 1–5.
2. **Fetch competitor homepage + top-ranking pages**. Also fetch `[competitor-url]/robots.txt` and `[competitor-url]/llms.txt` for GEO stance assessment. For topic coverage: run `sitemap_checker.py [competitor-url]` to confirm sitemap URL and reachability, then fetch the raw sitemap XML directly and read `<loc>` URL path patterns — folder-level segments absent from the audited site are direct content gap candidates.
3. **Assess across five dimensions** below.
4. **Identify 3 biggest gaps to close** and 3 biggest advantages to exploit.
5. **Test shared keywords in AI search** — ChatGPT and Perplexity. Note who gets cited.

### Competitor Assessment Dimensions

| Dimension | Opportunity Signal |
|---|---|
| Content depth gaps | Create the definitive resource on under-covered topics |
| Missing topic clusters | Map cluster and execute content plan |
| Schema advantages | Add missing schema immediately; reinforce where you have it |
| AI citation presence | If they're cited and you're not → audit GEO signals (§ 3) |
| E-E-A-T gaps | Leverage credentials where competitors use anonymous bylines |
| AI crawler configuration | If competitor blocks OAI-SearchBot or PerplexityBot in robots.txt → immediate GEO first-mover advantage. Run `robots_checker.py [competitor-url]`. Output labeled "External Observation Only." |
| llms.txt presence | If competitor lacks llms.txt → your llms.txt gives AI systems clearer indexing signal. Run `llms_txt_checker.py [competitor-url]`. Output labeled "External Observation Only." |
| Topic coverage gap (sitemap) | Fetch competitor's raw sitemap XML; `<loc>` URL path patterns absent from your site → direct content calendar input. Confirm sitemap reachability via `sitemap_checker.py [competitor-url]`, then read raw `<loc>` entries. Output labeled "External Observation Only." |

### Output Format

```
## Competitive Landscape
| Dimension | [Your Site] | [Competitor 1] | [Competitor 2] |

## Top 3 Gaps to Close
## Top 3 Advantages to Exploit
## AI Citation Gap (if applicable)
## Recommended Comparison Pages to Create
```

**Comparison page title formulas** (use these for new pages targeting competitive intent):
- X vs Y: `[A] vs [B]: [Key Differentiator] ([Year])`
- Alternatives: `[N] Best [A] Alternatives in [Year] (Free & Paid)`
- Roundup: `[N] Best [Category] Tools in [Year] — Compared & Ranked`

For roundup pages, add `ItemList` schema alongside `Article` — it signals a structured list to AI systems and improves citation probability. For "X vs Y" and "Alternatives to X" page content requirements, the 4-type comparison page playbook (fairness guidelines, CTA placement rules), feature matrix structure, and nominative fair use guidance, see `references/link-building.md` → "Comparison & Alternatives Page Playbook" section.

---
