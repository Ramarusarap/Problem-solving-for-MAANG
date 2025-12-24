from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def nCr(n: int, r: int) -> int:
            r = min(r, n - r)  # symmetry optimization
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
            return res

        return [nCr(rowIndex, i) for i in range(rowIndex + 1)]

""" nCr-for-each-i approach: the inner for loop runs ≈ n² / 4 times in total. """
