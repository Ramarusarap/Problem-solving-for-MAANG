class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val in-place and return the new length.

        Greedy + Two Pointers:
        - i marks the position to place the next valid element
        - j scans the array
        """

        i = 0  # position to place next non-val element

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
