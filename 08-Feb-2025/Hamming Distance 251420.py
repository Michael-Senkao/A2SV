# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def countSetBits(self, num: int) -> int:
        set_bit_count = 0
        while num > 0:
            set_bit_count += (num & 1)
            num >>= 1
        return set_bit_count
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        return self.countSetBits(xor)
        