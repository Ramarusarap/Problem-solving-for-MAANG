class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        x=events[0][0]
        y=events[0][1]
        sum=events[0][2]
        for i in range(1,len(events)):
            if events[i][0]>y:
                sum+=events[i][2]
                y=events[i][1]
            else:
                sum=max(sum,events[i][2])
                x=events[i][0]
                y=events[i][1]
        return sum



Input
events =
[[1,3,2],[4,5,2],[2,4,3]]

Use Testcase
Output
3
Expected
4
