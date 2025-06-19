# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

    
        nums.sort(reverse=True)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                operations += i

        return operations