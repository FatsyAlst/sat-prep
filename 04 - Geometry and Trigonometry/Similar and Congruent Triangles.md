---
domain: Geometry and Trigonometry
topic: Similar and Congruent Triangles
status: studied
tags: [geometry, triangles, similarity, congruence, sat-math]
---

# Similar and Congruent Triangles

## 1. Congruent Triangles

Two triangles are **congruent** ($\cong$) when they have the **exact same shape and size** — all three pairs of corresponding sides are equal, and all three pairs of corresponding angles are equal.

$$\triangle ABC \cong \triangle DEF \implies \begin{cases} AB = DE,\; BC = EF,\; AC = DF \\ \angle A = \angle D,\; \angle B = \angle E,\; \angle C = \angle F \end{cases}$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.1]
  % Triangle ABC
  \coordinate (A) at (0,0);
  \coordinate (B) at (3,0);
  \coordinate (C) at (1,2.2);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \node[below left, font=\small] at (A) {$A$};
  \node[below right, font=\small] at (B) {$B$};
  \node[above, font=\small] at (C) {$C$};
  % Side labels
  \node[below, font=\small, blue] at (1.5,0) {$5$};
  \node[right, font=\small, red] at (2.1,1.1) {$4$};
  \node[left, font=\small, green!60!black] at (0.4,1.1) {$3$};
  % Tick marks — AB (double)
  \draw[thick] (1.4,-0.15) -- (1.4,0.15);
  \draw[thick] (1.6,-0.15) -- (1.6,0.15);
  % Tick marks — BC (single)
  \draw[thick] (2.05,1.2) -- (1.85,1.0);
  % Tick marks — AC (triple)
  \draw[thick] (0.4,0.95) -- (0.6,1.15);
  \draw[thick] (0.45,1.05) -- (0.65,1.25);
  \draw[thick] (0.5,1.15) -- (0.7,1.35);
  % Angle arcs
  \draw[thick, red] (0.4,0) arc (0:65:0.4);
  \draw[thick, blue] (2.6,0) arc (180:118:0.4);
  \draw[thick, green!60!black] (0.84,1.88) arc (245:310:0.35);

  % Triangle DEF (identical, shifted right)
  \coordinate (D) at (5,0);
  \coordinate (E) at (8,0);
  \coordinate (F) at (6,2.2);
  \draw[thick] (D) -- (E) -- (F) -- cycle;
  \node[below left, font=\small] at (D) {$D$};
  \node[below right, font=\small] at (E) {$E$};
  \node[above, font=\small] at (F) {$F$};
  % Side labels
  \node[below, font=\small, blue] at (6.5,0) {$5$};
  \node[right, font=\small, red] at (7.1,1.1) {$4$};
  \node[left, font=\small, green!60!black] at (5.4,1.1) {$3$};
  % Tick marks — DE (double)
  \draw[thick] (6.4,-0.15) -- (6.4,0.15);
  \draw[thick] (6.6,-0.15) -- (6.6,0.15);
  % Tick marks — EF (single)
  \draw[thick] (7.05,1.2) -- (6.85,1.0);
  % Tick marks — DF (triple)
  \draw[thick] (5.4,0.95) -- (5.6,1.15);
  \draw[thick] (5.45,1.05) -- (5.65,1.25);
  \draw[thick] (5.5,1.15) -- (5.7,1.35);
  % Angle arcs
  \draw[thick, red] (5.4,0) arc (0:65:0.4);
  \draw[thick, blue] (7.6,0) arc (180:118:0.4);
  \draw[thick, green!60!black] (5.84,1.88) arc (245:310:0.35);

  % Congruence label
  \node[font=\large] at (4,1) {$\cong$};
