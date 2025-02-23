# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_XOR = reduce(lambda x,y: x ^ y, nums)
        
        operations = 0
        while total_XOR > 0 or k > 0:
            if total_XOR & 1 != k & 1:
                operations += 1
            k >>= 1
            total_XOR >>= 1
        return operations