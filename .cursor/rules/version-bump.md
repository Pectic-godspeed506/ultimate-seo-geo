---
description: Enforce version consistency when SKILL.md, CHANGELOG, or plugin files change
globs: "SKILL.md,CHANGELOG.md,.claude-plugin/**,plugins/**"
alwaysApply: false
---

# Version Bump Enforcement

When any of these files are modified, the version string MUST be updated consistently:

## Files that contain version strings (ALL must match)

1. `SKILL.md` frontmatter → `version: X.Y.Z`
2. `SKILL.md` body → `| **Version** | X.Y.Z |`
3. `.claude-plugin/marketplace.json` → `metadata.version` AND `plugins[0].version`
4. `plugins/ultimate-seo-geo/.claude-plugin/plugin.json` → `version`
5. `plugins/ultimate-seo-geo/skills/ultimate-seo-geo/SKILL.md` → frontmatter + table (synced by `setup-plugin.sh`)

## Before committing

1. If the change is a bugfix, feature, or behavioral change: bump the version
2. Run `python3 scripts/check_version_sync.py` — must exit 0
3. Run `python3 scripts/check-plugin-sync.py` — must exit 0
4. Add a `CHANGELOG.md` entry for the new version

## Version format

Use semantic versioning: `MAJOR.MINOR.PATCH`
- PATCH: bugfix, typo, false positive fix
- MINOR: new feature, new script, new reference file
- MAJOR: breaking change to skill structure or API
