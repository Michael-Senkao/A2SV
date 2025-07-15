# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        k = 2
        res = 0
        for i in range(1, n):
            min_sum = nums[i] + nums[i-1]
            while k < n and min_sum > nums[k]:
                k += 1

            if k - 1 > i:
                res = max(res, min_sum + nums[k - 1])
        
        return res