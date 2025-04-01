# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        numStr = bin(n)[2:]

        for i in range(1, len(numStr)):
            if numStr[i] == numStr[i-1]:
                return False

        return True