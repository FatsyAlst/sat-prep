---
type: homepage
tags:
  - dashboard
cssclasses:
  - wide
banner: media/sat.jpg
banner-height: 540
content-start: 351
banner-fade: -110
banner-x: 59
banner-y: 80
banner-radius: 20
banner-align: center
pixel-banner-flag-color: blue-fade-light
icon-image: media/sat-logo.png
banner-icon-image-alignment: right
icon-x: 70
icon-y: -95
icon-size: 110
icon-image-size-multiplier: 1
---

# SAT Math Prep

> [!success] 🏆 Official SAT Math: **770**, done
> Test taken **March 14, 2026**. Target was 730 and the official score came in **40 points above it**, higher than any practice test.
> 97th percentile overall · 98th percentile in Brazil · all four Math domains in the top band (680–800).
> → [[Official SAT — March 2026]]

**Exam date:** March 14, 2026 — ✅ taken
**Target score:** 730 → **Official: 770** ✅
**Practice best:** 750 (BT9 / BT10) | **Practice latest:** 730 (BT11)
**Status:** Prep complete. Admitted to KU Leuven 🎓
**Study plan:** [[Study Plan]] — all 4 phases completed

---

## Score Progression

```chart
type: line
labels: [BT4, BT5, BT6, BT7, BT8, BT9, OP1, OP2, BT10, OP3, OP4, BT11]
series:
  - title: Overall (%)
    data: [59, 77, 75, 86, 82, 91, 77, 91, 91, 91, 91, 86]
  - title: Algebra (%)
    data: [53, 93, 80, 80, 93, 87, 63, 100, 93, 93, 88, 93]
  - title: Advanced Math (%)
    data: [47, 64, 87, 87, 79, 86, 83, 94, 86, 85, 79, 86]
  - title: PSDA (%)
    data: [100, 88, 57, 100, 71, 100, 78, 67, 100, 89, 100, 88]
  - title: Geometry (%)
    data: [50, 57, 57, 83, 75, 100, 100, 83, 88, 100, 100, 75]
tension: 0.2
width: 90%
labelColors: true
fill: false
beginAtZero: false
spanGaps: true
yMin: 0
yMax: 100
```

> Update: add new test labels and data points to the arrays above after each practice test.

---

## Performance Overview

```dataviewjs
const tests = dv.pages('"Scores"')
    .where(p => p.type === "score-entry")
    .sort(p => p.date, 'asc');

const official = dv.pages('"Scores"')
    .where(p => p.type === "official-score")
    .sort(p => p.date, 'asc');

const labels = tests.map(t => t.test).values.concat(official.map(o => o.test + ' 🏆').values);
const mathScores = tests.map(t => t["math-score"]).values.concat(official.map(o => o["math-score"]).values);
const correctData = tests.map(t => t.correct).values.concat(official.map(() => null).values);
const target = 730;

const chartData = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Math Score',
                data: mathScores,
                borderColor: 'rgba(59, 130, 246, 1)',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                fill: true,
                tension: 0.3,
                pointRadius: 5,
                pointBackgroundColor: 'rgba(59, 130, 246, 1)',
                borderWidth: 2
            },
            {
                label: 'Correct (of 44)',
                data: correctData,
                borderColor: 'rgba(59, 130, 246, 0.4)',
                backgroundColor: 'rgba(59, 130, 246, 0.18)',
                type: 'bar',
                borderWidth: 1,
                borderRadius: 4,
                yAxisID: 'y1'
            },
            {
                label: `Target (${target})`,
                data: labels.map(() => target),
                borderColor: 'rgba(255, 186, 50, 0.6)',
                borderDash: [6, 4],
                borderWidth: 2,
                pointRadius: 0,
                fill: false
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                labels: { color: 'rgba(0, 0, 0, 0.55)', font: { size: 11 } }
            }
        },
        scales: {
            x: {
                ticks: { color: 'rgba(0, 0, 0, 0.4)' },
                grid: { color: 'rgba(0, 0, 0, 0.05)' }
            },
            y: {
                ticks: { color: 'rgba(0, 0, 0, 0.4)' },
                grid: { color: 'rgba(0, 0, 0, 0.05)' },
                min: 550,
                max: 800
            },
            y1: {
                display: false,
                beginAtZero: true,
                max: 44
            }
        }
    }
};

window.renderChart(chartData, this.container);
```

---

## Domain Breakdown — Latest Test (Bluebook Test 11)

