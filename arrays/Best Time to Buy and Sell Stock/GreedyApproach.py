class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit from a single buy and sell.

        Greedy Strategy:
        - Track the lowest buying price seen so far
        - At each day, calculate profit if sold today
        - If a lower price is found, greedily reset the buying point

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if len(prices) < 2:
            return 0

        buy = 0          # index of minimum price so far
        max_profit = 0  # maximum profit found

        for sell in range(1, len(prices)):
            # Greedy choice: if current price is lower, buy here
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                # Try selling today and update max profit
                max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit
