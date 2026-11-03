---
type: practice
tags: [desmos, practice, bluebook, module-2, beginner]
---

# Desmos Practice — SAT Bluebook Calculator

> A **beginner-friendly** guide to using Desmos on the Digital SAT.
> Desmos is built into the Bluebook app and available on **every** math question (both modules).
> This guide is organized from basics → advanced tricks, with SAT exercises at each step.
> **Goal:** Know exactly what to type and when to type it — no fumbling on test day.

---

# Part 1 — The Desmos Interface

> [!info]- What You See in Bluebook
>
> When you click the **calculator icon** in the Bluebook toolbar, Desmos opens as a panel:
>
> | Area | What it does |
> |---|---|
> | **Left panel** | Expression lines — numbered rows where you type equations |
> | **Right panel** | Graph — coordinate plane where everything is plotted |
> | **"+" button** (upper-left) | Add: Expression, Table, Note, or Folder |
> | **Wrench icon** | Graph settings (axis ranges, grid style) |
> | **Zoom +/−** | Zoom in or out on the graph |
>
> **Navigation:** Click and drag the graph to pan. Scroll or pinch to zoom.
>
> **Between modules:** Your Desmos work **resets** — nothing carries over from Module 1 to Module 2.
>
> **You also have your FX-991CW.** Use BOTH strategically:
> - **Desmos** → graphing, visual solving, intersections, regression, sliders
> - **FX-991CW** → quick arithmetic, polynomial roots, systems, verify mode

---

# Part 2 — Typing in Desmos (Master This First!)

> [!tip] Golden Rule: Type with your keyboard, NOT the on-screen buttons
> The on-screen keyboard is slow. Learn these shortcuts and you'll be 3× faster.

### Typing shortcuts

| You type | Desmos shows | Example |
|---|---|---|
| `/` or type `frac` | Fraction $\frac{a}{b}$ | `3/4` → $\frac{3}{4}$ |
| `^` | Exponent | `x^2` → $x^2$ |
| `_` | Subscript | `x_1` → $x_1$ |
| `sqrt` | $\sqrt{\phantom{x}}$ | `sqrt(x+1)` → $\sqrt{x+1}$ |
| `cbrt` | $\sqrt[3]{\phantom{x}}$ | `cbrt(8)` → $\sqrt[3]{8}$ |
| `nthroot` | $\sqrt[n]{\phantom{x}}$ | `nthroot(x,5)` → $\sqrt[5]{x}$ |
| `pi` | $\pi$ | `2pi` → $2\pi$ |
| `abs()` | $|x|$ | `abs(x-3)` → $|x-3|$ |
| `>=` | $\geq$ | `y >= 2x+1` → $y \geq 2x + 1$ |
| `<=` | $\leq$ | `y <= -x+5` → $y \leq -x + 5$ |
| `log` | $\log$ (base 10) | `log(100)` → $2$ |
| `ln` | $\ln$ (natural) | `ln(e)` → $1$ |

### ⚠️ The #1 Desmos error: Forgetting parentheses

| What you type | What Desmos computes | What you probably meant |
|---|---|---|
| `2x+3^2` | $2x + 9$ | $2(x+3)^2$ → type `2(x+3)^2` |
| `1/x+1` | $\frac{1}{x} + 1$ | $\frac{1}{x+1}$ → type `1/(x+1)` |
| `-x^2` | $-(x^2)$ = correct | — |
| `2^x+1` | $2^x + 1$ | $2^{x+1}$ → type `2^(x+1)` |

> **Rule:** When in doubt, add parentheses. They never hurt, but missing ones are devastating.

---

# Part 3 — Core Desmos Skills (with Exercises)

---

## Skill 1 — Graphing and Finding Intersections

> [!note] When to use
> Any question asking "what is the solution to..." or "at what point do these meet?"

### How to do it

1. Type each equation on its own line (Line 1, Line 2, etc.)
2. Desmos graphs them both
3. **Grey dots** appear at intersections, intercepts, vertices, and other "interesting points"
4. **Click a grey dot** → the coordinates appear as a label

### Important: You do NOT need to put equations in $y = $ form. Desmos handles ANY form:
- $3x + 2y = 7$ ✓
- $x^2 + y^2 = 25$ ✓
- $x = 5$ ✓ (vertical line)

---

> [!question]- 1.1 Basic system — intersection point
> $$\begin{cases} y = 3x - 5 \\ y = -x + 7 \end{cases}$$
> At what point do these lines intersect?
>
> **Desmos steps:**
> - Line 1: type `y = 3x - 5`
> - Line 2: type `y = -x + 7`
> - Click the grey dot where they cross
>
> > [!success]- Answer
> > $(3, 4)$
> >
> > **By hand check:** $3(3) - 5 = 4$ ✓ and $-3 + 7 = 4$ ✓
> >
> > ⏱️ **Time:** ~10 seconds with Desmos vs ~60 seconds by hand

