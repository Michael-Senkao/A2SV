# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (
                    row - 1 > -1 and 
                    col - 1 > -1 and 
                    matrix[row][col] != matrix[row - 1][col - 1]
                    ):
                    return False

        return True