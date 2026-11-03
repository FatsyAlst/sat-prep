#!/usr/bin/env python3
"""Final touches on the exported site, followed by a strict check of the result.

Usage: finish-site.py <vault dir> <site dir>

Touches
  - The Pixel Banner plugin draws the Homepage banner and logo from Obsidian-internal
    blob: URLs that mean nothing on the web. Point them at the real image files, using the
    note's own `banner:` and `icon-image:` properties, and restore the banner layout (text
    starting below the picture at the note's `content-start`, logo beside the title).
  - TikZ diagrams are drawn with Computer Modern fonts that the TikZJax plugin ships as a
    4.7 MB stylesheet. Instead of loading that on every page, save only the fonts the
    diagrams actually use (plus the plugin's small layout rule) and link that file from the
    pages that have a diagram.

Check (the script exits with an error if any of these fail, so a broken site is not published)
  - every note in the vault has a page,
  - no Obsidian-internal blob: link is left,
  - no TikZ diagram is still a loading spinner or a failed drawing,
  - every MathJax font the formulas ask for is on the site,
  - every stylesheet, script, image or video a page loads exists and is not an absolute path
    (which would break on a project site such as user.github.io/repo/).
"""
import html
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

if len(sys.argv) != 3:
    sys.exit("usage: finish-site.py <vault dir> <site dir>")
vault = Path(sys.argv[1]).resolve()
site = Path(sys.argv[2]).resolve()

problems: list[str] = []
warnings: list[str] = []


