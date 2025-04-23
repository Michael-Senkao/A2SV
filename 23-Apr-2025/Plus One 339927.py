# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        index = len(digits) - 1
        while index >= 0 and digits[index] > 8:
            digits[index] = 0
            index -= 1

        if index >=0:
            digits[index] += 1
            return digits
        return [1] + digits
        