# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        left,right = 0, len(s) - 1
        swaps = 0

        while left < right:
            if s[right] == '1':
                right -= 1
            elif s[left] == '0':
                left += 1
            else:
                swaps += right - left
                left += 1
                right -= 1

        return swaps