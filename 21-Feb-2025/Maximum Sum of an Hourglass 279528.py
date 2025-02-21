# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def calculatePrefixSum(self, prefix_sum, grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                top = prefix_sum[r - 1][c] if r > 0 else 0
                left = prefix_sum[r][c - 1] if c > 0 else 0
                diagonal = prefix_sum[r - 1][c - 1] if r > 0 and c > 0 else 0

                prefix_sum[r][c] = top + left + grid[r][c] - diagonal

    def maxSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS,COLS = len(grid), len(grid[0])

        if ROWS < 3 or COLS < 3:
            return 0

        prefix_sum = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        self.calculatePrefixSum(prefix_sum, grid)

        max_sum = 0
        
        for row in range(2, ROWS):
            for col in range(2, COLS):
                top = prefix_sum[row - 3][col] if row > 2 else 0
                left = prefix_sum[row][col - 3] if col > 2 else 0
                diagonal = prefix_sum[row - 3][col - 3] if row > 2 and col > 2 else 0

                exclude = grid[row-1][col] + grid[row - 1][col - 2]
                hourglass_sum = prefix_sum[row][col] - top - left  - exclude + diagonal
                max_sum = max(max_sum, hourglass_sum)


        return max_sum