```advanced-chart
{
  "type": "bar",
  "data": {
    "labels": ["Algebra", "Advanced Math", "Problem Solving", "Geometry & Trig"],
    "datasets": [{
      "label": "Bluebook Test 11 (%)",
      "data": [93, 86, 88, 75],
      "backgroundColor": ["rgba(255,182,193,0.55)", "rgba(173,216,230,0.55)", "rgba(255,228,181,0.55)", "rgba(178,223,219,0.55)"],
      "borderColor": ["rgba(255,150,170,1)", "rgba(130,190,220,1)", "rgba(240,200,140,1)", "rgba(130,200,195,1)"],
      "borderWidth": 1
    }]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "legend": {
        "labels": { "color": "rgba(0,0,0,0.7)", "font": { "size": 11 } }
      }
    },
    "scales": {
      "y": {
        "beginAtZero": true,
        "max": 100,
        "grid": { "color": "rgba(0,0,0,0.08)" },
        "ticks": { "color": "rgba(0,0,0,0.5)", "stepSize": 10 }
      },
      "x": {
        "grid": { "display": false },
        "ticks": { "color": "rgba(0,0,0,0.5)" }
      }
    }
  }
}
```

---

## Domain Radar

```dataviewjs
const tests = dv.pages('"Scores"')
    .where(p => p.type === "score-entry")
    .sort(p => p.date, 'asc');

const domains = ['Algebra', 'Adv Math', 'PSDA', 'Geometry'];
const keys = ['algebra', 'adv-math', 'psda', 'geometry'];
const totalKeys = ['algebra-total', 'adv-math-total', 'psda-total', 'geometry-total'];

const latest = tests.last();
const prev = tests.length > 1 ? tests[tests.length - 2] : first;

const chartData = {
    type: 'radar',
    data: {
        labels: domains,
        datasets: [
            {
                label: prev.test + ' (%)',
                data: keys.map((k, j) => Math.round(prev[k] / prev[totalKeys[j]] * 100)),
                borderColor: 'rgba(0, 0, 0, 0.2)',
                backgroundColor: 'rgba(0, 0, 0, 0.04)',
                pointBackgroundColor: 'rgba(0, 0, 0, 0.25)',
                borderWidth: 1,
                pointRadius: 3
            },
            {
                label: latest.test + ' (%)',
                data: keys.map((k, j) => Math.round(latest[k] / latest[totalKeys[j]] * 100)),
                borderColor: 'rgba(54, 162, 235, 1)',
                backgroundColor: 'rgba(54, 162, 235, 0.15)',
                pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                pointRadius: 5
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                labels: { color: 'rgba(0, 0, 0, 0.7)', font: { size: 11 } }
            }
        },
        scales: {
            r: {
                min: 0, max: 100,
                ticks: { display: false },
                grid: { color: 'rgba(0, 0, 0, 0.1)' },
                pointLabels: { color: 'rgba(0, 0, 0, 0.7)', font: { size: 12 } },
                angleLines: { color: 'rgba(0, 0, 0, 0.1)' }
            }
        }
    }
};

window.renderChart(chartData, this.container);
```

---

## Feedback & Analysis

### Official SAT — 770 🏆

Score: **770** on the official SAT (March 14, 2026). Range 740–800, 97th percentile.

Full trajectory: 600 → 680 → 660 → 700 → 710 → 750 → 640 (OP1) → 740 (OP2) → 750 (BT10) → 740 (OP3) → 740 (OP4) → 730 (BT11) → **770 (OFFICIAL)** ✅

> Peaked on the day that counted. The two BT11 warning signs (the Geometry dip and the PSDA unit error) did not show up on the real test: every Math domain landed in the 680–800 band. Test-day plan that worked: skip-and-return on hard questions, scratch paper for every sign, Desmos for visual problems, and guess on the last unanswered questions since wrong answers cost nothing.

### Bluebook Test 11 — Final Bluebook at 730

Score: **730** on Bluebook Test 11. Final Bluebook before exam day — exactly at target.

Trajectory over 12 tests: 600 → 680 → 660 → 700 → 710 → 750 → 640 (OP1) → 740 (OP2) → 750 (BT10) → 740 (OP3) → 740 (OP4) → **730 (BT11)** ✅

> Exactly at 730 target. Geometry dropped sharply to 75% (2/4 in Module 2 — 1 wrong + 1 omitted). PSDA had a unit/calculation error (answered 60000, correct was 6). Algebra and Adv Math held steady at 93% and 86%. Module 1 strong at 21/22.

