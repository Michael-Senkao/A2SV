# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        degrees = [0] * n

        for u,v in edges:
            degrees[v-1] += 1
            degrees[u-1] += 1

        for index, deg in enumerate(degrees):
            if deg == n - 1:
                return index + 1
        return -1 