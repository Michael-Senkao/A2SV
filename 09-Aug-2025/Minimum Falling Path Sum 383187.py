# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        min_path_sum = float('inf')
        curr_row = [0] * n

        for r in range(n - 1):
            next_row = [float('inf')] * n
            for c in range(n):
                curr_row[c] += matrix[r][c]
                next_row[c] = min(next_row[c], curr_row[c])
                if c - 1 >= 0:
                    next_row[c - 1] = min(next_row[c-1], curr_row[c])
                if c + 1 < n:
                    next_row[c + 1] = min(next_row[c+1], curr_row[c])
        
            curr_row = next_row
        for c in range(n):
            min_path_sum = min(min_path_sum, curr_row[c] + matrix[-1][c])
        return min_path_sum