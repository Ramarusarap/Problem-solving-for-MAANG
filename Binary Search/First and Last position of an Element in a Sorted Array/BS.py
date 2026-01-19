class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        The comments are Chat PT generated for better understanding------------------------------------------------------------>
        Time Complexity: O(log n)
        Space Complexity: O(1)

        Approach:
        - Use binary search to find:
          1) Lower bound  -> first index where nums[i] >= target
          2) Upper bound  -> first index where nums[i] > target
        - The answer range is [lower_bound, upper_bound - 1]
        """

        def lower_bound():
            low, high = 0, len(nums)

            # ❌ Original mistake:
            # Used while (low < high) with high = mid - 1
            # This mixes half-open interval logic with inclusive updates.
            # ✅ Fix: For low < high pattern, use high = mid (do NOT discard mid)

            while low < high:
                mid = (low + high) // 2

                # ❌ Original mistake:
                # Returning mid or mid-1 directly
                # mid is NOT guaranteed to be the boundary
                # ✅ Fix: Always return low after convergence

                if nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1

            return low

        def upper_bound():
            low, high = 0, len(nums)

            # ❌ Original mistake:
            # Same boundary violation as lower bound
            # ❌ Incorrectly used high = mid - 1 with low < high
            # ✅ Fix: Maintain half-open invariant [low, high)

            while low < high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    high = mid
                else:
                    low = mid + 1

            return low

        lb = lower_bound()
        ub = upper_bound() - 1

        # ❌ Original mistake:
        # No validation for target existence
        # ✅ Fix: Check bounds and value explicitly

        if lb <= ub and lb < len(nums) and nums[lb] == target:
            return [lb, ub]

        return [-1, -1]
