# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def check(self, left, right, s, n):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right


    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longestStart = 0
        longestStart, longestEnd = 0,1

        for i in range(1, n):
            start,end = self.check(i, i, s, n)
            if end - start > longestEnd - longestStart:
                longestStart, longestEnd = start,end

            start,end = self.check(i - 1, i, s, n)
            if end - start > longestEnd - longestStart:
                longestStart, longestEnd = start,end

        return s[longestStart: longestEnd]