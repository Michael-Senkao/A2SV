# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def dfs(self, node, graph, visited, vals):
        if node in visited:
            return
        visited.add(node)
        vals.append(node)
        for nei  in graph[node]:
            self.dfs(nei, graph, visited, vals)


    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = defaultdict(list)
        res = [None] * n

        for u,v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        for i in range(n):
            vals = []
            self.dfs(i, graph, visited, vals)

            sorted_vals = sorted(vals, key=lambda ind: s[ind])
            vals.sort()
            
            j = 0
            for indx in vals:
                res[indx] = s[sorted_vals[j]]
                j += 1
            
        
        return ''.join(res)