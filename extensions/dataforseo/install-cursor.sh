#!/usr/bin/env bash
set -euo pipefail

echo "=== DataForSEO Extension — Cursor Install ==="
echo ""

read -rp "Enter your DataForSEO login (email): " login
read -rp "Enter your DataForSEO password: " password

if [ -z "$login" ] || [ -z "$password" ]; then
    echo "Error: Both login and password are required."
    exit 1
fi

SHELL_RC=""
if [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [ -n "$SHELL_RC" ]; then
    if ! grep -q "DATAFORSEO_LOGIN" "$SHELL_RC" 2>/dev/null; then
        echo "" >> "$SHELL_RC"
        echo "# DataForSEO credentials (Ultimate SEO + GEO extension)" >> "$SHELL_RC"
        echo "export DATAFORSEO_LOGIN=\"$login\"" >> "$SHELL_RC"
        echo "export DATAFORSEO_PASSWORD=\"$password\"" >> "$SHELL_RC"
    fi
fi

echo ""
echo "To add as a Cursor MCP server, add this to your Cursor MCP settings:"
echo ""
echo "  {"
echo "    \"dataforseo-mcp-server\": {"
echo "      \"command\": \"npx\","
echo "      \"args\": [\"-y\", \"dataforseo-mcp-server\"],"
echo "      \"env\": {"
echo "        \"DATAFORSEO_LOGIN\": \"$login\","
echo "        \"DATAFORSEO_PASSWORD\": \"$password\""
echo "      }"
echo "    }"
echo "  }"
echo ""
echo "Done."
