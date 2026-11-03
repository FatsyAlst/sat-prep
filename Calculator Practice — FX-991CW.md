---
type: practice
tags: [calculator, practice, fx-991cw, module-2, hard]
---

# Calculator Practice — FX-991CW

> Custom SAT Math Module 2 questions designed for **750 → 800** push.
> Every exercise is at **Module 2 hard difficulty** — the level that separates 750 from 800.
> Each question is tagged with the **calculator feature** that makes it fastest and a **⚠️ Trap Alert** for where careless mistakes happen.

---

# FX-991CW Quick Reference

> [!info]- Calculator Overview — 13 Apps on HOME Screen
>
> | App | SAT Use | Access |
> |---|---|---|
> | **Calculate** | General computation, f(x)/g(x) definitions | HOME → 1 |
> | **Equation/Inequality** | Polynomial (deg 2–4), Simultaneous (2–4 unknowns), Solver, Inequality | HOME → 2 |
> | **Table** | Generate (x, f(x)) tables, compare f(x) vs g(x) | HOME → 3 |
> | **Statistics** | 1-Var stats, Regression (Linear, Quad, Log, Exp, Power) | HOME → 4 |
> | **Distribution** | Normal/Binomial/Poisson probabilities | HOME → 5 |
> | **Complex** | Complex number arithmetic | HOME → 6 |
> | **Base-N** | Number base conversions (rarely SAT-relevant) | HOME → 7 |
> | **Matrix** | Matrix operations (up to 4×4) | HOME → 8 |
> | **Vector** | Vector arithmetic | HOME → 9 |
> | **Ratio** | Solve proportions instantly | HOME → 10 |
> | **Spreadsheet** | Mini spreadsheet (up to 45 cells) | HOME → 11 |
> | **Math Box** | Factorization, random integers | HOME → 12 |
> | **Verify** | TRUE/FALSE checker for equations and inequalities | HOME → 13 |
>
> **CRITICAL differences from FX-991EX:**
> - ❌ **NO CALC button** — the CW does NOT have a CALC key
> - ❌ **NO SHIFT+SOLVE in Calculate mode** — use the Equation/Inequality app's Numerical Solver instead
> - ✅ **Polynomial solver goes up to degree 4** (not just degree 3)
> - ✅ **Simultaneous equations handles up to 4 unknowns** (not just 3)
> - ✅ **FORMAT button** replaces S⇔D — press it to toggle between exact and decimal forms
> - ✅ **SHIFT+EXE** gives the decimal approximation (≈) of exact results
> - ✅ **Define f(x) and g(x)** in Calculate mode — they carry over to Table mode
> - ✅ **Ratio app** solves proportions in one step
> - ✅ **Inequality solver** in the Equation/Inequality app

---

# Section A — Polynomial Solver (Degree 2, 3, and 4)

> **Calculator path:** HOME → Equation/Inequality → Polynomial → select degree (2, 3, or **4**)
> **What changed from the old doc:** This calculator handles **degree 4** polynomials (quartics), not just up to 3.

### How to use

1. Press **HOME** → select **Equation/Inequality**
2. Choose **Polynomial** → select degree (2, 3, or 4)
3. Enter coefficients in order: for $ax^2 + bx + c = 0$ enter $a$, $b$, $c$
4. Press **=** to get all roots (real and complex)
5. Press **FORMAT** to toggle between exact (surd/fraction) and decimal output

---

> [!question]- A1. Find $k$ for no real solutions
> For what value of $k$ does $3x^2 - 12x + k = 0$ have **no** real solutions?
> (A) $k = 11$  (B) $k = 12$  (C) $k = 13$  (D) $k = 14$
>
> **Strategy:** No real solutions ↔ discriminant $< 0$: $b^2 - 4ac < 0$
> **Calculator:** Try each $k$ in Polynomial degree 2 → $a=3$, $b=-12$, $c=k$. The one that gives complex roots wins.
>
> > [!success]- Answer
> > $\Delta = 144 - 12k$. We need $\Delta < 0$, i.e., $k > 12$.
> > $k = 12$: $\Delta = 0$ (exactly one solution — not "no solutions").
> > $k = 13$: $\Delta = 144 - 156 = -12 < 0$ ✓
> > **(C) $k = 13$**
> >
> > ⚠️ **Trap:** $k = 12$ gives the boundary case (one repeated root), NOT no solutions. "No real solutions" means $\Delta < 0$, **strictly less than**. The SAT puts the boundary value as a trap answer.

> [!question]- A2. Quadratic in disguise — exponential substitution
> If $9^x - 10 \cdot 3^x + 9 = 0$, what is the sum of all values of $x$?
>
> **Strategy:** $9^x = (3^x)^2$. Let $u = 3^x$ → $u^2 - 10u + 9 = 0$
> **Calculator:** Polynomial degree 2 → $a=1$, $b=-10$, $c=9$
>
> > [!success]- Answer
> > $u = 1$ or $u = 9$
> > $3^x = 1 \Rightarrow x = 0$
> > $3^x = 9 \Rightarrow x = 2$
> > Sum $= 0 + 2 = 2$
> >
> > ⚠️ **Trap:** Don't give $u = 1$ and $u = 9$ as the answer (sum 10). You must convert back to $x$. Also: $3^x = 1$ gives $x = 0$, not $x = 1$.

> [!question]- A3. Degree-4 polynomial — the CW advantage
> What are the real solutions to $x^4 - 5x^2 + 4 = 0$?
>
> **Calculator:** Polynomial degree 4 → $a=1$, $b=0$, $c=-5$, $d=0$, $e=4$
>
> > [!success]- Answer
> > Roots: $x = -2, -1, 1, 2$
> >
> > **Manual check:** Let $u = x^2$: $u^2 - 5u + 4 = 0 \Rightarrow (u-1)(u-4) = 0$
> > $u = 1 \Rightarrow x = \pm 1$, $u = 4 \Rightarrow x = \pm 2$
> >
> > ⚠️ **Trap:** The degree-4 solver gives ALL four roots directly — no substitution needed. This can save 60+ seconds on test day. Most students don't even know the CW can do degree 4.

