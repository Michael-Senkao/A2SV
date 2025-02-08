# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_element = float('inf')
        majority_count = 0

        for num in nums:
            if majority_count == 0:
                majority_element = num
                majority_count = 1
            elif num == majority_element:
                majority_count += 1
            else:
                majority_count -= 1
        return majority_element

