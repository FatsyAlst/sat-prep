---
type: reference
tags: [reference, arithmetic, rounding]
---

# Rounding Reference

> Quick reference for rounding decimal numbers — built for SAT grid-in answers where the problem specifies "round to the nearest \_\_\_".

---

## Place Value Map

Every digit after the decimal point has a fixed name based on its position:

| Position after `.` | Name | Decimal places to keep |
|---|---|---|
| 1st | **tenth** | 1 |
| 2nd | **hundredth** | 2 |
| 3rd | **thousandth** | 3 |
| 4th | **ten-thousandth** | 4 |
| 5th | **hundred-thousandth** | 5 |

> [!tip] The shortcut
> The name tells you how many decimal places to keep:
> - **tenth** → keep **1** decimal place
> - **hundredth** → keep **2** decimal places
> - **thousandth** → keep **3** decimal places

---

## The Universal Rounding Rule

> Look at the digit **one place to the right** of where you're rounding.
> - If it is **≥ 5** → round **up** (increase the last kept digit by 1)
> - If it is **< 5** → round **down** (keep the last kept digit as is)

---

## Full Example — Working through 9.21983

$$9.21983$$

| Round to the nearest… | Keep ___ decimals | Look at digit in position | That digit | Action | Result |
|---|---|---|---|---|---|
| **tenth** | 1 | 2nd (= **1**) | 1 < 5 | down | **9.2** |
| **hundredth** | 2 | 3rd (= **9**) | 9 ≥ 5 | up | **9.22** |
| **thousandth** | 3 | 4th (= **8**) | 8 ≥ 5 | up | **9.220** |
| **ten-thousandth** | 4 | 5th (= **3**) | 3 < 5 | down | **9.2198** |

---

## SAT-Specific Mistakes to Avoid

> [!warning] Copying one extra digit from the calculator
> "Round to the thousandth" = **3 decimal places**. If your calculator shows `0.29179`, the answer is `0.292` — not `0.2918`. Count the decimal places *before* copying.

> [!warning] Truncating instead of rounding
> Truncating means just cutting digits off. Rounding means checking the next digit first.
> - $\sqrt{85} = 9.2195...$
> - Truncated to hundredths: **9.21** ✗
> - Rounded to hundredths: **9.22** ✓ (3rd decimal is 9 ≥ 5 → round up)

> [!warning] Confusing "tenth" with "ten" / "hundredth" with "hundred"
> - **tenth** = $\frac{1}{10}$ = 0.1 → **after** the decimal point (1 place)
> - **ten** = 10 → **before** the decimal point
> These are completely different. The "-th" suffix always means a fraction (a small number after the decimal).

---

## Portuguese Equivalents

| English | Portuguese | Decimal places |
|---|---|---|
| tenth | décimo / uma casa decimal | 1 |
| hundredth | centésimo / duas casas decimais | 2 |
| thousandth | milésimo / três casas decimais | 3 |
| ten-thousandth | décimo de milésimo / quatro casas decimais | 4 |

---

## Test Day Checklist

Before writing any rounded answer on the SAT:

1. **Read the rounding instruction** — which place name does the problem use?
2. **Translate to a count** — tenth = 1, hundredth = 2, thousandth = 3
3. **Look at the next digit** — is it ≥ 5?
4. **Write the answer** — count the decimal places on your screen before copying

---

## Quick Reference Card

```
Number:   9 . 2  1  9  8  3
               │  │  │  │  │
               │  │  │  │  └─ hundred-thousandth (5th)
               │  │  │  └──── ten-thousandth     (4th)
               │  │  └─────── thousandth         (3rd)
               │  └────────── hundredth          (2nd)
               └───────────── tenth              (1st)
```
