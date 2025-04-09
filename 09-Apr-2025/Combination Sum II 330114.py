# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, currSum, vals):
            if currSum == target:
                res.append(vals.copy())
                return

            if currSum > target or index == len(candidates):
                return

            
            
            vals.append(candidates[index])
            backtrack(index + 1, currSum + candidates[index], vals)
            vals.pop()

            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                index += 1
            backtrack(index + 1, currSum, vals)
           
            


        res = []
        candidates.sort()
        backtrack(0, 0, [])
    
        return res