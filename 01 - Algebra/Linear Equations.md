---
domain: Algebra
topic: Linear Equations
status: studied
tags: [algebra, linear-equations, sat-math]
---

# Linear Equations

## Forms of Linear Equations

| Form | Equation | When to Use |
|------|----------|-------------|
| Slope-intercept | $y = mx + b$ | Graphing, identifying slope/intercept |
| Standard | $Ax + By = C$ | Finding intercepts, integer solutions |
| Point-slope | $y - y_1 = m(x - x_1)$ | When given a point and slope |

### Conversions

**Standard → Slope-intercept:**
$$Ax + By = C \implies y = -\frac{A}{B}x + \frac{C}{B}$$

**Point-slope → Slope-intercept:**
$$y - y_1 = m(x - x_1) \implies y = mx + (y_1 - mx_1)$$

---

## Slope

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x} = \frac{\text{rise}}{\text{run}}$$

| Slope | Direction |
|-------|-----------|
| $m > 0$ | Line rises left → right |
| $m < 0$ | Line falls left → right |
| $m = 0$ | Horizontal line ($y = b$) |
| Undefined | Vertical line ($x = a$) |

### Parallel and Perpendicular

- **Parallel lines**: $m_1 = m_2$ (same slope, different intercept)
- **Perpendicular lines**: $m_1 \cdot m_2 = -1$ (negative reciprocal slopes)

---

## Solving Linear Equations (One Variable)

**Method:**
1. Distribute and simplify each side
2. Collect variable terms on one side, constants on the other
3. Divide to isolate the variable

**Number of solutions:**

| Result | Solutions | Meaning |
|--------|-----------|---------|
| $x = \text{number}$ | Exactly one | Unique solution |
| $0 = \text{nonzero}$ (e.g., $0 = 5$) | None | Contradiction — inconsistent equation |
| $0 = 0$ | Infinitely many | Identity — both sides are the same |

**Example — No solution:**
$$3(x + 2) = 3x + k$$
$$3x + 6 = 3x + k$$
No solution when $k \neq 6$ (constants differ after variables cancel).

---

## Finding an Equation

**Given slope $m$ and a point $(x_1, y_1)$:**
$$y - y_1 = m(x - x_1)$$

**Given two points:**
1. $m = \frac{y_2 - y_1}{x_2 - x_1}$
2. Plug $m$ and one point into point-slope form

**Given x-intercept $(a, 0)$ and y-intercept $(0, b)$:**
$$\frac{x}{a} + \frac{y}{b} = 1$$

---

## Interpreting in Context (SAT Favorite)

In $y = mx + b$:
- **$m$ (slope)** = rate of change per unit of $x$
- **$b$ (y-intercept)** = initial value (value when $x = 0$)

> *"A plumber charges \$50 plus \$30 per hour"*
> $C = 30h + 50$ → slope is hourly rate, intercept is flat fee

---

## SAT Tips

1. **Equations with fractions** — multiply every term by the LCD first
2. **"What does the number represent?"** — always slope (rate) or y-intercept (starting value)
3. **No solution / infinite solutions** — compare coefficients: if variable coefficients are proportional but constants are not → no solution; if everything is proportional → infinite
4. **Creating equations from tables** — pick two rows to find slope, then use point-slope
5. **Quick intercepts from standard form** $Ax + By = C$: x-intercept = $C/A$, y-intercept = $C/B$
