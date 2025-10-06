# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        costs = {node: float("inf") for node in range(1, n+1)} # Stores the cost to reach each node in the network
        
        # Represent the network as a graph
        for u,v,w in times:
            graph[u].append((v,w))

        visited = set()
        heap = [(0, k)] #(cost, node)
        heapify(heap)
        costs[k] = 0
        

        while heap:
            current_cost, current_node = heappop(heap)
            if current_node in visited:
                continue
            costs[current_node] = current_cost
            visited.add(current_node) 

            for neighbor, cost in graph[current_node]:
                heappush(heap, (current_cost + cost, neighbor))

        if len(visited) != n: # All nodes cannot be visited
            return -1
        return max(costs.values())