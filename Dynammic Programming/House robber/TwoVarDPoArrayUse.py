class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Computes the maximum amount of money that can be robbed
        without robbing two adjacent houses.

        This approach does NOT modify the input array and uses
        constant extra space.
        """

        # next1 -> dp[i+1], next2 -> dp[i+2]
        next1, next2 = 0, 0

        # Traverse from right to left
        for i in range(len(nums) - 1, -1, -1):
            curr = max(nums[i] + next2, next1)
            next2 = next1
            next1 = curr

        return next1


Since dp[i] only depends on dp[i+1] and dp[i+2], we can optimize space by using two variables instead of a DP array.
