#!/bin/bash
set -e

PROJECT_NAME="mcup"
VERSION=$(grep '^version' pyproject.toml | cut -d'"' -f2)

echo "🔧 Building $PROJECT_NAME version $VERSION..."

echo "📦 Building Snap package..."
cd snap
snapcraft --destructive-mode --output "../${PROJECT_NAME}_${VERSION}_amd64.snap"
cd ..

rm -rf ../${PROJECT_NAME}_${VERSION}* *.build *.changes *.deb dist/

echo "📦 Building .deb package..."
python3 -m build --sdist
dpkg-buildpackage -us -uc -b

echo "✅ Build complete!"
echo "Output files:"
ls -lh ../${PROJECT_NAME}_${VERSION}_*.deb
ls -lh ./${PROJECT_NAME}_${VERSION}_*.snap