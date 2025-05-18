#!/bin/bash
set -e

PROJECT_NAME="mcup"
VERSION=$(grep '^version' pyproject.toml | cut -d'"' -f2)
DIST_DIR="./dist"

SNAP_NAME="${PROJECT_NAME}_${VERSION}_amd64.snap"
DEB_NAME="${PROJECT_NAME}_${VERSION}_all.deb"
BUILDINFO_NAME="${PROJECT_NAME}_${VERSION}_amd64.buildinfo"
CHANGES_NAME="${PROJECT_NAME}_${VERSION}_amd64.changes"

SNAP_OUT="${DIST_DIR}/${SNAP_NAME}"
DEB_OUT="${DIST_DIR}/${DEB_NAME}"
BUILDINFO_OUT="${DIST_DIR}/${BUILDINFO_NAME}"
CHANGES_OUT="${DIST_DIR}/${CHANGES_NAME}"

echo "🔧 Building $PROJECT_NAME version $VERSION..."

echo "🧹 Cleaning build artifacts..."
rm -rf dist snap/parts snap/stage snap/prime debian/mcup .pybuild
mkdir -p "$DIST_DIR"

if command -v lxc >/dev/null 2>&1 && snap list | grep -q lxd; then
    echo "📦 Building Snap with LXD..."
    snapcraft --use-lxd --output "$SNAP_NAME"
else
    echo "⚠️ LXD not found."
    echo "📦 Building Snap using destructive mode (may be fragile)..."
    snapcraft --destructive-mode --output "$SNAP_NAME"
fi

echo "📦 Moving Snap to dist folder..."
mv "$SNAP_NAME" "$SNAP_OUT"

echo "📦 Building Debian package..."
python3 -m hatchling build
dpkg-buildpackage -us -uc -b

echo "📦 Moving Debian artifacts to dist folder..."
mv "../$DEB_NAME" "$DEB_OUT"
mv "../$BUILDINFO_NAME" "$BUILDINFO_OUT"
mv "../$CHANGES_NAME" "$CHANGES_OUT"

echo "✅ Build complete!"
echo "🔍 Output files:"
ls "$SNAP_OUT" "$DEB_OUT" "$BUILDINFO_OUT" "$CHANGES_OUT"
