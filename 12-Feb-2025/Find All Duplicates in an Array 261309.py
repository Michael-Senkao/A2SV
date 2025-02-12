# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        index = 0
        # Use cyclic sort to sort nums
        while index < n:
            right_index = nums[index] - 1
            if right_index != index and nums[right_index] != right_index + 1:
                nums[right_index], nums[index] = nums[index], nums[right_index]
            else:
                index += 1
        
        # Find indexes that do not match their values
        for i in range(n):
            if i + 1 != nums[i]:
                res.append(nums[i])

        return res
                