\end{tikzpicture}
\end{document}
```

### Congruence Tests (How to Prove It)

You do **NOT** need to verify all 6 pairs. Any one of these shortcuts is sufficient:

| Test | What You Need | Diagram Hint |
|------|---------------|-------------|
| **SSS** | All 3 pairs of sides equal | Three pairs of tick marks |
| **SAS** | 2 sides + the angle **between** them | Angle must be the included angle |
| **ASA** | 2 angles + the side **between** them | Side must connect the two known angles |
| **AAS** | 2 angles + any side | Since 2 angles fix the third, one side determines size |
| **HL** | Hypotenuse + one leg (right triangles only) | Must have a right angle |

> [!warning] Invalid tests — these do **NOT** prove congruence
> - **AAA** — proves similarity, not congruence (same shape, but could be different sizes)
> - **SSA** (or ASS) — ambiguous case; two different triangles can have the same SSA

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % --- SAS Example ---
  \node[font=\bfseries\small] at (1.5,3) {SAS};
  \coordinate (A1) at (0,0);
  \coordinate (B1) at (3,0);
  \coordinate (C1) at (1.2,2.2);
  \draw[thick] (A1) -- (B1) -- (C1) -- cycle;
  % Highlight the two sides and included angle
  \draw[very thick, blue] (A1) -- (B1);
  \draw[very thick, blue] (A1) -- (C1);
  \draw[thick, red, ->] (0.5,0) arc (0:61:0.5);
  \node[red, font=\small] at (0.55,0.35) {$\theta$};
  \node[below, font=\small, blue] at (1.5,0) {$a$};
  \node[left, font=\small, blue] at (0.5,1.1) {$b$};
  \node[font=\footnotesize, gray] at (1.5,-0.5) {Included angle};

  % --- ASA Example ---
  \node[font=\bfseries\small] at (6.5,3) {ASA};
  \coordinate (A2) at (5,0);
  \coordinate (B2) at (8,0);
  \coordinate (C2) at (6.2,2.2);
  \draw[thick] (A2) -- (B2) -- (C2) -- cycle;
  % Highlight the two angles and included side
  \draw[very thick, blue] (A2) -- (B2);
  \draw[thick, red, ->] (5.5,0) arc (0:61:0.5);
  \draw[thick, red, ->] (7.55,0) arc (180:130:0.45);
  \node[red, font=\small] at (5.55,0.35) {$\alpha$};
  \node[red, font=\small] at (7.45,0.3) {$\beta$};
  \node[below, font=\small, blue] at (6.5,0) {$c$};
  \node[font=\footnotesize, gray] at (6.5,-0.5) {Included side};

  % --- HL Example ---
  \node[font=\bfseries\small] at (11.5,3) {HL};
  \coordinate (A3) at (10,0);
  \coordinate (B3) at (13,0);
  \coordinate (C3) at (10,2);
  \draw[thick] (A3) -- (B3) -- (C3) -- cycle;
  % Right angle mark
  \draw[thick] (10,0.3) -- (10.3,0.3) -- (10.3,0);
  % Highlight hypotenuse and leg
  \draw[very thick, red] (B3) -- (C3);
  \draw[very thick, blue] (A3) -- (C3);
  \node[right, font=\small, red] at (11.7,1.1) {Hyp};
  \node[left, font=\small, blue] at (10,1) {Leg};
  \node[font=\footnotesize, gray] at (11.5,-0.5) {Right triangle only};
\end{tikzpicture}
\end{document}
```

---

## 2. Similar Triangles

Two triangles are **similar** ($\sim$) when they have the **same shape but possibly different sizes** — all corresponding angles are equal, and all corresponding sides are in the same ratio (the **scale factor**).

$$\triangle ABC \sim \triangle DEF \implies \begin{cases} \angle A = \angle D,\; \angle B = \angle E,\; \angle C = \angle F \\[6pt] \dfrac{AB}{DE} = \dfrac{BC}{EF} = \dfrac{AC}{DF} = k \end{cases}$$

where $k$ is the **scale factor**.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % Small triangle
  \coordinate (A) at (0,0);
  \coordinate (B) at (3,0);
  \coordinate (C) at (0.8,2);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \node[below left, font=\small] at (A) {$A$};
  \node[below right, font=\small] at (B) {$B$};
  \node[above, font=\small] at (C) {$C$};
  \node[below, font=\small, blue] at (1.5,0) {$3$};
  \node[right, font=\small, red] at (2.0,1.1) {$4$};
  \node[left, font=\small, green!60!black] at (0.3,1) {$2$};
  % Angle arcs
  \draw[thick, orange] (0.4,0) arc (0:68:0.4);
  \draw[thick, purple] (2.6,0) arc (180:127:0.4);

  % Arrow
  \node[font=\Large] at (4.2,1) {$\sim$};
  \node[font=\small, gray] at (4.2,0.4) {$k = 2$};

  % Large triangle (scaled by 2)
  \coordinate (D) at (5.5,0);
  \coordinate (E) at (11.5,0);
  \coordinate (F) at (7.1,4);
  \draw[thick] (D) -- (E) -- (F) -- cycle;
  \node[below left, font=\small] at (D) {$D$};
  \node[below right, font=\small] at (E) {$E$};
  \node[above, font=\small] at (F) {$F$};
  \node[below, font=\small, blue] at (8.5,0) {$6$};
  \node[right, font=\small, red] at (9.5,2.1) {$8$};
  \node[left, font=\small, green!60!black] at (6.1,2) {$4$};
  % Angle arcs
  \draw[thick, orange] (6.0,0) arc (0:68:0.5);
  \draw[thick, purple] (11.0,0) arc (180:127:0.5);
