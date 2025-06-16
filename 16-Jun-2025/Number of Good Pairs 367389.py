# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = 0

        for num in nums:
            res += freq[num]
            freq[num] += 1

        return res