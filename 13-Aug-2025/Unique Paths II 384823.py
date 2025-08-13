# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0 for _ in range(n)] for _ in range(m)]

        paths[0][0] = 1
        for r in range(m):
            for c in range(n):
                if c + 1 < n and obstacleGrid[r][c + 1] == 0:
                    paths[r][c+1] += paths[r][c]
                if r + 1 < m and obstacleGrid[r + 1][c] == 0:
                    paths[r+1][c] += paths[r][c]

        return paths[-1][-1]