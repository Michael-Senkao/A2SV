# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        
        n = len(nums)
        left = 0
        product = 1
        ans = 0
        for right in range(n):
            product *= nums[right]
           
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
        
            ans += right - left + 1
        
        return ans