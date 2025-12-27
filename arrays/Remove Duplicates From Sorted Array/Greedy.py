from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place.

        Greedy + Two Pointers:
        - i tracks the position of the last unique element
        - j scans the array for new unique elements

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if not nums:
            return 0

        i = 0  # index of last unique element

        for j in range(1, len(nums)):
            # Greedy choice: keep element if it is different
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
