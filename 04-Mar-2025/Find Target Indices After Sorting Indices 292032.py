# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        lessCount = 0
        count = 0

        for num in nums:
            if num < target:
                lessCount += 1
            elif num == target:
                count += 1
        
        
        return list(range(lessCount, lessCount + count))