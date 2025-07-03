# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat), len(mat[0])
        visited = set()
        distanceMat = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        directions = [(1,0), (0,1), (-1, 0), (0,-1)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                    distanceMat[r][c] = 0

        while q:
            r,c, dist = q.popleft()
            for x,y in directions:
                dx = x + r
                dy = y + c
                if 0 <= dx < rows and 0 <= dy < cols and mat[dx][dy]:
                    distanceMat[dx][dy] = min(distanceMat[dx][dy], dist + 1)
                    if (dx, dy) not in visited:
                        q.append((dx, dy, distanceMat[dx][dy]))
                        visited.add((dx,dy))
        return distanceMat
                
                