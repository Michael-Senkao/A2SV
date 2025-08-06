# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dp(index, prev, nums):
            if index == len(nums):
                return 0
            if memo[index] != -1:
                return memo[index]
            lis = 0
            for i in range(index, len(nums)):
                if nums[i] > prev:
                    lis = max(lis, 1 + dp(i + 1, nums[i], nums))
            memo[index] = lis
            return memo[index]

        return dp(0, float('-inf'), nums)