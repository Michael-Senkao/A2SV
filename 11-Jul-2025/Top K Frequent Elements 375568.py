# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        k_freq = []

        for key, count in freq.items():
            heapq.heappush(k_freq, (count, key))
            if len(k_freq) > k:
                heapq.heappop(k_freq)

        return [key for _,key in k_freq]
