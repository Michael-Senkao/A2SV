# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-stones for stones in piles]
        heapq.heapify(maxHeap)

        while maxHeap and k:
            maxV = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, maxV // 2)
            
            k -= 1

        return -sum(maxHeap) if maxHeap else 0
            