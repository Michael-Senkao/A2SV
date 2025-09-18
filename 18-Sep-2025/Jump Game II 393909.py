# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps = 0
        indx = 0
        canReach = 0

        while canReach < n - 1:
            min_jumps += 1
            for j in range(indx, canReach + 1):
                canReach = max(canReach, nums[j] + j)
                if canReach >= n - 1:
                    return min_jumps
            i = j
            
        return min_jumps