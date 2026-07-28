"""Add or refresh the Google Analytics snippet after a MacFamilyTree export.

Run this from the repository root after exporting MacFamilyTree into ``tree/``:

    python3 add_footer.py
"""

from pathlib import Path
import re


EXPORT_DIRECTORY = Path("tree")
GTAG_FILE = Path("gtag.html")
START_MARKER = "<!-- family-tree-gtag:start -->"
END_MARKER = "<!-- family-tree-gtag:end -->"


def managed_footer(gtag_content: str) -> str:
    return f"<footer>\n{START_MARKER}\n{gtag_content.strip()}\n{END_MARKER}\n</footer>"


def replace_existing_analytics(content: str) -> str:
    """Remove a previously injected managed block or the legacy analytics footer."""
    managed_pattern = re.compile(
        rf"\s*<footer>\s*{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}\s*</footer>",
        re.DOTALL,
    )
    legacy_pattern = re.compile(
        r"\s*<footer>\s*<script async src=\"https://www\.googletagmanager\.com/gtag/js\?id=[^\"]+\"></script>"
        r".*?</script>\s*</footer>",
        re.DOTALL,
    )
    return legacy_pattern.sub("", managed_pattern.sub("", content))


def update_export() -> None:
    if not EXPORT_DIRECTORY.is_dir():
        raise SystemExit(f"Export directory not found: {EXPORT_DIRECTORY}")

    gtag_content = GTAG_FILE.read_text(encoding="utf-8")
    footer = managed_footer(gtag_content)

    for html_file in EXPORT_DIRECTORY.rglob("*.html"):
        content = replace_existing_analytics(html_file.read_text(encoding="utf-8"))
        if "</body>" not in content:
            print(f"Skipping {html_file}: no closing </body> tag.")
            continue

        updated_content = content.replace("</body>", f"{footer}\n</body>", 1)
        html_file.write_text(updated_content, encoding="utf-8")
        print(f"Updated analytics in {html_file}")


if __name__ == "__main__":
    update_export()
