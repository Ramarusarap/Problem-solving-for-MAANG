from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all permutations of the input list using
        an insert-based recursive approach.

        Strategy:
        - Recursively compute permutations of nums[1:].
        - Insert nums[0] into every possible position
          of each smaller permutation.

        Base Case:
        - An empty list has exactly one permutation: [[]]
        """

        # Base case: one permutation of an empty list
        if len(nums) == 0:
            return [[]]

        # Recursively get permutations of the remaining elements
        perms = self.permute(nums[1:])

        res = []

        # Insert the current element into every possible position
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()        # avoid modifying original permutation
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res
