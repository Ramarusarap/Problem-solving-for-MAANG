
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Computes the maximum amount of money that can be robbed
        without robbing two adjacent houses.

        This solution uses Bottom-Up Dynamic Programming and
        modifies the input array in place to achieve O(1) extra space.
        """

        # Append two dummy zeros to safely handle dp[i+1] and dp[i+2]
        nums.append(0)
        nums.append(0)

        # Process houses from right to left
        for i in range(len(nums) - 3, -1, -1):
            # Decide whether to rob the current house or skip it
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

        # nums[0] now contains the maximum amount that can be robbed
        return nums[0]

Time Complexity

O(n)
Single pass through the list
Space Complexity

O(1) (extra space)
No additional DP array
Input array reused
