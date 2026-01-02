class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        LeetCode 66 – Plus One

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        n = len(digits)

        # Extra space needed only if all digits are 9
        if all(d == 9 for d in digits):
            n += 1

        ans = [-1] * n
        idx = n - 1
        carry = 1

        # Process digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            ans[idx] = total % 10
            carry = total // 10
            idx -= 1

        # If most significant position is still empty
        if ans[0] == -1:
            ans[0] = carry

        return ans
