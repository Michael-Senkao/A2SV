# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow(left, right):
            while left <= right:
                mid = left + (right - left)//2
                if matrix[mid][0] > target:
                    right = mid - 1
                elif matrix[mid][-1] < target:
                    left = mid + 1
                else:
                    return findCol(0, len(matrix[0]) - 1, mid)

            return False
        

        def findCol(left, right, row):
            while left <= right:
                mid = left + (right - left)//2
                if matrix[row][mid] > target:
                    right = mid - 1
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    return True
            
            return False

        return findRow(0, len(matrix) - 1)
        