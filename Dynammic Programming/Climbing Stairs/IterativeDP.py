class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Computes the number of distinct ways to climb to the top.
        At each step, you can climb either 1 or 2 stairs.

        This is the most efficient solution:
        - Bottom-Up Dynamic Programming
        - Constant Space
        """

        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # prev1 -> ways to reach step (i-2)
        # prev2 -> ways to reach step (i-1)
        prev1, prev2 = 1, 2

        # Build the solution iteratively from step 3 to n
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr

        # prev2 holds the result for step n
        return prev2

Time Complexity

O(n)
The loop runs once from 3 to n
Each iteration does constant work

Space Complexity

O(1)
Uses only a fixed number of variables
No recursion
No auxiliary data structures

Why this is the most efficient

Same optimal time as memoization (O(n))
Better space usage (O(1) vs O(n))
No recursion stack
No hash map overhead
