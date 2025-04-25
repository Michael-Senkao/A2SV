# Problem: Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        count = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                count = 1
            else:
                count += 1
            if count < 3:
                nums[k] = nums[i]
                k += 1

        return k
        