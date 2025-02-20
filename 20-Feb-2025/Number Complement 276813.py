# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        pos = 0
        while num > 0:
            bit = (num & 1) ^ 1
            complement += bit * ( 1 << pos)
            num >>= 1
            pos += 1
        return complement