# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def cyclicSort(self, nums):
        n = len(nums)
        i = 0

        while i < n:
            val = nums[i]
            if val != i + 1 and nums[val - 1] != val:
                nums[i], nums[val - 1] = nums[val - 1], val
                continue
            i += 1

    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        self.cyclicSort(nums)
        for i, num in enumerate(nums):
            if i + 1 != num:
                res.append(num)

        return res