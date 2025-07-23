# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        start = end = -1

        for i in range(n):
            found = set()
            distinct = 0
            for j in range(i, n):
                if s[j].swapcase() in found:
                    found.add(s[j])
                elif s[j] not in found:
                    distinct += 1
                    found.add(s[j])

                if 2*distinct == len(found) and j - i > end - start:
                    start,end = i,j
                


        return "" if start == -1 else s[start: end + 1]
        