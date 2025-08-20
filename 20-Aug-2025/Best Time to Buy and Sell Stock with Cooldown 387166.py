# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dp(index, has_stock):
            if index >= len(prices):
                return 0
            if (index, has_stock) in memo:
                return memo[(index, has_stock)]
            
            take = skip = None
            if has_stock:
                take = prices[index] + dp(index + 2, False)
                skip = dp(index + 1, True)
            else:
                take = dp(index + 1, True) - prices[index]
                skip = dp(index + 1, False)

            memo[(index, has_stock)] = max(take, skip)
            return memo[(index, has_stock)]

        return dp(0, False)