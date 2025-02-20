# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def tranposeMatrix(self, matrix):
        rows,cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if col > row:
                    matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]

    
    def reverse(self, arr):
        n = len(arr)

        for i in range(n // 2):
            arr[i], arr[-i - 1] = arr[-i - 1], arr[i]
        


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix

        self.tranposeMatrix(matrix)

        for arr in matrix:
            self.reverse(arr)
        