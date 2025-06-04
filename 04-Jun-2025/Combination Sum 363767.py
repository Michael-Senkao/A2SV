# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def backtrack(self, index, currSum, values, candidates, target, res):
        if currSum == target:
            res.add(tuple(values[:]))
        if index == len(candidates) or currSum > target:
            return
        
        values.append(candidates[index])
        self.backtrack(index, currSum + candidates[index], values, candidates, target, res)
        values.pop()
        self.backtrack(index + 1, currSum, values, candidates, target, res)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        self.backtrack(0, 0, [], candidates, target, res)
        
        return [list(vals) for vals in res]