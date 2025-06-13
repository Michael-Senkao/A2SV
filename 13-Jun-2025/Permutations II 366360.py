# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def backtrack(self, indices, perm, nums, perms):
        if len(indices) == 0:
            perms.add(tuple(perm))

        for i in range(len(indices)):
            index = indices[i]
            perm.append(nums[index])
            self.backtrack(indices[:i] + indices[i + 1: ], perm, nums, perms)
            perm.pop()


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        indices = list(range(len(nums)))
        perms = set()
        self.backtrack(indices, [], nums, perms)

        return [list(perm) for perm in perms]
        