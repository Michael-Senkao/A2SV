# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1

        res = []
        for i in range(n):
            if indegree[i] == 0:
                res.append(i)

        return res