# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return 2*n if n & 1 else n