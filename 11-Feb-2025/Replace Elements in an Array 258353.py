# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        nums_to_index = {num:index for index, num in enumerate(nums)}
       
        for prev_num,new_num in operations:
            index = nums_to_index[prev_num]
            nums[index] = new_num
            nums_to_index[new_num] = index
            del nums_to_index[prev_num]

        return nums