### Domain Status

| Domain | OP4 | BT11 | Change | Priority |
|--------|-----|------|--------|----------|
| Algebra | 88% | **93%** | +5pp | 🟢 RECOVERED — back to 93% |
| Advanced Math | 79% | **86%** | +7pp | 🟢 RECOVERED — back to 86% |
| PSDA | 100% | **88%** | -12pp | 🟡 UNIT ERROR — 60000 vs 6 |
| Geometry & Trig | 100% | **75%** | -25pp | 🔴 BIGGEST DROP — 2/4 in M2 |

### Critical Findings

- 🔴 **Geometry crash (75%)** — worst since BT5 (57%). 1 wrong + 1 omitted in Module 2. Review Geo under time pressure.
- 🟡 **PSDA unit error** — answered 60000 instead of 6. Double-check units and order of magnitude on test day.
- ✅ **Algebra stable at 93%** — recovered from OP4's 88% dip.
- ✅ **Adv Math stable at 86%** — recovered from OP4's 79% dip.
- ✅ **Still at target** — 730 exactly. 8 of last 9 tests ≥ 730.

*Update this analysis manually after each practice test using [[Feedback Analysis]] template.*

![[goten-dbz-1.gif]]

---

## Study Notes

### Algebra (35% of test)
- [[Linear Equations]]
- [[Systems of Linear Equations]]
- [[Linear Inequality]]
- [[Graphs of Linear Systems and Inequalities]]

### Advanced Math (35% of test)
*No notes yet*

### Problem Solving & Data Analysis (15% of test)
*No notes yet*

### Geometry & Trigonometry (15% of test)
- [[Circles]]
- [[Similar and Congruent Triangles]]

---

## Quick Links

| | |
|---|---|
| [[Official SAT — March 2026]] | 🏆 Official result — **770** |
| [[Study Plan]] | 24-day study schedule |
| [[Score Log]] | All practice test scores |
| [[Bluebook Test 11]] | Latest test breakdown (Bluebook Test 11 — 730) |
| [[OnePrep Test 4]] | OnePrep Predicted #4 breakdown (740) |
| [[Bluebook Test 10]] | Previous Bluebook (750) |
| [[OnePrep Test 3]] | OnePrep Predicted #3 breakdown (740) |

---

## Resources

### Tools & Platforms

