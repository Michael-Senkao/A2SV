# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index):
            if index >= n:
                return 0
            if memo[index] != -1:
                return memo[index]
            memo[index] = max(dp(index+1), dp(index+2) + nums[index])
           
            return memo[index]

        n = len(nums)
        memo = [-1] * n
        
        return dp(0)