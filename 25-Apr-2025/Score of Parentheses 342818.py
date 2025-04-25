# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)
            elif stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                score = 0
                while stack[-1] != '(':
                    score += stack[-1]
                    stack.pop()
                stack.pop()
                stack.append(2*score)
        return sum(stack)
        