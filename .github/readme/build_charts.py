"""Rebuild the README charts (light + dark SVG) from the vault's own data.

Usage (from the repository root):  python .github/readme/build_charts.py

Scores come from the frontmatter of the notes in Scores/, the day-by-day
workload from the ticked checkboxes in Study Plan.md.
"""
import glob, os, re, sys
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.dirname(os.path.abspath(__file__))


def parse_plan(path):
    src = open(path, encoding="utf-8").read().split("\n")
    days = []
    cur = None
    section = None
    for i, line in enumerate(src):
        m = re.match(r"^## Day (\d+) — (\w+), (\w+ \d+)", line)
        if m:
            cur = dict(day=int(m.group(1)), weekday=m.group(2), date=m.group(3), drills=0, drill_lines=[], callouts=0, generated=0, tests=[], book=[], sette=[], preppy=[])
            days.append(cur); section=None; continue
        if re.match(r"^# ", line):
            cur = None if not line.startswith("# Phase") else cur
            if line.startswith("# March") or line.startswith("# Question Bank") or line.startswith("# Progress"): cur=None
            continue
        if cur is None: continue
        h = re.match(r"^### (.*)", line)
        if h: section = h.group(1); continue
        # drill counts: top-level checked items "- [x] N ..." or "- [x] **Domain — N questions**"
        m = re.match(r"^- \[x\] (?:\*\*[^—*]+— )?(\d+) ", line)
        if m and "Chapter" not in line:
            cur["drills"] += int(m.group(1)); cur["drill_lines"].append(line.strip()[:70])
        # nested under "Easy exercises:" style parents (Day 0)
        m2 = re.match(r"^\t- \[x\] (\d+) ", line)
        if m2 and cur["day"] == 0:
            cur["drills"] += int(m2.group(1)); cur["drill_lines"].append(line.strip()[:70])
        if section and section.startswith("Questions to review") and re.match(r"^> \[!", line):
            cur["callouts"] += 1
        if re.match(r"^> \[!question\]", line): cur["generated"] += 1
        if re.search(r"Full (Bluebook Test \d+|OnePrep Predicted Test #\d+)", line) and line.startswith("- [x]"):
            cur["tests"].append(re.search(r"(Bluebook Test \d+|OnePrep Predicted Test #\d+)", line).group(1))
        mb = re.search(r"Orange Book Chapter (\d+)", line)
        if mb and line.lstrip().startswith("- [x]"): cur["book"].append(int(mb.group(1)))
        ms = re.search(r"Problem Sette #(\d+)", line)
        if ms and line.lstrip().startswith("- [x]"): cur["sette"].append(int(ms.group(1)))
        mp = re.search(r"Preppy Taker - Practice #(\d+)", line)
        if mp and line.lstrip().startswith("- [x]"): cur["preppy"].append(int(mp.group(1)))

    return days


def load_tests():
    tests = []
    for f in glob.glob(os.path.join(ROOT, "Scores", "*.md")):
        txt = open(f, encoding="utf-8").read()
        fm = dict(re.findall(r"^([\w-]+):\s*(.+)$", txt.split("---")[1], re.M))
        if fm.get("type") != "score-entry":
            continue
        name = fm["test"]
        n = re.search(r"(\d+)$", name).group(1)
        src = "OnePrep" if name.startswith("OnePrep") else "Bluebook"
        lab = ("OP" if src == "OnePrep" else "BT") + n
        y, m, d = map(int, fm["date"].split("-"))
        g = lambda k: (int(fm[k]), int(fm[k + "-total"]))
        tests.append((lab, src, date(y, m, d), int(fm["math-score"]), int(fm["correct"]),
                      g("algebra"), g("adv-math"), g("psda"), g("geometry")))
    tests.sort(key=lambda t: (t[2], t[0] != "BT4", int(re.sub(r"\D", "", t[0]))))
    return tests

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

