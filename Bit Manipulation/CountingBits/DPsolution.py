from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Returns number of set bits for every number in [0, n].

        Time Complexity:
        - O(n)

        Space Complexity:
        - O(n)
        """

        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result
