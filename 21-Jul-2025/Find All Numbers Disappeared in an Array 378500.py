# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        i = 0
        while i < n:
            num = nums[i]
            if num == i + 1 or nums[num - 1] == num:
                i += 1
            else:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
        
        for i,num in enumerate(nums):
            if i + 1 != num:
                res.append(i + 1)
        return res