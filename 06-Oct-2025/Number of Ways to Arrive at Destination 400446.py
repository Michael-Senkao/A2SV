# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        costs = [float('inf')] * n

        adj_list = defaultdict(list)

        for u,v,time in roads:
            adj_list[u].append((v, time))
            adj_list[v].append((u, time))

        minHeap = [(0,0)] # (cost,intersection)
        costs[0] = 0
        ways = [0] * n
        ways[0] = 1

        while minHeap:
            cost,curr = heapq.heappop(minHeap)
            if cost > costs[curr]:
                continue 
            
            for nei, time in adj_list[curr]:
                if costs[curr] + time < costs[nei]:
                    
                    costs[nei] = costs[curr] + time
                    ways[nei] = ways[curr] 
                    heapq.heappush(minHeap,(costs[nei], nei))
                elif costs[curr] + time == costs[nei]:
                    ways[nei] = (ways[nei] + ways[curr]) % MOD
   
        return ways[-1]