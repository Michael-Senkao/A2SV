# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        size = len(piles)
        n = size // 3
        totalCoins = 0

        piles.sort()

        takeIndex = size - 2

        for _ in range(n):
            totalCoins += piles[takeIndex]
            takeIndex -= 2

        return totalCoins