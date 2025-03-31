# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefixProduct = 1

        for num in nums:
            res.append(prefixProduct)
            prefixProduct *= num

        suffixProduct = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffixProduct
            suffixProduct *= nums[i]

        return res