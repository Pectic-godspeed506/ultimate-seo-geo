#!/usr/bin/env bash
set -euo pipefail

echo "=== DataForSEO Extension — Claude Code Install ==="
echo ""

read -rp "Enter your DataForSEO login (email): " login
read -rp "Enter your DataForSEO password: " password

if [ -z "$login" ] || [ -z "$password" ]; then
    echo "Error: Both login and password are required."
    exit 1
fi

SETTINGS_FILE="$HOME/.claude/settings.json"
mkdir -p "$HOME/.claude"

if [ ! -f "$SETTINGS_FILE" ]; then
    echo '{}' > "$SETTINGS_FILE"
fi

python3 -c "
import json
with open('$SETTINGS_FILE', 'r') as f:
    settings = json.load(f)
settings.setdefault('mcpServers', {})
settings['mcpServers']['dataforseo-mcp-server'] = {
    'command': 'npx',
    'args': ['-y', 'dataforseo-mcp-server'],
    'env': {
        'DATAFORSEO_LOGIN': '$login',
        'DATAFORSEO_PASSWORD': '$password'
    }
}
with open('$SETTINGS_FILE', 'w') as f:
    json.dump(settings, f, indent=2)
print('MCP server configured in', '$SETTINGS_FILE')
"

echo ""
echo "Restart Claude Code to activate."
echo "Done."
