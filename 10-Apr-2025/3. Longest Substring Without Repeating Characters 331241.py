# Problem: 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0

        windowElements = set()
        res = 0

        for right in range(n):
            
            currChar = s[right]
            while currChar in windowElements:
                windowElements.remove(s[left])
                left += 1

            windowElements.add(currChar)
            res = max(res, len(windowElements))


        return res