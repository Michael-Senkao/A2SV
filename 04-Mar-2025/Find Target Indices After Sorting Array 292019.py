# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        lessCount = 0
        count = 0

        for num in nums:
            if num < target:
                lessCount += 1
            elif num == target:
                count += 1
        
        if count == 0:
            return []
        
        return list(range(lessCount, lessCount + count))