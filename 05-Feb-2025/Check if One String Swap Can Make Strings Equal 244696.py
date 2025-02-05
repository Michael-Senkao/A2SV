# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)

        first_err = -1
        for index in range(n):
            if s1[index] != s2[index]:
                if first_err == -1:
                    first_err = index
                elif first_err >= 0 and s2[first_err] == s1[index] and s1[first_err] == s2[index]:
                    first_err = -2 # One swap has been done
                else:
                    return False
                
        return first_err < 0