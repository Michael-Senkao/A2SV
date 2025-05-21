# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(prev, index):
            if index == len(s):
                return True
            
            for j in range(index,  len(s)):
                current = int(s[index: j + 1])
                if prev - current == 1 and dfs(current, j + 1):
                    return True
            return False
        for i in range(len(s) - 1):
            var = int(s[: i + 1])
            if dfs(var, i+1):
                return True
        return False
        