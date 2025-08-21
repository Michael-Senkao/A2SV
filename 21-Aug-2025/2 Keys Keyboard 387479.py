# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:

        curr_length = 1
        copied_length = 0
        steps = 0

        while curr_length != n:
            if n % curr_length == 0:
                copied_length = curr_length
                steps += 1
            curr_length += copied_length
            steps += 1
        return steps
        