THEMES = {
    "light": dict(
        page="#ffffff", ink="#0b0b0b", ink2="#52514e", muted="#898781", grid="#e1e0d9",
        base="#c3c2b7", band="rgba(11,11,11,0.035)", band2="rgba(11,11,11,0.06)",
        link="#c3c2b7", s1="#2a78d6", s2="#eb6834", s3="#1baf7a",
        seq=["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
             "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281"],
        tag="rgba(11,11,11,0.06)",
    ),
    "dark": dict(
        page="#0d1117", ink="#f0efec", ink2="#c3c2b7", muted="#898781", grid="#2c2c2a",
        base="#383835", band="rgba(255,255,255,0.035)", band2="rgba(255,255,255,0.06)",
        link="#52514e", s1="#3987e5", s2="#d95926", s3="#199e70",
        seq=["#0d366b", "#104281", "#184f95", "#1c5cab", "#256abf", "#2a78d6", "#3987e5",
             "#5598e7", "#6da7ec", "#86b6ef", "#9ec5f4", "#b7d3f6"], seq_dark=True,
        tag="rgba(255,255,255,0.07)",
    ),
}

TESTS = load_tests()
PLAN = parse_plan(os.path.join(ROOT, "Study Plan.md"))
OFFICIAL = ("Official SAT", date(2026, 3, 14), 770)
D0 = date(2026, 2, 8)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=12, fill="#000", anchor="start", weight=400, extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" {extra}>{esc(s)}</text>')


