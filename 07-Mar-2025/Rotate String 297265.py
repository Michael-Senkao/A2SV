# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        return len(s) == len(goal) and (s + s).find(goal) != -1