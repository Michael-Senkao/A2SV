# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        min_arrows = 1
        points.sort()
        max_start,min_end = points[0]

        for start,end in points:
            if start > min_end:
                min_arrows += 1
                max_start,min_end = start,end
            else:
                max_start = max(max_start, start)
                min_end = min(min_end, end)
        return min_arrows

