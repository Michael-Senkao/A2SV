# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def helper(self, left, right, nums):
        if left > right:
            return -1

        mid = left + (right - left) // 2
        
        l = nums[mid - 1] if mid > 0 else float('-inf')
        r = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')
        
        if l < nums[mid] > r:
            return mid
        leftHalf = self.helper(left, mid - 1, nums)
        if leftHalf >= 0:
            return leftHalf
        return self.helper(mid + 1,right, nums)
        
    def findPeakElement(self, nums: List[int]) -> int:
        return self.helper(0, len(nums) - 1, nums)