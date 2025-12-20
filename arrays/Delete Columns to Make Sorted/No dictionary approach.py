class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Counter to track the number of columns
        # that must be deleted to make the array sorted
        count = 0

        # Iterate column-wise using the index of characters
        for col in range(len(strs[0])):
            # Check whether the current column is sorted
            # by comparing adjacent rows
            for row in range(1, len(strs)):
                # If any character is smaller than the one above it,
                # the column violates non-decreasing order
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    # No need to check further rows for this column
                    break

        return count

Time Complexity: O(n × m)
Space Complexity: O(1)

where:
n = number of strings
m = length of each string
