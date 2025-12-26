
---

## Complexity Analysis

- **Time Complexity:** `O(m × n)`
- **Space Complexity:** `O(n)`

This is the most space-efficient DP solution for this problem.

---

## Why This Is Optimal (DP-wise)

- Every grid cell must be considered → time cannot be reduced
- Space is minimized to one row
- No recursion or extra memory required

---

## Interview One-Liner

> I optimize the grid DP to a single array by realizing each cell depends only on the current and previous column values.

---

## Notes
- Clean bottom-up DP
- Space optimized
- Interview-preferred solution
