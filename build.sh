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

SKIP_SNAP=0

for arg in "$@"; do
    if [[ "$arg" == "--skip-snap" ]]; then
        SKIP_SNAP=1
    fi
done

if [[ "$SKIP_SNAP" -eq 0 && ! -x "$(command -v snap)" ]]; then
    echo "⚠️  Snap is not installed on this system. Skipping snap build..."
    SKIP_SNAP=1
fi

if command -v apt >/dev/null 2>&1; then
    PKG_MANAGER="apt"
    UPDATE_CMD="sudo apt update"
    INSTALL_CMD="sudo apt install -y"
elif command -v dnf >/dev/null 2>&1; then
    PKG_MANAGER="dnf"
    UPDATE_CMD="sudo dnf makecache"
    INSTALL_CMD="sudo dnf install -y"
elif command -v pacman >/dev/null 2>&1; then
    PKG_MANAGER="pacman"
    UPDATE_CMD="sudo pacman -Sy"
    INSTALL_CMD="sudo pacman -S --noconfirm"
elif command -v zypper >/dev/null 2>&1; then
    PKG_MANAGER="zypper"
    UPDATE_CMD="sudo zypper refresh"
    INSTALL_CMD="sudo zypper install -y"
else
    echo "❌ Unsupported package manager. Install dependencies manually."
    exit 1
fi

echo "📦 Installing APT dependencies..."
APT_PACKAGES=(
    python3
    python3-all
    python3-setuptools
    python3-wheel
    python3-hatchling
    pybuild-plugin-pyproject
    devscripts
    debhelper
    fakeroot
    build-essential
    dh-python
)
$UPDATE_CMD
$INSTALL_CMD "${APT_PACKAGES[@]}"

if [[ "$SKIP_SNAP" -eq 0 ]]; then
    echo "📦 Installing Snap dependencies..."
    if ! snap list | grep -q snapcraft; then
        sudo snap install snapcraft --classic
    else
        echo "✅ Snapcraft is already installed."
    fi

    if ! snap list | grep -q lxd; then
        sudo snap install lxd
        sudo lxd init --auto
    else
        echo "✅ LXD is already installed."
    fi
fi

echo "🔧 Building $PROJECT_NAME version $VERSION..."

echo "🧹 Cleaning build artifacts..."
rm -rf dist snap/parts snap/stage snap/prime debian/mcup .pybuild
mkdir -p "$DIST_DIR"

if [[ "$SKIP_SNAP" -eq 1 ]]; then
    echo "🚫 Skipping snap build..."
else
    if command -v lxc >/dev/null 2>&1 && snap list | grep -q lxd; then
        echo "📦 Building Snap with LXD..."
        snapcraft --use-lxd --output "$SNAP_NAME"
    else
        echo "⚠️ LXD not found or not working."
        echo "📦 Building Snap using destructive mode (may be fragile)..."
        snapcraft --destructive-mode --output "$SNAP_NAME"
    fi

    echo "📦 Moving Snap to dist folder..."
    mv "$SNAP_NAME" "$SNAP_OUT"
fi

echo "📦 Building Debian package..."
python3 -m hatchling build
dpkg-buildpackage -us -uc -b

echo "📦 Moving Debian artifacts to dist folder..."
mv "../$DEB_NAME" "$DEB_OUT"
mv "../$BUILDINFO_NAME" "$BUILDINFO_OUT"
mv "../$CHANGES_NAME" "$CHANGES_OUT"

echo "✅ Build complete!"
echo "🔍 Output files:"
[[ "$SKIP_SNAP" -eq 0 ]] && ls "$SNAP_OUT"
ls "$DEB_OUT" "$BUILDINFO_OUT" "$CHANGES_OUT"