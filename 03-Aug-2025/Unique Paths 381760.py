# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        grid[0][0] = 1
        for r in range(m):
            for c in range(n):
                if c + 1 < n:
                    grid[r][c+1] += grid[r][c]
                if r + 1 < m:
                    grid[r+1][c] += grid[r][c]

        return grid[-1][-1]