def svg_wrap(w, h, body, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="t d" font-family="{FONT}">'
            f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>{body}</svg>')


def rounded_top_bar(x, y, w, h, r, fill):
    """Column with 4px rounded data-end, square at the baseline."""
    r = min(r, h, w / 2)
    if h <= 0:
        return ""
    return (f'<path d="M{x:.1f},{y + h:.1f} V{y + r:.1f} Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f} '
            f'H{x + w - r:.1f} Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f} V{y + h:.1f} Z" fill="{fill}"/>')


# ---------------------------------------------------------------- hero banner
def hero(t):
    W, H = 960, 196
    b = []
    b.append(text(0, 22, "SAT MATH · FEB 8 → MAR 14, 2026", 12, t["muted"], weight=600, extra='letter-spacing="1.2"'))
    # hero figure
    b.append(text(0, 104, "770", 76, t["ink"], weight=700))
    b.append(text(150, 70, "Official SAT Math score", 15, t["ink"], weight=600))
    b.append(text(150, 92, "Target was 730 (KU Leuven requirement)", 13, t["ink2"]))
    b.append(text(150, 112, "Range 740–800 · all four domains in the top band", 13, t["ink2"]))
    # stat tiles
    tiles = [("+170", "points from the first", "diagnostic (600)"),
             ("97th", "percentile among all", "testers · 98th in Brazil"),
             ("24", "planned study days", "in four phases"),
             ("12", "full-length timed", "practice tests"),
             ("85", "reviewed questions", "logged in the vault")]
    x0, y0, tw, gap = 0, 140, 180, 15
    for i, (v, l1, l2) in enumerate(tiles):
        x = x0 + i * (tw + gap)
        b.append(f'<rect x="{x}" y="{y0 - 6}" width="2" height="54" rx="1" fill="{t["s1"] if i == 0 else t["grid"]}"/>')
        b.append(text(x + 12, y0 + 18, v, 24, t["ink"], weight=650))
        b.append(text(x + 12, y0 + 34, l1, 11.5, t["ink2"]))
        b.append(text(x + 12, y0 + 48, l2, 11.5, t["ink2"]))
    return svg_wrap(W, H, "".join(b), "SAT Math prep at a glance",
                    "Official SAT Math 770, 40 above the 730 target; +170 from the first diagnostic; "
                    "97th percentile; 24 planned study days; 12 full-length practice tests; 85 reviewed questions.")


# ---------------------------------------------------------- score trajectory
PHASES = [  # label line 1, line 2, start, end (inclusive days)
    ("Diagnostics", "", date(2026, 2, 8), date(2026, 2, 9)),
    ("Phase 1", "Foundation", date(2026, 2, 16), date(2026, 2, 23)),
    ("Phase 2", "Targeted drilling", date(2026, 2, 24), date(2026, 3, 2)),
    ("Phase 3", "Integration & pacing", date(2026, 3, 3), date(2026, 3, 9)),
    ("Phase 4", "Final review", date(2026, 3, 10), date(2026, 3, 12)),
    ("Test", "day", date(2026, 3, 14), date(2026, 3, 14)),
]


def trajectory(t):
    W, H = 960, 480
    L, R, T, B = 52, 150, 128, 48
    pw, ph = W - L - R, H - T - B
    x_start, x_end = -0.8, 36.8  # days since Feb 8
    y_min, y_max = 560, 800

    def X(d, off=0.0):
        dd = (d - D0).days + off
        return L + (dd - x_start) / (x_end - x_start) * pw

    def Y(v):
        return T + (y_max - v) / (y_max - y_min) * ph

    b = []
    # title + legend
    b.append(text(0, 22, "Every full-length practice test, then the real one", 17, t["ink"], weight=650))
    b.append(text(0, 43, "SAT Math scaled score (200–800), by test date", 13, t["ink2"]))
    lx, ly = 0, 72
    # legend: Bluebook circle
    b.append(f'<circle cx="{lx + 6}" cy="{ly - 4}" r="5" fill="{t["s1"]}"/>')
    b.append(text(lx + 17, ly, "Bluebook practice test (College Board)", 12.5, t["ink2"]))
    lx += 262
    b.append(f'<rect x="{lx + 2}" y="{ly - 8}" width="8" height="8" fill="{t["s2"]}" transform="rotate(45 {lx + 6} {ly - 4})"/>')
    b.append(text(lx + 17, ly, "OnePrep predicted test (harder calibration)", 12.5, t["ink2"]))
    lx += 286
    b.append(f'<circle cx="{lx + 6}" cy="{ly - 4}" r="6" fill="{t["s3"]}"/>')
    b.append(text(lx + 17, ly, "Official SAT", 12.5, t["ink2"]))
    lx += 100
    b.append(f'<line x1="{lx}" y1="{ly - 4}" x2="{lx + 18}" y2="{ly - 4}" stroke="{t["ink2"]}" stroke-width="1.5"/>')
    b.append(text(lx + 24, ly, "730 target", 12.5, t["ink2"]))

    # phase bands
    for i, (l1, l2, s, e) in enumerate(PHASES):
        x1, x2 = X(s, -0.5), X(e, 0.5)
        b.append(f'<rect x="{x1:.1f}" y="{T - 36}" width="{x2 - x1:.1f}" height="{ph + 36}" fill="{t["band"] if i % 2 else t["band2"]}"/>')
        cx = (x1 + x2) / 2
        if l1 == "Diagnostics":
            b.append(text(x1 + 4, T - 21, "Pre-plan", 11, t["muted"], weight=600))
            b.append(text(x1 + 4, T - 8, "diagnostics", 10.5, t["muted"]))
        else:
            b.append(text(cx, T - 21, l1, 11, t["muted"], "middle", 600))
            b.append(text(cx, T - 8, l2, 10.5, t["muted"], "middle"))
    # y grid
    for v in (600, 650, 700, 750, 800):
        y = Y(v)
        b.append(f'<line x1="{L}" y1="{y:.1f}" x2="{L + pw}" y2="{y:.1f}" stroke="{t["grid"]}" stroke-width="1"/>')
        b.append(text(L - 8, y + 4, str(v), 11.5, t["muted"], "end", extra='style="font-variant-numeric:tabular-nums"'))
    b.append(f'<line x1="{L}" y1="{T + ph}" x2="{L + pw}" y2="{T + ph}" stroke="{t["base"]}" stroke-width="1"/>')
    # x ticks
    for d, lab in [(date(2026, 2, 8), "Feb 8"), (date(2026, 2, 15), "Feb 15"), (date(2026, 2, 22), "Feb 22"),
                   (date(2026, 3, 1), "Mar 1"), (date(2026, 3, 8), "Mar 8"), (date(2026, 3, 14), "Mar 14")]:
        x = X(d)
        b.append(f'<line x1="{x:.1f}" y1="{T + ph}" x2="{x:.1f}" y2="{T + ph + 5}" stroke="{t["base"]}" stroke-width="1"/>')
        b.append(text(x, T + ph + 20, lab, 11.5, t["muted"], "middle"))
    # travel note
    xt = X(date(2026, 2, 23))
    b.append(text(xt, Y(575), "Feb 22–24: moving from", 10.5, t["muted"], "middle"))
    b.append(text(xt, Y(575) + 13, "Belgium back to Brazil", 10.5, t["muted"], "middle"))
    # target line
    yT = Y(730)
    b.append(f'<line x1="{L}" y1="{yT:.1f}" x2="{L + pw}" y2="{yT:.1f}" stroke="{t["ink2"]}" stroke-width="1.5"/>')
    b.append(text(L + pw + 8, yT + 4, "730 · KU Leuven", 11.5, t["ink2"]))
    b.append(text(L + pw + 8, yT + 18, "requirement", 11.5, t["ink2"]))
    # points
    pts = []
    for (lab, src, d, sc, *_r) in TESTS:
        off = -0.3 if lab == "BT4" else (0.3 if lab == "BT5" else 0)
        pts.append((X(d, off), Y(sc), lab, src, sc))
    pts.append((X(OFFICIAL[1]), Y(OFFICIAL[2]), "OFF", "Official", OFFICIAL[2]))
    path = " ".join(("M" if i == 0 else "L") + f"{x:.1f},{y:.1f}" for i, (x, y, *_r) in enumerate(pts))
    b.append(f'<path d="{path}" fill="none" stroke="{t["link"]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    ring = t["page"]
    for (x, y, lab, src, sc) in pts:
        if src == "Bluebook":
            b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{ring}"/><circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{t["s1"]}"/>')
        elif src == "OnePrep":
            b.append(f'<rect x="{x - 6.2:.1f}" y="{y - 6.2:.1f}" width="12.4" height="12.4" fill="{ring}" transform="rotate(45 {x:.1f} {y:.1f})"/>'
                     f'<rect x="{x - 4.4:.1f}" y="{y - 4.4:.1f}" width="8.8" height="8.8" fill="{t["s2"]}" transform="rotate(45 {x:.1f} {y:.1f})"/>')
        else:
            b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{ring}"/><circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{t["s3"]}"/>')
    # selective labels
    def lab_at(lab):
        return next(p for p in pts if p[2] == lab)
    x, y, *_ = lab_at("BT4")
    b.append(text(x + 10, y + 4, "600 · first diagnostic", 12, t["ink"], weight=600))
    x, y, *_ = lab_at("BT9")
    b.append(text(x - 4, y - 14, "750 · target beaten", 12, t["ink"], "end", 600))
    x, y, *_ = lab_at("OP1")
    b.append(text(x, y + 22, "640 · OnePrep #1", 12, t["ink"], "middle", 600))
    b.append(text(x, y + 37, "0/5 on linear equations", 11, t["ink2"], "middle"))
    b.append(text(x, y + 51, "→ drill volume doubled", 11, t["ink2"], "middle"))
    x, y, *_ = lab_at("OFF")
    b.append(text(x + 14, y + 5, "770 · official", 13, t["ink"], weight=700))
    return svg_wrap(W, H, "".join(b), "SAT Math score trajectory",
                    "Line chart of 12 full-length practice tests and the official SAT from Feb 8 to Mar 14, 2026: "
                    "600, 680, 660, 700, 710, 750, OnePrep 640, OnePrep 740, 750, OnePrep 740, OnePrep 740, 730, official 770. "
                    "Target line at 730.")


# ------------------------------------------------------------- domain heatmap
DOMAINS = ["Algebra", "Advanced Math", "Problem Solving & Data Analysis", "Geometry & Trigonometry"]


def heatmap(t):
    W = 960
    L, T = 214, 92
    cw, chh, gap = 51, 40, 2
    n = len(TESTS)
    H = T + 4 * (chh + gap) + 76
    b = []
    b.append(text(0, 22, "Accuracy by domain, test by test", 17, t["ink"], weight=650))
    b.append(text(0, 43, "Share of questions answered correctly in each SAT Math domain", 13, t["ink2"]))
    lo, hi = 40, 100

    def col(p):
        k = (p - lo) / (hi - lo)
        k = max(0, min(1, k))
        idx = round(k * (len(t["seq"]) - 1))
        light_text = idx < 7 if t.get("seq_dark") else idx >= 6
        return t["seq"][idx], ("#ffffff" if light_text else "#0b0b0b")

    for j, row in enumerate(TESTS):
        x = L + j * (cw + gap)
        lab, src, d = row[0], row[1], row[2]
        b.append(text(x + cw / 2, T - 24, lab, 12, t["ink"], "middle", 600))
        b.append(text(x + cw / 2, T - 9, d.strftime("%b %-d"), 10.5, t["muted"], "middle"))
        for i in range(4):
            c, tot = row[5 + i]
            p = round(100 * c / tot)
            fill, ink = col(p)
            y = T + i * (chh + gap)
            b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{chh}" rx="4" fill="{fill}"/>')
            b.append(text(x + cw / 2, y + chh / 2 + 4.5, f"{p}%", 12.5, ink, "middle", 600,
                          'style="font-variant-numeric:tabular-nums"'))
    for i, dn in enumerate(DOMAINS):
        y = T + i * (chh + gap) + chh / 2 + 4.5
        b.append(text(0, y, dn, 12.5, t["ink"], weight=500))
    # official column
    xo = L + n * (cw + gap) + 14
    b.append(text(xo + 38, T - 24, "Official", 12, t["ink"], "middle", 700))
    b.append(text(xo + 38, T - 9, "Mar 14", 10.5, t["muted"], "middle"))
    for i in range(4):
        y = T + i * (chh + gap)
        b.append(f'<rect x="{xo}" y="{y}" width="76" height="{chh}" rx="4" fill="none" stroke="{t["s3"]}" stroke-width="1.5"/>')
        b.append(text(xo + 38, y + chh / 2 + 4.5, "680–800", 12.5, t["ink"], "middle", 600))
    # source markers under columns
    ys = T + 4 * (chh + gap) + 6
    for j, row in enumerate(TESTS):
        x = L + j * (cw + gap) + cw / 2
        if row[1] == "Bluebook":
            b.append(f'<circle cx="{x}" cy="{ys + 4}" r="3.5" fill="{t["s1"]}"/>')
        else:
            b.append(f'<rect x="{x - 3.2}" y="{ys + 0.8}" width="6.4" height="6.4" fill="{t["s2"]}" transform="rotate(45 {x} {ys + 4})"/>')
    # legend: ramp
    ly = H - 30
    b.append(text(0, ly + 9, "Correct", 11.5, t["ink2"]))
    for k, c in enumerate(t["seq"]):
        b.append(f'<rect x="{60 + k * 18}" y="{ly}" width="16" height="10" rx="2" fill="{c}"/>')
    b.append(text(60, ly + 26, "≤40%", 10.5, t["muted"]))
    b.append(text(60 + 12 * 18 - 2, ly + 26, "100%", 10.5, t["muted"], "end"))
    b.append(f'<circle cx="{300}" cy="{ly + 5}" r="3.5" fill="{t["s1"]}"/>')
    b.append(text(310, ly + 9, "Bluebook", 11.5, t["ink2"]))
    b.append(f'<rect x="{376.8}" y="{ly + 1.8}" width="6.4" height="6.4" fill="{t["s2"]}" transform="rotate(45 380 {ly + 5})"/>')
    b.append(text(390, ly + 9, "OnePrep", 11.5, t["ink2"]))
    b.append(f'<rect x="{454}" y="{ly}" width="16" height="10" rx="2" fill="none" stroke="{t["s3"]}" stroke-width="1.5"/>')
    b.append(text(476, ly + 9, "Official: College Board reports a score band per domain, not a count", 11.5, t["ink2"]))
    return svg_wrap(W, H, "".join(b), "Accuracy by domain",
                    "Heatmap of percent correct per SAT Math domain across 12 practice tests; "
                    "Advanced Math rose from 47% to the mid-80s, Geometry from 50% to 75-100%; "
                    "the official test placed all four domains in the 680-800 band.")


# ------------------------------------------------------------ daily workload
def daily(t):
    W = 960
    L, T = 150, 96
    days = PLAN + [dict(day="—", date="Mar 13"), dict(day="—", date="Mar 14")]
    n = len(days)
    cw = (W - L) / n
    bar_h = 96
    rows_y0 = T + bar_h + 34
    rh = 30
    H = rows_y0 + 5 * rh + 64
    b = []
    b.append(text(0, 22, "What the 24 days actually looked like", 17, t["ink"], weight=650))
    b.append(text(0, 43, "Every planned item that was ticked off in Study Plan.md, day by day", 13, t["ink2"]))

    # phase bands (by day number)
    bands = [("Day 0", 0, 0), ("Phase 1 · Foundation", 1, 7), ("Phase 2 · Targeted drilling", 8, 14),
             ("Phase 3 · Integration & pacing", 15, 21), ("Phase 4 · Final", 22, 24), ("Exam", 25, 26)]
    for i, (lab, a, z) in enumerate(bands):
        x1, x2 = L + a * cw, L + (z + 1) * cw
        b.append(f'<rect x="{x1:.1f}" y="{T - 30}" width="{x2 - x1:.1f}" height="{H - T - 6}" fill="{t["band"] if i % 2 else t["band2"]}"/>')
        if lab not in ("Day 0",):
            b.append(text((x1 + x2) / 2, T - 15, lab, 11, t["muted"], "middle", 600))
    # drills bars
    mx = 58
    for v in (25, 50):
        y = T + bar_h - v / mx * bar_h
        b.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W}" y2="{y:.1f}" stroke="{t["grid"]}" stroke-width="1"/>')
        b.append(text(L - 8, y + 4, str(v), 11, t["muted"], "end"))
    b.append(f'<line x1="{L}" y1="{T + bar_h}" x2="{W}" y2="{T + bar_h}" stroke="{t["base"]}" stroke-width="1"/>')
    b.append(text(0, T + bar_h / 2 - 4, "Question-bank", 12.5, t["ink"], weight=500))
    b.append(text(0, T + bar_h / 2 + 12, "drills", 12.5, t["ink"], weight=500))
    bw = min(18, cw - 6)
    for k, d in enumerate(PLAN):
        v = d["drills"]
        x = L + k * cw + (cw - bw) / 2
        h = v / mx * bar_h
        b.append(rounded_top_bar(x, T + bar_h - h, bw, h, 4, t["s1"]))
        if v in (50, 44, 37):
            b.append(text(x + bw / 2, T + bar_h - h - 6, str(v), 11, t["ink2"], "middle", 600))
    # day labels: plan day number + planned date
    b.append(text(L - 8, T + bar_h + 14, "Plan day", 10, t["muted"], "end"))
    b.append(text(L - 8, T + bar_h + 26, "planned date", 9.5, t["muted"], "end"))
    for k, d in enumerate(days):
        cx = L + k * cw + cw / 2
        if isinstance(d["day"], int):
            b.append(text(cx, T + bar_h + 14, str(d["day"]), 10.5, t["ink2"], "middle", 600))
        mon, dd = d["date"].split(" ")
        lab = d["date"] if dd in ("1", "16") or not isinstance(d["day"], int) else dd
        if not isinstance(d["day"], int):
            b.append(text(cx, T + bar_h + 14, mon, 10, t["ink2"], "middle", 600))
            lab = dd
        b.append(text(cx, T + bar_h + 26, lab, 9.5 if len(lab) < 5 else 8.5, t["muted"], "middle"))
    rows = [("Full practice test", "tests"), ("1600.io chapter", "book"), ("Problem Sette set", "sette"),
            ("OnePrep Preppy Taker", "preppy"), ("Questions reviewed", "callouts")]
    short = {"Bluebook Test 7": ("BT7", "700"), "Bluebook Test 8": ("BT8", "710"), "Bluebook Test 9": ("BT9", "750"),
             "OnePrep Predicted Test #1": ("OP1", "640"), "OnePrep Predicted Test #2": ("OP2", "740"),
             "Bluebook Test 10": ("BT10", "750"), "OnePrep Predicted Test #3": ("OP3", "740"),
             "OnePrep Predicted Test #4": ("OP4", "740"), "Bluebook Test 11": ("BT11", "730")}
    for r, (name, key) in enumerate(rows):
        y = rows_y0 + r * rh
        b.append(f'<line x1="0" y1="{y - 6}" x2="{W}" y2="{y - 6}" stroke="{t["grid"]}" stroke-width="1"/>')
        b.append(text(0, y + 13, name, 12.5, t["ink"], weight=500))
        for k, d in enumerate(PLAN):
            cx = L + k * cw + cw / 2
            vals = d[key]
            if key == "tests" and vals:
                a, s = short[vals[0]]
                fill = t["s1"] if a.startswith("BT") else t["s2"]
                b.append(f'<rect x="{cx - 15}" y="{y - 1}" width="30" height="20" rx="4" fill="{fill}"/>')
                b.append(text(cx, y + 13, s, 11, "#ffffff", "middle", 650))
            elif key in ("book", "sette") and vals:
                lab = "·".join(str(v) for v in vals)
                fs = 10.5 if len(lab) <= 3 else 9.5
                w = max(20, len(lab) * fs * 0.62 + 8)
                b.append(f'<rect x="{cx - w / 2:.1f}" y="{y}" width="{w:.1f}" height="18" rx="9" fill="{t["tag"]}"/>')
                b.append(text(cx, y + 13, lab, fs, t["ink"], "middle", 600))
            elif key == "preppy" and vals:
                for q in range(len(vals)):
                    b.append(f'<circle cx="{cx - (len(vals) - 1) * 5 + q * 10:.1f}" cy="{y + 9}" r="4" fill="{t["ink2"]}"/>')
            elif key == "callouts" and vals:
                b.append(text(cx, y + 13, str(vals), 11, t["ink2"], "middle", 600))
        if key == "tests":
            # exam day
            cx = L + 26 * cw + cw / 2
            b.append(f'<rect x="{cx - 15}" y="{y - 1}" width="30" height="20" rx="4" fill="{t["s3"]}"/>')
            b.append(text(cx, y + 13, "770", 11, "#ffffff", "middle", 700))
    # travel annotation under bars in phase 1/2 gap
    xa = L + 6 * cw
    b.append(text(xa + 1.5 * cw, T + bar_h - 30, "packing, flight", 10, t["muted"], "middle"))
    b.append(text(xa + 1.5 * cw, T + bar_h - 18, "Belgium → Brazil", 10, t["muted"], "middle"))
    b.append(text(xa + 1.5 * cw, T + bar_h - 6, "& college classes", 10, t["muted"], "middle"))
    foot = H - 36
    notes = ["Drills = College Board question-bank questions. From Day 16 on, each day's count was set by how many college classes Felipe had.",
             "Columns are plan days, not calendar days: the last week ran about two days behind and was compressed",
             "(BT11 was planned for Mar 11 and taken Mar 12). Chips: blue = Bluebook, orange = OnePrep, green = official SAT."]
    for q, line in enumerate(notes):
        b.append(text(0, foot + q * 14, line, 10.5, t["muted"]))
    return svg_wrap(W, H, "".join(b), "Daily workload across the 24-day plan",
                    "Day-by-day view of the study plan: question-bank drills per day (peaks of 50 and 44 in Phase 3), "
                    "full practice tests, 1600.io book chapters, Problem Sette sets, OnePrep Preppy Taker practices "
                    "and the number of questions reviewed in the vault.")


for name, fn in [("hero", hero), ("score-trajectory", trajectory), ("domain-heatmap", heatmap), ("daily-workload", daily)]:
    for mode, th in THEMES.items():
        open(os.path.join(OUT, f"{name}-{mode}.svg"), "w", encoding="utf-8").write(fn(th))
print("ok")