\end{tikzpicture}
\end{document}
```

$$\frac{3}{6} = \frac{4}{8} = \frac{2}{4} = \frac{1}{2} \qquad \text{(scale factor } k = 2\text{)}$$

### Similarity Tests (How to Prove It)

| Test | What You Need | How Often on SAT |
|------|---------------|------------------|
| **AA** | 2 pairs of equal angles | **Very common** — this is the main one |
| **SSS~** | All 3 pairs of sides proportional | Rare |
| **SAS~** | 2 pairs of sides proportional + included angle equal | Occasional |

> [!tip] Why AA is enough
> Since the angles of any triangle sum to $180°$, knowing 2 angles automatically determines the third. So **AA = AAA**, and that's all you need for similarity.

---

## 3. Setting Up Proportions

Once you establish similarity, the key skill is setting up the proportion **correctly**. The SAT tests this directly.

### The Rule

> [!important] Corresponding sides are opposite corresponding angles
> If $\triangle ABC \sim \triangle DEF$, then the side opposite $\angle A$ corresponds to the side opposite $\angle D$, and so on.

$$\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}$$

### Worked Example

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % Triangle 1
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (1,2.5);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \node[below left, font=\small] at (A) {$A$};
  \node[below right, font=\small] at (B) {$B$};
  \node[above, font=\small] at (C) {$C$};
  \node[below, font=\small] at (2,0) {$8$};
  \node[left, font=\small] at (0.4,1.25) {$5$};
  \node[right, font=\small] at (2.7,1.35) {$?$};

  % Triangle 2
  \coordinate (D) at (6,0);
  \coordinate (E) at (9,0);
  \coordinate (F) at (6.75,1.875);
  \draw[thick] (D) -- (E) -- (F) -- cycle;
  \node[below left, font=\small] at (D) {$D$};
  \node[below right, font=\small] at (E) {$E$};
  \node[above, font=\small] at (F) {$F$};
  \node[below, font=\small] at (7.5,0) {$6$};
  \node[left, font=\small] at (6.3,0.95) {$x$};
  \node[right, font=\small] at (8.0,1.0) {$?$};

  % Similarity label
  \node[font=\small] at (5,1.2) {$\sim$};
  
  % Angle marks to show correspondence
  \draw[thick, red] (0.4,0) arc (0:68:0.4);
  \draw[thick, red] (6.4,0) arc (0:68:0.4);
  \draw[thick, blue] (3.55,0) arc (180:140:0.45);
  \draw[thick, blue] (8.6,0) arc (180:140:0.4);
\end{tikzpicture}
\end{document}
```

**Given:** $\triangle ABC \sim \triangle DEF$, $AB = 8$, $AC = 5$, $DE = 6$. Find $DF$.

$$\frac{AB}{DE} = \frac{AC}{DF}$$

$$\frac{8}{6} = \frac{5}{x}$$

$$8x = 30 \implies x = \frac{30}{8} = 3.75$$

> [!warning] Common mistake — mismatching sides
> Make sure you pair sides from the **same triangle** in each fraction. A proportion like $\frac{AB}{AC} = \frac{DE}{DF}$ (ratio within each triangle) also works. But **never** mix sides from different triangles in one fraction like $\frac{AB}{EF} = \frac{AC}{DE}$.

---

## 4. Key Properties to Remember

### Similar Triangles — Ratios

If the scale factor between two similar triangles is $k$, then:

| Quantity | Ratio |
|----------|-------|
| Corresponding sides | $k$ |
| Corresponding perimeters | $k$ |
| Corresponding areas | $k^2$ |

**Example:** If two similar triangles have sides in ratio $1:3$, their areas are in ratio $1:9$.

### Angle Sum Property

$$\angle A + \angle B + \angle C = 180°$$

If you know two angles, you know the third. This is why **AA is sufficient** for similarity — knowing two angles determines the entire shape.

### Exterior Angle Theorem

$$\text{Exterior angle} = \text{Sum of two non-adjacent interior angles}$$

This is useful for finding hidden angle equalities that prove AA similarity.

---

## 5. Quick Decision Flowchart

> When you see a triangle problem on the SAT, follow this checklist:

1. **Are there parallel lines?** → Look for corresponding/alternate angles → **AA similarity**
2. **Do two triangles share a vertex?** → That's one equal angle. Look for a second (right angle, vertical angle, or from a parallel line) → **AA similarity**
3. **Are two lines crossing between parallel lines?** → Vertical angles + alternate interior angles → **AA similarity**
4. **Are you given all side lengths?** → Check if they're proportional → **SSS similarity**
5. **Is it asking for a missing side?** → Confirm similarity, then **set up a proportion**
6. **Is it asking for an area?** → Use $k^2$: square the side ratio

---

## SAT Tips

1. **AA is king** — on the SAT, virtually every similarity question is solved by finding two equal angles. Don't waste time looking for side ratios unless you have to.
2. **The order of letters matters** — $\triangle ABC \sim \triangle DEF$ means $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$. Set up proportions accordingly.
3. **Parallel lines = free similarity** — any time a line is parallel to one side of a triangle and cuts the other two sides, you get similar triangles. This is the **single most tested setup**.
4. **Right angles are your friend** — two right triangles only need **one more** equal angle to be similar (since the right angle is already shared).
5. **Altitude to the hypotenuse** — in a right triangle, the altitude from the right angle to the hypotenuse creates **three similar triangles** (the original + two smaller ones). This is a classic SAT setup.
6. **Watch for "not drawn to scale"** — don't judge similarity by how the triangles look. Use given angles and sides only.
7. **Congruence is rare on the SAT** — similar triangles appear much more often. When congruence does appear, it's usually in the context of isosceles/equilateral triangles or transformations (reflections, rotations).
8. **On Desmos** — if a problem gives you coordinates, plot the triangles. You can visually confirm similarity and measure side lengths.
