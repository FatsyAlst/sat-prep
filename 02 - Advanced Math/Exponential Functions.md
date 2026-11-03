---
domain: Advanced Math
topic: Exponential Functions
chapter: 1600.io Chapter 14
status: studied
tags: [advanced-math, exponential, growth, decay, sat-math]
---

# Exponential Functions

## The Standard Form

$$y = a \cdot b^x$$

| Parameter | Meaning |
|---|---|
| $a$ | Initial value ($y$-intercept: plug in $x = 0$) |
| $b$ | Growth/decay factor (multiplied each interval) |
| $x$ | Number of intervals |

- $b > 1$ → **growth**
- $0 < b < 1$ → **decay**
- $b = 1$ → constant (not exponential)

To find $b$ from a table: $b = \dfrac{y(x+1)}{y(x)}$ — divide consecutive values.

---

## Growth vs. Decay

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  width=11cm, height=7cm,
  axis lines=center,
  xlabel={$x$}, ylabel={$y$},
  xmin=-3, xmax=3, ymin=-0.5, ymax=9,
  xtick={-3,-2,-1,0,1,2,3},
  ytick={0,2,4,6,8},
  grid=both, grid style={line width=0.3pt, draw=black!10},
  tick label style={font=\footnotesize},
  legend style={at={(0.98,0.5)}, anchor=east, font=\footnotesize},
  clip=false,
]
\addplot[very thick, blue, domain=-3:2.1, samples=100] {2^x};
\addplot[very thick, red, domain=-2.1:3, samples=100] {2^(-x)};
\addplot[mark=*, mark size=3pt, green!60!black] coordinates {(0,1)};
\node[green!60!black, font=\footnotesize\bfseries, above right] at (axis cs:0.1,1) {$a=1$};
\legend{$y=2^x$ (growth), $y=2^{-x}$ (decay)}
\end{axis}
\end{tikzpicture}
\end{document}
```

---

## Unit Conversion for Exponents

When the model is written in one unit (e.g. years) but the problem gives another (e.g. quarters), **use a proportion** to rewrite the exponent.

**Method:**
$$\frac{\text{new variable}}{\text{conversion factor}} = \frac{\text{original variable}}{1}$$

**Example — doubling every year, rewrite in quarters ($q$, where 4 quarters = 1 year):**

$$y = a \cdot 2^t \quad\xrightarrow{\;q = 4t\;}\quad y = a \cdot 2^{q/4}$$

**Sanity check:** substitute one full original interval into the new exponent and verify it equals 1. Here: $q = 4 \Rightarrow$ exponent $= 4/4 = 1$ ✓

> [!warning] The SAT sometimes gives a wrong exponent that also passes this check. For example, $\frac{4}{q}$ also gives $\frac{4}{4} = 1$ when $q=4$ — but it's wrong because it implies $q$ increases → exponent decreases, which is backwards. Always verify the direction too.

---

## Solving Exponential Equations

**No logarithms needed.** Isolate the exponential term, then raise both sides to the **reciprocal of the power**:

$$\left(x^n\right)^{1/n} = x$$

**Example:**
$$3x^5 = 96 \implies x^5 = 32 \implies x = 32^{1/5} = 2$$

---

## Graph Shapes of $y = ab^{cx}$

### Sign of $a$
- $a > 0$ → graph **above** $x$-axis
- $a < 0$ → graph **below** $x$-axis (mirror image)

### Growth direction (sign of $c$)

| Condition | Behaviour |
|---|---|
| $b \geq 1$, $c > 0$ **or** $0 < b < 1$, $c < 0$ | Slow on left, fast on right (→ growth) |
| $b \geq 1$, $c < 0$ **or** $0 < b < 1$, $c > 0$ | Fast on left, slow on right (→ decay) |

### Four canonical shapes

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  name=p1,
  width=6cm, height=5cm,
  axis lines=center,
  xmin=-3, xmax=3, ymin=-1, ymax=9,
  xtick={-2,0,2}, ytick={0,4,8},
  tick label style={font=\tiny},
  grid=both, grid style={line width=0.3pt, draw=black!10},
  title={\small $y=2(2)^x$, $a>0$},
  title style={at={(0.5,1.06)}},
  clip=false,
]
\addplot[very thick, blue, domain=-3:2.05, samples=100] {2*2^x};
\end{axis}

\begin{axis}[
  name=p2,
  at={(6.5cm,0)},
  width=6cm, height=5cm,
  axis lines=center,
  xmin=-3, xmax=3, ymin=-9, ymax=1,
  xtick={-2,0,2}, ytick={-8,-4,0},
  tick label style={font=\tiny},
  grid=both, grid style={line width=0.3pt, draw=black!10},
  title={\small $y=-2(2)^x$, $a<0$},
  title style={at={(0.5,1.06)}},
  clip=false,
]
\addplot[very thick, red, domain=-3:2.05, samples=100] {-2*2^x};
\end{axis}

\begin{axis}[
  name=p3,
  at={(0,-5.5cm)},
  width=6cm, height=5cm,
  axis lines=center,
  xmin=-3, xmax=3, ymin=-1, ymax=9,
  xtick={-2,0,2}, ytick={0,4,8},
  tick label style={font=\tiny},
  grid=both, grid style={line width=0.3pt, draw=black!10},
  title={\small $y=2(2)^{-x}$, decay $a>0$},
  title style={at={(0.5,1.06)}},
  clip=false,
]
\addplot[very thick, teal, domain=-2.05:3, samples=100] {2*2^(-x)};
\end{axis}

\begin{axis}[
  name=p4,
  at={(6.5cm,-5.5cm)},
  width=6cm, height=5cm,
  axis lines=center,
  xmin=-3, xmax=3, ymin=-9, ymax=1,
  xtick={-2,0,2}, ytick={-8,-4,0},
  tick label style={font=\tiny},
  grid=both, grid style={line width=0.3pt, draw=black!10},
  title={\small $y=-2(2)^{-x}$, decay $a<0$},
  title style={at={(0.5,1.06)}},
  clip=false,
]
\addplot[very thick, violet, domain=-2.05:3, samples=100] {-2*2^(-x)};
\end{axis}
\end{tikzpicture}
\end{document}
```

---

## SAT Quick-Read Checklist

When you see an exponential function:

1. **$y$-intercept** → read $a$ directly (set $x = 0$)
2. **Growth or decay?** → check sign of $c$ and whether $b > 1$ or $b < 1$
3. **Unit mismatch?** → set up a proportion to convert the exponent before extracting any rate
4. **Solve for $x$?** → isolate the exponential term, raise to reciprocal power — no logs needed
