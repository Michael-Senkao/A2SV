# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def dfs(self, r, c, grid):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
            grid[r][c] = 0
            return (
                1 +
                self.dfs(r + 1, c, grid) +
                self.dfs(r - 1, c, grid) +
                self.dfs(r, c + 1, grid) +
                self.dfs(r, c - 1, grid)
            )
        return 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_area = max(max_area, self.dfs(r,c, grid))

        return max_area