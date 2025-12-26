class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        Find the maximum difference nums[j] - nums[i] such that j > i.

        Greedy Strategy:
        - Track the index of the minimum value seen so far
        - At each step, compute the difference with the current value
        - If a smaller value appears, greedily reset the minimum

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        min_index = 0
        max_diff = -1

        for i in range(1, len(nums)):
            # Greedily update maximum difference
            if nums[i] > nums[min_index]:
                max_diff = max(max_diff, nums[i] - nums[min_index])
            else:
                # Greedy choice: discard worse minimum
                min_index = i

        return max_diff
