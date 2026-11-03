---
domain: Advanced Math
topic: The Discriminant
chapter: 1600.io Chapter 11
status: studied
tags: [advanced-math, quadratics, discriminant, sat-math]
---

# The Discriminant

## The Formula

For a quadratic in standard form $y = ax^2 + bx + c$:

$$\Delta = b^2 - 4ac$$

The discriminant tells you exactly how many **real zeros** (roots / $x$-intercepts) the parabola has.

---

## The Three Cases

| $\Delta$ | Real roots | Graph behaviour |
|---|---|---|
| $\Delta > 0$ | **2 distinct** real roots | Parabola crosses $x$-axis at two points |
| $\Delta = 0$ | **1 repeated** real root | Vertex touches $x$-axis (tangent) |
| $\Delta < 0$ | **0 real roots** | Parabola never crosses $x$-axis; 2 complex conjugate roots |

---

## When to Use the Discriminant vs. When to Skip It

### Skip the discriminant — use these first:

**Factored form given (or quadratic factors cleanly):**
Count the distinct linear factors. $(x-r)^2$ = one repeated root; two distinct factors = two roots. Done.

**Vertex form given (or after completing the square):**
Check the vertex position relative to the $x$-axis and the sign of $a$:

| $a > 0$ (opens up) | Roots |
|---|---|
| Vertex below $x$-axis $(k < 0)$ | 2 real roots |
| Vertex on $x$-axis $(k = 0)$ | 1 real root |
| Vertex above $x$-axis $(k > 0)$ | 0 real roots |

For $a < 0$ (opens down), reverse all three: vertex above → 2 roots, on → 1 root, below → 0 roots.

### Use the discriminant when:
Standard form is all you have and it doesn't factor cleanly.

---

## Decision Flow

```
Quadratic given
      |
      ├── Factored form / factors cleanly? → Count distinct linear factors
      |
      ├── Vertex form / easy to complete square? → Check vertex vs. x-axis & sign of a
      |
      └── Otherwise → Compute Δ = b² − 4ac
```

> **SAT Key Takeaway:** the discriminant is your last resort, not your first. On the SAT, recognising which shortcut applies is faster than computing $\Delta$. If the quadratic is already in vertex form, never touch $b^2 - 4ac$ — just look at the picture.

---

## Important Connections

**Discriminant and tangent lines:**
A horizontal line $y = k$ is tangent to a parabola at exactly one point $\Leftrightarrow \Delta = 0$ after substituting $y = k$.

**Discriminant and Vieta's:**
$\Delta > 0$ only guarantees two *real* roots. For two *integer* roots, you need Vieta's + factor pairs — don't confuse these two conditions.

**Discriminant in systems (line + parabola):**
Substituting the line into the parabola and setting $\Delta > 0 / = 0 / < 0$ tells you how many intersections the system has — this is how most SAT system problems connect to the discriminant.

---

## SAT Tips

1. **Standard form only → compute $\Delta$**; factored or vertex form → skip $\Delta$ entirely.
2. **"Exactly one solution" in a system** → substitute and set $\Delta = 0$. This is the most common discriminant question type on the SAT.
3. **"Two real solutions"** means $\Delta > 0$; **"no real solutions"** means $\Delta < 0$. On grid-in questions, set up the inequality and solve for the parameter.
4. **$\Delta = 0$ ↔ tangent** — the parabola and the line kiss at one point, the vertex is on the line.
5. **Watch for "two integer solutions"** — this is NOT answered by $\Delta > 0$ alone; go straight to Vieta's and integer factor pairs of the constant term.
