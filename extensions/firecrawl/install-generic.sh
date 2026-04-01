#!/usr/bin/env bash
set -euo pipefail

echo "=== Firecrawl Extension — Generic Install ==="
echo ""
echo "This sets the FIRECRAWL_API_KEY environment variable."
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
elif [ -f "$HOME/.bash_profile" ]; then
    SHELL_RC="$HOME/.bash_profile"
fi

if [ -n "$SHELL_RC" ]; then
    if grep -q "FIRECRAWL_API_KEY" "$SHELL_RC" 2>/dev/null; then
        echo "FIRECRAWL_API_KEY already exists in $SHELL_RC — updating."
        sed -i.bak "s|export FIRECRAWL_API_KEY=.*|export FIRECRAWL_API_KEY=\"$api_key\"|" "$SHELL_RC"
    else
        echo "" >> "$SHELL_RC"
        echo "# Firecrawl API key (Ultimate SEO + GEO extension)" >> "$SHELL_RC"
        echo "export FIRECRAWL_API_KEY=\"$api_key\"" >> "$SHELL_RC"
    fi
    echo "Added to $SHELL_RC"
    echo "Run: source $SHELL_RC"
else
    echo "Could not detect shell config. Add manually:"
    echo "  export FIRECRAWL_API_KEY=\"$api_key\""
fi

echo ""
echo "Verify with: python scripts/crawl_adapter.py https://example.com --backend firecrawl --json"
echo "Done."
