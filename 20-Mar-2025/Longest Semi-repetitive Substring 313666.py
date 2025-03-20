# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        longestSemi = 0
        semiStart = -1
        left = 0

        for i in range(1, n):
            if s[i] == s[i-1]:
                left = semiStart + 1
                semiStart = i-1
            
            longestSemi = max(longestSemi, i - left + 1)
        
        return longestSemi
        