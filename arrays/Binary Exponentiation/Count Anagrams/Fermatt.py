class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        words = s.split()  
        # Time: O(N) for splitting, where N = total characters in string

        def factorial(x):
            """
            Computes x! % MOD
            Time: O(x)
            Space: O(1)
            """
            ans = 1
            for i in range(1, x + 1):
                ans = (ans * i) % MOD
            return ans

        def mod_inv(x):
            """
            Computes modular inverse using Fermat's Little Theorem
            Time: O(log MOD)
            Space: O(1)
            """
            return pow(x, MOD - 2, MOD)

        answer = 1

        for word in words:
            freq = {}
            # Time: O(len(word))
            # Space: O(1) since at most 26 lowercase letters

            for ch in word:
                freq[ch] = freq.get(ch, 0) + 1

            numerator = factorial(len(word))  # Time: O(len(word))

            denominator = 1
            for c in freq.values():
                denominator = (denominator * factorial(c)) % MOD
                # Total time across this loop ≤ O(len(word))

            ways = (numerator * mod_inv(denominator)) % MOD
            answer = (answer * ways) % MOD

        return answer
        # Overall Time Complexity: O(N * L)
        #   N = total characters in string
        #   L = maximum word length
        #
        # Overall Space Complexity: O(1) auxiliary
