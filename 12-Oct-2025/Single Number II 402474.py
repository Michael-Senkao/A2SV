# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for key,val in freq.items():
            if val == 1:
                return key
        