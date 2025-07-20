# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        min_arrows = 1
        points.sort()
        min_end = points[0][-1]

        for start,end in points:
            if start > min_end:
                min_arrows += 1
                min_end = end
            else:
                min_end = min(min_end, end)
        return min_arrows

