# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        i = len(piles) - 2

        total_coins = 0

        for _ in range(n):
            total_coins += piles[i]
            i -= 2
        
        return total_coins