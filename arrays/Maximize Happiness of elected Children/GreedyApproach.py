class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort happiness values in ascending order
        # We will iterate from the end to pick the largest values first
        happiness.sort()

        total = 0      # Stores the final maximum happiness sum
        dec = 0        # Represents the decrement applied after each selection

        # Traverse from the largest happiness values
        for i in range(len(happiness) - 1, -1, -1):
            # Stop once k elements are selected
            if k == 0:
                break

            # Current happiness after decrement
            current = happiness[i] - dec

            # Only add if the contribution is positive
            if current > 0:
                total += current   # Add adjusted happiness
                dec += 1            # Increase decrement for next pick
                k -= 1              # One selection used

        return total

⏱️ Time Complexity

Sorting: O(n log n)
Loop: O(n) (but breaks after k)
Overall: O(n log n) ✅ (optimal)

💾 Space Complexity

Sorting in-place
Extra variables only

O(1) extra space ✅
