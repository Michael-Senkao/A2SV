# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

import math
class Solution:
    def calcSum(self, divisor, nums):
        return sum(map(lambda x: math.ceil(x / divisor), nums))

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right  = 1, max(nums)
        res = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            _sum = self.calcSum(mid, nums)
           
            if _sum <= threshold:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res