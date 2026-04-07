#!/usr/bin/env bash
# copy-knowledge-files.sh
# Copies SKILL.md and key reference files into chatgpt/knowledge/ for easy upload
# to a ChatGPT Custom GPT. Run from the repo root.

set -e

DEST="chatgpt/knowledge"
mkdir -p "$DEST"
rm -f "$DEST"/*.md "$DEST"/*.json 2>/dev/null || true

cp SKILL.md "$DEST/"

mkdir -p "$DEST/procedures"
for f in references/procedures/*.md; do
  [ -f "$f" ] && cp "$f" "$DEST/procedures/"
done

for f in references/*.md references/*.json; do
  [ -f "$f" ] && cp "$f" "$DEST/"
done

COUNT=$(ls "$DEST" | wc -l | tr -d ' ')
echo "Copied $COUNT files to $DEST/"
echo "Upload these to your Custom GPT's Knowledge section."
