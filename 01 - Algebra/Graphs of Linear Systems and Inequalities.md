---
domain: Algebra
topic: Graphs of Linear Systems and Inequalities
status: studied
tags: [algebra, graphing, systems, inequalities, sat-math]
---

# Graphs of Linear Systems and Inequalities

## Graphing a Line

### From Slope-Intercept Form ($y = mx + b$)
1. Plot the y-intercept $(0, b)$
2. From there, use slope $m = \frac{\text{rise}}{\text{run}}$ to find a second point
3. Draw the line through both points

### From Standard Form ($Ax + By = C$)
1. Find x-intercept: set $y = 0 \implies x = C/A$ → point $(C/A, 0)$
2. Find y-intercept: set $x = 0 \implies y = C/B$ → point $(0, C/B)$
3. Draw the line through both intercepts

### Example: $y = \frac{2}{3}x - 1$

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.7]
  \draw[very thin, gray!30] (-4,-4) grid (4,4);
  \draw[thick,->] (-4.5,0) -- (4.5,0) node[right] {$x$};
  \draw[thick,->] (0,-4.5) -- (0,4.5) node[above] {$y$};
  \foreach \x in {-4,-3,-2,-1,1,2,3,4}
    \draw (\x,0.1) -- (\x,-0.1) node[below,font=\tiny] {$\x$};
  \foreach \y in {-4,-3,-2,-1,1,2,3,4}
    \draw (0.1,\y) -- (-0.1,\y) node[left,font=\tiny] {$\y$};
  \clip (-4,-4) rectangle (4,4);
  \draw[thick, blue, domain=-4:4, samples=50] plot (\x, {2/3*\x - 1});
  \filldraw[blue] (0,-1) circle (3pt) node[below right, font=\small] {$(0,-1)$};
  \filldraw[blue] (3,1) circle (3pt) node[above left, font=\small] {$(3,1)$};
  \node[blue, font=\small] at (2.5, 3) {$y = \frac{2}{3}x - 1$};
\end{tikzpicture}
\end{document}
```

---

## Reading Slope from a Graph

Given two visible points $(x_1, y_1)$ and $(x_2, y_2)$:
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

**Visual clues:**
- Steeper line = larger $|m|$
- Flatter line = smaller $|m|$
- Horizontal = $m = 0$, Vertical = undefined

---

## Graphing Systems of Equations

The **solution** of a system is the **intersection point** of the two lines.

### Example: $y = x + 1$ and $y = -x + 3$

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.7]
  \draw[very thin, gray!30] (-2,-2) grid (5,5);
  \draw[thick,->] (-2.5,0) -- (5.5,0) node[right] {$x$};
  \draw[thick,->] (0,-2.5) -- (0,5.5) node[above] {$y$};
  \foreach \x in {-2,-1,1,2,3,4,5}
    \draw (\x,0.1) -- (\x,-0.1) node[below,font=\tiny] {$\x$};
  \foreach \y in {-2,-1,1,2,3,4,5}
    \draw (0.1,\y) -- (-0.1,\y) node[left,font=\tiny] {$\y$};
  \clip (-2,-2) rectangle (5,5);
  \draw[thick, blue, domain=-2:4, samples=50] plot (\x, {\x + 1});
  \draw[thick, red, domain=-1:5, samples=50] plot (\x, {-\x + 3});
  \filldraw[black] (1,2) circle (3pt);
  \node[above right, font=\small] at (1,2) {$(1, 2)$};
  \node[blue, font=\small] at (-1.2, 0.5) {$y = x + 1$};
  \node[red, font=\small] at (4.2, -0.5) {$y = -x + 3$};
\end{tikzpicture}
\end{document}
```

Solution: $(1, 2)$ — where the lines cross.

### Visual Interpretation of Number of Solutions

| Graph | Solutions |
|-------|-----------|
| Lines cross at one point | **One solution** |
| Lines are parallel (never cross) | **No solution** |
| Lines overlap completely | **Infinitely many** |

---

## Graphing Linear Inequalities

### Steps
1. Graph the boundary line ($=$ version of the inequality)
2. Choose line style: **dashed** ($<$, $>$) or **solid** ($\leq$, $\geq$)
3. Shade the correct side: test a point (usually $(0,0)$)