> [!question]- 1.2 System in standard form
> $$\begin{cases} 2x + 3y = 12 \\ x - y = 1 \end{cases}$$
> What is the value of $y$?
>
> **Desmos steps:**
> - Line 1: type `2x + 3y = 12`
> - Line 2: type `x - y = 1`
> - Click intersection dot → read $y$
>
> > [!success]- Answer
> > Intersection: $(3, 2)$. So $y = 2$.
> >
> > ⚠️ **Trap:** The question asks for $y$, not $x$. Read carefully.

> [!question]- 1.3 Linear-quadratic system
> How many times do $y = x^2 - 4$ and $y = 2x - 1$ intersect?
>
> **Desmos steps:**
> - Line 1: `y = x^2 - 4`
> - Line 2: `y = 2x - 1`
> - Count the grey dots
>
> > [!success]- Answer
> > **2 intersections** at $(3, 5)$ and $(-1, -3)$
> >
> > **Algebraic verify:** $x^2 - 4 = 2x - 1 \Rightarrow x^2 - 2x - 3 = 0 \Rightarrow (x-3)(x+1) = 0$ ✓

> [!question]- 1.4 Absolute value equation
> Solve $|2x - 6| = x + 1$.
>
> **Desmos steps:**
> - Line 1: `y = abs(2x - 6)`
> - Line 2: `y = x + 1`
> - Click each intersection → read the $x$-values
>
> > [!success]- Answer
> > Intersections at $x = \frac{5}{3} \approx 1.67$ and $x = 7$
> >
> > ⚠️ **Trap:** Absolute value equations can have 0, 1, or 2 solutions. Don't assume there's always two.

> [!question]- 1.5 Finding $x$-intercepts
> What are the $x$-intercepts (zeros) of $f(x) = x^3 - 4x^2 + x + 6$?
>
> **Desmos steps:**
> - Line 1: `y = x^3 - 4x^2 + x + 6`
> - Click the grey dots on the $x$-axis
>
> > [!success]- Answer
> > $x$-intercepts at $x = -1, 2, 3$
> >
> > ⚠️ **Tip:** If a grey dot doesn't appear, zoom in to that area. Sometimes they're too close together to show at the default zoom.

---

## Skill 2 — Sliders for Parameter Questions

> [!note] When to use
> "For what value of $k$..." or "What value of $b$ makes the equation..." — any time there's an unknown constant you need to find.

### How to do it

1. Type the equation with the unknown constant (use any letter except $x$, $y$, $e$, $r$, $\pi$)
2. Desmos detects the unknown and shows **"add slider"** — click it
3. A slider appears under the expression line
4. Drag the slider and watch the graph change in real time
5. Stop when the visual condition is met (tangent, no intersection, passes through a point, etc.)
6. Read the slider value — that's your answer

### ⚠️ Slider WARNING

> [!warning] Sliders are NOT reliable for "no solution" (parallel lines) problems
> It's nearly impossible to visually confirm that two lines NEVER intersect — they might just intersect far off-screen. For "no solution," use algebra or the regression trick instead.

---

> [!question]- 2.1 Tangent to a parabola — find $k$
> For what positive value of $k$ is the line $y = kx$ tangent to the parabola $y = x^2 + 1$?
>
> **Desmos steps:**
> - Line 1: `y = x^2 + 1`
> - Line 2: `y = kx` → click "add slider" for $k$
> - Drag $k$ until the line just touches the parabola at exactly ONE point
>
> > [!success]- Answer
> > $k = 2$ (the line $y = 2x$ is tangent at $(1, 2)$)
> >
> > **By algebra:** $kx = x^2 + 1 \Rightarrow x^2 - kx + 1 = 0$. Tangent ↔ $\Delta = 0$: $k^2 - 4 = 0 \Rightarrow k = 2$.
> >
> > ⏱️ **Time:** ~15 seconds with slider vs ~45 seconds with algebra

> [!question]- 2.2 Horizontal line through a vertex
> The vertex of $y = 2(x - h)^2 + 5$ is at $y = 5$. What value of $h$ makes the parabola pass through $(3, 13)$?
>
> **Desmos steps:**
> - Line 1: `y = 2(x - h)^2 + 5` → slider for $h$
> - Line 2: Plot the point `(3, 13)`
> - Drag $h$ until the parabola passes through the point
>
> > [!success]- Answer
> > $13 = 2(3 - h)^2 + 5 \Rightarrow 2(3-h)^2 = 8 \Rightarrow (3-h)^2 = 4$
> > $h = 1$ or $h = 5$
> >
> > The slider will "snap" to both values as you drag through them.
> >
> > ⚠️ **Trap:** There are TWO valid values of $h$. The slider shows you this visually — the parabola passes through the point twice as you sweep $h$.

> [!question]- 2.3 System with exactly one solution
> For what value of $c$ do the equations $y = x^2 - 6x + c$ and $y = 0$ (the $x$-axis) have exactly one solution?
>
> **Desmos steps:**
> - Line 1: `y = x^2 - 6x + c` → slider for $c$
> - Watch the parabola — drag $c$ until it just touches the $x$-axis at ONE point
>
> > [!success]- Answer
> > $c = 9$ — parabola vertex sits exactly on the $x$-axis at $(3, 0)$
> >
> > $\Delta = 36 - 4c = 0 \Rightarrow c = 9$ ✓

