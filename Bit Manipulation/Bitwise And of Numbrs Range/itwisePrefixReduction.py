class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Returns the bitwise AND of all numbers in the range [left, right].

        Key Insight:
        - Only the common leftmost bits of left and right survive.
        - Any differing bit becomes 0 due to AND over the range.

        Time Complexity:
        - O(1)  (at most 32 shifts)

        Space Complexity:
        - O(1)
        """

        shift = 0

        # Remove differing bits
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Restore common prefix
        return left << shift
