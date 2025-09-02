# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/


class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.minDist = [float('inf')] * n

    def find(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, a, b, dist):
        parA = self.find(a)
        parB = self.find(b)

        if parA != parB:
            if self.rank[parB] > self.rank[parB]:
                self.parents[parA] = parB
            elif self.rank[parA] > self.rank[parB]:
                self.parents[parB] = parA
            else:
                self.parents[parB] = parA
                self.rank[parA] += 1
        
        minDist = min(self.minDist[parA], self.minDist[parB], dist)
        self.minDist[parA] = minDist
        self.minDist[parB] = minDist
        self.minDist[a] = minDist
        self.minDist[b] = minDist

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        dsu = DSU(n)
        for u,v,d in roads:
            dsu.union(u - 1, v - 1, d)

    
        return dsu.minDist[dsu.parents[0]]
        