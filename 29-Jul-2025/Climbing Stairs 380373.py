# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first,second = 1,2

        for _ in range(2, n):
            next_pos = first + second
            first = second
            second = next_pos
        
        return second