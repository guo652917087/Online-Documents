#!/usr/bin/env python3
"""
Generate Word documents (.docx) from Markdown files using Pandoc.

Usage:
    python tools/generate_word.py <product> <version> [--lang <zh|en|both>]
    
Examples:
    python tools/generate_word.py IMX93-GW8016 v1.0 --lang zh
    python tools/generate_word.py IMX93-GW8016 v1.0 --lang en
    python tools/generate_word.py IMX93-GW8016 v1.0 --lang both
"""

import argparse
import subprocess
import sys
from pathlib import Path


def generate_word_doc(md_file: Path, output_file: Path, title: str = None):
    """
    Convert Markdown to Word document using Pandoc.
    
    Args:
        md_file: Path to source Markdown file
        output_file: Path to output Word document
        title: Document title (optional)
    """
    print(f"Converting {md_file} to {output_file}...")
    
    # Build Pandoc command
    cmd = [
        "pandoc",
        str(md_file),
        "-o", str(output_file),
        "--from=markdown",
        "--to=docx",
        "--standalone",
        "--toc",  # Add table of contents
        "--toc-depth=3",
        "--number-sections",
        "--highlight-style=tango",
    ]
    
    # Add title if provided
    if title:
        cmd.extend(["--metadata", f"title={title}"])
    
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ Successfully generated: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error generating Word document: {e}")
        print(f"  stdout: {e.stdout}")
        print(f"  stderr: {e.stderr}")
        return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Generate Word documents from Markdown files"
    )
    parser.add_argument("product", help="Product name (e.g., IMX93-GW8016)")
    parser.add_argument("version", help="Version (e.g., v1.0)")
    parser.add_argument(
        "--lang",
        choices=["zh", "en", "both"],
        default="both",
        help="Language to generate (default: both)"
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory (default: docs/word)"
    )
    
    args = parser.parse_args()
    
    project_root = Path(__file__).parent.parent
    
    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = project_root / "docs" / "word" / args.product / args.version
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    languages = ["zh", "en"] if args.lang == "both" else [args.lang]
    
    success_count = 0
    failed_count = 0
    
    for lang in languages:
        # Source Markdown file
        md_file = (
            project_root / "docs" / lang / "products" / 
            args.product / args.version / "index.md"
        )
        
        if not md_file.exists():
            print(f"⚠ Warning: Source file not found: {md_file}")
            failed_count += 1
            continue
        
        # Output Word file
        lang_name = "Chinese" if lang == "zh" else "English"
        output_file = output_dir / f"{args.product}_{args.version}_{lang}.docx"
        
        # Document title
        title = f"{args.product} Documentation ({lang_name})"
        
        # Generate Word document
        if generate_word_doc(md_file, output_file, title):
            success_count += 1
        else:
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Word Document Generation Summary")
    print("=" * 60)
    print(f"Successful: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"Output directory: {output_dir}")
    print("=" * 60)
    
    if failed_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
