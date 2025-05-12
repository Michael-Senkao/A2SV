# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def helper(self, length, k):
        if length == 1:
            return 0

        half = length // 2
        if k <= half:
            return self.helper(half, k)
        elif k > half + 1:
            res = self.helper(half, 1 + length - k)
            return 1 ^ res # Invert the result
        else:
            return 1
            
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.helper(2**n - 1, k))