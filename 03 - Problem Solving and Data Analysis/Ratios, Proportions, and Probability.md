---
domain: Problem Solving and Data Analysis
topic: Ratios, Proportions, and Probability
chapter: 1600.io Chapter 12
status: studied
tags: [psda, ratios, proportions, probability, sat-math]
---

# Ratios, Proportions, and Probability

## Ratios

A ratio $a:b$ is equivalent to the fraction $\dfrac{a}{b}$. Ratios can appear as fractions, decimals, or colon notation — all interchangeable.

**Two types of fractions from a ratio $a:b$:**

| Type | Fraction | Use |
|---|---|---|
| Part-to-part | $\dfrac{a}{b}$ or $\dfrac{b}{a}$ | Comparing one part to another |
| Part-to-whole | $\dfrac{a}{a+b}$ or $\dfrac{b}{a+b}$ | Comparing one part to the total |

> **SAT trap:** read the question carefully — it may ask for a part-to-part ratio when you computed part-to-whole, or vice versa. The denominator tells you which one you need.

**Reducing ratios:** works exactly like reducing fractions.
- $4:10 = 2:5$
- $6:8:10 = 3:4:5$ (divide all terms by the same number)

**Ratios with more than two terms** (e.g. side lengths $3:4:5$) work the same way — reduce by dividing every term by the GCD.

---

## Proportions

A proportion sets two ratios equal: $\dfrac{a}{b} = \dfrac{c}{d}$.

**When to use proportions:** whenever a relationship has a **constant rate of change** — i.e., it is linear and passes through the origin. If it doesn't pass through the origin (has a fixed cost, intercept, etc.), proportions do NOT apply.

**Solving tip:** place the unknown in the **numerator on the left side** to minimise algebraic steps.

$$\frac{x}{\text{known}} = \frac{\text{known}}{\text{known}} \implies x = \text{cross-multiply and solve}$$

**Non-linear relationships — proportions fail:**
If $A = \pi r^2$, doubling $r$ does **not** double $A$ — it quadruples it. Always check whether the relationship is linear before writing a proportion.

**Subscript method for unknown ratios:** when both quantities in a ratio are variables, introduce subscripts ($r_1, r_2$) and cancel common factors algebraically instead of plugging in numbers.

---

## Probability

$$P(\text{event}) = \frac{\text{number of desired outcomes}}{\text{total number of possible outcomes}}$$

### Finding the Denominator — the "Reference Group" Rule

The denominator is always the **total number of entities in the reference group**. The reference group is usually signalled by an **"if" statement** in the question:

> *"If a plumber from California is chosen at random..."*
> → denominator = all plumbers from California (not all plumbers, not all Californians)

The **numerator must always be a subset of the denominator** — it cannot include people/things outside the reference group.

### Two-Way Tables

- The intersection of a row and column gives the count for both conditions simultaneously.
- Always identify the reference group first (the "if" clause) → that cell or marginal total becomes your denominator.
- The row and column totals (marginals) are the part-to-whole denominators when no condition is given.

### Bar Graphs

- Estimate carefully when gridlines are sparse — read the scale, note the axis label, and do not assume equal spacing.
- Pay attention to legends when multiple bars are shown per category.

### Multi-Step Probability

Some SAT problems require building a full scenario (lines, tables, lists) before computing the probability. Steps:
1. Set up the full sample space (draw a table or list if needed)
2. Identify the reference group
3. Count the favourable outcomes within that group
4. Compute the fraction

---

## SAT Tips

1. **Part-to-part vs part-to-whole:** decide which you need *before* writing any fraction — misreading this is the #1 ratio error.
2. **"If X is chosen at random..."** → that's your denominator. Circle the "if" clause.
3. **Proportions only for linear, origin-passing relationships** — check before using them.
4. **Unknown in numerator on the left** — cleaner algebra, fewer errors.
5. **Squared/cubed relationships** (area, volume) → do not use proportions; scale the formula directly.
6. **Multi-step probability** — slow down, build the full sample space, then count.
