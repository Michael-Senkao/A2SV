# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pairs_formed = 0

        freq = Counter(nums)
        for val in freq.values():
            pairs_formed += (val // 2)

        return [pairs_formed, n - 2*pairs_formed]