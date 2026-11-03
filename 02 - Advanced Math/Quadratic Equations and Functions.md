---
domain: Advanced Math
topic: Quadratic Equations and Functions
chapter: 1600.io Chapter 10
status: studied
tags: [advanced-math, quadratics, parabolas, sat-math]
---

# Quadratic Equations and Functions

## The Three Forms

| Form | Equation | What it reveals directly |
|---|---|---|
| Standard | $y = ax^2 + bx + c$ | $y$-intercept $= c$; sign of $a$ gives direction |
| Factored | $y = a(x+p)(x+q)$ | Roots: $x = -p$ and $x = -q$ |
| Vertex | $y = a(x-h)^2 + k$ | Vertex $= (h, k)$; axis of symmetry $x = h$ |

In all three forms, the sign of $a$ controls direction: $a > 0$ opens upward, $a < 0$ opens downward.

---

## Standard Form — $y = ax^2 + bx + c$

### Key formulas

$$x_v = -\frac{b}{2a} \qquad y_v = c - \frac{b^2}{4a}$$

The $y$-intercept is $(0, c)$ — read it off directly.

### Solving $ax^2 + bx + c = 0$

**Quadratic formula** (always works):
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Completing the square** (useful when converting to vertex form):
$$ax^2 + bx + c = a\!\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)$$

---

## Factored Form — $y = a(x+p)(x+q)$

The roots (zeros, $x$-intercepts) are $x = -p$ and $x = -q$.

**Vieta's formulas** — sum and product of roots for $ax^2 + bx + c = 0$:

$$r_1 + r_2 = -\frac{b}{a} \qquad r_1 \cdot r_2 = \frac{c}{a}$$

> **SAT use:** if the problem says "two integer solutions" and gives you a product, list all integer factor pairs of the product — the discriminant is a detour.

**Axis of symmetry from roots:** since the parabola is symmetric, the axis passes through the midpoint of the roots:
$$x_v = \frac{r_1 + r_2}{2} = -\frac{b}{2a}$$

This also means the two roots are always **equidistant from the vertex** — useful for finding a second root when one is given.

---

## Vertex Form — $y = a(x-h)^2 + k$

Vertex is $(h, k)$. Watch the sign: $(x - h)^2$ means the vertex is at $x = h$, not $x = -h$.

**Converting Standard → Vertex (completing the square):**
$$y = a\!\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)$$

So: $h = -\dfrac{b}{2a}$, $\quad k = c - \dfrac{b^2}{4a}$

---

## The Bermuda Triangle — Converting Between Forms

```
Standard Form          Factored Form
 y = ax² + bx + c  ←→  y = a(x+p)(x+q)
        ↕                      ↕
           Vertex Form
         y = a(x−h)² + k
```

| From | To | Method |
|---|---|---|
| Standard | Factored | Factor or use quadratic formula |
| Standard | Vertex | Complete the square |
| Factored | Standard | Expand |
| Vertex | Standard | Expand |
| Factored | Vertex | Midpoint of roots → $h$; plug back in → $k$ |

---

## Graphical Behaviour

| Feature | How to find it |
|---|---|
| Direction | Sign of $a$: up $(+)$, down $(-)$ |
| Vertex | $\left(-\frac{b}{2a},\; c - \frac{b^2}{4a}\right)$ or read from vertex form |
| Axis of symmetry | $x = -\frac{b}{2a}$ |
| $y$-intercept | $(0, c)$ from standard form |
| $x$-intercepts | Set $y = 0$, solve |
| Number of real roots | Sign of discriminant $\Delta = b^2 - 4ac$ |

**Horizontal line intersections:** $f(x) = k$ has the same number of solutions as the horizontal line $y = k$ intersecting the parabola. Count visually whenever a graph is provided — never solve algebraically when you can just read the picture.

---

## SAT Tips

1. **Vertex form is the most useful for SAT questions** — if a question mentions a vertex or asks about minimum/maximum, convert to vertex form immediately.
2. **Factored form is fastest for roots** — if you need zeros and the quadratic factors cleanly, go straight to factored form.
3. **The $y$-intercept is always $c$** in standard form — this is a free point, always check if a question can be answered by just reading $c$.
4. **Mirror symmetry shortcut:** one root given, vertex known → second root = $2h - r_1$. Never reconstruct the full equation if you can mirror.
5. **$a$ controls narrowness too:** larger $|a|$ = narrower parabola. The SAT occasionally asks about relative widths of two parabolas.
6. **Horizontal tangent = exactly one intersection = $\Delta = 0$** — this is the bridge between the discriminant and vertex form.
