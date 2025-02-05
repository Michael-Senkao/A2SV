# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        max_product = max(nums[0] * nums[1] * nums[-1], nums[-1]*nums[-2]*nums[-3])
        
        return max_product
