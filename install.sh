#!/bin/bash
set -e

echo "Installing APUS Commands..."

# Check root
if [ "$EUID" -ne 0 ]; then
    echo "This script requires root privileges."
    echo "Run: sudo ./install.sh"
    exit 1
fi

echo "Checking essential dependencies..."

ESSENTIAL=("python3" "cmake")

for dep in "${ESSENTIAL[@]}"; do
    if ! command -v "$dep" >/dev/null 2>&1; then
        echo "ERROR: Missing essential dependency '$dep'"
        echo "Install it using your package manager and run the installer again."
        exit 1
    fi
done

echo "Essential dependencies OK."

echo "Checking recommended tools..."

RECOMMENDED=("wget" "ninja" "tar")

for dep in "${RECOMMENDED[@]}"; do
    if ! command -v "$dep" >/dev/null 2>&1; then
        echo "WARNING: '$dep' is missing"
        echo "Install it to avoid issues with further versions of APUS Commands."
    fi
done

echo "Installing APUS executable..."
install -m 755 bin/apus /usr/bin/apus

echo "Installing APUS backend..."
mkdir -p /usr/lib/apus
cp -r apus/* /usr/lib/apus/

echo "Creating user directory ~/.apus/cache..."
USER_HOME=$(eval echo "~$SUDO_USER")
mkdir -p "$USER_HOME/.apus/cache"
chown -R "$SUDO_USER":"$SUDO_USER" "$USER_HOME/.apus"

echo "Installation complete."
echo "APUS packages (.apuspack) will be stored in ~/.apus/cache"
echo "You can run APUS using: apus"

