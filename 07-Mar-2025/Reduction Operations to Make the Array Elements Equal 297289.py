# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        distinct = 0
        maxOperation = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                distinct += 1
            maxOperation += distinct

        return maxOperation