# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows,cols = len(heights), len(heights[0])
        minEffort = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        minEffort[0][0] = 0
        minHeap = []
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        heapq.heappush(minHeap, (0, 0, 0))
        while minHeap:
            effort, r,c = heapq.heappop(minHeap)
            if effort > minEffort[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return effort

            for x,y in directions:
                dx = r + x
                dy = c + y

               
                if 0 <= dx < rows and 0 <= dy < cols:
                    eff = max(effort, abs(heights[r][c] - heights[dx][dy]))
                    if eff < minEffort[dx][dy]:
                        minEffort[dx][dy] = eff
                        heapq.heappush(minHeap, (eff, dx, dy))

        return minEffort[-1][-1]