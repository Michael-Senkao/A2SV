# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = [[]]

        for i in range(len(nums)):
            for j in range(len(sub_sets)):
                copy = sub_sets[j].copy()
                copy.append(nums[i])
                sub_sets.append(copy)

        return sub_sets