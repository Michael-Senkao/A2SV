# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i,j = 0,0
        res = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1 # Move to next child
            j += 1 # Move to next cookie

        return res
