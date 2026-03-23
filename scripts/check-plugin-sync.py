#!/usr/bin/env python3
"""Fail if the plugin skill bundle is out of sync with repo root or versions diverge."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _skill_frontmatter_version(path: Path) -> str:
    t = _read(path)
    if not t.startswith("---"):
        sys.exit(f"{path}: missing YAML frontmatter")
    try:
        _, fm, _ = t.split("---", 2)
    except ValueError:
        sys.exit(f"{path}: malformed frontmatter")
    for line in fm.splitlines():
        m = re.match(r"^  version:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip("'\"")
    sys.exit(f"{path}: metadata.version not found under frontmatter")


def main() -> int:
    skill_root = ROOT / "SKILL.md"
    skill_plugin = ROOT / "plugins/ultimate-seo-geo/skills/ultimate-seo-geo/SKILL.md"

    if _read(skill_root) != _read(skill_plugin):
        sys.exit(
            "SKILL.md mismatch: root != plugins/ultimate-seo-geo/skills/ultimate-seo-geo/SKILL.md\n"
            "Fix: bash setup-plugin.sh"
        )

    ref_root = ROOT / "references"
    ref_plugin = ROOT / "plugins/ultimate-seo-geo/skills/ultimate-seo-geo/references"
    if not ref_root.is_dir() or not ref_plugin.is_dir():
        sys.exit("references/ directories missing at root or under plugin skill path")

    root_names = sorted(f.name for f in ref_root.iterdir() if f.is_file())
    plug_names = sorted(f.name for f in ref_plugin.iterdir() if f.is_file())
    if root_names != plug_names:
        diff = sorted(set(root_names) ^ set(plug_names))
        sys.exit(
            "references/ filename set mismatch vs plugin copy.\n"
            f"  symmetric diff: {diff}\n"
            "Fix: bash setup-plugin.sh"
        )

    for name in root_names:
        if _read(ref_root / name) != _read(ref_plugin / name):
            sys.exit(
                f"references/{name} differs from plugin copy.\nFix: bash setup-plugin.sh"
            )

    market_path = ROOT / ".claude-plugin/marketplace.json"
    with open(market_path, encoding="utf-8") as f:
        market = json.load(f)
    meta_v = market["metadata"]["version"]
    listed_v = market["plugins"][0]["version"]
    if meta_v != listed_v:
        sys.exit(
            f"marketplace.json: metadata.version ({meta_v!r}) != plugins[0].version ({listed_v!r})"
        )

    plugin_json = ROOT / "plugins/ultimate-seo-geo/.claude-plugin/plugin.json"
    with open(plugin_json, encoding="utf-8") as f:
        pjson = json.load(f)
    pj_v = pjson["version"]

    sk_v = _skill_frontmatter_version(skill_root)

    versions = {
        "marketplace.metadata.version": meta_v,
        "marketplace.plugins[0].version": listed_v,
        "plugin.json version": pj_v,
        "SKILL.md metadata.version": sk_v,
    }
    unique = set(versions.values())
    if len(unique) != 1:
        lines = "\n".join(f"  {k}: {v!r}" for k, v in versions.items())
        sys.exit("Version strings must match everywhere:\n" + lines)

    print("Plugin sync + version alignment OK ✓")
    for k, v in versions.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
