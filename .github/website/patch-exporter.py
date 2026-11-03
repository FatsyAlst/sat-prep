#!/usr/bin/env python3
"""Small patch applied to the pinned Webpage HTML Export source before it is built.

TikZJax draws every diagram asynchronously (one WebAssembly TeX run per diagram) and leaves
a loading spinner in the page until it is done. The exporter only waits a moment for plugin
blocks, so without this patch the spinner is what ends up on the website instead of the
diagram. The patch makes it wait until every diagram on the page has been drawn.

Usage: patch-exporter.py <exporter checkout>
"""
import pathlib
import sys

checkout = pathlib.Path(sys.argv[1])
source = checkout / "src" / "plugin" / "render-api" / "render-api.ts"
text = source.read_text(encoding="utf-8")

anchor = "\t\t// check for invalid plugin blocks\n"
if text.count(anchor) != 1:
    sys.exit(f"patch-exporter: expected exactly one anchor in {source}, found {text.count(anchor)}. "
             "Was EXPORTER_REF changed? Update this patch for the new version.")

addition = (
    "\t\t// Added by the website build: wait for TikZJax diagrams (see .github/website/patch-exporter.py)\n"
    "\t\tExportLog.log(\"Waiting for TikZ diagrams to render...\");\n"
    "\t\tawait waitUntil(\n"
    "\t\t\t() =>\n"
    "\t\t\t\t!preview.containerEl.querySelector(\n"
    "\t\t\t\t\t\"script[type='text/tikz'], svg animate[attributeName='stroke-dasharray']\"\n"
    "\t\t\t\t) || checkCancelled(),\n"
    "\t\t\t90000,\n"
    "\t\t\t100\n"
    "\t\t);\n"
    "\t\tif (checkCancelled()) return undefined;\n"
    "\n"
)

source.write_text(text.replace(anchor, addition + anchor), encoding="utf-8")
print(f"patch-exporter: patched {source}")
