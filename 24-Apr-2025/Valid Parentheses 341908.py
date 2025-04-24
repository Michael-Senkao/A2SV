# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in valid_pairs:
                stack.append(ch)  # Push opening bracket onto stack
            elif stack and valid_pairs[stack[-1]] == ch:
                stack.pop()  # Valid closing bracket found, remove matching open bracket
            else:
                return False  # Mismatched bracket
        
        return not stack  # Stack should be empty if all brackets matched
