# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = [-1] * n
        edges = [redEdges, blueEdges]

        for index, (a,b) in enumerate(redEdges):
            graph[a].append((0, index))
        for index, (a,b) in enumerate(blueEdges):
            graph[a].append((1, index))
        
        visited = set()
        res[0] = 0
        q = deque()
        for edgeType, indx in graph[0]:
            q.append((edgeType, indx, 1))
            visited.add((edgeType, indx))
        
        while q:
            edgeType, indx, length = q.popleft()
            node = edges[edgeType][indx][-1]
            if res[node] < 0:
                res[node] = length

            for neiType, index in graph[node]:
                if (neiType, index) not in visited and neiType != edgeType:
                    q.append((neiType, index, length + 1))
                    visited.add((neiType, index))

        return res
        