---

## Skill 3 — The Regression Trick ($y_1 \sim ...$)

> [!note] When to use
> This is the single most powerful Desmos trick for the SAT.
> - Find an equation that fits a set of points
> - Find unknown constants in equivalent expressions
> - Solve ANY equation without graphing

> [!tip] Key concept: `~` is the regression operator
> `=` means "graph this equation exactly"
> `~` means "find the best-fit values for any unknowns"

### Method A — Regression from a table of data

1. Click **"+"** → **Table**
2. Enter $x$-values in the first column ($x_1$) and $y$-values in the second ($y_1$)
3. Points appear on the graph
4. On a new expression line, type the model you want:
   - Linear: `y_1 ~ mx_1 + b`
   - Quadratic: `y_1 ~ ax_1^2 + bx_1 + c`
   - Exponential: `y_1 ~ a*b^x_1`
   - Vertex form: `y_1 ~ a(x_1 - h)^2 + k`
5. Desmos displays the parameter values (e.g., $m = 2.5$, $b = 0.3$)

### Method B — Solving equations via regression

Instead of graphing $f(x) = 5$ and clicking the intersection, type:
- Define variables: `x_1 = [1, 2, 3, 4, 5]` (give it several test values)
- Then type: `Left Side ~ Right Side` (using `x_1` instead of `x`)
- Desmos finds the parameter values that make both sides match

### ⚠️ Subscripts are crucial
Type `x_1` (with underscore), NOT `x1` (which Desmos reads as "$x$ times $1$").
Same for `y_1` — use the underscore.

---

> [!question]- 3.1 Find the equation from a table
> | $x$ | $y$ |
> |---|---|
> | 1 | 5 |
> | 2 | 11 |
> | 3 | 21 |
> | 4 | 35 |
>
> Find the quadratic equation that fits this data.
>
> **Desmos steps:**
> - Click "+" → Table → enter the data
> - On a new line, type: `y_1 ~ ax_1^2 + bx_1 + c`
> - Read the parameter values
>
> > [!success]- Answer
> > $a = 2$, $b = 0$, $c = 3$
> > **Equation: $y = 2x^2 + 3$**
> >
> > **Verify:** $f(1) = 2+3 = 5$ ✓, $f(2) = 8+3 = 11$ ✓, $f(3) = 18+3 = 21$ ✓, $f(4) = 32+3 = 35$ ✓, $R^2 = 1$
> >
> > ⚠️ **Tip:** After running the regression, always verify against one data point. If $R^2 = 1$, the fit is perfect — no need to doubt the output.

> [!question]- 3.2 Exponential regression
> | $x$ | $y$ |
> |---|---|
> | 0 | 50 |
> | 1 | 75 |
> | 2 | 112.5 |
> | 3 | 168.75 |
>
> Find the exponential equation.
>
> **Desmos steps:**
> - Table → enter data
> - Type: `y_1 ~ a*b^x_1`
>
> > [!success]- Answer
> > $a = 50$, $b = 1.5$
> > Equation: $y = 50 \cdot 1.5^x$
> >
> > This means a 50% increase per unit of $x$.
> >
> > ⚠️ **Tip:** Growth factor $b = 1.5$ means +50% growth. Decay would be $b < 1$ (e.g., $b = 0.85$ means 15% decrease per unit).

> [!question]- 3.3 The power move: Finding unknown constants
> $(5x - 17)(4x - c) = 20x^2 + bx + 119$. Find $b$.
>
> **Desmos steps:**
> - Line 1: `x_1 = [1, 2, 3, 4]` (need at least as many test values as unknowns)
> - Line 2: `(5x_1 - 17)(4x_1 - c) ~ 20x_1^2 + bx_1 + 119`
> - Read the regression parameters
>
> > [!success]- Answer
> > $c = 7$, $b = -103$
> >
> > **Verify by expansion:** $(5x-17)(4x-7) = 20x^2 - 35x - 68x + 119 = 20x^2 - 103x + 119$ ✓
> >
> > ⏱️ **Time:** ~20 seconds with regression vs ~90 seconds expanding by hand

> [!question]- 3.4 Solving an equation via regression
> Solve $3^x = 5x + 2$ for $x > 0$.
>
> **Desmos steps (Method 1 — graph):**
> - Line 1: `y = 3^x`
> - Line 2: `y = 5x + 2`
> - Click intersection
>
> **Desmos steps (Method 2 — regression):**
> - Line 1: `3^x ~ 5x + 2` → Desmos auto-solves for $x$
>
> > [!success]- Answer
> > $x \approx 2.4$ (the positive solution)
> >
> > **Check:** $3^{2.4} \approx 13.97$ and $5(2.4)+2 = 14.0$ ✓
> >
> > The graphing method is usually cleaner here since you can see ALL solutions.
> >
> > ⚠️ **Tip:** Method 1 (graphing) is better when you want to see HOW MANY solutions exist. Method 2 (regression) is better when you know there's one solution and want it fast.

