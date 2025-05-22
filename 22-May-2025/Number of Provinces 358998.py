# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/


class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def find(self, child):
        if self.parents[child] == child:
            return child
        return self.find(self.parents[child])

    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)
        if parentA != parentB:
            self.parents[parentB] = parentA
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        provinces = 0
        
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j]:
                    dsu.union(i, j)
                    
        
        for i in range(n):
            if dsu.parents[i] == i:
                provinces += 1
        return provinces