# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        max_prob = [0]*n
        max_prob[start_node] = 1
     
        for i in range(len(edges)):
            u,v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        q = []
        heapq.heappush(q, (-1, start_node))

        while q:
            prob, curr = heapq.heappop(q)
            prob = -prob
            if prob < max_prob[curr]:
                continue
            if curr == end_node:
                return prob
            for nei, p in graph[curr]:
                dp = prob * p
                if dp > max_prob[nei]:
                    max_prob[nei] = dp
                    heapq.heappush(q, (-dp, nei))
        
        return 0


        