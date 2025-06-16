# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0

        for count in freq.values():
            res += count * (count - 1) // 2

        return res