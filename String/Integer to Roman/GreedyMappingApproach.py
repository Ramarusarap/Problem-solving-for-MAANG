class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.

        Approach:
        Greedy mapping from largest Roman values to smallest,
        including subtractive combinations (e.g., 900 -> CM).

        Time Complexity: O(1)
        - The loop runs over a fixed set of Roman symbols (13 entries).

        Space Complexity: O(1)
        - Output string size is bounded (max ~15 characters).
        """

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = []

        for i in range(len(values)):
            # Append the symbol while the value can be subtracted
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]

        return "".join(result)
