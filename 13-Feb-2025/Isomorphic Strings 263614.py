# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapped_s = {}
        mapped_t = set()
        

        for i in range(n):
            if s[i] not in mapped_s:
                if t[i] not in mapped_t:
                    mapped_s[s[i]] = t[i]
                    mapped_t.add(t[i])
                else:
                    return False
            elif mapped_s[s[i]] != t[i]:
                return False
        return True