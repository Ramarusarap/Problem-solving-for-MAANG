class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines whether `n` flowers can be planted in the flowerbed
        without violating the no-adjacent-flowers rule.

        Greedy approach:
        - Traverse the flowerbed from left to right
        - Place a flower whenever the current plot and its adjacent plots are empty
        """

        length = len(flowerbed)

        for i in range(length):
            # Proceed only if the current plot is empty
            if flowerbed[i] == 0:

                # Check left neighbor (or boundary)
                left_empty = (i == 0 or flowerbed[i - 1] == 0)

                # Check right neighbor (or boundary)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)

                # If both neighbors are empty, plant a flower here
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

        # Return True if all required flowers were planted
        return n <= 0

Complexity

Time: O(n)
Space: O(1)
