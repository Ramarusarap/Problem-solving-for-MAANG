class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Compute the minimum path sum from top-left to bottom-right
        using bottom-up dynamic programming with in-place updates.

        Each cell accumulates the minimum cost to reach it from
        either the top or the left.

        Time Complexity: O(m * n)
        Extra Space Complexity: O(1)
        """

        rows, cols = len(grid), len(grid[0])

        # Fill first row (only move right)
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]

        # Fill first column (only move down)
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]

        # Fill remaining cells
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[rows - 1][cols - 1]
