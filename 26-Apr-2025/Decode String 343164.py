# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        currStr = ''
        stack = []

        for char in s:
            if char == ']':
                
                string = ''
                while stack[-1].isalpha():
                    string = stack[-1] + string
                    stack.pop()
                
                mult = ''
                stack.pop()
                while stack and stack[-1].isnumeric():
                    mult = stack[-1] + mult
                    stack.pop()

                stack.append(int(mult) * string)
            else:
                stack.append(char)
        return ''.join(stack)