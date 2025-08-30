# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, size = 0):
        self.root = {i:i for i in range(size)}
        self.rank = [0]*size

    def find(self, node):
        if self.root[node] == node:
            return node
        return self.find(self.root[node])
    
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.root[parent_b] = parent_a
            elif self.rank[parent_b] > self.rank[parent_a]:
                self.root[parent_a] = parent_b
            else:
                self.root[parent_b] = parent_a
                self.rank[parent_a] += 1
            return True
        else:
            return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = UnionFind(n)
        for u,v in edges:
            if not graph.union(u-1,v-1):
                return [u,v]

        

        