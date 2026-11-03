---
domain: Geometry and Trigonometry
topic: Circles
status: studied
tags: [geometry, circles, sat-math]
---

# Circles

## 1. Basic Properties

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
  \draw[thick] (0,0) circle (2);
  \filldraw[black] (0,0) circle (1.5pt) node[below right, font=\small] {$O$};
  \draw[thick, red] (-2,0) -- (2,0);
  \node[red, below, font=\small] at (-1,0) {$d$};
  \draw[thick, blue, ->] (0,0) -- (1.414,1.414);
  \node[blue, above left, font=\small] at (0.85,0.85) {$r$};
\end{tikzpicture}
\end{document}
```

$$A = \pi r^2 \qquad C = 2\pi r = \pi d$$

| Property | Formula | Relationship |
|----------|---------|-------------|
| Radius | $r$ | Half the diameter |
| Diameter | $d = 2r$ | Longest chord |
| Area | $A = \pi r^2$ | Space inside |
| Circumference | $C = 2\pi r$ | Perimeter of circle |

> On the SAT, you'll almost always need to extract $r$ from a given diameter, area, or circumference before solving.

---

## 2. Arcs and Sectors

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
  \draw[thick] (0,0) circle (2);
  \filldraw[black] (0,0) circle (1.5pt);
  \draw[thick] (0,0) -- (2,0);
  \draw[thick] (0,0) -- ({2*cos(50)},{2*sin(50)});
  \draw[thick, green!60!black] ({2*cos(50)},{2*sin(50)}) arc (50:0:2);
  \node[green!60!black, right, font=\small] at ({2.1*cos(25)},{2.1*sin(25)}) {$s$};
  \node[font=\small] at (0.7,0.15) {$\theta$};
  \node[font=\small] at (0.85,0.55) {$r$};
  \draw[thick, ->] (0.5,0) arc (0:50:0.5);
  \fill[gray!20] (0,0) -- (2,0) arc (0:50:2) -- cycle;
  \draw[thick] (0,0) circle (2);
  \draw[thick] (0,0) -- (2,0);
  \draw[thick] (0,0) -- ({2*cos(50)},{2*sin(50)});
  \draw[thick, green!60!black] ({2*cos(50)},{2*sin(50)}) arc (50:0:2);
\end{tikzpicture}
\end{document}
```

**Arc length** (portion of circumference):
$$s = r\theta \qquad \text{(\(\theta\) in radians)}$$

**Sector area** (pizza slice):
$$A = \frac{1}{2}r^2\theta \qquad \text{(\(\theta\) in radians)}$$

**Using degrees instead:**
$$s = \frac{\theta}{360} \cdot 2\pi r \qquad A = \frac{\theta}{360} \cdot \pi r^2$$

### Degree ↔ Radian Conversion

$$\text{Radians} = \text{Degrees} \times \frac{\pi}{180} \qquad \text{Degrees} = \text{Radians} \times \frac{180}{\pi}$$

| Degrees | Radians |
|---------|---------|
| $30°$ | $\frac{\pi}{6}$ |
| $45°$ | $\frac{\pi}{4}$ |
| $60°$ | $\frac{\pi}{3}$ |
| $90°$ | $\frac{\pi}{2}$ |
| $180°$ | $\pi$ |
| $360°$ | $2\pi$ |

---

## 3. Equation of a Circle (Coordinate Geometry)

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.7]
  \draw[very thin, gray!30] (-4,-4) grid (6,6);
  \draw[thick,->] (-4.5,0) -- (6.5,0) node[right] {$x$};
  \draw[thick,->] (0,-4.5) -- (0,6.5) node[above] {$y$};
  \foreach \x in {-4,-3,-2,-1,1,2,3,4,5,6}
    \draw (\x,0.1) -- (\x,-0.1) node[below,font=\tiny] {$\x$};
  \foreach \y in {-4,-3,-2,-1,1,2,3,4,5,6}
    \draw (0.1,\y) -- (-0.1,\y) node[left,font=\tiny] {$\y$};
  \draw[thick, blue] (2,2) circle (2.5);
  \filldraw[black] (2,2) circle (2pt) node[below left, font=\small] {$(h,k)$};
  \draw[dashed, thick] (2,2) -- (4.2,3.5);
  \node[font=\small, above left] at (3.1,2.8) {$r$};
  \filldraw[blue] (4.2,3.5) circle (2pt) node[right, font=\small] {$(x,y)$};
