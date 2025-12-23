#!/bin/bash
set -e

PROJECT_NAME="mcup"
VERSION=$(grep '^version' pyproject.toml | cut -d'"' -f2)
RPM_VERSION="${VERSION//-/_}"
DIST_DIR="./dist"

DEB_NAME="${PROJECT_NAME}_${VERSION}_all.deb"
BUILDINFO_NAME="${PROJECT_NAME}_${VERSION}_amd64.buildinfo"
CHANGES_NAME="${PROJECT_NAME}_${VERSION}_amd64.changes"
RPM_NAME="${PROJECT_NAME}-${RPM_VERSION}-1.noarch.rpm"

DEB_OUT="${DIST_DIR}/${DEB_NAME}"
BUILDINFO_OUT="${DIST_DIR}/${BUILDINFO_NAME}"
CHANGES_OUT="${DIST_DIR}/${CHANGES_NAME}"
RPM_OUT="${DIST_DIR}/${RPM_NAME}"

SKIP_RPM=0
SKIP_DEB=0

for arg in "$@"; do
    if [[ "$arg" == "--skip-deb" ]]; then
        SKIP_DEB=1
    fi
    if [[ "$arg" == "--skip-rpm" ]]; then
        SKIP_RPM=1
    fi
done


if command -v apt >/dev/null 2>&1; then
    UPDATE_CMD="sudo apt update"
    INSTALL_CMD="sudo apt install -y"
    INSTALL_PACKAGES=(
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
        rpm
        python3-pip
    )
elif command -v dnf >/dev/null 2>&1; then
    UPDATE_CMD="sudo dnf makecache"
    INSTALL_CMD="sudo dnf install -y"
    INSTALL_PACKAGES=(
        python3
        python3-devel
        python3-setuptools
        python3-pip
        python3-wheel
        python3-hatchling
        rpm-build
    )
elif command -v pacman >/dev/null 2>&1; then
    UPDATE_CMD="sudo pacman -Sy"
    INSTALL_CMD="sudo pacman -S --noconfirm"
    INSTALL_PACKAGES=(
        python
        python-setuptools
        python-pip
        python-wheel
        python-hatchling
        rpm-tools
        base-devel
    )
elif command -v zypper >/dev/null 2>&1; then
    UPDATE_CMD="sudo zypper refresh"
    INSTALL_CMD="sudo zypper install -y"
    INSTALL_PACKAGES=(
        python3
        python3-devel
        python3-setuptools
        python3-pip
        python3-wheel
        python3-hatchling
        rpm-build
    )
else
    echo "Unsupported package manager. Install dependencies manually."
    exit 1
fi

echo "Installing build dependencies..."
$UPDATE_CMD
$INSTALL_CMD "${INSTALL_PACKAGES[@]}"

if [[ "$SKIP_RPM" -eq 0 ]]; then
    if ! command -v rpmbuild >/dev/null 2>&1; then
        echo "rpmbuild is not installed. Skipping RPM build..."
        SKIP_RPM=1
    fi
fi


echo "Building $PROJECT_NAME version $VERSION..."

echo "Cleaning build artifacts..."
rm -rf dist debian/mcup .pybuild rpm/SOURCES rpm/BUILD rpm/RPMS rpm/SRPMS rpm/BUILDROOT
mkdir -p "$DIST_DIR"


if [[ "$SKIP_DEB" -eq 1 ]]; then
    echo "Skipping Debian package build..."
else
    if command -v dpkg-buildpackage >/dev/null 2>&1; then
        echo "Building Debian package..."
        python3 -m hatchling build
        dpkg-buildpackage -us -uc -b

        echo "Moving Debian artifacts to dist folder..."
        mv "../$DEB_NAME" "$DEB_OUT"
        mv "../$BUILDINFO_NAME" "$BUILDINFO_OUT"
        mv "../$CHANGES_NAME" "$CHANGES_OUT"
    else
        echo "dpkg-buildpackage not found. Skipping Debian build."
    fi
fi

if [[ "$SKIP_RPM" -eq 1 ]]; then
    echo "Skipping RPM build..."
else
    echo "Building RPM package..."
    mkdir -p rpm/SOURCES
    mkdir -p dist/rpm-src/mcup-${RPM_VERSION}
    rsync -av --exclude 'dist' --exclude '.git' --exclude '.venv' --exclude 'rpm' . dist/rpm-src/mcup-${RPM_VERSION}/

    tar -czf rpm/SOURCES/mcup-${RPM_VERSION}.tar.gz -C dist/rpm-src mcup-${RPM_VERSION}
    rm -rf dist/rpm-src

    rpmbuild --define "_topdir $(pwd)/rpm" --define "version ${RPM_VERSION}" -ba rpm/mcup.spec
    
    echo "Moving RPM artifacts to dist folder..."
    find rpm/RPMS -name "*.rpm" -exec mv {} "$DIST_DIR" \;
fi

echo "Build complete!"
echo "Output files:"
[[ "$SKIP_DEB" -eq 0 ]] && ls "$DEB_OUT" "$BUILDINFO_OUT" "$CHANGES_OUT" 2>/dev/null
[[ "$SKIP_RPM" -eq 0 ]] && ls -1 "$DIST_DIR"/*.rpm