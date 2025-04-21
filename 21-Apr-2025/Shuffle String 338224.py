# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        string = [""]*n

        for i in range(n):
            string[indices[i]] = s[i]
            
        return "".join(string)