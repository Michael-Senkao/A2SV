# Problem: Minimum Cost to Make at Least One Valid Path in a Grid - https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def updateCell(i,j, cost, canReach):
            if i < 0 or j < 0 or i == n or j == m:
                return False

            if not canReach:
                cost += 1

            if cost < costs[i][j]:
                costs[i][j] = cost
                return True
            return False

        n,m = len(grid), len(grid[0])
        costs= [[float('inf') for _ in range(m)] for _ in range(n)]
        costs[0][0] = 0
        
        min_heap = []
        heapify(min_heap)
       
       # (cost, row, col)
        heapq.heappush(min_heap, (0,0,0))

        while min_heap:
            cost,i,j = heapq.heappop(min_heap)
            # print(i,j, cost)
            if (i,j) == (n-1, m-1):
                # print(costs)
                return cost

            # Right
            if updateCell(i,j+1,cost, grid[i][j] == 1):
                heapq.heappush(min_heap, (costs[i][j+1], i, j+1))
            # Left
            if updateCell(i,j-1,cost, grid[i][j] == 2):
                heapq.heappush(min_heap, (costs[i][j-1], i, j-1))
            # Down
            if updateCell(i+1,j,cost, grid[i][j] == 3):
                heapq.heappush(min_heap, (costs[i+1][j], i+1, j))
            # Up
            if updateCell(i-1,j,cost, grid[i][j] == 4):
                heapq.heappush(min_heap, (costs[i-1][j], i-1, j))

        return 0
        