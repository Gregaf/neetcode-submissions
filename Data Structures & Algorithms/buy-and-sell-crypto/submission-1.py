class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        profit_max = 0

        l = 0
        r = l + 1

        # O(n) time complexity each element is visited atleast once
        # O(1) space complexity due to a pointer based approach
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                profit_max = max(profit_max, profit)
                r += 1
            else:
                l = r
                r += 1
        
        return profit_max
    