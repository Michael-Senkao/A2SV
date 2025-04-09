# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freq = [0] * 3
        need = set(['a', 'b', 'c'])
        left = 0
        res = 0

        for i in range(n):
            if s[i] not in need:
                continue

            freq[ord(s[i]) - 97] += 1
            while all(freq):
                res += n - i
                if s[left] in need:
                    freq[ord(s[left]) - 97] -= 1

                left += 1

        return res