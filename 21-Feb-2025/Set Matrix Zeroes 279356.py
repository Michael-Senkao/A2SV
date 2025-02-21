# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        ROWS,COLS = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for row in range(ROWS):
            for col in range(COLS):
                if not matrix[row][col]:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(ROWS):
            for col in range(COLS):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0
        