# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        pairs = 0

        for num in nums:
            need = k - num

            if freq[need] > 0:
                pairs += 1
                freq[need] -= 1
            else:
                freq[num] += 1
        return pairs
