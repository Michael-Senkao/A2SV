# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def backtrack(self, left, right, generated, res):
        if left == 0 and right == 0:
            res.append(''.join(generated))
        if left:
            generated.append('(')
            self.backtrack(left - 1, right, generated, res)
            generated.pop()
        if right > left:
            generated.append(')')
            self.backtrack(left, right - 1, generated, res)
            generated.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(n,n,[],res)
        return res
        