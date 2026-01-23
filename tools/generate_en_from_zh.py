#!/usr/bin/env python3
"""
Generate English markdown files from Chinese markdown files (one-time conversion).
This creates editable English MD files that won't be overwritten by automated translation.

Usage:
    python tools/generate_en_from_zh.py <product> <version>
    
Example:
    python tools/generate_en_from_zh.py iot_hub v1.0
"""

import os
import re
import sys
import time
from pathlib import Path

import translators as ts

# Set region to avoid geolocation issues
os.environ["translators_default_region"] = "EN"


def translate_text(text: str) -> str:
    """Translate Chinese text to English using Google Translate API"""
    if not text.strip():
        return text
    try:
        result = ts.translate_text(
            text, translator='google', from_language='zh', to_language='en'
        )
        time.sleep(0.1)  # Small delay to avoid rate limiting
        return result
    except Exception as e:
        print(f"Translation error: {e}, returning original text")
        return text


def translate_text_preserve_code(md_text: str) -> str:
    """Translate Markdown text while preserving code blocks"""
    # Preserve code blocks using placeholders
    code_blocks = []

    def block_repl(match):
        code_blocks.append(match.group(0))
        return f"{{{{CODE_BLOCK_{len(code_blocks)-1}}}}}"

    fenced_pattern = re.compile(r"(```.*?```|````.*?````)", re.DOTALL)
    tmp = re.sub(fenced_pattern, block_repl, md_text)

    # Translate non-code content line by line
    lines = tmp.splitlines()
    out_lines = []
    for line in lines:
        # Skip pure HTML lines
        if re.match(r"^\s*<[^>]+>\s*$", line):
            out_lines.append(line)
            continue
        # Don't translate pure URLs
        if re.match(r"^\s*https?://", line):
            out_lines.append(line)
            continue
        # Don't translate empty lines
        if not line.strip():
            out_lines.append(line)
            continue
        # Translate [text](url) but preserve url
        def bracket_repl(m):
            txt = m.group(1)
            translated = translate_text(txt)
            return f"[{translated}]"

        line = re.sub(
            r"\[([^\]]+)\](\([^\)]+\))",
            lambda m: f"{bracket_repl(m)}{m.group(2)}",
            line,
        )
        # Translate remaining line
        out_lines.append(translate_text(line))

    out = "\n".join(out_lines)

    # Restore code blocks
    for i, block in enumerate(code_blocks):
        out = out.replace(f"{{{{CODE_BLOCK_{i}}}}}", block)

    return out


def process_file(src_path: Path, dst_path: Path):
    """Process a single file"""
    print(f"Processing {src_path}...")
    
    with src_path.open("r", encoding="utf-8") as f:
        src = f.read()

    en = translate_text_preserve_code(src)

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    with dst_path.open("w", encoding="utf-8") as f:
        f.write(en)
    
    print(f"Generated {dst_path}")


def main():
    """Main entry point"""
    if len(sys.argv) != 3:
        print("Usage: python generate_en_from_zh.py <product> <version>")
        print("Example: python generate_en_from_zh.py iot_hub v1.0")
        sys.exit(1)

    product = sys.argv[1]
    version = sys.argv[2]

    project_root = Path(__file__).parent.parent
    src_dir = project_root / "docs" / "zh" / "products" / product / version
    dst_dir = project_root / "docs" / "en" / "products" / product / version

    if not src_dir.exists():
        print(f"Error: Source directory not found: {src_dir}")
        sys.exit(1)

    print(f"Generating English documentation from Chinese...")
    print(f"Source: {src_dir}")
    print(f"Destination: {dst_dir}")

    for src_path in src_dir.rglob("*.md"):
        rel_path = src_path.relative_to(src_dir)
        dst_path = dst_dir / rel_path
        process_file(src_path, dst_path)

    print("\nGeneration complete!")
    print(f"English markdown files have been created in: {dst_dir}")
    print("You can now manually edit these files as needed.")


if __name__ == "__main__":
    main()
