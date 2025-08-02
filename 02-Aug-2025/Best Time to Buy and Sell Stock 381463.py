# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)

        return max_profit