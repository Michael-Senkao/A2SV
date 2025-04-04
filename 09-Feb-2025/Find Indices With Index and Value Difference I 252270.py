# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mini = maxi = 0
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[mini]: mini = i - indexDifference
            if nums[i - indexDifference] > nums[maxi]: maxi = i - indexDifference
            if nums[i] - nums[mini] >= valueDifference: 
                return [mini, i]
            if nums[maxi] - nums[i] >= valueDifference: 
                return [maxi, i]
        return [-1, -1]
            

        return [-1, -1]

        