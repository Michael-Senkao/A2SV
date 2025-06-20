# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def dfs(self, node, color, colors, adjList):
        colors[node] = color
        for nei in adjList[node]:
            if colors[nei] == -1:
                if not self.dfs(nei, color ^ 1, colors, adjList):
                    return False
            elif colors[nei] == color:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        adjList = defaultdict(list)
        for u in range(n):
            for v in graph[u]:
                adjList[u].append(v)
                adjList[v].append(u)

        for node in range(n):
            if colors[node] == -1 and not self.dfs(node, 0, colors, adjList):
                return False
        
        return True