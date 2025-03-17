# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n,m = len(firstList), len(secondList)
        ans = []

        i,j = 0,0
        while i < n and j < m:
            if firstList[i][0] > secondList[j][1]:
                j += 1
            elif secondList[j][0] > firstList[i][1]:
                i += 1
            else:
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                ans.append([start,end])

                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1

        return ans

        