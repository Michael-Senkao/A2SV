# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[nextZero] = nums[nextZero],nums[i]
                nextZero += 1
                