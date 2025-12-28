class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Counts the number of negative numbers in a matrix where
        each row and each column is sorted in non-increasing order.

        Time Complexity: O(m + n)
        - m = number of rows
        - n = number of columns
        - Pointer moves either left (col--) or down (r++) in each step.
        - Each row and column is visited at most once.

        Space Complexity: O(1)
        - Uses only constant extra space.
        - No additional data structures are created.
        """

        row = len(grid)
        col = len(grid[0]) - 1  # Start from top-right corner
        r = 0                  # Row pointer
        count = 0              # Stores total negative numbers

        # Traverse until we go out of bounds
        while r < row and col >= 0:
            # If current element is negative
            if grid[r][col] < 0:
                # All elements below this in the same column are also negative
                count += row - r

                # Move left to check next column
                col -= 1
            else:
                # Current element is non-negative
                # Move down to the next row
                r += 1

        return count
