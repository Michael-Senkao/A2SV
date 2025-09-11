# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_v,min_v = float('-inf'), float('inf')

        for num in nums:
            max_v = max(max_v, num)
            min_v = min(min_v, num)
        
        if max_v % min_v == 0:
            return min_v

        ans = 1
        for i in range(2, min_v):
            if min_v % i == 0 and max_v % i == 0:
                ans = i

        return ans