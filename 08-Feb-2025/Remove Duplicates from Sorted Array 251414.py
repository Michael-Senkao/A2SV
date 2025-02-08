# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        next_unique_index = 1

        for index in range(1, n):
            if nums[index] != nums[index - 1]:
                nums[next_unique_index] = nums[index]
                next_unique_index += 1
        
        return next_unique_index