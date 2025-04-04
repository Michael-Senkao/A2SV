# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
     
        def dp(index, currSum):
            if currSum == target:
                return 1
            if currSum > target or index == n:
                return 0

            if memo[index][currSum] != -1:
                return memo[index][currSum]
            count = 0
            for i in range(n):
                count += dp(i, currSum + nums[i])

            memo[index][currSum] = count
            return memo[index][currSum]

        n = len(nums)
        memo = [[-1 for _ in range(target)] for _ in range(n)]
        return dp(0, 0)
        