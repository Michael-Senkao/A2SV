# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endHeap = []
        
        for start,end in intervals:
            if endHeap and endHeap[0] < start:
                heapq.heappop(endHeap)
            heapq.heappush(endHeap, end)

        return len(endHeap)
        