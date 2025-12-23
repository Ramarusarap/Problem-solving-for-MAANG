class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges all overlapping intervals and returns the merged result.

        Approach:
        - Sort intervals by start time
        - Maintain a current interval [x, y]
        - Compare each interval with the current one and merge if overlapping
        """

        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        result = []

        # Initialize the first interval
        x = intervals[0][0]
        y = intervals[0][1]

        for i in range(len(intervals)):
            # Case 1: Current interval overlaps with [x, y]
            if intervals[i][0] <= y and intervals[i][0] >= x:
                # Extend the end of the current interval if needed
                y = max(intervals[i][1], y)

            # Case 2: Current interval is completely inside [x, y] on the left
            elif intervals[i][0] <= x and intervals[i][1] <= y:
                # Update start to the smaller value
                x = intervals[i][0]

            # Case 3: Current interval completely covers [x, y]
            elif intervals[i][0] < x and intervals[i][1] > y:
                # Expand both start and end
                x = intervals[i][0]
                y = intervals[i][1]

            # Case 4: No overlap with current interval
            else:
                # Push the previous interval to result
                result.append([x, y])

                # Start tracking a new interval
                x = intervals[i][0]
                y = intervals[i][1]

        # Append the last tracked interval
        result.append([x, y])

        return result

Time Complexity
O(n log n)
Sorting the intervals dominates the runtime.

Space Complexity
O(n)
Result list stores merged intervals.
