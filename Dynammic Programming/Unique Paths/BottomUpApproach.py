class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Compute the number of unique paths in an m x n grid
        using bottom-up dynamic programming.

        A robot can only move right or down.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """

        # DP table initialization
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
