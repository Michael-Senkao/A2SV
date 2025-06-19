# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        opposites = {
            1: [[0, -1, 1, 4, 6], [0,1, 1, 3, 5]],
            2: [[-1, 0, 2, 3, 4], [1, 0, 2, 5, 6]],
            3: [[0, -1, 1, 4, 6], [1, 0, 2, 5, 6]],
            4: [[1, 0, 2, 5, 6], [0, 1, 1, 3, 5]],
            5: [[-1, 0, 2, 3, 4], [0, -1, 1, 4, 6]],
            6: [[-1, 0, 2, 3, 4], [0, 1, 1, 3, 5]],
        }

        rows,cols = len(grid), len(grid[0])
        q = deque([(0,0)])
        visited = set([(0,0)]) # Mark start cell as visited

        while q:
            r,c = q.popleft()
            if (r,c) == (rows - 1, cols - 1):
                return True
            
            for opp in opposites[grid[r][c]]:
                dx = r + opp[0]
                dy = c + opp[1]
                if 0 <= dx < rows and 0 <= dy < cols and (dx,dy) not in visited and grid[dx][dy] in opp[2:]:
                    q.append((dx, dy))
                    visited.add((dx,dy))

        return False