> **Progressive disclosure:** Load this file only when the current task maps to this section (see `SKILL.md` §0). Do not load all procedure files for narrow tasks.

## 20. Site Migration SEO

Site migration = any change to URL structure, domain, protocol, or CMS. High-risk — poor migrations cause 30–90% traffic loss.

### Migration Risk Assessment

| Migration Type | Risk Level |
|---|---|
| HTTP → HTTPS | Low |
| Subdomain → subdirectory | Medium |
| URL restructure (same domain) | Medium-High |
| Domain change | High |
| CMS platform change | High |
| Domain + URL structure change | Very High — never do both at once |

### Migration Process (Summary)

**Pre-migration**: Crawl current site (all URLs + canonicals); export 16 months of GSC data; create complete old URL → new URL redirect map; update all internal links; prepare new sitemap; add + verify new GSC property.

**Migration day**: Deploy all redirects as **301** (not 302); spot-check 20–30 URLs; submit new sitemap immediately; run GSC URL Inspection on key pages.

**Post-migration**: Monitor GSC Coverage for 404 spikes (Day 1–3); check impressions (Day 3–7); check key rankings (Week 2); benchmark at Day 30.

For the complete step-by-step checklists, common mistakes, and post-migration monitoring schedule, see `references/site-migration.md`.

→ See `references/site-migration.md` | Run `scripts/redirect_checker.py`
