# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(index, curr_sum, half_sum):
            if curr_sum == half_sum:
                return True

            if index == len(nums) or curr_sum > half_sum:
                return False
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            memo[(index, curr_sum)] = dp(index + 1, curr_sum + nums[index], half_sum) or dp(index + 1, curr_sum, half_sum)
            return memo[(index, curr_sum)]

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        half_sum = total_sum // 2
        return dp(0, 0, half_sum)