- [Khan Academy SAT Prep](https://www.khanacademy.org/digital-sat)
- [SAT Suite Question Bank](https://satsuitequestionbank.collegeboard.org/)
- [OnePrep.xyz](https://www.oneprep.xyz/home)
- [Desmos Calculator](https://www.desmos.com/calculator) (built-in on DSAT)
- **CASIO FX-991CW** — personal scientific calculator (SAT-approved) → [[Calculator Practice — FX-991CW]]

![[image-52.png|319]]

### Books & Structured Courses

- [1600.io](https://1600.io/) — SAT Math Orange Book (structured theory + practice, used throughout study plan)

### Worksheets & Problem Sets

- [Problem Sette — DSAT Math Worksheets](https://drive.google.com/drive/folders/1x8YqppXjiGc19lVFg2YGYcjvSrkixqBO) — Tutorllini curated hard problem sets

---

## Video Library

### SAT Math Overview & Fundamentals

- [x] [All of SAT Math Explained in 26 Minutes](https://youtu.be/1bTkbmHx944) — LearnSATMath
- [ ] [EVERYTHING You Need to Know about the Digital SAT](https://youtu.be/06Y6OtRj0n8) — LearnSATMath

### Tips & Strategy

- [ ] [54 SAT Math Tips — DSAT 1](https://youtu.be/oPuJG6AJOlQ) — Hayden Rhodea SAT
- [ ] [54 SAT Math Tips — DSAT 2](https://youtu.be/VGu3mVqnmvg) — Hayden Rhodea SAT
- [ ] [54 SAT Math Tips — DSAT 3](https://youtu.be/F4QhEz2wL4k) — Hayden Rhodea SAT
- [ ] [54 SAT Math Tips — DSAT 4](https://youtu.be/XWwWTqa3y-0) — Hayden Rhodea SAT
- [ ] [Score 800 on SAT Math — 216 Tips (Full Compilation)](https://youtu.be/o9bnJ5hZmbU) — Hayden Rhodea SAT
- [ ] [Why You Run Out of Time on the SAT Math](https://youtu.be/yN_w-wqq14Q) — Risav Roy
- [ ] [Double your speed and accuracy on SAT math](https://youtu.be/Bq6dOiVIdWk) — SAT Prep Askerra

### Desmos Calculator

- [ ] [The only SAT Math DESMOS Guide you'll ever need](https://youtu.be/-pGNBb8M3LQ) — LearnSATMath
- [ ] [DESMOS Guide to an 800 on SAT Math (Fundamentals)](https://youtu.be/2wQqpUnHc7I) — Adiar Math
- [ ] [Solving the HARDEST SAT Math Questions ONLY using Desmos](https://youtu.be/SAIZErXDrK0) — PrepHub

### Domain-Specific

- [ ] [All of SAT Geometry and Trigonometry](https://youtu.be/u6LL3Pbo3HI) — James Lu SAT
- [ ] [How to solve Unit Circle questions on the SAT](https://youtu.be/f315tX5MYYE) — James Lu SAT
- [ ] [All of Percentages on the SAT](https://youtu.be/wThmYHwbOVo) — James Lu SAT
- [ ] [Can You Solve These SAT Triangle Questions?](https://youtu.be/_7TsZCELLYs) — Penguin Test Prep

### Hard Practice Problems

- [ ] [Last-Minute SAT Math Practice — Hard Questions ONLY](https://youtu.be/OQIA9yzffN8) — Penguin Test Prep
- [ ] [EVERYONE Bombs These SAT Math Questions](https://youtu.be/6rZovHC_9dk) — Penguin Test Prep
- [ ] [PART 2 — HARD SAT Math Mix](https://youtu.be/J4PCCTYBqXM) — Penguin Test Prep
- [ ] [5 Hardest SAT MATH Questions — March 2026](https://youtu.be/goPkdMJI6pA) — JZ TEST Prep
- [ ] [Hard Module 2 SAT Math Questions — March 2026](https://youtu.be/ZzfKhKfr-_4) — JZ TEST Prep
- [ ] [10 Must Know SAT MATH Questions — March 2026](https://youtu.be/gc_gUnI9aGs) — JZ TEST Prep
- [ ] [15 hardest SAT math questions EVER!](https://youtu.be/cr5I58p3ah4) — The SATGuy1600
- [ ] [5 Hardest SAT MATH Questions — March 2025](https://youtu.be/BOTqy-OYTxw) — DSAT Hackers
- [ ] [21 Hard SAT Math Problems](https://youtu.be/BIDJEj076jk) — Risav Roy
- [ ] [Very Tricky SAT Math Questions (you need to know)](https://youtu.be/8iAgkHPFoOc) — Risav Roy
- [ ] [4 Hard SAT Problems](https://youtu.be/ibbr9EazEQo) — Risav Roy
- [ ] [The SAT Math Questions Everyone gets Wrong](https://youtu.be/dEoFBES-LW0) — LearnSATMath

### Playlists & Series

- [ ] [Ottocento Course — Digital SAT Math targeting 800](https://www.youtube.com/playlist?list=PLf3ypEs9KobjdZqrdmd1LDtIg0Byzzc9k) — Tutorllini Test Prep
- [ ] [Digital SAT Math Tips (Shorts)](https://www.youtube.com/playlist?list=PLXmJvdMwHZJ-rEx7b-lgZhgnfzKJ_UnLZ) — Hayden Rhodea SAT
- [ ] [SAT Advanced Math](https://www.youtube.com/playlist?list=PLFTlQPGZm2x5GSfjxCdos1jCUIt5xnOgu) — Penguin Test Prep
- [ ] [SAT Problem-Solving and Data Analysis](https://www.youtube.com/playlist?list=PLFTlQPGZm2x6CXnxwxlAH-pIA_s-xv2x3) — Penguin Test Prep
- [ ] [150 Hard SAT Math Questions 2025](https://www.youtube.com/playlist?list=PL38uT-8cAPm34eBgBBfZyel9ptCnKybOh) — Thay Phi
- [ ] [Your SAT Coach — Math Shorts](https://www.youtube.com/@yoursatcoach/shorts) — Your SAT Coach

### Pre-Test Week (watch close to March 14)

- [ ] [How to Use the SAT Desmos Calculator Like a BOSS](https://youtu.be/qoUhn8PBaL8) — Penguin Test Prep
- [ ] [5 Hours of SAT Math Study](https://youtu.be/j1pDk3rBPmc) — Penguin Test Prep
