- This means the number has **at most 4 digits**.
- The algorithm performs:
- A constant number of arithmetic operations
- A fixed number of list lookups
- A fixed number of string concatenations
- There are **no loops that depend on input size**.

Since the number of operations never increases beyond a constant upper bound, the time complexity is:

> **O(1)**

---

### Why This Is Not O(log n)

Digit extraction is sometimes associated with `O(log n)`, but that only applies when `n` is **unbounded**.

In this problem:
- `log₁₀(3999)` is a constant
- Bounded logarithmic growth collapses to **O(1)**

---

## 💾 Space Complexity: O(1)

- Lookup tables have fixed size.
- No auxiliary data structures grow with input.
- Output length is bounded (maximum ~15 characters).

Therefore, space complexity is also **O(1)**.

---

## 🧪 Implementation

```python
class Solution:
  def intToRoman(self, num: int) -> str:
      """
      Convert integer to Roman numeral using digit lookup tables.

      Time Complexity: O(1)
      Space Complexity: O(1)
      """

      thousands = ["", "M", "MM", "MMM"]
      hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
      tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
      ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

      return (
          thousands[num // 1000] +
          hundreds[(num % 1000) // 100] +
          tens[(num % 100) // 10] +
          ones[num % 10]
      )
