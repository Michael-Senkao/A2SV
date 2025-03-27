# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextZeroIndex = 0
        nextTwoIndex = len(nums) - 1
        currIndex = 0

        while currIndex <= nextTwoIndex:
           
            if nums[currIndex] == 2:
                nums[currIndex],nums[nextTwoIndex] = nums[nextTwoIndex],nums[currIndex]
                nextTwoIndex -= 1
                continue
            elif nums[currIndex] == 0:
                nums[currIndex],nums[nextZeroIndex] = nums[nextZeroIndex],nums[currIndex]
                nextZeroIndex += 1
            
            currIndex += 1