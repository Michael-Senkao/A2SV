# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)// 3
        totalCoins = 0

        piles.sort()

        takeIndex = len(piles) - 2

        for _ in range(n):
            totalCoins += piles[takeIndex]
            takeIndex -= 2

        return totalCoins