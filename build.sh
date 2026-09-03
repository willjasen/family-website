#!/bin/sh

set -eu

project_directory=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$project_directory"

python3 add_footer.py

index_file="tree/index.html"
marker="<!-- family-tree-gtag:start -->"

if [ ! -f "$index_file" ]; then
  echo "Build failed: MacFamilyTree export not found at $index_file" >&2
  exit 1
fi

marker_count=$(grep -Foc "$marker" "$index_file" || true)
if [ "$marker_count" -ne 1 ]; then
  echo "Build failed: expected one Google Analytics block in $index_file, found $marker_count" >&2
  exit 1
fi

echo "Build complete: Google Analytics applied to the MacFamilyTree export."
