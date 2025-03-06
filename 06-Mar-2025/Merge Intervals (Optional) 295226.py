# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: (x[0], x[1]))
        res = []

        prevStart,prevEnd = intervals[0]
        

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prevEnd:
                prevEnd = max(prevEnd, intervals[i][1])
            else:
                res.append([prevStart, prevEnd])
                prevStart,prevEnd = intervals[i]

        res.append([prevStart, prevEnd])
        return res

