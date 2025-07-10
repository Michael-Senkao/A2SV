# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            first,second = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if first < second:
                first -= second
                heapq.heappush(max_heap, first)

        return -max_heap[0] if max_heap else 0