> [!question]- 3.5 Mean / statistics via regression
> The mean of $\{3, 7, x, 12, 5\}$ is $8$. Find $x$.
>
> **Desmos steps:**
> - Type: `mean(3, 7, x, 12, 5) ~ 8`
> - Or equivalently: `(3 + 7 + x + 12 + 5)/5 ~ 8`
>
> > [!success]- Answer
> > $x = 13$
> >
> > **Check:** $(3 + 7 + 13 + 12 + 5)/5 = 40/5 = 8$ ✓
> >
> > ⚠️ **This is wild:** You can put unknowns INSIDE Desmos statistical functions and it solves for them. `median(1, 2, x, 7, 9) ~ 4` will find $x$ that makes the median equal 4.

---

## Skill 4 — Vertex and Max/Min Finding

> [!note] When to use
> "What is the maximum/minimum value?" or "Find the vertex."

### How to do it

1. Type your quadratic: e.g., `y = -2x^2 + 8x - 3`
2. The parabola appears
3. A **grey dot** appears at the vertex
4. **Click it** → read the coordinates

That's it. No completing the square. No vertex formula.

---

> [!question]- 4.1 Maximum value
> What is the maximum value of $f(x) = -3x^2 + 18x - 22$?
>
> **Desmos:** Type `y = -3x^2 + 18x - 22` → click vertex dot
>
> > [!success]- Answer
> > Vertex at $(3, 5)$ → **Maximum value: $5$**
> >
> > **By formula:** $x = -18/(2 \times -3) = 3$. $f(3) = -27 + 54 - 22 = 5$ ✓
> >
> > ⚠️ **Trap:** $a = -3 < 0$ → opens DOWN → vertex is MAX (not min). If $a > 0$ → opens UP → vertex is MIN.

> [!question]- 4.2 Vertex form identification
> The vertex of $y = a(x - h)^2 + k$ is at $(3, -2)$ and the parabola passes through $(5, 6)$. Find $a$.
>
> **Desmos:**
> - Type `y = a(x - 3)^2 - 2` → slider for $a$
> - Plot the point `(5, 6)`
> - Drag slider until parabola hits the point
>
> > [!success]- Answer
> > $6 = a(5-3)^2 - 2 = 4a - 2 \Rightarrow 4a = 8 \Rightarrow a = 2$
> >
> > ⚠️ **Trap:** $(5-3)^2 = 4$, not $2$. Square the WHOLE expression inside the parentheses.

> [!question]- 4.3 Profit maximization (word problem)
> A company's profit is modeled by $P(x) = -2x^2 + 120x - 1000$, where $x$ is the number of units sold. How many units maximize profit?
>
> **Desmos:** Type `y = -2x^2 + 120x - 1000` → click vertex
>
> > [!success]- Answer
> > Vertex at $(30, 800)$ → **30 units** maximize profit (profit = \$800)
> >
> > ⚠️ **Trap:** The question asks for NUMBER OF UNITS ($x = 30$), not the maximum PROFIT ($800$). Read the question carefully.

---

## Skill 5 — Tables for Function Evaluation

> [!note] When to use
> Need to evaluate a function at many values, or find where $f(x) =$ some target.

### How to do it

1. **Define the function:** Line 1: `f(x) = x^2 - 4x + 3`
2. Click **"+"** → **Table**
3. Change the second column header from `y_1` to `f(x_1)`
4. Enter $x$-values in the first column
5. Desmos auto-computes $f(x)$ in the second column

### Lists shortcut
Type `[1, 2, 3...10]` in the first column to auto-fill integers 1 through 10.

---

> [!question]- 5.1 Finding zeros from a table
> For what values of $x$ does $f(x) = x^3 - 6x^2 + 11x - 6$ equal zero?
>
> **Desmos:**
> - Line 1: `f(x) = x^3 - 6x^2 + 11x - 6`
> - Table: $x_1 = [0, 1, 2, 3, 4]$, second column: `f(x_1)`
> - Look for where $f(x_1) = 0$
>
> > [!success]- Answer
> > $f(1) = 0$, $f(2) = 0$, $f(3) = 0$
> > **Zeros at $x = 1, 2, 3$**

> [!question]- 5.2 Finding where $f(x) = g(x)$
> Define $f(x) = 2^x$ and $g(x) = 3x + 1$. For what positive integer $x$ is $f(x) > g(x)$ for the first time?
>
> **Desmos:**
> - Line 1: `f(x) = 2^x`
> - Line 2: `g(x) = 3x + 1`
> - Table: `x_1 = [1, 2, 3, 4, 5, 6]`, columns for `f(x_1)` and `g(x_1)`
>
> > [!success]- Answer
> > | $x$ | $2^x$ | $3x+1$ |
> > |---|---|---|
> > | 1 | 2 | 4 |
> > | 2 | 4 | 7 |
> > | 3 | 8 | 10 |
> > | 4 | 16 | 13 |
> >
> > First time $f > g$: **$x = 4$**

