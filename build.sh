#!/bin/bash
set -e

PROJECT_NAME="mcup"
VERSION=$(grep '^version' pyproject.toml | cut -d'"' -f2)
SNAP_OUT="${PROJECT_NAME}_${VERSION}_amd64.snap"
DEB_OUT="../${PROJECT_NAME}_${VERSION}_all.deb"

echo "🔧 Building $PROJECT_NAME version $VERSION..."

echo "🧹 Cleaning Snap build artifacts..."
rm -rf snap/parts snap/stage snap/prime

if command -v lxc >/dev/null 2>&1 && snap list | grep -q lxd; then
    echo "📦 Building Snap with LXD..."
    snapcraft --use-lxd --output "$SNAP_OUT"
else
    echo "⚠️  LXD not found. FBuilding Snap using destructive mode (may be fragile)..."
    snapcraft --destructive-mode --output "$SNAP_OUT"
fi\

echo "🧹 Cleaning old .deb artifacts..."
rm -rf dist ../${PROJECT_NAME}_*.deb *.build *.changes

echo "📦 Building Debian package..."
python3 -m hatchling build
dpkg-buildpackage -us -uc -b

echo "✅ Build complete!"
echo "🔍 Output files:"
ls -lh "$SNAP_OUT"
ls -lh "$DEB_OUT"
