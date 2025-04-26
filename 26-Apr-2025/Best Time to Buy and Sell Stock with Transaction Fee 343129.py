# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def dp(index, hasStock, prices, fee):
            if index == len(prices):
                return 0
            if memo[index][hasStock] != -1:
                return memo[index][hasStock]
            if hasStock:
                sell = prices[index] - fee + dp(index + 1, False, prices, fee)
                not_sell = dp(index + 1, True, prices, fee)
                memo[index][hasStock] = max(sell, not_sell)
            else:
                buy = -prices[index] + dp(index + 1, True, prices, fee)
                not_buy = dp(index + 1, False, prices, fee)
                memo[index][hasStock] = max(buy, not_buy)
            return memo[index][hasStock]

        memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return dp(0, False, prices, fee)