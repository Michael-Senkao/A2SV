# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def can_finish(k):
            i = 0
            count = 0
            while i < n:
                count += ceil(piles[i]/k)
                i += 1
            return count <= h
        
        l,r = 1, max(piles)

        while l < r:
            mid = l + (r - l)//2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1

        return l