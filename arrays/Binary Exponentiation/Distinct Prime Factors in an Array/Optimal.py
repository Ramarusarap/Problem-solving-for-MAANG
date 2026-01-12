from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        """
        Returns the number of distinct prime factors of the product
        of all elements in nums.

        Approach:
        Factor each number independently using trial division and
        collect distinct prime factors in a set.

        Time Complexity: O(n * sqrt(M))
        Space Complexity: O(k), where k is the number of distinct primes
        """

        primes = set()

        for num in nums:
            d = 2
            while d * d <= num:
                while num % d == 0:
                    primes.add(d)
                    num //= d
                d += 1

            if num > 1:
                primes.add(num)

        return len(primes)
