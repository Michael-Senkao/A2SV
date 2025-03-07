# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = [-1]*n

        intervals = [[start,end,index] for index, (start,end) in enumerate(intervals)]
        endHeap = []

        intervals.sort(key=lambda x: x[0])

        for start,end,index in intervals:
            while endHeap and endHeap[0][0] <= start:
                _,ind = heapq.heappop(endHeap)
                res[ind] = index
            if start == end:
                res[index] = index
            else:
                heapq.heappush(endHeap, (end, index)) 
        
        return res