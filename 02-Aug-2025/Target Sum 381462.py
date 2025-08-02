# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(index, val, nums, target):
            if index == len(nums):
                return 1 if val == target else 0
            if (index, val) in memo:
                return memo[(index, val)]
            neg = dp(index + 1, val - nums[index], nums, target)
            pos = dp(index + 1, val + nums[index], nums, target)

            memo[(index, val)] = neg + pos
            return memo[(index, val)]

        memo = {}
        return dp(0, 0, nums, target)