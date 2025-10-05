# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = 0

        for num in nums:
            XOR ^= num

        return XOR