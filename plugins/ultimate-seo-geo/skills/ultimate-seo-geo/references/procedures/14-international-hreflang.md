> **Progressive disclosure:** Load this file only when the current task maps to this section (see `SKILL.md` §0). Do not load all procedure files for narrow tasks.

## 14. International SEO & Hreflang

### Audit — Step by Step

1. **Check existing hreflang** — View source, search `rel="alternate"`.
2. **Validate language codes** — ISO 639-1 format: `en-GB` ✅ `en-uk` ❌ (region uppercase).
3. **Check self-references** — Every page must hreflang to itself.
4. **Check return tags** — A links to B; B must link back to A.
5. **Check x-default** — `<link rel="alternate" hreflang="x-default" href="[fallback-url]">`.
6. **Check canonical alignment** — Hreflang only on canonical URLs.

### Critical Rules

| Rule | Fix |
|---|---|
| Self-reference required | Add `hreflang="[lang]"` to own page |
| Return tags required | Audit all alternate pages |
| `x-default` required | Add fallback URL tag |
| Chinese requires script qualifier | `zh-Hans` / `zh-Hant` ✅ — bare `zh` ❌ |
| Japanese code | `ja` ✅ — `jp` is a country code ❌ |

### Implementation Methods

Choose based on site scale:

| Method | Best For | Pros | Cons |
|---|---|---|---|
| **HTML `<link>` tags** | < 50 language variants | Easy to implement, visible in source | Bloats `<head>`, hard to maintain at scale |
| **HTTP headers** | Non-HTML files (PDFs, documents) | Works for any file type | Complex server config, not visible in HTML |
| **XML sitemap** | Large sites, cross-domain setups | Scalable, centralized management | Not visible on page, requires sitemap maintenance |

**Sitemap hreflang format** (recommended for large sites):
```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/page</loc>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://example.com/page" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page" />
  </url>
</urlset>
```
Every `<url>` entry must include all language alternates including itself. Cross-domain hreflang requires both domains verified in GSC.

→ See `references/international-seo.md` | Run `scripts/hreflang_checker.py`
