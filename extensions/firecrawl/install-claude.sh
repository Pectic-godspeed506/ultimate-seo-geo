#!/usr/bin/env bash
set -euo pipefail

echo "=== Firecrawl Extension — Claude Code Install ==="
echo ""
echo "This configures the Firecrawl MCP server for Claude Code."
echo "Get a free key at: https://www.firecrawl.dev/"
echo ""

read -rp "Enter your Firecrawl API key: " api_key

if [ -z "$api_key" ]; then
    echo "Error: API key cannot be empty."
    exit 1
fi

SETTINGS_FILE="$HOME/.claude/settings.json"
mkdir -p "$HOME/.claude"

if [ ! -f "$SETTINGS_FILE" ]; then
    echo '{}' > "$SETTINGS_FILE"
fi

python3 -c "
import json, sys
with open('$SETTINGS_FILE', 'r') as f:
    settings = json.load(f)
settings.setdefault('mcpServers', {})
settings['mcpServers']['firecrawl-mcp'] = {
    'command': 'npx',
    'args': ['-y', 'firecrawl-mcp'],
    'env': {'FIRECRAWL_API_KEY': '$api_key'}
}
with open('$SETTINGS_FILE', 'w') as f:
    json.dump(settings, f, indent=2)
print('MCP server configured in', '$SETTINGS_FILE')
"

echo ""
echo "Restart Claude Code to activate. Verify with:"
echo "  python scripts/crawl_adapter.py https://example.com --backend firecrawl --json"
echo "Done."
