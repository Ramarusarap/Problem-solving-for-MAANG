from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Counts the number of subarrays filled with only zeros.

        Approach:
        - Count lengths of consecutive zero blocks.
        - For a block of length k, number of zero-filled subarrays is:
              1 + 2 + ... + k
        - Sum this for all zero blocks.

        Time Complexity:
        - O(n^2) in worst case due to repeated summation inside factorialSum.

        Space Complexity:
        - O(1)
        """

        def factorialSum(a: int) -> int:
            """
            Returns sum of numbers from 1 to a.
            NOTE: This is equivalent to a * (a + 1) // 2,
            but implemented iteratively here.
            """
            ans = 0
            while a > 0:
                ans += a
                a -= 1
            return ans

        result = 0
        count = 0

        for i in nums:
            # If current element is non-zero, end the zero streak
            if i != 0 and count > 0:
                result += factorialSum(count)
                count = 0

            # Continue counting zeros
            if i == 0:
                count += 1

        # Add remaining zero streak (if array ends with zeros)
        result += factorialSum(count)

        return result
