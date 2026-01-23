#!/bin/bash
# Comprehensive documentation generation script
# This script handles:
# 1. English translation from Chinese
# 2. Word document generation (Chinese and English)
# 3. HTML site generation using MkDocs

set -e  # Exit on error

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "=========================================="
echo "Documentation Generation Pipeline"
echo "=========================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Parse arguments
PRODUCT="${1:-IMX93-GW8016}"
VERSION="${2:-v1.0}"
SKIP_TRANSLATION="${3:-no}"

print_info "Product: $PRODUCT"
print_info "Version: $VERSION"
echo ""

# Step 1: Generate English translation from Chinese (if not skipped)
if [ "$SKIP_TRANSLATION" = "yes" ] || [ "$SKIP_TRANSLATION" = "true" ]; then
    print_warning "Skipping translation step (--skip-translation flag set)"
    echo ""
else
    print_info "Step 1: Generating English translation from Chinese..."
    if python3 tools/generate_en_from_zh.py "$PRODUCT" "$VERSION"; then
        print_info "✓ English translation completed"
    else
        print_warning "⚠ English translation failed or skipped"
    fi
    echo ""
fi

# Step 2: Generate Word documents
print_info "Step 2: Generating Word documents..."
if python3 tools/generate_word.py "$PRODUCT" "$VERSION" --lang both; then
    print_info "✓ Word documents generated successfully"
else
    print_error "✗ Word document generation failed"
fi
echo ""

# Step 3: Build MkDocs site
print_info "Step 3: Building MkDocs documentation site..."
if command -v mkdocs &> /dev/null; then
    if mkdocs build --clean; then
        print_info "✓ MkDocs site built successfully"
        print_info "  Output: site/"
    else
        print_error "✗ MkDocs build failed"
    fi
else
    print_warning "⚠ MkDocs not installed. Skipping site generation."
    print_info "  Install with: pip3 install mkdocs mkdocs-material mkdocs-static-i18n"
fi
echo ""

# Summary
echo "=========================================="
echo "Generation Summary"
echo "=========================================="
print_info "Chinese source: docs/zh/products/$PRODUCT/$VERSION/"
print_info "English output: docs/en/products/$PRODUCT/$VERSION/"
print_info "Word documents: docs/word/$PRODUCT/$VERSION/"
print_info "HTML site: site/"
echo ""
print_info "To serve the site locally, run:"
echo "  mkdocs serve"
echo ""
print_info "To deploy to GitHub Pages, run:"
echo "  mkdocs gh-deploy"
echo ""
