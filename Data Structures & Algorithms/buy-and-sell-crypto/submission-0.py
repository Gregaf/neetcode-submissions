class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        profit_max = 0

        # Brute force approach O(n^2)
        for i in range(len(prices) - 1):
            day_price = prices[i]
            for j in range(i + 1, len(prices), 1):
                profit_max = max(profit_max, prices[j] - day_price)

        return profit_max

    