\end{tikzpicture}
\end{document}
```

### Standard Form

$$(x - h)^2 + (y - k)^2 = r^2$$

- Center: $(h,k)$
- Radius: $r$

> Watch the signs: $(x - 3)^2 + (y + 2)^2 = 16$ → center $(3, -2)$, radius $4$.

### General (Expanded) Form

$$x^2 + y^2 + Dx + Ey + F = 0$$

**To convert to standard form → complete the square:**

**Example:** $x^2 + y^2 - 6x + 4y - 12 = 0$

$$\begin{aligned}
(x^2 - 6x) + (y^2 + 4y) &= 12 \\
(x^2 - 6x + 9) + (y^2 + 4y + 4) &= 12 + 9 + 4 \\
(x - 3)^2 + (y + 2)^2 &= 25
\end{aligned}$$

Center: $(3, -2)$, Radius: $5$

### Finding Center and Radius from General Form (Quick Formula)

Given $x^2 + y^2 + Dx + Ey + F = 0$:

$$\text{Center} = \left(-\frac{D}{2},\, -\frac{E}{2}\right) \qquad r = \sqrt{\frac{D^2}{4} + \frac{E^2}{4} - F}$$

---

## 4. Lines and Chords

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
  \draw[thick] (0,0) circle (2);
  \filldraw[black] (0,0) circle (1.5pt);
  % Tangent point
  \filldraw[black] (2,0) circle (1.5pt) node[below left, font=\small] {$P$};
  % Radius to tangent point
  \draw[dashed, thick] (0,0) -- (2,0);
  \node[font=\small, above] at (1,0.1) {$r$};
  % Tangent line
  \draw[thick, orange] (2,-2) -- (2,2);
  \node[orange, right, font=\small] at (2,1.5) {Tangent};
  % Right angle mark
  \draw[thick] (1.75,0) -- (1.75,0.25) -- (2,0.25);
  % Chord
  \draw[thick, blue] (-1.5,{sqrt(4-2.25)}) -- (1.5,{sqrt(4-2.25)});
  \node[blue, above, font=\small] at (0,{sqrt(4-2.25)+0.1}) {Chord};
\end{tikzpicture}
\end{document}
```

### Tangent Lines

A **tangent** touches the circle at exactly one point.

$$\text{Radius} \perp \text{Tangent at the point of tangency}$$

This creates a right angle → use the **Pythagorean theorem** to find unknown lengths.

### Chords

A **chord** is a segment connecting two points on the circle. The diameter is the longest chord.

**Key properties:**
- A radius perpendicular to a chord **bisects** the chord
- Equal chords are equidistant from the center
- The perpendicular from the center to a chord bisects the chord

---

## 5. Inscribed Angles and Central Angles

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]
  \draw[thick] (0,0) circle (2);
  \filldraw[black] (0,0) circle (1.5pt) node[below, font=\small] {$O$};
  % Central angle
  \draw[thick, red] (0,0) -- (2,0);
  \draw[thick, red] (0,0) -- ({2*cos(80)},{2*sin(80)});
  \draw[red, thick, ->] (0.6,0) arc (0:80:0.6);
  \node[red, font=\small] at (0.45,0.55) {$2\alpha$};
  % Inscribed angle
  \filldraw[blue] ({2*cos(200)},{2*sin(200)}) circle (1.5pt) node[left, font=\small] {$A$};
  \draw[thick, blue] ({2*cos(200)},{2*sin(200)}) -- (2,0);
  \draw[thick, blue] ({2*cos(200)},{2*sin(200)}) -- ({2*cos(80)},{2*sin(80)});
  \draw[blue, thick, ->] ({2*cos(200)+0.45*cos(15)},{2*sin(200)+0.45*sin(15)}) arc (15:55:0.45);
  \node[blue, font=\small] at ({2*cos(200)+0.65*cos(35)},{2*sin(200)+0.65*sin(35)}) {$\alpha$};
  % Arc points
  \filldraw[black] (2,0) circle (1.5pt) node[right, font=\small] {$B$};
  \filldraw[black] ({2*cos(80)},{2*sin(80)}) circle (1.5pt) node[above right, font=\small] {$C$};
\end{tikzpicture}
\end{document}
```

### Inscribed Angle Theorem

$$\text{Inscribed angle} = \frac{1}{2} \times \text{Central angle}$$

Both angles intercept the same arc.

### Special Cases

| Configuration | Result |
|--------------|--------|
| Inscribed angle on a semicircle | Always $90°$ |
| Two inscribed angles on the same arc | They are equal |
| Central angle | Equals the intercepted arc |

---

## 6. Intersecting Chords, Secants, and Tangents

### Two Chords Intersecting Inside

$$PA \cdot PB = PC \cdot PD$$

### Two Secants from External Point

$$PA \cdot PB = PC \cdot PD$$

(where $PA$ and $PB$ are the near and far intersections of one secant, and $PC$, $PD$ for the other)

### Tangent-Secant from External Point

$$(\text{tangent})^2 = (\text{near}) \times (\text{far})$$

$$PT^2 = PA \cdot PB$$

---

## SAT Tips

1. **Always identify $r$ first** — most problems give you diameter, area, or circumference and expect you to work with the radius
2. **Completing the square** appears frequently — practice converting general form to standard form quickly
3. **Tangent = right angle** — when you see a tangent line, set up Pythagorean theorem
4. **Arc/sector as a fraction** — think of it as $\frac{\theta}{360}$ (degrees) or $\frac{\theta}{2\pi}$ (radians) of the full circle
5. **Inscribed angle in semicircle = 90°** — this shortcut appears on nearly every SAT
6. **On Desmos** — type $(x-h)^2 + (y-k)^2 = r^2$ to graph a circle and visually verify intersections or tangent points
7. **Coordinate problems** — if asked for a point on the circle, substitute into the equation and solve; if two points, use distance formula for the diameter
