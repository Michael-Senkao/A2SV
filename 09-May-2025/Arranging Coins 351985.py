# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((math.sqrt(1 + 4*2*n) - 1) / 2)
        