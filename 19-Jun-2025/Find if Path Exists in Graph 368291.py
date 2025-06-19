# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import defaultdict, deque

class Solution:
    def hasValidPath(self, source, destination, graph):
        visited = set()
        q = deque([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        return False

        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return self.hasValidPath(source, destination, graph)