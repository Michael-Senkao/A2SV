# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        seen = [False] * 26
        freq = [0] * 26
        res = []

        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        stack = []
        for char in s:
            indx = ord(char) - ord('a')
            freq[indx] -= 1
            if seen[indx]: 
                continue
            seen[indx] = True

            while stack and stack[-1] > char and freq[ord(stack[-1]) - ord('a')] > 0:
                ch = stack.pop()
                seen[ord(ch) - ord('a')] = False
            
            stack.append(char)
        
        return ''.join(stack)