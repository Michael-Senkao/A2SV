# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(index, curr_amount, coins, target_amount):
            if curr_amount == target_amount:
                return 0
            if index == len(coins) or curr_amount > target_amount:
                return float('inf')
            
            if (index, curr_amount) in memo:
                return memo[(index, curr_amount)]
            cost = float('inf') 
            
            for i in range(index, len(coins)):
                x = 1 + dp(i, curr_amount + coins[index], coins, target_amount)
                cost = min(cost, x)
            cost = min(cost, dp(index + 1, curr_amount, coins, target_amount))
            memo[(index, curr_amount)] = cost
            return memo[(index, curr_amount)]

        memo = {}
        coins.sort(reverse=True)
        ans = dp(0, 0, coins, amount)
        return -1 if ans == float('inf') else ans