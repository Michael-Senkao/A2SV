# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                stack.pop()

        return "".join(stack)