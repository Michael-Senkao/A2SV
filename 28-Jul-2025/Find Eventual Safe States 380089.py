# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adjList = defaultdict(list)
        indegree = [0] * n

        for v in range(n):
            for u in graph[v]:
                adjList[u].append(v)
                indegree[v] += 1

       
        q = deque()
        safe_nodes = []
        for v in range(n):
            if indegree[v] == 0:
                safe_nodes.append(v)
                q.append(v)

      
        while q:
            node = q.popleft()
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    safe_nodes.append(nei)
        return sorted(safe_nodes)