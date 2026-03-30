---
description: When the user says "deploy", "ship", "push", or "release"
globs:
alwaysApply: false
---

# Deploy checklist

When the user asks to deploy, ship, push, or release, execute ALL of these steps in order. Do not skip any.

## 1. Sync plugin bundle

Copy all modified files from repo root to `plugins/ultimate-seo-geo/skills/ultimate-seo-geo/`.
Verify with `diff -q` that every file matches.

## 2. Compile check

Run `python3 -c "import py_compile; py_compile.compile('scripts/<file>.py', doraise=True)"` on every modified `.py` file.

## 3. Commit and push

```bash
git add -A
git commit -m "vX.Y.Z — summary"
git push origin main
```

## 4. Create GitHub Release (required — never skip)

```bash
gh release create vX.Y.Z \
  --title "vX.Y.Z — summary" \
  --notes "release notes" \
  --target main
```

The Claude.ai web app Marketplace reads from GitHub Releases, not commits. Without a published Release, the Marketplace will NOT serve the new version.

## 5. Verify release

```bash
python3 scripts/check_github_release.py
```

Must exit 0. If it fails, fix the release before telling the user deployment is complete.
