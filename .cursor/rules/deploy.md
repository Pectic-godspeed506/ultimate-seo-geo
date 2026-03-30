---
description: When the user says "deploy", "ship", "push", or "release"
globs:
alwaysApply: false
---

# Deploy

Read and follow `RELEASE.md` at the repo root. It is the single source of truth for all deployment steps.

At minimum, never skip these steps:
1. **Bump version** (step 1 in RELEASE.md) — update the version string in ALL of these locations to the same value:
   - `SKILL.md` frontmatter: `version:` and `updated:` fields
   - `SKILL.md` body: "Skill at a glance" table Version and Updated rows
   - `.claude-plugin/marketplace.json`: `metadata.version` and `plugins[0].version`
   - `plugins/ultimate-seo-geo/.claude-plugin/plugin.json`: `version`
2. Sync plugin bundle (step 2 in RELEASE.md)
3. Validate with `python3 scripts/check-plugin-sync.py` (step 3)
4. Commit and push (step 6)
5. **Create GitHub Release** (step 6a — required, never skip)
6. Verify with `python3 scripts/check_github_release.py` (step 6c)
