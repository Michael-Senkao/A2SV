# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        max_non_overlap = 1
        intervals.sort(key=lambda x: x[-1])
        prev_end = intervals[0][-1]
        for i in range(1, n):
            start,end = intervals[i]
            if start >= prev_end:
                max_non_overlap += 1
                prev_end = end

        return n - max_non_overlap
