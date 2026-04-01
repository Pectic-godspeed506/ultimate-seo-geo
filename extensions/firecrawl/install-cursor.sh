#!/usr/bin/env bash
set -euo pipefail

echo "=== Firecrawl Extension — Cursor Install ==="
echo ""
echo "This sets the FIRECRAWL_API_KEY and provides MCP configuration for Cursor."
echo "Get a free key at: https://www.firecrawl.dev/"
echo ""

read -rp "Enter your Firecrawl API key: " api_key

if [ -z "$api_key" ]; then
    echo "Error: API key cannot be empty."
    exit 1
fi

SHELL_RC=""
if [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [ -n "$SHELL_RC" ]; then
    if ! grep -q "FIRECRAWL_API_KEY" "$SHELL_RC" 2>/dev/null; then
        echo "" >> "$SHELL_RC"
        echo "# Firecrawl API key (Ultimate SEO + GEO extension)" >> "$SHELL_RC"
        echo "export FIRECRAWL_API_KEY=\"$api_key\"" >> "$SHELL_RC"
        echo "Added to $SHELL_RC"
    fi
fi

echo ""
echo "To add as a Cursor MCP server, add this to your Cursor MCP settings:"
echo ""
echo "  {"
echo "    \"firecrawl-mcp\": {"
echo "      \"command\": \"npx\","
echo "      \"args\": [\"-y\", \"firecrawl-mcp\"],"
echo "      \"env\": {\"FIRECRAWL_API_KEY\": \"$api_key\"}"
echo "    }"
echo "  }"
echo ""
echo "Verify with: python scripts/crawl_adapter.py https://example.com --backend firecrawl --json"
echo "Done."
