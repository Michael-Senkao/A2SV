# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(index, curr_sum):
            if curr_sum == amount:
                return 1
            if index >= n or curr_sum > amount:
                return 0
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            memo[(index, curr_sum)] = dp(index, curr_sum + coins[index]) + dp(index+1, curr_sum)
            return memo[(index, curr_sum)]

        n = len(coins)
        return dp(0, 0)