# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        can_reach = 0

        for i in range(len(nums)):
            if i > can_reach:
                return False
                
            can_reach = max(can_reach, i + nums[i])
            if can_reach >= n - 1:
                return True

        return True