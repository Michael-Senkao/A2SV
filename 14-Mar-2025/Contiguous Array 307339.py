# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
    
        found = {0: -1}
        res = 0
        count = 0

        for index,num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1

            if count in found:
                size = index - found[count]
                res = max(res, size)
            else:
                found[count] = index

        return res