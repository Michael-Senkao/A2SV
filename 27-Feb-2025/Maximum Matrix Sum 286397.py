# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total = 0
        min_v = float('inf')
        negative_count = 0
        zero_count = 0

        for r in range(n):
            for c in range(n):
                if matrix[r][c] < 0:
                    min_v = min(min_v, -matrix[r][c])
                    total += -matrix[r][c]
                    negative_count += 1
                elif matrix[r][c] > 0:
                    min_v = min(min_v, matrix[r][c])
                    total += matrix[r][c]
                else:
                    zero_count += 1
                    
        if negative_count & 1 and zero_count == 0:
            return total - 2*min_v
        return total
