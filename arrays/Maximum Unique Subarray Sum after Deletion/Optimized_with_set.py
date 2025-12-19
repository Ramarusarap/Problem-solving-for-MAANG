class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_pos = set()
        max_negative = -101  # constraint-based initialization

        for num in nums:
            if num < 0:
                max_negative = max(max_negative, num)
            else:
                unique_pos.add(num)

        # If no non-negative numbers exist
        if not unique_pos:
            return max_negative

        return sum(unique_pos)

Time Complexity: O(n)
Space Complexity: O(k)
where k is the number of unique non-negative elements

You cannot reduce space below O(k) because uniqueness must be tracked.
