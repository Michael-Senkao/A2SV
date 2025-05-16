# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def canTake(self, candy, candies, k):
        n = len(candies)
        ind = 0
        person = 0
        while ind < n and person < k:
            person += candies[ind] // candy
            ind += 1
        return person >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        
        total = sum(candies)
        if total < k:
            return 0
        res = 0
        left, right = 1, max(candies)
        while left <= right:
            mid = left + (right - left)//2

            if self.canTake(mid,candies,k):
                
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return res

