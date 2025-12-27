from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array which sum to zero.

        Approach:
        - Sort the array
        - Fix one element (i)
        - Use two pointers (j, k) to find pairs that sum to -nums[i]
        - Greedily move pointers based on current sum
        - Skip duplicates to avoid repeated triplets

        Time Complexity: O(n^2)
        Space Complexity: O(1) (excluding output)
        """

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # Move both pointers and skip duplicates
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    # Greedy choice: need a larger sum
                    j += 1
                else:
                    # Greedy choice: need a smaller sum
                    k -= 1

        return result
