#!/usr/bin/env bash
set -euo pipefail

echo "=== DataForSEO Extension — Generic Install ==="
echo ""
echo "This sets DataForSEO credentials as environment variables."
echo "Create an account at: https://dataforseo.com/"
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
elif [ -f "$HOME/.bash_profile" ]; then
    SHELL_RC="$HOME/.bash_profile"
fi

if [ -n "$SHELL_RC" ]; then
    if ! grep -q "DATAFORSEO_LOGIN" "$SHELL_RC" 2>/dev/null; then
        echo "" >> "$SHELL_RC"
        echo "# DataForSEO credentials (Ultimate SEO + GEO extension)" >> "$SHELL_RC"
        echo "export DATAFORSEO_LOGIN=\"$login\"" >> "$SHELL_RC"
        echo "export DATAFORSEO_PASSWORD=\"$password\"" >> "$SHELL_RC"
        echo "Added to $SHELL_RC"
    else
        echo "DataForSEO credentials already exist in $SHELL_RC"
    fi
    echo "Run: source $SHELL_RC"
else
    echo "Could not detect shell config. Add manually:"
    echo "  export DATAFORSEO_LOGIN=\"$login\""
    echo "  export DATAFORSEO_PASSWORD=\"$password\""
fi

echo ""
echo "Done."
