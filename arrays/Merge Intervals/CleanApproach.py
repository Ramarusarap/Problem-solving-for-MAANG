class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals.

        Approach:
        - Sort intervals by start time
        - Expand the current interval if overlap exists
        - Otherwise, push current interval to result
        """

        intervals.sort(key=lambda x: x[0])
        result = []

        start, end = intervals[0]

        for i in range(1, len(intervals)):
            # Overlapping intervals
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                # Non-overlapping interval
                result.append([start, end])
                start, end = intervals[i]

        result.append([start, end])
        return result

Time Complexity
O(n log n)
Sorting dominates

Space Complexity
O(n)
Output list stores merged intervals
