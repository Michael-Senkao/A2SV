# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calculate(self, c, d, graph):
        if c not in graph or d not in graph:
            return -1.0
        if c == d:
            return 1

        q = deque()
        q.append((c, 1))
        visited = set([c])

        while q:
            node,product = q.popleft()

            if node == d:
                return product # Target found

            for nei, factor in graph[node]:
                if nei not in visited:
                    q.append((nei, factor * product))
                    visited.add(nei)
        return -1


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        # Create the graph
        for i, (u,v) in enumerate(equations):
            graph[u].append((v,values[i]))
            graph[v].append((u,1 / values[i] if values[i] else 0))
     
        ans = []
        # Iterate over queries and solve for wach query
        for c,d in queries:
            ans.append(self.calculate(c,d,graph))

        return ans