> [!question]- A4. Finding $k$ for exactly one real solution (discriminant = 0)
> The equation $k x^2 + 8x + 2 = 0$ has exactly one real solution. If $k > 0$, what is the value of $k$?
>
> **Calculator approach:** Try values in Polynomial degree 2 until you see a double root.
>
> > [!success]- Answer
> > $\Delta = 64 - 8k = 0 \Rightarrow k = 8$
> > **Verify:** Polynomial → $a=8$, $b=8$, $c=2$ → double root at $x = -\frac{1}{2}$ ✓
> >
> > ⚠️ **Trap:** "Exactly one solution" means discriminant = 0. Also, the question says $k > 0$; if it didn't, you'd need to consider $k = 0$ (which makes it linear with one solution too, but that's a different case).

> [!question]- A5. Factoring with abstract coefficients — find $b$
> If $3x^2 + bx - 8 = 0$ has solutions $x = \frac{2}{3}$ and $x = -4$, what is $b$?
>
> **Calculator strategy:** Use Vieta's to find $b$:
> Sum of roots $= -b/a$, so $\frac{2}{3} + (-4) = -\frac{b}{3}$
>
> > [!success]- Answer
> > $\frac{2}{3} - 4 = -\frac{10}{3} = -\frac{b}{3}$, so $b = 10$
> >
> > **Verify with Polynomial:** $a=3$, $b=10$, $c=-8$ → roots $\frac{2}{3}$ and $-4$ ✓
> >
> > ⚠️ **Trap:** Vieta's formula: sum $= -b/a$ (note the negative). If you forget the negative sign, you get $b = -10$.

> [!question]- A6. Quadratic with radical solutions — vertex from roots
> The solutions to $2x^2 - 12x + 7 = 0$ are $x = p$ and $x = q$. What is the $x$-coordinate of the vertex of $y = 2x^2 - 12x + 7$?
>
> **Calculator:** Polynomial degree 2 → $a=2$, $b=-12$, $c=7$ → get roots. Vertex $x = \frac{p+q}{2}$.
>
> > [!success]- Answer
> > Vertex $x$-coordinate $= -b/(2a) = 12/4 = 3$
> > (You don't even need the roots — the vertex formula is faster.)
> >
> > **But verify with calculator roots:** $x = \frac{12 \pm \sqrt{144-56}}{4} = \frac{12 \pm \sqrt{88}}{4}$
> > Average $= 12/4 = 3$ ✓
> >
> > ⚠️ **Trap:** The vertex $x$-coordinate is always the **average** of the roots, regardless of whether roots are rational or irrational.

> [!question]- A7. Cubic — one real root is given, find the other
> One solution to $x^3 - 7x^2 + 14x - 8 = 0$ is $x = 1$. What is the product of the other two solutions?
>
> **Calculator:** Polynomial degree 3 → $a=1$, $b=-7$, $c=14$, $d=-8$
>
> > [!success]- Answer
> > Roots: $x = 1, 2, 4$
> > Product of "other two" $= 2 \times 4 = 8$
> >
> > **By Vieta's:** Product of ALL three roots $= -d/a = 8$. Since one root is $1$, the product of the other two is $8/1 = 8$.
> >
> > ⚠️ **Trap:** For a cubic $ax^3 + bx^2 + cx + d = 0$: product of all roots $= -d/a$ (note the negative!). If $d$ were positive $8$, the product would be $-8$.

> [!question]- A8. "How many real solutions?" — the $x$-intercept counter
> How many distinct real solutions does $x^4 - 8x^2 + 12 = 0$ have?
>
> **Calculator:** Polynomial degree 4 → $a=1$, $b=0$, $c=-8$, $d=0$, $e=12$
>
> > [!success]- Answer
> > Let $u = x^2$: $u^2 - 8u + 12 = 0 \Rightarrow (u - 2)(u - 6) = 0$
> > $u = 2 \Rightarrow x = \pm\sqrt{2}$, $u = 6 \Rightarrow x = \pm\sqrt{6}$
> > **4 distinct real solutions**
> >
> > The calculator confirms: 4 real roots.
> >
> > ⚠️ **Trap:** If one of the $u$-values were negative (e.g., $u = -3$), then $x^2 = -3$ has no real solutions — only 2 real roots total. Always check the sign of $u$.

> [!question]- A9. Difference of squares in disguise
> What are the solutions to $\left(\frac{x}{2} - 3\right)^2 = 49$?
>
> **Strategy:** Recognize $(A)^2 = 49 \Rightarrow A = \pm 7$.
>
> > [!success]- Answer
> > $\frac{x}{2} - 3 = 7 \Rightarrow x = 20$
> > $\frac{x}{2} - 3 = -7 \Rightarrow x = -8$
> >
> > **Calculator verify:** Expand to $\frac{x^2}{4} - 3x + 9 - 49 = 0 \Rightarrow x^2 - 12x - 160 = 0$
> > Polynomial: $a=1$, $b=-12$, $c=-160$ → roots $20$ and $-8$ ✓
> >
> > ⚠️ **Trap:** Taking the square root of both sides gives TWO cases ($+$ and $-$). Many students only do the positive case and miss $x = -8$.

> [!question]- A10. Exponential min/max from completed-square form
> $f(x) = (x - 4)^2 + 3$. What is the minimum value of $2^{f(x)}$?
>
> > [!success]- Answer
> > $f(x) \geq 3$ for all $x$ (minimum at $x=4$).
> > Since $2^t$ is increasing, $2^{f(x)} \geq 2^3 = 8$.
> > **Minimum value: $8$**
> >
> > **Calculator verify:** Use Table mode with $f(x) = 2^{(x-4)^2+3}$ to confirm the minimum near $x = 4$.
> >
> > ⚠️ **Trap:** The minimum of $2^{f(x)}$ is NOT $2^0 = 1$ — it's $2^{\min f(x)}$. The exponent's minimum is $3$, not $0$.

---

# Section B — Simultaneous Equations (2, 3, and 4 Unknowns)

> **Calculator path:** HOME → Equation/Inequality → Simultaneous Equations → select number of unknowns (2, 3, or **4**)
> **What changed:** The CW handles **4 unknowns**, not just 3. For the SAT, 2 and 3 unknowns are most common, but 4-unknown capability means you can solve non-standard setups.

### How to use

1. **HOME** → **Equation/Inequality** → **Simultaneous Equations**
2. Choose number of unknowns (2, 3, or **4**)
3. Enter coefficients: $a_1 x + b_1 y = c_1$, etc.
4. Press **=** → solution appears
5. If "No Solution" or "Infinite Solutions" appears — that IS the answer

---

> [!question]- B1. No-solution system — find the constant
> The system below has no solution. What is the value of $a$?
> $$\begin{cases} 3x - 5y = 8 \\ 9x + ay = 15 \end{cases}$$
>
> **Strategy:** No solution ↔ parallel lines ↔ $\frac{3}{9} = \frac{-5}{a}$ but $\frac{8}{15} \neq \frac{-5}{a}$ (different intercepts)
>
> > [!success]- Answer
> > $\frac{3}{9} = \frac{-5}{a} \Rightarrow \frac{1}{3} = \frac{-5}{a} \Rightarrow a = -15$
> >
> > **Verify:** Simultaneous → $[3, -5, 8]$ and $[9, -15, 15]$ → "No Solution" ✓
> >
> > ⚠️ **Trap:** The ratio must match for the coefficients of $x$ AND $y$. It's $\frac{a_1}{a_2} = \frac{b_1}{b_2}$. The sign on $a = -15$ is critical — if you forget the negative from $-5$, you get $a = 15$ (wrong).

> [!question]- B2. Infinite solutions — find $k$ (harder version)
> For what value of $k$ does this system have infinitely many solutions?
> $$\begin{cases} 2x + 6y = 10 \\ kx + 3y = 5 \end{cases}$$
>
> > [!success]- Answer
> > Infinite solutions ↔ the equations are proportional.
> > Second equation times $2$: $2kx + 6y = 10$. Must equal the first: $2x + 6y = 10$.
> > So $2k = 2 \Rightarrow k = 1$.
> >
> > **Verify:** $[2, 6, 10]$ and $[1, 3, 5]$ → "Infinite Solutions" ✓
> >
> > ⚠️ **Trap:** For infinite solutions, ALL three ratios must match: $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$. If only the first two match, it's no solution (parallel, different intercept).

> [!question]- B3. System from word problem — mixture
> A chemist mixes a 20% acid solution with a 50% acid solution to create 600 mL of a 30% acid solution. How many mL of the 20% solution are used?
>
> **Setup:** $x + y = 600$ and $0.20x + 0.50y = 0.30(600) = 180$
> **Calculator:** Clear fractions: $20x + 50y = 18000$, so simultaneous → $[1, 1, 600]$ and $[20, 50, 18000]$
>
> > [!success]- Answer
> > $x = 400$, $y = 200$
> > **400 mL of the 20% solution**
> >
> > ⚠️ **Trap:** The percentages must go on the AMOUNTS, not on the volumes separately. $0.20 \times x + 0.50 \times y = 0.30 \times 600$. Many students write $0.20 + 0.50 = 0.30$ (nonsense).

> [!question]- B4. Three-variable system — SAT-style
> $$\begin{cases} x + y + z = 15 \\ 2x - y + z = 8 \\ x + 2y - z = 10 \end{cases}$$
> What is $x + z$?
>
> **Calculator:** Simultaneous 3 unknowns → enter rows
>
> > [!success]- Answer
> > $x = 3, y = 5, z = 7$
> > $x + z = 10$
> >
> > ⚠️ **Trap:** Read what the question asks: $x + z$, not just $x$ or $z$ individually. For 3-variable systems, the calculator is drastically faster than elimination by hand.

> [!question]- B5. System where they ask for an expression (no unique solution needed)
> If $3x + 4y = 18$ and $6x + 8y = k$, for what value of $k$ does the system have infinitely many solutions?
>
> > [!success]- Answer
> > The second equation must be a multiple of the first.
> > $6x + 8y = 2(3x + 4y) = 2(18) = 36$
> > $k = 36$
> >
> > ⚠️ **Trap:** Don't try to solve for $x$ and $y$ — you can't (one equation, two unknowns). Recognize that the second equation is $2 \times$ the first.

> [!question]- B6. System with one linear, one quadratic — find the number of solutions
> How many solutions does this system have?
> $$\begin{cases} y = x^2 - 4x + 5 \\ y = 2x - 3 \end{cases}$$
>
> **Strategy:** Set equal: $x^2 - 4x + 5 = 2x - 3 \Rightarrow x^2 - 6x + 8 = 0$
> **Calculator:** Polynomial degree 2 → $a=1$, $b=-6$, $c=8$
>
> > [!success]- Answer
> > $x = 2$ or $x = 4$ → $\Delta = 36 - 32 = 4 > 0$ → **2 solutions**
> > Points: $(2, 1)$ and $(4, 5)$
> >
> > ⚠️ **Trap:** The simultaneous equation solver on the CW only handles LINEAR systems. For a linear-quadratic system, you must substitute and reduce to a polynomial, THEN use the polynomial solver.

> [!question]- B7. System hidden in a word problem — rates
> A boat travels 60 km upstream in 4 hours and 60 km downstream in 3 hours. What is the speed of the current?
>
> **Setup:** Let $b$ = boat speed, $c$ = current speed.
> Upstream: $(b - c) \times 4 = 60 \Rightarrow b - c = 15$
> Downstream: $(b + c) \times 3 = 60 \Rightarrow b + c = 20$
>
> **Calculator:** Simultaneous → $[1, -1, 15]$ and $[1, 1, 20]$
>
> > [!success]- Answer
> > $b = 17.5$, $c = 2.5$
> > **Current speed: 2.5 km/h**
> >
> > ⚠️ **Trap:** Upstream means you SUBTRACT the current (it slows you down). Downstream means you ADD. If you swap them, you get the answers swapped too.

> [!question]- B8. Minimum value of $b$ for two real intersections
> For what value of $b$ does the line $y = bx$ first become tangent to the parabola $y = x^2 + 1$?
>
> **Strategy:** Set $bx = x^2 + 1 \Rightarrow x^2 - bx + 1 = 0$. Tangent ↔ $\Delta = 0$.
>
> > [!success]- Answer
> > $\Delta = b^2 - 4 = 0 \Rightarrow b = \pm 2$
> > For two intersections: $b^2 > 4$, i.e., $b > 2$ or $b < -2$.
> > **Tangent when $b = 2$ (or $b = -2$)**
> >
> > **Verify:** Polynomial → $a=1$, $b=-2$, $c=1$ → double root at $x=1$ ✓
> >
> > ⚠️ **Trap:** "First becomes tangent" means the boundary case $\Delta = 0$. Two intersections need $\Delta > 0$, which means $|b| > 2$. The SAT may ask for the minimum POSITIVE value of $b$, which is $2$.

---

# Section C — Inequality Solver (NEW Feature!)

> **Calculator path:** HOME → Equation/Inequality → Inequality
> **Why this matters:** The CW can solve quadratic and linear inequalities directly — gives you the solution interval. Most students don't know this app exists.

### How to use

1. **HOME** → **Equation/Inequality** → **Inequality**
2. Select the inequality type (e.g., $ax^2 + bx + c > 0$)
3. Enter coefficients
4. Press **=** → the calculator shows the solution interval (e.g., $x < -2$ or $x > 3$)

---

> [!question]- C1. Quadratic inequality — Domain of a square root
> What is the domain of $f(x) = \sqrt{x^2 - 5x + 6}$?
>
> **Strategy:** Need $x^2 - 5x + 6 \geq 0$
> **Calculator:** Inequality → $a=1$, $b=-5$, $c=6$, type $\geq 0$
>
> > [!success]- Answer
> > Factor: $(x-2)(x-3) \geq 0$
> > Solution: $x \leq 2$ or $x \geq 3$
> >
> > The calculator gives the interval directly.
> >
> > ⚠️ **Trap:** The parabola opens up ($a > 0$), so it's $\geq 0$ OUTSIDE the roots. Many students pick "between" the roots ($2 \leq x \leq 3$), which is the region where the expression is $\leq 0$.

> [!question]- C2. Range of $k$ for two real solutions
> For what values of $k$ does $2x^2 + kx + 8 = 0$ have two distinct real solutions?
>
> **Strategy:** Need $\Delta > 0$: $k^2 - 64 > 0$
> **Calculator:** Inequality → $a=1$, $b=0$, $c=-64$, variable is $k$, type $> 0$
>
> > [!success]- Answer
> > $k^2 > 64 \Rightarrow k < -8$ or $k > 8$
> >
> > ⚠️ **Trap:** Two DISTINCT solutions means $\Delta > 0$ (strictly). If the question said "at least one real solution," it would be $\Delta \geq 0$, so $k \leq -8$ or $k \geq 8$. The boundary matters!

> [!question]- C3. Quadratic inequality from a word problem
> A ball's height is modeled by $h(t) = -5t^2 + 30t + 2$ (meters, seconds). During what time interval is the ball above 37 meters?
>
> **Strategy:** $-5t^2 + 30t + 2 > 37 \Rightarrow -5t^2 + 30t - 35 > 0 \Rightarrow t^2 - 6t + 7 < 0$
> **Calculator:** Inequality → $a=1$, $b=-6$, $c=7$, type $< 0$
>
> > [!success]- Answer
> > Roots: $t = 3 \pm \sqrt{2} \approx 1.59$ and $4.41$
> > Ball above 37 m for $3 - \sqrt{2} < t < 3 + \sqrt{2}$ (roughly $1.59 < t < 4.41$)
> >
> > ⚠️ **Trap:** You must divide by $-5$ and FLIP the inequality: $> 0$ becomes $< 0$. If you forget to flip, you get the complement interval (ball BELOW 37 m).

> [!question]- C4. System of linear inequalities — find valid integer values
> How many positive integer values of $x$ satisfy BOTH $3x - 2 > 7$ AND $5x + 1 < 31$?
>
> **By hand (fast):** $3x > 9 \Rightarrow x > 3$ and $5x < 30 \Rightarrow x < 6$
>
> > [!success]- Answer
> > $3 < x < 6$ → positive integers: $x = 4, 5$
> > **2 values**
> >
> > ⚠️ **Trap:** $x > 3$ means $x = 3$ is NOT included. And $x < 6$ means $x = 6$ is NOT included. Boundary values are excluded with strict inequalities.

> [!question]- C5. Absolute value inequality
> Solve: $|3x - 6| \leq 12$
>
> **Strategy:** $-12 \leq 3x - 6 \leq 12 \Rightarrow -6 \leq 3x \leq 18 \Rightarrow -2 \leq x \leq 6$
>
> > [!success]- Answer
> > $-2 \leq x \leq 6$
> >
> > **Verify with calculator:** Try $x = -2$: $|{-6 - 6}| = 12 \leq 12$ TRUE ✓
> > Try $x = -3$: $|{-9 - 6}| = 15 \leq 12$ FALSE ✓
> >
> > ⚠️ **Trap:** $|A| \leq B$ means $-B \leq A \leq B$ (AND). $|A| \geq B$ means $A \leq -B$ OR $A \geq B$ (OR). Students routinely mix these up.

---

# Section D — Numerical Solver

> **Calculator path:** HOME → Equation/Inequality → Solver
> **Why this matters:** Solves ANY equation of the form $f(x) = 0$ numerically, even when you can't factor or solve algebraically. It finds one root near a starting guess.

### How to use

1. **HOME** → **Equation/Inequality** → **Solver**
2. Enter the equation in the form **LHS = RHS** (or $f(x) = 0$)
3. Provide a starting guess (the calculator iterates from there)
4. Press **=** → you get a numerical root

### ⚠️ Important: The solver finds ONE root near your starting guess. If there are multiple roots, you must try different starting values.

---

> [!question]- D1. Equation with no clean algebraic solution
> Solve $x \cdot 2^x = 12$ for $x > 0$.
>
> **Calculator:** Solver → $x \cdot 2^x - 12 = 0$, guess $x = 2$
>
> > [!success]- Answer
> > $x \approx 2.27$
> > (Verify: $2.27 \times 2^{2.27} \approx 2.27 \times 4.83 \approx 10.96$ — close. More precisely $x \approx 2.263$)
> >
> > ⚠️ **Trap:** On the SAT, if the answer choices are integers or simple fractions and none match your solver output, you've set up the equation wrong. The solver's power is confirming your setup.

> [!question]- D2. Compound interest — when does it double?
> An account earns 6% annual interest compounded annually. After how many complete years will an initial deposit first more than double?
>
> **Strategy:** $1.06^t > 2$. Use Solver: $1.06^t - 2 = 0$
> **Calculator:** Solver → guess $t = 10$
>
> > [!success]- Answer
> > $t \approx 11.90$. First COMPLETE year: **$t = 12$**
> >
> > **Verify:** $1.06^{11} \approx 1.898$ (not doubled). $1.06^{12} \approx 2.012$ (doubled!) ✓
> >
> > ⚠️ **Trap:** "Complete years" → round UP. The mathematical solution is $11.9$, but you need $t = 12$ complete years for the amount to actually exceed double.

> [!question]- D3. Exponential decay — when does it reach a threshold?
> The mass (in grams) of a radioactive substance is modeled by $M(t) = 200 \cdot (0.85)^t$, where $t$ is in days. After how many complete days is the mass first below 50 grams?
>
> **Calculator:** Solver → $200 \cdot 0.85^t - 50 = 0$, guess $t = 8$
>
> > [!success]- Answer
> > $0.85^t = 0.25 \Rightarrow t = \frac{\ln(0.25)}{\ln(0.85)} \approx 8.53$
> > First complete day below 50 g: **$t = 9$**
> >
> > ⚠️ **Trap:** "First BELOW" → round UP. At $t = 8$: $M = 200(0.85)^8 \approx 54.4$ g (still above). At $t = 9$: $M \approx 46.3$ g (below!) ✓

> [!question]- D4. Finding where two nonlinear functions intersect
> At what positive value of $x$ do $f(x) = \ln(x+1)$ and $g(x) = \sqrt{x}$ intersect?
>
> **Calculator:** Solver → $\ln(x+1) - \sqrt{x} = 0$, guess $x = 3$
>
> > [!success]- Answer
> > $x \approx 3.51$
> > The SAT would give this as a multiple-choice with rounded options.
> >
> > ⚠️ **Trap:** On the SAT, transcendental equations like this almost always appear as multiple-choice. Use the solver to distinguish between close answer choices.

> [!question]- D5. Polynomial that resists factoring
> What is the positive real solution to $x^3 + 2x = 10$?
>
> **Calculator:** Solver → $x^3 + 2x - 10 = 0$, guess $x = 2$
>
> > [!success]- Answer
> > $x \approx 1.82$
> >
> > Alternatively, use Polynomial degree 3: $a=1$, $b=0$, $c=2$, $d=-10$ → gives exact roots.
> >
> > ⚠️ **Trap:** The polynomial solver might be better here since it finds ALL roots, not just one near your guess.

---

# Section E — Table Mode

> **Calculator path:** HOME → Table
> **Key upgrade:** Define $f(x)$ and $g(x)$ in Calculate mode first — they carry into Table mode automatically.

### How to use

1. **HOME** → **Table**
2. Enter $f(x) = ... $ (and optionally $g(x) = ...$)
3. Set **Start**, **End**, **Step** values
4. Browse the table; look for zeros, intersections, or max/min

### Pro tip: Define f(x) in Calculate mode

1. In **Calculate mode**, type $f(x) = 3x^2 - 2x + 1$ and press **=** (this stores the function)
2. Switch to **Table mode** — $f(x)$ is already loaded
3. This saves re-entering complex functions

---

> [!question]- E1. Reading transformations from a table
> The table below shows values of $g(x)$. If $g(x) = f(x - 2) + 3$ and $g(5) = 10$, what is $f(3)$?
>
> | $x$ | $g(x)$ |
> |---|---|
> | 3 | 4 |
> | 5 | 10 |
> | 7 | 22 |
>
> > [!success]- Answer
> > $g(5) = f(5 - 2) + 3 = f(3) + 3 = 10$
> > $f(3) = 7$
> >
> > ⚠️ **Trap:** $f(x - 2)$ shifts the graph RIGHT by 2 (not left). And the $+3$ shifts UP. To undo: subtract 3 from the output, and add 2 to the input. Many students subtract 2 from the input (wrong direction).

> [!question]- E2. Finding a function from table data
> | $x$ | $f(x)$ |
> |---|---|
> | 0 | 5 |
> | 1 | 15 |
> | 2 | 45 |
> | 3 | 135 |
>
> Which is $f(x)$?
> (A) $5 + 10x$  (B) $5 \cdot 3^x$  (C) $5x^2 + 5$  (D) $15^x$
>
> **Calculator:** Table mode → try each. Enter $f(x) = 5 \cdot 3^x$ → compare.
>
> > [!success]- Answer
> > The ratio $f(1)/f(0) = 3$, $f(2)/f(1) = 3$, $f(3)/f(2) = 3$ — constant ratio → exponential.
> > **(B) $f(x) = 5 \cdot 3^x$** ✓
> >
> > ⚠️ **Trap:** (A) is linear — fails at $f(2) = 25 \neq 45$. (C) gives $f(1) = 10 \neq 15$. (D) gives $f(0) = 1 \neq 5$. Check at least two points.

> [!question]- E3. Finding when $f(x) > g(x)$ with nonlinear functions
> For how many integer values of $x$ in $[0, 10]$ is $2^x > x^3$?
>
> **Calculator:** Table → $f(x) = 2^x$, $g(x) = x^3$, Start: 0, End: 10, Step: 1. Count where $f > g$.
>
> > [!success]- Answer
> > | $x$ | $2^x$ | $x^3$ | $2^x > x^3$? |
> > |---|---|---|---|
> > | 0 | 1 | 0 | ✓ |
> > | 1 | 2 | 1 | ✓ |
> > | 2 | 4 | 8 | ✗ |
> > | … | … | … | … |
> > | 9 | 512 | 729 | ✗ |
> > | 10 | 1024 | 1000 | ✓ |
> >
> > $2^x > x^3$ at $x = 0, 1, 10$. **Answer: 3**
> >
> > ⚠️ **Trap:** Exponentials eventually dominate polynomials, but there's a "dip" where the polynomial is larger. The crossover can be non-obvious — the table reveals it instantly.

> [!question]- E4. Remainder Theorem via Table
> When $p(x) = 2x^3 - 5x^2 + 3x - 7$ is divided by $(x - 3)$, what is the remainder?
>
> **Calculator:** Table → $f(x) = 2x^3 - 5x^2 + 3x - 7$, evaluate at $x = 3$ (or just use Calculate mode).
>
> > [!success]- Answer
> > $p(3) = 54 - 45 + 9 - 7 = 11$
> > **Remainder: 11**
> >
> > ⚠️ **Trap:** Remainder Theorem: dividing by $(x - c)$, evaluate at $x = c$. Dividing by $(x - 3)$ → evaluate at $x = 3$ (not $x = -3$).

> [!question]- E5. Exponential growth — multi-year percent increase
> A population grows by 8% per year. What is the total percent increase over 5 years?
>
> **Calculator:** Table → $f(x) = 100 \cdot 1.08^x$, evaluate at $x = 5$
>
> > [!success]- Answer
> > $f(5) = 100 \times 1.08^5 \approx 146.93$
> > Total increase: $\approx 46.93\%$ (NOT $40\%$!)
> >
> > ⚠️ **Trap:** 8% per year for 5 years ≠ 40%. Compound growth is multiplicative: $1.08^5 \approx 1.4693$, so it's about 46.9%. The SAT loves putting $40\%$ as a trap answer.

> [!question]- E6. Evaluating a rational function at multiple points
> $f(x) = \frac{x^2 - 9}{x - 3}$ for $x \neq 3$. What is $f(3.001)$?
>
> **Calculator:** Table → $f(x) = \frac{x^2 - 9}{x - 3}$, put $x = 3.001$
>
> > [!success]- Answer
> > $\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3} = x + 3$ for $x \neq 3$
> > $f(3.001) = 6.001$
> >
> > ⚠️ **Trap:** Even though $f$ is undefined at $x = 3$, you can simplify to $x + 3$ and see that the limit is $6$. The SAT tests whether you can handle removable discontinuities.

---

# Section F — Statistics & Regression

> **Calculator path:** HOME → Statistics → 1-Variable or Regression type
> **Regression types available:** Linear ($y = a + bx$), Quadratic ($y = a + bx + cx^2$), Logarithmic, e-Exponential, ab-Exponential, Power

### How to use — 1-Variable Statistics

1. **HOME** → **Statistics** → **1-Variable**
2. Enter data values (with optional frequencies)
3. Press **AC** then **OPTN**
4. Select: $\bar{x}$, $\sigma_x$ (population SD), $s_x$ (sample SD), $n$, $\Sigma x$, $\Sigma x^2$, Min, Max, Med, Q1, Q3

### How to use — Regression

1. **HOME** → **Statistics** → select regression type
2. Enter $(x, y)$ pairs
3. Press **AC** then **OPTN** → get coefficients, $r$ (correlation), $r^2$
4. Use $\hat{y}$ to predict values

---

> [!question]- F1. Finding the missing value to hit a target mean
> A set of 6 test scores is $\{72, 85, 91, 78, 88, x\}$. If the mean is exactly 84, what is $x$?
>
> **Calculator:** $\frac{72 + 85 + 91 + 78 + 88 + x}{6} = 84$
>
> > [!success]- Answer
> > $414 + x = 504 \Rightarrow x = 90$
> >
> > ⚠️ **Trap:** Sum = mean × count. Don't add only 5 numbers when there are 6.

> [!question]- F2. Effect of an outlier on mean vs. median
> Data set: $\{2, 5, 7, 8, 9, 10, 50\}$. If the outlier $50$ is replaced by $11$, which changes more — the mean or the median?
>
> **Calculator:** 1-Variable for both versions.
>
> > [!success]- Answer
> > Original: Mean = $91/7 = 13.0$, Median = $8$
> > New ($50 \to 11$): Mean = $52/7 \approx 7.43$, Median = $8$
> > The **mean** changes by $5.57$; the **median** doesn't change at all.
> >
> > ⚠️ **Trap:** The median is "resistant" to outliers; the mean is not. This is one of the SAT's favorite conceptual questions.

> [!question]- F3. Quadratic regression from three points
> Three points: $(1, 3)$, $(2, 9)$, $(3, 19)$. Find the quadratic function that passes through all three.
>
> **Calculator:** Statistics → Quadratic regression → enter points → get $a$, $b$, $c$
>
> > [!success]- Answer
> > Set up system $a + b + c = 3$, $4a + 2b + c = 9$, $9a + 3b + c = 19$.
> > Solve: $a = 2$, $b = 0$, $c = 1$. So $f(x) = 2x^2 + 1$.
> > Verify: $f(1) = 3$ ✓, $f(2) = 9$ ✓, $f(3) = 19$ ✓
> >
> > ⚠️ **Trap:** The regression on the calculator uses least-squares fitting, which with exactly 3 points for a quadratic gives the exact answer. But the CW's quadratic regression format is $y = a + bx + cx^2$ — the coefficient ORDER is reversed from standard form. Always verify at least one point.

> [!question]- F4. Interpreting slope in context
> An ecologist records the number of deer in a region over 8 years. The line of best fit is $y = 15.2x + 340$, where $x$ is years since 2015 and $y$ is deer population. Which statement is the best interpretation of $15.2$?
>
> (A) The population in 2015 was about 15
> (B) The population increases by about 15 deer per year
> (C) There were 15 more deer in 2023 than in 2015
> (D) The population will reach 15,200 eventually
>
> > [!success]- Answer
> > **(B)** — The slope $15.2$ means the population increases by approximately 15.2 deer per year.
> >
> > ⚠️ **Trap:** (A) confuses slope with intercept. (C) confuses total change with rate. The slope is the **rate of change per unit of $x$**.

> [!question]- F5. Population vs. sample standard deviation
> Data set: $\{4, 8, 6, 5, 7\}$. What is the population standard deviation?
>
> **Calculator:** 1-Variable → enter data → OPTN → $\sigma_x$
>
> > [!success]- Answer
> > Mean = 6. Deviations: $-2, 2, 0, -1, 1$. Squared: $4, 4, 0, 1, 1$. Variance = $10/5 = 2$. $\sigma = \sqrt{2} \approx 1.41$.
> >
> > ⚠️ **Trap:** The SAT almost always uses POPULATION standard deviation ($\sigma_x$, divide by $n$), not sample SD ($s_x$, divide by $n-1$). On the FX-991CW, $\sigma_x$ and $s_x$ are separate options — make sure you pick the right one.

> [!question]- F6. Exponential regression — predict future value
> Year data: $(0, 100), (1, 120), (2, 144), (3, 173), (4, 207)$. Using exponential regression, predict the value at $x = 6$.
>
> **Calculator:** Statistics → ab-Exponential → enter data → use $\hat{y}$ at $x = 6$
>
> > [!success]- Answer
> > The data follows $y = 100 \cdot 1.2^x$ (growth factor 1.2).
> > $\hat{y}(6) = 100 \times 1.2^6 \approx 298.6$
> >
> > ⚠️ **Trap:** For exponential regression, the CW offers TWO types:
> > - **e-Exp:** $y = a \cdot e^{bx}$ (natural base)
> > - **ab-Exp:** $y = a \cdot b^x$ (general base)
> > For most SAT problems, **ab-Exp** is more natural since growth rates are given as percentages.

> [!question]- F7. Interquartile range
> Data: $\{2, 5, 7, 8, 10, 12, 15, 18, 20\}$. What is the IQR?
>
> **Calculator:** 1-Variable → enter data → OPTN → Q1 and Q3
>
> > [!success]- Answer
> > 9 values. Q1 = median of lower half $\{2, 5, 7, 8\}$ = $6$. Q3 = median of upper half $\{12, 15, 18, 20\}$ = $16.5$.
> > IQR = $16.5 - 6 = 10.5$
> >
> > ⚠️ **Trap:** Different methods for computing quartiles exist (include/exclude median). The SAT and the FX-991CW both exclude the median when the count is odd. Practice with your calculator to confirm it matches.

> [!question]- F8. Correlation coefficient — which is the best fit?
> You enter 5 data points and get $r = 0.78$ for linear regression and $r^2 = 0.92$ for quadratic. Which model is a better fit?
>
> > [!success]- Answer
> > Linear: $r^2 = 0.78^2 = 0.608$ (60.8% of variation explained)
> > Quadratic: $r^2 = 0.92$ (92% of variation explained)
> > **Quadratic is the better fit.**
> >
> > ⚠️ **Trap:** Compare $r^2$ values, NOT $r$ values, especially across different model types. $r$ is only defined for linear models — for non-linear, use $r^2$.

---

# Section G — Ratio Mode (NEW — Hidden Gem!)

> **Calculator path:** HOME → Ratio
> **Why this matters:** Instantly solves proportions like $\frac{a}{b} = \frac{c}{d}$ for any unknown. Eliminates cross-multiplication errors, which are a silent killer on the SAT.

### How to use

1. **HOME** → **Ratio**
2. Choose format: $A : B = C : D$ or $\frac{A}{B} = \frac{C}{D}$
3. Enter the three known values and leave one blank
4. Press **=** → the missing value appears

---

> [!question]- G1. Similar triangles — find a side
> Triangles $PQR$ and $STU$ are similar with $\frac{PQ}{ST} = \frac{QR}{TU}$. If $PQ = 8$, $ST = 12$, and $QR = 14$, what is $TU$?
>
> **Calculator:** Ratio → $8 : 14 = 12 : x$ or $\frac{8}{12} = \frac{14}{x}$
>
> > [!success]- Answer
> > $\frac{8}{12} = \frac{14}{TU} \Rightarrow TU = \frac{12 \times 14}{8} = 21$
> >
> > ⚠️ **Trap:** Set up corresponding sides correctly. $PQ$ corresponds to $ST$, and $QR$ corresponds to $TU$. If you swap the correspondence, you get the reciprocal ratio.

> [!question]- G2. Scale factor and area
> Two similar rectangles have a length ratio of $3:5$. If the smaller rectangle has area $36$, what is the area of the larger?
>
> > [!success]- Answer
> > Area ratio = (length ratio)$^2$ = $(3/5)^2 = 9/25$
> > $\frac{36}{\text{Area}_{\text{large}}} = \frac{9}{25} \Rightarrow \text{Area}_{\text{large}} = \frac{36 \times 25}{9} = 100$
> >
> > **Calculator:** Ratio → $9 : 25 = 36 : x$ → $x = 100$
> >
> > ⚠️ **Trap:** Area scales as the SQUARE of the linear ratio, not the ratio itself. If you use $3:5$ directly, you get $60$ (wrong).

> [!question]- G3. Unit conversion chain
> A car uses 8 liters of fuel per 100 km. If fuel costs \$1.50 per liter, how much does fuel cost for a 350 km trip?
>
> **Calculator:** Ratio → $8 : 100 = x : 350$ → $x = 28$ liters → $28 \times 1.50 = 42$
>
> > [!success]- Answer
> > **\$42**
> >
> > ⚠️ **Trap:** This is a two-step ratio problem. First find liters, then multiply by price. The SAT loves embedding a unit conversion inside a word problem — the Ratio mode handles step one instantly.

> [!question]- G4. Percent "greater than" vs. percent "of"
> If $A$ is 60% greater than $B$, and $B = 200$, what is $A$?
>
> > [!success]- Answer
> > "60% greater than" means $A = B + 0.60B = 1.60B = 1.60 \times 200 = 320$
> >
> > ⚠️ **Trap:** "60% greater than" $\neq$ "60% of."
> > - 60% OF 200 = $120$
> > - 60% GREATER THAN 200 = $200 + 120 = 320$
> >
> > This is one of the most common traps for 750+ students. The SAT WILL put $120$ as a trap answer.

> [!question]- G5. Multi-step percent increase
> A stock increases by 20% one year and then decreases by 20% the next year. What is the net percent change?
>
> **Calculator:** $100 \times 1.20 \times 0.80 = ?$
>
> > [!success]- Answer
> > $100 \times 1.20 \times 0.80 = 96$
> > Net change: $-4\%$ (a LOSS, not break-even)
> >
> > ⚠️ **Trap:** $+20\%$ then $-20\%$ does NOT get you back to the original. The "20% decrease" is applied to the LARGER number ($120$), so you lose more than you gained. The SAT puts $0\%$ as a trap answer.

---

# Section H — Verify Mode (Sign-Error Killer)

> **Calculator path:** HOME → Verify
> **Your #1 weapon against careless mistakes.** After solving ANY equation, plug your answer back in and check TRUE/FALSE.

### How to use

1. **HOME** → **Verify**
2. Type equation with your answer: e.g., $3(5) - 7 = 2(5) + 3$ → FALSE → answer is wrong
3. Supports: `=`, `≠`, `>`, `<`, `≥`, `≤`

### When to use on test day

- After solving ANY equation: plug back in
- When unsure about a sign: verify the expression
- "Which value satisfies...": try each answer choice
- Radical/rational equations: check for extraneous solutions

---

> [!question]- H1. Extraneous solution check — radical equation
> Solve $\sqrt{2x + 7} = x + 2$. Verify both solutions.
>
> **Squaring:** $2x + 7 = x^2 + 4x + 4 \Rightarrow x^2 + 2x - 3 = 0$
> **Calculator (Polynomial):** $a=1$, $b=2$, $c=-3$ → $x = 1$ or $x = -3$
>
> > [!success]- Answer
> > **Verify $x = 1$:** $\sqrt{9} = 3$ and $1 + 2 = 3$ → TRUE ✓
> > **Verify $x = -3$:** $\sqrt{1} = 1$ and $-3 + 2 = -1$ → $1 = -1$ → FALSE ✗
> >
> > Only $x = 1$ is valid. $x = -3$ is extraneous.
> >
> > ⚠️ **Trap:** Squaring introduces extraneous solutions. ALWAYS verify when you square both sides.

> [!question]- H2. Rational equation — domain restriction
> Solve $\frac{x^2 - 4}{x - 2} = x + 5$.
>
> **Simplify LHS:** $\frac{(x-2)(x+2)}{x-2} = x + 2$ for $x \neq 2$.
> So $x + 2 = x + 5 \Rightarrow 2 = 5$?? No solution!
>
> > [!success]- Answer
> > **No solution.** The equation simplifies to a contradiction.
> >
> > But wait — what if a student cross-multiplies incorrectly and gets $x = 2$?
> > **Verify $x = 2$:** $\frac{0}{0} = 7$?? UNDEFINED → FALSE ✗
> >
> > ⚠️ **Trap:** $x = 2$ makes the denominator $0$. Always check domain restrictions in rational equations. "No solution" IS a valid answer on the SAT.

> [!question]- H3. Verifying inequality solutions — multiple choice
> Which of the following satisfies $|4x - 12| > 8$ AND $x < 5$?
> (A) $x = 0$ (B) $x = 2$ (C) $x = 4$ (D) $x = 6$
>
> **Verify each with calculator:**
>
> > [!success]- Answer
> > (A) $x = 0$: $|{-12}| = 12 > 8$ ✓ AND $0 < 5$ ✓ → **Works!**
> > (B) $x = 2$: $|{-4}| = 4 > 8$? NO ✗
> > (C) $x = 4$: $|4| = 4 > 8$? NO ✗
> > (D) $x = 6$: $|12| = 12 > 8$ ✓ BUT $6 < 5$? NO ✗
> >
> > **(A) $x = 0$**
> >
> > ⚠️ **Trap:** $|4x - 12| > 8$ means $x < 1$ or $x > 5$. Combined with $x < 5$: only $x < 1$ works. (D) satisfies the absolute value inequality but fails the second condition.

> [!question]- H4. System verification — off-by-one trap
> You solve $\begin{cases} 5x + 3y = 21 \\ 2x - y = 3 \end{cases}$ and get $x = 3, y = 2$. Verify.
>
> **Verify equation 1:** $5(3) + 3(2) = 15 + 6 = 21$ ✓
> **Verify equation 2:** $2(3) - 2 = 6 - 2 = 4 \neq 3$ ✗
>
> > [!success]- Answer
> > The "solution" fails equation 2. Redo with calculator:
> > Simultaneous → $[5, 3, 21]$ and $[2, -1, 3]$ → $x = \frac{30}{11}$, $y = \frac{27}{11}$
> >
> > ⚠️ **Trap:** A solution must satisfy ALL equations. Checking only one equation is insufficient. Always verify BOTH (or all three for 3-variable systems).

> [!question]- H5. The sign-error gauntlet — Module 2 level
> Solve: $-2(3x - 4) + 5 = 3(2 - x) - (x + 1)$
>
> > [!success]- Answer
> > **Left:** $-6x + 8 + 5 = -6x + 13$
> > **Right:** $6 - 3x - x - 1 = -4x + 5$
> > $-6x + 13 = -4x + 5$
> > $-2x = -8$
> > $x = 4$
> >
> > **Verify:** $-2(12 - 4) + 5 = -2(8) + 5 = -16 + 5 = -11$
> > $3(2 - 4) - (5) = 3(-2) - 5 = -6 - 5 = -11$ ✓
> >
> > ⚠️ **Trap alert — sign errors in every step:**
> > - $-2(3x) = -6x$ ✓ (not $+6x$)
> > - $-2(-4) = +8$ ✓ (not $-8$)
> > - $-(x+1) = -x - 1$ ✓ (not $-x + 1$)

---

# Section I — Calculate Mode Essentials

> **Calculator path:** HOME → Calculate
> **CRITICAL CORRECTION from old doc:** The FX-991CW has **NO CALC button**. You cannot press "CALC" to substitute values into stored expressions.

### What you CAN do in Calculate mode

| Feature | How |
|---|---|
| Define functions | Type $f(x) = 3x^2 + 1$, press = |
| Evaluate | Type $f(5)$, press = → gives $76$ |
| Define two functions | $f(x)$ and $g(x)$ — both are stored |
| Composition | Type $f(g(2))$ directly |
| Previous answer | Use **Ans** to chain calculations |
| Exact ↔ Decimal | Press **FORMAT** to toggle |
| Force decimal | Press **SHIFT** then **=** (gives ≈) |
| Fractions | Use fraction template (press the fraction key) |
| Mixed numbers | Available via FORMAT |

### ⚠️ No CALC button — workarounds

- **Old method (FX-991EX):** Type expression with $x$, press CALC, enter value
- **New method (FX-991CW):** Define $f(x) = \text{expression}$, then type $f(\text{value})$
- **OR:** Use the **Numerical Solver** (Equation/Inequality → Solver)
- **OR:** Use **Table mode** to evaluate at specific points

---

> [!question]- I1. Function composition
> If $f(x) = 2x + 3$ and $g(x) = x^2 - 1$, what is $f(g(3)) - g(f(3))$?
>
> **Calculator:** Define both functions. Type $f(g(3))$ → then $g(f(3))$ → subtract.
>
> > [!success]- Answer
> > $g(3) = 9 - 1 = 8$, $f(8) = 16 + 3 = 19$
> > $f(3) = 6 + 3 = 9$, $g(9) = 81 - 1 = 80$
> > $f(g(3)) - g(f(3)) = 19 - 80 = -61$
> >
> > ⚠️ **Trap:** $f(g(x)) \neq g(f(x))$ in general. And the order of operations inside the parentheses matters — compute the INNER function first.

> [!question]- I2. Exact vs. decimal — when FORMAT matters
> What is $\frac{7}{12} + \frac{5}{18}$?
>
> **Calculator:** Type as fractions → press = → get exact form. Press FORMAT to toggle.
>
> > [!success]- Answer
> > $\frac{7}{12} + \frac{5}{18} = \frac{21}{36} + \frac{10}{36} = \frac{31}{36}$
> >
> > Calculator shows $\frac{31}{36}$. Press FORMAT → $0.8\overline{6}$.
> >
> > ⚠️ **Trap:** On the SAT, if answer choices are fractions, keep things exact — don't round a decimal. If answer choices are decimals, press FORMAT to convert.

> [!question]- I3. Converting between fraction and decimal on answer entry
> The SAT answer grid accepts both fractions and decimals. If your calculator gives $\frac{31}{36}$, and you need to enter a decimal, how do you convert?
>
> > [!success]- Answer
> > Press **FORMAT** to see $0.86111...$
> > Or press **SHIFT** then **=** to get the decimal approximation.
> > For the SAT grid: enter $.8611$ (truncated) or $31/36$ (fraction).
> >
> > ⚠️ **Trap:** On the digital SAT, you can enter fractions directly (e.g., 31/36). You don't NEED to convert to decimal. But if you do convert, don't round too aggressively.

> [!question]- I4. Chaining calculations with Ans
> $\sqrt{2 + \sqrt{3 + \sqrt{4}}}$ = ?
>
> **Calculator:** Start from the inside: $\sqrt{4} = 2$ → $\sqrt{3 + \text{Ans}} = \sqrt{5}$ → $\sqrt{2 + \text{Ans}}$
>
> > [!success]- Answer
> > $\sqrt{4} = 2$
> > $\sqrt{3 + 2} = \sqrt{5} \approx 2.236$
> > $\sqrt{2 + \sqrt{5}} \approx \sqrt{4.236} \approx 2.058$
> >
> > ⚠️ **Trap:** Work from the INSIDE out with nested radicals. Using Ans chains each step without re-entering.

> [!question]- I5. Degree vs. radian mode check
> What is $\sin(30)$ in degree mode vs. radian mode?
>
> **Calculator:** Check the icon in the top status bar — "D" for degree, "R" for radian.
>
> > [!success]- Answer
> > **Degree mode:** $\sin(30°) = 0.5$ ✓ (correct for SAT)
> > **Radian mode:** $\sin(30) \approx -0.988$ (WRONG for SAT unless the problem gives radians)
> >
> > 🚨 **CRITICAL:** The SAT uses **degrees** unless the problem explicitly states radians (rare). Before any trig calculation, confirm you're in degree mode. On the CW, go to **SETTINGS** → **Angle Unit** → **Degree**.

---

# Section J — Mixed Module 2 Hard Simulation

> **🕐 Timed: 22 questions in 35 minutes. Use your calculator strategically.**
> **Difficulty: These are the questions that separate 750 from 800.**

---

> [!question]- J1. 🕐 Find $k$ — system with no solutions
> $$\begin{cases} 4x + 6y = 10 \\ 6x + ky = 12 \end{cases}$$
> For what value of $k$ does this system have no solution?
>
> > [!success]- Answer
> > Parallel: $\frac{4}{6} = \frac{6}{k} \Rightarrow k = 9$
> > Check: $\frac{10}{12} \neq \frac{6}{9}$? Well $\frac{10}{12} = \frac{5}{6}$ and $\frac{6}{9} = \frac{2}{3}$. Are these equal? $\frac{5}{6} \neq \frac{2}{3}$ ✓ → No solution confirmed.
> >
> > ⚠️ **Trap:** You MUST also verify the intercept ratio ≠ coefficient ratio. If all three ratios matched, it would be infinite solutions, not zero.

> [!question]- J2. 🕐 Quadratic in disguise
> If $(\sqrt{x})^2 - 6\sqrt{x} + 8 = 0$ and $x > 0$, what is the product of all solutions?
>
> > [!success]- Answer
> > Let $u = \sqrt{x}$: $u^2 - 6u + 8 = 0 \Rightarrow (u-2)(u-4) = 0$
> > $u = 2 \Rightarrow x = 4$, $u = 4 \Rightarrow x = 16$
> > Product $= 4 \times 16 = 64$
> >
> > ⚠️ **Trap:** Don't give the product of the $u$-values ($8$). Convert back to $x$ first.

> [!question]- J3. 🕐 Horizontal shift direction
> The graph of $y = f(x)$ is shifted $3$ units to the RIGHT to produce $y = g(x)$. If $f(x) = x^2$, what is $g(x)$?
>
> > [!success]- Answer
> > $g(x) = f(x - 3) = (x - 3)^2$
> >
> > ⚠️ **Trap:** Shift RIGHT → subtract from $x$ inside the function: $f(x - 3)$. Shift LEFT → add: $f(x + 3)$. This is counterintuitive and the #1 transformation trap on the SAT.

> [!question]- J4. 🕐 Circle — diameter given two endpoints
> The endpoints of a diameter of a circle are $(2, -3)$ and $(8, 5)$. What is the equation of the circle?
>
> > [!success]- Answer
> > Center = midpoint: $\left(\frac{2+8}{2}, \frac{-3+5}{2}\right) = (5, 1)$
> > Diameter $= \sqrt{(8-2)^2 + (5-(-3))^2} = \sqrt{36+64} = 10$
> > Radius $= 5$
> > $(x - 5)^2 + (y - 1)^2 = 25$
> >
> > ⚠️ **Trap:** Equation uses RADIUS, not diameter. If diameter = $10$, radius = $5$, and $r^2 = 25$ (not $100$).

> [!question]- J5. 🕐 Inscribed angle theorem
> In circle $O$, central angle $AOB = 130°$. Point $C$ is on the major arc $AB$. What is $\angle ACB$?
>
> > [!success]- Answer
> > The inscribed angle subtends the MINOR arc $AB$ (since $C$ is on the MAJOR arc).
> > $\angle ACB = \frac{1}{2} \times 130° = 65°$
> >
> > ⚠️ **Trap:** If $C$ were on the minor arc, the inscribed angle would subtend the major arc: $\frac{1}{2}(360° - 130°) = 115°$. Which arc the inscribed angle "sees" depends on which arc the vertex is NOT on.

> [!question]- J6. 🕐 Unit circle — large radian value
> What is $\sin\left(\frac{13\pi}{6}\right)$?
>
> > [!success]- Answer
> > $\frac{13\pi}{6} = 2\pi + \frac{\pi}{6}$ → same as $\sin\left(\frac{\pi}{6}\right) = \frac{1}{2}$
> >
> > **Calculator (radian mode):** $\sin(13\pi/6) = 0.5$ ✓
> >
> > ⚠️ **Trap:** Reduce the angle by subtracting $2\pi$ (or $360°$) repeatedly until you're in $[0, 2\pi)$. $13\pi/6 - 2\pi = 13\pi/6 - 12\pi/6 = \pi/6$.

> [!question]- J7. 🕐 Vertex form from table
> A quadratic function $f$ satisfies: $f(1) = 5$, $f(3) = 5$, $f(2) = 3$. Write $f(x)$ in vertex form.
>
> > [!success]- Answer
> > Since $f(1) = f(3) = 5$, the axis of symmetry is $x = 2$ (midpoint).
> > Vertex: $(2, 3)$ (since $f(2) = 3$, and $3 < 5$, this is a minimum).
> > $f(x) = a(x - 2)^2 + 3$
> > Plug in $(1, 5)$: $5 = a(1) + 3 \Rightarrow a = 2$
> > $f(x) = 2(x - 2)^2 + 3$
> >
> > ⚠️ **Trap:** The symmetry trick ($f(1) = f(3)$ → axis at $x = 2$) is faster than setting up three equations. Learn to spot symmetric function values.

> [!question]- J8. 🕐 Percent increase ratio
> Last year, a store sold $n$ items at \$40 each. This year, it sold 20% more items at a price 10% higher. What is the ratio of this year's revenue to last year's?
>
> > [!success]- Answer
> > Last year: $40n$
> > This year: $1.20n \times 44 = 52.8n$
> > Ratio: $\frac{52.8n}{40n} = 1.32$ → This year is **32% more**.
> >
> > ⚠️ **Trap:** You can't just add percentages: $20\% + 10\% = 30\%$ is WRONG. You multiply the factors: $1.20 \times 1.10 = 1.32$ → 32%.

> [!question]- J9. 🕐 Quadratic zeros via sign analysis
> $f(x) = -(x - 3)(x + 5)$. For what values of $x$ is $f(x) > 0$?
>
> > [!success]- Answer
> > Zeros at $x = 3$ and $x = -5$. Leading coefficient negative → parabola opens DOWN.
> > $f(x) > 0$ between the roots: $-5 < x < 3$
> >
> > ⚠️ **Trap:** Negative leading coefficient means the parabola opens DOWN — positive values are BETWEEN the roots, not outside.

> [!question]- J10. 🕐 Triangle inscribed in semicircle (Thales' Theorem)
> Triangle $ABC$ is inscribed in a semicircle with diameter $AB = 10$. If $AC = 6$, what is $BC$?
>
> > [!success]- Answer
> > Thales' Theorem: angle at $C$ (inscribed in semicircle) is $90°$.
> > $BC = \sqrt{AB^2 - AC^2} = \sqrt{100 - 36} = \sqrt{64} = 8$
> >
> > ⚠️ **Trap:** Memorize Thales' Theorem — any triangle inscribed in a semicircle (with one side as the diameter) has a $90°$ angle opposite the diameter.

> [!question]- J11. 🕐 Exponential growth — non-standard phrasing
> A bacteria colony triples every 4 hours. If there are 500 bacteria at $t = 0$, how many are there at $t = 12$ hours?
>
> > [!success]- Answer
> > In 12 hours: $12/4 = 3$ tripling periods.
> > $500 \times 3^3 = 500 \times 27 = 13{,}500$
> >
> > ⚠️ **Trap:** The growth factor is $3$ (triples), and the period is $4$ hours. The exponent is $t/4$, not $t$. $P(t) = 500 \cdot 3^{t/4}$.

> [!question]- J12. 🕐 Square inscribed in a circle
> A square is inscribed in a circle of radius $5$. What is the area of the square?
>
> > [!success]- Answer
> > The diagonal of the square = diameter of circle $= 10$.
> > If diagonal $= d$, side $= d/\sqrt{2} = 10/\sqrt{2} = 5\sqrt{2}$.
> > Area $= (5\sqrt{2})^2 = 50$
> >
> > **Shortcut:** Area of square $= \frac{d^2}{2} = \frac{100}{2} = 50$.
> >
> > ⚠️ **Trap:** Area is NOT $10^2 = 100$ (that's the area of the circumscribing square, not the inscribed one). Also: diagonal ≠ side.

> [!question]- J13. 🕐 Projectile symmetry
> A ball is launched upward. Its height is $h(t) = -16t^2 + 64t + 5$. At what time does it reach its maximum height?
>
> > [!success]- Answer
> > $t = -\frac{b}{2a} = -\frac{64}{2(-16)} = -\frac{64}{-32} = 2$ seconds.
> >
> > **Calculator:** Polynomial degree 2 → $a=-16$, $b=64$, $c=5$ → roots at $t \approx -0.077$ and $t \approx 4.077$.
> > Midpoint $= \frac{-0.077 + 4.077}{2} = 2.0$ ✓
> >
> > ⚠️ **Trap:** Max height TIME is $t = -b/(2a)$, not the max HEIGHT itself. The max height is $h(2) = -64 + 128 + 5 = 69$ feet.

> [!question]- J14. 🕐 The "answer the right thing" trap
> If $x^2 + 5x - 6 = 0$, what is $x^2 + 5x$?
>
> > [!success]- Answer
> > From the equation: $x^2 + 5x = 6$. Done.
> >
> > ⚠️ **Trap:** Don't solve for $x$ and then compute $x^2 + 5x$. The answer is staring at you in the equation.

> [!question]- J15. 🕐 "Neither" as a valid answer
> Lines $\ell_1$ and $\ell_2$ have slopes $\frac{2}{3}$ and $\frac{3}{2}$. What is their relationship?
>
> > [!success]- Answer
> > Parallel: slopes equal? $\frac{2}{3} \neq \frac{3}{2}$ → Not parallel.
> > Perpendicular: product $= -1$? $\frac{2}{3} \times \frac{3}{2} = 1 \neq -1$ → Not perpendicular.
> > **Neither parallel nor perpendicular.**
> >
> > ⚠️ **Trap:** Many students see $\frac{2}{3}$ and $\frac{3}{2}$ and think "reciprocal = perpendicular." NO — perpendicular requires the NEGATIVE reciprocal. $\frac{2}{3}$ and $-\frac{3}{2}$ would be perpendicular.

> [!question]- J16. 🕐 Completing the square — find $c$ for a specific vertex
> What value of $c$ makes the vertex of $y = x^2 - 8x + c$ have a $y$-coordinate of $3$?
>
> > [!success]- Answer
> > Vertex $y$-value: $c - \frac{b^2}{4a} = c - \frac{64}{4} = c - 16$
> > Set equal to $3$: $c - 16 = 3 \Rightarrow c = 19$
> >
> > **Verify:** $y = x^2 - 8x + 19 = (x-4)^2 + 3$ → vertex $(4, 3)$ ✓
> >
> > ⚠️ **Trap:** The vertex $y$-coordinate is $c - b^2/(4a)$, NOT $c - b/(2a)$.

> [!question]- J17. 🕐 Nonlinear system — number of solutions
> How many solutions does the system $y = x^2$ and $y = 2x + 3$ have?
>
> **Calculator:** $x^2 = 2x + 3 \Rightarrow x^2 - 2x - 3 = 0$. Polynomial → $a=1$, $b=-2$, $c=-3$
>
> > [!success]- Answer
> > $\Delta = 4 + 12 = 16 > 0$ → **2 solutions**
> > Roots: $x = 3$ and $x = -1$
> >
> > ⚠️ **Trap:** A line can intersect a parabola at 0, 1, or 2 points — determined by the discriminant of the resulting quadratic.

> [!question]- J18. 🕐 Statistics — comparing two groups
> Group A: mean 72, SD 5. Group B: mean 78, SD 12. A student scored 80 in Group A and 90 in Group B. In which group did the student perform relatively better?
>
> > [!success]- Answer
> > Group A z-score: $\frac{80 - 72}{5} = 1.6$ standard deviations above mean
> > Group B z-score: $\frac{90 - 78}{12} = 1.0$ standard deviations above mean
> > **Relatively better in Group A** (higher z-score)
> >
> > ⚠️ **Trap:** Higher raw score ≠ better relative performance. Use z-scores to compare across different distributions.

> [!question]- J19. 🕐 Arc length with algebra
> In a circle with radius $r$, an arc of length $3\pi$ is subtended by a central angle of $60°$. What is $r$?
>
> > [!success]- Answer
> > Arc length $= \frac{\theta}{360} \times 2\pi r$
> > $3\pi = \frac{60}{360} \times 2\pi r = \frac{1}{6} \times 2\pi r = \frac{\pi r}{3}$
> > $r = 9$
> >
> > ⚠️ **Trap:** Don't confuse arc length ($s = r\theta$) with sector area ($A = \frac{1}{2}r^2\theta$). Also make sure degree vs radian is consistent.

> [!question]- J20. 🕐 The hardest trap — answering the wrong quantity
> The sum of three consecutive even integers is 66. What is the LARGEST of the three?
>
> **Calculator:** Let $x, x+2, x+4$. $3x + 6 = 66 \Rightarrow x = 20$.
>
> > [!success]- Answer
> > The three integers: $20, 22, 24$. **LARGEST = 24**
> >
> > ⚠️ **Trap:** The question asks for the LARGEST, not the smallest or the middle. $x = 20$ is the smallest. The answer is $x + 4 = 24$.

> [!question]- J21. 🕐 Area ratio from similar triangles
> Triangle $ABC$ has sides $3, 4, 5$. Triangle $DEF$ is similar with the longest side equal to $15$. What is the ratio of their areas?
>
> > [!success]- Answer
> > Scale factor: $\frac{15}{5} = 3$
> > Area ratio: $3^2 = 9$
> > Area of $DEF$ / Area of $ABC = 9$
> >
> > ⚠️ **Trap:** Areas scale as the SQUARE of the linear scale factor. Not $3×$, but $9×$.

> [!question]- J22. 🕐 Domain constraint omission
> What is the domain of $f(x) = \frac{\sqrt{x - 2}}{x - 5}$?
>
> > [!success]- Answer
> > Numerator: $x - 2 \geq 0 \Rightarrow x \geq 2$
> > Denominator: $x - 5 \neq 0 \Rightarrow x \neq 5$
> > **Domain: $x \geq 2$ and $x \neq 5$**, or $[2, 5) \cup (5, \infty)$
> >
> > ⚠️ **Trap:** You need BOTH conditions. Students often remember the square root restriction but forget the denominator ≠ 0 (or vice versa).

---

# Summary — Test Day Calculator Strategy (FX-991CW)

> [!abstract] Pre-Test Checklist
>
> - [ ] **Angle mode:** DEGREE (not radian) — check Settings → Angle Unit
> - [ ] **Batteries:** Fresh
> - [ ] **Know how to access (by heart):**
>   - Polynomial solver (degree 2, 3, 4): HOME → Equation/Inequality → Polynomial
>   - Simultaneous equations (2, 3, 4 unknowns): HOME → Equation/Inequality → Simultaneous
>   - Inequality solver: HOME → Equation/Inequality → Inequality
>   - Numerical solver: HOME → Equation/Inequality → Solver
>   - Table mode: HOME → Table
>   - Statistics: HOME → Statistics
>   - Ratio: HOME → Ratio
>   - Verify: HOME → Verify
> - [ ] **Remember:** No CALC button. Use $f(x) =$ definition or Solver instead.
> - [ ] **FORMAT** toggles exact ↔ decimal. **SHIFT+EXE** forces ≈.

> [!abstract] Module 2 Decision Tree
>
> **Quadratic equation asked?** → Polynomial solver
> **System of equations?** → Simultaneous solver (rewrite in $ax + by = c$ form first)
> **"For what value of $k$..."** → Discriminant analysis + calculator to verify
> **Table of data → find equation?** → Statistics regression
> **Proportion / similar figures?** → Ratio mode
> **"Which value satisfies..."** → Verify mode (plug each choice)
> **Complex expression evaluation?** → Calculate mode with $f(x)$ definition
> **"How many solutions?"** → Polynomial discriminant or Table scan
> **You solved something → now check it?** → ALWAYS Verify mode before submitting

> [!abstract] The 10-Second Verification Habit
>
> After solving **any** equation:
> 1. Switch to Verify mode (HOME → 13)
> 2. Type the original equation with your solution plugged in
> 3. If TRUE → submit confidently
> 4. If FALSE → redo the problem (your sign is probably wrong)
>
> This habit alone can save 20–40 points on test day.

---

*Total questions: ~70 | Sections: 10 | Estimated completion time: 4–5 hours (do across multiple sessions)*
*All exercises are Module 2 hard difficulty. If you can do these, you can do the SAT.*