### Example: $y \leq -x + 2$

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.7]
  \draw[very thin, gray!30] (-3,-3) grid (5,5);
  % Shaded region: below the line y = -x + 2
  \fill[blue!15] (-3,5) -- (5,-3) -- (-3,-3) -- cycle;
  \draw[thick,->] (-3.5,0) -- (5.5,0) node[right] {$x$};
  \draw[thick,->] (0,-3.5) -- (0,5.5) node[above] {$y$};
  \foreach \x in {-3,-2,-1,1,2,3,4,5}
    \draw (\x,0.1) -- (\x,-0.1) node[below,font=\tiny] {$\x$};
  \foreach \y in {-3,-2,-1,1,2,3,4,5}
    \draw (0.1,\y) -- (-0.1,\y) node[left,font=\tiny] {$\y$};
  \draw[thick, blue] (-3,5) -- (5,-3);
  \node[blue, font=\small] at (4, -1) {$y \leq -x + 2$};
  \node[blue!50, font=\footnotesize, rotate=-45] at (0.5, -1.5) {\textit{shaded region}};
\end{tikzpicture}
\end{document}
```

- **Solid line** because $\leq$ (boundary is included)
- **Shaded below** because $y \leq$
- Test $(0,0)$: $0 \leq -0 + 2 = 2$ ✓ → $(0,0)$ is in the shaded region

### Quick Rule for $y$ Isolated

| Inequality | Shade |
|------------|-------|
| $y > mx + b$ or $y \geq mx + b$ | **Above** the line |
| $y < mx + b$ or $y \leq mx + b$ | **Below** the line |

---

## Systems of Linear Inequalities

The solution is the **overlapping shaded region** (feasible region) of all inequalities.

### Example: $y > x - 1$ AND $y \leq -2x + 4$

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.7]
  \draw[very thin, gray!30] (-3,-3) grid (5,5);
  % Feasible region: above y = x-1 AND below y = -2x+4
  % Vertices: blue line at bottom edge (-2,-3), intersection (5/3, 2/3),
  %           red line at top edge (-0.5, 5), then window corners
  \fill[green!20] (-2,-3) -- (5/3, 2/3) -- (-0.5, 5) -- (-3, 5) -- (-3, -3) -- cycle;
  \draw[thick,->] (-3.5,0) -- (5.5,0) node[right] {$x$};
  \draw[thick,->] (0,-3.5) -- (0,5.5) node[above] {$y$};
  \foreach \x in {-3,-2,-1,1,2,3,4,5}
    \draw (\x,0.1) -- (\x,-0.1) node[below,font=\tiny] {$\x$};
  \foreach \y in {-3,-2,-1,1,2,3,4,5}
    \draw (0.1,\y) -- (-0.1,\y) node[left,font=\tiny] {$\y$};
  % Boundary lines
  \draw[thick, blue, dashed, domain=-2:4.5, samples=50] plot (\x, {\x - 1});
  \draw[thick, red, domain=-0.5:3.5, samples=50] plot (\x, {-2*\x + 4});
  % Labels
  \node[blue, font=\small] at (4.2, 3.8) {$y > x - 1$};
  \node[red, font=\small] at (3.5, 4.8) {$y \leq -2x + 4$};
  % Intersection point
  \filldraw[black] (5/3, 2/3) circle (2.5pt);
  \node[font=\small, right] at (2, 0.3) {$\left(\frac{5}{3}, \frac{2}{3}\right)$};
\end{tikzpicture}
\end{document}
```

To find the intersection point of the boundary lines:
$$x - 1 = -2x + 4 \implies 3x = 5 \implies x = \frac{5}{3}, \quad y = \frac{2}{3}$$

---

## SAT Strategies for Graph Questions

1. **"Which point is in the solution set?"** — plug each answer choice into ALL inequalities; it must satisfy every one
2. **"Which graph represents the system?"** — check line styles (solid/dashed), slopes, and shading direction
3. **"How many solutions does the system have?"** — count intersection points visually, or compare slopes
4. **Reading solutions from graphs** — the coordinates of the intersection point ARE the solution
5. **Estimating from graphs** — the SAT sometimes shows a graph and asks for approximate values; read carefully from the axes
6. **Boundary cases** — a point ON a dashed line is NOT in the solution set; on a solid line, it IS

---

## Key Formulas Reference

| Task | Formula |
|------|---------|
| Slope between two points | $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| x-intercept | Set $y = 0$, solve for $x$ |
| y-intercept | Set $x = 0$, solve for $y$ |
| Midpoint | $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ |
| Distance | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