---

## Skill 6 — Inequalities and Shaded Regions

> [!note] When to use
> "Which point is in the solution region?" or "Graph the system of inequalities."

### How to do it

1. Type each inequality on its own line:
   - `y >= 2x + 1`
   - `y < -x + 5`
2. Desmos shades the valid region for each
3. The **overlap** (darkest shading) = solution set
4. To check a point: plot it as `(a, b)` — if it's in the darkest region, it works

### Advanced overlap trick (from SAT tutors)
Combine into one expression: `x + y <= 10 {y >= 2x - 3}`
This shows ONLY the overlap region — no ambiguity.

---

> [!question]- 6.1 Which point satisfies both inequalities?
> $$\begin{cases} y > 2x - 3 \\ y \leq -x + 6 \end{cases}$$
> Which point is in the solution region?
> (A) $(4, 1)$  (B) $(1, 4)$  (C) $(3, 3)$  (D) $(5, 0)$
>
> **Desmos:**
> - Line 1: `y > 2x - 3`
> - Line 2: `y <= -x + 6`
> - Plot each point: `(4, 1)`, `(1, 4)`, `(3, 3)`, `(5, 0)`
> - See which point falls in the darkest shaded overlap
>
> > [!success]- Answer
> > (A): $1 > 5$? NO ✗
> > (B): $4 > -1$? YES ✓ and $4 \leq 5$? YES ✓ → **(B) $(1, 4)$**
> > (C): $3 > 3$? NO ✗ (strict inequality!)
> > (D): $0 > 7$? NO ✗
> >
> > ⚠️ **Trap:** (C) fails because $y > 2x - 3$ is STRICT (not $\geq$). $3 > 3$ is FALSE.

