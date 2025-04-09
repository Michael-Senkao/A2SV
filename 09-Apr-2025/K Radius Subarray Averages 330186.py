# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        res = [-1] * n

        if n < 2*k + 1:
            return res
        
        left = 0
        size = 2*k + 1
      
        total = sum(nums[: size - 1])

        for right in range(size - 1, n):
            total += nums[right]
            res[right - k] = total // size
            total -= nums[left]
            left += 1

        return res