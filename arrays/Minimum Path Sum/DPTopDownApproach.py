class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Compute the minimum path sum from top-left to bottom-right
        using top-down DP with memoization.

        Allowed moves: right or down.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """

        rows, cols = len(grid), len(grid[0])
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]

        def helper(row: int, col: int) -> int:
            # Return cached result if already computed
            if memo[row][col] != -1:
                return memo[row][col]

            # Base case: bottom-right cell
            if row == rows - 1 and col == cols - 1:
                memo[row][col] = grid[row][col]
                return memo[row][col]

            # If last row, can only move right
            if row == rows - 1:
                memo[row][col] = grid[row][col] + helper(row, col + 1)

            # If last column, can only move down
            elif col == cols - 1:
                memo[row][col] = grid[row][col] + helper(row + 1, col)

            # General case: choose min of right and down
            else:
                memo[row][col] = grid[row][col] + min(
                    helper(row, col + 1),
                    helper(row + 1, col)
                )

            return memo[row][col]

        return helper(0, 0)
