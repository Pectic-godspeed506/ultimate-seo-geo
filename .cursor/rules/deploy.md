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
   - `AGENTS.md` header table: `Version` row
   - `README.md` and `plugins/ultimate-seo-geo/README.md`: version badge
   - `GEMINI.md`, `.github/copilot-instructions.md`, `chatgpt/instructions.txt`: script/ref counts if changed
2. Run `python3 scripts/check_version_sync.py` — must exit 0
3. Sync plugin bundle: `bash setup-plugin.sh`
4. Validate with `python3 scripts/check-plugin-sync.py` — must exit 0
5. Run eval regression: `python3 scripts/score_eval_transcript.py --all-fixtures` — must exit 0
6. Compile check: `for f in scripts/*.py; do python3 -m py_compile "$f"; done`
7. Commit and push
8. **Create GitHub Release** (step 6a — required, never skip): `gh release create vX.Y.Z ...`
9. Verify release: `python3 scripts/check_github_release.py` — must exit 0
10. **Update local Claude terminal install** (step 6b — never skip):
    ```bash
    bash setup-plugin.sh && \
    cp -r plugins/ultimate-seo-geo/. \
      ~/.claude/plugins/marketplaces/ultimate-seo-geo/plugins/ultimate-seo-geo/
    echo "✓ Claude terminal plugin updated — restart claude to reload"
    ```
11. **Refresh Claude marketplace cache** (step 6c — never skip):
    ```bash
    cd ~/.claude/plugins/marketplaces/ultimate-seo-geo && \
      git fetch origin && git reset --hard origin/main && \
      echo "✓ Marketplace cache at $(git log --oneline -1)"
    ```
    Then restart Claude Code to reload the plugin.

> Steps 10–11 update the **local Claude install**. Without them, the running Claude Code instance keeps the old version even after the GitHub Release is live.