def norm(text: str) -> str:
    """Compare names the way the exporter rewrites them (case, spaces, punctuation)."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


pages = sorted(site.rglob("*.html"))
page_by_key = {norm(str(p.relative_to(site).with_suffix(""))): p for p in pages}
file_by_key = {norm(str(p.relative_to(site))): p for p in site.rglob("*") if p.is_file()}
notes = [
    n
    for n in sorted(vault.rglob("*.md"))
    if not any(part.startswith(".") for part in n.relative_to(vault).parts)
]

# Every exported page has <base href=".."> (or "."), so its relative links start at the site
# root rather than at the page's own folder.
BASE = re.compile(r"<base\s[^>]*?href=\"([^\"]*)\"", re.I)


def base_dir(page: Path, text: str) -> Path:
    match = BASE.search(text)
    if match:
        return (page.parent / match.group(1)).resolve()
    # Fragments such as site-lib/html/file-tree-content.html are loaded into a page by script,
    # so their links also start at the site root.
    return site if "site-lib" in page.relative_to(site).parts else page.parent.resolve()


def url_from(base: Path, target: Path) -> str:
    rel = os.path.relpath(target, base).replace(os.sep, "/")
    return urllib.parse.quote(rel, safe="/-._~")


def frontmatter(note: Path) -> dict[str, str]:
    text = read(note)
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    data = {}
    for line in text[3:end].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if match:
            data[match.group(1)] = match.group(2).strip("\"'")
    return data


def exported_file(value: str) -> str | None:
    """A note property that names a vault file (or a web address) -> where it is on the site."""
    value = value.strip().removeprefix("!").removeprefix("[[").removesuffix("]]").split("|")[0]
    if re.match(r"^https?://", value):
        return value
    target = file_by_key.get(norm(value))
    return str(target.relative_to(site)).replace(os.sep, "/") if target else None


# ---------------------------------------------------------------- 1. banner and logo
PIXEL_BANNER_SETTINGS = vault / ".obsidian" / "plugins" / "pexels-banner" / "data.json"
PIXEL_BANNER = json.loads(read(PIXEL_BANNER_SETTINGS)) if PIXEL_BANNER_SETTINGS.exists() else {}


def add_style(text: str, tag_at: int, style: str) -> str:
    """Add CSS declarations to the opening tag that starts at tag_at."""
    end = text.index(">", tag_at)
    tag = text[tag_at:end]
    match = re.search(r'\sstyle="([^"]*)"', tag)
    if match:
        merged = match.group(1).rstrip("; ") + "; " + style
        tag = tag[: match.start(1)] + merged + tag[match.end(1):]
    else:
        tag += f' style="{style}"'
    return text[:tag_at] + tag + text[end:]


BLOB = re.compile(r"blob:app://obsidian\.md/[0-9a-f-]+")
BANNER_DIV = re.compile(r'<div class="pixel-banner-image"[^>]*>')
ICON_IMG = re.compile(r'<img\b[^>]*\bclass="banner-icon-image[^"]*"[^>]*>')
banner_pages = 0

for note in notes:
    props = frontmatter(note)
    if "banner" not in props and "icon-image" not in props:
        continue
    page = page_by_key.get(norm(str(note.relative_to(vault).with_suffix(""))))
    if page is None:
        continue  # reported below as a note without a page
    text = read(page)
    base = base_dir(page, text)

    def where(prop: str) -> str | None:
        found = exported_file(props[prop]) if prop in props else None
        if found is None and prop in props:
            problems.append(f"{note.relative_to(vault)}: {prop} '{props[prop]}' is not on the site")
        if found is None or found.startswith("http"):
            return found
        return url_from(base, site / found)

    banner_url, icon_url = where("banner"), where("icon-image")
    original = text
    if banner_url:
        text = BANNER_DIV.sub(lambda m: BLOB.sub(banner_url, m.group(0)), text)
    if icon_url:
        text = ICON_IMG.sub(
            lambda m: BLOB.sub(icon_url, m.group(0)).replace(" is-unresolved", ""), text
        )

    # Layout. In Obsidian, Pixel Banner sets its CSS variables on the note's view (so the logo
    # sees them too), adds the gap around the banner and pushes the text down to the note's
    # `content-start`. The export only keeps the variables on the banner itself, so the title
    # and logo end up on top of the picture. Restore the same three things here.
    banner = BANNER_DIV.search(text)
    if banner:
        doc_at = text.rfind('<div class="obsidian-document', 0, banner.start())
        sizer_at = text.rfind('<div class="markdown-preview-sizer', 0, banner.start())
        if doc_at < 0 or sizer_at < doc_at:
            problems.append(f"{page.relative_to(site)}: could not place the banner layout")
        else:
            variables = dict(re.findall(r"(--pixel-banner-[\w-]+):\s*([^;\"]+)", banner.group(0)))
            start = re.sub(r"[^0-9.]", "", props.get("content-start", "")) or str(
                PIXEL_BANNER.get("contentStartPosition", 355)
            )
            variables["--pixel-banner-content-start"] = f"{start}px"
            variables["--pixel-banner-banner-gap"] = f"{PIXEL_BANNER.get('bannerGap', 12)}px"
            doc_style = "; ".join(f"{k}: {v.strip()}" for k, v in variables.items())
            # the sizer first (it comes later in the text), then the document div
            text = add_style(text, sizer_at, "padding-top: var(--pixel-banner-content-start)")
            text = add_style(text, doc_at, doc_style)
    if text != original:
        page.write_text(text, encoding="utf-8")
        banner_pages += 1
        print(f"banner: {page.relative_to(site)}: image {banner_url}, logo {icon_url}")

# ---------------------------------------------------------------- 2. TikZ fonts
TIKZ_CSS = vault / ".obsidian" / "plugins" / "obsidian-tikzjax" / "styles.css"
tikz_pages = [p for p in pages if "block-language-tikz" in read(p)]
tikz_font_pages = 0

if tikz_pages and TIKZ_CSS.exists():
    css = read(TIKZ_CSS)
    face_rule = re.compile(r"@font-face\s*\{[^}]*\}")
    faces: dict[str, str] = {}
    for rule in face_rule.findall(css):
        family = re.search(r"font-family:\s*([^;]+);", rule)
        if family:
            faces[family.group(1).strip().strip("\"'")] = rule
    layout = face_rule.sub("", css).strip()  # the plugin's own rule that centres the drawings

    fonts_on_page: dict[Path, set[str]] = {}
    for page in tikz_pages:
        text = read(page)
        drawn = "\n".join(re.findall(r"<svg\b.*?</svg>", text, flags=re.S))
        used = {
            name
            for name in faces
            if name in drawn
            and re.search(r"(?<![A-Za-z0-9_-])" + re.escape(name) + r"(?![A-Za-z0-9_-])", drawn)
        }
        if used:
            fonts_on_page[page] = used

    if fonts_on_page:
        all_fonts = sorted(set().union(*fonts_on_page.values()))
        css_path = site / "site-lib" / "styles" / "tikzjax.css"
        css_path.parent.mkdir(parents=True, exist_ok=True)
        css_path.write_text(
            layout + "\n" + "\n".join(faces[name] for name in all_fonts) + "\n", encoding="utf-8"
        )
        for page in fonts_on_page:
            text = read(page)
            link = f'<link rel="stylesheet" href="{url_from(base_dir(page, text), css_path)}">'
            if link not in text:
                page.write_text(text.replace("</head>", link + "\n</head>", 1), encoding="utf-8")
                tikz_font_pages += 1
        print(
            f"tikz: {len(all_fonts)} fonts ({css_path.stat().st_size // 1024} KB) "
            f"linked from {tikz_font_pages} pages: {', '.join(all_fonts)}"
        )
    else:
        problems.append("TikZ blocks are on the site but none of them contains a drawing that uses a TikZ font")

# ---------------------------------------------------------------- 3. checks
ASSET_TAG = re.compile(r"<(?:link|script|img|video|audio|source|iframe|embed)\b[^>]*>", re.I)
ATTR = re.compile(r"\b(?:href|src)=\"([^\"]+)\"")
LINK_TAG = re.compile(r"<a\b[^>]*\bhref=\"([^\"]+)\"", re.I)
MATHJAX_URL = re.compile(r"url\([\"']?(site-lib/fonts/mathjax_[^\"')]+)[\"']?\)")
EXTERNAL = re.compile(r"^([a-z][a-z0-9+.-]*:|#|//)", re.I)

missing_assets: dict[str, set[str]] = {}
missing_links: dict[str, set[str]] = {}
absolute_urls: dict[str, set[str]] = {}
missing_fonts: dict[str, set[str]] = {}
mathjax_fonts: set[str] = set()


def resolve(base: Path, url: str) -> Path | None:
    url = html.unescape(url)
    if not url or EXTERNAL.match(url):
        return None
    path = urllib.parse.unquote(url.split("#")[0].split("?")[0])
    return (base / path).resolve() if path else None


def shown(target: Path) -> str:
    try:
        return str(target.relative_to(site))
    except ValueError:
        return str(target)


for page in pages:
    text = read(page)
    name = str(page.relative_to(site))
    base = base_dir(page, text)

    if BLOB.search(text):
        problems.append(f"{name}: an Obsidian-internal blob: link is still in the page")
    if "invalid.site" in text:
        problems.append(f"{name}: a TikZ drawing failed (placeholder image)")
    if 'type="text/tikz"' in text:
        problems.append(f"{name}: a TikZ diagram was never drawn (its source is still in the page)")
    if 'attributeName="stroke-dasharray"' in text:
        problems.append(f"{name}: a TikZ diagram is still a loading spinner")

    for url in MATHJAX_URL.findall(text):
        mathjax_fonts.add(url)
        target = resolve(base, url)
        if target is not None and not target.exists():
            missing_fonts.setdefault(shown(target), set()).add(name)

    for tag in ASSET_TAG.findall(text):
        for url in ATTR.findall(tag):
            if url.startswith("/") and not url.startswith("//"):
                absolute_urls.setdefault(url, set()).add(name)
                continue
            target = resolve(base, url)
            if target is not None and not target.exists():
                missing_assets.setdefault(shown(target), set()).add(name)
    for url in LINK_TAG.findall(text):
        target = resolve(base, url)
        if target is not None and not target.exists():
            missing_links.setdefault(html.unescape(url), set()).add(name)

for note in notes:
    if norm(str(note.relative_to(vault).with_suffix(""))) not in page_by_key:
        problems.append(f"{note.relative_to(vault)}: this note has no page on the site")

for font, on in sorted(missing_fonts.items()):
    problems.append(f"missing MathJax font {font} (needed by {len(on)} pages)")
for url, on in sorted(absolute_urls.items()):
    problems.append(f"absolute path {url} breaks on a project site (used by {len(on)} pages)")
for asset, on in sorted(missing_assets.items()):
    problems.append(f"missing file {asset} (used by {len(on)} pages, e.g. {sorted(on)[0]})")
for url, on in sorted(missing_links.items()):
    warnings.append(f"link to {url} goes nowhere (on {len(on)} pages, e.g. {sorted(on)[0]})")

# ---------------------------------------------------------------- 4. report
print(
    f"\n{len(notes)} notes, {len(pages)} pages, {banner_pages} banner page(s) repaired, "
    f"{len(tikz_pages)} pages with TikZ, {len(mathjax_fonts)} MathJax fonts referenced"
)
for warning in warnings[:25]:
    print(f"warning: {warning}")
if problems:
    print(f"\n{len(problems)} PROBLEMS:")
    for problem in problems[:60]:
        print(f"  - {problem}")
    sys.exit(1)
print("site check passed")