> [!question]- 6.2 Shading direction
> Graph $y < x^2 - 4$.
>
> **Desmos:** Type `y < x^2 - 4`
>
> > [!success]- Answer
> > Desmos shades the region BELOW the parabola $y = x^2 - 4$ (with a dashed boundary since it's strict $<$).
> >
> > ⚠️ **Trap:** $y <$ → shade BELOW. $y >$ → shade ABOVE. For $x <$ → shade LEFT. For $x >$ → shade RIGHT.

---

## Skill 7 — Checking Answer Choices (Equivalent Expressions)

> [!note] When to use
> "Which expression is equivalent to...?" — graph the original and each choice.

### How to do it

1. Graph the original expression: `y = [original]` on Line 1
2. Graph each answer choice on Lines 2–5
3. The correct answer will **perfectly overlap** Line 1
4. **Toggle trick:** Click the colored circle next to each line to show/hide it. If two graphs look identical when toggled, they're equivalent.

---

> [!question]- 7.1 Which expression is equivalent?
> Which is equivalent to $\frac{x^2 - 4}{x + 2}$ for $x \neq -2$?
> (A) $x + 2$  (B) $x - 2$  (C) $x^2 - 2$  (D) $\frac{x-4}{2}$
>
> **Desmos:**
> - Line 1: `y = (x^2 - 4)/(x + 2)`
> - Line 2: `y = x + 2`
> - Line 3: `y = x - 2`
> - Toggle Line 1 and Line 3 — they should perfectly overlap (except at $x = -2$)
>
> > [!success]- Answer
> > **(B) $x - 2$** — the graphs overlap perfectly.
> >
> > **Algebra:** $\frac{x^2-4}{x+2} = \frac{(x-2)(x+2)}{x+2} = x - 2$ ✓
> >
> > ⚠️ **Tip:** There's a tiny hole in Line 1 at $x = -2$ (undefined), but Line 3 passes through that point. This visual difference confirms the domain restriction — but for SAT purposes, answers (B) and the original are "equivalent for $x \neq -2$."

> [!question]- 7.2 Factored form check
> Which is equivalent to $2x^2 + 5x - 3$?
> (A) $(2x - 1)(x + 3)$  (B) $(2x + 1)(x - 3)$  (C) $(2x - 3)(x + 1)$  (D) $(2x + 3)(x - 1)$
>
> **Desmos:**
> - Line 1: `y = 2x^2 + 5x - 3`
> - Line 2: `y = (2x - 1)(x + 3)` — check if it overlaps
>
> > [!success]- Answer
> > **(A) $(2x - 1)(x + 3)$** — perfect overlap ✓
> >
> > **Quick verify:** $(2x-1)(x+3) = 2x^2 + 6x - x - 3 = 2x^2 + 5x - 3$ ✓

---

## Skill 8 — Circle Equations

> [!note] When to use
> Finding center, radius, or if a point lies on a circle.

### How to do it

1. Type the circle equation (any form):
   - Standard: `(x - 3)^2 + (y + 2)^2 = 25`
   - General: `x^2 + y^2 - 6x + 4y - 12 = 0`
2. Desmos graphs the circle
3. **Grey dots** appear at top and bottom (max/min $y$-values)
4. Click them → midpoint of top and bottom = center; distance = diameter

---

> [!question]- 8.1 Find center and radius from general form
> $x^2 + y^2 + 8x - 6y - 11 = 0$. What are the center and radius?
>
> **Desmos:** Type `x^2 + y^2 + 8x - 6y - 11 = 0`
> Click the top and bottom grey dots → find midpoint and distance
>
> > [!success]- Answer
> > Complete the square:
> > $(x^2 + 8x + 16) + (y^2 - 6y + 9) = 11 + 16 + 9$
> > $(x+4)^2 + (y-3)^2 = 36$
> > Center: $(-4, 3)$, Radius: $6$
> >
> > **Desmos verify:** Top of circle at $(-4, 9)$, bottom at $(-4, -3)$.
> > Midpoint $= (-4, 3)$ ✓. Distance $= 12$, so diameter $= 12$, radius $= 6$ ✓
> >
> > ⚠️ **Trap:** When completing the square: $(y - 6y)$ needs $(-6/2)^2 = 9$ added to BOTH sides. Students often add to one side only.

> [!question]- 8.2 Does a point lie on the circle?
> Does the point $(1, 5)$ lie on the circle $(x - 3)^2 + (y - 2)^2 = 13$?
>
> **Desmos:** Graph the circle and plot the point `(1, 5)`. If the point appears ON the circle, yes.
>
> > [!success]- Answer
> > $(1-3)^2 + (5-2)^2 = 4 + 9 = 13$ ✓ — **Yes**, the point lies on the circle.
> >
> > ⚠️ **Tip:** On the calculator, you could also use Verify mode: $(1-3)^2 + (5-2)^2 = 13$ → TRUE.

---

## Skill 9 — Domain Restrictions

> [!note] When to use
> Piecewise functions, restricted graphs, or any question about "the function is defined for..."

### How to do it

Use curly braces `{}` after the expression:
- `y = x^2 {x >= 0}` — only the right half of the parabola
- `y = 2x + 1 {-3 < x < 3}` — only between $x = -3$ and $x = 3$

### Piecewise functions
- `y = {x > 0: x^2, x <= 0: -x}`
  - When $x > 0$: parabola
  - When $x \leq 0$: line $y = -x$

---

> [!question]- 9.1 Piecewise graph
> Graph the piecewise function:
> $$f(x) = \begin{cases} 2x + 3 & \text{if } x < 1 \\ x^2 & \text{if } x \geq 1 \end{cases}$$
>
> **Desmos:** Type `y = {x < 1: 2x + 3, x >= 1: x^2}`
>
> > [!success]- Answer
> > At $x = 1$: left piece gives $2(1)+3 = 5$, right piece gives $1^2 = 1$.
> > There's a **jump** at $x = 1$ (from $5$ to $1$).
> >
> > ⚠️ **Tip:** Look for open/filled circles at the boundary. The filled circle (at $x = 1$) belongs to the $x^2$ branch since the condition is $x \geq 1$.

> [!question]- 9.2 Restricted domain for projectile
> A ball's height is $h(t) = -16t^2 + 48t + 4$ for $t \geq 0$. When does it hit the ground?
>
> **Desmos:** Type `y = -16x^2 + 48x + 4 {x >= 0}` → find where it crosses $y = 0$
>
> > [!success]- Answer
> > Click the $x$-intercept (the one where $x > 0$): $t \approx 3.08$ seconds
> >
> > **Exact:** $t = \frac{-48 \pm \sqrt{2304 + 256}}{-32} = \frac{-48 \pm \sqrt{2560}}{-32}$
> > $t \approx 3.08$ ✓ (taking the positive root)
> >
> > ⚠️ **Trap:** The domain restriction `{x >= 0}` prevents Desmos from showing the meaningless negative-time solution.

---

## Skill 10 — Built-in Statistics Functions

> [!note] When to use
> Quick stats calculations without opening a stats table.

### Available functions in Desmos

```
mean(1, 2, 3, 4)       → 2.5
median(1, 3, 5, 7)     → 4
stdev(1, 2, 3)          → 0.816...
stdevp(1, 2, 3)         → 0.816... (population SD)
total(1, 2, 3, 4)       → 10
min(3, 1, 4, 1)         → 1
max(3, 1, 4, 1)         → 4
sort(3, 8, 1, 6)        → [1, 3, 6, 8]
length([1, 2, 3])       → 3
```

### Lists

```
a = [1, 2, 3, 4, 5]       → defines a list
[1, 2...100]                → integers 1 to 100
total([1, 2...100])         → sum of 1 + 2 + ... + 100 = 5050
mean([85, 90, 78, 92])     → average of the list
```

---

> [!question]- 10.1 Quick mean calculation
> What is the mean of $\{12, 18, 22, 25, 31, 42\}$?
>
> **Desmos:** Type `mean(12, 18, 22, 25, 31, 42)`
>
> > [!success]- Answer
> > $\frac{150}{6} = 25$

> [!question]- 10.2 Find the missing value using unknowns in stats functions
> The median of $\{2, 5, x, 11, 14\}$ (already in order) is $8$. What is $x$?
>
> **Desmos:** Type `median(2, 5, x, 11, 14) ~ 8` (regression trick!)
>
> > [!success]- Answer
> > The median of 5 sorted values is the 3rd value, so $x = 8$.
> >
> > ⚠️ **Tip:** You can also just reason: median of 5 values is the middle one. The data is sorted, so the middle value IS $x$. Therefore $x = 8$.

---

# Part 4 — Advanced Tricks for 750+ Scorers

---

## Trick 1 — Convert Decimal to Fraction

When Desmos shows a decimal answer, look for the **fraction button** that appears to the left of the expression value. Click it to convert.

Example: If Desmos shows $0.8\overline{3}$, clicking the button gives $\frac{5}{6}$.

---

## Trick 2 — Matching Answer Choices with $\pi$ or Radicals

If answer choices are in terms of $\pi$:
- Type your expression divided by $\pi$: e.g., `area/pi`
- If the result is a clean number (like $16$), the answer is $16\pi$

If answer choices have $\sqrt{3}$:
- Divide by $\sqrt{3}$: `result/sqrt(3)`
- If you get a clean number, that's the coefficient

---

## Trick 3 — Finding Factors of Polynomials

1. Graph the polynomial: `y = x^3 - 6x^2 + 11x - 6`
2. Click $x$-intercepts: $x = 1, 2, 3$
3. Factors: $(x-1)(x-2)(x-3)$

Faster than synthetic division or factoring by grouping.

---

## Trick 4 — Point Coordinates

You can extract coordinates of a point:
- `(5, 9).x` → gives $5$
- `(5, 9).y` → gives $9$

Useful when a point is calculated from a formula and you need just one coordinate.

---

## Trick 5 — Number of Solutions Visually

| What you see | How many solutions |
|---|---|
| Graphs don't touch | **0 solutions** |
| Graphs touch at exactly 1 point | **1 solution** (tangent) |
| Graphs cross at 2 points | **2 solutions** |
| Graphs perfectly overlap | **Infinite solutions** |

For quadratics: graph `y = ax^2 + bx + c` and count $x$-intercepts.

---

# Part 5 — When NOT to Use Desmos

> [!warning] Desmos is powerful, but not always the fastest tool

| Situation | Better Tool |
|---|---|
| Simple arithmetic ($3 \times 7 + 2$) | Mental math or FX-991CW |
| Polynomial roots | FX-991CW polynomial solver (faster!) |
| System of linear equations | FX-991CW simultaneous solver (faster!) |
| Plugging in to verify | FX-991CW verify mode (faster!) |
| "What does the slope represent?" | Your brain (concept question) |
| Simple $2x + 5 = 11$ | By hand (3 seconds) |

> [!tip] The Balanced Strategy
> **Understand the math** → use Desmos/calculator to **execute faster** and **verify answers**.
> Desmos solves ~70% of SAT math problems. But you still need conceptual understanding to know WHAT to type.

---

# Part 6 — Desmos vs. FX-991CW Decision Matrix

| Problem Type | Desmos | FX-991CW | Winner |
|---|---|---|---|
| Visualize functions | ✅ graphs instantly | ❌ no graphing | **Desmos** |
| Find intersection | ✅ click grey dot | ✅ simultaneous solver | **Tie** (CW faster for linear) |
| Quadratic roots | ✅ click $x$-intercepts | ✅ polynomial solver | **CW** (exact roots instantly) |
| Regression / curve fit | ✅ `y_1 ~ ...` | ✅ Statistics mode | **Desmos** (more flexible) |
| Verify an answer | ❌ no verify feature | ✅ TRUE/FALSE | **CW** |
| Inequalities (shading) | ✅ visual shading | ✅ solution interval | **Desmos** (visual) |
| Sliders for unknowns | ✅ dynamic | ❌ | **Desmos** |
| Quick arithmetic | ❌ overkill | ✅ fast | **CW** |
| Stats (mean, SD) | ✅ `mean()`, `stdev()` | ✅ 1-Variable mode | **Tie** |
| Proportions | ❌ overkill | ✅ Ratio mode | **CW** |
| Equivalent expressions | ✅ graph overlay | ❌ | **Desmos** |
| Circle center/radius | ✅ graph + click | ❌ (manual algebra) | **Desmos** |

---

# Part 7 — Practice Simulation (Timed)

> **🕐 Do these 10 questions in 15 minutes using Desmos.**
> For each, write down WHAT you typed into Desmos.

---

> [!question]- SIM-1. 🕐
> Solve: $x^2 - 7x + 10 = 0$. What is the greater solution?
>
> > [!success]- Answer
> > Graph `y = x^2 - 7x + 10` → click the right $x$-intercept: $x = 5$
> > (Or use CW polynomial solver — faster for this one)

> [!question]- SIM-2. 🕐
> For what value of $k$ does $y = kx + 3$ pass through $(4, 11)$?
>
> > [!success]- Answer
> > - Type `y = kx + 3` → slider for $k$
> > - Plot `(4, 11)`
> > - Drag until line hits the point: $k = 2$
> > (Or just compute: $11 = 4k + 3 \Rightarrow k = 2$)

> [!question]- SIM-3. 🕐
> Data: $(1, 4), (2, 7), (3, 10), (4, 13)$. What is the slope of the line of best fit?
>
> > [!success]- Answer
> > Table → enter data → type `y_1 ~ mx_1 + b`
> > $m = 3$, $b = 1$. **Slope = 3**

> [!question]- SIM-4. 🕐
> What is the vertex of $y = -x^2 + 6x - 5$?
>
> > [!success]- Answer
> > Graph it → click vertex: $(3, 4)$

> [!question]- SIM-5. 🕐
> How many solutions does $|x - 3| = 2x + 1$ have?
>
> > [!success]- Answer
> > Graph `y = abs(x - 3)` and `y = 2x + 1` → count intersections: **1 solution** (at $x = \frac{2}{3}$)

> [!question]- SIM-6. 🕐
> Which point is in the solution set of $y \leq x + 4$ AND $y > -2x + 1$?
> (A) $(0, 0)$  (B) $(-3, 2)$  (C) $(2, 7)$  (D) $(1, 3)$
>
> > [!success]- Answer
> > Graph both inequalities → plot points → **(D) $(1, 3)$** is in the overlap.
> > Check: $3 \leq 5$ ✓ and $3 > -1$ ✓

> [!question]- SIM-7. 🕐
> The equation $(3x + a)(2x + b) = 6x^2 + cx + 10$ is true for all $x$. If $a$ and $b$ are positive, what is $c$?
>
> > [!success]- Answer
> > **This problem is underdetermined — Desmos regression alone is unreliable here.**
> >
> > Expand: $(3x+a)(2x+b) = 6x^2 + (3b+2a)x + ab$
> >
> > Match coefficients: $ab = 10$ and $c = 3b + 2a$
> >
> > All positive integer pairs $(a, b)$ with $ab = 10$:
> >
> > | $a$ | $b$ | $c = 3b + 2a$ |
> > |---|---|---|
> > | 1 | 10 | 32 |
> > | 2 | 5 | **19** |
> > | 5 | 2 | 16 |
> > | 10 | 1 | 23 |
> >
> > On the SAT, the answer choices will contain exactly one of $\{16, 19, 23, 32\}$ — pick it.
> >
> > ⚠️ **Desmos trap:** Regression converges to whichever pair it finds first (depends on starting values). You may get $c=19$ or $c=23$ or any other valid answer. **Do not rely on Desmos for underdetermined problems like this — use the algebraic approach.**

> [!question]- SIM-8. 🕐
> Center of the circle $x^2 + y^2 - 10x + 4y + 13 = 0$?
>
> > [!success]- Answer
> > Graph it → click top/bottom dots → midpoint = center: $(5, -2)$
> > **Algebra verify:** $(x-5)^2 + (y+2)^2 = 25 + 4 - 13 = 16$. Center $(5, -2)$ ✓

> [!question]- SIM-9. 🕐
> $f(x) = 3 \cdot 2^x$. For what value of $x$ does $f(x) = 96$?
>
> > [!success]- Answer
> > Graph `y = 3*2^x` and `y = 96` → click intersection: $x = 5$
> > **Check:** $3 \cdot 2^5 = 3 \cdot 32 = 96$ ✓

> [!question]- SIM-10. 🕐
> The mean of five numbers is 20. Four of them are $15, 18, 22, 25$. What is the fifth?
>
> > [!success]- Answer
> > Type: `mean(15, 18, 22, 25, x) ~ 20`
> > $x = 20$ (since $15+18+22+25 = 80$, need $100$ total, so $x = 20$)

---

# Quick Reference Card (Print This!)

> [!abstract] Desmos Cheat Sheet for Test Day
>
> **Graphing:** Type equations directly (any form). Click grey dots for coordinates.
>
> **Solve anything:** Graph both sides → click intersection. Or use `LHS ~ RHS`.
>
> **Find vertex:** Graph quadratic → click vertex dot.
>
> **Sliders:** Use for "find $k$" questions. Type equation with letter → "add slider" → drag.
>
> **Regression:** Table + `y_1 ~ model` finds constants instantly.
>
> **Equivalent expressions:** Graph both → see if they overlap.
>
> **Inequalities:** Type with `>=`, `<=`, `>`, `<` → shading shows solution region.
>
> **Stats:** `mean()`, `median()`, `stdev()`, `total()` work directly.
>
> **Domain:** Add `{condition}` after expression: `y = x^2 {x >= 0}`
>
> **Piecewise:** `y = {x > 0: x^2, x <= 0: -x}`
>
> **Subscripts:** Always use `x_1`, NOT `x1`. Underscore matters!
>
> **Parentheses:** When in doubt, add them. `2(x+3)^2` ≠ `2x+3^2`

---

*Total exercises: ~35 | Estimated completion time: 2–3 hours*
*Start with Skills 1–4 (core), then move to Skills 5–10 (advanced), then the simulation.*
*By test day, every technique here should feel automatic.*
