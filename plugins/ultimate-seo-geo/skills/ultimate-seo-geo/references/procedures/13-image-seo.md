> **Progressive disclosure:** Load this file only when the current task maps to this section (see `SKILL.md` §0). Do not load all procedure files for narrow tasks.

## 13. Image SEO

### Audit — Step by Step

1. **Check each `<img>`** — alt text? Declared width/height? WebP format?
2. **Identify LCP image** — Confirm `fetchpriority="high"` and NOT lazy-loaded.
3. **Check file sizes** — DevTools Network, actual KB per image.
4. **Fix missing alt text** — Descriptive, 10–125 chars.
5. **Check responsive images** — `srcset` and `sizes` on content images.

### Checklist + Fix Directives

| Element | Standard | Fix |
|---|---|---|
| Alt text | Descriptive, 10–125 chars | "[what + context]" e.g. "White ceramic mug on wooden desk" |
| Format | WebP preferred | Convert to WebP; AVIF for cutting-edge |
| File size | Thumbnails <50KB; content <100KB; heroes <200KB | Squoosh/Cloudinary; CDN compression |
| Responsive | `srcset` and `sizes` | Add multi-resolution srcset |
| Lazy loading | Below-fold only | Never lazy-load LCP image |
| Dimensions | `width` and `height` on all `<img>` | Prevents CLS |
| LCP image | `fetchpriority="high"` | `<img fetchpriority="high" src="hero.webp">` |
| Non-LCP images | `decoding="async"` | Prevents image decoding from blocking the main thread |

**Progressive enhancement:**
```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Descriptive alt text" width="800" height="600"
       loading="lazy" decoding="async">
</picture>
```

**Don't**: Add `loading="lazy"` to the LCP image.

**JPEG XL** — Chrome reversed its 2022 removal decision in November 2025, implementing via a Rust-based decoder. Not yet in Chrome stable as of March 2026. Offers ~20% lossless savings over JPEG with zero quality loss. Monitor for 2026/2027 adoption; not yet practical for production deployment.

→ See `references/image-seo.md`
