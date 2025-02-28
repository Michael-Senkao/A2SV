# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def helper(index, prev_jump, next_pos):
    
            if index >= len(stones):
                return False
            if stones[index] > next_pos:
                return False
            if stones[index] < next_pos:
                return helper(index + 1, prev_jump, next_pos)
            if index == len(stones) - 1:
                return True
            return (
                helper(index + 1, prev_jump - 1, stones[index] + prev_jump - 1) or 
                helper(index + 1, prev_jump, stones[index] + prev_jump) or 
                helper(index + 1, prev_jump + 1, stones[index] + prev_jump + 1)
            )

        return helper(0, 0, stones[0])
            