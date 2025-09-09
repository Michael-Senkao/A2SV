# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            right_index = nums[i] - 1
            if (0 <= right_index < n) and right_index != i and nums[right_index] != nums[i]:
                nums[i], nums[right_index] = nums[right_index], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1