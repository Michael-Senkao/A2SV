# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        def is_valid(r,c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            return True

        m,n = len(grid), len(grid[0])
        maxHeap = []
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        maxHealth = [[0 for _ in range(n)] for _ in range(m)]

        health -= grid[0][0]
        heapq.heappush(maxHeap, (-health, 0,0))
        maxHealth[0][0] = health


        
        while maxHeap:
            h,i,j = heappop(maxHeap)
            h = -h
            if h < maxHealth[i][j]:
                continue
            if (i,j) == (m-1, n-1):
                if h > 0:
                    return True
            else:
                for x,y in directions:
                    r,c = i + x, j + y
                    
                    if is_valid(r, c):
                        dh = h - grid[r][c]
                        if dh > maxHealth[r][c]:
                            maxHealth[r][c] = dh
                            heappush(maxHeap, ( -dh, r,c))


        return False

