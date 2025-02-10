# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index, n):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            memo[index] = max(dp(index+1, n), dp(index+2, n) + nums[index])
           
            return memo[index]

        n = len(nums)
        if n==1:
            return nums[0]
        memo = {}
        result = dp(0, n-1)
        memo = {}
        result = max(result, dp(1, n))
        return result