# Integer to Roman

LeetCode problem: Convert an integer to its Roman numeral representation.

---

## 📌 Problem Statement

Given an integer `num`, convert it to a Roman numeral.

### Constraints
- `1 ≤ num ≤ 3999`

Roman numerals use the following symbols:

| Symbol | Value |
|------|------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Subtractive notation is used for specific cases:
- `IV` (4), `IX` (9)
- `XL` (40), `XC` (90)
- `CD` (400), `CM` (900)

---

## ✅ Optimal Approach

This solution uses **digit-wise lookup tables** for ones, tens, hundreds, and thousands.

Each digit position has a fixed Roman representation, which allows direct indexing without loops or subtraction.

---

## 🧠 Why Time Complexity Is O(1)

### Key Justification

- The input range is **strictly bounded**:
