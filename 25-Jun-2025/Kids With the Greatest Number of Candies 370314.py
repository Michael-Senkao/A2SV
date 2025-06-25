# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        n = len(candies)
        maxC = max(candies)
        res = [False] * n

        for i in range(n):
            res[i] = candies[i] + extraCandies >= maxC
        return res