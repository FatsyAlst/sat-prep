---
domain: Algebra
topic: Systems of Linear Equations
status: studied
tags: [algebra, systems, sat-math]
---

# Systems of Linear Equations

A system of two linear equations in two variables:
$$\begin{cases} a_1x + b_1y = c_1 \\ a_2x + b_2y = c_2 \end{cases}$$

---

## Solving Methods

### Substitution
1. Isolate one variable in one equation
2. Substitute into the other equation
3. Solve → back-substitute

> Best when one variable already has coefficient 1 or is already isolated.

**Example:**
$$\begin{cases} y = 3x - 1 \\ 2x + y = 9 \end{cases}$$
Substitute: $2x + (3x - 1) = 9 \implies 5x = 10 \implies x = 2, \; y = 5$

### Elimination (Addition)
1. Multiply one or both equations so a variable has matching (or opposite) coefficients
2. Add or subtract equations to eliminate that variable
3. Solve → back-substitute

> Best when both equations are in standard form.

**Example:**
$$\begin{cases} 3x + 2y = 12 \\ x - 2y = 4 \end{cases}$$
Add both: $4x = 16 \implies x = 4, \; y = 0$

---

## Number of Solutions

| Condition | Solutions | Geometrically |
|-----------|-----------|---------------|
| $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ | **One** (unique) | Lines intersect |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$ | **None** | Lines are parallel |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | **Infinite** | Same line |

### Quick Check (Slope Comparison)
Convert both to slope-intercept form:
- **Different slopes** → one solution
- **Same slope, different intercept** → no solution
- **Same slope, same intercept** → infinite solutions

---

## Systems with a Parameter

*"For what value of $k$ does the system have no solution?"*

$$\begin{cases} 2x + ky = 6 \\ 4x + 6y = 10 \end{cases}$$

No solution when slopes are equal but intercepts differ:
$$\frac{2}{4} = \frac{k}{6} \neq \frac{6}{10}$$
$$k = 3$$
Check: $\frac{6}{10} = 0.6 \neq \frac{6}{6} = 1$ ✓ → No solution when $k = 3$

---

## Word Problems Strategy

1. **Define variables** — write what $x$ and $y$ represent
2. **Write two equations** from two different conditions
3. **Solve** using substitution or elimination
4. **Check** the answer makes sense in context

### Common Setups
| Scenario | Equations |
|----------|-----------|
| Mixture problems | $x + y = \text{total}$ and $\text{rate}_1 \cdot x + \text{rate}_2 \cdot y = \text{total value}$ |
| Speed/distance | $d = rt$ for each leg of the trip |
| Cost problems | quantity equation + value equation |

**Example:**
*"Tickets cost \$8 for adults and \$5 for children. 200 tickets sold totaling \$1,300."*
$$\begin{cases} a + c = 200 \\ 8a + 5c = 1300 \end{cases}$$
From first: $a = 200 - c$. Substitute: $8(200-c) + 5c = 1300 \implies c = 100, \; a = 100$

---

## SAT Tips

1. **Speed matters** — if one equation already has a variable isolated, use substitution; otherwise prefer elimination
2. **"How many solutions?"** — don't solve, just compare slopes (coefficients)
3. **Systems with fractions** — multiply to clear denominators first
4. **The SAT sometimes gives systems disguised as word problems** — look for two unknowns and two conditions
5. **Check your answer** — plug the solution back into BOTH original equations
