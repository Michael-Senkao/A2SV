# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

from collections import deque

class Solution:
    def markVisited(self, i, j, grid):
        rows,cols = len(grid), len(grid[0])
        q = deque([(i,j)])
        grid[i][j] = '0'
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r,c = q.popleft()
            for x,y in directions:
                dx = r + x
                dy = c + y
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == '1':
                    q.append((dx, dy))
                    grid[dx][dy] = '0'

    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    self.markVisited(i,j, grid)

        return num_islands