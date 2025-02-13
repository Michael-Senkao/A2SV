# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index = 0
        while index < n:
            correct_index = nums[index]
            if correct_index != index and nums[correct_index] != nums[index]:
                nums[index], nums[correct_index] = nums[correct_index], nums[index]
                pass
            else:
                index += 1

        print(nums)
        return [num for index,num in enumerate(nums) if num != index]