# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
        '+': lambda a,b: a + b,
        '-': lambda a,b: a - b,
        '*': lambda a,b: a * b,
        '/': lambda a,b: int(a / b) # Makes sure to return an integer
        }

        stack = []
        for token in tokens:
            if token in operations:
                b,a = stack.pop(), stack.pop()
                res = operations[token](a,b)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]