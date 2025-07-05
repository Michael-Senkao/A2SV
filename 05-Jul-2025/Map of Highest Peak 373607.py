# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def isInbound(self, r,c,rows,cols):
        return 0 <= r < rows and 0 <= c < cols

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows,cols = len(isWater), len(isWater[0])
        q = deque()
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    q.append((r,c, 0))
                    isWater[r][c] = 0
                    visited.add((r,c))
        
        while q:
            r,c,height = q.popleft()
            for x,y in directions:
                dx = x + r
                dy = y + c
                if self.isInbound(dx,dy,rows,cols) and (dx,dy) not in visited:
                    isWater[dx][dy] = height + 1
                    q.append((dx,dy, isWater[dx][dy]))
                    visited.add((dx,dy))

        return isWater