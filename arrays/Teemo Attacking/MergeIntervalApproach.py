class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        Calculates the total time a character remains poisoned.

        Each attack at time t causes poisoning from t to t + duration - 1.
        Overlapping poison intervals are merged to avoid double counting.
        """

        # Start and end of the current poison interval
        s = timeSeries[0]
        e = s + duration - 1

        total = 0
        n = len(timeSeries)

        # Iterate through subsequent attack times
        for i in range(1, n):
            currs = timeSeries[i]
            curre = currs + duration - 1

            # If current poison overlaps with the previous interval
            if currs <= e:
                # Extend the current poison interval
                e = max(e, curre)
            else:
                # No overlap: finalize the previous interval
                total += e - s + 1
                s, e = currs, curre

        # Add the last poison interval duration
        total += e - s + 1

        return total

Time Complexity:
O(n)

Space Complexity:
O(1)
