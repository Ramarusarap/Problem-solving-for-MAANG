class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        ns, ne = newInterval

        for s, e in intervals:
            # Case 1: interval completely before newInterval
            if e < ns:
                result.append([s, e])

            # Case 3: interval completely after newInterval
            elif s > ne:
                result.append([ns, ne])
                ns, ne = s, e  # treat current interval as the new interval

            # Case 2: overlapping interval
            else:
                ns = min(ns, s)
                ne = max(ne, e)

        # Append the final merged interval
        result.append([ns, ne])

        return result

Time & Space: O(n)
