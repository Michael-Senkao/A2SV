# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def backtrack(self, i, n, k, curr, res):
        if len(curr) == k:
            res.append(curr.copy())
            return
        if i > n:
            return
        
        curr.append(i)
        self.backtrack(i + 1, n, k, curr, res) # Take
        curr.pop()
        self.backtrack(i + 1, n, k, curr, res) # Don't take

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(1, n, k, [], res)
        return res