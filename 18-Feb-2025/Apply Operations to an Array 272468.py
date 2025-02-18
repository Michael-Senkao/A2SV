# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        write_index,read_index = 0,0
        
        while read_index < n - 1:
            if nums[read_index] == 0:
                read_index += 1
                continue
            if nums[read_index + 1] == nums[read_index]:
                nums[read_index + 1] *= 2
                read_index += 1

            nums[write_index] = nums[read_index]
            read_index += 1
            write_index += 1

        if read_index < n and nums[read_index] > 0:
            nums[write_index] = nums[read_index]
            write_index += 1

        for i in range(write_index, n):
            nums[i] = 0

        return nums