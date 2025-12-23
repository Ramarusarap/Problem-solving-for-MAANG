class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines whether `n` new flowers can be planted in the flowerbed
        without violating the no-adjacent-flowers rule.

        Greedy approach:
        - Traverse the flowerbed
        - Place a flower whenever both adjacent plots are empty
        """

        l = len(flowerbed)

        # Edge case: single plot
        if l == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0

        # Traverse the flowerbed
        for i in range(l):
            # Only attempt to plant if current plot is empty
            if flowerbed[i] == 0:
                # Case 1: Middle plots
                if i != 0 and i != l - 1:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

                # Case 2: First plot
                elif i == 0:
                    if flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

                # Case 3: Last plot
                elif i == l - 1:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

        return n <= 0


Time Complexity

O(n)
Single pass through the flowerbed.

Space Complexity

O(1)
In-place modification of the input array.
No extra data structures used.
