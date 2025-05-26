# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n,m = len(name), len(typed)

        if m < n or name[0] != typed[0]:
            return False

        i = j = 0
        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
                
        while j < m and typed[j] == typed[j-1]:
            j += 1
            
        return i == n and j == m