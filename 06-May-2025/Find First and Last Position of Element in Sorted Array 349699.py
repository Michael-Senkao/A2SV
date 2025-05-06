# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def findFirst(self, nums, target):
        left,right = 0, len(nums) - 1
        ind = -1
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                ind = mid
                right = mid - 1

        return ind

    def findLast(self, nums, target):
        left,right = 0, len(nums) - 1
        ind = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                ind = mid
                left = mid + 1

        return ind
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findFirst(nums, target), self.findLast(nums, target)]