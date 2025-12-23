class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Returns the minimum number of intervals to remove
        so that the remaining intervals do not overlap.

        Greedy approach:
        - Always keep the interval with the earliest end time.
        """

        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            # If current interval does not overlap, keep it
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            else:
                # Overlapping interval -> remove it
                removals += 1

        return removals

Time Complexity

O(n log n)
Sorting dominates the runtime.
Single linear scan afterward.

Space Complexity

O(1)
In-place sorting.

Only constant extra variables used.
